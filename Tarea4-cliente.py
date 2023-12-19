import socket
import time

def enviar_servidor(comando):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('192.168.100.90', 3490))  # Debes cambiar la IP y puerto según tu configuración

    cliente.send(comando.encode('utf-8'))
    response = cliente.recv(1024).decode('utf-8')

    if comando == "bye":
        print(response)
        time.sleep(1)
        cliente.close()
        exit()
    else:
        print(response)

if __name__ == "__main__":
    while True:
        comando = input()
        enviar_servidor(comando)
