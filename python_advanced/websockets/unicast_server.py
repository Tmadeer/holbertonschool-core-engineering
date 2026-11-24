#!/usr/bin/env python3
"""Unicast WebSocket server managing multiple connected clients."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Track connected clients and unicast U:<message> back to sender."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            if isinstance(message, str):
                await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the unicast WebSocket server on 127.0.0.1:8765."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
