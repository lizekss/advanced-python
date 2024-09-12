import json

import requests

N_REQUESTS = 77
N_WORKERS = 77

base_url = 'https://jsonplaceholder.typicode.com/posts/'

import threading
import time

global_lock = threading.Lock()

def worker(i):
    url = f'{base_url}/{i}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with global_lock:
            with open("result", "a+") as file:
                file.write(json.dumps(data))
                file.write("\n")
    else:
        print(f'Error: {response.status_code}')

threads = []

start_time = time.time()

for i in range(N_WORKERS):
    t = threading.Thread(target=worker, args=(i + 1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()

print("All workers have finished. Time: ", end_time - start_time)

