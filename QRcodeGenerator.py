import sys
from PIL import Image

import qrcode

def insertLogo():
    # TODO fix file naming convention
    im = Image.open('some_file.png')
    im = im.convert("RGBA")
    logo = Image.open('logo.png')
    basewidth = 150

    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize))

    box = ((im.size[0] - logo.size[0]) // 2,
           (im.size[1] - logo.size[1]) // 2)
    im.paste(logo, box)
    im.save('some_file.png')


def generateQRcode(ssid, t, p, h):
    """Function to get the QR code

    :param ssid: Service Set Identifier, is the name of your network/Wi-Fi
    :param t: The encryption type of your network(WEP, WPA, WPA2...) https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access
    :param p: Password of your network device
    :param h: SSID hidden
    :return: None
    """
    wifi_format = f"WIFI:S:{ssid};T:{t};P:{p};H:{h};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(wifi_format)
    qr.make()

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("some_file.png")  # TODO fix file naming convention


def inputInfo():
    ssid = input("Enter your wifi name:")
    encryption = input("Enter your router encryption type (WEP, WPA, WPA2):")
    password = input("Enter your wifi password:")
    hidden = False
    generateQRcode(ssid, encryption, password, hidden)
    insertLogo() # TODO fix, panel checks


def argParser():
    """Parse commands from CLI """
    import argparse  # only needed if called from CLI

    parse = argparse.ArgumentParser()
    parse.add_argument(
        '-ssid',
        '--service_set_id',
        type=str,
        required=True,
        help=f'Service Set Identifier (SSID) is your Wi-Fi\'s name.'
    )
    parse.add_argument(
        '-e',
        '--encryption_type',
        type=str,
        help=f'This is the type of encryption used on your Wi-Fi (WEP, WPA, WPA2, etc.)'
    )
    parse.add_argument(
        '-p',
        '--password',
        type=str,
        required=True,
        help='The password of your Wi-Fi network.'
    )
    parse.add_argument(
        '-hid',
        '--hidden',
        default=False,
        action='store_true',
        help='Append to command if your SSID is hidden.'
    )
    parse.add_argument(
        '-l',
        '--logo',
        type=str,
        help='The file location you want in the middle of your QR code.'
    )

    args = parse.parse_args()
    generateQRcode(*vars(args).values())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        argParser()
    else:
        inputInfo()
