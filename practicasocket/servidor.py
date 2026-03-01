import socket
import threading

HOST = '127.0.0.1'
PORT = 8000

def manejar_cliente(cliente, addr):
    print(f"Cliente {addr} conectado")
    
    while True:
        try:
            datos = cliente.recv(1024)
            if not datos:
                break

            mensaje = datos.decode()
            print(f"Operación recibida: {mensaje}")

            datos = mensaje.split()

            if len(datos) != 3:
                respuesta = "Formato invalido"
            else:
                num1 = float(datos[0])
                operacion = datos[1]
                num2 = float(datos[2])

                if operacion == "+":
                    resultado = num1 + num2
                elif operacion == "-":
                    resultado = num1 - num2
                elif operacion == "*":
                    resultado = num1 * num2
                elif operacion == "/":
                    if num2 == 0:
                        respuesta = "División entre cero no permitida"
                        cliente.send(respuesta.encode())
                        continue
                    resultado = num1 / num2
                else:
                    respuesta = "Operación no válida"
                    cliente.send(respuesta.encode())
                    continue

                respuesta = str(resultado)

            print(f"Resultado enviado: {respuesta}")
            cliente.send(respuesta.encode())

        except Exception as e:
            print("Error:", e)
            break

    cliente.close()
    print("El cliente se desconecto")

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()

    print("Servidor escuchando...")

    while True:
        cliente, addr = servidor.accept()
        hilo = threading.Thread(target=manejar_cliente, args=(cliente, addr))
        hilo.start()

iniciar_servidor()