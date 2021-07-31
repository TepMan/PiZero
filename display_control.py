import time
import sys

sys.path.append('./lib')
import SPI
import SSD1305

from PIL import Image
from PIL import ImageDraw

# Raspberry Pi pin configuration:
RST = None  # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 24
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display with hardware SPI:
display = SSD1305.SSD1305_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Initialize library.
display.begin()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = display.width
height = display.height


def display_blocks(block_count: int):
    image = Image.new('1', (width, height))
    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    if block_count > 0:
        draw.rectangle((0, 0, 11, height), outline=0, fill=1)
    if block_count > 1:
        draw.rectangle((13, 0, 24, height), outline=0, fill=1)
    if block_count > 2:
        draw.rectangle((26, 0, 37, height), outline=0, fill=1)
    if block_count > 3:
        draw.rectangle((39, 0, 50, height), outline=0, fill=1)
    if block_count > 4:
        draw.rectangle((52, 0, 63, height), outline=0, fill=1)
    if block_count > 5:
        draw.rectangle((65, 0, 76, height), outline=0, fill=1)
    if block_count > 6:
        draw.rectangle((78, 0, 89, height), outline=0, fill=1)

    # Display image.
    display.image(image)
    display.display()
    time.sleep(.1)


def display_clear():
    display.clear()
    display.display()
