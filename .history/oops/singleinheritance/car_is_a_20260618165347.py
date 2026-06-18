from vehicle_is_a import vehicle

class car(vehicle):

    def drive(self):
        print("Car is driving")

    def car_details(self):
        print("Car details are:")
        super().vehicle_details()
        print("Thank for enquiry")

#parent class para con called directly from child class after creating child class object and values of all parameters
#got assigned to parent class con which are directly passed from child class while object creation of child class
c= car("Mercedes", 5000000, "White")
c.start()
c.drive()
c.car_details()


#c= car("Mercedes", 5000000, "White")= parent class para con is called auto from child class objkect craetion and we passed the values to parameters of that con from here only
# Vehicle Started = parent class instance method called 
# Car is driving = child class instance method called 
# Car details are:= child class instance method called 
# Brand :Mercedes price: 5000000 color:White  #parent class instance method called 
# Thank for enquiry = child class instance method called 


c= car("BMW", 5000000, "White")
c.start()
c.drive()
c.car_details()