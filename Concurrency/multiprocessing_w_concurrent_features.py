# Import necessary modules
import concurrent
import concurrent.futures  # Provides tools for running code concurrently using threads or processes
import time  # Used here to simulate delays and measure execution time

# Record the start time of the entire program
start_time = time.time()

# Define a function that simulates doing some work for a given number of seconds
def do_something(seconds):
    print(f'Starting to do something for {seconds} seconds...')
    time.sleep(seconds)  # Pause execution for 'seconds' amount of time (simulating a time-consuming task)
    return f'Finished doing something for {seconds} seconds...'

# This ensures that the code below only runs when this file is executed directly
# and NOT when imported as a module in another file.
if __name__ == "__main__":

    # Use a ProcessPoolExecutor to run multiple processes in parallel
    # max_workers=5 means at most 5 processes will run at once
    #
    # The "with" statement here is a CONTEXT MANAGER:
    # - It automatically starts the ProcessPoolExecutor.
    # - It ensures that once the code block inside "with" finishes, 
    #   all worker processes are properly closed (cleaned up).
    # - This is safer than manually starting and shutting down the pool.
    #
    # In short: the "with" block manages setup and teardown automatically.
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:

        # A list of seconds that each task will take
        secs = [5, 4, 3, 2, 1]

        # Submit tasks to the executor pool.
        # Each call to executor.submit() schedules do_something(sec)
        # to run in a separate process and returns a Future object.
        results = [executor.submit(do_something, sec) for sec in secs]

        # as_completed() yields each Future as it finishes (not in submission order)
        # This allows results to print as soon as each task is done.
        for r in concurrent.futures.as_completed(results):
            print(r.result())  # Print the return value of do_something()

        # After all futures complete, this line runs in the main process
        print('All somethings were done')

        # Record end time and calculate total execution time
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
