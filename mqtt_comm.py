import paho.mqtt.client as mqtt
from Measurement import Measurement

TOPIC = "iaq/data"
BROKER_ADDRESS = "raspi4"
PORT = 1883
QOS = 1

client = mqtt.Client()
client.connect(BROKER_ADDRESS, PORT)

print("Connected to MQTT Broker: " + BROKER_ADDRESS)
print("==================================")
print(" ")


def send_data(data:Measurement):
    payload = data.toJSON()
    print("Payload: " + str(payload))

    client.publish(TOPIC, payload, qos=QOS)

