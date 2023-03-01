import aiohttp
import asyncio
import time
import async_timeout


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(100):
        async with session.get(url) as response:
            print(f"Page took {time.time() - page_start}")
            return response.status


async def get_multiple_pages(loop, *urls):
    tasks = []

    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    urls = [
        'http://google.com',
        'http://example.com'
    ]

    start = time.time()
    pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
    print(f"All took {time.time() - start}")

    for page in pages:
        print(page)
