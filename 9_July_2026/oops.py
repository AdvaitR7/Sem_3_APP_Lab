class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


c1 = Car("Toyota", "Fortuner")
c1.display()

'''
Brand: Toyota
Model: Fortuner
'''