from emailClient import *
from DataParser import OpenWeatherParser

class RainNotifier:
    def __init__(self,) -> None:
        self.receivers = []
        self.mail_clinet = Mail()
        self.openWeatherParser = OpenWeatherParser("http://api.openweathermap.org/data/2.5/forecast")

    def sendAlert(self):
        for receiver in self.receivers:
            receiver_id = receiver["email_id"]
            receiver_lat = receiver["lat"]
            receiver_lng = receiver["lng"]
            will_rain_today = self.openWeatherParser.willRainToday(lat=receiver_lat,lng=receiver_lng)
            if will_rain_today:
                subject = "Rain Aleart 🌧️"
                msg = "Don't forget to carry your ☂️"
                self.mail_clinet.sendMail(to_email=receiver_id,subject=subject,body=msg)
    
    def addSubscriber(self,id:str,lat:float,lng:float):
        receiver = {}
        receiver["email_id"] = id
        receiver["lat"] = lat
        receiver["lng"] = lng
        self.receivers.append(receiver)

    def addSubscriber(self,data :dict):
        self.receivers.append(data)
    

