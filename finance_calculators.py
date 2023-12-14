# this is a  capstone project
import math

# initial user screen and option menu
print( """investment \t- to calculate the amount of interest you'll earn on your investment \n
      bond \t- to calculate the amount you'll have to pay on a home loan""")
menu_option=input("Enter either \'investment\' or \'bond\' from the menu above to proceed:\n")
menu_option=menu_option.lower() # making it lowercase so that it is independent of user capitalisation

# value control: if is not either of the two option give an error message otherwise proceed.
if menu_option not in ['investment', 'bond']:
    print("Invalid input value")

elif menu_option=="investment":
    principal=float(input("Please specify the amount of money that you will be depositing in £:\n"))
    i_rate=int(input("Please insert the interest rate %:\n"))
    yrs=int(input("Please provide the number of years you plan on investing:\n"))
    interest=input("Please specify if you want the \'simple\' or \'compound\' interest option:\n")
        #value control for interest and calculating the amount returned
    interest=interest.lower()
    if interest not in ["simple", "compound"]:
        print("Invalid input value")
    elif interest=="simple":
        A=principal*(1+i_rate*yrs)
        print(f"you will receive £{A}.")
    else:
        A=principal*math.pow(1+i_rate,yrs)
        print(f"you will receive £{A}.")  
        
elif menu_option=="bond":
    Val_now=float(input("Please provide the present value of the house in £:\n"))
    i_rate=int(input("Please insert the interest rate %:\n"))
    t_repay_months=int(input("Please provide the number of months you plan to repay the bond:\n"))
    repayment=(i_rate*Val_now)/(1-(1+i_rate)**(-t_repay_months))
    print(f"your monthly payment will be £{repayment}")
