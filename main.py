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
    woning = Woning(naam="Slimme woning", smarthub_object=hub, logger_instance=logger)

    logger.log(f"Woning {woning.naam} succesvol aangemaaktt en smarthub {hub.naam} gekoppeld","SETUP")

    #regels
    regel1 = {
        "trigger_event": "beweging_gedetecteerd",
        "kamer_naam_conditie": "Living",
       "actie_apparaat_naam": "Lamp Living Luster",
       "actie_methode": "zet_aan"
    }
    hub.registreer_regel(regel1)
    logger.log(f"{len(hub.regels)} regels geregistreerd bij SmartHub.", "SETUP")

    # kamers en aan wonign toevoegen
    living = Kamer(naam="Living", logger_instance=logger)
    keuken = Kamer(naam="Keuken", logger_instance=logger)
    slaapkamer_groot = Kamer(naam="Slaapkamer groot", logger_instance=logger)
    slaapkamer_klein = Kamer(naam="Slaapkamer klein", logger_instance=logger)
    badkamer1e = Kamer(naam="Badkamer 1e Verdiep", logger_instance=logger)
    badkamer2e = Kamer(naam="Badkamer 2e Verdiep", logger_instance=logger)
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
    lamp_living_luster = Lamp(naam="Lamp Living Luster", logger_instance=logger,helderheid=0)
    living.voeg_apparaat_toe(lamp_living_luster)

    thermo_living = Thermostaat(naam="Thermostaat in Living", ingestelde_temp= 21.0, logger_instance=logger)
    living.voeg_apparaat_toe(thermo_living)

    gordijn_living_tuin = Gordijn(naam="Gordijn Living met Zicht op Tuin", logger_instance=logger)
    living.voeg_apparaat_toe(gordijn_living_tuin)

    bewegings_sensor_living = Bewegingssensor(naam="Beweginssensor Living", smarthub_ref=hub, logger_instance=logger)
    living.voeg_apparaat_toe(bewegings_sensor_living)

    #keuken
    lamp_keuken_ledstrip = Lamp(naam="Lamp Keuken ledstrip", helderheid=95, logger_instance=logger)
    keuken.voeg_apparaat_toe(lamp_keuken_ledstrip)

    Rookmelder_keuken = Rookmelder(naam="Rookmelder keuken", smarthub_ref=hub, logger_instance=logger)
    keuken.voeg_apparaat_toe(Rookmelder_keuken)

    #slaapkamer groot
    lamp_slk_groot = Lamp(naam="Lamp Slaapkamer groot", logger_instance=logger)
    slaapkamer_groot.voeg_apparaat_toe(lamp_slk_groot)
    lamp_slk_groot_nacht = Lamp (naam="Nachtlamp Slaapkamer Groot", logger_instance=logger)
    slaapkamer_groot.voeg_apparaat_toe(lamp_slk_groot_nacht)
    deurslot_slk_groot = Deurslot(naam="Slot Slaapkamer groot", logger_instance=logger)
    slaapkamer_groot.voeg_apparaat_toe(deurslot_slk_groot)
    gordijn_slk_groot = Gordijn(naam="Gordijn Slaapkamer Groot", logger_instance=logger)
    slaapkamer_groot.voeg_apparaat_toe(gordijn_slk_groot)
    thermo_slk_groot = Thermostaat(naam="Thermostaat Slaapkamer groot", ingestelde_temp=18.0, logger_instance=logger)
    slaapkamer_groot.voeg_apparaat_toe(thermo_slk_groot)

    #slaapkamer klein
    
    lamp_slk_klein = Lamp(naam="Lamp Slaapkamer klein", logger_instance=logger)
    slaapkamer_klein.voeg_apparaat_toe(lamp_slk_klein)
    lamp_slk_klein_nacht = Lamp (naam="Nachtlamp Slaapkamer klein", logger_instance=logger)
    slaapkamer_klein.voeg_apparaat_toe(lamp_slk_klein_nacht)
    deurslot_slk_klein = Deurslot(naam="Slot Slaapkamer klein", logger_instance=logger)
    slaapkamer_klein.voeg_apparaat_toe(deurslot_slk_klein)
    gordijn_slk_klein = Gordijn(naam="Gordijn Slaapkamer klein", logger_instance=logger)
    slaapkamer_klein.voeg_apparaat_toe(gordijn_slk_klein)
    thermo_slk_klein = Thermostaat(naam="Thermostaat Slaapkamer klein", ingestelde_temp=18.0, logger_instance=logger)
    slaapkamer_klein.voeg_apparaat_toe(thermo_slk_klein)

    #badkamer1e
    lamp_badkamer1e = Lamp(naam="Lamp Badkamer 1e", logger_instance=logger)
    badkamer1e.voeg_apparaat_toe(lamp_badkamer1e)
    deurslot_badkamer1e = Deurslot(naam="Slot badkamer 1e", logger_instance=logger)
    badkamer1e.voeg_apparaat_toe(deurslot_badkamer1e)

    #badkamer2e
    lamp_badkamer1e = Lamp(naam="Lamp Badkamer 2e", logger_instance=logger)
    badkamer2e.voeg_apparaat_toe(lamp_badkamer1e)
    deurslot_badkamer2e = Deurslot(naam="Slot badkamer 2e", logger_instance=logger)
    badkamer2e.voeg_apparaat_toe(deurslot_badkamer2e)

    #bewoners

    arne = Bewoner(naam="Arne", logger_instance=logger)
    clara = Bewoner(naam="Clara", logger_instance=logger)

    woning.voeg_bewoner_toe(arne)
    woning.voeg_bewoner_toe(clara)

    arne.verplaats(living, logger_instance=logger)
    clara.verplaats(keuken, logger_instance=logger)

    logger.log("Apparaten en bewoners toegevoegd en bewoners verplaatst met logger attached", "SETUP")

    logger.log("Setup woning voltooid.")

    return woning, logger, hub


def simuleer_tijdstap(woning_obj, logger_obj, hub_obj):
    logger_obj.log("nieuwe tijdstap", "SIM")

    if not woning_obj.kamers:
        logger_obj.log("Geen kamers dus bewoners knn zich niet verplaatsen.","SIM")
        return
    
    kamers_lijst = list(woning_obj.kamers.values())

    for bewoner in woning_obj.bewoners:
        oude_kamer = bewoner.huidige_kamer
        nieuwe_kamers_lijst = [k for k in kamers_lijst if k != oude_kamer] #rechtstreeks aangepast v stack overflow. zie history voor verbetering als nodig

        if not nieuwe_kamers_lijst:
            if len(kamers_lijst) > 1:
                logger_obj.log(f"{bewoner.naam} blijft in {oude_kamer.naam if oude_kamer else "geen andere kamer beschikbaar"}", "SIM")
                nieuwe_kamer = oude_kamer
            elif len(kamers_lijst) == 1:
                logger_obj.log(f"{bewoner.naam} blijft in {oude_kamer.naam if oude_kamer else "maar 1 kamer"}", "SIM")
                nieuwe_kamer = oude_kamer
        else:
            nieuwe_kamer= random.choice(nieuwe_kamers_lijst)

        if nieuwe_kamer and (nieuwe_kamer != oude_kamer or not oude_kamer): # or not oude kamer-> als er geen oude kamer was dan...
            bewoner.verplaats(nieuwe_kamer, logger_instance=logger_obj)

            logger_obj.log(f"{bewoner.naam} is nu in {nieuwe_kamer.naam}", "SIM")

            for apparaat in nieuwe_kamer.get_apparaten():
                if isinstance(apparaat, Bewegingssensor):
                    if apparaat.status:
                        logger_obj.log(f"Bewegingssensor {apparaat.naam} in{nieuwe_kamer.naam} detecteerd een beweging.", "SENSOR")
                        apparaat.detecteer_beweging()
                    else:
                        logger_obj.log(f"Bewegingssensor {apparaat.naam} in{nieuwe_kamer.naam} staat uit","SENSOR")
        elif nieuwe_kamer == oude_kamer:
            logger_obj.log(f"{bewoner.naam} blijft in {oude_kamer.naam if oude_kamer else "geen kamer"}", "SIM")
    logger_obj.log("Reset beweginssensoren")
    for kamer in woning_obj.kamers.values():
        for app in kamer.get_apparaten():
            if isinstance(app, Bewegingssensor):
                app.reset_sensor()


def toon_hoofd_menu():
    print("1. Start auto simulatie (x tijdstappen)")
    print("2. Genereer/update html statusoverzicht")
    print("3. Voer handmatig actie uit op apparaat")
    print("4. Toon laatste paar logs")
    print("0. Exit")

def vraag_gebruikers_keuze():
    while True:
        try:
            keuze = int(input("Kies een optie: "))
            return keuze
        except ValueError:
            print("Ongeldige input, voer een cijfer in! 1-4")
        
def voer_handmatige_actie_uit(woning_obj,logger_obj):
    if not woning_obj or not logger_obj:
        print("Fout geen woning of logger, dit is nodig voro handmatige actie")
        return
    alle_apparaten = woning_obj.get_alle_apparaten()
    if not alle_apparaten:
        print("geen apparaten beschikbaar voor handm actie")
        return
    
    print("Apparaten:")
    for i, app in enumerate(alle_apparaten):
        print(f"{i+1}. {app.naam} in {app.kamer.naam if app.kamer else "geen kamer"}"
              f"Status: {"aan" if app.status else "UIT"}")
        
    while True:
        try:
            app_keuze_index = int(input(f"Kies apparaaat met nr of 0 om te exiten."))
            if app_keuze_index ==0:
                return
            if 1<= app_keuze_index <= len(alle_apparaten):
                gekozen_apparaat = alle_apparaten[app_keuze_index-1]
                break
            else:
                print("Geen geldig appnummer...")
        except ValueError:
            print("Voer geldig cijfer in")

    print(f"gekozen apparaat: {gekozen_apparaat.naam}")
    print("Mogelijke acties:'aan', 'uit', 'toggle'")
    #enkel voor algemene app, specifieke nog toevooegen vr lamp thermo etc.

    actie = input("Welke actie uitvoeren?").strip().lower()

    log_msg = f"Handmatige actie voor: {gekozen_apparaat.naam}: {actie}"

    if actie=="aan":
        gekozen_apparaat.zet_aan()
    elif actie=="uit":
        gekozen_apparaat.zet_uit()
    elif actie=="toggle":
        gekozen_apparaat.toggle_status()

    elif isinstance(gekozen_apparaat, Lamp) and actie == "helderheid":
        try:
            niveau = int(input("Helderheid: 0-100: "))
            gekozen_apparaat.pas_helderheid_aan(niveau)
        except ValueError:
            logger_obj.log("Helderheid ongeldig, mt tussen 0-100 zijn")
    else:
        logger_obj.log(f"Onbekende handmatige actie {actie} voor {gekozen_apparaat}.")
        return

    print(f"{actie} uitgevoerd op {gekozen_apparaat.naam} Satus: {gekozen_apparaat.get_status_details()}")


def toon_laatste_logs(logger_obj, aantal = 7):
    if not logger_obj:
        print("Geen logger initialised")
        return
    print(f"Laatste {aantal} logs:")
    logs = logger_obj.get_logs()
    if not logs:
        print("Geen logs beschikbaar?")
        return
    for entry in logs[-aantal:]:
        print(entry)
    

if __name__ == "__main__": # zou ervoor moeten zorgen dat ik main.py enkel rehctstreeks kan uitvoeren
                            #en dus niet als ik het geimporteerd heb.
    mijn_woning, mijn_logger, mijn_hub = setup_woning() # zelfde vorlgorde als de returns

    mijn_logger.log("\n Woning realtime")
    mijn_logger.log(mijn_woning)

    html_gen = HTMLGenerator(logger_instance=mijn_logger)

    html_gen.gen_site(woning_obj=mijn_woning, logger_obj=mijn_logger)

    # aantal_tijdstappen = 5
    # seconden_per_stap = 1

    while True:
        toon_hoofd_menu()
        gebruikers_input = vraag_gebruikers_keuze()
        
        if gebruikers_input == 1:
            try:
                aantal_tijdstappen = int(input("Hvl tijdstappen wil je simuleren?"))
                seconden_per_stap = float(input("Hoeveel seconden vertraging per stap? bv 0.5, 1 of 2"))
            except Exception:
                print("Geldig cijfer invoeren aub")  
                continue
            mijn_logger.log(f"Start sim met {aantal_tijdstappen} tijdstappen per stap {seconden_per_stap} seconden wachten.")

            for i in range(aantal_tijdstappen):
                mijn_logger.log(f"\n tijdstap {i+1}/{aantal_tijdstappen}")


                simuleer_tijdstap(mijn_woning, mijn_logger, mijn_hub) 
                
                # update de html na elke 2 stappen, anders moielijk om realtime sim te volgen als traag stappen vergroten
                if (i+1) % 2 ==0 or (i + 1) == aantal_tijdstappen:
                    html_gen.gen_site(woning_obj=mijn_woning, logger_obj=mijn_logger)
                time.sleep(seconden_per_stap)

            mijn_logger.log("\nEinde sim")
            mijn_logger.log(mijn_woning)
        elif gebruikers_input == 2:
            mijn_logger.log("HTML statusoverzicht gevraagd")
            html_gen.gen_site(woning_obj=mijn_woning, logger_obj=mijn_logger)            
            mijn_logger.log("site updated.")
        elif gebruikers_input == 3:
            voer_handmatige_actie_uit(mijn_woning, mijn_logger)

        elif gebruikers_input == 4:
            try:
                aantal = int(input("Hvl recente log entries wilt je zien?"))
                if not aantal:
                    aantal = 10
                toon_laatste_logs(mijn_logger,aantal)
            except ValueError:
                mijn_logger.log("Geef geldig cijfer i vr aantal logs")
                toon_laatste_logs(mijn_logger) #default v 7 gebruiken
        elif gebruikers_input == 0:
            break
        else:
            mijn_logger.log("Ongeldige menukeuze!!")


    mijn_logger.close()

    mijn_logger.log(f"HTMLGEN klaar Kijk in {html_gen.output_map} voor index.html")
    print("Einde programma.")

