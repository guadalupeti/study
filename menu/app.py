from restaurant import Restaurant
from drink import Drink
from item_menu import ItemMenu
from food import Food
from dessert import Dessert

pizza = Restaurant('Pizza Place', 'Pizzeria')
coca = Drink('Coca-Cola', 7.0,'Big')
pepperoni = Food('Pepperoni Pizza', 50.0, ', delicious extra-thin dough, mozzarella and pepperoni.')
cake = Dessert('Super Chocolate Cake', 30, 'Big')


pizza.addItem(pepperoni)
pizza.addItem(coca)
pizza.addItem(cake)
coca.applyDiscount(0.2)




def main():
    pizza.showMenu

if __name__ == '__main__':
    main()