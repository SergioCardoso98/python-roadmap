# Define the ElectricVehicle class representing an electric vehicle
class ElectricVehicle:
    
    # Constructor method to initialize an ElectricVehicle object
    # It takes parameters for common vehicle attributes plus battery-specific info
    def __init__(self, type, brand, year, model, battery_model, battery_status):
        self.type = type                  # Type of vehicle (e.g., car, truck, SUV)
        self.brand = brand                # Brand or manufacturer name
        self.year = year                  # Year of manufacture
        self.model = model                # Model name or number
        self.battery_model = battery_model  # Battery model/type used in the vehicle
        self.battery_status = battery_status  # Battery charge status as a percentage (0-100)
    
    # Method to print out the vehicle's details in a readable format
    def print_self(self):
        print(
            f' Type: {self.type}\n'
            f' Brand: {self.brand}\n'
            f' Year: {self.year}\n'
            f' Model: {self.model}\n'
            f' Battery: {self.battery_model}\n'
            f' Battery status(%): {self.battery_status}\n'
        )
    
    # Method to simulate charging the battery to full capacity
    def charge_battery(self):
        self.battery_status = 100  # Set battery status to 100% (fully charged)
        print(f'Battery charged to {self.battery_status}%\n')  # Confirm the battery is fully charged
