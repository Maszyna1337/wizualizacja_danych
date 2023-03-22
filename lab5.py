import math
#Zadanie1
#a = int(input("podaj a: "))
#b = int(input("podaj b: "))
#try:
#   wynik = pow(a, 2)+(a*b)+pow(b, 2)
#    zadanie1 = open("zadanie1.txt", "a+")
#    zadanie1.write(str(wynik))
#    zadanie1.close()
#except ValueError:
#    if type(a) or type(b) != float:
#        print("Nie podano liczb całkowitych")
#
#Zadanie2


def suma(lista1, lista2):
    lista3 = []
    for i in range(0, len(lista1)):
        tmp = 0
        tmp = lista1[i] + lista2[i]
        lista3.append(tmp)
    return lista3


a = [1, 2, 3, 8]
b = [1, 2, 3, 8]
zadanie2 = suma(a, b)
print(zadanie2)
#Zadanie3
tekst = open("tekst1.txt", "r+", encoding="utf-8")
odczyt = tekst.read()
znaki = []
duze = []
for i in range(100, 135):
    znaki.append(odczyt[i])
    if odczyt[i].isupper():
        duze.append(odczyt[i])
try:
    a = sum(1 for i in znaki if i.isupper())
    print(duze)
    print("Duże litery: ", a)
except ValueError:
    if a == 0:
        print("Nie ma dużych liter")
#Zadanie4

lista = [6, 4, 2, 4, 1, 734, 132]
b = 10
zadanie4 = [lista[i] for i in range(len(lista)) if lista[i] > b]
print(zadanie4)

#Zadanie5
ulamek = pow((2/7), 3)
cos = pow(math.cos(39), 2)
e = pow(math.e, 3)
pierwiastek = pow((e+cos), (1/5))
wynik = pierwiastek + ulamek + math.pi
print(round(wynik, 2))



