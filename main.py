import random
import time;

from smart_home.apparaten.lamp import Lamp
from smart_home.apparaten.thermostaat import Thermostaat
from smart_home.apparaten.deurslot import Deurslot
from smart_home.apparaten.bewegingssensor import Bewegingssensor
from smart_home.apparaten.rookmelder import Rookmelder
from smart_home.apparaten.gordijn import Gordijn

from smart_home.kamers.kamer import Kamer
from smart_home.bewoners.bewoner import Bewoner
from smart_home.core.woning import Woning
from smart_home.core.smarthub import SmartHub

from smart_home.utils.logger import Logger
from smart_home.utils.html_generator import HTMLGenerator

def setup_woning():
    # logger en logbestand path
    log_bestandsnaam = "smart_home_log.log"
    logger = Logger(log_bestandsnaam)
    # smarthub
    hub = SmartHub(logger, "Smarthub 1")
    # woning naam geven en koppelen met hub
    woning = Woning(naam="Slimme woning", smarthub_object=hub)

    logger.log(f"Woning {woning.naam} succesvol aangemaaktt en smarthub {hub.naam} gekoppeld","SETUP")

    # kamers en aan wonign toevoegen
    living = Kamer(naam="Living")
    keuken = Kamer(naam="Keuken")
    slaapkamer_groot = Kamer(naam="Slaapkamer groot")
    slaapkamer_klein = Kamer(naam="Slaapkamer klein")
    badkamer1e = Kamer(naam="Badkamer 1e Verdiep")
    badkamer2e = Kamer(naam="Badkamer 2e Verdiep")
    bureau = Kamer(naam="Bureau")

    woning.voeg_kamer_toe(living)
    woning.voeg_kamer_toe(keuken)
    woning.voeg_kamer_toe(slaapkamer_groot)
    woning.voeg_kamer_toe(slaapkamer_klein)
    woning.voeg_kamer_toe(badkamer1e)
    woning.voeg_kamer_toe(badkamer2e)
    woning.voeg_kamer_toe(bureau)

    #apparaten in kamers zetten
    #living
    lamp_living_luster = Lamp(naam="Lamp Living Luster")
    living.voeg_apparaat_toe(lamp_living_luster)

    thermo_living = Thermostaat(naam="Thermostaat in Living", ingestelde_temp= 21.0)
    living.voeg_apparaat_toe(thermo_living)

    gordijn_living_tuin = Gordijn(naam="Gordijn Living met Zicht op Tuin")
    living.voeg_apparaat_toe(gordijn_living_tuin)

    bewegings_sensor_living = Bewegingssensor(naam="Beweginssensor Living", smarthub_ref=hub)
    living.voeg_apparaat_toe(bewegings_sensor_living)

    #keuken
    lamp_keuken_ledstrip = Lamp(naam="Lamp Keuken ledstrip", helderheid=95)
    keuken.voeg_apparaat_toe(lamp_keuken_ledstrip)

    Rookmelder_keuken = Rookmelder(naam="Rookmelder keuken", smarthub_ref=hub)
    keuken.voeg_apparaat_toe(Rookmelder_keuken)

    #slaapkamer groot
    lamp_slk_groot = Lamp(naam="Lamp Slaapkamer groot")
    slaapkamer_groot.voeg_apparaat_toe(lamp_slk_groot)
    lamp_slk_groot_nacht = Lamp (naam="Nachtlamp Slaapkamer Groot")
    slaapkamer_groot.voeg_apparaat_toe(lamp_slk_groot_nacht)
    deurslot_slk_groot = Deurslot(naam="Slot Slaapkamer groot")
    slaapkamer_groot.voeg_apparaat_toe(deurslot_slk_groot)
    gordijn_slk_groot = Gordijn(naam="Gordijn Slaapkamer Groot")
    slaapkamer_groot.voeg_apparaat_toe(gordijn_slk_groot)
    thermo_slk_groot = Thermostaat(naam="Thermostaat Slaapkamer groot", ingestelde_temp=18.0)
    slaapkamer_groot.voeg_apparaat_toe(thermo_slk_groot)

    #slaapkamer klein
    
    lamp_slk_klein = Lamp(naam="Lamp Slaapkamer klein")
    slaapkamer_klein.voeg_apparaat_toe(lamp_slk_klein)
    lamp_slk_klein_nacht = Lamp (naam="Nachtlamp Slaapkamer klein")
    slaapkamer_klein.voeg_apparaat_toe(lamp_slk_klein_nacht)
    deurslot_slk_klein = Deurslot(naam="Slot Slaapkamer klein")
    slaapkamer_klein.voeg_apparaat_toe(deurslot_slk_klein)
    gordijn_slk_klein = Gordijn(naam="Gordijn Slaapkamer klein")
    slaapkamer_klein.voeg_apparaat_toe(gordijn_slk_klein)
    thermo_slk_klein = Thermostaat(naam="Thermostaat Slaapkamer klein", ingestelde_temp=18.0)
    slaapkamer_klein.voeg_apparaat_toe(thermo_slk_klein)

    #badkamer1e
    lamp_badkamer1e = Lamp(naam="Lamp Badkamer 1e")
    badkamer1e.voeg_apparaat_toe(lamp_badkamer1e)
    deurslot_badkamer1e = Deurslot(naam="Slot badkamer 1e")
    badkamer1e.voeg_apparaat_toe(deurslot_badkamer1e)

    #badkamer2e
    lamp_badkamer1e = Lamp(naam="Lamp Badkamer 2e")
    badkamer2e.voeg_apparaat_toe(lamp_badkamer1e)
    deurslot_badkamer2e = Deurslot(naam="Slot badkamer 2e")
    badkamer2e.voeg_apparaat_toe(deurslot_badkamer2e)

    #bewoners

    arne = Bewoner(naam="Arne")
    clara = Bewoner(naam="clara")

    woning.voeg_bewoner_toe(arne)
    woning.voeg_bewoner_toe(clara)

    arne.verplaats(living, logger_instance=logger)
    clara.verplaats(keuken, logger_instance=logger)

    logger.log("Apparaten en bewoners toegevoegd en bewoners verplaatst met logger attached", "SETUP")

    print("Setup woning voltooid.")

    return woning, logger, hub


def simuleer_tijdstap(woning_obj, logger_obj, hub_obj):
    pass


if __name__ == "__main__": # zou ervoor moeten zorgen dat ik main.py enkel rehctstreeks kan uitvoeren
                            #en dus niet als ik het geimporteerd heb.
    mijn_woning, mijn_logger, mijn_hub = setup_woning() # zelfde vorlgorde als de returns

    print("\n Woning realtime")
    print(mijn_woning)

    html_gen = HTMLGenerator()

    html_gen.gen_site(woning_obj=mijn_woning, logger_obj=mijn_logger)

    mijn_logger.close()

    print(f"normaal gezien zou de html moeten gegenerate zijn... check {html_gen.output_map} voor index.html")


