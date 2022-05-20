# Touchdesigner-LED-Matrix-Server
This repository contains a touchdesigner patch with a custom UDP server which sends real time visuals to a raspberry pi UDP client connected to an LED Matrix Pannel using Hzellers rgb-rpi-led library https://github.com/hzeller/rpi-rgb-led-matrix

Run the UDP client on the raspberry pi - sudo python3 matrixServer.py (will have to install PILLOW and unblock UDP port 51000 if using firewall)

Copy the IP address into the script op in touchdesigner

Everything is set up for a 32x32 led matrix pannel but it can push far more pixels, able to run 32x448 screen at 60 fps on an M1 mac
