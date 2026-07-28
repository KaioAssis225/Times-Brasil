import urllib.request
import re
import time

teams_p1 = [
    ("01", "real_madrid.png", "Real Madrid", "https://lt.wikipedia.org/wiki/Real_Madrid_CF"),
    ("02", "barcelona.png", "FC Barcelona", "https://lt.wikipedia.org/wiki/FC_Barcelona"),
    ("03", "atletico_madrid.png", "Atlético Madrid", "https://lt.wikipedia.org/wiki/Atl%C3%A9tico_de_Madrid"),
    ("04", "athletic_bilbao.png", "Athletic Bilbao", "https://lt.wikipedia.org/wiki/Athletic_Club"),
    ("05", "real_sociedad.png", "Real Sociedad", "https://lt.wikipedia.org/wiki/Real_Sociedad"),
    ("06", "real_betis.png", "Real Betis", "https://lt.wikipedia.org/wiki/Real_Betis"),
    ("07", "villarreal.png", "Villarreal CF", "https://lt.wikipedia.org/wiki/Villarreal_CF"),
    ("08", "valencia.png", "Valencia CF", "https://lt.wikipedia.org/wiki/Valencia_CF"),
    ("09", "sevilla.png", "Sevilla FC", "https://lt.wikipedia.org/wiki/Sevilla_FC"),
    ("10", "osasuna.png", "CA Osasuna", "https://lt.wikipedia.org/wiki/CA_Osasuna"),
    ("11", "celta_vigo.png", "RC Celta de Vigo", "https://lt.wikipedia.org/wiki/RC_Celta_de_Vigo"),
    ("12", "rayo_vallecano.png", "Rayo Vallecano", "https://lt.wikipedia.org/wiki/Rayo_Vallecano"),
    ("13", "getafe.png", "Getafe CF", "https://lt.wikipedia.org/wiki/Getafe_CF"),
    ("14", "girona.png", "Girona FC", "https://lt.wikipedia.org/wiki/Girona_FC"),
    ("15", "mallorca.png", "RCD Mallorca", "https://lt.wikipedia.org/wiki/RCD_Mallorca"),
    ("16", "alaves.png", "Deportivo Alavés", "https://lt.wikipedia.org/wiki/Deportivo_Alav%C3%A9s"),
    ("17", "espanyol.png", "RCD Espanyol", "https://lt.wikipedia.org/wiki/RCD_Espanyol"),
    ("18", "levante.png", "Levante UD", "https://lt.wikipedia.org/wiki/Levante_UD"),
    ("19", "elche.png", "Elche CF", "https://lt.wikipedia.org/wiki/Elche_CF"),
    ("20", "real_oviedo.png", "Real Oviedo", "https://lt.wikipedia.org/wiki/Real_Oviedo")
]

teams_p2 = [
    ("01", "racing_santander.png", "Racing de Santander", "https://lt.wikipedia.org/wiki/Racing_de_Santander"),
    ("02", "deportivo_la_coruna.png", "Deportivo La Coruña", "https://lt.wikipedia.org/wiki/RC_Deportivo_de_La_Coru%C3%B1a"),
    ("03", "almeria.png", "UD Almería", "https://lt.wikipedia.org/wiki/UD_Almer%C3%ADa"),
    ("04", "malaga.png", "Málaga CF", "https://lt.wikipedia.org/wiki/M%C3%A1laga_CF"),
    ("05", "las_palmas.png", "UD Las Palmas", "https://lt.wikipedia.org/wiki/UD_Las_Palmas"),
    ("06", "castellon.png", "CD Castellón", "https://lt.wikipedia.org/wiki/CD_Castell%C3%B3n"),
    ("07", "burgos.png", "Burgos CF", "https://lt.wikipedia.org/wiki/Burgos_CF"),
    ("08", "eibar.png", "SD Eibar", "https://lt.wikipedia.org/wiki/SD_Eibar"),
    ("09", "cordoba.png", "Córdoba CF", "https://lt.wikipedia.org/wiki/C%C3%B3rdoba_CF"),
    ("10", "sporting_gijon.png", "Sporting de Gijón", "https://lt.wikipedia.org/wiki/Sporting_de_Gij%C3%B3n"),
    ("11", "ceuta.png", "AD Ceuta FC", "https://lt.wikipedia.org/wiki/AD_Ceuta_FC"),
    ("12", "albacete.png", "Albacete Balompié", "https://lt.wikipedia.org/wiki/Albacete_Balompi%C3%A9"),
    ("13", "fc_andorra.png", "FC Andorra", "https://lt.wikipedia.org/wiki/FC_Andorra"),
    ("14", "granada.png", "Granada CF", "https://lt.wikipedia.org/wiki/Granada_CF"),
    ("15", "real_sociedad_b.png", "Real Sociedad B", "https://lt.wikipedia.org/wiki/Real_Sociedad_B"),
    ("16", "leganes.png", "CD Leganés", "https://lt.wikipedia.org/wiki/CD_Legan%C3%A9s"),
    ("17", "real_valladolid.png", "Real Valladolid", "https://lt.wikipedia.org/wiki/Real_Valladolid"),
    ("18", "cadiz.png", "Cádiz CF", "https://lt.wikipedia.org/wiki/C%C3%A1diz_CF"),
    ("19", "mirandes.png", "CD Mirandés", "https://lt.wikipedia.org/wiki/CD_Mirand%C3%A9s"),
    ("20", "huesca.png", "SD Huesca", "https://lt.wikipedia.org/wiki/SD_Huesca"),
    ("21", "cultural_leonesa.png", "Cultural Leonesa", "https://lt.wikipedia.org/wiki/Cultural_y_Deportiva_Leonesa"),
    ("22", "real_zaragoza.png", "Real Zaragoza", "https://lt.wikipedia.org/wiki/Real_Zaragoza")
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("=== PRIMERA DIVISION URLS ===")
for num, fn, name, page_url in teams_p1:
    time.sleep(1.0)
    try:
        req = urllib.request.Request(page_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            matches = re.findall(r'//upload\.wikimedia\.org/wikipedia/[^"\s]+\.(?:png|svg|gif|jpg)', html)
            if matches:
                img_url = "https:" + matches[0]
                print(f'("{num}", "{fn}", "{name}", "{img_url}"),')
            else:
                print(f'# MISSING P1: {num} {name}')
    except Exception as e:
        print(f'# ERR P1: {num} {name}: {e}')

print("\n=== SEGUNDA DIVISION URLS ===")
for num, fn, name, page_url in teams_p2:
    time.sleep(1.0)
    try:
        req = urllib.request.Request(page_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            matches = re.findall(r'//upload\.wikimedia\.org/wikipedia/[^"\s]+\.(?:png|svg|gif|jpg)', html)
            if matches:
                img_url = "https:" + matches[0]
                print(f'("{num}", "{fn}", "{name}", "{img_url}"),')
            else:
                print(f'# MISSING P2: {num} {name}')
    except Exception as e:
        print(f'# ERR P2: {num} {name}: {e}')
