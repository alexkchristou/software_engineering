# This is a shopping cart program for pet items


# ========================= Functions ========================= #
# This function adds item to the cart through user input
def cart_userinput(cart):
    # here we show the existing items in the cart
    
    item = input("Please type the item you want to add: ")
    price = float(input("How much does the item cost?: £"))
    quantity = int(input(" How many would you like to add to your cart? "))
    
    # here we call the function that will add the requested item, and quantity for the price given.
    cart = add_item(cart,item,price,quantity)
    return cart

# This function adds a new item to the cart dictionary and a new price for the item. It returns the updated cart dictionary.
def add_item(cart,item,price,quantity):
    
    if 'items' not in cart.keys():
        cart['items'] = []
        cart['prices'] = []
        cart['quantity'] = []
        cart['total_prices'] = []

    cart['items'].append(item)
    cart['prices'].append(price)
    cart['quantity'].append(quantity)
    cart['total_prices'].append(quantity*price)
    cart['total'] = cart.get('total',0) + price*quantity
    return cart

# This function removes items from the cart list. It calculates the new total and removes the price for that item using the index.
def remove_item(cart):
    try:
        remove_choice = input("Please type the item you would like to remove or its index number: ").lower()
        remove_quantity = int(input ("How many would you like to remove? (default is all)") or -1 )
        if remove_choice in cart['items']:
            index = cart['items'].index(remove_choice)
            function_reduce_quantity(index,remove_quantity)
            
        # If the user gives the index of the item to edit then this is the index instead.
        elif int(remove_choice)-1 <= len(cart['items']):
            index = int(remove_choice)-1
            function_reduce_quantity(index,remove_quantity)
        else:
            print ("Item not found in the cart")
    
    # This is for handling errors of incorrect value
    except ValueError: 
        print('Incorrect value provided. Try again. ')
    return cart

# This function takes the index and the quantity that we want to reduce the item in the cart by. 
# Then it recalculates the cart list if there is quantity of the item left. Otherwise it completely removes the item.
def function_reduce_quantity(index,remove_quantity):
    # this is the case where we keep the item in the list but we reduce its quantity
    # I need to recalculate the quantity remaining the total price remaining and the total remaining
    if  cart['quantity'][index] > remove_quantity > 0: 

        cart['quantity'][index] -= remove_quantity
        cart['total_prices'][index] = cart['quantity'][index] * cart['prices'][index]
        cart['total'] = cart.get('total',0) - cart['prices'][index] * remove_quantity
    
    # In this case we remove the item completely from the list
    else:
        cart['quantity'].pop(index) 
        cart['total_prices'].pop(index)
        cart['total'] -= cart['prices'][index]
        cart['prices'].pop(index)
        cart['items'].pop(index)


# This function takes the items in the cart and prices and prints them in a clear format.
def show_cart(cart):
    print ("--"*20)
    print('Welcome to Carts and Paws! \n \n')
    print('This is your shopping cart:')
    if 'items' not in cart.keys():
        print("Your cart is empty!")
    else:
        # here we print the header
        print('#','','Item','\t','Quantity','\t'*2, "Unit Price", '\t', "Total price")
        for index,item in enumerate(cart['items']):
            print (index+1,end = '. ')
            print(item, end = '')
            print('\t'*2, end = '')
            print(cart['quantity'][index], end = '')
            print('\t'*2, end = '')
            print(f"£ {cart['prices'][index]}", end = '')
            print('\t'*2, end = '')
            print(f"£ {cart['total_prices'][index]}")
    print ("--"*20)

# This function provides the menu option and returns the menu choice for the program
def menu():
    print( '''
Would you like to:
1. Add an item to your cart
2. Remove an item from your cart
3. Calculate the total cost of your cart
4. See our discounted items today
5. Checkout
'''
    )
    menu_choice = (input())
    return menu_choice

# This function holds a predefined list of items
def discount_items():
    discount = dict()
    discount = {'apples':1.20,'eggs':5.15,'milk':2.30}
    return discount

# This function prints on the screen the predefined list of items
def show_discount():
    discount = discount_items()
    print(40*'-')
    print("Here are some of our discounted items today:")
    for key in discount.keys():
        print(f'{key} £{discount[key]}')
    return discount

# This function adds to the cart items from the predefined list.
def discount_assistant(cart):
    discount = show_discount()
    try:
        choice_discount = (input('''
Would you like to add any of these discount items on your cart today? 
(type the choice number or -1 to return to the main menu)'''))
        if choice_discount == '-1':
            print ("Taking you back to main menu...one moment please...")
            return cart
        else:
            price = float(discount[choice_discount])
            quantity = int(input("How many would you like? "))
            cart = add_item(cart,choice_discount,price,quantity)
            return cart
    except TypeError: 
        print("Incorrect discount item input")

# ========================= START OF PROGRAM ========================= #
cart = dict()
done = False

# For the first run I will show a discount of items to help the user

while done is False:
    show_cart(cart)
    menu_choice = menu()
    if menu_choice == '1':
        cart_userinput(cart)
    elif menu_choice == '2':
        remove_item(cart)
    elif menu_choice == '3':
        print (f"The total cost of your cart is £ {cart['total']}")
    elif menu_choice == '4':
        discount_assistant(cart)
    elif menu_choice == '5':
        done = True
        print ("Thank you for shopping with us today!")
    else:
        print ("Invalid menu choice. Please try again.")

# ========================= END OF PROGRAM ========================= #