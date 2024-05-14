# this script will try to visualise the train data #

# import libraries#
import pandas as pd

df = pd.read_csv("train.csv")
print(df.columns)
print(df['PoliticalFactors'].min()) #ranges 0 to 16
print(df.info())
print(df.std)