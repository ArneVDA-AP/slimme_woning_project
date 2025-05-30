from .apparaat_basis import Apparaat

class Rookmelder(Apparaat):
    def __init__(self, naam:str, kamer=None, smarthub_ref=None):
        super().__init__(naam, kamer)
        self._rook_gedetecteerd: bool = False
        self._alarm_actief: bool = False
        self.smarthub = smarthub_ref

        if not self.status:
            super().zet_aan()

    def detecteer_rook(self):
        if not self.status:
            print(f"DEBUG: Rook,elder {self.naam} staat UIT en kan niet dtecteren.")
            return

        if not self._rook_gedetecteerd:
            self._rook_gedetecteerd = True
            self._alarm_actief = True

            print(f"ALARM! Rook gedetecteerd door {self.naam}! Alarm geactiveerd")

            if self.smarthub:
                try:
                    data = {"kamer_naam": self.kamer.naam if self.kamer else "Onbekend, Geen kamer"}
                    self.smarthub.ontvang_notificatie(
                        apparaat=self,
                        event_type="rook_alarm",
                        data=data
                    )
                    print(f"DEBUG: Notificatie 'rook alarm' gestuurd naar smarthub door {self.naam}")
                except Exception as e:
                    print(f"FOUT: Onverwachte fout van {self.naam} fout: {e}")

    def reset_alarm(self):
        if self._alarm_actief or self._rook_gedetecteerd:
            self._rook_gedetecteerd = False
            self._alarm_actief = False

            print(f"Alarm en rookalarm voor {self.naam} gereset.")

            #later ook reset notificatie smarthub schrijven
    @property
    def rook_gedetecteerd(self) -> bool:
        return self._rook_gedetecteerd
    @property
    def alarm_actief(self) -> bool:
        return self._alarm_actief
    
    def get_status_details(self) -> str:
        rook_status_tekst = "Geen rook"
        if self.rook_gedetecteerd:
            rook_status_tekst = "ROOK!!!"
            if self.alarm_actief:
                rook_status_tekst += "ALARM!!!!"
        sensor_actief_status = "Actief" if self.status else "inactief"
        return f"Sensor: {sensor_actief_status}. Rook: {rook_status_tekst}"
