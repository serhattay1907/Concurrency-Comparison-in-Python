import threading
import time

# SIR model simulation function
def sir_model_thread(thread_id, beta, gamma, population, infected, days):
    susceptible = population - infected
    recovered = 0

    # Simulation loop
    for day in range(1, days + 1):
        new_infected = (beta * susceptible * infected) / population
        new_recovered = gamma * infected

        susceptible -= new_infected
        infected += new_infected - new_recovered
        recovered += new_recovered

    print(f"Thread {thread_id} finished with {infected:.2f} infected and {recovered:.2f} recovered after {days} days.")

# Parameters
population = 1000  # Total population
infected = 10      # Initial infected
beta = 0.3         # Infection rate
gamma = 0.1        # Recovery rate
days = 100         # Days to simulate
num_threads = 4    # Number of threads

# Timing measurement
start_time = time.time()

threads = []
for i in range(num_threads):
    thread = threading.Thread(target=sir_model_thread, args=(i + 1, beta, gamma, population, infected, days))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

end_time = time.time()
print(f"Total time for threads: {end_time - start_time:.4f} seconds.")
