import time
import cv2
import threading
from project import settings

import os
from pathlib import Path

from app.services.filter.qr import add_qrcode

import random

import shutil


DEFAULT_CAMERA_URL = settings.CAMERA_URL_STREAM

class VideoCamera(object):
    def __init__(self, mjpg_host=DEFAULT_CAMERA_URL):
        
        self.video = cv2.VideoCapture(mjpg_host)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

    """
    filterにフィルター用の関数を入れることで任意のフィルタを実現することができる。
    """
    def get_filtered_frame(self, filt):
        filtered_frame = filt(self.frame)
        ret, jpeg = cv2.imencode('.jpg', filtered_frame)
        return jpeg.tobytes()
    
    def get_filtered_frame_with_qr(self, message, filter_function=None):
        """[summary]
        
        Arguments:
            filter_function {[type]} -- [description]
            message {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        filtered_frame = self.frame

        if filter_function is not None:
            filtered_frame = filter_function(self.frame)
        qred_frame = add_qrcode(filtered_frame, message)
        
        ret, jpeg = cv2.imencode('.jpg', qred_frame)
        return jpeg.tobytes()
    
    def overlay_logo_without_mask(self, frame):

        img = cv2.imread(os.path.dirname(__file__) + '/images/rancher.png')

        img = cv2.resize(img, (200, 200))

        # 画像のサイズを取得
        img_height, img_width, _ = img.shape[:3]

        img = img[0:img_height, 0:img_width]

        # フレームサイズ取得
        frame_width = len(frame[0])
        frame_height = len(frame)

        start_y = frame_height - img_height

        frame[ start_y:frame_height, 0: img_width] = img

        return frame
    
    def randomize_logo(self):

        rancher_logo = os.path.dirname(__file__)+"/images/rancher.png"

        p = Path(os.path.dirname(__file__)+"/images/")
        files = list(p.glob("*"))
        # print(files)

        img_index = random.randint(0, len(files) - 1)
        print("Decided index:" + str(img_index))
        print(files[img_index])

        shutil.copy2(files[img_index], rancher_logo)