#!/usr/bin/python3

import time
import datetime

def turnPumpOn():
    print("Turning pump on")

def turnPumpOff():
    print("Turning pump off")

def main():
    print("BerryGarden")

    schedule = [
            ((8, 0), (8, 15)),
            ((14, 0), (14, 15)),
            ((21, 0), (21, 15)),
            ]

    print()
    print("Schedule:")
    for s in schedule:
        print(s)

    pumpOn = False
    while True:
        t = datetime.datetime.now().time()

        # Check if currently in a schedule
        inSchedule = False
        for s in schedule:
            start = datetime.time(s[0][0], s[0][1])
            end = datetime.time(s[1][0], s[1][1])
            if start <= t and t < end:
                inSchedule = True
                break

        if inSchedule:
            if not pumpOn:
                print(t)
                turnPumpOn()
            pumpOn = True
        else:
            # If not in any schedules, turn pump off
            if pumpOn:
                print(t)
                turnPumpOff()
            pumpOn = False

        try:
            time.sleep(10)
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            break

if __name__ == "__main__":
    # execute only if run as a script
    main()
