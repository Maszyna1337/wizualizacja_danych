import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#ZADANIE 1

x = np.arange(5, 10, .15)
y = np.tan(x)+(np.cos(x)/2)
plt.plot(x, y, label='f(x)=tan(x)+cos(x)/2')
plt.xlabel('x')
plt.xlabel('f(x)')
plt.xlim(5, 10)
plt.title('Wykres funkcji f(x)')
plt.show()

#ZADANIE 2

x1 = np.arange(0, 10, .25)
x2 = np.arange(1, 6)
y1 = np.sin(x1)+0.4
y2 = (x2+5)/2
plt.subplot(2, 2, 1)
plt.plot(x1, y1, 'r-.', label='sin(x)+0.4')
plt.xticks([0, 2.5, 5, 7.5, 10])
plt.yticks([-0.5, 0, 0.5, 1])
plt.xlabel('x')
plt.ylabel('sin(x)+0.4')
plt.legend(loc='lower left')
plt.subplot(2, 2, 4)
plt.bar(x2, y2, color='b', label='f(x)=(x+5)/2')
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([0, 1, 2, 3, 4, 5])
plt.xlabel('x')
plt.ylabel('wykres funkcji')
plt.legend(loc='upper left')
plt.show()

#ZADANIE 3

df = pd.read_csv('glass.data', header=0, sep=',', decimal='.')
new_df = df[df['Magnesium'] > 3.6]
grouped_df = df.groupby(df['Type_of_glass']).size()
grouped_df.plot(kind='pie', autopct='%.2f%%')
plt.legend(title='Typ szkła')
plt.show()

#ZADANIE 4

grupa = df.groupby('Type_of_glass')['Sodium'].sum()
sns.set(style='whitegrid')
plt.figure(figsize=(10, 6))
sns.barplot(data=grupa, x='Type_of_glass', y='Sodium', hue='Type_of_glass')
plt.xlabel('Type of Glass')
plt.ylabel('Sodium Consumption')
plt.title('Zużycie sodu dla każdego typu szkła')
plt.legend()
plt.show()