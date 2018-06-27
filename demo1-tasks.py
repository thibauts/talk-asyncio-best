import asyncio

loop = asyncio.get_event_loop()


async def mytask1():
    while True:
        print('Hello, asyncio 1 !')
        await asyncio.sleep(0.5)


async def mytask2():
    while True:
        print('Hello, asyncio 2 !')
        await asyncio.sleep(1.0)


loop.create_task(mytask1())
loop.create_task(mytask2())
loop.run_forever()
