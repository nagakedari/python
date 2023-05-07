import concurrent.futures
import time

def do_something(sleep_seconds):
    print(f'Sleeping {sleep_seconds} second(s)...')
    time.sleep(sleep_seconds)
    return f'Done Sleeping...{sleep_seconds}'

secs = [5,4,3,2,1]
start_time = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    # using List comprehension
    results = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    # using map
    # executor.map(do_something, secs)

print(f'time taken: {time.perf_counter() - start_time} seconds')