#Representing dates in different ways
#Date objects in Python have a great number of ways they can be printed out as strings. In some cases, you want to know the date in a clear, language-agnostic format. In other cases, you want something which can fit into a paragraph and flow naturally.
#Print out the same date, August 26, 1992 (the day that Hurricane Andrew made landfall in Florida), in a number of different ways, by using the “ .strftime() ” method. Store it in a variable called “Andrew”. 
#Instructions: 
#Print it in the format 'YYYY-MM', 'YYYY-DDD' and 'MONTH (YYYY)'
from datetime import date

#create object Andrew to store date
Andrew = date(1992, 8, 26)

#in format YYYY-MM
print(Andrew.strftime('%Y-%m'))

#in format YYYY-DDD
print(Andrew.strftime('%Y-%d'))

#in format MONTH(YYYY)
print(Andrew.strftime('%m(%Y)'))
