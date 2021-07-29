import bme
import time
from display_control import display_clear, display_status

# display_clear()
# control = True
#
# while control:
#     for i in range(100):
#         display_status(i)
#         time.sleep(0.5)
#
#     display_clear()
#
#     char = input("Zum Beenden x drücken: ")
#
#     if char == 'x' or char == 'X':
#         control = False

print("BME Test:")

bme.init("/dev/i2c-1", 119)
bme.set_timezone("TZ=Europe/London")   # other options include "TZ=Asia/Singapore" or "TZ=US/Denver"
bme.forced_mode()
print(" year mon day h min sec  Tmp degC            Prs Pa         Hum %rH           GsR Ohm   Status")
data = bme.get_data()
print(data)
print("Installation succeeded")