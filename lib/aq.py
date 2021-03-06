import serial
import time


class AQ:
    """A Class for the MonkMakes Air Quality Board for Raspberry Pi"""

    temp = 0
    eco2 = 0
    ser = None

    def __init__(self):
        self.ser = serial.Serial("/dev/ttyS0", 9600)

    def get_eco2(self):
        self.send("c")
        self._wait_for_message()
        return self.eco2

    def get_temp(self):
        self.send("t")
        self._wait_for_message()
        return self.temp

    def leds_manual(self):
        self.send("m")

    def leds_automatic(self):
        self.send("a")

    def set_led_level(self, slider_value):
        self.send(str(slider_value))

    def buzzer_on(self):
        self.send("b")

    def buzzer_off(self):
        self.send("q")

    def send(self, message):
        self.ser.write(bytes(message + "\n", 'utf-8'))

    def _wait_for_message(self):
        time.sleep(0.1)  # give attiny time to respond
        incoming_message = str(self.ser.readline()[:-2].decode("utf-8"))  # remove LF, CR turn into string
        message_parts = incoming_message.split("=")
        if len(message_parts) == 2:
            code, value = message_parts
            if code == "t":
                self.temp = float(value)
            elif code == "c":
                self.eco2 = float(value)
