#	Please take care of missing data present in the “Data.csv” file using python module “sklearn.impute” and its methods, also collect all the data that has “Salary” less than “70,000”.


import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

#read the csv file
df = pd.read_csv("C:/Users/arunb/Documents/Manasa/360Digi Training/Python/Materials/Data sets/Data.csv")
print(df)
#use SimpleImputer to handle missing values
# applying mean function for age
mean_imputer = SimpleImputer(missing_values=np.nan,strategy = "mean")
df["age"] = pd.DataFrame(mean_imputer.fit_transform(df[["age"]]))
print("************")
print(df["age"].isna().sum()) #checking if any NAn values are present

#apply median for outliners in salaries
median_imputer = SimpleImputer(missing_values=np.nan,strategy = 'median')
df["Salaries"] = pd.DataFrame(median_imputer.fit_transform(df[["Salaries"]]))
df["Salaries"].isna().sum()

#apply mode for below columns
mode_imputer = SimpleImputer(missing_values = np.nan, strategy = 'most_frequent')
df["Position"] = pd.DataFrame(mode_imputer.fit_transform(df[["Position"]]))
df['State'] = pd.DataFrame(mode_imputer.fit_transform(df[['State']]))
df['MaritalDesc'] = pd.DataFrame(mode_imputer.fit_transform(df[['MaritalDesc']]))
df['EmploymentStatus'] = pd.DataFrame(mode_imputer.fit_transform(df[['EmploymentStatus']]))
df['CitizenDesc'] = pd.DataFrame(mode_imputer.fit_transform(df[['CitizenDesc']]))
df['Race'] = pd.DataFrame(mode_imputer.fit_transform(df[['Race']]))
df['Department'] = pd.DataFrame(mode_imputer.fit_transform(df[['Department']]))
df.isnull().sum()

#constant imputer for Sex column
constant_imputer = SimpleImputer(missing_values = np.nan, strategy = 'constant', fill_value = 'F')
df['Sex'] = pd.DataFrame(constant_imputer.fit_transform(df[['Sex']]))
df.isnull().sum()

#collect all the data with salary less than 70000
df_salary_lt_70000 = df[df['Salaries'] < 70000]

#we can also use RandomImputer for age column
#from feature_engine.imputation import RandomSampleImputer
#random_imputer = RandomSampleImputer([&#39;age&#39;])
#df['age'] = pd.DataFrame(random_imputer.fit_transform(df[['age']]))
#df['age'].isna().sum()

#print the result DataFrame
print("############")
print(df_salary_lt_70000)
