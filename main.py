from bme68x import BME68X
import bme68xConstants as cnst
import bsecConstants as bsec
import time, sys
from display_control import display_clear, display_status

bme = BME68X(cnst.BME68X_I2C_ADDR_HIGH, bsec.BSEC_ENABLE)

display_clear()

print("Air Qualitiy Measurement Tool v1.0")
print("==================================")
print(" ")

try:
    while True:
        data = bme.get_bsec_data()
        iaq = data["iaq"]
        temp = data["temperature"]
        hum = data["humidity"]
        print("Temperature : " + '{:.1f}°C'.format(temp))
        print("Humidity    : " + '{:.1f}%'.format(hum))
        print("Air Quality : " + str(iaq))

        if 0 < iaq < 20:
            display_status(100)
            print("Air quality is excellent!")
        if 21 < iaq < 50:
            display_status(90)
            print("Air quality is excellent!")
        if 51 < iaq < 100:
            display_status(80)
            print("Air quality is good.")
        if 101 < iaq < 150:
            display_status(70)
            print("Air quality is lightly polluted.")
        if 151 < iaq < 200:
            display_status(60)
            print("Air quality is moderately polluted.")
        if 201 < iaq < 250:
            display_status(50)
            print("Air quality is heavily polluted.")
        if 251 < iaq < 300:
            display_status(40)
            print("Air quality is severely polluted!")
        if 301 < iaq < 350:
            display_status(30)
            print("Air quality is severely polluted!")
        if 351 < iaq < 400:
            display_status(20)
            print("Air quality is extremely polluted!")
        if 401 < iaq:
            display_status(10)
            print("Air quality is extremely polluted!")

        time.sleep(5)

except KeyboardInterrupt:
    display_clear()
    print("Program interrupted by user!")
