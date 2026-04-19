import socket

HOST = '127.0.0.1'
PORT = 5000

def iniciar_cliente():
    try:
        # Configuración del socket TCP/IP
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((HOST, PORT))

        print(f"Conectado al servidor en {HOST}:{PORT}")
        print("Escribí 'éxito' para terminar.\n")

        while True:
            mensaje = input("Mensaje a enviar: ")

            # Condición de salida según consigna
            if mensaje.lower() == "éxito":
                break

            if not mensaje.strip(): # Evita enviar mensajes vacíos
                continue

            # 1. Enviar el mensaje al servidor
            cliente.send(mensaje.encode('utf-8'))
            print(f"Enviaste: {mensaje}")

            # 2. Recibir la respuesta 
            respuesta_binaria = cliente.recv(1024)
            
            # 3. Decodificar y mostrar la respuesta del servidor
            respuesta_texto = respuesta_binaria.decode('utf-8')
            print(f"Servidor dice: {respuesta_texto}")

        # Cerrar conexión
        cliente.close()
        print("Conexión finalizada correctamente.")

    except ConnectionRefusedError:
        print("Error: No se pudo conectar. ¿El servidor está encendido?")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    iniciar_cliente()