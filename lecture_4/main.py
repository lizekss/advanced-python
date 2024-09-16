import asyncio
import time

import aiohttp

from worker_fns import writer, worker_with_separate_files

N_REQUESTS = 77
BASE_URL = 'https://jsonplaceholder.typicode.com/posts/'

async def run_async_tasks():
    async with aiohttp.ClientSession() as session:
        writer_task = asyncio.create_task(writer(N_REQUESTS))

        worker_tasks = [
            asyncio.create_task(worker_with_separate_files(i + 1, session, BASE_URL))
            for i in range(N_REQUESTS)
        ]

        await asyncio.gather(*worker_tasks)
        await writer_task

start_time = time.time()
asyncio.run(run_async_tasks())
end_time = time.time()

print(f"All workers have finished. Time: {end_time - start_time:.2f} seconds")