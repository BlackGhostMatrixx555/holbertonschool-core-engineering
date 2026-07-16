#!/usr/bin/env python3
"""
WebSocket unicast server.
"""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()

async def connection_handler(websocket):
    """Handler for WebSocket connections with unicast messaging."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
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
