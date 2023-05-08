#For the data set “Indian_cities”
#a)	Construct Boxplot on total effective literacy rate and draw inferences
import matplotlib.pyplot as plt
plt.hist(df.effective_literacy_rate_total)
#Inferences
#	Data is not symmetrical
#	It has negative skewness
#	Outliners are present in dataset

#b)	Find out the number of null values in each column of the dataset and delete them.
print(df.isnull().sum())
print(df.dropna(inplace = True))
