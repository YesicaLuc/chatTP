# server/db_utils.py
import sqlite3
from datetime import datetime

DB_PATH = 'chat.db'

def init_db():
    """Crea la tabla de mensajes si no existe."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contenido TEXT NOT NULL,
            fecha_envio TEXT NOT NULL,
            ip_cliente TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_message(contenido: str, ip_cliente: str):
    """Guarda un mensaje con timestamp e IP en la base."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
    cursor.execute('''
        INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
        VALUES (?, ?, ?)
    ''', (contenido, timestamp, ip_cliente))
    conn.commit()
    conn.close()
