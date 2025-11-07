from OpenFile import OpenFile

# ---------------------------------------------------------
# Step 2: Use the custom context manager
# ---------------------------------------------------------

# Using the custom context manager to write to a file
with OpenFile('./Context Managers/guinea_pig_text_file.txt', 'w') as f:
    # Inside this block, 'f' is the open file object
    # We can safely write to it
    print("[WITH BLOCK] Writing to file...")
    f.write('Written inside the Custom Context Manager class\n')

# Step 3: Check if the file is closed after exiting the 'with' block
print(f"[AFTER WITH] Is file closed? {f.closed}")

#Usefull for 
# Managing file operations safely (open, read, write, close)
# Handling database connections to ensure they are properly closed
# Acquiring and releasing threading or multiprocessing locks
# Managing network sockets to ensure they are closed after use
# Temporarily changing working directories
# Managing temporary files or directories
# Opening and safely closing hardware resources (e.g., serial ports, cameras)
# Starting and stopping timers for performance measurement
# Setting up and tearing down logging configurations
# Managing transactions in databases with commit/rollback on exit
# Handling resource-intensive objects that require explicit cleanup (e.g., GPU memory)
# Suppressing exceptions in specific code blocks
# Redirecting stdout or stderr temporarily
# Managing HTTP sessions for requests to ensure proper cleanup
# Managing context-specific configurations (like changing environment variables temporarily)
# Resource pooling, e.g., acquiring a connection from a pool and releasing it automatically
