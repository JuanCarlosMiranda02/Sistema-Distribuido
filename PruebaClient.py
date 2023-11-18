import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost=socket.gethostname()
ip=socket.gethostbyname(localhost)
# Connect the socket to the port where the server is listening
ip_address=input("Ingrese la IP del servidor: ")
server_address = (ip_address, 3490)
print('Conectando a la dirección {} puerto {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = "IP cliente: {} ".format(ip)
    print('Enviando IP al servidor')
    sock.sendall(message.encode())


    while True:
        data = sock.recv(1024)
        if not data:
        	break
        #Decodificar datos
        print('Se recibió un mensaje del servidor: {!r}'.format(data.decode()))
        

finally:
    print('closing socket')
    sock.close()
