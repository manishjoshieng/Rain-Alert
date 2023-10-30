from RainAleart import RainNotifier
import pandas as pd


def start_rain_notification_service():
    rain_notifier = RainNotifier()
    df = pd.read_csv("rain_alert_receiver.csv")
    for index, row in df.iterrows():
        receiver = {key:value for key,value in row.items()}
        rain_notifier.addSubscriber(receiver)
    rain_notifier.sendAlert()



def main():
    start_rain_notification_service()

if __name__=="__main__":
    main()