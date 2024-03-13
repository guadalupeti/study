from item_menu import ItemMenu

class Food(ItemMenu):
    def __init__(self, name, price, desc):
        super().__init__(name,price)
        self.desc = desc
    
    def __str__(self):
        return self.name
    
    def applyDiscount(self,disc):
        self.price -= (self.price * disc)