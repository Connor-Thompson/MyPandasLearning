#One of the most used method for getting a quick overview of the DataFrame,
#is the head() method. The head() method returns the headers and a specified
#number of rows, starting from the top.

import pandas as pd

df = pd.read_csv("data.csv")
#The use of .head(), allows the user to chose the first however many rows they
#want to view in the DataFrame. To view upto row 50, input 51 because row 0 is included
print("These rows were chosen spefically using the .head() method")
print(df.head(10))
#If nothing is in the .head(), then it only shows the first 5 rows
print("If .head() is not specified with a number. Then it returns the first 5 rows. As seen below: ")
print(df.head())

#.tail() can be used for the same purpose but from the bottom of the table
print("This is using .tail()")
print(df.tail(10))

#INFO ABOUT THE DATA

#The use of .info() tells me the information for all 164 rows in each column
print("This tells me information for all the rows in each column")
print(df.info())



