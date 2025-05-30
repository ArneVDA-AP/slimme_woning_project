class Woning:
    def __init__(self, naam:str, smarthub_object):
        self.naam:str = naam
        self.kamers: dict = {}
        self.bewoners: list = []
        self.smarthub = smarthub_object


        if self.smarthub:

            try:
                self.smarthub.set_woning(self)
            except AttributeError:
                self.logger.log(f"Waarschuwing: Smarthub obj heeft gn set_woning methode,"
                      f"kan woning {self.naam} niet koppelen aan de hub {self.smarthub}")
    
    def voeg_kamer_toe(self, kamer_obj):
        if kamer_obj.naam not in self.kamers:
            self.kamers[kamer_obj.naam] = kamer_obj
            self.logger.log(f"Debug: kamer {kamer_obj.naam} toegevoegd aan {self.naam}")
        else:
            self.logger.log(f"DEBUG: kamer{kamer_obj.naam} bestaat al in woning.")
    
    def get_kamer(self, kamer_naam:str):
        return self.kamers.get(kamer_naam)
    
    def voeg_bewoner_toe(self, bewoner_obj):
        if bewoner_obj not in self.bewoners:
            self.bewoners.append(bewoner_obj)

            self.logger.log(f"DEBUG: Bewoner {bewoner_obj.naam} toegevoegd aan {self.naam}")
        else:
            self.logger.log(f"DEBUG: Bewoner {bewoner_obj.naam} al in woning aanwezig.")

    def get_alle_apparaten(self) -> list:
        alle_app_lijst = []
        for kamer_obj in self.kamers.values(): # zelfde als for kamer of kamers in TS/JS
            alle_app_lijst.extend(kamer_obj.get_apparaten())
        return alle_app_lijst
    
    def __str__(self) -> str:
        header = f"--Woning-- {self.naam} --\n"

        kamers_info = "Kamers: "
        if not self.kamers:
            kamers_info += "Geen kamers in de woning\n"
        else:
            for kamer_naam in self.kamers.keys():
                kamers_info += f" {kamer_naam}\n"

        bewoner_info = "Bewoners:\n "
        if not self.bewoners:
            bewoner_info += "Geen bewoners in de woning"
        else:
            for bewoner in self.bewoners:
                bewoner_info += f"{str(bewoner)}\n"
        if self.smarthub.naam:
            smarthub_info = f"smarthub {self.smarthub.naam}"
        else:
            smarthub_info = "Geen smarthub ingesteld>?"

        return header+ "\n" + kamers_info + "\n" + bewoner_info + "\n" + smarthub_info
    