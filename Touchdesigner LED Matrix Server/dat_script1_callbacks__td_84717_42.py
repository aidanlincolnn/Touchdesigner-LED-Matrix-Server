# me - this DAT
# scriptOp - the OP which is cooking

import numpy as np
import socket
from PIL import Image

UDPClientSocket = UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#serverAddressPort   = ("127.0.0.1", 51000)
serverAddressPort   = ("169.254.28.93", 51000)
bufferSize          = 3072

# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
def onSetupParameters(scriptOp):
	return

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return


def onCook(scriptOp):
	img =  op('null1').numpyArray(delayed=True)
	image_without_alpha = img[:,:,:3]
	image = (image_without_alpha  * 255).round().astype(np.uint8)
	bytess = image.tobytes()
	UDPClientSocket.sendto(bytess, serverAddressPort)
	#scriptOp.copyNumpyArray(img)
	return
