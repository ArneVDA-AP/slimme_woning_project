class Bewoner:
    def __init__(self, naam:str, logger_instance=None):
        self.naam: str = naam
        self.huidige_kamer = None
        self.logger = logger_instance

        if self.logger:
            self.logger.log(f"{self.naam}'angemaakt.", "BEWONER_CONF")

    def verplaats(self, nieuwe_kamer_obj, logger_instance=None):
        oude_kamer_naam = " "
        if self.huidige_kamer:
            oude_kamer_naam = getattr(self.huidige_kamer,"naam","onbekende oude kamer")

        self.huidige_kamer = nieuwe_kamer_obj

        nieuwe_kamer_naam = "None"
        if self.huidige_kamer:
            nieuwe_kamer_naam = getattr(self.huidige_kamer, "naam", "Onbekende nieuwe kamer")
            self.logger.log(f"DEBUG: verplaats: {self.naam} huidige kamer is nu:"
                  f"{self.huidige_kamer.naam if self.huidige_kamer.naam else 'None'}")

            nieuwe_kamer_naam = self.huidige_kamer.naam

            log_msg = f"Bewoner {self.naam} verplaatst van {oude_kamer_naam} naar {nieuwe_kamer_naam}"

            if logger_instance:
                logger_instance.log(log_msg, type_event="BEWEGING")
            else:
                self.logger.log(f"DEBUG: {log_msg}")

    def __str__(self)-> str:

        self.logger.log(f"DEBUG: __Str__: {self.naam} huidige kamer is nu:"
            f"{self.huidige_kamer.naam if self.huidige_kamer.naam else 'None'}")

        
        locatie = "Nog niet in een kamer"
        if self.huidige_kamer:
            try:
                locatie = f"in kamer {self.huidige_kamer.naam}"
            except AttributeError:
                locatie= "in kamer zonder naam, niet echt mogelijk..."
        return f"{self.naam} in {locatie}"
    
    