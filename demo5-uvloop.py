import asyncio
import uvloop


async def mytask():
    print('Hello, uvloop !')


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

loop = asyncio.get_event_loop()
loop.create_task(mytask())
loop.run_forever()
