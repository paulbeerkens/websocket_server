from aiohttp import web

async def hello(request):
    return web.Response(text="Hello World")

async def handler(request):
    return web.Response(text=f"I see you {request.remote}");

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/',hello)])
    app.add_routes([web.get('/handler',handler)])

    web.run_app(app)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
