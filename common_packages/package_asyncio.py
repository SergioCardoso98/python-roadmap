import asyncio  # Import the asyncio module for asynchronous programming

# Define an asynchronous function that greets a user by name
async def greet_basic(name):
    print('Fetching name')  # Prints a message immediately (non-blocking)
    await asyncio.sleep(2)  # Pause this coroutine for 2 seconds (simulate waiting)
    print(f'Hello {name}')  # After waiting, print the greeting

# Define another asynchronous function that takes a full name (first, middle, last)
async def greet_extended(first_name, middle_names, last_name):
    print('Fetching full name')  # Inform that the full name is being processed
    await asyncio.sleep(5)  # Pause this coroutine for 5 seconds (simulate longer waiting)
    # Concatenate the full name and print the greeting
    print(f'Hello {first_name + middle_names + last_name}')

# Define the main coroutine that runs multiple async tasks concurrently
async def main():
    # asyncio.gather() allows multiple coroutines to run at the same time
    await asyncio.gather(
        greet_extended('Abilio', ' Sergio Cardoso ', 'Fonseca'),
        greet_extended('Sofia', ' Marcia Joana ', 'Pastrana')
    )

# Run the asynchronous greet_basic function for 'Abilio'
asyncio.run(greet_basic('Abilio'))

# Run the asynchronous greet_basic function for 'Sofia'
asyncio.run(greet_basic('Sofia'))

# Run the main coroutine, which executes two greet_extended coroutines concurrently
asyncio.run(main())
