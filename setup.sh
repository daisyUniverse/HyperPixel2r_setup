#!/bin/bash

echo "This is gonna do a bunch of bullshit and hopefully it will make this display work good"

echo "[ UPDATE PACKAGELIST ]"
sudo apt update -y

echo "[ INSTALL GIT AND PYTHON3-PIP ]"
sudo apt install git python3-pip -y

echo "[ INSTALL SDL & OTHER PYGAME PREQS ]"
sudo apt install libsdl2-dev libsdl2-mixer-dev libsdl2-gfx-dev libsdl2-image-dev libsdl2-net-dev libsdl2-ttf-dev -y

echo "[ INSTALL UPDATED PYGAME ( THIS WILL TAKE FOREVER ON A PI ZERO! ) ]"
sudo python3 -m pip install pygame --upgrade

echo "[ UPGRADE PACKAGES ( THIS WILL TAKE FOREVER ON A PI ZERO! ) ]"
sudo apt upgrade -y

echo "[ ENABLE I2C FOR TOUCHSCREEN SUPPORT ]"
sudo raspi-config nonint do_i2c 1

echo "[ DOWNLOAD & INSTALL DISPLAY DRIVERS ]"
git clone https://github.com/pimoroni/hyperpixel2r
sudo bash hyperpixel2r/install.sh

echo "[ DOWNLOAD & INSTALL HYPERPIXEL PYTHON MODULE ]"
git clone https://github.com/pimoroni/hyperpixel2r-python
sudo bash hyperpixel2r-python/install.sh

echo "[ TRYING TO UNFUCK THE I2C ]"
sudo ln -sf /dev/i2c-* /dev/i2c-11

echo "[ WILL REBOOT NOW :3 BYE BYE ]"
sudo reboot
