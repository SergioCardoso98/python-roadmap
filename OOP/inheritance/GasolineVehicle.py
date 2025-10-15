# Define the GasolineVehicle class representing a gasoline-powered vehicle
class GasolineVehicle:
    
    # Constructor method to initialize a GasolineVehicle object
    # It takes parameters for general vehicle attributes plus motor and fuel info
    def __init__(self, type, brand, year, model, motor_model, fuel_tank_status):
        self.type = type                # Type of vehicle (e.g., car, truck, SUV)
        self.brand = brand              # Brand or manufacturer name
        self.year = year                # Year of manufacture
        self.model = model              # Model name or number
        self.motor_model = motor_model  # Motor/engine model used in the vehicle
        self.fuel_tank_status = fuel_tank_status  # Fuel amount in the tank (liters)
    
    # Method to print out the vehicle's details in a readable format
    def print_self(self):
        print(
            f' Type: {self.type}\n'
            f' Brand: {self.brand}\n'
            f' Year: {self.year}\n'
            f' Model: {self.model}\n'
            f' Motor: {self.motor_model}\n'
            f' Deposit(L): {self.fuel_tank_status}\n'  # Fuel tank level in liters
        )
    
    # Method to simulate filling the fuel tank to a fixed capacity (50 liters)
    def fill_deposit(self):
        self.fuel_tank_status = 50  # Set fuel tank status to 50 liters (full tank assumption)
        print(f'Deposit filled to {self.fuel_tank_status}L\n')  # Confirm the fuel tank is full
