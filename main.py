import time
from bme68x_control import read_data
from display_control import display_clear, display_blocks
from mqtt_comm import send_data

display_clear()

print("Air Qualitiy Measurement Tool v1.0")
print("==================================")
print(" ")

try:
    while True:
        data = read_data()

        display_blocks(int(data["iaq-state"]))

        print("Timestamp   : " + data["timestamp"])
        print("Air Quality : " + str(data["iaq"]))
        # print("Description : " + data["description"])
        # print("IAQ State   : " + data["iaq-state"].name)
        print("Temperature : " + '{:.1f}°C'.format(data["temperature"]))
        print("Humidity    : " + '{:.1f}%'.format(data["humidity"]))
        print(" ")

        send_data(data)

        time.sleep(30)

except KeyboardInterrupt:
    display_clear()
    print("Program interrupted by user!")
