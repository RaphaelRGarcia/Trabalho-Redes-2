import socket

# Endereço IP e porta do computador A
host = '#IP'
port = 6347

# Criação do socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao computador A
sock.connect((host, port))
print("Conexão estabelecida com o computador A")

# Recebe dados do computador A
data = sock.recv(1024).decode()
print("Computador A enviou:", data)

# Envia dados para o computador A
data = "Olá, sou o computador B!"
sock.sendall(data.encode())

# Fecha a conexão
sock.close()