# Examen Parcial 1 - Chat en tiempo real con WebSockets y Docker

Aplicacion de chat compuesta por un **servidor** (que corre dentro de un
contenedor Docker) y **dos clientes** (que corren en terminales de VS Code).
Se usa la libreria **websockets** con **asyncio**: cada participante puede
enviar y recibir mensajes al mismo tiempo, sin esperar turnos, y el servidor
difunde los mensajes entre todos.

## Participantes

- **Servidor**: recibe conexiones, envia mensajes y los distribuye entre los clientes.
- **Cliente 1**: envia y recibe mensajes.
- **Cliente 2**: envia y recibe mensajes.

## Requisitos

- Docker (Docker Desktop) instalado y en ejecucion.
- Python 3 con la libreria `websockets` para los clientes:
  ```bash
  pip install "websockets>=14,<16"
  ```
- Visual Studio Code con dos terminales.

## Como ejecutar la aplicacion

### 1. Iniciar el servidor dentro del contenedor Docker

Desde la carpeta del proyecto ejecutar:

```bash
docker compose up
```

Deberia verse:

```
Servidor WebSocket escuchando en ws://localhost:8765
Esperando conexiones de los clientes...
```

El `docker-compose.yml` construye la imagen (Dockerfile) y publica el puerto
**8765** del contenedor en el puerto **8765** de la computadora anfitriona.

> Nota: en PowerShell usa `docker compose up` (con espacio). Si tu version de
> Docker es antigua, usa `docker-compose up`.

### 2. Conectar Cliente 1 desde una terminal de VS Code

Abrir una **primera terminal** en la carpeta del proyecto y ejecutar:

```bash
python cliente_chat.py
```

Cuando pida el nombre, escribir: `CLIENTE 1`

### 3. Conectar Cliente 2 desde otra terminal de VS Code

Abrir una **segunda terminal** (boton `+` en el panel de terminales) y ejecutar:

```bash
python cliente_chat.py
```

Cuando pida el nombre, escribir: `CLIENTE 2`

### 4. Chatear

- Escribir un mensaje en cualquier terminal y presionar **Enter**: el mensaje
  se difunde a todos los participantes.
- El servidor tambien puede escribir: en la terminal donde corre Docker,
  escribir un mensaje y presionar **Enter**, y los dos clientes lo recibiran.
- Para terminar un cliente escribir `salir`.



## Archivos

| Archivo             | Descripcion                                                        |
| ------------------- | ------------------------------------------------------------------ |
| `servidor_chat.py`  | Servidor WebSocket: difunde los mensajes entre todos los clientes  |
| `cliente_chat.py`   | Cliente WebSocket: envia y recibe mensajes a la vez                |
| `docker-compose.yml`| Ejecuta el servidor en Docker publicando el puerto 8765            |
| `Dockerfile`        | Imagen del servidor con la libreria websockets                     |
| `requirements.txt`  | Dependencias (websockets)                                          |
| `README.md`         | Estas instrucciones                                                |
# ExamenDistribuidas
