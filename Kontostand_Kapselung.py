class Bankkonto:
    def __init__(self, kontonummer, kontostand):
        self.konotnummer = kontonummer
        self._kontostand = kontostand




    def einzahlen(self, betrag:float):

        self._kontostand = betrag + self._kontostand
        print(f"Du hast eingezahlt {self._kontostand}€")
        return self._kontostand

    def abheben(self, betrag: float):
        if betrag <= self._kontostand:
            self._kontostand = self._kontostand - betrag
        else:
            print(f"Nicht genug vorhanden {self._kontostand}")
        return self._kontostand 

    def zeige_kontostand(self):
        print(f"Aktueller Kontostand {self._kontostand}€")
        return self._kontostand





Transkation = Bankkonto(1234455, 700)
print(Transkation.zeige_kontostand())
print(Transkation.einzahlen(200))

print(Transkation.abheben(100))

print(Transkation.zeige_kontostand())