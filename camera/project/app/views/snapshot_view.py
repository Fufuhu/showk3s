from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.services.video_camera import VideoCamera
from uuid import uuid4

from project.settings import CAMERA_IMAGE_DIRECTORY

from app.views.logo_stream_view import overlay_logo
from app.services.filter.qr import add_qrcode

from app.services.aws.s3 import upload_file

cam = VideoCamera()

BUCKET_NAME='showk3s'

class SnapView(View):

    def get(self, request):
        filename = str(uuid4()) + '.jpg'
        save_directory = CAMERA_IMAGE_DIRECTORY
        full_path = save_directory + filename

        # ファイル名とバケット名からS3のパスを設定
        file_path_s3 = 'https://' + BUCKET_NAME + '.s3-ap-northeast-1.amazonaws.com/' + filename

        image = cam.get_filtered_frame_with_qr(
            message=file_path_s3,
            #filter_function=overlay_logo
            filter_function=cam.overlay_logo_without_mask
        )


        # ファイルの書き込み???
        with open(full_path, "wb") as fout:
            fout.write(image)

        upload_file(
            bucket_name=BUCKET_NAME,
            filepath=full_path
        )

        return HttpResponse(image, content_type="image/jpeg")