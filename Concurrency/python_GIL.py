
# Example: Demonstrating Python's Global Interpreter Lock (GIL)

# This script shows how the GIL affects performance in multi-threaded vs
# multi-process Python programs when performing a CPU-bound task.

# Run this file with:
#    python gil_demo.py


import threading
import multiprocessing
import time

# ---------------------------------------------------------------
# A CPU-bound task: computing the sum of squares up to n
# ---------------------------------------------------------------
def cpu_bound_task(n):
    total = 0
    for i in range(n):
        total += i * i
    return total


# ---------------------------------------------------------------
# Helper function to measure execution time
# ---------------------------------------------------------------
def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    print(f"{func.__name__} took {end - start:.2f} seconds")


# ---------------------------------------------------------------
# Run the CPU-bound task using multiple threads
# ---------------------------------------------------------------
def run_with_threads(n, num_threads):
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=cpu_bound_task, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


# ---------------------------------------------------------------
# Run the CPU-bound task using multiple processes
# ---------------------------------------------------------------
def run_with_processes(n, num_processes):
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=cpu_bound_task, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


# ---------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------
if __name__ == "__main__":
    N = 50_000_000     # size of computation
    THREADS = 4
    PROCESSES = 4

    print(f"\nRunning CPU-bound task ({N:,} iterations)...\n")

    # 1️⃣ Single-threaded baseline
    measure_time(cpu_bound_task, N)

    # 2️⃣ Multi-threaded version (affected by the GIL)
    measure_time(run_with_threads, N, THREADS)

    # 3️⃣ Multi-process version (true parallelism)
    measure_time(run_with_processes, N, PROCESSES)

    print("\nNote:")
    print("- Threads share one GIL → no real speed-up for CPU-bound tasks.")
    print("- Processes each have their own GIL → true parallel execution.")
