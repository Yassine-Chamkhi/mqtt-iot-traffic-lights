class TrafficLight:
    def __init__(self, mqttClient, lightColor, role):
        self.mqttClient = mqttClient
        self.lightColor = lightColor
        self.role = role

    def changeColor(self, color, opposite=False):
        if opposite:
            if color == "red":
                self.lightColor = "green"
            elif color == "green":
                self.lightColor ="red"
        else:
            self.lightColor = color
    
    def switchColor(self):
        if self.lightColor == "red":
            self.lightColor = "green"
        elif self.lightColor == "green":
            self.lightColor = "red"
    
    def publishChange(self):
        self.mqttClient.publish("trafficLights/"+self.role, self.lightColor)
        print("My current color: "+ self.lightColor)