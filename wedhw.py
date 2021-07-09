
###1) Build a Shopping Cart
##You can use either lists or dictionaries. The program should have the following capabilities:

##1) Takes in input
#2) Stores user input into a dictionary or list
#3) The User can add or delete items
#4) The User can see current shopping list
#5) The program Loops until user 'quits'
#6) Upon quiting the program, print out all items in the user's list


from IPython.display import clear_output

#Create a global list
cart = []

def show_cart():
    clear_output()
    print("Your cart contains: ")
    for item in cart:
        print(item)
        
def add_item(item):
    clear_output()
    cart.append(item)
    print(f"{item} was added to your cart")
    
def remove_item(item):
    clear_output()
    cart.remove(item)
    print(f"{item} was removed from your cart")
    
def clear_cart():
    clear_output()
    cart.clear()
    print("Your cart is empty")
    
    
def shopping_cart():
    while True:
        response= input("What would you like to do? You can: quit/ add/ remove/ show or clear. Only type one at a time.")
    
        if response.lower()== "quit":
            show_cart()
            print("Thanks for shopping")
            break

        elif response.lower()== 'add':
            item = input("What would you like to add? ")
            add_item(item)
        elif response.lower()== 'remove':
            #show_the_cart
            item = input("What item would you like to remove?")
            remove_item(item)
        elif response.lower()== 'show':
            show_cart()
        elif response.lower()== 'clear':
            clear_cart()
        else:
            print("That ain't it")
        
shopping_cart()






###Create a Module in VS Code and Import It into jupyter notebook
##Module should have the following capabilities:
##1) Has a function to calculate the square footage of a house
##Reminder of Formula: Length X Width == Area

##2) Has a function to calculate the circumference of a circle
##Program in Jupyter Notebook should take in user input and use imported 
##functions to calculate a circle's circumference or a houses square footage
import math

def sqrft (length, width): 
    print(f"The area is {length*width}")


##2 pi * r
def circumference1 (r): 
    circumference = 2*math.pi *r
    print(circumference)

