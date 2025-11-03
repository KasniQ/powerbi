import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# BLINKIT DATA ANALYSIS IN PYTHON

df = pd.read_csv("C:/Users/kasni/Documents/GitHub/powerbi/Project2/Blinkit Data/BlinkIT Grocery Data.csv")

print(df.head(10))              #df.head(10) <- first 10 records, this works only in jupyter notebook
                                #df.tail(15) <- last 15 records