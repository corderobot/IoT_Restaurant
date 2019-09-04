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

#----- WEB SERVICE -----#



#----- COMMUNICATION -----#

#Sends warning to firefighters server
def send(ip, portn):
    import socket               
    sock = socket.socket()
    
    sock.connect((ip, portn))
    
    sock.send("on")
    
    print("succesful")
    sock.close()


#Port declaration

p0 = Pin(32, Pin.OUT)

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 3000))
s.listen(5)

#IP de bomberos
host = "192.168.43.193"
port = 1883

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request.decode())

    if request == "on":
        p0.value(1)
    else:
        p0.value(0)
        
        
    #response = 'Holi'
    #conn.send(response)
    conn.close()
