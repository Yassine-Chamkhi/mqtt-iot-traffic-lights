import time
import paho.mqtt.client as mqtt

from traffic_light import TrafficLight

followerTrafficLight = TrafficLight(mqtt.Client(), "red", "follower")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    if msg.topic == "trafficLights/leader":
        followerTrafficLight.changeColor(msg.payload, True)
        followerTrafficLight.publishChange()

followerTrafficLight.mqttClient.on_connect = on_connect
followerTrafficLight.mqttClient.on_message = on_message

brokerIP = input("Please input the broker IP address:")

followerTrafficLight.mqttClient.connect(brokerIP, 1883)
followerTrafficLight.mqttClient.subscribe("trafficLights/leader")

followerTrafficLight.mqttClient.loop_forever()



