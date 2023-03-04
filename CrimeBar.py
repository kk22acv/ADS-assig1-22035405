# Importing modules
import pandas as pd 
import matplotlib.pyplot as plt

# Defining Function
def Barchat(): 

# Reading The File using pandas
    fd=pd.read_csv("Crime Statistics Of Bangladesh.csv")
    
# Plotting BarChart
    plt.bar(fd["Year"],fd["Total Cases"],label="Total Cases",color="red")
    
#Plotting the labels
    plt.xlabel("Year")
    plt.ylabel("Crime Cases")
    plt.title("Crime Cases by Year")
    plt.legend()
    plt.grid()
    plt.show()

# Calling the Function
print(Barchat())  
