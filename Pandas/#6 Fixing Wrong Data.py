#FIXING WRONG DATA
#"Wrong data" does not have to be "empty cells"
#or "wrong format", it can just be wrong, like if someone registered "199"
#instead of "1.99".


#Replacing values
import pandas as pd

#original data table

df = pd.read_csv('dirtydata.csv')

print(df.to_string())


#ALTERED DATA IN TABLE
df = pd.read_csv("dirtydata.csv")

#Locate row 7 in the column Duration and set it to 45 instead of 420
df.loc[7, 'Duration'] = 45
#Formats the dates correctly
df['Date'] = pd.to_datetime(df['Date'])
#Confirms and applys the changes to the table
df.dropna(subset=['Date'], inplace = True)

#Prints the whole table and applies the changes stated
print("---- Look at row 7 and compare it to teh original and look at the change of data ----")
print(df.to_string())

#Altering data if it were in a big dataset

df = pd.read_csv('dirtydata.csv')
df["Date"] = pd.to_datetime(df["Date"])

#loop through all of the rows in the table
for x in df.index:
    #if a row in the 'Duration' column is higher than 120
    if df.loc[x, "Duration"] > 120:
        #then find take that row in 'Duration' and set it to 60
        df.loc[x, "Duration"] = 60

print("In this table, the row number 7 would have been located, seen as higher than 120 and then made to be 60")
print(df.to_string())
