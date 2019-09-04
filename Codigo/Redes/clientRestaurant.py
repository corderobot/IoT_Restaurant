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

#----- WEB SERVICE -----#

def saf():
    html ="""
    <html>
        <head>
        <title>SAF</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:,">
        <style>
            html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
            h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}
            .button{display: inline-block; background-color: #31ad00; border: none;
            border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
            .button2{background-color: #f30c0c;}
        </style>
        </head>
        <body>
        <h1>Sistem Against Fires</h1>
        <p><a href="/?fire=yes"><button class="button">ALERT FIREFIGHTERS</button></a></p>
        <h1>Sistema de Iluminación</h1>
        <p><a href="/?light=on"><button class="button">ON</button></a></p>
        <p><a href="/?light=off"><button class="button">OFF</button></a></p>
        </body>
    </html>
    """
    return html

#----- COMMUNICATION -----#

#Sends warning to central server
def send(ip, portn):
    import socket               
    sock = socket.socket()
    
    sock.connect((ip, portn))
    
    sock.send("on")
    
    print("succesful")
    sock.close()

def sendon(ip, portn):
    import socket               
    sock = socket.socket()
    
    sock.connect((ip, portn))
    
    sock.send("on")
    
    print("succesful")
    sock.close()

def sendoff(ip, portn):
    import socket               
    sock = socket.socket()
    
    sock.connect((ip, portn))
    
    sock.send("off")
    
    print("succesful")
    sock.close()


#----- EXECUTION -----#
#Server IP
host = "192.168.43.80"
port = 8080

#LIght System
hostl = "192.168.43.38"
portl = 3000 

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

#Port Declaration
a5 = Pin(4, Pin.OUT)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)

    fion = request.find('/?fire=yes')
    if fion == 6:
        send(host, port)
        pass

    lion = request.find('/?light=on')
    if lion == 6:
        a5.value(1);
        sendon(hostl, portl)

    lioff = request.find('/?light=off')
    if lioff == 6:
        a5.value(0);
        sendoff(hostl, portl)
        
    response = saf()
    conn.send(response)
    conn.close()
