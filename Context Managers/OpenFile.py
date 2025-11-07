# ---------------------------------------------------------
# Custom Context Manager Example in Python
# ---------------------------------------------------------

# A context manager in Python is a tool that sets something up,
# lets you use it safely, and then automatically cleans it up.
# This ensures resources (like files) are properly closed even if an error occurs.

# ---------------------------------------------------------
# Step 1: Define a custom context manager class
# ---------------------------------------------------------

class OpenFile:
    def __init__(self, path, mode):
        #Initialize the context manager.
        #Parameters:
        #- path: The file path to open
        #- mode: The mode to open the file ('r', 'w', 'a', etc.)
        self.file_path = path
        self.mode = mode
        self.file = None  # Will hold the file object

    def __enter__(self):
        #This method is called when entering the 'with' block.
        #It opens the file and returns the file object so it can be used inside the block.
        print(f"[ENTER] Opening file '{self.file_path}' in mode '{self.mode}'")
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        #This method is called when exiting the 'with' block.
        #It closes the file, ensuring cleanup even if an exception occurred.
        #Parameters:
        #- exc_type: The type of exception (if any)
        #- exc_val: The value of the exception (if any)
        #- traceback: The traceback object (if any)
        
        if self.file:
            self.file.close()
            print(f"[EXIT] File '{self.file_path}' closed")
        if exc_type:
            # This block runs if an exception occurred inside the 'with' block
            print(f"[EXIT] An exception occurred: {exc_val}")
        # Returning False (or None) lets exceptions propagate if they happened
        return False


