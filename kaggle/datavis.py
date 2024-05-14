# this script will try to visualise the train data #

# import libraries#
import pandas as pd
import matplotlib as mlt
import numpy as np
import seaborn as sns

# start of program

df = pd.read_csv("train.csv")
print(df.columns)
print(df['PoliticalFactors'].min()) #ranges 0 to 16
print(df.info())
print(df.describe())

#drop the label column
df1 = df.drop('FloodProbability',axis = 1)
print (df1.head())
print (df1.info())