# Examen Parcial 1 - Cliente de chat en tiempo real con WebSockets.
# Envia y recibe mensajes al mismo tiempo, sin esperar turnos.
# Ejecutar en dos terminales de VS Code: python cliente_chat.py

import asyncio
import os

from websockets.asyncio.client import connect

# Direccion del servidor; se puede cambiar con la variable de entorno WS_URL.
URL = os.environ.get("WS_URL", "ws://localhost:8765")


async def recibir(websocket):
    # Imprime todo lo que llega de los demas participantes.
    async for mensaje in websocket:
        print(mensaje)


async def main():
    # El nombre identifica al participante ([CLIENTE 1], [CLIENTE 2], ...).
    nombre = input("Tu nombre (ej. CLIENTE 1): ").strip() or "CLIENTE"

    async with connect(URL) as websocket:
        # Mini interfaz: separa la bienvenida de los mensajes del chat.
        print("=" * 44)
        print(f"  CHAT EN TIEMPO REAL - {nombre}")
        print("  Ya puedes escribir tu mensaje y presionar Enter.")
        print("  Escribe 'salir' para terminar.")
        print("=" * 44)

        # Tarea que escucha mensajes entrantes mientras escribimos.
        asyncio.create_task(recibir(websocket))

        loop = asyncio.get_running_loop()
        while True:
            try:
                # input() bloquea, por eso se ejecuta en otro hilo
                # y la recepcion de mensajes sigue activa.
                mensaje = await loop.run_in_executor(None, input)
            except EOFError:
                break

            if mensaje.strip().lower() == "salir":
                break

            await websocket.send(f"[{nombre}]: {mensaje}")


if __name__ == "__main__":
    asyncio.run(main())
