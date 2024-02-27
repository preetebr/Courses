#Scrip do cliente para comunição do vídeo 40_41.py 
#Execução via python .\Python\BosonTreinamentos\cliente.py 


import socket

HOST = '127.0.0.1'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(str.encode('Boson'))
data = s.recv(1024)

print('Mensagem ecoada:', data.decode())