#REMOVING DUPLICATE DATA FROM TABLES

#DISCOVERING DUPLICATES

import pandas as pd

df = pd.read_csv("dirtydata.csv")

#To discover duplicates, we can use the duplicated() method.
#The duplicated() method returns a Boolean values for each row: true being its own
#false being its a duplicate
print(df.duplicated())

#REMOVING DUPLICATES

df = pd.read_csv('dirtydata.csv')
#This will remove any duplicated rows from the table using the drop_duplicates method
df.drop_duplicates(inplace = True)
#Formats the dates
df["Date"] = pd.to_datetime(df['Date'])
#Sorts wrong data in row 7, set what row to locate and the column to search
#and then assign the value you want to set it to
df.loc[7, "Duration"] = 45

print(df.to_string())



