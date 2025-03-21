class Aplikace:
    def __init__(self, spravce):
       self.spravce = spravce  # Uložíme správce pojištěnců do atributu třídy Aplikace

    def spustit_aplikaci(self):
       while True:
          akce = input(
             "1 - Přidat pojištěnce\n"
             "2 - Zobrazit všechny pojištěnce\n"
             "3 - Vyhledat pojištěnce\n"
             "4 - Konec\n"
             "Vyberte akci: "
          )

          if akce == "1":
             self.pridat_pojistence_uzivatelsky()
          elif akce == "2":
             self.spravce.vypis_pojistencu()
          elif akce == "3":
             self.vyhledat_pojistence_uzivatelsky()  # Zavoláme metodu pro hledání pojištěnce
          elif akce == "4":
             print("Konec aplikace.")
             break
          else:
             print("Neplatná volba. Zkuste to znovu.")

    def pridat_pojistence_uzivatelsky(self):
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        while True:
            try:
                vek = int(input("Zadejte věk: "))
                if vek <= 0:
                    print("Věk musí být kladné číslo.")
                else:
                    break
            except ValueError:
                print("Neplatný formát věku. Zadejte prosím číslo.")
        telefon = input("Zadejte telefonní číslo: ")
        self.spravce.pridat_pojistence(jmeno, prijmeni, vek, telefon)
        print("Pojištěnec byl přidán.")

    def vyhledat_pojistence_uzivatelsky(self):
        jmeno = input("Zadejte hledané jméno (nebo nechte prázdné): ") or None
        prijmeni = input("Zadejte hledané příjmení (nebo nechte prázdné): ") or None
        vek_str = input("Zadejte hledaný věk (nebo nechte prázdné): ")
        vek = int(vek_str) if vek_str else None
        telefon = input("Zadejte hledané telefonní číslo (nebo nechte prázdné): ") or None

        nalezeni = self.spravce.vyhledat_pojistence(jmeno, prijmeni, vek, telefon)

        if nalezeni:
          print("Nalezený pojištěnci:")
          for p in nalezeni:
             print(p)
        else:
          print("Pojištěnec nenalezen.")