# Import the ElectricVehicle class from its module
from ElectricVehicle import ElectricVehicle

# Import the GasolineVehicle class from its module
from GasolineVehicle import GasolineVehicle

# Define the HybridVehicle class that inherits from both ElectricVehicle and GasolineVehicle
class HybridVehicle(ElectricVehicle, GasolineVehicle):

    # The constructor method initializes the HybridVehicle object
    # It receives parameters related to the vehicle, battery, motor, and fuel tank
    def __init__(self, type, brand, year, model, battery_model, battery_status, motor_model, fuel_tank_status):
        
        # These attributes are common to all vehicles, so we set them here
        self.type = type
        self.brand = brand
        self.year = year
        self.model = model
        
        # Initialize the electric vehicle part by calling its constructor
        # Pass the battery-specific parameters to ElectricVehicle's __init__
        ElectricVehicle.__init__(self, type, brand, year, model, battery_model, battery_status)
        
        # Initialize the gasoline vehicle part by calling its constructor
        # Pass the motor and fuel tank specific parameters to GasolineVehicle's __init__
        GasolineVehicle.__init__(self, type, brand, year, model, motor_model, fuel_tank_status)
    
    # This method prints out the information of the hybrid vehicle in a clean format
    def print_self(self):
        print(
            f' Type: {self.type}\n'                    # Print vehicle type
            f' Brand: {self.brand}\n'                  # Print vehicle brand
            f' Year: {self.year}\n'                    # Print year of manufacture
            f' Model: {self.model}\n'                  # Print model name or number
            f' Battery: {self.battery_model}\n'       # Print battery model (from ElectricVehicle)
            f' Battery status(%): {self.battery_status}\n'  # Print battery charge status percentage
            f' Motor: {self.motor_model}\n'            # Print motor model (from GasolineVehicle)
            f' Deposit(L): {self.fuel_tank_status}\n' # Print amount of fuel in tank (liters)
        )
