"""
A simple Python script to receive messages from a client over
Bluetooth using PyBluez (with Python 2).
"""

import bluetooth

port = 1
backlog = 0
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind(("", port))
s.listen(backlog)
try:
    client, clientInfo = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            if data == b"COMP\r\n":
                print("Cool Bluetooth")
            print(data)
            client.send(data)  # Echo back to client
            for i in range(2):
                print("Hello")
except:
    print("Closing socket")
    client.close()
    s.close()
