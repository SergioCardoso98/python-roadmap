from dataclasses import dataclass, field

# Using @dataclass decorator to simplify class creation with built-in features
@dataclass  # frozen=True → makes the dataclass immutable | eq=False → disables automatic equality comparison
class DataclassExploration:
    # Normal attribute with a default value
    normal_assign: str = "Default_value"
    # Attribute that should be a list or dict, using default_factory to avoid mutable default argument issues
    list_or_dict_assign: list = field(default_factory=list)

    # __post_init__ runs automatically after the dataclass __init__ method
    def __post_init__(self):
        # Check if the normal_assign attribute is still the default value
        if self.normal_assign == "Default_value":
            print('Object initiated with default value')
        # Raise an error if list_or_dict_assign is empty
        if not self.list_or_dict_assign:
            raise ValueError('list_or_dict_assign can\'t be empty')

    # Custom method to describe the class (Doesnt bellong to DataClasses, its mine)
    def what_is_this(self):
        print('This is a class to test the dataclasses package')

# A regular Python class without dataclass features
class ClassWithoutDataclassPackage:
    def __init__(self):
        # Set some var
        self.value = "some value"

    def what_is_this(self):
        print('This is a class without using dataclasses package')


# Create an instance of DataclassExploration with a non-empty list
test = DataclassExploration(list_or_dict_assign=[1, 2, 3, 4, 5])
print('--- DataclassExploration ---')
test.what_is_this()  # Call method
print('Attributes and methods:', dir(test))  # dir shows all attributes and methods
print('Dataclass object representation:', test)  # Default __repr__ shows fields
print('-----------')

# Create an instance of the regular class
test2 = ClassWithoutDataclassPackage()
print('--- ClassWithoutDataclassPackage ---')
test2.what_is_this()  # Call method
print('Attributes and methods:', dir(test2))  # dir shows attributes and methods
print('Regular class object representation:', test2)  # Default __repr__ just shows object address
