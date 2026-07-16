#!/usr/bin/env python3
"""
WebSocket echo server.
"""
import asyncio
import websockets

async def connection_handler(websocket):
    """Handler for WebSocket connections."""
    async for message in websocket:
        await websocket.send(message)

async def main():
    """Starts the WebSocket server."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
