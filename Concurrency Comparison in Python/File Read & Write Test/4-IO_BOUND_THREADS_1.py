import threading
import time

# Simulating file reading and writing task (I/O-bound)
def io_task(thread_id, file_name):
    start_time = time.time()
    with open(file_name, "a") as f:
        f.write(f"Data written by thread {thread_id}\n")
    end_time = time.time()
    print(f"Thread {thread_id} finished in {end_time - start_time:.4f} seconds.")

# Number of threads and file name
num_threads = 5
file_name = "thread_output.txt"

# Timing measurement
start_time = time.time()

threads = []
for i in range(num_threads):
    thread = threading.Thread(target=io_task, args=(i + 1, file_name))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

end_time = time.time()
print(f"Total time for threads: {end_time - start_time:.4f} seconds.")
