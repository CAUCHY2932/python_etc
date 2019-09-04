import qrcode
import zxing

"""
需要库
pip install pillow
pip install qrcode
pip install zxing
"""


def gen_pic1():
    img = qrcode.make('hello, world')

    img.save('test.png')


def gen_pic2():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('hello, qrcode')
    qr.make(fit=True)
    img = qr.make_image()
    img.save('123.png')


def parse_pic():
    pic_path = '123.png'

    reader = zxing.BarCodeReader()
    barcode = reader.decode(pic_path)
    print(barcode.parsed)
