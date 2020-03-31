# Raspberrypi CAN Joystick Controller

This tutorial is to allow any raspberry pi device to act as a HID device specifically a Joystick. This project has been created to control Live For Speed using real vehicle CAN Bus drive-by-wire data.
Reference and credits to [_DATENSCHUTZ_](http://www.isticktoit.net/?p=1383)

### Step 0 - The right kernel

We need to use the 4.4 Kernel
```
$ sudo BRANCH=next rpi-update
```

### Step 1 - Enabling the required modules and drivers

To enable device tree overlay
```
$ echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
$ echo "dwc2" | sudo tee -a /etc/modules
```

Enabling libcomposite driver
```
$ sudo echo "libcomposite" | sudo tee -a /etc/modules
```

### Step 2 - Creating the config script

The configuration is volatile, so it must be run on each startup.
Create a file can_to_joystick in /usr/bin/ using your favourite text editor. Type the following
```
$ sudo touch /usr/bin/can_to_joystick
$ sudo chmod +x /usr/bin/can_to_joystick
```

Then, you need to run this script automatically at startup. Open /etc/rc.local with this command
```
$ sudo nano /etc/rc.local
```

Add the following before the line containing exit 0:
```
/usr/bin/can_to_joystick # libcomposite configuration
```

### Step 3 - Creating the HID gadget
This is the global configuration, so it does not matter how many USB features your Pi will use.
Feel free to change serial number, manufacturer and product name in this block.

```
#!/bin/bash
cd /sys/kernel/config/usb_gadget/
mkdir -p can_to_joystick_gadget
cd can_to_joystick_gadget
echo 0x1d6b > idVendor # Linux Foundation
echo 0x0104 > idProduct # Multifunction Composite Gadget
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB # USB2
mkdir -p strings/0x409
echo "KO31032020" > strings/0x409/serialnumber
echo "Kommu.ai" > strings/0x409/manufacturer
echo "Kommu.ai CAN2JOY USB Device" > strings/0x409/product
mkdir -p configs/c.1/strings/0x409
echo "Config 1: ECM network" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/MaxPower

# Making the gadget as the HID device
mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > functions/hid.usb0/report_desc
ln -s functions/hid.usb0 configs/c.1/


ls /sys/class/udc > UDC
```

### Writing the Python Script to decode the CAN Bus

First of all, for available HID, please use the keycode ("Usage ID (Hex)") from the table 12 on page 53pp of the [_USB HID Usage Tables_](https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf) document. 
