from pojistenec import Pojistenec

class Aplikace:
    def __init__(self):
        self.pojistenci = []  # Seznam pojištěnců je definován přímo v aplikaci

    def pridej_pojistence(self):
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        vek = int(input("Zadejte věk: "))
        telefon = input("Zadejte telefonní číslo: ")
        pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.pojistenci.append(pojistenec)
        print("Pojištěnec byl přidán.")

    def vypis_pojistencu(self):
        if self.pojistenci:
            for pojistenec in self.pojistenci:
                print(pojistenec)
        else:
            print("Žádní pojištěnci nejsou k dispozici.")

    def vyhledej(self, jmeno=None, prijmeni=None):
        nalezeni = []
        for pojistenec in self.pojistenci:
            if (jmeno is None or pojistenec.jmeno.lower() == jmeno.lower()) and \
               (prijmeni is None or pojistenec.prijmeni.lower() == prijmeni.lower()):
                nalezeni.append(pojistenec)

        if nalezeni:
            print("Nalezený pojištěnci:")
            for pojistenec in nalezeni:
                print(pojistenec)
        else:
            print("Pojištěnec nenalezen.")

    def spustit_aplikaci(self):
        while True:
            akce = input(
                "Vyberte akci:\n"
                "1 - Přidat pojištěnce\n"
                "2 - Zobrazit všechny pojištěnce\n"
                "3 - Vyhledat pojištěnce\n"
                "4 - Konec\n"
                "Vaše volba: "
            )

            if akce == "1":
                self.pridej_pojistence()
            elif akce == "2":
                self.vypis_pojistencu()
            elif akce == "3":
                jmeno = input("Zadejte jméno pojištěnce: ")
                prijmeni = input("Zadejte příjmení pojištěnce: ")
                self.vyhledej(jmeno, prijmeni)
            elif akce == "4":
                print("Aplikace byla ukončena.")
                break
            else:
                print("Neplatná volba, zkuste to znovu.")
