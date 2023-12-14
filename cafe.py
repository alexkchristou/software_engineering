#Task with lists and dictionaries

#I will first create a list for the items on the menu
#then I will create two lists with the values of the stock and price for each item
menu=["tea","juice","cake","latte"]
stock_val=[1,2,3,4]
price_val=[5,6,7,8]

#then I will create two dictionaries, one for stock and one for price, with keys the list menu and values the lists containing each value
#I had to google how to get past the errors I was getting for creating the dictionary. I used the zip function to create a list of tuples for the dictionary fucntion to read
stock_dic=dict(zip(menu,stock_val))
price_dic=dict(zip(menu,price_val))

total_cost_stock=0.0
for item in menu:
    total_cost_stock+=stock_dic[item]*price_dic[item]
print(f"The total cost of the stock is: £{total_cost_stock}")

#I might need some help with using the run and debug option of the studio; I am not comfortable using it yet.