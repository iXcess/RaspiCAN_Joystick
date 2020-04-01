import socket
import struct

# Create UDP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to LFS.
sock.bind(('127.0.0.1', 30000))

while True:
    # Receive data.
    data = sock.recv(256)

    if not data:
        break # Lost connection
  
    # Unpack the data.
    outgauge_pack = struct.unpack('I3sxH2B7f2I3f15sx15sx', data)
    time = outgauge_pack[0]
    car = outgauge_pack[1]
    flags = outgauge_pack[2]
    gear = outgauge_pack[3]
    speed = outgauge_pack[5]
    rpm = outgauge_pack[6]
    turbo = outgauge_pack[7]
    engtemp = outgauge_pack[8]
    fuel = outgauge_pack[9]
    oilpressure = outgauge_pack[10]
    oiltemp = outgauge_pack[11]
    dashlights = outgauge_pack[12]
    showlights = outgauge_pack[13]
    throttle = outgauge_pack[14]
    brake = outgauge_pack[15]
    clutch = outgauge_pack[16]
    display1 = outgauge_pack[17]
    display2 = outgauge_pack[18]

    print(speed*3.7)

# Release the socket.
sock.close()
