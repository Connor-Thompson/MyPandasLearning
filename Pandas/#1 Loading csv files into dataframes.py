import pandas as pd

#The line is given the csv file name and told to read the data inside it
df = pd.read_csv('data.csv')
#prints the data in a terminal, the ".to_string()" tells the line to print the
#whole table intead of teh default first and last 5 rows
print(df) 

#options.display.max_rows can only tell you so many rows because it can't fully
#find out how many rows there are without a sort of idea
print("This just tells me there are more than 60 rows in the table")
print(pd.options.display.max_rows)
#by setting the maximum rows to the highest number, this creates another
#way to display the whole table
pd.options.display.max_rows = 9999
#tells the program to read the file and which file to read
df = pd.read_csv('data.csv')
#prints the whole table because of teh use of max_rows
print(df)
