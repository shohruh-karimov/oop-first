# №1

# class Device:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def turn_on(self):
#         print("Device is turned on.")
#
#     def turn_off(self):
#         print("Device is turned off.")
#
#
# class CoffeeMachine(Device):
#     def __init__(self, brand, model, capacity):
#         super().__init__(brand, model)
#         self.capacity = capacity
#
#     def make_coffee(self):
#         print("Coffee is being made.")
#
#
# class Blender(Device):
#     def __init__(self, brand, model, power):
#         super().__init__(brand, model)
#         self.power = power
#
#     def blend(self):
#         print("Blending...")
#
#
# class MeatGrinder(Device):
#     def __init__(self, brand, model, speed):
#         super().__init__(brand, model)
#         self.speed = speed
#
#     def grind_meat(self):
#         print("Meat is being ground.")
#
#
# coffee_machine = CoffeeMachine("Philips", "HD7461", 1.5)
# coffee_machine.turn_on()
# coffee_machine.make_coffee()
# coffee_machine.turn_off()
#
# blender = Blender("KitchenAid", "KSB560", 800)
# blender.turn_on()
# blender.blend()
# blender.turn_off()
#
# meat_grinder = MeatGrinder("Kenwood", "MG510", 2000)
# meat_grinder.turn_on()
# meat_grinder.grind_meat()
# meat_grinder.turn_off()

# №2

class Ship:
    def __init__(self, name, displacement):
        self.name = name
        self.displacement = displacement

    def sail(self):
        print(f"{self.name} is sailing.")

    def anchor(self):
        print(f"{self.name} is anchoring.")


class Frigate(Ship):
    def __init__(self, name, displacement, missile_count):
        super().__init__(name, displacement)
        self.missile_count = missile_count

    def fire_missiles(self):
        print(f"{self.name} is firing missiles.")


class Destroyer(Ship):
    def __init__(self, name, displacement, torpedo_count):
        super().__init__(name, displacement)
        self.torpedo_count = torpedo_count

    def launch_torpedoes(self):
        print(f"{self.name} is launching torpedoes.")


class Cruiser(Ship):
    def __init__(self, name, displacement, aircraft_count):
        super().__init__(name, displacement)
        self.aircraft_count = aircraft_count

    def launch_aircraft(self):
        print(f"{self.name} is launching aircraft.")


frigate = Frigate("Frigate1", 5000, 20)
frigate.sail()
frigate.fire_missiles()
frigate.anchor()

destroyer = Destroyer("Destroyer1", 8000, 10)
destroyer.sail()
destroyer.launch_torpedoes()
destroyer.anchor()

cruiser = Cruiser("Cruiser1", 10000, 5)
cruiser.sail()
cruiser.launch_aircraft()
cruiser.anchor()