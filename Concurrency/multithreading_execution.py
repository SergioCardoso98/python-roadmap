# Import necessary modules
import time  # Used here to simulate delays and measure execution time
import threading  # Provides tools for running code concurrently using threads

# Record the start time of the entire program
start_time = time.time()

# Define a function that simulates doing some work for a given number of seconds
def do_something(seconds):
    print(f'Starting to do something for {seconds} seconds...')
    time.sleep(seconds)  # Pause execution for 'seconds' amount of time (simulating a time-consuming task)
    print(f'Finished doing something for {seconds} seconds...')

# This ensures that the code below only runs when this file is executed directly
# and NOT when imported as a module in another file.
if __name__ == "__main__":

    # A list of seconds that each task will take
    secs = [5, 4, 3, 2, 1]

    # Create a list of Thread objects.
    # Each thread will run the do_something function with a different argument from secs.
    tasks = [threading.Thread(target=do_something, args=(sec,)) for sec in secs]

    # Start all threads
    # This tells Python to begin executing each thread concurrently
    for t in tasks:
        t.start()

    # Wait for all threads to complete
    # join() blocks the main program until the thread has finished its work
    for t in tasks:
        t.join()  # Ensures the main thread waits for this thread to finish

    # After all threads are done, print a final message
    print('All somethings were done')

    # Record end time and calculate total execution time
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
