# me - this DAT
# scriptOp - the OP which is cooking

import numpy as np
import socket

import sys
mypath = "/usr/local/lib/python3.7/site-packages"
if mypath not in sys.path:
	sys.path = [mypath] + sys.path
from PIL import Image

UDPClientSocket = UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serverAddressPort = ("169.254.206.16",51000)
bufferSize = 3072

def onCook(scriptOp):
	img = op('null1').numpyArray(delayed=True)
	image_without_alpha = img[:,:,:3]
	image = (image_without_alpha  * 255).round().astype(np.uint8)
	bytess = image.tobytes()
	UDPClientSocket.sendto(bytess, serverAddressPort)
	return

