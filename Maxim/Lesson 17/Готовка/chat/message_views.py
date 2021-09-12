from aiohttp import web

async def getMessage(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def sendMessage(request):
    text = "Hello, " + 'name'
    return web.Response(text=text)