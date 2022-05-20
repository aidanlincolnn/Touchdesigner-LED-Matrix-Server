from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
import socket

options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.chain_length = 1
options.gpio_slowdown = 3
options.pwm_bits =11
options.show_refresh_rate =True
options.brightness = 95
options.hardware_mapping="adafruit-hat-pwm"
options.limit_refresh_rate_hz=100
matrix = RGBMatrix(options = options)
canvas = matrix.CreateFrameCanvas()

print("Matrix Initialized")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localIP = s.getsockname()[0]
localPort   = 51000
bufferSize  = 3072 #for 1 led screens 32x32x3

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
UDPServerSocket.bind((localIP, localPort))

print("RPi IP Address: ",localIP)
print("UDP Server Listening For Content On Port: ",localPort)

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    im = Image.frombytes("RGB", (options.cols, options.rows), message, "raw")
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
    canvas.SetImage(im)
    matrix.SwapOnVSync(canvas)
