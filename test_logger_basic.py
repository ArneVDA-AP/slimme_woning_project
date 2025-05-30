import os;
from smart_home.utils.logger import Logger;

LOG_FILENAME = "testlog.log"

logger_memory = Logger()
logger_memory.log("eerste testbericht", "TEST")
logger_memory.log("Tweede testbericht", type_event="DEBUGMEME")
assert len(logger_memory.get_logs()) == 2
assert "eerste testbericht" in logger_memory.get_logs()[0]
assert "DEBUGMEME" in logger_memory.get_logs()[1]
logger_memory.close()
print("______" * 12)

logger_file = Logger(log_file_path=LOG_FILENAME)
assert os.path.exists(LOG_FILENAME)

logger_file.log("test bestandlog 1", "FILELOG")
logger_file.log("Test bestandlog 2", "DEBUGFILE")
assert len(logger_file.get_logs()) == 2

try:
    with open(LOG_FILENAME, "r", encoding="utf-8") as f:
        logs = f.read()
        print(f"{LOG_FILENAME}: \n{logs.strip()}")
        assert "test bestandlog 1" in logs
        assert "DEBUGFILE" in logs
except Exception as e:
    print(f"FOUT: P{LOG_FILENAME} niet gevonden.")
print("______" * 12)


logger_file.clear_logs()
assert len(logger_file.get_logs()) == 0

print(f"Logs na clear: {logger_file.get_logs()}")

try:
    with open(LOG_FILENAME, "r", encoding="utf-8") as f:
        logs_cleared = f.read()
        print(f"{LOG_FILENAME}: \n{logs_cleared.strip()}")
        assert "test bestandlog 1" in logs_cleared
except Exception as e:
    print(f"FOUT: P{LOG_FILENAME} niet gevonden.")
print("______" * 12)


# logger sluiten

logger_file.log("log voor sluiten", "PRECLOSE")
logger_file.close()
print("verwacht: fout want logger is gesloten")
try:
    logger_file.log("nenenenenen","mnenen")
except Exception as e:
    print(f"fout bij loggen na sluiten(duh): {e}")

