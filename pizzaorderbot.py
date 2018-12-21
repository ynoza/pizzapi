'''
Pizza Order App
'''
from pizzapy import *

#MAIN ---------------------------------------------------------------------------------------------------------------------------------

print ("ITS PIZZA TIME! I'm the PizzaBot here to help you order Pizza! Let's order some fresh Dominos Pizza!")

print ("First, I need a bit of information to place the order.")

service = input("Is this Delivery or Carryout? ")

customer = Customer(input("What's your first name? "), input("What's your last name? "), input("What's your email? "), input("What's your number? "))
customer.add_Address(Address(input("What's your street address (unit number & street name)? "), input("What city do you live in? "), input("What state/province/territory are you in? ")), input("What is your postal code? "), input("Do you live in Canada(ca) or USA (us)? ")))

store = StoreLocator.find_closest_store_to_customer(customer)

print ("The closest store I found to your address is: " + store)

menu = my_local_dominos.get_menu()

print("What would you like to order?")
cont = "yes"
order = Order.begin_customer_order(customer, my_local_dominos)
while (cont = "yes"):
    item = input("Give me an item to search for: ")
    menu.search(Name = item)

    code = input ("Which of these items do you want to add (please type item code): ")
    order.add_item(code)

    cont = input("Do you want to add more items? ")

print ("This is your order: " + order)

print ("Next I need your Credit Card info.")

card = CreditCard(input("Please enter your credit card number: "), input("Please enter your expiration date: "), input("Please enter your security code: "), input("Please enter your zip code: "))

print ("Thank you! I am now going to place your order!")

order.place(card)
my_local_dominos.place_order(order, card)


