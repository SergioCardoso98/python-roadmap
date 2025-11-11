"""
===============================================================
Process Cleanup: multiprocessing vs ProcessPoolExecutor
===============================================================

Feature / Action            | multiprocessing            | ProcessPoolExecutor           | Notes
----------------------------|---------------------------|-------------------------------|---------------------------------------
Start process               | p.start()                 | Automatically on submit()     | submit() schedules the task; pool starts workers
Wait for completion         | p.join()                  | as_completed() or result()    | join() blocks until process finishes; as_completed() yields results as they complete
Clean up system resources   | Yes, after join()         | Automatically at end of 'with'| join() prevents zombie processes; 'with' cleans up all workers
Force stop / kill a process | p.terminate() + p.join()  | executor.shutdown(wait=True)  | terminate stops process; shutdown ensures proper cleanup
Automatic exception handling| ❌ Must handle manually    | ✅ Handled inside 'with'      | Even if a task fails, 'with' cleans up workers
Manual resource management  | Needed for files, sockets | Still needed for non-process resources | Both require cleanup of external resources
Zombie processes if skipped | Likely if join() is skipped | No, context manager handles it | Skipping join() leaves zombie processes in OS

Key Takeaways:
1. join() → waits for process and lets OS reclaim system resources (PID, memory), preventing zombies.
2. terminate() → forcibly stops a process if stuck; always call join() after to fully clean up.
3. ProcessPoolExecutor + with → automatically handles starting, waiting, and cleaning for all worker processes.
4. External resources (files, sockets, DB connections) must still be cleaned manually.
"""
