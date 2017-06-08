class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status = "for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    
    def sell(self):
        self.status = "sold"
        print self.status
        return self

    
    def displayinfo(self):
        print "Price: $" + str(self.price)
        print "Item Name" + str(self.item_name)
        print "Weight:" + str(self.weight)
        print "Brand" + str(self.brand)
        print "Cost: $" + str(self.cost)
        print "Status:" + str(self.status)
        return self


product1 = Product(10,"Phone",5,"Apple",2)
product1.sell().displayinfo()

