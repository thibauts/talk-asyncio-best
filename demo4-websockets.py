import asyncio
import websockets


async def main():

  ws = await websockets.connect('ws://localhost:8000/feed')
  while True:
    message = await ws.recv()
    print(message)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())