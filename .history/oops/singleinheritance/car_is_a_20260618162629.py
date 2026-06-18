from vehicle_is_a import vehicle

class car(vehicle):

    def drive(self):
        print("Car is driving")

    def car_details(self):
        print("Car details are:")
        super().vehicle_details