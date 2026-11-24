#!/usr/bin/env python3
"""WebSocket client using asyncio and websockets."""

import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to a WebSocket URI, send one text message, and return one reply."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        if isinstance(response, bytes):
            return response.decode()
        return response


async def main() -> None:
    """Connect to ws://localhost:8765, send 'Hello WebSocket', and print reply."""
    response = await connect_and_send("ws://localhost:8765", "Hello WebSocket")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
