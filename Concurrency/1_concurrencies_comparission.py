# ===============================================================
# Concurrency Comparison: Sync vs Multithreading vs Multiprocessing vs Asyncio
# ===============================================================
# 
# Feature / Aspect            | Synchronous (Sync)       | Multithreading              | Multiprocessing             | Asyncio (Async/Await)         | Notes / GIL Considerations
# ----------------------------|-------------------------|-----------------------------|-----------------------------|-------------------------------|----------------------------------------
# Execution Model             | Sequential, blocking    | Threads share memory, run concurrently | Separate processes, separate memory | Single-threaded, event loop, cooperative multitasking | Threads share memory; processes are isolated; asyncio uses single thread
# CPU-bound task efficiency   | Poor for CPU-heavy tasks | Limited by GIL → CPU-bound is inefficient | Excellent for CPU-bound tasks | Poor for CPU-bound tasks unless offloaded | GIL prevents multiple threads from executing Python bytecode simultaneously
# I/O-bound task efficiency   | Poor, blocks on I/O     | Good → threads can wait on I/O | Good → processes can do I/O independently | Excellent → event loop can handle many I/O tasks | Asyncio shines with high-latency I/O; threads also help for I/O
# Memory usage                | Minimal, single process | Low → threads share memory | Higher → each process has own memory | Minimal → single thread, coroutines | Processes duplicate memory; threads are lightweight
# Start / cleanup overhead    | Minimal                 | Low                         | Higher → OS spawns processes | Minimal → just start event loop | Process start is expensive; thread start is cheap
# Ease of programming         | Easiest                 | Medium → need locks for shared data | Medium → need IPC/queues for sharing | Medium → async/await syntax, event loop management | Threads need locks to avoid race conditions
# Task granularity            | Coarse, sequential      | Medium → threads suitable for parallel I/O tasks | Coarse → CPU-heavy tasks or isolated work | Fine → many small async tasks | Choose based on task size and parallelism
# Error / Exception handling  | Simple                  | Medium → exceptions propagate to thread only | Medium → exceptions need catching via join / queues | Medium → exceptions in coroutines must be awaited and handled | Multiprocessing exceptions need careful handling
# When to use                 | Small scripts, simple tasks | I/O-heavy tasks, GUIs, network requests | CPU-heavy tasks, parallel data processing | High-concurrency I/O tasks (networking, web scraping) | GIL limits CPU concurrency for threads, not processes
# Zombie processes risk       | ❌ None                 | ❌ Low                      | ✅ Possible if not joined properly | ❌ None, handled by event loop | Always join processes to prevent zombies
# Automatic cleanup           | ✅                      | ❌ Need manual thread management | ❌ Need manual process join/terminate | ✅ Event loop handles coroutines | Threads & processes may require manual cleanup for external resources
