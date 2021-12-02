##########################
# Classes and Variables #
########################

orders = []

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
            self.toppings = topp
        self.description = desc
        
    def add_topping(self, topp):
        self.toppings.append(topp)
        
    def set_bun(self, bun):
        self.bun = bun
        
    def set_patty(self, patty):
        self.patty = patty
        
    def set_bun(self, cheese):
        self.cheese = cheese
        

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
        
    def display(self):
       print("\t --> the", self.name,"is our celeb and tasty "+ 
             self.entree,"served with a " + self.side,"and an unlimited choice of",
             self.drink,"for a price of:",str(self.price)+'$. \n')


class Order:
    num = None
    items = []
    total = 0

    def __init__(self):
        orders.append(self)
        self.num = len(orders)
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
    counter = 1
    for i in menu[1].keys():
        print (i.get_name(), i.description, "(", counter, ")")
    selected_burger = input("What is your choice? ")  
    if selected_burger == 0:     
        name = "Build your own"
        price = 13.00
        print_buns
        bun = input("")
        print_patty
        patty = input("")
        print_cheese
        cheese = input("")
        b = Burger(name, price, bun, patty, cheese, topp=[], desc="")
        print_toppings()
        while topp != 0:
            topp = input("Enter topping or 0 ")
            b.add_topping(topp)
    else:
        b = menu["Burgers"][selected_burger]

    return b

def print_toppings():
    print("Here are your toppings options\n")
    for i in toppings:
        print(i)
    print("What topping would you like? Press 0 if done")
    
def print_buns():
    print("Here are your bun options\n")
    for i in buns:
        print(i)
    print("What bun would your like? Press 0 if none")
    
def print_patty():
    print("Here are your patty options\n")
    for i in patties:
        print(i)
    print("What patty would you like? Press 0 if none")

def print_cheese():
    print("Here are your cheese options\n")
    for i in cheeses:
        print(i)
    print("What cheese would you like? Press 0 if none")

def user_input_drink():
    d = Drink()
    for key,value in menu["Drinks"].items() :
        print(key)

    choice = input("Select your  Drink: ")
    if choice in menu["Drinks"]:
        d = menu["Drinks"][choice]
        return d

    else:
        print("invalid drink name")
    # ask user for input and store it in drink object
    
       


def user_input_side():
    s = Side()
    # ask user for input and store it in side object
    return s


def user_input_combo(menuCombo):   
    c = menuCombo
    #display menu
    for i in c.keys():
        c.get(i).display()
    comboPick = str(input('Please tap 1 for combo #1, 2 for combo #2, 3 for combo #3, '))
    return (combo_menu.get(comboPick).price) # can return a tuple
    # ask user for input and store it in combo object
    # ask user for input and store it in combo object
    # a combo must include one burger, one side, and one drink
    return c
def pickItem(choice):
    
    Pick_item = {
                "0": False,
                "1": user_input_burger(),
                "2": user_input_side(),
                "3": user_input_side(),
                "4": user_input_combo()
                }  
    return Pick_item.get(choice,"please choose between 1 or 2 or 3")

def take_order():
    # ask user for name for the order
    # repeat taking order until client is done
    # display order details
    # display a thank you message
    
   
    
    print("Welcome to Burger Shop\n\n")
    more = True
    count = 0
    while more != False:
        if count == 0:
            print("What can I get you started with? ")
        else:
            print("Select an item or enter 0 to quit\n")
            selected_item = input("A Burger(1), Drink(2), Side(3), or make a Combo(4) ")
            # try:
            #     pickItem(selected_item)
            #  except (KeyError,ValueError, TypeError, NameError) as error:
            #      print(f"Unexpected {error = }")
            
            if selected_item == 0:
                more = False
            else:
                if selected_item == 1:
                    user_input_burger()
                elif selected_item == 2:
                    user_input_drink()
                elif selected_item == 3:
                    user_input_side()
                elif selected_item == 4:
                    user_input_combo()
                else:
                    print("Please enter a valid option")
            count = count + 1
    print("\n Thanks for placing your order with us! ")


###############
# Menu Items #
#############

buns = ["Brioche", "Ciabatta", "Plain"]
patties = ["Angus", "Beef", "Sirloin", "Veggie", "Chicken Filet"]
cheeses = ["American", "Cheddar", "Gouda", "Pepperjack"]
toppings = ["Arugula", "Avocado", "Bacon", "Lettuce", "Mayo", "Mushrooms", "Onion", "Pickles", "Tomato", "Grilled Onions", "Spicy Mayo"]
beer = ["Corona","Blue Moon", "Stella"]
lemonade = ["Pink", "Original", "Peach"]
smoothie = ["Strawberry Banana", "Mango", "Peanut Butter Banana"]

menu = {
    "Burgers" : {
        "Build your own": Burger("Build your own", 0, "", "", "", [], \
            ""),
        "The AJ": Burger("The AJ", 14.00, buns[1], patties[3], cheeses[2], [ toppings[1], toppings[6], toppings[0], toppings[5] ], \
            "Beautifully crafted sandwich on a ciabatta roll with a veggie patty, gouda, avocado, onion, arugula, and mushroom"),
      
        "The Big Al" : Burger("The Big Al", 17.00, buns[2], patties[2], cheeses[0], [ toppings[3], toppings[8], toppings[4], toppings[7] ], \
            "Our most popular burger option!! Filled with a thick soft juicy patty. Comes with lettuce,tomato,mayo,and pickles"),
      
        "The Triple Bypass" : Burger("The Triple Bypass", 22.00, buns[0], patties[0], cheeses[1], [ toppings[9], toppings[2] ], \
            "Six All-American Angus patties topped with cheddar, grilled onions and a mountain of bacon!!! So good that you won't \
                even regret saying goodbye to your family!"),
        "The Classic": Burger("The classic ", 12.00, buns[0], patties[1], cheeses[1],[ toppings[3], toppings[6], toppings[8], toppings[4], toppings[2] ],\
                              "Made with 100% pure beef topped with lettuce, onions, tomatoes and cheddar."),
        "The PG": Burger("The PG", 13.00, buns[0], patties[4], cheeses[3],[ toppings[3], toppings[6], toppings[8], toppings[10], toppings[2] ], \
                              "Spicy chicken sandwich with lettuce, tomatoes, onion, and three strips crispy bacon and homemmade spicy mayo.")
    },

    "Sides" : { 
        "French Fries": Side("hand cut fries", 4.99, "medium"),
        "Classic salad" :Side("romane lettuce,olive oil,crushed garlic,Parmesan cheese,croutons",5.99,"medium"),
        "Onion rings" :Side("onion dipped in bread crumbs and then deep fried",3.99,"medium"),
        "Coleslaw" :Side("finely shredded raw cabbage with a salad dressing.",2.00,"small")
        
        

    },

   

    "Drinks" : {
        "Soft Drink": Drink("medium","Soft Drink", 1.00),
        "Strawberry Banana Smoothie": Drink("medium",smoothie[0], 2.00),
        "Mango Smoothie": Drink("medium",smoothie[1], 2.00),
        "Peanut Butter Banana Smoothie": Drink("medium",smoothie[2], 2.00),
        "Pink Lemonade": Drink("medium",lemonade[0],2.00),
        "Original Lemonade": Drink("medium",lemonade[1],2.00),
        "Peach Lemonade": Drink("medium",lemonade[2],2.00),
        "Corona": Drink("medium",beer[0],6.00), 
        "Blue Moon" :Drink("medium",beer[1],6.00),
        "Stella" :Drink("medium",beer[2],6.00),
       

    }
}


combo_menu = {
                "1": Combo("combo1", 12, list(menu['Burgers'])[0],list(menu['Sides'])[0],list(menu['Drinks'])[0]),
                "2": Combo("combo2", 12, list(menu['Burgers'])[1],list(menu['Sides'])[0],list(menu['Drinks'])[0]),
                "3": Combo("combo3", 12, list(menu['Burgers'])[2],list(menu['Sides'])[0],list(menu['Drinks'])[0])
             }


take_order()


##########
# Tests #
########

ord = Order()
ord.add_item(menu["Burgers"]["The Classic"])
for i in ord.items[0].toppings:
    print(i)
