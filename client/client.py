# client/client.py
import socket

HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024
FIN_CMD = 'éxito'   # Usuario escribirá "éxito" para terminar

def run_client():
    """Conecta al servidor y envía mensajes hasta que el usuario escriba FIN_CMD."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Conectado a {HOST}:{PORT}")
        while True:
            msg = input("Tu mensaje (escribe 'éxito' para salir): ")
            if msg.strip().lower() == FIN_CMD:
                print("Cerrando cliente.")
                break
            s.sendall(msg.encode())
            data = s.recv(BUFFER_SIZE)
            print('Respuesta del servidor:', data.decode())

if __name__ == '__main__':
    run_client()
