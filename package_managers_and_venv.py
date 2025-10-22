# ============================================
# Understanding the virtual environment in 
# package_managers_and_venv folder
# ============================================

# 1. What is the virtual environment here?
# -----------------------------------------
# In your folder "package_managers_and_venv", you created a venv named
# "package_managers_and_venv" (or similar). This creates an isolated Python 
# environment inside that folder.

# 2. Directory structure created:
# -------------------------------
# Inside "package_managers_and_venv", you'll find:
#
#   package_managers_and_venv/
#       bin/ (on macOS/Linux) or Scripts\ (on Windows)  
#           - contains the Python executable and scripts like pip
#       lib/ or Lib/ 
#           - stores installed Python packages for this environment
#       include/ (on Unix-like systems)
#           - headers for compiling extensions
#       pyvenv.cfg 
#           - configuration file with info like Python version and base interpreter path
#
# This structure is self-contained so packages you install here won’t affect
# your system Python or other projects.

# 3. Python executable inside the venv:
# -------------------------------------
# When you run `which python3` inside the activated environment, you get:
# 
#   /Users/ctw04025/PersonalLearning/python-roadmap/package_managers_and_venv/bin/python3
#
# This is the Python interpreter inside your venv.
# 
# Important:
# - This executable is usually a "copy" or a "symlink" of the system Python executable.
#
# What’s a symlink?
# -----------------
# - A symlink (symbolic link) is like a shortcut or alias to another file.
# - It points to the original file but doesn’t duplicate it.
# - Think of it like a "soft link" — if the original changes, the symlink reflects that.
# - On Unix/macOS, you can see symlinks using `ls -l`.
#
# Why use a symlink or copy?
# --------------------------
# - Using symlinks saves disk space and keeps the venv lightweight.
# - Sometimes a copy is used for portability or compatibility reasons.
#
# You can check which one is used by:
#   ls -l /Users/ctw04025/PersonalLearning/python-roadmap/package_managers_and_venv/bin/python3

# 4. Activation of the venv:
# --------------------------
# When you activate the virtual environment:
# 
#   source package_managers_and_venv/bin/activate
#
# The shell modifies your PATH environment variable so the venv’s bin directory
# is searched first.
#
# This means running `python3` or `pip` calls the venv’s Python and pip,
# isolating your project dependencies from the system-wide Python.

# 5. What happens when you install packages with pip inside this venv?
# --------------------------------------------------------------------
# - Packages get installed inside the venv’s lib/site-packages folder.
# - They are NOT available globally, preventing conflicts.
# - pip, setuptools, and wheel are pre-installed inside the venv, so you can
#   immediately install packages without any extra setup.

# 6. Deactivation:
# ----------------
# Run `deactivate` to return to your normal shell environment,
# which uses the system-wide Python again.

# 7. Why use venv in a project like package_managers_and_venv?
# -----------------------------------------------------------
# - To isolate dependencies for this specific project.
# - To avoid messing up global Python packages.
# - To make sure everyone working on this project uses the same versions.
# - To create a clean environment for testing package managers or Python tools.

# 8. Notes on Python versions:
# ----------------------------
# The venv uses whichever Python interpreter you ran `python -m venv` with.
# If you want a different Python version, you need to install it separately
# and then create a venv using that Python explicitly, e.g.:
# 
#   /path/to/python3.9 -m venv package_managers_and_venv

# 9. Extra tips:
# --------------
# - You can check your installed packages in the venv by running:
#     pip list
# - You can export your current environment’s packages to a requirements file:
#     pip freeze > requirements.txt
# - Recreate the environment on another machine by:
#     pip install -r requirements.txt

