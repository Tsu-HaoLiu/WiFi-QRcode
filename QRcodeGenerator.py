import sys
import qrcode

def generateQRcode(SSID, T, P, H):
    """Function to get the QR code

    :param SSID: Service Set Identifier, is the name of your network/Wi-Fi
    :param T: The encryption type of your network(WEP, WPA, WPA2...) https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access
    :param P: Password of your network device
    :param H: SSID hidden
    :return: None
    """
    wifi_format = f"WIFI:S:{SSID};T:{T};P:{P};H:{bool(H)};;"
    img = qrcode.make(wifi_format)
    # qrcode.image.pil.PilImage
    img.save("some_file.png")

def inputInfo():
    ssid = input("Enter your wifi name:")
    encryption = input("Enter your router encryption type (WEP, WPA, WPA2):")
    password = input("Enter your wifi password:")
    hidden = False
    generateQRcode(ssid, encryption, password, hidden)


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
