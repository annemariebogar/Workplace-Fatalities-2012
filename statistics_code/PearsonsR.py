import statistics
import math

def pearsonsR(xlist, ylist):
    xMean = statistics.mean(xlist)
    yMean = statistics.mean(ylist)
    num = xDenom = yDenom = 0
    for k in range(len(xlist)):
        num += (xlist[k] - xMean) * (ylist[k] - yMean)
        xDenom += math.pow((xlist[k] - xMean), 2)
        yDenom += math.pow((ylist[k] - yMean), 2)
    denom = math.sqrt(xDenom * yDenom)
    r = num / denom
    return r

years = [31, 45, 49, 50, 57, 58, 60, 68, 79, 80, 81, 82, 82, 94, 98, 101, 103, 104, 104, 107, 108, 108, 110, 111, 111, 112, 112, 118, 119, 122, 123, 123, 124, 125, 126, 128, 131, 135, 136, 137, 138, 173, 175, 179, 184, 191, 206, 237, 238, 521]
rate = [2.6, 3.4, 3.6, 2.2, 2.6, 8.9, 3.5, 3.5, 3.4, 3.2, 3, 3.8, 3.8, 4.3, 6.6, 12.2, 1.7, 4, 4.2, 2.1, 2.7, 2.6, 5.7, 17.7, 3.5, 5.5, 3.1, 3.3, 2.2, 3.5, 2.4, 1.4, 4.9, 3.4, 2.3, 5.2, 6.1, 7.3, 4.8, 2.5, 2.5, 6.9, 3.1, 2.3, 2.4, 4.8, 6.4, 5.4, 2.7, 6.7]
#print(pearsonsR(years, rate))