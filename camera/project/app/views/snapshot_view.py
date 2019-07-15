from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.services.video_camera import VideoCamera
from uuid import uuid4

from project.settings import CAMERA_IMAGE_DIRECTORY

from app.views.logo_stream_view import overlay_logo
from app.services.filter.qr import add_qrcode

cam = VideoCamera()

class SnapView(View):

    def get(self, request):
        # image = cam.get_frame()
        # image = overlay_logo(image)
        # image = cam.get_filtered_frame(overlay_logo)
        image = cam.get_filtered_frame_with_qr(
            message="hogehogehoge",
            filter_function=overlay_logo
        )
        save_directory = CAMERA_IMAGE_DIRECTORY

        filename = str(uuid4()) + '.jpg'
        print(filename)
        full_path = save_directory + filename

        # ファイルの書き込み???
        with open(full_path, "wb") as fout:
            fout.write(image)

        return HttpResponse(image, content_type="image/jpeg")