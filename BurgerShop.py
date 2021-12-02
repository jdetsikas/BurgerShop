##########################
# Classes and Variables #
########################

orders = []


# FoodItem Class
# Parent Class to all BurgerShop items
# All FoodItems will have a name and price
class FoodItem:
    name = ''
    price = None

    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    ### Getters and setters
    def set_name(self, name):
        self.name = name
    def set_price(self, price):
        self.price = price
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price


# Burger Class
# Child of FoodItem
# Has additional Parameters of bun, patty, cheese, toppings, description
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
        
    ###  Adds toppings to list
    def add_topping(self, topp):
        self.toppings.append(topp)
    
    ###  Getters and setters  
    def set_bun(self, bun):
        self.bun = bun
        
    def set_patty(self, patty):
        self.patty = patty
        
    def set_bun(self, cheese):
        self.cheese = cheese
        

    def add_topping(self, topp):
        self.toppings.append(topp)


# Drink Class
# Child of FoodItem
# Has an additional parameter size
class Drink(FoodItem):
    size = ''

    def __init__(self, size, name, price):
        super().__init__(name, price)
        self.size = size


# Side Class
# Child of FoodItem
# Has an additional parameter size
class Side(FoodItem):
    size = ''

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size


# Combo Class
# Child of FoodItem
# Has additional parameters ent, side, drink
# Each additional parameter is an Object.  A Burger, Side, and Drink
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


#  Order Class
#  Keeps track of all the items and the total price
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
    def display(self):
        print("\
            ----------------------------------\n\
            ----------- Your Order -----------\n\
            ----------------------------------\n\n\
            Item:                   Price:\n\
            ")
        for idx, obj in enumerate(self.items):
            cost = float(obj.price)
            format_price = "{:.2f}".format(cost)

            print(f"\
            {idx + 1}. {obj.name}\n\
                                    ${format_price} \
            ")
        
        print(f"\n\
            ----------------------------------\n\
            Total: ${self.calc_total()}\
            ")


########################
### Helper Functions ###
########################


# Function to take user input and store it as a Burger Object
def user_input_burger():
    counter = 1

    print(" 0. Build Your Own")
    
    for i in menu["Burgers"].keys(): # Loops through the menu Dictionary and prints all the options available
        b = menu["Burgers"][i]
        print (f" {counter}.", b.get_name(), "-", b.description)
        counter += 1

    selected_burger = input("What is your choice? ")  
    
    if selected_burger == "Build Your Own":  #  If the user wants to build their own Burger, this runs through their options
        
        b = user_create_burger() #  Calls user_create_burger to handle everything but adding toppings
        addTopp = True

        print("\nOptions:")
        print(" 0. None")
           
        for idx, top in enumerate(toppings): # Runs through the topping options list and prints the options 
            print(f" {idx + 1}. {top}")

        #  While the user still wants more toppings to their Burger
        #  Loops through asking what else they want to add
        while addTopp != False:
            choice = input("Enter topping: ")
            if choice == "None":
                addTopp = False
            else:
                topp = choice
                if topp in toppings:
                    b.add_topping(topp)
                else:
                    print("Please enter a valid topping \n")
                    

    #  If they select an option other than the build your own
    #  It gets stored as a Burger Object
    else:
        b = menu["Burgers"][selected_burger]

    
    # Prints the users selection
    print(b.name, b.price, b.description, b.toppings)
    return b

#  Function that will create a custom Burger Object with every thing toppings
def user_create_burger():
    name = "Build Your Own"
    price = 13
    desc = "Built-to-order burger"


    #  A sub function that is used to select all the choices from the dictionary 
    def custom_selection(type, list):
        print("\nOptions:")
        print(" 0. None")

        for idx, val in enumerate(list):
            print(f" {idx + 1}. {val}")
        
        userInput = input(f"Please select a {type}: ")
        choice = ""

        if userInput == "None":
            choice = "None"
        else:
            choice = userInput

        print("Selected", choice)
        return choice
    
    bun = custom_selection("bun", buns)
    patty = custom_selection("patty", patties)
    cheese =custom_selection("cheese", cheeses)
    topp = []

    return Burger(name, price, bun, patty, cheese, topp, desc) # A Burger with all selections

def user_input_drink():
    # d = Drink()
    for key,value in menu["Drinks"].items() :
        print(key)

    
    while True:
        choice = input("Select your  Drink: ")
        if choice in menu["Drinks"]:
            d = menu["Drinks"][choice]
            return d
            break
        else:
            print("invalid drink name")
            choice = input("Select your  Drink: ")
             
             
    
    # ask user for input and store it in drink object


def user_input_side():
    #s = Side()
    # ask user for input and store it in side object
    for key,value in menu["Sides"].items() :
        print(key)
    choice = 1
    while(choice != 0):
        choice = input("Select your  Side or 0: ")
        if choice in menu["Sides"]:
            s = menu["Sides"][choice]
        return s

    else:
        print("invalid drink name")
    #return s


def user_input_combo():   
    c = combo_menu
    #display menu
    # ask user for input and store it in combo object
    # ask user for input and store it in combo object
    # a combo must include one burger, one side, and one drink
    for i in c.keys():
        c.get(i).display()
    comboPick = str(input('Please tap 1 for combo #1, 2 for combo #2, 3 for combo #3, '))
    return (combo_menu.get(comboPick).price) # can return a tuple
    
def pickItem(choice):
    
    Pick_item = {
                "0": False,
                "1": user_input_burger(),
                "2": user_input_side(),
                "3": user_input_drink(),
                "4": user_input_combo(combo_menu)
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
            selected_item = input("A Burger(1), Drink(2), Side(3), or make a Combo(4) ")
        else:
            print("Select an item or enter 0 to quit\n")
            
            try:
                 pickItem(selected_item)
            except (KeyError,ValueError, TypeError, NameError) as error:
                  print(f"Unexpected {error}")
            
            if selected_item == 0:
                more = False
            else:
                if selected_item == "Burger":
                    user_input_burger()
                elif selected_item == "Drink":
                    user_input_drink()
                elif selected_item == "Side":
                    user_input_side()
                elif selected_item == "Combo":
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
