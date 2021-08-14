import paho.mqtt.client as mqtt
import json

TOPIC = "iaq/data"
BROKER_ADDRESS = "raspi4"
PORT = 1883
QOS = 1

client = mqtt.Client()

client.connect(BROKER_ADDRESS, PORT)

print("Connected to MQTT Broker: " + BROKER_ADDRESS)
print("==================================")
print(" ")


def send_data(data):
    payload = json.dumps(data)

    client.publish(TOPIC, payload, qos=QOS)
    client.loop()
