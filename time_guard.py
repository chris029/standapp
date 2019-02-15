import time

class TimeGuard:
    """Description of TimeGuard
    timeInt - ...
    status - ...
    sleepTime - a delay for CheckTime function; it's format is minutes * seconds"""
    
    __sleepTime = 10*60
    
    def __init__(self, timeInt=60*60, status=False):
        # timeInt = seconds * minutes
        self.__timeInt = timeInt
        self.__initTime = int(time.time())
    
    # timeInt getter
    @property
    def timeInt(self):
        return self.__timeInt
 
    # timeInt setter
    @timeInt.setter
    def timeInt(self, value):
        if(value.isdigit()):
            "value is in minutes; initTime update"
            self.__initTime = int(time.time())
            self.__timeInt = value * 60
        else:
            print('Error, input is not a number')
            
    # check system time every <sleepTime> seconds with timeInt
    # return True if timeInt has passed
    def CheckTime(self):
        curTime = int(time.time())
        while(self.__initTime + self.__timeInt >= curTime):
            time.sleep(self.__sleepTime)
            curTime = int(time.time())
        return True
