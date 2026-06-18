class vehicle:
    
    def start(self):
        print("Vehicle Started")

    def __init__(self, brand, price, color):
        self.brand= brand
        self.price=price
        self.color=color
    
    def vehicle_details(self):
        print(f"Brand :{self.brand }")
