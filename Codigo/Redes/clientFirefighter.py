#----- CLIENT CONNECTION -----#

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

#Sends warning to central server
def send(ip, portn):
    import socket               
    sock = socket.socket()
    
    sock.connect((ip, portn))
    
    sock.send("1")
    
    print("succesful")
    sock.close()


#----- EXECUTION -----#

import socket

#Web declaration

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1883))
s.listen(2)

#Pin declaration

a0 = Pin(26, Pin.OUT)
a2 = Pin(34, Pin.IN)

while True:
    if a0.value() == 0:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request.decode())
        print(request)
        if request == "on":
            a0.value(1)
            print("Alarma encendida")
        conn.close()
    else:
        if a2.value():
            a0.value(0)
            print("Alarma Apagada")
