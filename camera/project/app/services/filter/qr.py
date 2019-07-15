import qrcode
import cv2
import os
from uuid import uuid4

def add_qrcode(frame, message):
    """フレーム(frame)に対してメッセージ(message)の含まれた
    QRコードをオーバーレイします。
    
    Arguments:
        frame {?} -- OpenCVのframe
        message {str} -- QRコードに含める画像
    Returns:
        [?] -- QRコードがオーバーレイされた画像
    """

    # QRコードの生成
    file_name = message.split('/')[-1]
    file_name = file_name.replace('.jpg','.png')
    # file_name = message + ".png"

    if not os.path.isfile(file_name):
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_L
        )

        qr.add_data(message)
        qr.make(fit=True)

        qr_code = qr.make_image(fill_color="black", back_color="white")
        qr_code.save(file_name)

    # QRコードのオーバーレイ
    ## QRコード画像の読込
    img = cv2.imread(file_name)
    img = cv2.resize(img, (200, 200))

    ## 画像のサイズを取得する
    img_height, img_width, _ = img.shape[:3]

    img = img[0:img_height, 0:img_width]

    ## フレームのサイズ取得
    frame_width = len(frame[0])
    frame_height = len(frame)

    ## 画像の配置位置を決める
    start_x = frame_width - img_width
    start_y = frame_height - img_height
    frame[ start_y:frame_height, start_x:frame_width ] = img

    return frame




