import asyncio
from sanic import Sanic, response

app = Sanic()


@app.route('/')
async def index(request):
    return response.json({
        'message': 'Hello, Sanic !'
        })


@app.websocket('/feed')
async def feed(request, ws):
    while True:
        await ws.send('Hello, Sanic !')
        await asyncio.sleep(1)


app.run()
