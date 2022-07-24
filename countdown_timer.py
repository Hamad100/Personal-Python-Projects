# Countdown Program

from time import sleep

countDown = input("What number should we count down from?")

countDown = int(countDown)

if countDown <=0:
    print("Invalid Entry. Number must higher than 0")
else:
    print("Countdown started")
    while countDown >= 0:
        print(countDown)
        countDown -= 1
        sleep(1)