import time

from lib.aq import AQ

print("Air Qualitiy Measurement Tool v1.0")
print("==================================")
print(" ")

aq = AQ()

try:
    while True:
        coValue = aq.get_eco2()
        tmpValue = aq.get_temp()
        print("CO2-Wert ist " + str(coValue) + " Temp. ist " + str(tmpValue))
        time.sleep(15)

except KeyboardInterrupt:
    print("Program interrupted by user!")
