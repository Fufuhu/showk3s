from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
import cv2
import os

from app.services.video_camera import VideoCamera
from app.services.filter.qr import add_qrcode

cam =  VideoCamera()
PATH = os.path.dirname(__file__)

def overlay_logo(frame):
    # 参考URL
    # https://code-graffiti.com/blending-images-with-opencv-in-python/
    img = cv2.imread(PATH+'/rancher.png')

    # 画像のサイズを取得する
    # img_widthは画像の横幅, img_heightは画像の縦幅
    img_height, img_width, _ = img.shape[:3]
    # print(img_width)
    # img_height, img_width = img.shape[:2]
    img = img[0:img_height, 0:img_width]

    # フレームサイズの取得
    frame_width = len(frame[0])
    frame_height = len(frame)
    # フレームと画像サイズの差を取得
    delta_width = frame_width - img_width
    # print("delta_width:" + str(delta_width))
    # start_yは画像の配置先となるフレーム左上端のy座標
    start_y = frame_height - img_height

    # end_yは画像の配置先となるフレーム右下端のy座標
    end_y = frame_height

    # 重ね合わせ用にフレームから切り取る範囲を確認
    roi = frame[ start_y:end_y, 0:img_width ]

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    
    bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
    fg = cv2.bitwise_and(img,img,mask=mask)


    dst = cv2.add(bg, fg)
    frame[start_y:frame_height, 0:img_width] = dst

    return frame


class LogoStreamView(View):
    def get_stream(self):
        # https://stackoverflow.com/questions/49680152/opencv-live-stream-from-camera-in-django-webpage

        while True:
            frame = cam.get_filtered_frame(overlay_logo)
            yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    def get(self, request):
        return StreamingHttpResponse(self.get_stream(), content_type='multipart/x-mixed-replace;boundary=frame')