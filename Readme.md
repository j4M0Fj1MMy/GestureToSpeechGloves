Setup SSP Bluetooth Profile on Raspberry Pi:
Sudo nano /etc/system/system/dbus-org.bluez.service
ExecStart=/usr/lib/bluetooth/bluetooth -C
ExecStartPost=/usr/bin/sdptool add SP
*Save and reboot Raspberry Pi and then pair phone and raspberry pi
pip install pybluez
and run the bluetoothcon.py
