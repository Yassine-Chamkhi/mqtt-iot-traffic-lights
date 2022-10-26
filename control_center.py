import paho.mqtt.client as mqtt

controlCenter = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    if msg.topic == "trafficLights/leader":
        print("Leader light color: "+ str(msg.payload))
    elif msg.topic == "trafficLights/follower":
        print("Follower light color: "+ str(msg.payload))

controlCenter.on_connect = on_connect
controlCenter.on_message = on_message

brokerIP = input("Please input the broker IP address:")


controlCenter.connect(brokerIP, 1883)
controlCenter.subscribe("trafficLights/leader")
controlCenter.subscribe("trafficLights/follower")
controlCenter.loop_forever()