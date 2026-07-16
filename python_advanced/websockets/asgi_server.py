#!/usr/bin/env python3
"""
ASGI server with WebSocket integration using Starlette.
"""
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    """HTTP endpoint returning an HTML page."""
    return HTMLResponse("<h1>WebSocket App</h1>")


async def websocket_endpoint(websocket):
    """WebSocket endpoint echoing messages back to the client."""
    await websocket.accept()
    while True:
        try:
            message = await websocket.receive_text()
            await websocket.send_text(message)
        except Exception:
            # Breaks loop if the client disconnects or an error occurs
            break


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
