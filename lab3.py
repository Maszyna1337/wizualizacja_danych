import random
#Zadanie 1
a = [1-x for x in range(1, 10)]
print(a)
b = [4**x for x in range(0,8)]
print(b)
c = [x for x in b if x % 2 == 0]
print(c)
#Zadanie 2
a = random.sample(range(1, 100),10)
lista = [x for x in a if x % 2 == 0]
print(lista)
#Zadanie 3
slownik = {"Jajka": "sztuki", "Mleko": "litry", "Mąka": "kilogramy", "Ryba": "sztuki"}
szt = {value for value, key in slownik.items() if key == "sztuki"}
print(szt)
#Zadanie 4


def trojkat(a4, b4, c4):
    if (a4**2)+(b4**2) == c4**2:
        print("Trójkąt jest prostokątny")
        return 0
    elif (b4**2)+(c4**2) == a4**2:
        print("Trójkąt jest prostokątny")
        return 0
    elif (c4**2)+(a4**2) == b4**2:
        print("Trójkąt jest prostokątny")
        return 0
    else:
        print("Trójkąt nie jest prostokątny")
        return -1


print(trojkat(17, 8 , 15))
#Zadanie 5


def trapez(a5 = 5, b5 = 2, h5 = 3):
    return ((a5+b5)*h5)/2


print(trapez())
#zadanie 6


def ciag(pierwszy = 1, mnoznik = 4, dlugosc = 10):
    for i in range(pierwszy, dlugosc):
        pierwszy *= mnoznik
    print(pierwszy)


print(ciag())
#Zadanie 7


def ciag2(* wyra):
    iloczyn = 1
    for i in range(1, len(wyra)):
        4
    print(iloczyn)


print(ciag2(1, 2, 3))
#Zadanie 8
lista = {"Jajko": 2.50, "Złoto": 500, "Komputer": 2799.99}
def produkty(** lista):
    cal = 0
    for i in len(lista):
        cal += lista.value(i)
    return cal

print(produkty(lista))








