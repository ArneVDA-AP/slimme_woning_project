from smart_home.apparaten.gordijn import Gordijn;

gordijn1 = Gordijn(naam="testgordijn1")
print(gordijn1)
print(f"Details: {gordijn1.get_status_details()}")

assert gordijn1.status is True
assert gordijn1.positie == "gesloten"
print("=" * 22)

gordijn1.open_gordijn()
print(gordijn1)
print(f"Details: {gordijn1.get_status_details()}")
assert gordijn1.positie == "open"
gordijn1.open_gordijn()
print("=" * 22)

gordijn1.sluit_gordijn()
print(gordijn1)
print(f"Details: {gordijn1.get_status_details()}")
assert gordijn1.positie == "gesloten"
print("="* 23)

gordijn1.stel_positie_in("half open")
print(gordijn1)
print(f"Details: {gordijn1.get_status_details()}")
assert gordijn1.positie == "half open"

gordijn1.stel_positie_in("foutoutouf")
print(gordijn1)
print(f"Details: {gordijn1.get_status_details()}")
assert gordijn1.positie == "half open"
print("=" * 22)

gordijn1.zet_uit()
print(gordijn1)
print(f"Details: {gordijn1.get_status_details()}")
gordijn1.open_gordijn()
print("="*23)

gordijnfout = Gordijn(naam="foutgordijn", begin_positie="dididid")
print(gordijnfout)
print(f"Details: {gordijnfout.get_status_details()}")
assert gordijnfout.positie == "gesloten"
