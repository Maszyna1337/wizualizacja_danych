#Zadanie 1.
import math
print(pow(math.e, 10))
liczba = math.log(5+math.sin(8)**2)
print(pow(liczba, 1/6))
print(math.floor(3.55))
print(math.ceil(4.80))
#Zadanie 2.
imie = "JAKUB"
nazwisko = "SOBCZYNSKI"
print(imie.capitalize(), nazwisko.capitalize())
#Zadanie 3.
piosenka = "la la la"
print(piosenka.count("la"))
#Zadanie 4.
str = "zadanie czwarte"
print(str[1], str[14])
#Zadanie 5.
st = "jakis napis"
print(st.split())
#Zadanie 6.
print("String: {0}, float: {1}, hex: {2:x}".format("string", 0.3, 0x4E8))
#Zadanie 7.
sporty = ["siatka", "piłka nożna", "koszykówka", "boks"]
sporty.reverse()
print(sporty)
sporty.append("golf")
print(sporty)
#Zadanie 8.
skroty = {'np': 'na przykład', 'min': 'minimalnie', 'cyt': 'cytując'}
print(skroty['np'])
#Zadanie 9.
gry = {'cs:go': "3789h", 'cyberpunk': '137h', 'dark souls 3': '275h'}
print(len(gry))
#Zadanie 10.
zdanie = input("Podaj zdanie: ")
print(zdanie.count('a'))
# Zadanie 11.
a = input("Podaj a:")
b = input("Podaj b:")
c = input("Podaj c:")
if a > b:
    if a > c:
        print(a, " jest najwieksze")
    else:
        print(c, "Jest najwieksze")
elif b > a:
    if b > c:
        print(b, " jest najwieksze")
    else:
        print(c, " jest najwieksze")
else:
    print(c, " jest najwieksze")
#Zadanie 12.
lista = [1, 2.3, 6, 1.34, 13]
for x in range(len(lista)):
    lista[x] = lista[x]**2
print(lista)
#Zadanie 13.
dodanie = []
i = 0
while i < 10:
    l = int(input("Podaj liczbe: "))
    if l % 2 == 0:
        dodanie.append(l)
    i += 1
print(dodanie)


