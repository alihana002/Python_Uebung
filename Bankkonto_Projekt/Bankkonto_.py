import datetime


class Bankkonto:
    # setter erwartet das =
    # Liste nicht in Konstruktor übergben sonst wird immer die selbe Liste aufgerufen und erweitert 
    def __init__(self, kontostand:float = 0):
       # self.kontonummer = kontonummer
        self._kontostand = kontostand
        self._Transaktionsverlauf = []
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
    def kontostand(self,kontostand_neu: float):
        if kontostand_neu < 0:
           raise ValueError("Fehler: Wert darf nicht negativ sein")
       # muss neuen Wert prüfen
       # Übergeben den neuen Parameter den alten
        self._Transaktionsverlauf.append(kontostand_neu)
        self._kontostand = kontostand_neu 

 
    def einzahlen(self, betrag:float):

        self._kontostand = betrag + self._kontostand
        self._Transaktionsverlauf.append(self._kontostand)
        return f"Du hast {betrag} eingezahlt und jetzt hast du {self._kontostand}"
                                  
    def abheben(self, betrag: float):
        if betrag <= self._kontostand:
            self._kontostand = self._kontostand - betrag
            self._Transaktionsverlauf.append(self._kontostand)
            return f"Du hast {betrag} abgehoben"
        else:
            return f"Nicht genug vorhanden {self._kontostand}"
    # Mit Property kannst du direkt auf die Methode zugreifen ohne ()  
    @property
    def zeige_kontostand(self):
       
        return f"Aktueller Kontostand {self._kontostand}€"
    
    'Property darf keine Parameter enthalten bzw Zustände ändern'
    @property
    def Transaktionsverlauf(self):
        return self._Transaktionsverlauf



        
        






Transaktion= Bankkonto()


# Setter werden = so aufgerufen deshalb nicht mit ()
Transaktion.kontostand = 800

print(Transaktion.einzahlen(200))

print(Transaktion.abheben(100))

print("\nVerlauf: ")
for i in Transaktion.Transaktionsverlauf:
    print(i)