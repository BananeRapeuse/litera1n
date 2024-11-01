<img src="litera1n_banner.jpeg" alt="logo">

# litera1n

An iOS/iPadOS/tvOS Jailbreak for all A5-A11 devices using the checkm8 exploit.
 
For libusb errors, refer to this guide: ["Click here"](https://www.smallcab.net/download/programme/xm-07/how-to-install-libusb-driver.pdf)

# Disclaimer
 We are not responsible for your device problemes, or any data loosing/corrupting, boot loop, ...


# Compatability

- iPhone: iPhone 4s --> iPhone X
- iPad: iPad 2 --> iPad 7th gen
- iPod Touch: iPod Touch 5th gen --> iPod Touch 7th gen
- AppleTV: AppleTV 3rd gen --> AppleTV 4k 1st gen

# checkm8
- permanent unpatchable bootrom exploit for hundreds of millions of iOS devices

- meant for researchers, this is not a jailbreak with Cydia yet

- allows dumping SecureROM, decrypting keybags for iOS firmware, and demoting device for JTAG

- current SoC support: s5l8947x, s5l8950x, s5l8955x, s5l8960x, t8002, t8004, t8010, t8011, t8015

- future SoC support: s5l8940x, s5l8942x, s5l8945x, s5l8747x, t7000, t7001, s7002, s8000, s8001, s8003, t8012

- full jailbreak with Cydia on latest iOS version is possible, but requires additional work

# Testers
<a href= https://github.com/BananeRapeuse/litera1n/blob/main/testers.md>Testers</a>, 
DM me on discord: `frelon111` or reddit: `Ph0qu3_111` to be a tester,
all the testers will be added in the `"thanks to"` part of the [official website](https://bananerapseuse.github.io/litera1n) and on the [credits part of the github](https://github.com/BananeRapeuse/litera1n?tab=readme-ov-file#credits).

# Features
- GUI
- CLI
- DFU tool ~ `python dfu.py`
- Menu
- Open source

# TO DO:
- ~~[x] Make the GUI better~~
- [ ] Make a working DFU Tool

# Installation and jailbreaking process:
### RUN ALL OF THIS USING ADMIN COMMAND PROMPT
## Preinstall
git from https://git-scm.com/

python from https://python.org

## Installation:
Download the last [release](https://github.com/bananerapeuse/litera1n/releases) and type this in cmd:

```
cd litera1n
python main.py
0
```
you must type 0 before anythings to install dependencies and drivers
### Optional (recomended)
Run command prompt as administrator and cd to litera1n folder, type `cpbin` ~ this allows you to run `litera1n` from anywhere by typing `checkra1n` from cmd

## Jailbreak
in `main.py`, type `1` for a command line jailbreak or `2` for a bad GUI jailbreak

### Must do
- With A11 devices, you **must** disable passcode before jailbreak ! (Settings: TouchID/FaceID and code ----> disable the code)

- To jailbreak your device, you **must** use a USB-A to Lightning cable, USB-C to Lightning is not compatible.

# Troubleshooting:
1. restart your computer at least 3 times after installing drivers
2. re-try the jailbreak
3. With A9 devices, if you get stuck at the "Checkra1n boot" type `Ctrl+C` in the cmd or unplug and replug the phone

# Errors:
 **1.** 
 File "C:\Users\users\Downloads\ipwndfu-master\ipwndfu-master\ipwndfu", line 47, in <module>
    device = dfu.acquire_device()
  File "C:\Users\users\Downloads\ipwndfu-master\ipwndfu-master\dfu.py", line 16, in acquire_device
    for device in usb.core.find(find_all=True, idVendor=0x5AC, idProduct=0x1227, backend=backend):
  File "C:\Users\users\Downloads\ipwndfu-master\ipwndfu-master\usb\core.py", line 1263, in find
    raise NoBackendError('No backend available')
usb.core.NoBackendError: No backend available
 
 
(also remember to install python with this error)

_with this error you must read the #must do section_ **(it is possible you encounter problemes with all the dependencies installed, for moment we don't have find how to fix this issue, please re-try on a other computer (the only way to "fix" the issue))**

# Credits:
- [axi0mX](https://github.com/axi0mx) for the checkm8 exploit, ipwndfu and the checkm8 description
- [Checkra1n](https://github.com/checkra1n) for checkra1n
- [walac](https://github.com/walac) for pyusb
- [Starmax](https://www.reddit.com/user/Starmax02/) :tester
