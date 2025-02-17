# Example of abstrection through car example.

class car():
    def __init__(self):
     self.acceleration = False,
     self.brake = False,
     self.steering = False,

    def starting_car(self):
        self.acceleration = True
        self.brake = False
        self.steering = True
        return "Car is starting..."

car1 = car()
print(car1.starting_car())


#* all the implementation details are hidden from the user.such as acceleration, brake, steering etc.
#* The user does not need to know how the car is starting, he just needs to know that the car is starting.
#* conclision is that abstrection is a way to hide the implementation details and show  only the functionality to the user.