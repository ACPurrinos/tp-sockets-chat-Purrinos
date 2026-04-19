# server.py

import socket
import sqlite3
from datetime import datetime

# -------------------------------
# Configuración del servidor
# -------------------------------
HOST = '127.0.0.1'  # localhost
PORT = 5000         # puerto

# -------------------------------
# Inicializar base de datos
# -------------------------------
def init_db():
    try:
        conn = sqlite3.connect("chat.db")
        cursor = conn.cursor()  #permite ejecutar sql

        # Crear tabla si no existe
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contenido TEXT,
            fecha_envio TEXT,
            ip_cliente TEXT
        )
        """)

        conn.commit() #guardar en db
        conn.close()
    except Exception as e:
        print("Error al inicializar la base de datos:", e)


# -------------------------------
# Guardar mensaje en la DB
# -------------------------------
def guardar_mensaje(contenido, ip):
    try:
        conn = sqlite3.connect("chat.db")
        cursor = conn.cursor()

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
        INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
        VALUES (?, ?, ?)
        """, (contenido, fecha, ip))

        conn.commit()
        conn.close()

        return fecha

    except Exception as e:
        print("Error al guardar mensaje:", e)
        return None


# -------------------------------
# Inicializar socket
# -------------------------------
def iniciar_servidor():
    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind((HOST, PORT))
        servidor.listen()

        print(f"Servidor escuchando en {HOST}:{PORT}")
        return servidor

    except OSError as e:
        print("Error: el puerto puede estar ocupado:", e)
        return None


# -------------------------------
# Aceptar conexiones
# -------------------------------
def aceptar_conexiones(servidor):
    while True:
        try:
            cliente, direccion = servidor.accept()
            print(f"Conexión desde {direccion}")

            manejar_cliente(cliente, direccion)

        except Exception as e:
            print("Error al aceptar conexiones:", e)


# -------------------------------
# Manejar cliente
# -------------------------------
def manejar_cliente(cliente, direccion):
    ip = direccion[0]

    try:
        while True:
            mensaje = cliente.recv(1024).decode()

            if not mensaje:
                break

            print(f"Mensaje recibido de {ip}: {mensaje}")

            fecha = guardar_mensaje(mensaje, ip)

            if fecha:
                respuesta = f"Mensaje recibido: '{mensaje}' el {fecha}"
            else:
                respuesta = "Error al guardar mensaje"

            cliente.send(respuesta.encode())

    except Exception as e:
        print("Error con el cliente:", e)

    finally:
        cliente.close()
        print(f"Conexión cerrada con {ip}")


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    init_db()
    servidor = iniciar_servidor()

    if servidor:
        aceptar_conexiones(servidor)