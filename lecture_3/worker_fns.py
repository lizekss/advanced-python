import json
import os
import queue
import requests

def worker_with_global_lock(url, lock):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with lock:
            with open('result', 'a') as file:
                json.dump(data, file, indent=4)
                file.write(',\n')
    else:
        print(f'Error: {response.status_code}')

file_queue = queue.Queue()

def worker_with_separate_files(index, url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        filename = f'result{index}'
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        file_queue.put(index)
    else:
        print(f'Error: {response.status_code}')

def writer(num_workers):
    count = 0
    with open('data.json', 'w') as file:
        file.write('[\n')
        while True:
            index = file_queue.get()
            count += 1
            filename = f'result{index}'

            # Read the JSON data from the file
            with open(filename, 'r') as f:
                data = json.load(f)
                json.dump(data, file, indent=4)
                if count < num_workers:
                    file.write(',\n')
                else:
                    file.write('\n')

            # Delete the file after processing
            os.remove(filename)

            if count == num_workers:  # Sentinel value to stop the writer thread
                break
        file.write(']')
