# -*- coding: utf-8 -*-
import time, os

warning_threshold = 0.2

os.system('/usr/bin/notify-send "Batnot started."')

def main():
    global warning_threshold
    charging = False
    new = 0
    hasAlerted = False
    while True:
        old = new
        fh = open("/sys/class/power_supply/BAT0/charge_now", 'r')
        new = float(fh.read())
        fh.close()

        fh = open("/sys/class/power_supply/BAT0/charge_full", 'r')
        full = float(fh.read())
        fh.close()

        fh = open("/sys/class/power_supply/BAT0/status", 'r')
        status = fh.read()
        charging = (status == 'Charging\n') or (status == 'Full\n')
        fh.close()

        power = new/full
        # os.system('/usr/bin/notify-send "Power: %s"'%str(power))
        # print("------\nPower: %f\nStatus: %s" % (power, status))
        if power < warning_threshold and not hasAlerted and not charging:
            # print("Warning: Power below 30%")
            os.system('wall "Warning: battery power low"')
            os.system('/usr/bin/notify-send "Warning: battery power low"')
            hasAlerted = True
        elif charging:
            hasAlerted = False
        time.sleep(20)

if __name__ == "__main__":
    main()
