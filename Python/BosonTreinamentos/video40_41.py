#socket - redes
#Scrip do cliente para comunição do cliente.py  


import socket

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Aguardando conexão de um cliente')

conn, ender = s.accept() #conexão / endereço

print('Conectado em ', ender)
while True: 
    data = conn.recv(1024)
    if not data:
        print('Fechando conexão')
        conn.close()
        break
    conn.sendall(data)