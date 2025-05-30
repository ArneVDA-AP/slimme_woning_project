from .apparaat_basis import Apparaat;

class Lamp(Apparaat):
    def __init__(self, naam:str, kamer=None, helderheid: int = 100):
        super().__init__(naam, kamer)

        # self.helderheid:int = self._valideer_helderheid(helderheid)
        self._helderheid:int = 100
        self.pas_helderheid_aan(helderheid)

        # Ik ga er van uit dat als we een helderheid instellen
        # dat we ook willen dat de lamp automatisch gaat branden.
        # de lamp is standaard uit, status wordt standaard op False
        # geinitialiseerd in onze superclass appaarat.
        # Ook gaan we ervan uit dat als helderheid op 0 gezet wordt en
        # de lamp is aan dat we willen dat de lamp 'vanzelf' uitgaat.
        # if self.helderheid > 0 and not self.status:
        #     super().zet_aan()
        
        # elif self.helderheid == 0 and self.status:
        #     super().zet_uit()
    
    @property
    def helderheid(self) -> int:
        return self._helderheid

    def _valideer_helderheid(self, niveau:int) -> int:
            if not 0 <= niveau <= 100:
                self.logger.log(f"WAARSCHUWINGL Ongeldige helderheid ({niveau} voor {self.naam} waarde moet 0-100 zijn!)")
                return max(0, min(niveau, 100))
            return niveau
    
    def pas_helderheid_aan(self, niveau:int):
         self._helderheid = self._valideer_helderheid(niveau)
         self.logger.log(f"DEBUG: Helderheid van {self.naam} aangepast naar {self.helderheid}%")

        # Zie redenering hierboven in mijn constructor, eerst daar
        # ook gezet maar na de @property voor helderheid toe te voegen
        # is het enkel hier ook goed want we roepen pas_helderheid al aan
        # in de constructor. dit is DRY als ik me niet vergis.
         if self.helderheid > 0 and not self.status:
            super().zet_aan()
         elif self.helderheid == 0 and self.status:
            super().zet_uit()

    def get_status_details(self) -> str:
        return f"Helderheid: {self.helderheid}%"
    
    def zet_aan(self):
        super().zet_aan()

        # lamp aangezet met 0 helderheid? Automatisch naar 100.
        if self.helderheid == 0 and self.status:
            self.pas_helderheid_aan(100)
    