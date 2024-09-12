from concurrent.futures import ThreadPoolExecutor
import threading
import time
from worker_fns import writer, worker_with_separate_files, worker_with_global_lock

N_REQUESTS = 77
N_WORKERS = 50
BASE_URL = 'https://jsonplaceholder.typicode.com/posts/'

'''
Since blocking on writing into a single file was a bottleneck,
the approach of using a producer-consumer pattern was tried,
removing the need for a global lock by having the workers
write into separate files, and having their output assembled
by a single writer thread that waits on a queue.
'''
def run_threads():
    threads = []

    writer_thread = threading.Thread(target=writer, args=(N_REQUESTS,))
    threads.append(writer_thread)
    writer_thread.start()

    for i in range(N_REQUESTS):
        url = f'{BASE_URL}/{i + 1}'
        worker_thread = threading.Thread(
            target=worker_with_separate_files,
            args=(i + 1, url)
        )
        threads.append(worker_thread)
        worker_thread.start()

    for thread in threads:
        thread.join()


'''
Similar performance was shown by the simpler approach
of having a global lock on the output file,
but limiting the number of workers through ThreadPoolExecutor
'''
def run_threads_pool():
    global_lock = threading.Lock()
    with ThreadPoolExecutor(max_workers=N_WORKERS) as executor:
        for i in range(N_REQUESTS):
            url = f'{BASE_URL}/{i + 1}'
            executor.submit(worker_with_global_lock, url, global_lock)


start_time = time.time()
run_threads()
end_time = time.time()

print(f"All workers have finished. Time: {end_time - start_time:.2f} seconds")
