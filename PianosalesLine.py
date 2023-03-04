# Importing modules
import pandas as pd
import matplotlib.pyplot as plt

# Defining Function
def Linechat():

# Reading The File using pandas
    df=pd.read_csv("piano_salesone.csv")

# Plotting BarChart
    plt.plot(df["YEAR"],df["VERTICAL PIANOS"],label="VERTICAL PIANOS",marker=".")
    plt.plot(df["YEAR"],df["GRAND PIANOS"],label="GRAND PIANOS")
    plt.plot(df["YEAR"],df["ELECTRONIC"],label="ELECTRONIC")
    plt.xlabel("Year")
    
# Plotting Labels
    plt.ylabel("Piano sales")
    plt.title("Yearly Piano Sales")
    plt.legend()
    plt.grid()
    plt.show()

#Calling the function
print(Linechat())
