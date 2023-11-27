#age quiz practical task
#user input for the age. integer casting to make it an integer.
age=int(input('Please provide your age - Truthfully.'))

#a single if statement if the person is over 40.
if age>40:print('You are over the hill.')

#an elif statement to provide a customised message based on the age of the person. 
# Note: both statements can be correct at the same time eg. age >40 and >100.
if age>100:   print("Sorry, you are dead.")
elif age>=65: print ("Enjoy your retirement!")
elif age<13:  print("You qualify for the kiddie discount.")
elif age==21: print(" Congrats on your 21st!")
else:         print("Age is but a number.")