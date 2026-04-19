import sqlite3

def leer_mensajes():
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mensajes")
    filas = cursor.fetchall()
    
    print("\n--- CONTENIDO DE LA BASE DE DATOS ---")
    for fila in filas:
        print(f"ID: {fila[0]} | Mensaje: {fila[1]} | Fecha: {fila[2]} | IP: {fila[3]}")
    conn.close()

if __name__ == "__main__":
    leer_mensajes()