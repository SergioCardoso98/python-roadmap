# 🧠 Pathlib Study Script
# Learn: Path creation, expansion, existence check, file read/write, cwd/home usage

from pathlib import Path

# --- 1️⃣ Setup paths ---
# Expand '~' to full home directory
p = Path('~').expanduser()   # or simply: p = Path.home()

# Create a nested path for learning projects
python_roadmap = p / 'PersonalLearning' / 'python-roadmap'
print("Python roadmap path:", python_roadmap)

# Show available methods and attributes of Path objects (for exploration)
print("\nAvailable Path methods:")
print(dir(python_roadmap))

# --- 2️⃣ Check if a specific subdirectory exists ---
check_path_existence = python_roadmap / 'common_packages'
print("\nDoes 'common_packages' exist?", check_path_existence.exists())

# --- 3️⃣ Display important directories ---
current_working_dir = Path.cwd()
print("\nCurrent directory:", current_working_dir)

home_dir = Path.home()
print("Home directory:", home_dir)

# --- 4️⃣ (Optional) Create directories if missing ---
#check_path_existence.mkdir(parents=True, exist_ok=True)

# --- 5️⃣ Create and write to a text file ---
#file = check_path_existence / "python-roadmap.txt"
#file.write_text("1. Learn pathlib\n2. Practice file handling\n3. Master Python I/O")
#print("\nFile written:", file)

# --- 6️⃣ Read back the file contents ---
#content = file.read_text()
#print("\nFile contents:\n", content)

# --- 7️⃣ Attempt to read another file safely (e.g., pyvenv.cfg) ---
pyenv_file_to_read = check_path_existence / 'pyvenv.cfg'
print("\nAttempting to read pyvenv.cfg...")

if pyenv_file_to_read.exists():
    print(pyenv_file_to_read.read_text())
else:
    print("⚠️ pyvenv.cfg not found at:", pyenv_file_to_read)

# --- ✅ Done ---
print("\n✅ Pathlib demo complete!")
