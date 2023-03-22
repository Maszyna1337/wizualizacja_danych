#Zadanie1
#a = [x * 2 for x in range(0, 31)]
#plik = open("zapis.txt", "w")
#plik.write(str(a))
#plik.close()
#Zadanie2
#plik1 = open("zapis.txt", "r")
#r = plik1.read()
#print(r)
#plik1.close()
#Zadanie3
#linie = ["pierwsza", "druga", "trzecia"]
#with open("tekst.txt", "r+") as plik2:
#    for line in linie:
#        plik2.write(line)
#        plik2.write('\n')
#    print(plik2.read())
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
class ciag:
    pierwszy = []
    wartosci = []
    roznica = []
    ile_elementow = []

    def wyswietl_dane(self):
        return self.wartosci

    def pobierz_elementy(self):
        self.wartosci = int(input("Podaj wartosc"))

    def pobierz_parametry(self):
        self.pierwszy = int(input("Podaj pierwszy wyraz"))
        self.roznica = int(input("Podaj roznice"))
        self.ile_elementow = int(input("Podaj liczbe elementow"))
        for self.pierwszy in range(self.pierwszy, self.ile_elementow):
            self.pierwszy+=self.roznica
            self.wartosci += self.pierwszy

wyraz = ciag()
ciag.pobierz_parametry(wyraz)
print(ciag.wyswietl_dane(wyraz))
