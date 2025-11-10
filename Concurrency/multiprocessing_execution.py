import multiprocessing  # Needed for creating and managing multiple processes
import time  # Used to simulate work and measure execution time

# This is the function that each process will run
start_time = time.time()  # Record start time

def do_something():
    print('Starting to do something')
    time.sleep(2)  # Simulate a task that takes 2 seconds
    print('Finished doing something')

# The if __name__ == "__main__" block is essential for multiprocessing,
# especially on Windows and macOS where the 'spawn' start method is used.
# Without this, the child processes will try to re-run the top-level code,
# causing infinite process creation or runtime errors.
if __name__ == "__main__":
    processes_list = []  # Keep track of all created processes

    # Create 5 separate processes
    for _ in range(5):
        # Create a Process object targeting the 'do_something' function
        p = multiprocessing.Process(target=do_something)
        p.start()  # Start the process: it runs 'do_something' in parallel
        processes_list.append(p)  # Add process to the list for later joining

    # Wait for all processes to finish
    for process in processes_list:
        process.join()  # Blocks until the individual process is done

    # This line runs only in the main process, after all child processes complete
    print('All somethings were done')
    end_time = time.time()  # Record end time
    print(f"Execution time: {end_time - start_time:.6f} seconds")


#Key Notes
#do_something() is only executed in the child process when p.start() is called.
#The top-level code (loop creating processes) must not run in the child process, hence the if __name__ == "__main__": guard.
#process.join() ensures the main process waits for each child before printing the final message.
#Each process runs completely independently — they don’t share memory unless explicitly set up

# note:
# Do NOT name this script 'multiprocessing.py' or any other name that clashes with
# standard library modules (like 'time.py', 'os.py', etc.).
# If you do, Python may import your script instead of the built-in 'multiprocessing' module,
# which will cause errors such as:
# AttributeError: module 'multiprocessing' has no attribute 'Process'
# or ImportError when other modules try to import 'multiprocessing'.
# Always use a unique, descriptive filename like 'my_multiprocessing_test.py'.