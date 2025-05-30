from .apparaat_basis import Apparaat;


class Gordijn(Apparaat):
    MOGELIJKE_POSITIES = ["open", "gesloten", "half open"]

    def __init__(self, naam:str, kamer=None, begin_positie:str = "gesloten"):
        super().__init__(naam, kamer)

        if begin_positie not in self.MOGELIJKE_POSITIES:
            self.logger.log(f"WAARSCHUWINF: Ongeldige beginpositie {begin_positie} voor {self.naam}"
                  "Juiste opties: open, gesloten, half open")
            self._positie:str = "gesloten"
        else:
            self._positie:str = begin_positie
        
        if not self.status:
            super().zet_aan()

    def open_gordijn(self):
        if not self.status:
            self.logger.log(f"DEBUG: gordijn {self.naam} staat UIT ")
            return
        if self._positie != "open":
            self._positie = "open"
            self.logger.log(f"DEBUG: Gordijn {self.naam} geopend")
        else:
            self.logger.log(f"gordijn {self.naam} was al open")
    
    def sluit_gordijn(self):
        if not self.status:
            self.logger.log(f"DEBUG: gordijn {self.naam} staat UIT ")
            return
        if self._positie != "gesloten":
            self._positie = "gesloten"
            self.logger.log(f"DEBUG: gordijn {self.naam} gesloten")
        else:
            self.logger.log(f"DEBUG: gordijn {self.naam} was al gesloten")
    
    def stel_positie_in(self, nieuwe_positie: str):
        if not self.status:
            self.logger.log(f"DEBUG: gordijn {self.naam} staat UIT ")
            return
        
        if nieuwe_positie in self.MOGELIJKE_POSITIES:
            if self._positie != nieuwe_positie:
                self._positie = nieuwe_positie
                self.logger.log(f"DEBUG: Gordijn {self.naam} ingesteld op {self._positie}")
            else:
                self.logger.log(f"DEBUG: gordijn {self.naam} stond al op {self._positie}")
        else:
            self.logger.log(f"WAARSCHUWINF: Ongeldige positie {nieuwe_positie} voor {self.naam}"
                f"Juiste opties: {self.MOGELIJKE_POSITIES}")
    @property
    def positie(self)-> str:
        return self._positie
    
    def get_status_details(self) -> str:
        status_tekst = "AAN" if self.status else "UIT"
        return f"Status:{status_tekst} Positie: {self.positie}"
    