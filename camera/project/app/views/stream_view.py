from django.views.generic import View
from django.http import StreamingHttpResponse

from app.services.video_camera import VideoCamera

cam = VideoCamera()

class StreamView(View):
    def get_stream(self):
        # https://stackoverflow.com/questions/49680152/opencv-live-stream-from-camera-in-django-webpage

        while True:
            frame = cam.get_frame()
            yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    def get(self, request):
        return StreamingHttpResponse(self.get_stream(),\
             content_type='multipart/x-mixed-replace;boundary=frame')