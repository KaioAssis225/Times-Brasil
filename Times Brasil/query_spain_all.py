import urllib.request
import json
import time

teams_p1 = [
    ("01", "Real Madrid", "real_madrid.png", "Real_Madrid_CF"),
    ("02", "FC Barcelona", "barcelona.png", "FC_Barcelona"),
    ("03", "Atlético Madrid", "atletico_madrid.png", "Atl%C3%A9tico_Madrid"),
    ("04", "Athletic Bilbao", "athletic_bilbao.png", "Athletic_Bilbao"),
    ("05", "Real Sociedad", "real_sociedad.png", "Real_Sociedad"),
    ("06", "Real Betis", "real_betis.png", "Real_Betis"),
    ("07", "Villarreal CF", "villarreal.png", "Villarreal_CF"),
    ("08", "Valencia CF", "valencia.png", "Valencia_CF"),
    ("09", "Sevilla FC", "sevilla.png", "Sevilla_FC"),
    ("10", "CA Osasuna", "osasuna.png", "CA_Osasuna"),
    ("11", "RC Celta de Vigo", "celta_vigo.png", "RC_Celta_de_Vigo"),
    ("12", "Rayo Vallecano", "rayo_vallecano.png", "Rayo_Vallecano"),
    ("13", "Getafe CF", "getafe.png", "Getafe_CF"),
    ("14", "Girona FC", "girona.png", "Girona_FC"),
    ("15", "RCD Mallorca", "mallorca.png", "RCD_Mallorca"),
    ("16", "Deportivo Alavés", "alaves.png", "Deportivo_Alav%C3%A9s"),
    ("17", "RCD Espanyol", "espanyol.png", "RCD_Espanyol"),
    ("18", "Levante UD", "levante.png", "Levante_UD"),
    ("19", "Elche CF", "elche.png", "Elche_CF"),
    ("20", "Real Oviedo", "real_oviedo.png", "Real_Oviedo")
]

teams_p2 = [
    ("01", "Racing de Santander", "racing_santander.png", "Racing_de_Santander"),
    ("02", "Deportivo La Coruña", "deportivo_la_coruna.png", "Deportivo_de_La_Coru%C3%B1a"),
    ("03", "UD Almería", "almeria.png", "UD_Almer%C3%ADa"),
    ("04", "Málaga CF", "malaga.png", "M%C3%A1laga_CF"),
    ("05", "UD Las Palmas", "las_palmas.png", "UD_Las_Palmas"),
    ("06", "CD Castellón", "castellon.png", "CD_Castell%C3%B3n"),
    ("07", "Burgos CF", "burgos.png", "Burgos_CF"),
    ("08", "SD Eibar", "eibar.png", "SD_Eibar"),
    ("09", "Córdoba CF", "cordoba.png", "C%C3%B3rdoba_CF"),
    ("10", "Sporting de Gijón", "sporting_gijon.png", "Sporting_de_Gij%C3%B3n"),
    ("11", "AD Ceuta FC", "ceuta.png", "AD_Ceuta_FC"),
    ("12", "Albacete Balompié", "albacete.png", "Albacete_Balompi%C3%A9"),
    ("13", "FC Andorra", "fc_andorra.png", "FC_Andorra"),
    ("14", "Granada CF", "granada.png", "Granada_CF"),
    ("15", "Real Sociedad B", "real_sociedad_b.png", "Real_Sociedad_B"),
    ("16", "CD Leganés", "leganes.png", "CD_Legan%C3%A9s"),
    ("17", "Real Valladolid", "real_valladolid.png", "Real_Valladolid"),
    ("18", "Cádiz CF", "cadiz.png", "C%C3%A1diz_CF"),
    ("19", "CD Mirandés", "mirandes.png", "CD_Mirand%C3%A9s"),
    ("20", "SD Huesca", "huesca.png", "SD_Huesca"),
    ("21", "Cultural Leonesa", "cultural_leonesa.png", "Cultural_y_Deportiva_Leonesa"),
    ("22", "Real Zaragoza", "real_zaragoza.png", "Real_Zaragoza")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

print("=== PRIMERA DIVISION ===")
for num, name, fn, title in teams_p1:
    time.sleep(1.0)
    url = f"https://lt.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&pithumbsize=1000&format=json"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            pid = list(pages.keys())[0]
            if 'thumbnail' in pages[pid]:
                print(f"[LT P1] {num} {name}: {pages[pid]['thumbnail']['source']}")
            else:
                print(f"[MISSING P1] {num} {name}: {title}")
    except Exception as e:
        print(f"[ERR P1] {num} {name}: {e}")

print("\n=== SEGUNDA DIVISION ===")
for num, name, fn, title in teams_p2:
    time.sleep(1.0)
    url = f"https://lt.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&pithumbsize=1000&format=json"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            pid = list(pages.keys())[0]
            if 'thumbnail' in pages[pid]:
                print(f"[LT P2] {num} {name}: {pages[pid]['thumbnail']['source']}")
            else:
                print(f"[MISSING P2] {num} {name}: {title}")
    except Exception as e:
        print(f"[ERR P2] {num} {name}: {e}")
