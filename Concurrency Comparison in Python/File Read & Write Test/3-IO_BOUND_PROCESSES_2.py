import multiprocessing
import time

# Simulating file reading and writing task
def io_task(process_id, file_name):
    start_time = time.time()
    with open(file_name, "a") as f:
        f.write(f"Data written by process {process_id}\n")
    end_time = time.time()
    print(f"Process {process_id} finished in {end_time - start_time:.4f} seconds.")

# Number of processes and file name
num_processes = 5
file_name = "process_output.txt"

# Timing measurement
start_time = time.time()

processes = []
for i in range(num_processes):
    process = multiprocessing.Process(target=io_task, args=(i + 1, file_name))
    processes.append(process)
    process.start()

# Wait for all processes to complete
for process in processes:
    process.join()

end_time = time.time()
print(f"Total time for processes: {end_time - start_time:.4f} seconds.")
