from smart_home.apparaten.lamp import Lamp;


lamp1 = Lamp(naam="Testlamp1 dd")
print(lamp1)
print(f"Status: {lamp1.status} Details: {lamp1.get_status_details()}")
print("+_____+" * 5)

# lamp met helderheid 0 om helderheid 0 = status uit te testen

lamp2 = Lamp(naam="Testlamp2 ee", helderheid = 0)
print(lamp2)
print(f"Status: {lamp2.status} Details: {lamp2.get_status_details()}")
lamp2.pas_helderheid_aan(50)
print(lamp2)
print(f"Status: {lamp2.status} Details: {lamp2.get_status_details()}")
lamp2.zet_uit()
print(lamp2)
print(f"Status: {lamp2.status} Details: {lamp2.get_status_details()}")
print("+_____+" * 5)

# helderheid aanpassen testen

lamp1.pas_helderheid_aan(30)
print(lamp1)
print(f"Status: {lamp1.status} Details: {lamp1.get_status_details()}")
lamp1.pas_helderheid_aan(0)
print(lamp1)
print(f"Status: {lamp1.status} Details: {lamp1.get_status_details()}")
lamp1.zet_aan()
print(lamp1)
print(f"Status: {lamp1.status} Details: {lamp1.get_status_details()}")

# test ongeldige helderheid
lamp1.pas_helderheid_aan(1222)
print(lamp1)
print(f"Status: {lamp1.status} Details: {lamp1.get_status_details()}")
lamp1.pas_helderheid_aan(-333)
print(lamp1)
print(f"Status: {lamp1.status} Details: {lamp1.get_status_details()}")
