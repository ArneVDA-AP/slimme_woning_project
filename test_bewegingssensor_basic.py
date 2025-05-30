from smart_home.apparaten.bewegingssensor import Bewegingssensor

sensor1 = Bewegingssensor(naam="TestSensor1")
print(sensor1)
print(f"Details: {sensor1.get_status_details()}")

assert sensor1.status is True
assert sensor1.beweging_gedetecteerd is False

sensor1.detecteer_beweging()
print(f"Details: {sensor1.get_status_details()}")
assert sensor1.beweging_gedetecteerd is True

print("\n verwacht: geen beweging gedetecteerd")
sensor1.detecteer_beweging()

sensor1.reset_sensor()
print(f"Details: {sensor1.get_status_details()}")
assert sensor1.beweging_gedetecteerd is False

sensor1.zet_uit()
print(sensor1)
print("\n verwacht: sensor uit")
sensor1.detecteer_beweging()
print(f"Details: {sensor1.get_status_details()}")
assert sensor1.beweging_gedetecteerd is False