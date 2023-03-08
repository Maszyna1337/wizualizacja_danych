"""
a = 'napis \ndrugi'
print(a)
b = 2
c = 4.2
print(b, c)
d = 5+3j
print(d)
e = c+d
print(e)
f = c//b
print(f)
g = c % b
print(g)
h = b**2
print(h)
i = b**1/2
j = pow(b, 1/2)
print(i, j)
print('b = b + 2')
print(b)
b += 2
print(b)

listy = ['a', 4, 5, 6, [1, 2, 3], 5.6]
print(listy)
listy.append(3)
print(listy)
print(listy[5])

lista = [1, 7, 3, 5, 2, 4]
print(lista)
#dodać element na wybrane miejsce
lista.insert(1, 6)
print(lista)
#dodac kilka elementow
zmienna = (3, 8)
lista.extend(zmienna)
print(lista)
#usunąć element z listy o danej pozycji
lista.pop(5)
print(lista)
#usunąć element z listy o danej wartosci
lista.remove(4)
print(lista)
#odwrocic elementy listy
lista.reverse()
print(lista)
#zrobic sortowanie
lista.sort()
print(lista)

slownik = {'a': 2, 1: 2, 4: 'ab'}
print(slownik)
print(slownik[4])
slownik['klucz'] = 'wartosc'
print(slownik)
slownik.pop('klucz')
print(slownik)
print(slownik.keys())
print(slownik.values())

print('a=%(zm)d' % {'zm':12})
print('a={}, b={}'.format(12, 12))
napis = 'a={}, b={}'
print(napis.format(12,12))

#a = input('podaj a:')
#b = input('podaj b:')
#print(a)
#print(b)
#print(type(a))
#a = int(a)
#if a > b:
#    print(a)
#elif a < b:
#    print(b)
#else:
#    print('a=b')

a = input('podaj a:')
b = input('podaj b:')
if a==b:
    print('Liczby są równe')
else:
    print('Liczby są różne')

a = input('podaj a:')
b = input('podaj b:')
c = input('podaj c:')
d = input('podaj d:')
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if (a>b) & (c>d):
    print('a wieksze od b i c wieksze od d')
else:
    print('a jest mniejsze od b lub c jest mniejsze od d')

for x in range(1, 6, 1):
    print(x)
else:
    print('koniec petli')

for x in listy:
    print(x)

for i in range(0, len(listy)):
    print(listy[i])

licznik = 0
while licznik != len(listy):
    print(listy[licznik])
    licznik += 1

liczby = [3, 4, 5, 1, 7, 8]
a = int(input('podaj a'))
i = 0
while i != len(liczby):
    if a - liczby[i] == 0:
        print('{} - {} = 0'.format(a, liczby[i]))
        break
    i += 1
"""
liczby = [1, 2, 2, 2, 4, 5, 6]
i = 0
while i != len(liczby):
    if liczby[i] == 2:
        liczby.pop(i)
        continue
    i += 1
else:
    print(liczby)
