class Bike(object):

    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "Price is: $" + str(self.price)
        print "Max speed: " + str(self.max_speed) + "Mph"
        print "Total miles:" + str(self.miles)
        return self

    def ride(self):
        print "Riding" 
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
        return self

bike1 = Bike(10, 120)
bike1.ride().ride().ride().reverse().displayinfo()

bike2 = Bike(55, 200)
bike2.ride().ride().reverse().reverse().displayinfo()

bike3 = Bike(44, 300)
bike3.reverse().reverse().reverse().displayinfo()

