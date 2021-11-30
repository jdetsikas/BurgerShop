# Implementing a burger shop


class FoodItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class Burger(FoodItem):

    def __init__(self, name, price, bun, patty, cheese, temp, toppings, description):
        super().__init__(name, price)
        self.bun = bun
        self.patty = patty
        self.cheese = cheese
        self.temp = temp
        self.description = description

    def __str__(self):
        return ""

    def set_patty(self, patty):
        self.patty = patty

    def set_temp(self, temp):
        self.temp = temp

    def get_patty(self):
        return self.patty

    def get_temp(self):
        return self.temp


class Drink(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price)


class Side(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price)


class Combo(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price)


class Order:
    pass


def user_input_burger():
    # ask user for input and store it in burger object
    name = "Build your own"
    price = 12.99
    bun = input("What type of bun would you like? ")
    patty = input("What type of patty would you like? ")
    temp = input("What temp would you like it to be cooked? ")
    b = Burger(name, price, bun, patty, temp)

    return b


def user_input_drink():
    # ask user for input and store it in drink object
    for drink in drink_dict:
        print(drink)
    drink_order = input("Which drink would you like? ")
    d = Drink(drink_order, drink_dict[drink_order])

    return d


def user_input_side():
    s = Side()
    # ask user for input and store it in side object
    return s


def user_input_combo():
    c = Combo()
    # ask user for input and store it in combo object
    # a combo must include one burger, one side, and one drink
    return c


def take_order():
    # ask user for name for the order
    # repeat taking order until client is done
    # display order details
    # display a thank you message
    print("Welcome to Burger Shop")


burger1 = Burger("The AJ", 14.00, "Ciabatta", "Veggie Patty", "Gouda", "medium", "Beautifully crafted sandwich on a ciabatta roll "
                                                                    "with a veggie patty, gouda, avocado, onion, "
                                                                    "arugula, and mushroom")
burger2 = Burger("The AJ", 14.00, "Ciabatta", "Veggie Patty", "Gouda", "medium", "Beautifully crafted sandwich on a ciabatta roll "
                                                                    "with a veggie patty, gouda, avocado, onion, "
                                                                    "arugula, and mushroom")
theTripleBypass = Burger("The Triple ByPass", 22.00, "Brioche", "Angus Patty", "Cheddar", "medium", ["grilled onions", "bacon"], \
    "Six All-American Angus patties topped with cheddar, grilled onions and a mountain of bacon!!! So good that you won't even\
        regret saying goodbye to your family!")

burgerList = [burger1, burger2]
print(burgerList[0].name)
# burger_dict = {'The AJ': [14.00, "Veggie Patty", "Gouda", "medium", "Beautifully crafted sandwich on a ciabatta roll "
#                                                                     "with a veggie patty, gouda, avocado, onion, "
#                                                                     "arugula, and mushroom"]}
drink_dict = {}

take_order()
