import threading
import time
import random

# Number of philosophers
NUM_PHILOSOPHERS = 5

# Number of chopsticks (forks)
NUM_CHOPSTICKS = NUM_PHILOSOPHERS

# List to represent chopsticks
chopsticks = [threading.Lock() for _ in range(NUM_CHOPSTICKS)]

# Function for philosopher behavior
def philosopher(philosopher_id):
    while True:
        # Thinking
        print(f'Philosopher {philosopher_id} is thinking.')
        time.sleep(random.uniform(1, 3))

        # Start eating
        print(f'Philosopher {philosopher_id} is hungry and trying to pick up chopsticks.')
        chopstick1 = chopsticks[philosopher_id]
        chopstick2 = chopsticks[(philosopher_id + 1) % NUM_PHILOSOPHERS]

        # Attempt to pick up chopsticks
        chopstick1.acquire()
        chopstick2.acquire()

        # Eating
        print(f'Philosopher {philosopher_id} is eating.')
        time.sleep(random.uniform(2, 4))

        # Release chopsticks after eating
        chopstick1.release()
        chopstick2.release()

        # Finish eating
        print(f'Philosopher {philosopher_id} finished eating and returned to thinking.')

# Create and start philosopher threads
philosopher_threads = []
for i in range(NUM_PHILOSOPHERS):
    philosopher_threads.append(threading.Thread(target=philosopher, args=(i,)))
    philosopher_threads[-1].start()

# Wait for all philosopher threads to finish
for thread in philosopher_threads:
    thread.join()
