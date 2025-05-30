from .apparaat_basis import Apparaat;



class Thermostaat(Apparaat):
    MIN_TEMP = 10.0
    MAX_TEMP = 30.0

    def __init__(self, naam, kamer=None, ingestelde_temp: float = 20.0, logger_instance=None):
        super().__init__(naam, kamer, logger_instance=logger_instance)
        self._ingestelde_temp: float = self.MIN_TEMP
        self.stel_temp_in(ingestelde_temp)

        # if not self.status:
        #     super().zet_aan()

    # vergelijkbaar met valideer_helderheid maar dan voor temp, :.1f voor de float zodat het altijd .x is
    def _valideer_temperatuur(self, temp: float) -> float:
        if not self.MIN_TEMP <= temp <= self.MAX_TEMP:
            self.logger.log(f"WAARSCHUWING: Ongeldige temperatuur {temp}C voor {self.naam} "
                  f"Wordt beperkt tot {self.MIN_TEMP:.1f} - {self.MAX_TEMP:.1f}")
            return max(self.MIN_TEMP, min(temp,self.MAX_TEMP))
        return temp

    def stel_temp_in(self, gradenC: float):
        self._ingestelde_temp = self._valideer_temperatuur(gradenC)
        self.logger.log(f"DEBUG: Ingestelde temperatuur van {self.naam} veranderd naar {self._ingestelde_temp:.1f}C")

        # gewoon voor de zekerheid aanzetten. Kans is klein dat de thermostaat
        # uit staat maar toch. Als we een temp instellen gaat die dus aan.
        # niet echt DRY eigenlijk. dus ik ga ze toch uit constructor wegdoen
        if not self.status:
            super().zet_aan()

    @property
    def ingestelde_temp(self) -> float:
        return self._ingestelde_temp

    def get_status_details(self) -> str:
        return f"Ingesteld: {self.ingestelde_temp:.1f}C"

