# Inheritance allows a class (child class) to inherit attributes and methods
# from another class (parent class), promoting code reuse and creating
# a hierarchy between classes.

# Import the HybridVehicle class which inherits from ElectricVehicle and GasolineVehicle
from HybridVehicle import HybridVehicle

# Create an instance of HybridVehicle with the following attributes:
# 'car' is the type,
# 'bmw' is the brand,
# 2025 is the manufacturing year,
# 'IX_Hybrid' is the model,
# 'Super Battery' is the battery model,
# 20 is the initial battery charge percentage,
# 'Super Motor' is the motor model,
# 30 is the initial fuel tank level in liters.
hybrid_car = HybridVehicle('car', 'bmw', 2025, 'IX_Hybrid', 'Super Battery', 20, 'Super Motor', 30)

# Print all details of the hybrid car
hybrid_car.print_self()

# Call the method inherited from ElectricVehicle to charge the battery fully
hybrid_car.charge_battery()

# Call the method inherited from GasolineVehicle to fill the fuel tank
hybrid_car.fill_deposit()

# Print the updated details after charging battery and filling fuel tank
hybrid_car.print_self()
