import time
import paho.mqtt.client as mqtt

from traffic_light import TrafficLight

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print("follower successfully changed to color: "+ str(msg.payload))

leaderTrafficLight = TrafficLight(mqtt.Client(), "red", "leader")
leaderTrafficLight.mqttClient.on_connect = on_connect
leaderTrafficLight.mqttClient.on_message = on_message
leaderTrafficLight.mqttClient.connect("localhost", 1883)
leaderTrafficLight.mqttClient.subscribe("trafficLights/follower")

while True:
    time.sleep(3)
    leaderTrafficLight.switchColor()
    leaderTrafficLight.publishChange()


