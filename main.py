import time
from display_control import display_clear, display_status

display_clear()
control = True

while control:
    for i in range(100):
        display_status(i)
        time.sleep(0.5)

    display_clear()

    char = input("Zum Beenden x drücken: ")

    if char == 'x' or char == 'X':
        control = False
