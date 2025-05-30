class Kamer:
    def __init__(self, naam:str, logger_instance= None):
        self.naam: str = naam
        self.apparaten = []
        self.logger = logger_instance

    def voeg_apparaat_toe(self, apparaat_obj):
        if apparaat_obj not in self.apparaten:
            self.apparaten.append(apparaat_obj)

            apparaat_obj.kamer = self
            self.logger.log(f"DEBUG: Apparaat {apparaat_obj.naam} toegevoegd aan kamer {self.naam}.")
        else:
            self.logger.log(f"DEBUG: apparaat {apparaat_obj.naam} is al in kamer {self.naam}")

    def verwijder_apparaat(self, apparaat_obj_of_naam):
        apparaat_gevonden = None
        if isinstance(apparaat_obj_of_naam, str):
            for appie in self.apparaten:
                if appie.naam == apparaat_obj_of_naam:
                    apparaat_gevonden = appie
                    break
                #als de if niet activeert is het omdat apparaatobjofnaam geen str is dus kunnen we 
                #het als obj beschouwen in de else hieronder
        else:
            if apparaat_obj_of_naam in self.apparaten:
                apparaat_gevonden = apparaat_obj_of_naam
        
        if apparaat_gevonden:
            self.apparaten.remove(apparaat_gevonden)
            apparaat_gevonden.kamer = None

            self.logger.log(f"DEBUG: {apparaat_gevonden.naam} verweijderd uit kamer {self.naam}")
        else:
            self.logger.log(f"Debug: {str(apparaat_obj_of_naam)} niet gevonden in {self.naam}. Kan dus niet verwijderen.")
        
    def get_apparaten(self) -> list:
        return self.apparaten
    
    def __str__(self) -> str:
        kamernaamHead = f"Kamer: {self.naam}\n"
        if not self.apparaten:
            return kamernaamHead+" heeft nog geen apparaten in kamer."
        # ik wil hier alle __str__ methodes van elke apparaat hier verzamelen om makkelijk
        # en gecentraliseerd te kunnen returnen. zeker nog invoege, met een lijst en appends
        apparaten_tekst_lijst = []
        for app in self.apparaten:
            apparaten_tekst_lijst.append(str(app))

        return kamernaamHead + "\n".join(apparaten_tekst_lijst)
    