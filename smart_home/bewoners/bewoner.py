class Bewoner:
    def __init__(self, naam:str):
        self.naam: str = naam
        self.huidige_kamer = None
        # self.logger = None

    def verplaats(self, nieuwe_kamer_obj, logger_instance=None):
        oude_kamer_naam = ""
        if self.huidige_kamer:
            oude_kamer_naam = self.huidige_kamer.naam

            self.huidige_kamer = nieuwe_kamer_obj

            nieuwe_kamer_naam = self.huidige_kamer.naam

            log_msg = f"Bewoner {self.naam} verplaatst van {oude_kamer_naam} naar {nieuwe_kamer_naam}"

            if logger_instance:
                logger_instance(log_msg, type_event="beweging")
            else:
                print(f"DEBUG: {log_msg}")

    def __str__(self)-> str:
        locatie = "Nog niet in een kamer"
        if self.huidige_kamer:
            try:
                locatie = f"in kamer {self.huidige_kamer.naam}"
            except AttributeError:
                locatie= "in kamer zonder naam, niet echt mogelijk..."
        return f"Bewoner: {self.naam} in {locatie}"
    
    