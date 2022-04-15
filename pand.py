import pandas as pd
data=pd.read_csv("/home/admin123/Documents/NUMPY/j.csv",header=0)#header is for starting
# print(data.head())#By default it took 5 lines
# print(data.head(7))#It take 7 lines
# print(data.describe())
# print(data.iloc[3])
# print(data.iloc[0:6])


data1=pd.read_csv("/home/admin123/Documents/NUMPY/j.csv",header=0,index_col=0)#header is starting
print(data1.head())
print(data1.loc["kirti 11 45"])

