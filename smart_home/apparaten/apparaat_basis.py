from abc import ABC, abstractmethod;

class Apparaat(ABC):
    def __init__(self, naam: str, kamer=None):
        self.naam: str = naam
        self._status: bool = False
        self.kamer = kamer
        # self.logger = None

    def zet_aan(self):
        if not self._status:
            self._status = True
            # TODO Logger implementeren voor alle prints.
            # Denk aan deze comment en doe hem pas weg als ik alle prints
            # heb vervangen.
            print(f"DEBUG: Apparaat '{self.naam}' AAN gezet.")
        else:
            print(f"DEBUG: Apparaat '{self.naam}' was al AAN.")

    def zet_uit(self):
        if self._status:
            self._status = False
            print(f"DEBUG: Apparaat '{self.naam}' UIT gezet.")
        else:
            print(f"DEBUG: Apparaat '{self.naam}' was al UIT.")
            
    def toggle_status(self):
        self._status = not self._status
        status_tekst = "AAN" if self._status else "UIT"
        print(f"DEBUG: Apparaat '{self.naam}' status getoggled naar {status_tekst}")

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
        
        return f"Apparaat: {self.naam} (Kaner: {kamer_info}) - Status: {status_tekst}"

