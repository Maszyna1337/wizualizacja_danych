import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#ZADANIE1

x = np.linspace(-3, 7, 35)
y = x ** 2 / np.tan(x) + 5 * x
plt.plot(x, y, label='f(x)=x^2/tan(x)+5x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('wykres funkcji f(x)')
plt.legend()
plt.xlim(-3, 7)
plt.show()
plt.savefig('Jakub_Sobczynski_1.png')

#ZADANIE2

x1 = np.arange(4, 10, 1)
x2 = np.arange(0, 10, .1)
y1 = np.sqrt(x1)
y2 = (np.cos(x2))+0.4
plt.subplot(3, 1, 1)
plt.bar(x1, y1, color='b', label='f(x)=√(x)')
plt.legend()
plt.xlim(3.5, 9.5)
plt.title('Wykres słupkowy funckji')
plt.xlabel('x')
plt.ylabel('wynik funckji')
plt.yticks([1, 2, 3])
plt.subplot(3, 1, 3)
plt.plot(x2, y2, color='g', label='cos(x)+0.4', linewidth=6)
plt.legend()
plt.title('Wykres cos(x)+0.4')
plt.xlabel('x')
plt.ylabel('cos(x)+0.4')
plt.xlim(0, 10)
plt.ylim(-0.5, 1.5)
plt.show()

#ZADANIE3

df = pd.read_csv('glass.data', header=0, sep=',', decimal='.')
new_df = df[df['Refractive_index'] < 1.51766]
grouped_df = new_df.groupby(df['Type_of_glass']).size()
grouped_df.plot(kind='bar')
plt.xlabel('Typ szkła')
plt.ylabel('Ilość')
plt.title('Ilość każdego typu szkła')
plt.show()

#ZADANIE 4

df = pd.read_csv("glass.data")
df = df.groupby('Type_of_glass')['Aluminum'].sum()
df.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=14, figsize=(6, 6),
        labels=['Sodium', "Magnesium", "Silicon", "Potassium", 'Calcium', 'Barium', "Iron"])
plt.legend()
plt.title("zużycie Aluminium")
plt.savefig('im_naz_zad4b.png')
plt.show()
