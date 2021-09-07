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

def run_server(runner):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    loop.run_until_complete(site.start())
    loop.run_forever()

def keep_alive():
    runner = web_server()
    server = Thread(target=run_server, args=(runner,))
    server.start()
