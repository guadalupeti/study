from rating import Rating
from item_menu import ItemMenu

class Restaurant:
    restaurants = []
    def __init__(self,name,type):
        self._name = name.title()
        self.type = type.upper()
        self._active = False
        self._rating = []
        self._menu = []
        Restaurant.restaurants.append(self)


    def __str__(self):
        return f'Name: {self._name} | Type: {self.type}'
    @classmethod
    def list(cls):
        print(f'{'Name'.ljust(25)} | {'Type'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant.type.ljust(25)} | {restaurant.sit.ljust(25)}')
            if len(restaurant._rating) != 0:
                print(f'Ratings: {'⭐'*(restaurant.averageRating)}')
            else:
                print('\033[31mReviews were not found!\033[m')
            

    @property
    def sit(self):
        return '☑' if self._active else '☐'
    
    @property
    def alternate(self):
        self._active = not self._active

    def addRating(self, name, rate):
        r = Rating(name,rate)
        self._rating.append(r)
    @property
    def averageRating(self):
        if not self._rating:
            return 0
        else:
            grade_sum = sum(rating._rate for rating in self._rating)
            
        people = len(self._rating)
        average = round(grade_sum/people)

        return average


    def addItem(self,item):
        if isinstance(item,ItemMenu):
            self._menu.append(item)
    @property
    def showMenu(self):
        print(f'{self._name} Menu')
        for n,item in enumerate(self._menu):
            if hasattr(item, 'size'):
                msg = f'{n + 1} - {item.name} | ${item.price:.2f} | Size: {item.size}'
            else:
                msg = f'{n + 1} - {item.name} | ${item.price:.2f} | Description: {item.desc}'
            print(msg)
