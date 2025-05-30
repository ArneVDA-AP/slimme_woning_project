from apparaten.lamp import Lamp;

class SmartHub:
    def __init__(self, logger_instance, naam:str = "Default Smarthub"):
        self.naam:str = naam
        self.logger = logger_instance
        self.woning = None
        self.regels: list = []
        self.actief_scenario: str = "standaard"

        if self.logger:
            self.logger.log(f"Smarthub {self.naam} gestart", "HUB")
        else:
            print(f"Smarthub {self.naam} gestart maar zonder logger")
        
    def set_woning(self, woning_obj):
        self.woning = woning_obj
        if self.logger:
            self.logger.log(f"{self.naam} gekoppeld aan woning.", "HUB")
        else:
            print(f"{self.naam} gekoppeld aan woning. geen logger")
    
    def ontvang_notificatie(self, apparaat, event_type:str, data: dict = {}):
        apparaat_naam = getattr(apparaat, "naam", "geen apparaatnaam ingesteld")
        log_msg = (f"self.naam notificatie ontvangen:"
                   f"Apparaat: {apparaat_naam}, event: {event_type}"
                   f"data:{data}")
        
        if self.logger:
            self.logger.log(log_msg,"HUB")
        else:
            print(f"{log_msg}")

        self.verwerk_notif(apparaat, event_type, data)

    def verwerk_notif(self, apparaat, event_type:str, data: dict):
        log_msg = f"{self.naam} verwerkt: Event: {event_type}, data:{data}"

        if self.logger:
            self.logger.log(log_msg, "HUB")
        else:
            print(f"DEBUG: {log_msg}")

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
                                print(f"lamp {appar_in_kamer.naam} in kamer {kamer_naam_beweging} AAN door beweging.")
            else:
                if self.logger:
                    self.logger.log(f"geen kamernaam of woning gevonden","HUB") 

        elif event_type == "rook_alarm":
            kamer_naam_rook = data.get("kamer_naam", "Kamer onbekend, niet ingesteld")
            msg = f"ROOKALARM!!!! kamer {kamer_naam_rook} rookmelder: {getattr(apparaat, "naam", "Onbekend, geen rookmelder ingesteld")}"

            if self.logger:
                self.logger.log(msg, "ROOKALARM")
            else:
                print(f"ALARM! {msg}")

        else:
            if self.logger:
                self.logger.log("onbekende event type", "HUB")