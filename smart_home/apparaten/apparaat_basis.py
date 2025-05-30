from abc import ABC, abstractmethod;

class Apparaat(ABC):
    def __init__(self, naam: str, kamer=None, logger_instance=None):
        self.naam: str = naam
        self._status: bool = False
        self.kamer = kamer
        self.logger = logger_instance

        if self.logger:
            kamer_naam_str = self.kamer.naam if self.kamer else "geen kamer"
            self.logger.log(f"Apparaat {self.naam} aangemaakt, {type(self).__name__} in {kamer_naam_str}", "APPCONFIG")

    def zet_aan(self):
        if not self._status:
            self._status = True
            # TODO Logger implementeren voor alle prints.
            # Denk aan deze comment en doe hem pas weg als ik alle prints
            # heb vervangen.
            self.logger.log(f"DEBUG: Apparaat '{self.naam}' AAN gezet.")
        else:
            self.logger.log(f"DEBUG: Apparaat '{self.naam}' was al AAN.")

    def zet_uit(self):
        if self._status:
            self._status = False
            self.logger.log(f"DEBUG: Apparaat '{self.naam}' UIT gezet.")
        else:
            self.logger.log(f"DEBUG: Apparaat '{self.naam}' was al UIT.")
            
    def toggle_status(self):
        self._status = not self._status
        status_tekst = "AAN" if self._status else "UIT"
        self.logger.log(f"DEBUG: Apparaat '{self.naam}' status getoggled naar {status_tekst}")

    @property
    def status(self) -> bool:
        return self._status

    # get_status_details moet door elke subclass zelf ingevuld worden.
    # dit is een beetje de 'kern' van waarom apparaat een abstracte class is
    @abstractmethod
    def get_status_details(self) -> str:
        pass

    def __str__(self) -> str:
        status_tekst = "AAN" if self.status else "UIT"

        kamer_info = "Niet ingesteld"
        if self.kamer:
            try:
                kamer_info = self.kamer.naam
            except AttributeError:
                # self.kamer is al wel ingesteld maar wss heeft
                # het nog geen .naam attribuut, of een 'typeerror'
                kamer_info = "Kamer naam onbekend. Bestaat .naam attribuut?"
        
        return f"Apparaat: {self.naam} (Kamer: {kamer_info}) - Status: {status_tekst}"

