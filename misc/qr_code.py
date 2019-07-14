import qrcode

file_name = "qr_code.png"

qr_string = "QRコードをPythonで出力してみるぞい"

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L
)

qr.add_data(qr_string)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(file_name)