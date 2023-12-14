#This task is under user defined functions T16
#This program calculates the users total holiday cost, which includes the plane cost, the hotel cost and car-rental cost
#The user will have options for the city they are flying to, which affects plane cost
#The hotel cost and the car-rental daily cost will be fixed. 
#Edit: I have added a hotel option menu to prvide additional choice to the user if he/she wishes to.
#The user defines how many days of hotel stay and car rental he/she will spend on his/her holidays.

#------------------- User defined functions -------------------#

#This function provides a travel option menu by destination city 
def options_city():
    print("\nHello! This is your personal trip calculator! Which city would you like to travel to? \n")
    print("Your options are: \n\t- [B]arcelona \n\t- [A]thens \n\t- [N]ew York\n\t- [T]romso")

#This function provides a hotel option menu
def options_hotel():
    print("\nDo you have a hotel preference? \n")
    print("Your hotel options are: \n\t- [1] star  \n\t- [2] star \n\t- [3] star \n\t- [4] star \n\t- [5] star \n\t- [N]o preference\n")

#This function takes the number of nights from the program, calls the hotel option menu and then calculates the total cost of the stay.
def hotel_cost(nights):
    options_hotel()
    hotel_pref=input()
    if hotel_pref[0]=="1":
        ppn=50.0
    elif hotel_pref[0]=="2":
        ppn=100.0
    elif hotel_pref[0]=='3':
        ppn=150.0
    elif hotel_pref[0]=='4':
        ppn=250.0
    elif hotel_pref[0]=='5':
        ppn=500.0
    elif hotel_pref[0]=='n':
        ppn=200.0
    else:
        print("Invalid choice. Exiting...")
        return
    cost=ppn*nights
    return cost
#This function takes the first letter of the string, mathes it with the relevant city from the option menu, and then calculates the price of the flight.
def plane_cost(city):
    if city[0]=='a':
        price_flight=150.0
    elif city[0]=='b':
        price_flight=50.0
    elif city[0]=='n':
        price_flight=250.0
    elif city[0]=='t':
        price_flight=100.0
    else: 
        print ("Unrecognised city! Exiting....")
        return
    return price_flight

#This function takes the number of days of the car rental and then returns the car rental cost. Fixed rate of 130 per day in this example.
def car_cost(days):
    return days*130.0

#------------------- Start of program -------------------#

try:
#User input for destination city, number of nights at hotel and number of days for car rental
    options_city()
    city_flight=input().lower()
    num_nights=int(input("How many nights will you stay at the hotel?:\n"))
    rental_days=int(input("How many days will you hire a car for?:\n"))

#We calculate the total cost of the holiday by invoking each cost function and summing them together
    total_cost= plane_cost(city_flight)+hotel_cost(num_nights)+car_cost(rental_days)
    print(f"The estimated cost for this holiday is: £ {str(total_cost)}")


#Handling different types of error 
except ValueError as ve:
    print("Invalid value. Exiting....")
except TypeError as te:
    print ("Invalid choice...Exiting...")
except UnboundLocalError as ue:
    print("")

#------------------- End of program -------------------#

