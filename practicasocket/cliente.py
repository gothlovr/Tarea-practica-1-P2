import socket

HOST = '127.0.0.1'
PORT = 8000
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

while True:
    n1 = input("Ingresa el primer digito: ")
    op = input("Ingresa la operación a realizar (+, -, *, /): ")
    n2 = input("Ingresa el segundo digito: ")

    mensaje = n1 + " " + op + " " + n2
    cliente.send(mensaje.encode())

    respuesta = cliente.recv(1024).decode()
    print("Respuesta: ", respuesta)

    op2 = input("¿Deseas hacer otra operación? (s/n): ")
    if  op2 != "s":
        break

cliente.close()