class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0


    
    def display_all(self):
        print "Price:" + str(self.price)
        print "Speed" + str(self.speed) + "mph"
        print "Fuel:" + str(self.fuel)
        print "Mileage" + str(self.mileage) + "mph"
        if self.price <= 10000:
            print "Tax: 12%"
        else:
            print "Tax: 15%"
        return self

car1 = Car(20000, 35, "Full", 15)
car1.display_all()
    