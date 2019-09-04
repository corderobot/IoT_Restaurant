#----- CLIENT CONNECTION -----#

from machine import Pin
import network
import time

ssid = 'AndroidAP'			#SSID of the network
password = 'hola1234'	#Password of the network

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
    pass
print('Connection successful')
print(station.ifconfig())

#----- WEB SERVICE -----#

def web_page():
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
    
    sock.send("1")
    
    print("succesful")
    sock.close()


#----- EXECUTION -----#
host = "192.168.43.80"
port = 8080

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

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
    response = web_page()
    conn.send(response)
    conn.close()
