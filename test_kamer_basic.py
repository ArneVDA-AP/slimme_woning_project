from smart_home.apparaten.lamp import Lamp
from smart_home.apparaten.thermostaat import Thermostaat
from smart_home.kamers.kamer import Kamer;

testKamertje = Kamer(naam="Testkamertje")
print(testKamertje)
assert testKamertje.naam == "Testkamertje"
assert len(testKamertje.get_apparaten()) == 0
print("..."* 15)

lamp_testkamertje = Lamp(naam="testlamp1")
thermo_testkamertje = Thermostaat(naam="testthermo1")

testKamertje.voeg_apparaat_toe(lamp_testkamertje)
testKamertje.voeg_apparaat_toe(thermo_testkamertje)

print(testKamertje)

assert len(testKamertje.get_apparaten()) == 2
assert lamp_testkamertje in testKamertje.get_apparaten()
assert thermo_testkamertje in testKamertje.get_apparaten()

assert lamp_testkamertje.kamer == testKamertje
assert thermo_testkamertje.kamer == testKamertje

if lamp_testkamertje.kamer:
    print(f"Lamp kamer {lamp_testkamertje.kamer.naam}")
else:
    print(f"Geen kamer voor {lamp_testkamertje}")

if thermo_testkamertje.kamer:
    print(f"Lamp kamer {thermo_testkamertje.kamer.naam}")
else:
    print(f"Geen kamer voor {thermo_testkamertje}")

testKamertje.verwijder_apparaat("testlamp1")
print(testKamertje)
assert len(testKamertje.get_apparaten()) == 1
assert lamp_testkamertje not in testKamertje.get_apparaten()

assert lamp_testkamertje.kamer is None
if lamp_testkamertje.kamer:
    print(f"Lamp kamer {lamp_testkamertje.kamer.naam}")
else:
    print(f"Geen kamer voor {lamp_testkamertje}")

testKamertje.voeg_apparaat_toe(lamp_testkamertje)
assert len(testKamertje.get_apparaten()) == 2
testKamertje.verwijder_apparaat(lamp_testkamertje)
print(testKamertje)
assert len(testKamertje.get_apparaten()) == 1
assert lamp_testkamertje not in testKamertje.get_apparaten()
assert lamp_testkamertje.kamer is None

print("..."* 15)

# fout object/naam. niet bestaand proberen deleten
testKamertje.verwijder_apparaat("blaalalalal")
assert len(testKamertje.get_apparaten()) == 1
print("..."* 15)

print("Test gedaan")