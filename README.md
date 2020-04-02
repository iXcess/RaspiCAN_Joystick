# Raspi CAN Wireless Joystick Controller

In this project, we allow real vehicle CAN messages decoded on a Raspberry Pi to control and communicate with Live For Speed (LFS) running on a Windows machine. The method used in this section is a non-direct method and involves the use of an xbox360 emulator. Communication between the Raspberry Pi and Windows machine is wireless using UDP packets.

The pub/sub from ROS is used for message communication. The raspberry pi is first loaded with Ubuntu 16.04 (LXDE) and ROS Kinetic installed and can be found [_here_](https://downloads.ubiquityrobotics.com/pi.html). ROS is used to make the development simple.

## Pre-requisite
On the window's machine, download and install all the required drivers and emulators:

1. [_xBox_360_Controller_Emulator_](https://www.x360ce.com/)
2. [_vJoy_Device_Driver_](http://vjoystick.sourceforge.net/joomla256.02/index.php/download-a-install/download)
3. [_Python3_](https://www.python.org/downloads/)

## Concept

Real vehicle hardware for example electronic power steering, drive-by-wire brake and accelerator ECU will send CAN data into the engine control module. In the simulator's case, we have designed our own electronic power steering, brake and accelerator to send CAN Bus data straight to the CAN Bus which is also connected to the Raspberry Pi 3B+.

The CAN data is then decoded and the appropriate actuator commands are sent wirelessly to the windows machine. A python script running on the windows machine will decode the UDP message and the actuator commands are mapped into the joystick input. 

A rich amount of data from LFS can be sent back to the Raspberry Pi ECU using same method, data such as vehicle speed, engine rpm, throttle position etc are sent as feedback back to the vehicle hardware.

![High Level Explanation](/images/high_level.jpg)
