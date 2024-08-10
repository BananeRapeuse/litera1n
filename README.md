<img src="litera1n.png" alt="logo">

# litera1n

An iOS/iPadOS/tvOS Jailbreak for all A4-A11 devices and iPhone 3GS
 
For libusb errors, refer to this guide: ["Click here"](https://www.smallcab.net/download/programme/xm-07/how-to-install-libusb-driver.pdf)

We are always in developement but you can also jailbreak (jailbreak is ready to use)

# Compatability

- iPhone: iPhone 3GS --> iPhone X
- iPad: iPad 2 --> iPad 7th gen
- iPod Touch: iPod 2nd gen --> iPod 7th gen
- AppleTV: AppleTV 3rd gen --> AppleTV 4k 1st gen

# Exploits
- steaks4uce: iPod Touch 2nd gen
- limera1n: iPod Touch 3rd gen, iPhone 3GS, all A4 devices
- SHAtter: All A4 devices
- checkm8: All A5-A11 devices

## steaks4uce
A heap overflow exists in the iPod touch (2nd generation) (both old and new bootroms) DFU Mode when sending a USB control message of request type 0xA1, request 0x1. This exploit is also referred to as the steaks4uce (steak sauce) exploit.

## limera1n
The limera1n exploit is the bootrom and iBoot exploit used to run unsigned code (and thereby jailbreak) the iPod touch (3rd generation), the iPhone 3GS and all A4-based devices. First used in the limera1n tool by geohot, it can perform a tethered jailbreak on the aforementioned devices. The jailbreak can then be turned into an untethered jailbreak with other exploits, such as the 0x24000 Segment Overflow or the Packet Filter Kernel Exploit.

## SHAtter
SHA-1 Image Segment Overflow or SHAtter was an exploit that allowed unsigned code execution from a flaw in the bootrom. It was never used in a public jailbreak because the limera1n exploit was released first, and more devices were vulnerable to it. SHAtter was patched in the A5 bootrom and therefore, never officially released.

## checkm8
The checkm8 exploit is a BootROM exploit with a CVE ID of CVE-2019-8900 used to run unsigned code on iOS, iPadOS, tvOS, watchOS, bridgeOS, audioOS, and Haywire devices with processors between an A5 and an A11, a S1P and a S3, a S5L8747, and a T2 (and thereby jailbreak it). Jailbreaks based on checkm8 are semi-tethered jailbreaks as the exploit works by taking advantage of vulnerabilities in the USB DFU stack. The main use-after-free is actually unpatched in T8020, T8027 or T8030, but cannot be exploited without a memory leak, of which the one used in checkm8 was made unreachable in T8020 and above.

# Testers
<a href= https://github.com/BananeRapeuse/litera1n/blob/main/testers.md>Testers,</a>
DM me on discord: `frelon111` or reddit: `Ph0qu3_111` to be a tester,
all the testers will be added in the `"thanks to"` part of the [official website](https://bananerapseuse.github.io/litera1n) and on the [credits part of the github](https://github.com/BananeRapeuse/litera1n?tab=readme-ov-file#credits).

# Insrallation process:
# RUN ALL OF THIS USING ADMIN COMMAND PROMPT
## Preinstall
git from https://git-scm.com/

python from https://python.org
### IMPORTANT
cd to the libusb folder after cloning/downloading and copy **libusb.dll** to c:/windows/system32 and c:/windows/syswow64 (only if 64bit) then run **infinstaller.exe** from libusb folder and install the .inf file by right clicking. AFter that copy **Libusb0.sys** to c:/windows/system32/Drivers and c:/windows/syswow64 (only if 64bit)

## Must do
- With A11 devices, you **must** disable passcode before jailbreak ! (Settings: TouchID/FaceID and code ----> disable the code)

- after downloading, cd into the folder and type `python main.py`
type `"0"` to install dependencies

- To jailbreak your device, you **must** use a USB-A to Lightning cable, USB-C to Lightning is not compatible.

### Optional (recomended)
Run command prompt as administrator and cd to litera1n folder, type `cpbin` ~ this allows you to run `litera1n` from anywhere by typing `checkra1n` from cmd

## Steps
For the menu, simply follow installation
for the instant checkra1n cd to the folder and type `cpbin.lnk` (allows you to just type checkra1n from anywhere, boot flags not supported yet)
For a bad GUI version cd to the folder and type `python gui.py`

## Installation:
Download the last [release](https://github.com/bananerapeuse/litera1n/releases) and type this in cmd:

```
cd litera1n
python main.py
```

# Features
- Gui
- Cli
- DFU tool ~ `python dfu.py`
- Menu
- Open source

# TO DO:
- [ ] Make the GUI better

# Troubleshooting:
1. restart your computer at least 3 times after installing drivers
2. re-try the jailbreak

# Errors:
 **1.** File "C:\Users\users\Downloads\ipwndfu-master\ipwndfu-master\ipwndfu", line 47, in <module>
    device = dfu.acquire_device()
  File "C:\Users\users\Downloads\ipwndfu-master\ipwndfu-master\dfu.py", line 16, in acquire_device
    for device in usb.core.find(find_all=True, idVendor=0x5AC, idProduct=0x1227, backend=backend):
  File "C:\Users\users\Downloads\ipwndfu-master\ipwndfu-master\usb\core.py", line 1263, in find
    raise NoBackendError('No backend available')
usb.core.NoBackendError: No backend available
 
 
(also remember to install python with this error)

_with this error you must read the #must do section_

# Credits:
- [axi0mX](https://github.com/axi0mx) for the checkm8 exploit and ipwndfu
- [pod2g](https://github.com/pod2g) for the steaks4uce exploit
- [geohot](https://github.com/geohot) for the limera1n exploit
- [posixninja](https://github.com/posixninja) and [pod2g](https://github.com/pod2g) for the SHAtter exploit
- [Kim Jong Cracks](https://github.com/KJCracks) for checkra1n
- [walac](https://github.com/walac) for pyusb
- [The apple wiki](https://theapplewiki.com/wiki/) for exploits's description
 # Disclaimer
 We are not responsible for your device problemes, or any data loosing/corrupting, ...
