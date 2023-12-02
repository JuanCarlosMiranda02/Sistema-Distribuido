import socket, threading, os, shutil
global condicion
# Función que maneja la conexión para un cliente
def handle_client(client_socket):
    try:
        client_address = client_socket.getpeername()
        data = client_socket.recv(1024)
        print('Conexión de: ', client_address)
        print('Se recibieron datos de {}: {}'.format(client_address, data.decode()))
        message = b'Usted se ha conectado exitosamente al servidor'
        client_socket.send(message)
        condicion=True
        while condicion:
            data = client_socket.recv(1024)
            if not data:
                print('No hay datos de', client_address)
                break
            command_parts = data.decode().strip().split(maxsplit=1)
            comando = command_parts[0]
            if "mv" in comando:
                if len(command_parts) > 1:
                    archivo=command_parts[1]
                    rutaActual = os.getcwd() + '/' + archivo
                    rutaNueva = client_socket.recv(1024).decode()
                    if os.path.isfile(rutaActual):
                        client_socket.sendall(b"ready")
                        # Mover el archivo
                        shutil.move(rutaActual, os.path.join(rutaNueva, archivo))
                        print(f'El archivo ha sido movido con éxito.')
                    else:
                        print(f'El archivo no existe en la ruta especificada.')
            if "ls" in comando:
                lista=os.listdir()
                listaConvertida='\n'.join(lista)
                response_message=bytes(listaConvertida,'utf-8')
                client_socket.send(response_message)
            if "echo" in comando:
                if len(command_parts) > 1:
                    response_message = bytes(command_parts[1], 'utf-8') 
                    client_socket.send(response_message)
                elif comando.lower()=='bye':
                    condicion=False
                    break
    finally:
        # Clean up the connection
        client_socket.close()
        print('Conexión cerrada con: ', client_address)
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('0.0.0.0', 3490)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(4)
print('Esperando conexiones...')
while True:
    # Wait for a connection
    client_socket, client_address = sock.accept()
    # Inicia un nuevo hilo para manejar la conexión con el cliente
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()