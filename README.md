# i3wm battery notifications
Notifications for low battery power in i3 window manager on Ubuntu. Possibly on other distros as well.

## Usage

To simply install the program to your PATH run:
`make install`

To install it and add its launch to your i3 config file run:
`make add` (Recommended)

If you'd rather have it be the percentage of the actual battery capacity, change the line

`fh = open("/sys/class/power_supply/BAT0/charge_full_design", 'r')`

to

`fh = open("/sys/class/power_supply/BAT0/charge_full", 'r')`

## Notice
This program assumes that your battery is named BAT0. If this is not the case, then correct it in the code. I haven't gotten around to making an automatic recognition yet.
