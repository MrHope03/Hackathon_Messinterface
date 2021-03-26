import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 


host = "192.168.1.101"

port = 5001

filename = "student1.txt"

filesize = os.path.getsize(filename)
