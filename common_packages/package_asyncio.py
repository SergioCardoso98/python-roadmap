import asyncio

async def greet_basic(name):
    print('Fecthing name')
    await asyncio.sleep(2)
    print(f'Hello {name}')

async def greet_extended(first_name, middle_names, last_name):
    print('Fetching full name')
    await asyncio.sleep(5)
    print(f'Hello {first_name + middle_names + last_name}')

async def main():
    await asyncio.gather(
        greet_extended('Abilio', ' Sergio Cardoso ', 'Fonseca'),
        greet_extended('Sofia', ' Marcia Joana ', 'Pastrana')
    )

asyncio.run(greet_basic('Abilio'))
asyncio.run(greet_basic('Sofia'))
asyncio.run(main())
