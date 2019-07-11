import time
import cv2
import threading
from project import settings

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