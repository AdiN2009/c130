import pandas as pd 
import csv

df = pd.read_csv("Data_merged.csv")
print(df.shape)

print(df.columns)


df.drop(columns=['Unnamed: 0', 'Luminosity', 'Star_name_y', 'Distance_y', 'Mass_y', 'Radius_y'], inplace=True)
columns_to_clean = ['id', 'Star_name_x', 'Distance_x', 'Mass_x', 'Radius_x']
df[columns_to_clean] = df[columns_to_clean].fillna(0)


print(df.columns)
print(df.describe())
print(df.info())
print(df.dtypes)


df.to_csv('final_data.csv',index=True, index_label="id")
