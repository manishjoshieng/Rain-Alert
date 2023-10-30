import requests
import os, json
from datetime import datetime, timedelta
from enum import Enum
from JsonHandler import JsonHandler


class DATA_VALIDITY(Enum):
    SECOND  = 0
    MINUTE  = 1
    HOUR    = 2
    DAY     = 3
    WEEK    = 4
    MONTH   = 5
    QUARTER = 6
    YEAR    = 7


class DataParser:
    def __init__(self,url,key,cacheFileName, validTill = DATA_VALIDITY.DAY) -> None:
        self.url = url
        self.key = os.environ.get(key)
        self.fileName = cacheFileName
        self.validity = validTill
        self.fileHandler = JsonHandler(cacheFileName)
    
    def _getCacheData(self, key):
        old_data = self.fileHandler.getFile()
        if old_data:
            data = old_data.get(key)
            if data:
                valid_time = datetime.strptime(data["timestamp"],"%Y-%m-%d:%H-%M-%S")
                if valid_time > datetime.now():
                    return data["data"]
        return None
            
    def fatchData(self,param, keyid=None):
        if keyid:
            key = {key:value for key, value in param.items() if key != keyid}
        else:
            key = param
        data_key = str(key)
        data = self._getCacheData(data_key)
        if data:
            return data
        
        response = requests.get(url=self.url,params=param)
        if response.status_code == 200:
            data = response.json()
            cache_data = {}
            cache_data[data_key] = {}
            cache_data[data_key]["timestamp"] = self._get_next_valid_time().strftime("%Y-%m-%d:%H-%M-%S")
            cache_data[data_key]["data"] = data
            self.fileHandler.updateFile(cache_data)
            return data
        response.raise_for_status
        return None       
                
    def _get_next_valid_time(self, delta=1):
        data_validity = self.validity
        current_time = datetime.now()

        if data_validity == DATA_VALIDITY.SECOND:
            return current_time + timedelta(seconds=delta)
        elif data_validity == DATA_VALIDITY.MINUTE:
            return current_time + timedelta(minutes=delta)
        elif data_validity == DATA_VALIDITY.HOUR:
            return current_time + timedelta(hours=delta)
        elif data_validity == DATA_VALIDITY.DAY:
            return current_time + timedelta(days=delta)
        elif data_validity == DATA_VALIDITY.WEEK:
            return current_time + timedelta(weeks=delta)
        elif data_validity == DATA_VALIDITY.MONTH:
            # WARNING: This is a simple implementation and doesn't handle all edge cases for months
            return current_time + timedelta(days=delta * 30)
        elif data_validity == DATA_VALIDITY.QUARTER:
            return current_time + timedelta(days=delta * 90)
        elif data_validity == DATA_VALIDITY.YEAR:
            return current_time + timedelta(days=delta * 365)



class OpenWeatherParser(DataParser):
    def __init__(self, url, validTill=DATA_VALIDITY.DAY) -> None:
        super().__init__(url, "OPEN_WEATHER_API_KEY","OPEN_WEATHER_DATA", validTill)
        self.units = "metrix"
        self.lang = "en"
        self.cnt = 6

    def getWeatherData(self, lat,lng):
        param = {
            "lat" : lat,
            "lon" : lng,
            "appid" : self.key,
            "units" : "metric",
            "lang"  :  "en",
            "cnt"   :   self.cnt
        }
        data = self.fatchData(param,"appid")
        return data
    
    def willRainToday(self, lat:float, lng:float):
        weather_data = self.getWeatherData(lat,lng)
        if weather_data:
            list_of_data = weather_data.get("list")
            for instance in list_of_data:
                if instance["weather"][0]["id"] < 700:
                    return True
        return False    