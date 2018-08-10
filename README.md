# i3wm battery notifications
Notifications for low battery power in i3 window manager on Ubuntu.

# Usage
Add the below line to the i3 config file.

`exec --no-startup-id python3 [PATH TO FILE]/batnot.py`

In the top of the python file you can change the threshold for warnings, default 20% (of the actual battery capacity).

If you'd rather have it be the percentage of the battery design capacity, change the line

`fh = open("/sys/class/power_supply/BAT0/charge_full", 'r')`

to

`fh = open("/sys/class/power_supply/BAT0/charge_full_design", 'r')`
