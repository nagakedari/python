import threading
import time

def do_something(sleep_seconds):
    print('function started.....')
    time.sleep(sleep_seconds)
    print('function completed....')

start_time = time.perf_counter()
t = threading.Thread(target=do_something, args=[1])
t.start()
t.join()
print(f'time taken: {time.perf_counter() - start_time} seconds')

