# server/server.py
import socket
import sys
from DB_utils import init_db, save_message
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5000
BACKLOG = 5
BUFFER_SIZE = 1024

def init_socket():
    """Configura el socket TCP/IP y lo pone a escuchar."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(BACKLOG)
        print(f"Servidor escuchando en {HOST}:{PORT}")
        return s
    except OSError as e:
        print(f"Error al inicializar socket: {e}")
        sys.exit(1)

def handle_client(conn, addr):
    """Recibe mensajes de un cliente, los guarda y responde."""
    ip = addr[0]
    with conn:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            mensaje = data.decode().strip()
            # Guardamos en la BD
            save_message(mensaje, ip)
            # Respondemos con timestamp
            respuesta = f"Mensaje recibido: {datetime.now().isoformat()}"
            conn.sendall(respuesta.encode())

def run_server():
    """Función principal que arranca el servidor."""
    init_db()              # 1. Preparamos la base de datos
    sock = init_socket()   # 2. Arrancamos el socket
    try:
        while True:
            conn, addr = sock.accept()   # 3. Aceptamos nuevos clientes
            print(f"Conexión desde {addr}")
            handle_client(conn, addr)
    except KeyboardInterrupt:
        print("Servidor detenido por usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        sock.close()

if __name__ == '__main__':
    run_server()
