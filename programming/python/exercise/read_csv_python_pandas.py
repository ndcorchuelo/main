import pandas as pd
import os

path = "C:\\Users\\nicolas.corchuelo\\Dropbox\\My PC (DESKTOP-CCAR0HT)\\Desktop\\"

os.chdir(path)

print(os.getcwd())
print(os.listdir())

df = pd.read_csv('afectaciones_disponibilidad.csv',index_col=0, sep = ',')

print(df.head())