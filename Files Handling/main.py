# =========================
# Python File & JSON Handling Basics
# =========================

import os
import json

# 1. Open a file
# Modes: 'r'=read, 'w'=write, 'a'=append, 'rb'=read binary, 'wb'=write binary
f = open("example.txt", "r")

# 2. Read from a file
content = f.read()          # entire file
lines = f.readlines()       # list of lines
line = f.readline()         # single line
f.close()                   # always close or use 'with'

# 3. Write to a file
with open("example.txt", "w") as f:
    f.write("Hello World\n")
    f.writelines(["Line1\n", "Line2\n"])

# 4. Append to a file
with open("example.txt", "a") as f:
    f.write("Appending new line\n")

# 5. Read & write JSON
data = {"name": "Alice", "age": 30, "skills": ["Python", "ML"]}

# Write JSON to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)   # indent=4 for pretty formatting

# Read JSON from file
with open("data.json", "r") as f:
    loaded_data = json.load(f)
print(loaded_data["name"])  # access JSON fields

# Convert JSON string to Python dict
json_str = '{"city": "Paris", "population": 2148327}'
parsed = json.loads(json_str)

# Convert Python dict to JSON string
json_text = json.dumps(data, indent=2)

# 6. Binary files (images, etc.)
with open("image.png", "rb") as f:
    data = f.read()
with open("copy.png", "wb") as f:
    f.write(data)

# 7. File existence & info
exists = os.path.exists("example.txt")
size = os.path.getsize("example.txt")

# 8. Deleting a file
# os.remove("example.txt")

# =========================
# Tips:
# - Always use 'with' to auto-close files
# - Use 'try/except' for safe handling
# - 'r+' allows read & write
# - json.load() / json.dump() for files
# - json.loads() / json.dumps() for strings
# =========================
