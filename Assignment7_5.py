#For the data set “Indian_cities”
# a)	Construct histogram on literates_total and comment about the inferences
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/arunb/Documents/Manasa/360Digi Training/Python/Materials/Data sets/Indian_cities.csv")
plt.hist(df.literates_total)
	
# b)	Construct scatter  plot between  male graduates and female graduates
import matplotlib.pyplot as plt
x = df.male_graduates
y = df.female_graduates

plt.scatter(x, y, edgecolors = 'black')
