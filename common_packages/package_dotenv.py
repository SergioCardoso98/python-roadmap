# --------------------------------------------
# Example: Using python-dotenv to manage environment variables
# --------------------------------------------

# Import the two main helpers from the dotenv package:
# - load_dotenv(): loads variables from .env into the system environment (os.environ)
# - dotenv_values(): reads variables directly from a .env file into a Python dictionary
from dotenv import load_dotenv, dotenv_values

# Import os to access environment variables stored in os.environ
import os


# --------------------------------------------
# 1. Read .env file into a Python dictionary
# --------------------------------------------
# dotenv_values() simply parses the .env file and returns key-value pairs as strings.
# It does NOT modify your system environment.
# Useful if you just want to directly access values without polluting os.environ.
config = dotenv_values('.env')


# --------------------------------------------
# 2. Load .env variables into the environment
# --------------------------------------------
# load_dotenv() reads the .env file and adds its variables to os.environ,
# which makes them accessible via os.getenv() or os.environ["VAR_NAME"].
load_dotenv()


# --------------------------------------------
# 3. Access variables from the environment
# --------------------------------------------
# os.getenv("PORT") retrieves the value of the PORT variable
# that was loaded into the environment by load_dotenv().
# If the variable doesn’t exist, it returns None instead of raising an error.
port = os.getenv("PORT")
print(port)  # should print the value of PORT from the .env file


# --------------------------------------------
# 4. Access variables directly from the config dictionary
# --------------------------------------------
# Here we print all the variables as they were read from the .env file.
# This shows the raw dictionary returned by dotenv_values().
# Example output: OrderedDict([('PORT', '3000'), ('DATABASE_URL', 'postgres://...')])
print(config)


#✅ Use dotenv_values() when you want local access only
#✅ Use load_dotenv() when you want system-wide access (for other libraries or dependencies)
#By default, dotenv_values('.env') looks for .env in the current working directory — not necessarily the script’s directory.