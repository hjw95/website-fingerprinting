import numpy
import time

def generateFeature(data):
    feature = []
    currentSeconds = -1
    consecutiveCount = 0
    packetPerSecond = []
    for packet in data['packets']:
        #2018-09-15 16:00:30.099882
        timeStampTime = 0
        try:
            timeStampTime = time.strptime(packet['timestamp'], "%Y-%m-%d %H:%M:%S.%f")
        except:
            timeStampTime = time.strptime(packet['timestamp'], "%Y-%m-%d %H:%M:%S")
        if(currentSeconds != timeStampTime.tm_sec):
            if(currentSeconds != -1):
                packetPerSecond.append(consecutiveCount)
            currentSeconds = timeStampTime.tm_sec
            consecutiveCount = 0
        else:
            consecutiveCount += 1
    feature.append(numpy.std(packetPerSecond))
    feature.append(numpy.mean(packetPerSecond))
    feature.append(numpy.median(packetPerSecond))
    feature.append(numpy.min(packetPerSecond))
    feature.append(numpy.max(packetPerSecond))
    return feature