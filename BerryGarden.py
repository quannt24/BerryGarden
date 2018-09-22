#!/usr/bin/python3

import time
import datetime
import RPi.GPIO as GPIO

PUMP_CTL_PIN = 7

schedule = [
        ((0, 0), (0, 15)),
        ((6, 0), (6, 15)),
        ((9, 0), (9, 15)),
        ((12, 0), (12, 15)),
        ((15, 0), (15, 15)),
        ((18, 0), (18, 15)),
        ]

def turnPumpOn():
    print("Turning pump on")
    GPIO.output(PUMP_CTL_PIN, True)

def turnPumpOff():
    print("Turning pump off")
    GPIO.output(PUMP_CTL_PIN, False)

def main():
    print("BerryGarden")

    # Setup GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PUMP_CTL_PIN, GPIO.OUT)
    GPIO.output(PUMP_CTL_PIN, False)

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
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    except Exception as e:
        print("Exception: " + str(e))
    finally:
        GPIO.cleanup()
