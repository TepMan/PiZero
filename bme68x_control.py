from enum import IntEnum
from bme68x import BME68X
import bme68xConstants as cnst
import bsecConstants as bsec
import time

bme = BME68X(cnst.BME68X_I2C_ADDR_HIGH, bsec.BSEC_ENABLE)


class IaqState(IntEnum):
    EXCELLENT = 7
    GOOD = 6
    LIGHTLY = 5
    MODERATELY = 4
    HEAVILY = 3
    SEVERELY = 2
    EXTREMELY = 1


def read_data():
    data = bme.get_bsec_data()
    iaq = data["iaq"]
    temp = data["temperature"]
    hum = data["humidity"]
    timestamp = time.asctime()

    description = get_iaq_description(iaq)

    measurement = {'iaq': iaq,
                   'temperature': temp,
                   "humidity": hum,
                   "timestamp": timestamp,
                   "iaq_description": get_iaq_description(iaq),
                   "description": description[0],
                   "iaq-state": description[1]}

    return measurement


def get_iaq_description(iaq: float):
    if 0 < iaq < 50:
        return "Air quality is excellent!", IaqState.EXCELLENT
    if 51 < iaq < 100:
        return "Air quality is good.", IaqState.GOOD
    if 101 < iaq < 150:
        return "Air quality is lightly polluted.", IaqState.LIGHTLY
    if 151 < iaq < 200:
        return "Air quality is moderately polluted.", IaqState.MODERATELY
    if 201 < iaq < 250:
        return "Air quality is heavily polluted.", IaqState.HEAVILY
    if 251 < iaq < 350:
        return "Air quality is severely polluted!", IaqState.SEVERELY
    if 351 < iaq :
        return "Air quality is extremely polluted!", IaqState.EXTREMELY
