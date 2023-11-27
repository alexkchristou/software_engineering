# this is practical task 2

# save the given sentence
sentence= "The!quick!brown!fox!jumps!over!the!lazy!dog."

#replace any ! with  blank space. I wrap it in a print command
print ( sentence.replace("!"," ") )

#also now make everything uppercase. An alternative option would have been to save the output of the first method to a new parameter 
print ( sentence.replace("!"," ").upper())

#reprint the sentence in reverse. I will assume that the output of the last modification is the one to be reversed. 
#In order to do this we take the last outout and we slice with a negative step of -1
print(
    sentence.replace('!',' ').upper()[::-1]
)