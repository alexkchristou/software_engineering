# practical task award.py
# first we need the input for the time performed in each of the events. We should also specify the units
t_swim=input("What was your time in swimming (minutes):")
t_cyc=input("What was your time in cycling (minutes):")
t_run=input("What was your time in running (minutes):")

t_total=t_swim+t_cyc+t_run
print(t_total)

#calculate the award with an if statement. Print the result
if t_total <= 100: award='Provincial Colours'
elif t_total<105: award="Provincial Half Colours"
elif t_total<110: award="Provincial Scroll"
else: award="No award"
print (f"based on your timings you will receive {award}.")
