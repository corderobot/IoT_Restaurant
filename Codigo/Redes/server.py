#----- SERVER CONNECTION -----#

from machine import Pin
import network
import time

ssid = 'AndroidAP'            #SSID of the network
password = 'hola1234'   #Password of the network

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
    pass
print('Connection successful')
print(station.ifconfig())

#----- COMMUNICATION -----#

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8080))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)

    #response = 'Holi'
    #conn.send(response)
    conn.close()
