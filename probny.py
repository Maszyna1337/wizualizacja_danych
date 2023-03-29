import math
#zadanie1
#tekst = open("tekst1.txt", "r+", encoding="utf-8")
#odczyt = tekst.read()
#znaki = []
#for i in range(71, 111):
#    znaki.append(odczyt[i])
#a = znaki.count("a")
#if a == 0:
#   print("Brak liter")
#else:
#    print(a)
#Zadanie2
lista = [0.3, 2, 1.4, 3]
listafl = [lista[i] for i in range(0, len(lista)) if type(lista[i]) == float]
print(lista)
print(listafl)
#Zadanie3

def dodanie(lista):
    p = lista[0]
    for i in range(0, len(lista)):
        lista.append(p+lista[i])
    return lista


print(dodanie([1, 3, 3, 7]))
#Zadanie4
a = pow(math.sin(56), 2)
ulamek = (4**2)/25
log = math.log(85, 3)
pierwiastek = pow((ulamek+log), (1/4))
wynik = a+pierwiastek
print(round(wynik, 2))

#Zadanie5
#plik = open("plik.txt", "w+")
n = int(input("Podaj n"))
wynik = 0
try:
    for i in range(1, n+1):
        wynik+=i
    #plik.write(wynik)
    #plik.close()
except ValueError:
    if n<0:
        print("Liczba musi byc dodatnia")