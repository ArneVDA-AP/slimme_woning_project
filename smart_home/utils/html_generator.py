import os

class HTMLGenerator:
    def __init__(self, output_map: str = "_site/"):
        self.output_map:str = output_map
        try:
            os.makedirs(self.output_map, exist_ok=True)
            print(f"INFO; output map is aangemaakt of bestond al {self.output_map}")
        except Exception as e:
            print(f"FOUT: geen output folder {self.output_map} fout: {e}")
        
    def gen_site(self, woning_obj, logger_obj = None):
        if not woning_obj:
            print("FOUT woning_obj verplicht!")
            return
        
        print(f"START gen site voor woning {woning_obj.naam}")

        self.gen_index_pagina(woning_obj)

        for kamer_naam, kamer_obj in woning_obj.kamers.items():
            self.gen_kamer_pagina(kamer_obj)

        if logger_obj:
            self.gen_log_pagina(logger_obj)
        
        self._gen_css()

        print(f"INFO sitegen voltooid in map {self.output_map}")

    def gen_index_pagina(self, woning_obj):
        bestandnaam = os.path.join(self.output_map, "index.html")

        html_content_list = []
        html_content_list.append(f"""
            <!DOCTYPE html>
            <html lang="nl">
            <head>
                <meta charset="UTF-8">
                <title>Slimme woning: {woning_obj.naam}</title>
                <link rel="stylesheet" href="style.css">
            </head>
            <body>
                <h1>Overzicht Slimme Woning:{woning_obj.naam}</h1>
                
                <h2>Kamers:</h2>
                <ul>
        """)

        if not woning_obj.kamers:
            html_content_list.append("<li>Nog geen kamers in de woninig</li>")
        else:
            for kamer_naam in sorted(woning_obj.kamers.keys()):
                kamer_page_link = f"{kamer_naam.lower().replace(" ", "_")}.html"
                html_content_list.append(f"<li><a href='{kamer_page_link}'>{kamer_naam}</a></li>")

        html_content_list.append("</ul>")
        
        html_content_list.append("<h2>Algemene Informatie</h2>")
        html_content_list.append(f"<p>Bewonersaantal: {len(woning_obj.bewoners)}</p>")

        if woning_obj.smarthub:
            hub_naam = woning_obj.smarthub.naam
            html_content_list.append(f"<p>SmartHub: {hub_naam}</p>")
        
        log_page_path = os.path.join(self.output_map, "logs.html")
        if os.path.exists(log_page_path):
            html_content_list.append("<p><a href='logs.html'>Logs</a></p>")

        #einde html
        html_content_list.append("</body>")
        html_content_list.append("</html>")

        try:
            with open(bestandnaam, "w", encoding="utf-8") as f:
                f.write("\n".join(html_content_list))
            print(f"INFO: index {bestandnaam} gemaakt.")
        except Exception as e:
            print(f"FOUT: kon index {bestandnaam} niet maken. fout: {e}")

    def gen_log_pagina(self, logger_obj):
        bestandsnaam = os.path.join(self.output_map, "logs.html")

        html_content_list = []
        html_content_list.append("""
            <!DOCTYPE html>
            <html lang="nl">
            <head>
                <meta charset="UTF-8">
                <title>Logs Slimme woning</title>
                <link rel="stylesheet" href="style.css">
            </head>            
            <body>
                <p><a href="index.html">Index</a></p>
                <h1>Logs</h1>
                <pre>
                <code>""")
        # pre wordt gebruikt voor geformatteerde teksten, code wordt vaak binnenin een pre gebruikt
        # puur layoutgewijs om is te proberen.
        log_entries = logger_obj.get_logs()
        if not log_entries:
            html_content_list.append("Nog niks gelogd.")
        else:
            for entry in reversed(log_entries): #reversed zodat laatste nieuwe logs eerst komen in de lijst
                html_content_list.append(entry)
        
        html_content_list.append("</code></pre>")
        html_content_list.append("</body></html>")

        try:
            with open(bestandsnaam, "w", encoding="utf-8") as f:
                f.write("\n".join(html_content_list))
            print(f"Pagina voor logs {bestandsnaam} gemaakt")
        except Exception as e:
            print(f"FOUT: kon index {bestandsnaam} niet maken. fout: {e}")

    def gen_kamer_pagina(self, kamer_obj):
        kamer_page_link = kamer_obj.naam.lower().replace(" ", "_") # zelfde als bij html link, de layout voor links, zonder spaties dus
                                                                  # Ik had ergens iets van slugs gezien maar dit is eigenlijik een manuele versie
        
        bestandsnaam = os.path.join(self.output_map, f"{kamer_page_link}.html")

        html_content_list = []
        html_content_list.append(f"""
            <!DOCTYPE html>
            <html lang="nl">
            <head>
                <meta charset="UTF-8">
                <title>Kamer {kamer_obj.naam}</title>
                <link rel="stylesheet" href="style.css">
            </head>            
            <body>
                <p><a href="index.html">Index</a></p>
                <h1>Kamer: {kamer_obj.naam}</h1>
                <h2>Apparaten: </h2>""")

        if not kamer_obj.apparaten:
            html_content_list.append(f"Geen apparaten in kamer {kamer_obj.naam}")
        else:
            html_content_list.append("<ul>")
            for app in kamer_obj.apparaten:
                type_naam = type(app).__name__ # __name__ is een manier om de .naam property waarde te krijgen
                status = "AAN" if app.status else "UIT"
                details_app = app.get_status_details()

                #strong betekent belangrijk in html, wordt dan vet etc
                html_content_list.append(f"""
                    <li>
                        <strong>{app.naam}</strong> [{type_naam}]:
                        Status: {status}. Details: {details_app}
                    </li>""")
            html_content_list.append("</ul>")

        html_content_list.append("</body></html>")

        try:
            with open(bestandsnaam,"w", encoding="utf-8") as f:
                f.write("\n".join(html_content_list))
            print(f"INFO: Kamerpagina'{bestandsnaam}' voor '{kamer_obj.naam} gemaakt'.")
        except Exception as e:
            print(f"FOUT: Kon pagina niet maken. Fout: {e}")


    def _gen_css(self):
        bestandnaam = os.path.join(self.output_map, "style.css")

        css_content = """
        body{
        font-family:sans-serif;}
        """

        try:
            with open(bestandnaam, "w", encoding="utf-8") as f:
                f.write(css_content)
            print(f"CSS BESTAND {bestandnaam} aangemaakt")
        except Exception as e:
            print(f"FOUT kon css bestand niet aanmaken. fout: {e}")

        