import pandas as pd
import matplotlib.pyplot as plt

path = 'AP\modulo8\culoteta.xlsx'
encuesta = pd.read_excel(path)

total = len(encuesta['culo o teta'])
culos = len(encuesta[encuesta['culo o teta'] == 'culo'])
tetas = len(encuesta[encuesta['culo o teta'] == 'teta'])
promedio = [culos/total, tetas/total]
name = ['culo', 'teta']

plt.pie(promedio, labels= name, autopct='%0.1f %%')
plt.show()