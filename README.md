# Environmental-measurement-RaspberryPiPico
Measure carbon dioxide concentration, temperature, and humidity in the air using a Raspberry Pi Pico.

## Installation
## Writing the farmware
Write the MicroPython firmware to the Raspberry Pi Pico.

1. Connect to the PC while pressing the BOOTSEL button on the Raspberry Pi Pico and open RPI-RP2(H:) drive.
1. Open the INDEX.HTM file in the drive to the following page.  
    https://www.raspberrypi.com/documentation/microcontrollers/?version=E0C9125B0D9B
1. Open MicroPython and download the following file.  
    https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2
1. Copy the downloaded file into the drive and the firmware will be written.  
## Prepare the editor
Install Thonny to create and write program to the Raspberry Pi Pico.

1. Open the following page and install the appropriate one for your OS.  
    https://thonny.org/
1. If "MicroPython(Raspberry Pi Pico)・ComX" in the bottom right hand corner is displayed, it is OK.  
1. Run the following code in the editor, and the LED on the board will blick.  
```python
from machine import Pin
import utime

led = Pin(25, Pin.OUT) # = Pin("LED", Pin.OUT)
while True:
    led.value(1)
    utime.sleep(.5)
    led.value(0)
    utime.sleep(.5)
```
(If the editor does not recognise the Raspberry Pi Pico, re-write the firmware.)  
