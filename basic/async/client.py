import aiohttp
import datetime
import logging
import time
import asyncio

logging.root.setLevel(logging.DEBUG)


async def fetch_one(url, i):
    start = time.time()
    logging.info("(%d) Fetch url %s at %s", i, url, datetime.datetime.now())
    async with aiohttp.ClientSession() as session:
        await session.get(url)
    logging.info("(%d) Fetched url %0.3f sec", i, time.time() - start)


async def main(url, n):
    coroutines = [fetch_one(url, i) for i in range(n)]
    await asyncio.gather(*coroutines)


if __name__ == '__main__':
    asyncio.run(main('http://localhost:8080', 100))
