import socket

puerto=3490
#Entrada de datos
#DireccionIP = (input("ingresa la direccion a la que te quieras conectar\n")) # Se ingresa la direccion a la cual desea conectarse - 127.0.1.1
DireccionIP=input("Ingresa una dirección para conectar: ")
#Intermedio de la operacion
mi_socket = socket.socket() #creacion de socket
address=(DireccionIP, puerto) #Creacion de la direccion y puerto
print('la direccion es: {}'.format(*address))
mi_socket.connect(address)   #establecemos conexion 
#Envio de datos
MCliente = ("Hola desde el cliente") #Se crea el mensaje que se mandara
mi_socket.send(MCliente.encode()) #Se manda el mensaje codificado
condicion=True
try:
    respuesta = mi_socket.recv(1024)
    print('Se recibio un mensaje de el servidor: {!r}'.format(respuesta.decode()))
    while True:
        MCliente = (input("Ingresa el comando que gustes\n"))
        mi_socket.send(MCliente.encode()) #Se manda el mensaje codificado
        if (MCliente.lower() == "bye"):
            break
        respuesta = mi_socket.recv(1024)
        print(respuesta.decode())
        if not respuesta:
            break
finally:
    print("Se cerrara la conexion")
    mi_socket.close()

