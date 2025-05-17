The [HyperPixel2r](https://www.elektor.com/hyperpixel-2-1-round-hi-res-display-for-raspberry-pi) from Pimoroni is a round 2.1” IPS capacitive touchscreen with high-speed DPI interface. Like its square and rectangular HyperPixel 4 brothers, the 2r is intended for Raspberry Pi. Actually, the size is optimized for the Raspberry Pi Zero and Zero 2W but, as it has the standard 40-pin HAT connector, it can be plugged on any Raspberry Pi equipped with such a connector as long as you are careful about the mechanical side of things.

It has 18-bit color depth (meaning 262,144 colors) and supports up to 60 frames per second (FPS). The viewing area has a 2.1” or 53.3 mm diameter and a viewing angle of 175°. Its full diameter is 72 mm with a height of 11 mm. With a Pi Zero attached with short stand-offs, the total height (or depth, whatever you prefer) is 17 mm.

As the display uses almost every pin of the HAT connector, you cannot add other extension boards. However, the display does provide an alternate I2C port for connecting things to.

In this project, I'm using the Hyperpixel with the **Raspi Zero W**.

The drivers only work with **Raspberry Pi OS Buster** (last time I checked). So burn an SD card with the [legacy OS](https://downloads.raspberrypi.com/raspios_lite_armhf/images/raspios_lite_armhf-2021-05-28/). (supposedly support for Bullseye is being worked on).
It's easiers to work with [SSH](https://www.raspberrypi.com/documentation/computers/remote-access.html#introduction-to-remote-access). So set-up everything correctly during set-up.

## basic set-up

this is highly experimental and run this at your own risk, but eventually when this is ironed out you should be able to run this setup by using this command
```
curl "https://raw.githubusercontent.com/daisyUniverse/HyperPixel2r_setup/refs/heads/main/setup.sh" | sudo bash
```


