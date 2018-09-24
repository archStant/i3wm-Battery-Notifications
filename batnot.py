# -*- coding: utf-8 -*-
import time
import os


os.system('/usr/bin/notify-send "Batnot started."')


def main():
    fh = open("/sys/class/power_supply/BAT0/charge_full_design", 'r')
    full = float(fh.read())
    fh.close()

    warning_threshold1 = 0.2
    warning_threshold2 = 0.10
    warning_threshold3 = 0.05

    hasAlerted1 = False
    hasAlerted2 = False
    hasAlerted3 = False
    hasAlertedFull = False

    charging = False
    new = 0
    while True:
        fh = open("/sys/class/power_supply/BAT0/charge_now", 'r')
        new = float(fh.read())
        fh.close()

        fh = open("/sys/class/power_supply/BAT0/status", 'r')
        status = fh.read()
        charging = (status == 'Charging\n') or (status == 'Full\n')
        fh.close()

        power = new / full
        # os.system('/usr/bin/notify-send "Power: %s"' % str(power))
        print("------\nPower: %f\nStatus: %s" % (power, status))
        if power < warning_threshold1 and not hasAlerted1 and not charging:
            # print("Warning: Power below 30%")
            # os.system('wall "Warning: battery power at %d\%"' % (int(warning_threshold1 * 100)))
            os.system('/usr/bin/notify-send "Warning: battery at %f"' % warning_threshold1)
            hasAlerted1 = True
        elif power < warning_threshold2 and not hasAlerted2 and not charging:
            # print("Warning: Power below 30%")
            # os.system('wall "Warning: battery power at %d\%"' % (int(warning_threshold2 * 100)))
            os.system('/usr/bin/notify-send "Warning: battery power low 2"')
            hasAlerted2 = True
        elif power < warning_threshold3 and not hasAlerted3 and not charging:
            # print("Warning: Power below 30%")
            # os.system('wall "Warning: battery power at %d\%"' % (int(warning_threshold3 * 100)))
            os.system('/usr/bin/notify-send "Warning: battery power low 3"')
            hasAlerted3 = True
        elif charging:
            hasAlerted1 = False
            hasAlerted2 = False
            hasAlerted3 = False
        time.sleep(20)


if __name__ == "__main__":
    main()
