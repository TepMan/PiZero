import time
import datetime
from mqtt_comm import send_data
from Measurement import Measurement
from lib.aq import AQ

# print("Air Qualitiy Measurement Tool v1.0")
# print("==================================")
# print(" ")

aq = AQ()

try:
    while True:
        coValue = aq.get_eco2()
        tmpValue = aq.get_temp()

        measurement = Measurement(tmpValue, coValue)

        #print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - CO2-Wert: " + str(coValue) + " / Temp.: " + str(tmpValue))

        send_data(measurement)
        time.sleep(30)

except KeyboardInterrupt:
    print("Program interrupted by user!")
