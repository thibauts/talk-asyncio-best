import asyncio
import websockets
import json

FEED_URL = 'wss://ws-feed.gdax.com'


async def feed(product_ids, channels):

    ws = await websockets.connect(FEED_URL)

    await ws.send(json.dumps({
        'type': 'subscribe',
        'product_ids': product_ids,
        'channels': channels
        }))

    while True:
        message = await ws.recv()
        event = json.loads(message)
        yield event


async def main():

    async for event in feed(['BTC-EUR'], ['full']):
        print(json.dumps(event, indent=True))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())