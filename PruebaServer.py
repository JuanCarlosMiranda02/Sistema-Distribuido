import socket
import sys
import threading

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)

# Bind the socket to the port
server_address = (hostname, 3490)
print('Iniciando en {}, puerto {}, IP {}'.format(*server_address, ip))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(4)
while True:
    # Wait for a connection
    print('Esperando una conexión...')
    connection, client_address = sock.accept()
    try:
        print('Conexión de: ', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('Se recibieron datos de {}'.format(client_address))
            if data:
                print('Enviando respuesta a {}'.format(client_address))
                message='Usted se ha conectado exitosamente al servidor'
                connection.sendall(message.encode())
            else:
                print('No hay datos de', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
