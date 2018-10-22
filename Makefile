install:
	sudo chmod +x i3-battery-notification.py
	sudo cp i3-battery-notification.py /usr/bin/i3-battery-notification

add: install
	echo "\n#Start the battery notification script\nexec --no-startup-id i3-battery-notification" >> ~/.config/i3/config
