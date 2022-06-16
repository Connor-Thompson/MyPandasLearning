#CLEANING DATA IN THE WRONG FORMAT

#In our Data Frame, we have two cells with the wrong format.
#Check out row 22 and 26, the 'Date' column should be a string that
#represents a date:

#Let's try to convert all cells in the 'Date' column into dates.
#Pandas has a to_datetime() method for this:

import pandas as pd

df = pd.read_csv('dirtydata.csv')

#This focuses on the date column and formats all the data into the correct format
#for a date
df['Date'] = pd.to_datetime(df['Date'])

print("If you look at row 22, the data given is NaT(Not a Time) but in row 26, the data has been formatted to look like the rest of teh dates")

print(df.to_string())

#remove the rows missing a date
#The subset is in place because that is the column that we are wanting to search
#for empty data in teh rows
    df.dropna(subset=['Date'], inplace = True)

print("As seen, row 22 has been removed becuase their was no date in the date column")
print(df.to_string())

