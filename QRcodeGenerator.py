import sys
import re
from collections import defaultdict

from PIL import Image

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles import moduledrawers as md
from qrcode.image.styles.colormasks import RadialGradiantColorMask


def insert_logo(img: Image,
                filename: str,
                logo_file: str,
                logo_size: int = 150):

    # convert the image to RGBA
    img = img.convert("RGBA")
    logo = Image.open(logo_file)
    base_width = logo_size

    # calculate the percentage with the base width and resize the logo
    # to not completely covert the QR code making it unreadable
    wpercent = (base_width / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((base_width, hsize))

    # Calculating logo to image size and paste the logo to the QR code
    box = ((img.size[0] - logo.size[0]) // 2,
           (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, box)
    img.save(filename)


def generate_qr_code(userinput: dict, filename: str):
    """Function to generate the QR code and save the image

    :param ssid: Service Set Identifier, is the name of your network/Wi-Fi
    :param encryption_type: The encryption type of your network(WEP, WPA, WPA2...) https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access
    :param password: Password of your network device
    :param hidden_ssid: SSID hidden
    :param color: Color of the QR code back_color, center_color, edge_color
    :return: PilImage
    """

    ssid = userinput['ssid']
    encryption_type = userinput['encryption'] or ''
    password = userinput['password']
    hidden_ssid = userinput['hidden'] or False
    color = userinput['color'] or ((255, 255, 255), (255, 255, 255), (255, 255, 255))

    # qrcode.image.pil.PilImage
    wifi_format = f"WIFI:S:{ssid};T:{encryption_type};P:{password};H:{hidden_ssid};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # add the data to the QR code
    qr.add_data(wifi_format)
    qr.make()

    # make the QR code image
    img = qr.make_image(
        fill_color="black",
        back_color="white",
        image_factory=StyledPilImage,
        module_drawer=md.RoundedModuleDrawer(),
        eye_drawer=md.RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask(back_color=color[0],
                                           center_color=color[1],
                                           edge_color=color[2])
    )
    
    # save the file
    img.save(filename)
    return img


def main(userinput):
    filename = f"{userinput['ssid']}_QRCode.png"

    # color string to tuple
    if userinput.get('color'):
        colors = list()
        colors_input = re.sub(r'\((.*)\)', r'\1', userinput['color']).split('), (')
        for num in colors_input:
            colors.append(tuple(map(lambda x: int(x), num.split(','))))
        userinput['color'] = colors

    qr_img = generate_qr_code(userinput, filename)

    # if a logo file is available then insert the logo to the QR code
    if logo := userinput.get('logo', False):
        size = userinput.get('size', 150)
        insert_logo(qr_img, filename, logo, int(size))


def input_info():
    """Provide a way to input values instead of CLI"""
    user_info = defaultdict()

    user_info['ssid'] = input("Enter your wifi name:")
    if not user_info.get('ssid', False):
        raise ValueError('Missing wifi name')

    user_info['encryption'] = input("Enter your router encryption type (WEP, WPA, WPA2):")

    user_info['password'] = input("Enter your wifi password:")
    if not user_info.get('password', False):
        raise ValueError('Missing wifi password')

    user_info['hidden'] = bool(input("Is your SSID hidden? (True, False)") or False)
    if logo := input("Location of your logo (optional):"):
        user_info['logo'] = logo
        user_info['size'] = int(input("Size you want your logo (default: 150):") or 150)

    user_info['color'] = input("RGB color of the QR code center, edge, background (default: black & white)") or \
        "(255, 255, 255), (255, 255, 255), (255, 255, 255)"

    main(user_info)


def arg_parser():
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
    parse.add_argument(
        '-c',
        '--color',
        type=str,
        help='RGB color of your QR code separated by comma'
             'center, edge, background\n'
             'e.g: -c "(255, 255, 255), (204, 153, 255), (0, 0, 230)"'
    )

    args = parse.parse_args()
    main(vars(args))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_parser()
    else:
        input_info()
