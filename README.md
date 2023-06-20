# WiFi-QRcode
Generate a simple QR code of your Wi-Fi info to share with famliy and friends to quickly join your network without the dreaded "What's the wifi password" question.


## Features

- Custom center logo
- Custom logo size
- Customizable inner, outer and background colors

## Normal Usage
```python
$ python qr_logo_generator.py
```


## CLI Usage

```python
$ python qr_logo_generator.py --help
usage: qr_logo_generator.py [-h] -ssid SSID [-e ENCRYPTION] -p PASSWORD [-hid]
                          [-l LOGO] [-s SIZE]
```
| Argument                                                     | Type                | Description                                                                                                                |
| ------------------------------------------------------------ | ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
  |-ssid, -service_set_id | Required | Service Set Identifier (SSID) is your Wi-Fi's name.|
  |-e, --encryption | |  This is the type of encryption used on your Wi-Fi (WEP, WPA, WPA2, etc.)|
  |-p, --password  | Required | The password of your Wi-Fi network.|
  | -hid, --hidden  | |   Append to command if your SSID is hidden.|
  | -l, --logo  | Optional | The file location you want in the middle of your QR code.|
  | -s, --size | Optional |  The size of your logo (default: 150).|
  | -c, --color | Optional |  Add RGB based colors separated by comma center, edge, background - "(255, 255, 255), (204, 153, 255), (0, 0, 230)" |




## Screenshots

![Custom QR codes](https://github.com/Tsu-HaoLiu/WiFi-QRcode/assets/96331813/cb1ac66e-b971-4cd5-9b17-f54e8aef7797)
