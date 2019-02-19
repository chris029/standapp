import time

class TimeGuard:
    """Description of TimeGuard
    timeInt - ...
    status - ...
    sleepTime - a delay for CheckTime function; it's format is minutes * seconds"""
    
    __sleepTime = 10 * 60
    
    def __init__(self, timeInt=60, status=False):
        # timeInt = seconds * minutes
        self.__status = status
        self.__timeInt = timeInt * 60
        self.__initTime = int(time.time())
    
    def getStatus(self):
        return self.__status
    
    def getTimeInt(self):
        return self.__timeInt
 
    def setTimeInt(self, value):
        if(value.isdigit()):
            "value is in minutes; initTime update"
            self.__initTime = int(time.time())
            self.__timeInt = int(value) * 60
        else:
            print('Error, input is not a number')
            
    # check system time every <sleepTime> seconds with timeInt
    # return True if timeInt has passed
    def CheckTime(self):
        curTime = int(time.time())
        print("Current time interval: {}".format(self.__timeInt))
        
        if(self.__initTime + self.__timeInt >= curTime):
            self.__status = False
        else:
            self.__status = True
