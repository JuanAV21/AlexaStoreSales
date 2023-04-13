#
# Created April 11, 2023
# Description: This file is going to be responsible for reading the data and making all of the calculations for the data
#
#
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import scipy as sp
import numpy as np
import os


class calculations:
    target = "data/scanner_data.csv"
    df = None

    def __init__(self):
        path = os.path.dirname(os.getcwd())
        path = os.path.join(path, self.target)
        self.df = pd.read_csv(path)

    def head(self):
        return self.df.head()

    def totalSales(self):
        #returns total sales
        return self.df["Sales_Amount"].sum()

    def meanOfSales(self):
        #returns Mean of sales
        return self.df["Sales_Amount"].mean()

    def modeOfSales(self):
        return self.df["Sales_Amount"].mode()


objectvar = calculations()
print(objectvar.head())
print("mode: ", objectvar.df["Sales_Amount"].mode())
