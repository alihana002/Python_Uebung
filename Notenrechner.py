class Notenrechner:
    def __init__(self, noten: list[int]):
        self.noten = noten 


        # Methode die ich aufrufe, aber muss nicht in Konstruktor
        

    # auf die Eigenschaften der Klasse greift die Methode über self zu
    def berechne_durchschnitt(self) -> float:
        if not self.noten:
            return 0.0 
        
        return sum(self.noten) / len(self.noten)


    def Note_hinzufügen(self, neue_note) -> int:
        if 1 <= neue_note <= 6:
            self.noten.append(neue_note)
        else: 
            print("ungültige Zahl")
            



Rechnung = Notenrechner([1, 4, 6, 6, 4, 1, 2,3])
        
Rechnung.Note_hinzufügen(4)
print(Rechnung.noten)
print(Rechnung.berechne_durchschnitt())


