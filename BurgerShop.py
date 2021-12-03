
#    ___                     __ _                    ___    _                _ __  
#   | _ )   _  _      _ _   / _` |   ___      _ _   / __|  | |_      ___    | '_ \ 
#   | _ \  | +| |    | '_|  \__, |  / -_)    | '_|  \__ \  | ' \    / _ \   | .__/ 
#   |___/   \_,_|   _|_|_   |___/   \___|   _|_|_   |___/  |_||_|   \___/   |_|__  
# _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
# "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
                                                                             
#         ▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒                                
#       ░░▒▒░░▒▒░░▒▒░░░░░░░░                              
#     ▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                            
#   ▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░                          
#   ▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                          
#   ▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒                          
#     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒                            
#     ▓▓░░░░████░░░░░░░░░░░░░░                            
#     ░░██▓▓▓▓▓▓▓▓████░░░░████                            
#   ██▓▓░░░░░░░░░░░░░░░░░░░░██▓▓                          
#   ████░░░░░░░░████████████████                          
#   ▒▒▒▒██░░████████████████▒▒▒▒                          
#   ▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒░░░░▒▒                          
#     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     

import BurgerMenu
###########################
## Classes and Variables ##
###########################

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



#  Keeps track of all the items and the total price
class Order():
    items = []
    total = 0
    guestName = ""

    def add_item(self, item):
        self.items.append(item)

    def calc_total(self):
        for it in self.items:
            self.total += it.get_price()
        formatted_total = "{:.2f}".format(self.total)
        return formatted_total

    def display(self):
        print(f"\
            ------------------------------------------------------\n\
            --------------------- Your Order ---------------------\n\
            ------------------------------------------------------\n\n\
            Customer Name: {self.guestName}\n\
            Item(s):                                        Price:\n\
            ")
        for idx, obj in enumerate(self.items):
            cost = float(obj.price)
            format_price = "{:.2f}".format(cost)

            print(f"\
            {idx + 1}. {obj.name}\n\
                                                            ${format_price} \
            ")
        
        print(f"\n\
            -------------------------------------------------------\n\
            Total: ${self.calc_total()}\
            ")


######################
### Main Functions ###
######################


# Function to take user input and store it as a Burger Object
def user_input_burger(ord):
    counter = 0

    for key in menu["Burgers"].keys(): # Loops through the menu Dictionary and prints all the options available
        counter += 1
        b = menu["Burgers"][key]
        print (f" {counter}.", b.name, "-", b.description)

    selected_burger = input("What is your choice? ")  
    
    if (selected_burger == "1") or (selected_burger.lower == "build your own"):  #  If the user wants to build their own Burger, this runs through their options
        
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
    ord.add_item(b)

#  Function that will create a custom Burger Object with every thing toppings
def user_create_burger(ord):
    name = "Build Your Own"
    price = 13
    desc = "Built-to-order burger"


    #  A sub function that is used to select all the choices from the dictionary 
    def custom_selection(type, list):
        print("\nOptions:")
        print(" 0. None")

        for idx, val in enumerate(list):  # Prints all options
            print(f" {idx + 1}. {val}")
        
        userInput = input(f"Please select a {type}: ")
        choice = ""

        if userInput == "None":
            choice = "None"
        else:
            choice = userInput

        print("Selected", choice)
        return choice
    
    #  Sub function runs for all parameters
    bun = custom_selection("bun", buns)
    patty = custom_selection("patty", patties)
    cheese = custom_selection("cheese", cheeses)
    topp = []

    return Burger(name, price, bun, patty, cheese, topp, desc)

def user_input_item(dict, ord):
    list = getList(dict)
    counter = 0

    print("\nOptions:\n")
    for key in dict.keys():
        counter += 1
        print(f" {counter}. {key}")
    
    choice = input("\nPlease input your desired item name or number: ")

    while check_input(choice, len(list), list) == False:
        choice = input("Please input a valid option: ")

    try:
        print("You Selected:", list[int(choice) - 1])
        numSelect = list[int(choice) -1]
        item = dict[numSelect]
        ord.add_item(item)
    except:
        strSelect = choice.lower().title()
        print(f"You Selected: {strSelect}")
        item = dict[strSelect]
        ord.add_item(item)

def take_order():
    more = True
    count = 0
    newOrd= Order()

    print("Welcome to Burger Shop!\n")
    name = input("Please enter a name for your order: ")
    newOrd.guestName = name.lower().title()

    while more != False:
        if count == 0:
            print(f"\nWhat can I get you started with, {newOrd.guestName}? ")
            print("\nOptions:\n")
            print(" 1. Burgers\n 2. Drinks\n 3. Sides\n 4. Combos")
            selected_item = input("\nInput Option Number or Name: ")

            while check_input(selected_item, 4, ["burgers", "drinks", "sides", "combos"]) == False:
                selected_item = input("Please input a valid option: ")
            
            pickItem(selected_item, newOrd)
            count = count + 1
        else:
            print("\nWould you like to add another item?")
            print("\nOptions:\n")
            print(" 1. Burgers\n 2. Drinks\n 3. Sides\n 4. Combos\n 5. Finish Order\n")
            selection = input("Selection: ")

            while check_input(selection, 5, ["burgers", "drinks", "sides", "combos", "finish order"]) == False:
                selection = input("Please input a valid option: ")

            if pickItem(selection, newOrd) == "Done":
                more = False
            else:
                more = True

    newOrd.display()

########################
### Helper Functions ###
########################

def check_input(inp, range, list):
    lowList = []
    for item in list:
        lowList.append(item.lower())
    
    # Checks if the input is in the list without case sensitivity
    if inp.lower() in lowList:
        return True
    # If not, checks if the input is a valid number
    else:
        try:
            if int(inp) > range:
                return False
            elif int(inp) < 1:
                return False
        except:
            return False
    # If there have been no errors, the input must be valid
    return True
    
def pickItem(choice, ord):
    if choice == 0:
        return print("Please select a valid option")
    elif ( ( choice == "1" ) or ( choice.lower() == "burgers" ) ): 
        user_input_burger(ord)
    elif ( ( choice == "2" ) or ( choice.lower() == "drinks" ) ): 
        user_input_item(menu["Drinks"], ord)
    elif ( ( choice == "3" ) or ( choice.lower() == "sides" ) ): 
        user_input_item(menu["Sides"], ord)
    elif ( ( choice == "4" ) or ( choice.lower() == "combos" ) ): 
        user_input_item(combo_menu, ord)
    elif ( ( choice == "5" ) or ( choice.lower() == "finish order" ) ): 
        return "Done"
    return False

def getList(dict):
    list = []
    for key in dict:
        list.append(key)
    return list

##################
### Menu Items ###
##################

buns = ["Brioche", "Ciabatta", "Plain"]
patties = ["Angus", "Beef", "Sirloin", "Veggie", "Chicken Filet"]
cheeses = ["American", "Cheddar", "Gouda", "Pepperjack"]
toppings = ["Arugula", "Avocado", "Bacon", "Lettuce", "Mayo", "Mushrooms", "Onion", "Pickles", "Tomato", "Grilled Onions", "Spicy Mayo"]
beer = ["Corona","Blue Moon", "Stella"]
lemonade = ["Pink Lemonade", "Original Lemonade", "Peach Lemonade"]
smoothie = ["Strawberry Banana Smoothie", "Mango Smoothie", "Peanut Butter Banana Smoothie"]

menu = {
    "Burgers" : {
        "Build Your Own": Burger("Build Your Own", 12, "None", "None", "None", [], "Built-to-order burger"),
        "The AJ": Burger("The AJ", 14.00, buns[1], patties[3], cheeses[2], [ toppings[1], toppings[6], toppings[0], toppings[5] ], \
            "Beautifully crafted sandwich on a ciabatta roll with a veggie patty, gouda, avocado, onion, arugula, and mushroom"),
      
        "The Big Al" : Burger("The Big Al", 17.00, buns[2], patties[2], cheeses[0], [ toppings[3], toppings[8], toppings[4], toppings[7] ], \
            "Our most popular burger option!! Filled with a thick soft juicy patty. Comes with lettuce,tomato,mayo,and pickles"),
      
        "The Triple Bypass" : Burger("The Triple Bypass", 22.00, buns[0], patties[0], cheeses[1], [ toppings[9], toppings[2] ], \
            "Six All-American Angus patties topped with cheddar, grilled onions and a mountain of bacon!!! So good that you won't "\
                "even regret saying goodbye to your family!"),
        "The Classic": Burger("The classic ", 12.00, buns[0], patties[1], cheeses[1],[ toppings[3], toppings[6], toppings[8], toppings[4], toppings[2] ],\
                              "Made with 100% pure beef topped with lettuce, onions, tomatoes and cheddar."),
        "The PG": Burger("The PG", 13.00, buns[0], patties[4], cheeses[3],[ toppings[3], toppings[6], toppings[8], toppings[10], toppings[2] ], \
                              "Spicy chicken sandwich with lettuce, tomatoes, onion, and three strips crispy bacon and homemmade spicy mayo.")
    },
    "Sides" : { 
        "French Fries": Side("French Fries", 4.99, "medium"),
        "Classic Salad" :Side("Caeser Salad",5.99,"medium"),
        "Onion Rings" :Side("Onion Rings",3.99,"medium"),
        "Coleslaw" :Side("Coleslaw",2.00,"small")
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
    "The AJ Combo": Combo("AJ Combo", 12, list(menu['Burgers'])[0],list(menu['Sides'])[0],list(menu['Drinks'])[0]),
    "The Big Al Combo": Combo("Big Al Combo", 12, list(menu['Burgers'])[1],list(menu['Sides'])[0],list(menu['Drinks'])[0]),
    "The Bypass Combo": Combo("Bypass Combo", 12, list(menu['Burgers'])[2],list(menu['Sides'])[0],list(menu['Drinks'])[0])
}

take_order()



##########
# Tests #
########
