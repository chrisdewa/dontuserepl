import asyncio

from aiohttp import web
from threading import Thread

__all__ = (
    'keep_alive',
)

def web_server():
    def main(request):
        return web.Response(text="I'm alive")
        
    app = web.Application()
    app.add_routes([web.get('/', main)])
    runner = web.AppRunner(app)
    return runner

def keep_alive():
    runner = web_server()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    loop.run_until_complete(site.start())
