Chat Básico Cliente-Servidor

Este proyecto implementa un chat básico cliente-servidor usando sockets en Python y una base de datos SQLite para almacenar los mensajes.

📁 Estructura de carpetas

chat_basic/
├── README.md
├── server/
│   ├── server.py
│   └── db_utils.py
└── client/
    └── client.py

Dónde ubicar este archivo:
Coloca README.md en la raíz del proyecto chat_basic/, junto a las carpetas server/ y client/.

🚀 Prerrequisitos

Python 3.6 o superior

Módulo estándar sqlite3 incluido con Python

🛠️ Instalación y configuración

Clona el repositorio o descomprime el ZIP:

git clone <URL_DEL_REPO>
cd chat_basic

(Opcional) Crea un entorno virtual:

python3 -m venv venv
source venv/bin/activate

No hay dependencias externas, sólo Python estándar.

▶️ Uso

Iniciar el servidor (en una terminal):

cd server
python server.py

El servidor escuchará en localhost:5000.

Se creará (o inicializará) la base de datos chat.db.

Iniciar el cliente (en otra terminal):

cd client
python client.py

Escribe mensajes y presiona Enter para enviarlos.

Escribe éxito para cerrar el cliente.

🧩 Detalles de implementación

Modularización: La lógica de base de datos está en db_utils.py y la lógica de red en server.py.

Manejo de errores:

Se captura OSError si el puerto ya está en uso.

Se manejan excepciones de SQLite en caso de problemas con la base de datos.

Comentarios: Cada sección clave del código incluye comentarios explicativos.