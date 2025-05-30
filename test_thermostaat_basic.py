from smart_home.apparaten.thermostaat import Thermostaat

thermo1 = Thermostaat(naam="TestThermostaat1 ff")
print(thermo1)
print(f"Status: {thermo1.status}, Details: {thermo1.get_status_details()}")

assert thermo1.status is True
assert thermo1.ingestelde_temp == 20.0
print("--" * 10)

# specifieke temp
thermo2 = Thermostaat(naam="TestThermostaat2 fd", ingestelde_temp=18.5)
print(thermo2)
print(f"Status: {thermo2.status}, Details: {thermo2.get_status_details()}")
# assert thermo2.status is True
assert thermo2.ingestelde_temp == 18.5
print("--" * 10)

# temp aanpassen bestaande thermo
thermo1.stel_temp_in(22.0)
print(thermo1)
print(f"Status: {thermo1.status}, Details: {thermo1.get_status_details()}")
assert thermo1.ingestelde_temp == 22.0
thermo1.zet_uit()
print(thermo1)
print(f"Status: {thermo1.status}, Details: {thermo1.get_status_details()}")
assert thermo1.status is False
thermo1.stel_temp_in(23.0)
print(thermo1)
print(f"Status: {thermo1.status}, Details: {thermo1.get_status_details()}")
assert thermo1.status is True
assert thermo1.ingestelde_temp == 23.0
print("--" * 10)

# ongeldige temp
thermo2.stel_temp_in(5.0) #kleiner dan MIN_TEMP
print(thermo2)
print(f"Status: {thermo2.status}, Details: {thermo2.get_status_details()}")
assert thermo2.ingestelde_temp == Thermostaat.MIN_TEMP

thermo2.stel_temp_in(35.0)
print(thermo2)
print(f"Status: {thermo2.status}, Details: {thermo2.get_status_details()}")
assert thermo2.ingestelde_temp == Thermostaat.MAX_TEMP
