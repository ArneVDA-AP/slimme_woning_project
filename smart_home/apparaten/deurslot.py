from .apparaat_basis import Apparaat;

class Deurslot(Apparaat):
    def __init__(self, naam:str, kamer=None, logger_instance=None):
        super().__init__(naam, kamer, logger_instance=logger_instance)
        
    def vergrendel(self):
        if not self.status:
            super().zet_aan() # aan = true dus in dit geval VERgrendel
            self.logger.log(f"DEBUG: Deurslot {self.naam} VERgrendeld")
        else:
            self.logger.log(f"DEBUG: Deurslot {self.naam} was al VERgrendeld")
    def ontgrendel(self):
        if self.status:
            super().zet_uit() # omgekeerde v vergrendel
            self.logger.log(f"DEBUG: Deurslot {self.naam} ONTgrendeld")

        else:
            self.logger.log(f"DEBUG: Deurslot {self.naam} was al ONTgrendeld")
            
    def get_status_details(self) -> str:
        if self.status:
            return "Status: Op slot"
        else:
            return "Status: Ontgrendeld"
        
    