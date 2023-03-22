#Zadanie1
a = [x * 2 for x in range(0, 31)]
plik = open("zapis.txt", "w")
plik.write(str(a))
plik.close()
#Zadanie2
plik1 = open("zapis.txt", "r")
r = plik1.read()
print(r)
plik1.close()
#Zadanie3
linie = ["pierwsza", "druga", "trzecia"]
with open("tekst.txt", "r+") as plik2:
    for line in linie:
        plik2.write(line)
        plik2.write('\n')
    print(plik2.read())
#Zadanie4
class NaZakupy:
    nazwa_produktu = []
    ilosc = []
    jednostka_miary = []
    cena_jed = []

    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wypisz(self):
        return self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed

    def ile_produktu(self):
        return self.ilosc, self.jednostka_miary

    def ile_kosztuje(self):
        print(self.ilosc*self.cena_jed)


p1 = NaZakupy("jabłko", 2, "sztuki", 3.99)
p2 = NaZakupy("Mąka", 4, "kilogramy", 4.50)
print(NaZakupy.wypisz(p2))
print(NaZakupy.ile_produktu(p2))
NaZakupy.ile_kosztuje(p2)

#Zadanie5


class ciagi:
    def __init__(self):
        self.ciag = []

    def wyswietl_dane(self):
        return self.ciag

    def pobierz_dane(self):
        for i in range(1, 10):
            el = int(input("Podaj wyrazy ciągu"))
            self.ciag.append(el)

    def pobierz_parametry(self):
        a1 = int(input("Podaj pierwszy element "))
        roznica = int(input("Podaj roznice "))
        ilosc = int(input("podaj ilosc elementow "))
        self.ciag = [a1 + i*roznica for i in range(ilosc)]

    def suma(self):
        return sum(self.ciag)

    def policz_elementy(self):
        return len(self.ciag)


#Zadanie6
class robaczek:
    x = []
    y = []
    krok = []
    ile_krokow = []

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += ile_krokow*self.krok

    def idz_w_dol(self, ile_krokow):
        self.y -= ile_krokow*self.krok

    def idz_w_lewo(self, ile_krokow):
        self.x -= ile_krokow*self.krok

    def idz_w_prawo(self, ile_krokow):
        self.x += ile_krokow*self.krok

    def zwroc_wspolrzedne(self):
        return self.x, self.y


kroki = robaczek(0, 0, 1)
kroki.idz_w_gore(2)
kroki.idz_w_dol(3)
print(kroki.zwroc_wspolrzedne())



