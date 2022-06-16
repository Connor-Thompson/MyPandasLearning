import pandas as pd

df = pd.read_csv('data.csv')

#This creates a mean using the .mean() method using the data
#only in the 'Calories' cloumn
mean = df["Calories"].mean()

#Mean = the average value (the sum of all values divided by number of values).
df["Calories"].fillna(mean, inplace = True)

#printing the first 28 rows
print("The rows 17 and 27 are filled with the MEAN value because they were null")
print(df.head(28))

#This one creates a mediun using the .median() method using the data
#only in the Calories Column
df = pd.read_csv('data.csv')

x = df["Calories"].median()

#Median = the value in the middle, after you have sorted all values ascending.
df["Calories"].fillna(x, inplace = True)

print("This table has the null rows 17 and 27 filled with the MEDIAN")
print(df.head(28))

#This one creates a mediun using the .median() method using the data
#only in the Calories Column
df = pd.read_csv('data.csv')

#Mode = the value that appears most frequently.
x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print("Rows 17 and 27 in the calories column are filled using the mode of the other data")
print(df.head(28))
