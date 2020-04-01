
from vjoy import vj, setJoy
import numpy as np
import time

print("vj opening", flush=True)
vj.open()

time.sleep(1)


print("sending axes", flush=True)

# valueX, valueY between -1.0 and 1.0
# scale between 0 and 16000
scale = 10000.0
i = 0;
while True:
	i = i + 1
	xPos = np.sin(2.0*np.pi*i/1000)
	yPos = np.sin(2.0*np.pi*i/100)
	zPos = np.sin(2.0*np.pi*i/10000)
	setJoy(xPos, yPos, zPos, 0x00000001, scale)
	time.sleep(0.01)
	if (i == 10000):
		i = 0

print("vj closing", flush=True)
vj.close()