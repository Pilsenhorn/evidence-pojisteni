from pojistnik import Pojistnik

class SpravcePojistniku:
    def __init__(self):
        self.pojistenci = []

    def pridat_pojistence(self, jmeno, prijmeni, vek, telefon):
        pojistenec = Pojistnik(jmeno, prijmeni, vek, telefon)
        self.pojistenci.append(pojistenec)

    def vyhledat_pojistence(self, jmeno=None, prijmeni=None, vek=None, telefon=None):
        nalezeni = []
        for pojistenec in self.pojistenci:
            if (
                (jmeno is None or pojistenec.jmeno == jmeno) and
                (prijmeni is None or pojistenec.prijmeni == prijmeni) and
                (vek is None or pojistenec.vek == vek) and
                (telefon is None or pojistenec.telefon == telefon)
            ):
                nalezeni.append(pojistenec)
        return nalezeni

    def vypis_pojistencu(self):
        if not self.pojistenci:
            print("Žádní pojištěnci nejsou k dispozici.")
        for pojistenec in self.pojistenci:
            print(pojistenec)