class Bankkonto:
    # setter erwartet das = 
    def __init__(self, kontostand = 0):
       # self.kontonummer = kontonummer
        self._kontostand = kontostand
    # Beide Funktionen müssen Kontostand heißen, für getter und setter
  
    @property
    def kontostand(self):
        return self._kontostand
    
    '''
    Vorher getter platzieren, dann setter mit Property
    sonst erkennt python die Funktion kontostand nicht
    vorrausetzung property, dann setter 

    '''
    @kontostand.setter
    def kontostand(self,kontostand_Neu: float):
        if kontostand_Neu < 0:
           raise ValueError("Fehler: Wert darf nicht negativ sein")
       # muss neuen Wert prüfen
       # Übergeben den neuen Parameter den alten
        self._kontostand = kontostand_Neu   

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





'''
Transkation = Bankkonto(1234455, 700)
print(Transkation.zeige_kontostand)
print(Transkation.einzahlen(200))

print(Transkation.abheben(100))

print(Transkation.zeige_kontostand)

'''
Transaktion = Bankkonto()
# Setter werden = so aufgerufen deshalb nicht mit ()
Transaktion.kontostand = 100
print(Transaktion.kontostand)
