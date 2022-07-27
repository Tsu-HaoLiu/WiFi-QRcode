# WiFi-QRcode
Generate a simple QR code of your Wi-Fi info to share with famliy and friends to quickly join your network without the dreaded "What's the wifi password" question.


## CLI Usage

```python
$ python QRcodeGenerator.py --help
usage: QRcodeGenerator.py [-h] -ssid SSID [-e ENCRYPTION] -p PASSWORD [-hid]
                          [-l LOGO] [-s SIZE]
```
| Argument                                                     | Type                | Description                                                                                                                |
| ------------------------------------------------------------ | ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
  |-ssid, -service_set_id | | Service Set Identifier (SSID) is your Wi-Fi's name.|
  |-e, --encryption | |  This is the type of encryption used on your Wi-Fi (WEP, WPA, WPA2, etc.)|
  |-p, --password  | | The password of your Wi-Fi network.|
  | -hid, --hidden  | |   Append to command if your SSID is hidden.|
  | -l, --logo  | | The file location you want in the middle of your QR code.|
  | -s, --size | |  The size of your logo (default: 150).|



## Screenshots


![Custom QR codes](https://user-images.githubusercontent.com/96331813/180595795-db6986b2-30f9-4931-bf82-74ad91321834.png)


## Types

