from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
import cv2
import os

from app.services.video_camera import VideoCamera

cam =  VideoCamera()
PATH = os.path.dirname(__file__)

def overlay_logo(frame):
    img = cv2.imread(PATH+'/rancher.png')
    # img = cv2.imread("rancher.png", -1)

    # 画像のサイズを取得する
    rows, cols, _ = img.shape
    roi = frame[0:rows, 0:cols]
    img = img[0:rows, 0:cols]

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    
    bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
    fg = cv2.bitwise_and(img,img,mask=mask)

    dst = cv2.add(bg, fg)
    frame[0:rows, 0:cols] = dst

    # return frame
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