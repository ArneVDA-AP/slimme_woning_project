import datetime;

class Logger:
    def __init__(self, log_file_path:str = None):
        self.log_entries = []
        self.log_file_path:str | None = log_file_path # Unions zoals in TS. i love python

        if self.log_file_path:
            try:
                self.file_geopend = open(self.log_file_path, "a+", encoding="utf-8")
                print(f"INFO: Logbestand: {self.log_file_path}")
            except Exception as e:
                print(f"FOUT: kon log {self.log_file_path} niet openen/aanmaken. fout: {e}")

                self.file_geopend = None
                self.log_file_path = None
        
        else:
            self.file_geopend = None

    
    def log(self, msg:str, type_event:str="INFO"):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        log_entry_str = f"{timestamp} - {type_event} - {msg}"

        self.log_entries.append(log_entry_str)
        print(log_entry_str)

        if self.file_geopend:
            try:
                self.file_geopend.write(f"{log_entry_str}\n")
                self.file_geopend.flush() # direct schrijvene

            except Exception as e:
                print(f"FOUT: Kon niet naar logbestand {self.log_file_path} schrijven, fout: e")

    def get_logs(self) -> list[str]:
        return self.log_entries
    
    def clear_logs(self):
        if self.log_entries != []:
            self.log_entries = []
            print(f"INFO: logs gewist, staan nog wel in logbestand {self.log_file_path}")
        else:
            print("intern loggeheugen was al of nog leeg. niets om te wissen")

    def close(self):
        if self.file_geopend:
            try:
                self.log("Logger sluiten", type_event="SYSTEEM")
                self.file_geopend.close()
                self.file_geopend = None
            except Exception as e:
                print(f"FOUT bij het sluiten logbestand '{self.log_file_path}'. Fout: {e}")
    