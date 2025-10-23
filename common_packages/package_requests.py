"""
HTTP Request Examples with the `requests` Library
-------------------------------------------------
This script demonstrates how to:
  1. Send a GET request (retrieve data)
  2. Send a POST request (submit data)
  3. Include query parameters in a GET request
  4. Handle errors gracefully using raise_for_status()

Libraries Used:
    - requests: Simplifies making HTTP requests in Python
"""

import requests

# ----------------------------------------------------------------------
# 1️⃣  GET REQUEST — Retrieve Public GitHub Events
# ----------------------------------------------------------------------
print("\n=== GET Request to GitHub API ===")

# Send a GET request to GitHub's public events API
response_get = requests.get("https://api.github.com/events")

# Print HTTP status code (200 = OK, 404 = Not Found, etc.)
print("Status Code:", response_get.status_code)

# Print part of the response body (text)
print("Response Text (first 300 chars):")
print(response_get.text[:300])  # Print only a snippet to avoid clutter

# Show available attributes/methods on the response object
print("Available attributes and methods:", dir(response_get))


# ----------------------------------------------------------------------
# 2️⃣  POST REQUEST — Send Data to a Test API
# ----------------------------------------------------------------------
print("\n=== POST Request to httpbin.org ===")

# Data to send in the POST request body
data = {'key': 'value'}

# Send POST request to httpbin (it just echoes what you send)
response_post = requests.post('https://httpbin.org/post', data=data)

print("Status Code:", response_post.status_code)
print("Response JSON:")
print(response_post.json())  # httpbin returns JSON, so use .json() instead of .text

print("Available attributes and methods:", dir(response_post))


# ----------------------------------------------------------------------
# 3️⃣  GET REQUEST WITH QUERY PARAMETERS
# ----------------------------------------------------------------------
print("\n=== GET Request with Query Parameters ===")

# Define query parameters (these appear in the URL as ?key1=value1&key2=value2)
payload = {'key1': 'value1', 'key2': 'value2'}

response_get_with_params = requests.get('https://httpbin.org/get', params=payload)

print("Status Code:", response_get_with_params.status_code)
print("Response JSON:")
print(response_get_with_params.json())

print("Available attributes and methods:", dir(response_get_with_params))


# ----------------------------------------------------------------------
# 4️⃣  ERROR HANDLING — Raise Exceptions for Bad Responses
# ----------------------------------------------------------------------
print("\n=== Error Handling Example ===")

try:
    response_check = requests.get("https://api.github.com/events")
    # Will raise HTTPError if response code is 4xx or 5xx
    response_check.raise_for_status()
    print("Request succeeded! ✅")
except requests.exceptions.HTTPError as e:
    print("HTTP error occurred:", e)
except requests.exceptions.RequestException as e:
    print("Other request error occurred:", e)

# ----------------------------------------------------------------------
# ✅ END OF SCRIPT
# ----------------------------------------------------------------------
print("\nAll requests completed successfully.")
