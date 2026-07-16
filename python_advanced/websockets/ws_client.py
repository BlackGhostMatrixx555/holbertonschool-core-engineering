#!/usr/bin/env python3
"""
WebSocket client.
"""
import asyncio
import os
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Connects to a WebSocket server, sends a message, and returns the response."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    """Main function to run the client."""
    # Use the WS_URI environment variable if set by the checker, otherwise default to localhost
    uri = os.getenv("WS_URI", "ws://localhost:8765")
    response = await connect_and_send(uri, "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
