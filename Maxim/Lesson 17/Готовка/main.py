import asyncio
from aiohttp import web
from routers import routes

app = web.Application()

for route in routes:
    print(route[0], route[1], route[2], route[3])
    app.router.add_route(route[0], route[1], route[2], name=route[3])

if __name__ == '__main__':
    web.run_app(app)