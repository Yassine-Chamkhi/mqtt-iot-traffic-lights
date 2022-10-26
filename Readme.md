## Traffic Light Simulation based on MQTT and "Raspberry Pi Desktop" Virtual Machines
In this IoT project (school assignment), I simulate the basic behaviour of traffic lights (written in python) by making them communicate through an MQTT broker (Mosquitto). For the simulation, I used two Virtual Machines containing the Raspberry Pi Desktop OS. In one of them, we have the Mosquitto Broker and the leader light, in the other we have the folower light.

The leader light changes its color every 3 seconds and publishes it to the topic ```trafficLights/leader```. The follower light subscribes to that topic, updates its color and publishes its state to the topic ```trafficLights/follower``` upon reading the leader's message. We have a third element that is the control center that we can deploy in a third machine to observe the state of both lights. It can be extended to add the ability to control the lights' status in a future update.

## Running the code
Run the mosquitto broker with a configuration file where connections from all ip addresses are accepted:
```mosquitto -c path/to/configuration/file/```
Copy the leader_light.py and traffic_light.py to the same machine as the broker. Copy the follower_light.py and traffic_light.py files to the second machine.
Run ```python leader_light.py``` and ```python follower_light.py``` in their respective machines and run ```python control_center.py``` in your machine to observe the state of both lights at the same time.
