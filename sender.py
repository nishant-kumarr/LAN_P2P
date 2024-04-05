import socket
import os


s = socket.socket()

host = socket.gethostname()

port = 12345

s.bind((host, port))


s.listen(5)

server_ip = socket.gethostbyname(host)
print("\nListening to ip : ",server_ip)


print('Waiting for connection...')

conn, addr = s.accept()

print(f"\nConnection established with {addr[0]} : {addr[1]}\n")


import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
filename = filedialog.askopenfilename()

print("Selected file:", filename)


file_size = os.path.getsize(filename)


conn.sendall(file_size.to_bytes(8, byteorder='big'))

with open(filename, 'rb') as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        conn.sendall(data)

print('File sent successfully\n\n')

conn.close()