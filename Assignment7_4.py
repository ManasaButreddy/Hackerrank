#For the dataset “Indian_cities”, 
#a)	Find out top 10 states in female-male sex ratio
import pandas as pd
import numpy as np
mydf = pd.read_csv("C:/Users/arunb/Documents/Manasa/360Digi Training/Python/Materials/Data sets/Indian_cities.csv")

#grouping the values by state
state_group  = mydf.groupby('state_name').sum()
#print(state_group)

#after grouping by state name, arrange sex_ration values in ascending order

female_male_sr = state_group[['sex_ratio']].sort_values('sex_ratio', ascending = False)
print('\n')
print(female_male_sr.head(10)) # print top 10 states

######################################################################################################################
# b)	Find out top 10 cities in total number of graduates
import pandas as pd
import numpy as np

#read csv file
grad = pd.read_csv("C:/Users/arunb/Documents/Manasa/360Digi Training/Python/Materials/Data sets/Indian_cities.csv")

#group by cities
city_group = grad.groupby('name_of_city').sum()

#sort by cities having highest graduates
print((city_group[['total_graduates']].sort_values('total_graduates', ascending = False)).head(10))

########################################################################################################################
#c)	Find out top 10 cities and their locations in respect of  total effective_literacy_rate.
print((grad[['name_of_city','effective_literacy_rate_total','location']].sort_values('effective_literacy_rate_total', ascending = False)).head(10))
