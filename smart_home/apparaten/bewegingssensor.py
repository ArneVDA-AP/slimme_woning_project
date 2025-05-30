from .apparaat_basis import Apparaat;

class Bewegingssensor (Apparaat):
    def __init__(self, naam:str, kamer=None, smarthub_ref=None):
        super().__init__(naam, kamer)
        self._beweging_gedetecteerd: bool = False
        self.smarthub = smarthub_ref

        if not self.status:
            super().zet_aan()
    
    def detecteer_beweging(self):
        if not self.status:
            print(f"DEBUG: Bewegingssensor {self.naam} staat UIT dus kan niet detecteren.")
            return
        if not self._beweging_gedetecteerd:
            self._beweging_gedetecteerd = True
            print(f"DEBUG: Beweging gedetecteerd door{self.naam}!")

            if self.smarthub:
                try:
                    self.smarthub.ontvang_notificatie(
                        apparaat=self,
                        event_type="beweging_gedetecteerd",
                        data={"kamer_naam":self.kamer.naam if self.kamer else "Onbekend, Geen kamer"}
                    )
                    print(f"DEBUG: Notificatie naat smarthub gestuurd door {self.naam}.")
                except AttributeError as e:
                    print(f"FOUT: Kon sSmarhub niet notificeren vanuit {self.naam}. Fout: {e}")
            else:
                print(f"WAARSCHUWING: Geen smarthun gekoppeld aan {self.naam}, notificatie kan niet gestuurd worden..")
                
    def reset_sensor(self):
        if self._beweging_gedetecteerd:
            self._beweging_gedetecteerd = False
            print(f"DEBUG: Sensor {self.naam} gereset, geen beweging meer.")
                
    @property
    def beweging_gedetecteerd(self)-> bool:
        return self._beweging_gedetecteerd

    def get_status_details(self) -> str:
        detectie_status = "Ja" if self._beweging_gedetecteerd else "Nee"
        sensor_status = "Actief" if self.status else "Inactief"
        return f"Sensor: {sensor_status} Beweging gedetecteerd: {detectie_status}"