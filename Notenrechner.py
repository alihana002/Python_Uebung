class Notenrechner:
    def __init__(self, noten: list[int]):
        self.noten = noten 


        # Methode die ich aufrufe, aber muss nicht in Konstruktor
        self.berechne_durchschnitt = self.berechne_durchschnitt()


    # auf die Eigenschaften der Klasse greift die Methode über self zu
    def berechne_durchschnitt(self) -> float:
        if not self.noten:
            return 0.0 
        
        return sum(self.noten) / len(self.noten)


    def Note_hinzufügen(self) -> int:
        if <= 1 noten <= 6:
            self.noten.append



Rechnung = Notenrechner([1, 4, 6, 6, 4, 1, 2,3])
        

print(Rechnung.berechne_durchschnitt)


