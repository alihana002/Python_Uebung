class Bankkonto:
    def __init__(self, kontonummer, kontostand):
        self.kontonummer = kontonummer
        self._kontostand = kontostand




    def einzahlen(self, betrag:float):

        self._kontostand = betrag + self._kontostand
        print(f"Du hast {betrag} eingezahlt")
        return f"Jetzt hast du {self._kontostand}"

    def abheben(self, betrag: float):
        if betrag <= self._kontostand:
            self._kontostand = self._kontostand - betrag
            return f"Du hast {betrag} abgehoben"
        else:
            return f"Nicht genug vorhanden {self._kontostand}"
    # Mit Property kannst du direkt auf die Methode zugreifen ohne ()  
    @property
    def zeige_kontostand(self):
        return f"Aktueller Kontostand {self._kontostand}€"





Transkation = Bankkonto(1234455, 700)
print(Transkation.zeige_kontostand)
print(Transkation.einzahlen(200))

print(Transkation.abheben(100))

print(Transkation.zeige_kontostand)