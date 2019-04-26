# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle is lowest level class


class Vehicle:
    def __init__(self):
        pass

# Vehicle is GroundVehicle's base class


class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

# Ground Vehicle is Car's base class


class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass

# Ground Vehicle is Motorcycle's base class


class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass

# Vehicle is FlightVehicle's base class


class FlightVehicle(Vehicle):
    def __init(self):
        super().__init__()
        pass

# Flight Vehicle is Airplane's base class


class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass

# FlightVehicle is Starship's base class


class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass
