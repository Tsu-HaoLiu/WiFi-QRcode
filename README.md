# WiFi-QRcode
Generate a simple QR code of your Wi-Fi info to share with famliy and friends to quickly join your network without the dreaded "What's the wifi password" question.


## Usage

```python
$ python QRcodeGenerator.py --help
usage: QRcodeGenerator.py [-h] -ssid SSID [-e ENCRYPTION] -p PASSWORD [-hid]
                          [-l LOGO] [-s SIZE]
```
| Argument                                                     | Type                | Description                                                                                                                |
| ------------------------------------------------------------ | ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
  |-ssid SSID, -service_set_id SSID | | Service Set Identifier (SSID) is your Wi-Fi's name.|
  |-e ENCRYPTION, --encryption ENCRYPTION | |  This is the type of encryption used on your Wi-Fi (WEP, WPA, WPA2, etc.)|
  |-p PASSWORD, --password PASSWORD  | | The password of your Wi-Fi network.|
  | -hid, --hidden  | |   Append to command if your SSID is hidden.|
  | -l LOGO, --logo LOGO  | | The file location you want in the middle of your QR code.|
  | -s SIZE, --size SIZE | |  The size of your logo (default: 150).|



## Screenshots


![Custom QR codes](https://user-images.githubusercontent.com/96331813/180595795-db6986b2-30f9-4931-bf82-74ad91321834.png)


## Types

