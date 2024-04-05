import socket
import os
import tkinter as tk
from tkinter import filedialog
s = socket.socket()

#host = input("\nEnter the sender ip address: ")
host = "192.168.20.146"       

port = 12345

s.connect((host, port))

print('Connected to sender')

file_size_bytes = s.recv(8)
file_size = int.from_bytes(file_size_bytes, byteorder='big')

file_obj = filedialog.asksaveasfile(
    defaultextension="*.*",  # Default extension if none provided by the user
    filetypes=[("Select extension (FileType)","*.*"), ("Text", "*.txt"), ("JPG", ".jpg"), ("PNG", ".png"), ("PDF",".pdf"), ("GIF", ".gif"), 
               ("MP3",".mp3"), ("MP4",".mp4")]  # Dropdown menu options
)


filename = file_obj.name if file_obj else None

if filename:
  
    with open(filename, 'wb') as f:
        while True:
            data = s.recv(1024)
            if not data:
                break
            f.write(data)

    print('File received successfully')
else:
    print('File saving canceled by user')

s.close()