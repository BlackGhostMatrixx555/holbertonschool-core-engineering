#!/usr/bin/env python3
"""
WebSocket broadcast server.
"""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Handler for WebSocket connections with broadcast messaging."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients.copy():
                try:
                    await client.send(f"B:{message}")
                except ConnectionClosed:
                    # Ignore if the client disconnected 
                    # before we could send the message
                    pass
    except ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


async def main():
    """Starts the WebSocket server."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())
