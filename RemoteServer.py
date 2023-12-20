import socket, threading, os
def manejarCliente(socketCliente):
    try:
        condicion =True
        clienteAddress= socketCliente.getpeername()
        datos = socketCliente.recv(1024)
        print('Conexión de: ', clienteAddress)
        print('Se recibieron datos de {}: {}'.format(clienteAddress, datos.decode()))
        message = b'Usted se ha conectado exitosamente a un servidor remoto'
        socketCliente.send(message)
        while condicion:
            datos = socketCliente.recv(1024)
            if not datos:
                print('No hay datos de', clienteAddress)
                break
            parteComando = datos.decode().strip().split(maxsplit=1)
            comando = parteComando[0]
            if "ls" in comando:
                lista=os.listdir()
                listaConvertida='\n'.join(lista)
                response_message=bytes(listaConvertida,'utf-8')
                socketCliente.send(response_message)
            if "bye" in comando:
                break
            
    finally:
            print('Cerrando conexion con el servidor remoto')
            socketCliente.close()
#puerto para conectar al servidor central
sockCentral= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address=('192.168.1.11',3490)
sockCentral.connect(address)
MCliente = ("Hola desde servidor remoto") #Se crea el mensaje que se mandara
sockCentral.send(MCliente.encode()) #Se manda el mensaje codificado
mensaje=sockCentral.recv(1024)
print(mensaje.decode())
#puerto para habilitar solicitudes de clientes
sRemoto=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
remoteAddress = ('127.0.1.1', 3490)
sRemoto.bind(remoteAddress)
sRemoto.listen(3)
print('Esperando conexiones...')
while True:
    # Esperando una conexión
    socketCliente, clienteAddress = sRemoto.accept()
    # Inicia un nuevo hilo para manejar la conexión con el cliente
    client_thread = threading.Thread(target=manejarCliente, args=(socketCliente,))
    client_thread.start()
#Manejar a diferentes usuarios

