import asyncio
import time

# Record the start time of the entire program
start_time = time.time()

# ------------------------------
# Coroutine function
# ------------------------------
# A coroutine is a special kind of function that can pause execution (yield control)
# and resume later. It is defined with 'async def'. Under the hood, calling a coroutine
# does not execute it immediately. Instead, it returns a coroutine object that can be awaited.
# When you 'await' it, the event loop runs the coroutine until it hits another await
# or completes, allowing other coroutines to run in the meantime.
async def do_something(seconds):  
    print(f"[INFO] Starting task: simulate work for {seconds} seconds...")
    
    # asyncio.sleep is a coroutine that suspends execution without blocking the event loop
    await asyncio.sleep(seconds)
    
    # Return a result when done
    return f"[INFO] Finished task for {seconds} seconds"

# ------------------------------
# Sequential execution
# ------------------------------
async def main1():
    start_time_main1 = time.time()
    print("\n=== Running Main1: Sequential Execution ===")
    
    # Await each coroutine one by one; they run sequentially
    task1 = await do_something(3)
    task2 = await do_something(2)
    task3 = await do_something(1)
    
    # Print results
    print(task1)
    print(task2)
    print(task3)

    end_time_main1 = time.time()
    print(f"[TIME] Main1 completed in {end_time_main1 - start_time_main1:.2f} seconds\n")

# ------------------------------
# Concurrent execution with create_task
# ------------------------------
async def main2():
    start_time_main2 = time.time()
    print("\n=== Running Main2: Concurrent Execution with asyncio.create_task ===")
    
    secs = [3, 2, 1]
    # create_task schedules the coroutine to run concurrently
    tasks = [asyncio.create_task(do_something(sec)) for sec in secs]
    
    # Await each task to finish and print its result
    for t in tasks:
        await t
        print(t.result())

    end_time_main2 = time.time()
    print(f"[TIME] Main2 completed in {end_time_main2 - start_time_main2:.2f} seconds\n")

# ------------------------------
# Concurrent execution with gather
# ------------------------------
async def main3():
    start_time_main3 = time.time()
    print("\n=== Running Main3: Concurrent Execution with asyncio.gather ===")
    
    secs = [3, 2, 1]
    # asyncio.gather runs all coroutines concurrently and returns results in order
    results = await asyncio.gather(*(do_something(sec) for sec in secs))
    
    for r in results:
        print(r)

    end_time_main3 = time.time()
    print(f"[TIME] Main3 completed in {end_time_main3 - start_time_main3:.2f} seconds\n")

# ------------------------------
# Concurrent execution with TaskGroup (Python 3.11+)
# ------------------------------
async def main4():
    start_time_main4 = time.time()
    print("\n=== Running Main4: Concurrent Execution with asyncio.TaskGroup ===")
    
    secs = [3, 2, 1]
    results = []

    # TaskGroup ensures all tasks are awaited and cancels others if one fails
    async with asyncio.TaskGroup() as tg:
        for s in secs:
            task = tg.create_task(do_something(s))
            results.append(task)

    # Print results after all tasks are finished
    for r in results:
        print(r.result())

    end_time_main4 = time.time()
    print(f"[TIME] Main4 completed in {end_time_main4 - start_time_main4:.2f} seconds\n")
    
# ------------------------------
# Concurrent execution with Lock (safe shared resource modification)
# ------------------------------
# ------------------------------
# Quick note about Locks
# ------------------------------
# A Lock is used to prevent multiple coroutines from accessing the same shared resource at the same time.
# This is useful when you have data that could get corrupted if modified concurrently.
#
# Under the hood:
# - The Lock maintains an internal flag (locked/unlocked) and a queue of waiting coroutines.
# - When a coroutine tries `await lock.acquire()`, Python checks the flag:
#       - If unlocked: it sets the flag to locked and continues.
#       - If locked: the coroutine is paused and put in the queue until the lock is released.
# - When a coroutine calls `lock.release()`, the next coroutine in the queue is resumed.
# - Python does NOT compare lock objects like function names; each Lock instance is independent.
#
# Example usage:
shared_counter = 0  # shared resource
lock = asyncio.Lock()  # create a lock

async def increment():
    global shared_counter
    # Detailed explanation:
    # - `lock` is an asyncio.Lock() instance that acts as a gate for accessing the shared resource.
    # - When a coroutine reaches `async with lock`, it asks the lock for permission to proceed:
    #       1. If the lock is currently unlocked, the coroutine acquires it immediately and enters the block.
    #       2. If the lock is already locked by another coroutine, this coroutine is paused and placed in a waiting queue.
    # - While inside the `async with` block, no other coroutine can enter until the current one releases the lock.
    # - When the block is exited, the lock is automatically released, and the next waiting coroutine (if any) is resumed.
    #
    # This prevents race conditions: without the lock, two coroutines could read, modify, and write
    # `shared_counter` at the same time, leading to incorrect results.
    # Only one coroutine can enter this block at a time because they share this lock object.
    async with lock:
        temp = shared_counter
        await asyncio.sleep(0.1)  # simulate some work
        shared_counter = temp + 1
        print(f"Counter incremented to: {shared_counter}")

async def main5():
    start_time_main5 = time.time()
    print("\n=== Running Main5: Concurrent Increments with Lock ===")
    
    global shared_counter
    shared_counter = 0  # reset counter before starting

    # Run multiple increments concurrently
    await asyncio.gather(*(increment() for _ in range(5)))

    print(f"[INFO] Final counter value: {shared_counter}")

    end_time_main5 = time.time()
    print(f"[TIME] Main5 completed in {end_time_main5 - start_time_main5:.2f} seconds\n")


# ------------------------------
# Run the selected main function
# ------------------------------
# Uncomment any main function to test it individually

# asyncio.run(main1())
# asyncio.run(main2())
# asyncio.run(main3())
#asyncio.run(main4())
asyncio.run(main5())

print("\n[INFO] All tasks were completed")

# Record end time and total execution time
end_time = time.time()
print(f"[TIME] Total execution time: {end_time - start_time:.2f} seconds\n")

# ------------------------------
# Quick note about Futures
# ------------------------------
# A Future is like a placeholder for a result that isn’t ready yet.
# When you run a coroutine or task, it returns a Future.
# You can 'await' it to pause execution until the result is available.

