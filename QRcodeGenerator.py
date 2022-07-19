import sys
from PIL import Image

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles import moduledrawers as md

filename = ""

def insertLogo(img, logo_file: str, logo_size: int = 150):

    img = img.convert("RGBA")
    logo = Image.open(logo_file)
    basewidth = logo_size

    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize))

    box = ((img.size[0] - logo.size[0]) // 2,
           (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, box)
    img.save(filename)


def generateQRcode(ssid, t, p, h):
    """Function to get the QR code

    :param ssid: Service Set Identifier, is the name of your network/Wi-Fi
    :param t: The encryption type of your network(WEP, WPA, WPA2...) https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access
    :param p: Password of your network device
    :param h: SSID hidden
    :return: None
    """
    # qrcode.image.pil.PilImage
    wifi_format = f"WIFI:S:{ssid};T:{t};P:{p};H:{h};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(wifi_format)
    qr.make()

    img = qr.make_image(
        fill_color="black",
        back_color="white",
        image_factory=StyledPilImage,
        module_drawer=md.RoundedModuleDrawer(),
        eye_drawer=md.RoundedModuleDrawer()
    )

    img.save(filename)
    return img


def imageCombo(userinput):
    global filename
    filename = f"{userinput['ssid']}_QRCode.png"

    qrimg = generateQRcode(userinput['ssid'], userinput['encryption'],
                           userinput['password'], userinput['hidden'])

    if logo := userinput.get('logo', False):
        size = userinput.get('size', 150)
        insertLogo(qrimg, logo, int(size))


def inputInfo():
    user_info = dict()

    user_info['ssid'] = input("Enter your wifi name:")
    user_info['encryption'] = input("Enter your router encryption type (WEP, WPA, WPA2):")
    user_info['password'] = input("Enter your wifi password:")
    user_info['hidden'] = bool(input("Is your SSID hidden? (True, False)"))
    if logo := input("Location of your logo (optional):"):
        user_info['logo'] = logo
        user_info['size'] = input("Size of your logo (default: 150):")

    imageCombo(user_info)


def argParser():
    """Parse commands from CLI """
    import argparse  # only needed if called from CLI

    parse = argparse.ArgumentParser()
    parse.add_argument(
        '-ssid',
        '-service_set_id',
        type=str,
        required=True,
        help=f'Service Set Identifier (SSID) is your Wi-Fi\'s name.'
    )
    parse.add_argument(
        '-e',
        '--encryption',
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
    parse.add_argument(
        '-s',
        '--size',
        type=int,
        default=150,
        help='The size of your logo (default: 150).'
    )

    args = parse.parse_args()
    imageCombo(vars(args))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        argParser()
    else:
        inputInfo()
