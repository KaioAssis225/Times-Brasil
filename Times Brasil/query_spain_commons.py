import urllib.request
import json
import time

p1_teams = [
    ("01", "Real Madrid", "real_madrid.png", "File:Real Madrid CF.svg"),
    ("02", "FC Barcelona", "barcelona.png", "File:FC Barcelona (crest).svg"),
    ("03", "Atlético Madrid", "atletico_madrid.png", "File:Atletico Madrid 2017 Logo.svg"),
    ("04", "Athletic Bilbao", "athletic_bilbao.png", "File:Athletic Club (spain) logo.svg"),
    ("05", "Real Sociedad", "real_sociedad.png", "File:Real Sociedad logo.svg"),
    ("06", "Real Betis", "real_betis.png", "File:Real Betis Balompie logo.svg"),
    ("07", "Villarreal CF", "villarreal.png", "File:Villarreal CF logo.svg"),
    ("08", "Valencia CF", "valencia.png", "File:Valencia CF logo.svg"),
    ("09", "Sevilla FC", "sevilla.png", "File:Sevilla FC logo.svg"),
    ("10", "CA Osasuna", "osasuna.png", "File:CA Osasuna logo.svg"),
    ("11", "RC Celta de Vigo", "celta_vigo.png", "File:RC Celta de Vigo logo.svg"),
    ("12", "Rayo Vallecano", "rayo_vallecano.png", "File:Rayo Vallecano logo.svg"),
    ("13", "Getafe CF", "getafe.png", "File:Getafe CF logo.svg"),
    ("14", "Girona FC", "girona.png", "File:Girona FC logo.svg"),
    ("15", "RCD Mallorca", "mallorca.png", "File:RCD Mallorca logo.svg"),
    ("16", "Deportivo Alavés", "alaves.png", "File:Deportivo Alaves logo.svg"),
    ("17", "RCD Espanyol", "espanyol.png", "File:RCD Espanyol logo.svg"),
    ("18", "Levante UD", "levante.png", "File:Levante UD logo.svg"),
    ("19", "Elche CF", "elche.png", "File:Elche CF logo.svg"),
    ("20", "Real Oviedo", "real_oviedo.png", "File:Real Oviedo logo.svg")
]

p2_teams = [
    ("01", "Racing de Santander", "racing_santander.png", "File:Racing de Santander logo.svg"),
    ("02", "Deportivo La Coruña", "deportivo_la_coruna.png", "File:Deportivo de La Coruña logo.svg"),
    ("03", "UD Almería", "almeria.png", "File:UD Almería logo.svg"),
    ("04", "Málaga CF", "malaga.png", "File:Málaga CF logo.svg"),
    ("05", "UD Las Palmas", "las_palmas.png", "File:UD Las Palmas logo.svg"),
    ("06", "CD Castellón", "castellon.png", "File:CD Castellón logo.svg"),
    ("07", "Burgos CF", "burgos.png", "File:Burgos CF logo.svg"),
    ("08", "SD Eibar", "eibar.png", "File:SD Eibar logo.svg"),
    ("09", "Córdoba CF", "cordoba.png", "File:Córdoba CF logo.svg"),
    ("10", "Sporting de Gijón", "sporting_gijon.png", "File:Sporting de Gijón logo.svg"),
    ("11", "AD Ceuta FC", "ceuta.png", "File:AD Ceuta FC logo.svg"),
    ("12", "Albacete Balompié", "albacete.png", "File:Albacete Balompié logo.svg"),
    ("13", "FC Andorra", "fc_andorra.png", "File:FC Andorra logo.svg"),
    ("14", "Granada CF", "granada.png", "File:Granada CF logo.svg"),
    ("15", "Real Sociedad B", "real_sociedad_b.png", "File:Real Sociedad logo.svg"),
    ("16", "CD Leganés", "leganes.png", "File:CD Leganés logo.svg"),
    ("17", "Real Valladolid", "real_valladolid.png", "File:Real Valladolid logo.svg"),
    ("18", "Cádiz CF", "cadiz.png", "File:Cádiz CF logo.svg"),
    ("19", "CD Mirandés", "mirandes.png", "File:CD Mirandés logo.svg"),
    ("20", "SD Huesca", "huesca.png", "File:SD Huesca logo.svg"),
    ("21", "Cultural Leonesa", "cultural_leonesa.png", "File:Cultural Leonesa logo.svg"),
    ("22", "Real Zaragoza", "real_zaragoza.png", "File:Real Zaragoza logo.svg")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

print("=== PRIMERA DIVISION ===")
for num, name, fn, file_title in p1_teams:
    time.sleep(1.5)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(file_title)}&prop=imageinfo&iiprop=url&iiurlwidth=1280&format=json"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            pid = list(pages.keys())[0]
            if pid != "-1":
                ii = pages[pid].get('imageinfo', [{}])[0]
                thumb = ii.get('thumburl') or ii.get('url')
                print(f"[FOUND P1] {num} {name}: {thumb}")
            else:
                print(f"[MISSING P1] {num} {name}: {file_title}")
    except Exception as e:
        print(f"[ERR P1] {num} {name}: {e}")

print("\n=== SEGUNDA DIVISION ===")
for num, name, fn, file_title in p2_teams:
    time.sleep(1.5)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(file_title)}&prop=imageinfo&iiprop=url&iiurlwidth=1280&format=json"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            pid = list(pages.keys())[0]
            if pid != "-1":
                ii = pages[pid].get('imageinfo', [{}])[0]
                thumb = ii.get('thumburl') or ii.get('url')
                print(f"[FOUND P2] {num} {name}: {thumb}")
            else:
                print(f"[MISSING P2] {num} {name}: {file_title}")
    except Exception as e:
        print(f"[ERR P2] {num} {name}: {e}")
