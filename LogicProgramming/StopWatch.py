import time


def start():
    return time.time()


def stop():
    return time.time()


def getElapsedTime():
    starts = int(input("Enter 0 to Start:"))
    startTime = start()
    stops = int(input("Enter 0 to Stop Time:"))
    endTime = stop()
    timeElapsed = endTime - startTime
    print("Time elapsed from Start to Stop is: ", timeElapsed, " Sec")


def main():
    print("hello jaaaaaaaa")
    getElapsedTime()


main()
