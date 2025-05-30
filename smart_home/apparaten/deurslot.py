from .apparaat_basis import Apparaat;

class Deurslot(Apparaat):
    def __init__(self, naam:str, kamer=None):
        super().__init__(naam, kamer)

    def vergrendel(self):
        if not self.status:
            super().zet_aan() # aan = true dus in dit geval VERgrendel
            print(f"DEBUG: Deurslot {self.naam} VERgrendeld")
        else:
            print(f"DEBUG: Deurslot {self.naam} was al VERgrendeld")
    def ontgrendel(self):
        if self.status:
            super().zet_uit() # omgekeerde v vergrendel
            print(f"DEBUG: Deurslot {self.naam} ONTgrendeld")

        else:
            print(f"DEBUG: Deurslot {self.naam} was al ONTgrendeld")
            
    def get_status_details(self) -> str:
        if self.status:
            return "Status: Op slot"
        else:
            return "Status: Ontgrendeld"
        
    