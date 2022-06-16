#PANDAS PLOTTING

#In pandas, you would use the plot() method to create diagrams
#We have to use Pyplot because it allows us to vizualise the diagram on screen

#Calls the panda submodule
import pandas as pd

#Calls the Pyplot submodule
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

#This line allows the table to be plotted as a diagram
df.plot()
#This line shows and makes the diagram vizualise the diagram
plt.show()

#SCATTER PLOT

#Specify that you want a scatter plot with the kind argument
#kind = 'scatter'

#A scatter plot needs an x- and a y-axis.

#In the example below we will use "Duration" for the x-axis and "Calories" for
#the y-axis.

#Include the x and y arguments like this:

#x = 'Duration', y = 'Calories'

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = "Duration", y = "Calories")

plt.show()


#HISTOGRAM DIAGRAM

#kind = 'hist'

df = pd.read_csv('data.csv')
#Specify the column that is wanted in the histogram
df["Duration"].plot(kind = 'hist')

df.plot()

plt.show()

