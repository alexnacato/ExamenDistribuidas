# Examen Parcial 1 - Servidor de chat en tiempo real con WebSockets.
# Difunde cada mensaje de un cliente a todos los conectados y
# permite al servidor participar en el chat desde su consola.

import asyncio
import sys

from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

PORT = 8765

# Conexiones activas de los clientes.
clientes = set()


async def difundir(mensaje):
    # Envia el mensaje a todos los clientes conectados.
    # Si uno ya se desconecto, se quita sin afectar a los demas.
    for c in list(clientes):
        try:
            await c.send(mensaje)
        except ConnectionClosed:
            clientes.discard(c)


async def atender(websocket):
    # Atiende a un cliente: escucha sus mensajes y los reenvia a todos.
    clientes.add(websocket)
    try:
        async for mensaje in websocket:
            print(mensaje)
            await difundir(mensaje)
    finally:
        # El cliente se desconecto: lo quitamos de la lista.
        clientes.discard(websocket)


async def consola_servidor():
    # Difunde lo que el servidor escribe en su consola como [SERVIDOR].
    # input() bloquea, por eso se ejecuta en otro hilo con run_in_executor.
    loop = asyncio.get_running_loop()
    while True:
        # input() no es seguro en un hilo con TTY interactivo;
        # sys.stdin.readline() lee igual y funciona en cualquier caso.
        linea = await loop.run_in_executor(None, sys.stdin.readline)
        if not linea:
            break  # stdin cerrado (EOF).
        texto = linea.strip()
        if texto:
            await difundir(f"[SERVIDOR]: {texto}")


async def main():
    async with serve(atender, "0.0.0.0", PORT):
        print(f"Servidor WebSocket escuchando en ws://localhost:{PORT}")
        print("Esperando conexiones de los clientes...")

        asyncio.create_task(consola_servidor())
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
