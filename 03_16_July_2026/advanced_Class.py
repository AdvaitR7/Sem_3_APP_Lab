from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model   

    def get_model(self):
        return self._model

    @abstractmethod
    def display_info(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_info(self):
        print("Car Brand :", self.brand)
        print("Model     :", self.get_model())
        print("Seats     :", self.seats)


class Bike(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc

    def display_info(self):
        print("Bike Brand :", self.brand)
        print("Model      :", self.get_model())
        print("Engine CC  :", self.cc)


print("====== Car Details ======")
c1 = Car("Tesla", "Model S", 5)
c1.display_info()

print("\n====== Bike Details ======")
b1 = Bike("Yamaha", "RX100", 100)
b1.display_info()




# #OUTPUT

# ====== Car Details ======
# Car Brand : Tesla
# Model     : Model S
# Seats     : 5

# ====== Bike Details ======
# Bike Brand : Yamaha
# Model      : RX100
# Engine CC  : 100