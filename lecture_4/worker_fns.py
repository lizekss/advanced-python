import asyncio
import json
import os

import aiofiles

file_queue = asyncio.Queue()


async def worker_with_separate_files(index, session, url):
    url = f'{url}/{index}'
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            filename = f'result{index}.json'

            async with aiofiles.open(filename, 'w') as file:
                await file.write(json.dumps(data, indent=4))

            await file_queue.put(index)
        else:
            print(f'Error: {response.status} for {url}')


async def writer(num_workers):
    count = 0

    async with aiofiles.open('data.json', 'w') as final_file:
        await final_file.write("[\n")
        while count < num_workers:
            index = await file_queue.get()
            count += 1
            filename = f'result{index}.json'

            async with aiofiles.open(filename, 'r') as file:
                data = await file.read()
                await final_file.write(data)
                if count < num_workers:
                    await final_file.write(",\n")
                else:
                    await final_file.write("\n")

            os.remove(filename)
        await final_file.write("]")
