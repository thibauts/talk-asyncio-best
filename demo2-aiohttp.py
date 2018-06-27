import asyncio
import aiohttp
import json

URL = 'http://httpbin.org/get'


async def fetch(url):

    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.json()
        return data


async def main():

    urls = [
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get'
    ]

    requests = [fetch(url) for url in urls]

    results = await asyncio.gather(*requests)

    print(json.dumps(results, indent=2))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())