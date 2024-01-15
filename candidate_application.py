# This program asks the user to provide his details and then exports those in a csv file.

#****************** IMPORTS ******************#
import os
from datetime import datetime, date

#****************** START FUNCTIONS ******************#

def read_candidate_parameters():
    # Read the candidate paramenters if they exist in a csv. Else use the predetermined ones.
    if not os.path.exists("candidate_parameters.csv"):
        print ("Path of the candidate parameter file is Invalid")
        with open("candidate_parameters.csv", "w") as default_file:
            default_file.write("name;surname;mobile;city;country;programming;years_work_experience")

    with open('candidate_parameters.csv', 'r') as inputfile:
        str_parameters = inputfile.readlines()      
        parameters = str_parameters[0].split(';')
        parameters = [x.capitalize() for x in parameters]
    return parameters

def show_application(parameters):
    
    print('='*100)
    for index,parameter_value in enumerate(parameters):
        try:
            print(index+1,end=' ')
            print(parameter_value.ljust(30)+'\t', end= '')
            print(application[parameter_value])
        except KeyError:
            print("---")
    print('='*100)

def menu_options():   
        try:
            menu_choice = input(''' 
Choose one of the following:
e           exit
1-7         edit part of your application 
'submit'    submit your application
>''')
            if menu_choice == 'submit':
                return True
            elif menu_choice == 'e':
                return menu_choice
            elif 8 > int(menu_choice) > 0 :
                return int(menu_choice) 
            else:
                print("Invalid menu choice. Try again")
                return False
        except ValueError:
            print("Value error. Try again with the correct input")
            return False

def edit_application(parameters):
    index = choice -1
    application[parameters[index]] = input(f'Please type your {parameters[index]}: ')

    # Input check section. Based on the parameter
    # If it is the mobile or the years of experience, we want it to be digits
    # Everything else it should be characters.
    if parameters[index] == 'Mobile':
        if not application[parameters[index]].isdigit():
            print("Invalid phone number")
            application.pop(parameters[index])
    elif parameters[index] == 'Years_work_experience':
        if not application[parameters[index]].isdigit():
            print("Invalid number")
            application.pop(parameters[index])
    else:
        if application[parameters[index]].isdigit():
            print("Invalid value. Numerics are not allowed")
            application.pop(parameters[index])

def submit_application():
    try:
        timenow=str(datetime.today()).split()[0]
        filename = f"applicant_{application.get('Name')}_{application.get('Surname')}_{timenow}.txt"
        with open(filename,'w') as outfile:
            
            for index,parameter_value in enumerate(parameters):
                outfile.write(parameter_value.ljust(30)+'\t')
                outfile.write(application[parameter_value])
                outfile.write('\n')
        print ("Your application has been submitted successfuly! Good luck!")
    
    except KeyError:
        print ('Your application is missing information and has not been submitted.')


#****************** END FUNCTIONS ******************#



#****************** PROGRAM START ******************#
done = False
application = dict()
while done is False:
    parameters = read_candidate_parameters()
    show_application(parameters)

    choice = menu_options()
    if choice is True:
            submit_application()
            done = True
    elif choice is False:
        pass
    elif choice == 'e':
        print('Your application has not been submitted. Goodbye!')
        done = True
    else:
        edit_application(parameters)





#****************** PROGRAM END ******************#