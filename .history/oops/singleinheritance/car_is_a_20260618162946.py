from vehicle_is_a import vehicle

class car(vehicle):

    def drive(self):
        print("Car is driving")

    def car_details(self):
        print("Car details are:")
        super().vehicle_details()
        print("Thank for enquiry")

#parent class para con called directly from child class after creating child class object and values of all parameters
#got assigned to parent class con 
c= car("Mercedes", 5000000, "White")
c.start()
c.drive()
c.car_details()