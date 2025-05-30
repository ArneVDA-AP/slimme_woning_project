from ..apparaten.lamp import Lamp;

class SmartHub:
    def __init__(self, logger_instance, naam:str = "Default Smarthub"):
        self.naam:str = naam
        self.logger = logger_instance
        self.woning = None
        self.regels: list[dict] = []
        self.actief_scenario: str = "standaard"

        if self.logger:
            self.logger.log(f"Smarthub {self.naam} gestart", "HUB")
        else:
            self.logger.log(f"Smarthub {self.naam} gestart maar zonder logger")
        
    def set_woning(self, woning_obj):
        self.woning = woning_obj
        if self.logger:
            self.logger.log(f"{self.naam} gekoppeld aan woning.", "HUB")
        else:
            self.logger.log(f"{self.naam} gekoppeld aan woning. geen logger")


    def registreer_regel(self, regel_dict:dict):
        self.regels.append(regel_dict)
        if self.logger:
            self.logger.log(f"Nieuwe regel geregistreert in Smarthub {self.naam}"
                            f"regel: {regel_dict}")
        

    def ontvang_notificatie(self, apparaat, event_type:str, data: dict = {}):
        apparaat_naam = getattr(apparaat, "naam", "geen apparaatnaam ingesteld")
        log_msg = (f"self.naam notificatie ontvangen:"
                   f"Apparaat: {apparaat_naam}, event: {event_type}"
                   f"data:{data}")
        
        if self.logger:
            self.logger.log(log_msg,"HUB")
        else:
            self.logger.log(f"{log_msg}")

        # self.verwerk_notif(apparaat, event_type, data)
        self._evalueer_en_voer_regels_uit(event_type, data, trigger_apparaat=apparaat)
    
    def _evalueer_en_voer_regels_uit(self, getriggered_event_type:str, event_data: dict, trigger_apparaat):
        if not self.woning:
            if self.logger: self.logger.log("geen woning gekoppeld, kan geen regels uitvoeren")
            return
        
        for regel_index, regel in enumerate(self.regels):
            if regel.get("trigger_event") == getriggered_event_type:
                
                kamer_conditie = regel.get("kamer_naam_conditie")
                event_kamer = event_data.get("kamer_naam")
                if kamer_conditie and (not event_kamer or event_kamer != kamer_conditie):
                    continue #volgende kamer moet regel krijgen niet deze
                if self.logger:
                    self.logger.log(f"{regel_index+1} getriggered: {regel}")
                actie_apparaat_naam = regel.get("actie_apparaat_naam")
                actie_methode_naam = regel.get("actie_methode")
                actie_waarde = regel.get("actie-waarde")

                if not actie_apparaat_naam or not actie_methode_naam:
                    if self.logger:self.logger.log(f" regel {regel_index+1} is nie compleet mist app of method")
                    continue

                doel_apparaat = None
                for app_in_woning in self.woning.get_alle_apparaten():
                    if app_in_woning.naam == actie_apparaat_naam:
                        doel_apparaat = app_in_woning
                        break
                if doel_apparaat:
                    if hasattr(doel_apparaat, actie_methode_naam):
                        methode_aant_e_roepen = getattr(doel_apparaat, actie_methode_naam)
                        
                        try:
                            if actie_waarde is not None:
                                methode_aant_e_roepen(actie_waarde)
                            else:
                                methode_aant_e_roepen()
                        except Exception as e:
                            if self.logger: self.logger.log("Voert actie uit")
                    else:
                        print(f"acite methode niet gevonden op apparaat {doel_apparaat.naam}")

            if getriggered_event_type == "rook_alarm":
                kamer_naam_rook = event_data.get("kaner_naam", "locatie onbekend")
                apparaat_naam_rook = getattr(trigger_apparaat, "naam", "gn apparaat")
                msg = f"Dringend rookalarm in {kamer_naam_rook} sensor {apparaat_naam_rook}"

                if self.logger: self.logger.log(msg)
                else:
                    print(msg)

    def verwerk_notif(self, apparaat, event_type:str, data: dict):
        log_msg = f"{self.naam} verwerkt: Event: {event_type}, data:{data}"

        if self.logger:
            self.logger.log(log_msg, "HUB")
        else:
            self.logger.log(f"DEBUG: {log_msg}")

        if event_type == "beweging_gedetecteerd":
            kamer_naam_beweging = data.get("kamer_naam")
            if kamer_naam_beweging and self.woning:
                kamer_obj = self.woning.get_kamer(kamer_naam_beweging)

                if kamer_obj:
                    for appar_in_kamer in kamer_obj.get_apparaten():
                        if isinstance(appar_in_kamer, Lamp) and not appar_in_kamer.status:
                            appar_in_kamer.zet_aan()
                            if self.logger:
                                self.logger.log(f"lamp {appar_in_kamer.naam} in kamer {kamer_naam_beweging} AAN door beweging.", "HUB")
                            else:
                                self.logger.log(f"lamp {appar_in_kamer.naam} in kamer {kamer_naam_beweging} AAN door beweging.")
            else:
                if self.logger:
                    self.logger.log(f"geen kamernaam of woning gevonden","HUB") 

        elif event_type == "rook_alarm":
            kamer_naam_rook = data.get("kamer_naam", "Kamer onbekend, niet ingesteld")
            msg = f"ROOKALARM!!!! kamer {kamer_naam_rook} rookmelder: {getattr(apparaat, "naam", "Onbekend, geen rookmelder ingesteld")}"

            if self.logger:
                self.logger.log(msg, "ROOKALARM")
            else:
                self.logger.log(f"ALARM! {msg}")

        else:
            if self.logger:
                self.logger.log("onbekende event type", "HUB")