import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv('medical_examination.csv')
print(df.head())

#create the displot 
plt.figure(figsize=(12,6), dpi=150)
sns.displot(data=df)
plt.show()

