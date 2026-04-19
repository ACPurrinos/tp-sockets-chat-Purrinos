# -------------------------------------------------------
# PFOgit init 1:  Implementación de un Chat Básico Cliente-Servidor
# Alumno: Purriños Andrea
# IFTS 29 - Programación sobre Redes
# -------------------------------------------------------

# Chat Básico Cliente-Servidor (Sockets & SQLite)

Este proyecto es una implementación de un sistema de chat básico utilizando **Sockets TCP/IP** en Python. Permite la comunicación entre un servidor y un cliente, almacenando todos los mensajes recibidos en una base de datos **SQLite**.


## Requisitos
* Python 3.x instalado.
* No requiere librerías externas (utiliza `socket`, `sqlite3` y `datetime` de la librería estándar).

## Estructura del Proyecto
```bash
.
├── server.py    # Lógica del servidor y gestión de DB
├── client.py    # Interfaz del cliente para envío de mensajes
└── chat.db      # Base de datos SQLite (se genera automáticamente)


## Instrucciones de Uso

### 1. Ejecutar el Servidor
Abrí una terminal en la carpeta del proyecto y ejecutá:
```bash
python server.py
```
El servidor se iniciará en `localhost:5000` y creará el archivo `chat.db` si no existe.

### 2. Ejecutar el Cliente
Abrí **otra terminal** distinta y ejecutá:
```bash
python client.py
```

### 3. Interacción
* Escribí mensajes en la terminal del cliente y presioná `Enter`.
* El servidor confirmará la recepción y guardará el dato.
* Para finalizar la conexión, escribí la palabra **`éxito`** en el cliente.

## Formato de la Base de Datos
La tabla `mensajes` cuenta con la siguiente estructura:
| `id` | INTEGER | Clave primaria autoincremental. |
| `contenido` | TEXT | El cuerpo del mensaje enviado. |
| `fecha_envio`| TEXT | Timestamp del momento de recepción. |
| `ip_cliente` | TEXT | Dirección IP desde donde se conectó el cliente. |


## Notas de la Entrega
* **Materia:** IFTS 29 - Programación sobre Redes
* **Tecnologías:** Python, SQLite.

