from abc import ABC, abstractmethod

class ItemMenu:
    def __init__(self,name,price):
        self.name = name
        self.price = float(price)

    @abstractmethod
    def applyDiscount(self,disc):
        pass
        