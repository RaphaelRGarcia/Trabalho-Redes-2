import socket

# Endereço IP e porta para escutar
host = '#IP'
port = 6347

# Criação do socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula o socket ao endereço e porta
sock.bind((host, port))

# Aguarda por conexões
sock.listen(1)

# Aceita uma conexão
print("Aguardando conexão...")
conn, addr = sock.accept()
print("Conexão estabelecida com:", addr)

# Envia dados para o computador B
data = "Olá, sou o computador A!"
conn.sendall(data.encode())

# Recebe dados do computador B
data = conn.recv(1024).decode()
print("Computador B enviou:", data)

# Fecha a conexão
conn.close()