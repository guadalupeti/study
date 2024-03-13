from item_menu import ItemMenu

class Dessert(ItemMenu):
    def __init__(self,name, price,size):
        super().__init__(name,price)
        self.size = size
    
    def applyDiscount(self, disc):
        self.price -= (self.price * disc)