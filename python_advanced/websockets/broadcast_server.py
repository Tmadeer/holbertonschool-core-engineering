#!/usr/bin/env python3
"""Broadcast WebSocket server distributing messages to all connected clients."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def broadcast(message):
    """Send a prefixed message to all currently connected clients."""
    payload = f"B:{message}"
    clients = list(connected_clients)
    if not clients:
        return
    results = await asyncio.gather(
        *(client.send(payload) for client in clients),
        return_exceptions=True,
    )
    for client, result in zip(clients, results):
        if isinstance(result, Exception):
            connected_clients.discard(client)


async def connection_handler(websocket):
    """Track connected clients and broadcast incoming text messages."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            if isinstance(message, str):
                await broadcast(message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the broadcast WebSocket server on 127.0.0.1:8765."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
