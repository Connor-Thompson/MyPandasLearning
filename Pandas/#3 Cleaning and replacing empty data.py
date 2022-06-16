#DATA CLEANING

#Data cleaning is the process of fixing any bad data that is found in your dataset
#Bad data could be, empty cells, data in the wrond format, wrong data, duplicates

#Cleaning Empty Cells

import pandas as pd

df = pd.read_csv("data.csv")

#This is creating a new dataframe using the old one but leaves the

#original unaltered because of the use of the .dropna() method.  By default,
#the dropna() method returns a new DataFrame, and will not change the original.
new_df = df.dropna()
#This will print the new table and all of it using the .to_string method
print("This table is only displaying the rows that have all the data in the columns")
print(new_df.to_string())

#If you want to change the original DataFrame, use the inplace = True argument
#with in the dropna() method

#REPLACING/FILLING DATA

df = pd.read_csv('data.csv')
#Becuase we are wanting to change the null rows with the given data, we have to
#use the inplace = True argument to make those changes in the file
df.fillna(130)

print(df.head(28))

#REPLACING DATA IN SPECIFIC COLUMNS
df = pd.read_csv('data.csv')

#This line establishes the chosen column we want to auto fill data in and uses
#the inplace = True statement to make the changes happen
print("The filled in gap is only made in the calories column")
df["Calories"].fillna(130, inplace = True)

print(df.head(28))
