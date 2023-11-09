import pandas as pd
import matplotlib.pyplot as plt

data = {
    'curso A': [('lunes', 20), ('martes', 25), ('miercoles', 30), ('jueves', 22), ('viernes', 28)],
    'curso B': [('lunes', 18), ('martes', 21), ('miercoles', 26), ('jueves', 19), ('viernes', 23)],
    'curso C': [('lunes', 15), ('martes', 17), ('miercoles', 20), ('jueves', 14), ('viernes', 18)]   
}

df = pd.DataFrame(data)

for curso, datos in df.items():
    dias = [x[0] for x in datos]
    alumnos = [x[1] for x in datos]
    plt.bar(dias, alumnos, label=curso)

plt.xlabel('dia')
plt.ylabel('cantidad de alumnos')
plt.title('cantidad de alumnos por curso')
plt.legend

plt.show()