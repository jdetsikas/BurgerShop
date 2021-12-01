##########################
# Classes and Variables #
########################

class FoodItem:
    name = ''
    price = ''

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
    bun = ''
    patty = ''
    cheese = ''
    toppings = []
    description = ''

    def __init__(self, name, price, bun, patty, cheese, topp, desc):
        super().__init__(name, price)
        self.bun = bun
        self.patty = patty
        self.cheese = cheese
        for item in topp:
            self.toppings.append(item)
        self.description = desc

class Drink(FoodItem):
    size = ''

    def __init__(self, size, name, price):
        super().__init__(name, price)
        self.size = size


class Side(FoodItem):
    size = ''

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size


class Combo(FoodItem):
    entree = None
    side = None
    drink = None

    def __init__(self, name, price, ent, side, drink):
        super().__init__(name, price)
        self.entree = ent
        self.side = side
        self.drink = drink


class Order:
    num = None
    items = []
    total = 0

    def __init__(self, item):
        self.items.append(item)
    def add_item(self, item):
        self.items.append(item)
    def calc_total(self):
        for it in self.items:
            self.total += it.get_price()
        return self.total


#####################
# Helper Functions #
###################

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
    # deprecated, will fix
    #for drink in drink_dict:
    #    print(drink)
    #drink_order = input("Which drink would you like? ")
    #d = Drink(drink_order, drink_dict[drink_order])

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


###############
# Menu Items #
#############

menu = {
    "Burgers" : {
        "The AJ" : Burger("The AJ", 14.00, "Ciabatta", "Veggie Patty", "Gouda", ["avocado", "onion", "arugula", "mushrooms"], \
            "Beautifully crafted sandwich on a ciabatta roll with a veggie patty, gouda, avocado, onion, arugula, and mushroom"),
      
        "The Big Al" : Burger("The Big Al", 17.00, "plain", "Sirloin", "American Cheese", ["lettuce", "tomato", "mayo", "pickles"], \
            "Our most popular burger option!! Filled with a thick soft juicy patty. Comes with lettuce,tomato,mayo,and pickles"),
      
        "The Triple Bypass" : Burger("The Triple Bypass", 22.00, "Brioche", "Angus Patty", "Cheddar", ["grilled onions", "bacon"], \
            "Six All-American Angus patties topped with cheddar, grilled onions and a mountain of bacon!!! So good that you won't \
                even regret saying goodbye to your family!"),
        "The Classic": Burger("The classic ", 12.00, "Brioche", "beef Patty", "Cheddar",["lettuce", "onions","tomatoes" ,"mayo", "bacon"],\
                              "Made with 100% pure beef topped with lettuce, onions, tomatoes and cheddar.")
        "The PG": Burger("The PG", 13.00, "Brioche", "Chicken Filet", "Pepperjack, [lettuce, onions, tomatoes, spicy mayo, bacon"), \
                              "Spicy chicken sandwich with lettuce, tomatoes, onion, and three strips crispy bacon and homemmade spicy mayo."
    },

    "Sides" : { 
        "French Fries": Side("hand cut fries", 4.99, "medium"),
        "Classic salad" :Side("romane lettuce,olive oil,crushed garlic,Parmesan cheese,croutons",5.99,"medium"),
        "Onion rings" :Side("onion dipped in bread crumbs and then deep fried",3.99,"medium"),
        "Coleslaw" :Side("finely shredded raw cabbage with a salad dressing.",2.00,"small")
        
        

    },

    "Drinks" : {
        "Soft Drink":Drink("medium","Soft Drink", 1.00),
        "Smoothie": Drink("medium","strawberry bananna", 2.00),

    }
}


take_order()
