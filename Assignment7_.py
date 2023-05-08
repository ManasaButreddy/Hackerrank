import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

#read the csv file
df = pd.read_csv("C:/Users/arunb/Documents/Manasa/360Digi Training/Python/Materials/Data sets/Data.csv")
print(df)
#use SimpleImputer to handle missing values
mean_imputer = SimpleImputer(missing_values=np.nan,strategy = "mean")
#imputer.fit(df['Salaries'])
df["Salaries"] = pd.DataFrame(mean_imputer.fit_transform(df[["Salaries"]]))
print("************")
print(df["Salaries"].isna().sum()) #checking if any NAn values are present

#collect all the data with salary less than 70000
df_salary_lt_70000 = df[df['Salaries'] < 70000]

#print the result DataFrame
print("############")
print(df_salary_lt_70000)
