import time

class kline:
    timestamp = 0
    low = 0.0
    high = 0.0
    open = 0.0
    close = 0.0
    volume = 0.0
    currency_volume = 0.0

    def printMyself(self):
        print("K线数据(timestamp:%s,\tlow:%f,\thigh:%f,\topen:%f,\tclose:%f,\tvolume:%f,\tcurrency_volume:%f" 
        %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.timestamp/1000)), self.low, self.high, self.open, self.close, self.volume, self.currency_volume))
    

    def __init__(self, timestamp, low, high, open, close, volume, currency_volume):
        self.timestamp = timestamp
        self.low = low
        self.high = high
        self.open = open
        self.close = close
        self.volume = volume
        self.currency_volume = currency_volume

