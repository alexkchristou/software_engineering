#Start of code for string handling task
#we want to read a string, so lets try input
#initialising the dummy variable that will be receiving each character of the string.
#the reason I use it is that I cannot change directly the text string and replace the character.
#i then use enumerate to take the string character and the number position.
#I modify each character one at a time with an if and add it to the dummy variable.
text=input("Please provide a string for the task:\n")
output=[]
for i,txt in enumerate (text):
    if i%2==0:
        output.append(txt.upper())
    else:
        output.append(txt.lower())
print("".join(output))