import requests

colors = ["red", "RED", "pink", "PINK", "BLUE", "blue", "WHITE", "white", "GREEN", "green", "ORANGE", "orange"]

class Hue:
    def __init__(self, user, ip, lamp):
        self.user = user
        self.ip = ip
        self.lamp = lamp
        self.url = 'http://{}/api/{}/lights/{}/state/'.format(self.ip, self.user, self.lamp)
    def set_lamp(self, is_on):
        data = {'on': is_on}
        requests.put(self.url, json=data)
    def set_color(self, color):
        if color == "ORANGE" or "orange":
            data = {"on": True, "sat": 254, "bri": 254, "hue": 10880}
        elif color == "GREEN" or "green":
            data = {"on": True, "sat": 254, "bri": 254, "hue": 21760}
        elif color == "WHITE" or "white":
            data = {"on": True, "sat": 254, "bri": 254, "hue": 32640}
        elif color == "BLUE" or "blue":
            data = {"on": True, "sat": 254, "bri": 254, "hue": 43520}
        elif color == "PINK" or "pink":
            data = {"on": True, "sat": 254, "bri": 254, "hue": 54400}
        elif color == "RED" or "red":
            data = {"on": True, "sat": 254, "bri": 254, "hue": 65280}
        requests.put(self.url, json=data)
