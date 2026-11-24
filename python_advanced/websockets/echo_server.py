#!/usr/bin/env python3
"""Echo WebSocket server using asyncio and websockets."""

import asyncio
import websockets


async def connection_handler(websocket):
    """Echo every incoming text message back to the connected client."""
    async for message in websocket:
        if isinstance(message, str):
            await websocket.send(message)


async def main():
    """Start the WebSocket server on 127.0.0.1:8765."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
