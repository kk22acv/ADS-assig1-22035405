# Importing modules
import matplotlib.pyplot as plt 
import pandas as pd

#Defining the function
def Piechart():
    
#Reading the CSV File
    fd=pd.read_csv("CrimePIE.csv")
 
#setting the figuresize
    plt.figure(figsize=(30,10))
#Font size of text in PieChart
    textprops = {"fontsize":15}
#Plotting the Pie Chart
    plt.pie(fd["Dacoity"],labels=fd["Unit Name"],autopct="%.2f%%",shadow=True,
            radius=0.9,textprops =textprops)
    plt.legend(fontsize=10)
    plt.title("Crime Cases in Each Region ",fontsize=20)
    plt.show()
    
#Calling the function
print(Piechart())
