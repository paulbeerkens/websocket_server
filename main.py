from aiohttp import web
import aiohttp

async def hello(request):
    return web.Response(text="Hello World")

async def handler(request):
    return web.Response(text=f"I see you {request.remote}");


async def websocket_handler(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/',hello)])
    app.add_routes([web.get('/handler',handler)])
    app.add_routes([web.get('/ws', websocket_handler)])

    web.run_app(app)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
