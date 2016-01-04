__author__ = 'Fisherworks'

from datetime import datetime

def dateTimeElementDelta(start, end, limit):
    delta = 0
    borrowFlag = False

    if end >= start:
        delta = end - start
    else:
        delta = end + limit - start
        borrowFlag = True

    #print start, end, delta
    return delta, borrowFlag


def isLeapYear(year):
    """Determine whether a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def dateTimeDelta(time_start = datetime(2012,1,13,11,55,0), time_end=datetime(2012,1,13,11,55,0)):
    """the time delta between 2 datetime, output a list with format
    [sec, min, hour, day, mon, year] as delta numbers of each level"""
    timeEnd = [time_end.second, time_end.minute, time_end.hour,
               time_end.day, time_end.month, time_end.year]
    timeStart = [time_start.second, time_start.minute, time_start.hour,
                 time_start.day, time_start.month, time_start.year]
    if time_start > time_end:
        raise Exception('End date is older!')

    timeLimit = [60, 60, 24, 0, 12, 0]

    if timeStart[4] in [1, 3, 5, 7, 8, 10, 12]:
        timeLimit[3] = 31
    elif timeStart[4] in [4, 6, 9, 11]:
        timeLimit[3] = 30
    elif timeStart[4] == 2:
        if isLeapYear(timeStart[5]):
            print 'leap'
            timeLimit[3] = 29
        else:
            timeLimit[3] = 28
    else:
        raise Exception('wrong month')

    timeDelta = [0, 0, 0, 0, 0, 0]
    for id in range(len(timeStart)):
        #print id
        timeDelta[id], borrowFlag = dateTimeElementDelta(timeStart[id], timeEnd[id], timeLimit[id])
        if borrowFlag is True:
            if timeEnd [id + 1] >= 1:
                timeEnd[id + 1] -= 1
            else:
                timeEnd[id + 1] = timeLimit[id + 1] - 1

    return timeDelta

def test():
    time1 = datetime.strptime('2012-1-13 11:55:00', "%Y-%m-%d %H:%M:%S")
    #print time1.year, time1.month, time1.day
    time2 = datetime.now()
    #time2 = datetime.strptime('2016-03-11 15:05:00', "%Y-%m-%d %H:%M:%S")

    deltaMyApi = dateTimeDelta(time1, time2)
    print ("I've spent {} years {} months {} days {} hours {} minutes and {} seconds with my dear 1st little one."
           .format(deltaMyApi[5], deltaMyApi[4], deltaMyApi[3], deltaMyApi[2], deltaMyApi[1], deltaMyApi[0]))

    time_delta = time2 - time1

    print ("Time delta by python built-in api: {}".format(time_delta))
    print ("Time delta in seconds by python api: {}".format(time_delta.total_seconds()))


if __name__ == "__main__":
    test()