import time
from mqtt_comm import send_data

print("Air Qualitiy Measurement Tool v1.0")
print("==================================")
print(" ")

try:
    while True:
        time.sleep(30)

except KeyboardInterrupt:
    print("Program interrupted by user!")
