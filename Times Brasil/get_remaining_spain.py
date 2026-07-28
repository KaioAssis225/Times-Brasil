import urllib.request
import time
import os
from PIL import Image

dir_p1 = r"c:\Users\matheus.cardoso\Desktop\Times Brasil\Futebol Espanha\Primera Division"
dir_p2 = r"c:\Users\matheus.cardoso\Desktop\Times Brasil\Futebol Espanha\Segunda Division"

CANVAS_SIZE = (1024, 1024)
TARGET_SIZE = 880

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

missing_p1 = [
    ("04", "athletic_bilbao.png", "Athletic Bilbao", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Athletic_Club_%28spain%29_logo.svg/1280px-Athletic_Club_%28spain%29_logo.svg.png"),
    ("18", "levante.png", "Levante UD", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Levante_UD_logo.svg/1280px-Levante_UD_logo.svg.png"),
    ("19", "elche.png", "Elche CF", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Elche_CF_logo.svg/1280px-Elche_CF_logo.svg.png"),
    ("20", "real_oviedo.png", "Real Oviedo", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Real_Oviedo_logo.svg/1280px-Real_Oviedo_logo.svg.png")
]

missing_p2 = [
    ("04", "malaga.png", "Málaga CF", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Malaga_cf.gif/1280px-Malaga_cf.gif"),
    ("05", "las_palmas.png", "UD Las Palmas", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/UD_Las_Palmas_logo.png/1280px-UD_Las_Palmas_logo.png"),
    ("07", "burgos.png", "Burgos CF", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Burgos_CF_logo.svg/1280px-Burgos_CF_logo.svg.png"),
    ("08", "eibar.png", "SD Eibar", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/SD_Eibar_logo_2016.svg/1280px-SD_Eibar_logo_2016.svg.png"),
    ("09", "cordoba.png", "Córdoba CF", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/C%C3%B3rdoba_CF_logo.svg/1280px-C%C3%B3rdoba_CF_logo.svg.png"),
    ("10", "sporting_gijon.png", "Sporting de Gijón", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/R_sporting_de_gijon.gif/1280px-R_sporting_de_gijon.gif"),
    ("11", "ceuta.png", "AD Ceuta FC", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/AD_Ceuta_FC.png/1280px-AD_Ceuta_FC.png"),
    ("12", "albacete.png", "Albacete Balompié", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Albacete_Balompie_logo.svg/1280px-Albacete_Balompie_logo.svg.png"),
    ("13", "fc_andorra.png", "FC Andorra", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/FC_Andorra.png/1280px-FC_Andorra.png"),
    ("14", "granada.png", "Granada CF", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Granada_CF_logo.svg/1280px-Granada_CF_logo.svg.png"),
    ("16", "leganes.png", "CD Leganés", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Club_Deportivo_Legan%C3%A9s.png/1280px-Club_Deportivo_Legan%C3%A9s.png"),
    ("17", "real_valladolid.png", "Real Valladolid", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Real_Valladolid_logo.svg/1280px-Real_Valladolid_logo.svg.png"),
    ("18", "cadiz.png", "Cádiz CF", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/C%C3%A1diz_CF_logo.svg/1280px-C%C3%A1diz_CF_logo.svg.png"),
    ("19", "mirandes.png", "CD Mirandés", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/CD_Mirand%C3%A9s.png/1280px-CD_Mirand%C3%A9s.png"),
    ("20", "huesca.png", "SD Huesca", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/SD_Huesca.png/1280px-SD_Huesca.png"),
    ("21", "cultural_leonesa.png", "Cultural Leonesa", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Cultural_y_Deportiva_Leonesa_logo.svg/1280px-Cultural_y_Deportiva_Leonesa_logo.svg.png"),
    ("22", "real_zaragoza.png", "Real Zaragoza", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Real_cd_zaragoza.gif/1280px-Real_cd_zaragoza.gif")
]

all_teams_p1 = [
    {"num": "01", "name": "Real Madrid", "filename": "real_madrid.png"},
    {"num": "02", "name": "FC Barcelona", "filename": "barcelona.png"},
    {"num": "03", "name": "Atlético Madrid", "filename": "atletico_madrid.png"},
    {"num": "04", "name": "Athletic Bilbao", "filename": "athletic_bilbao.png"},
    {"num": "05", "name": "Real Sociedad", "filename": "real_sociedad.png"},
    {"num": "06", "name": "Real Betis", "filename": "real_betis.png"},
    {"num": "07", "name": "Villarreal CF", "filename": "villarreal.png"},
    {"num": "08", "name": "Valencia CF", "filename": "valencia.png"},
    {"num": "09", "name": "Sevilla FC", "filename": "sevilla.png"},
    {"num": "10", "name": "CA Osasuna", "filename": "osasuna.png"},
    {"num": "11", "name": "RC Celta de Vigo", "filename": "celta_vigo.png"},
    {"num": "12", "name": "Rayo Vallecano", "filename": "rayo_vallecano.png"},
    {"num": "13", "name": "Getafe CF", "filename": "getafe.png"},
    {"num": "14", "name": "Girona FC", "filename": "girona.png"},
    {"num": "15", "name": "RCD Mallorca", "filename": "mallorca.png"},
    {"num": "16", "name": "Deportivo Alavés", "filename": "alaves.png"},
    {"num": "17", "name": "RCD Espanyol", "filename": "espanyol.png"},
    {"num": "18", "name": "Levante UD", "filename": "levante.png"},
    {"num": "19", "name": "Elche CF", "filename": "elche.png"},
    {"num": "20", "name": "Real Oviedo", "filename": "real_oviedo.png"}
]

all_teams_p2 = [
    {"num": "01", "name": "Racing de Santander", "filename": "racing_santander.png"},
    {"num": "02", "name": "Deportivo La Coruña", "filename": "deportivo_la_coruna.png"},
    {"num": "03", "name": "UD Almería", "filename": "almeria.png"},
    {"num": "04", "name": "Málaga CF", "filename": "malaga.png"},
    {"num": "05", "name": "UD Las Palmas", "filename": "las_palmas.png"},
    {"num": "06", "name": "CD Castellón", "filename": "castellon.png"},
    {"num": "07", "name": "Burgos CF", "filename": "burgos.png"},
    {"num": "08", "name": "SD Eibar", "filename": "eibar.png"},
    {"num": "09", "name": "Córdoba CF", "filename": "cordoba.png"},
    {"num": "10", "name": "Sporting de Gijón", "filename": "sporting_gijon.png"},
    {"num": "11", "name": "AD Ceuta FC", "filename": "ceuta.png"},
    {"num": "12", "name": "Albacete Balompié", "filename": "albacete.png"},
    {"num": "13", "name": "FC Andorra", "filename": "fc_andorra.png"},
    {"num": "14", "name": "Granada CF", "filename": "granada.png"},
    {"num": "15", "name": "Real Sociedad B", "filename": "real_sociedad_b.png"},
    {"num": "16", "name": "CD Leganés", "filename": "leganes.png"},
    {"num": "17", "name": "Real Valladolid", "filename": "real_valladolid.png"},
    {"num": "18", "name": "Cádiz CF", "filename": "cadiz.png"},
    {"num": "19", "name": "CD Mirandés", "filename": "mirandes.png"},
    {"num": "20", "name": "SD Huesca", "filename": "huesca.png"},
    {"num": "21", "name": "Cultural Leonesa", "filename": "cultural_leonesa.png"},
    {"num": "22", "name": "Real Zaragoza", "filename": "real_zaragoza.png"}
]

def process_missing_items(missing_list, output_dir, league_name):
    print(f"\nDownloading missing {league_name}...")
    for num, filename, name, url in missing_list:
        time.sleep(2.0)
        print(f"[{num}] {name}...", end=" ", flush=True)
        raw_path = os.path.join(output_dir, f"raw_{filename}")
        std_path = os.path.join(output_dir, filename)
        num_path = os.path.join(output_dir, f"{num}_{filename}")
        
        downloaded = False
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=10) as response, open(raw_path, 'wb') as f:
                    f.write(response.read())
                downloaded = True
                break
            except Exception:
                time.sleep(2.0)
                
        if not downloaded:
            print("Download failed")
            continue
            
        try:
            with Image.open(raw_path) as img:
                img = img.convert("RGBA")
                bbox = img.getbbox()
                if bbox:
                    img = img.crop(bbox)
                    
                w, h = img.size
                ratio = min(TARGET_SIZE / w, TARGET_SIZE / h)
                new_w, new_h = int(w * ratio), int(h * ratio)
                
                img_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
                canvas = Image.new("RGBA", CANVAS_SIZE, (0, 0, 0, 0))
                canvas.paste(img_resized, ((CANVAS_SIZE[0] - new_w) // 2, (CANVAS_SIZE[1] - new_h) // 2))
                
                canvas.save(std_path, "PNG", optimize=True)
                canvas.save(num_path, "PNG", optimize=True)
                print("100% OK!")
            if os.path.exists(raw_path):
                os.remove(raw_path)
        except Exception as e:
            print(f"Error: {e}")

process_missing_items(missing_p1, dir_p1, "Primera Division")
process_missing_items(missing_p2, dir_p2, "Segunda Division")

# Re-generate index.html for Primera Division
html_content_p1 = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Futebol Espanha - Primera División (La Liga)</title>
    <style>
        :root {{
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-color: #f8fafc;
            --accent-color: #ef4444;
            --accent-glow: rgba(239, 68, 68, 0.2);
            --border-color: #334155;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg-color); color: var(--text-color); padding: 2rem 1rem; }}
        header {{ text-align: center; margin-bottom: 3rem; }}
        header h1 {{ font-size: 2.5rem; font-weight: 800; background: linear-gradient(135deg, #ef4444, #eab308); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem; }}
        header p {{ color: #94a3b8; font-size: 1.1rem; }}
        .stats-badge {{ display: inline-block; background: var(--accent-glow); border: 1px solid var(--accent-color); color: var(--accent-color); padding: 0.4rem 1rem; border-radius: 9999px; font-weight: 600; font-size: 0.9rem; margin-top: 1rem; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1.5rem; max-width: 1400px; margin: 0 auto; }}
        .card {{ background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 1rem; padding: 1.5rem; display: flex; flex-direction: column; align-items: center; transition: all 0.3s ease; }}
        .card:hover {{ transform: translateY(-5px); border-color: var(--accent-color); box-shadow: 0 10px 25px -5px var(--accent-glow); }}
        .img-container {{ width: 140px; height: 140px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; background-image: linear-gradient(45deg, #182234 25%, transparent 25%), linear-gradient(-45deg, #182234 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #182234 75%), linear-gradient(-45deg, transparent 75%, #182234 75%); background-size: 16px 16px; border-radius: 0.75rem; padding: 10px; }}
        .img-container img {{ max-width: 100%; max-height: 100%; object-fit: contain; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.5)); }}
        .team-name {{ font-size: 1.1rem; font-weight: 700; text-align: center; margin-bottom: 0.5rem; }}
        .specs {{ font-size: 0.8rem; color: #64748b; text-align: center; }}
        footer {{ text-align: center; margin-top: 4rem; color: #64748b; font-size: 0.9rem; }}
    </style>
</head>
<body>
    <header>
        <h1>Futebol Espanha - Primera División (La Liga)</h1>
        <p>Coleção de imagens e escudos dos 20 times da Primera División da Espanha em alta resolução</p>
        <div class="stats-badge">20 Imagens Padronizadas (1024x1024 PNG Transparente)</div>
    </header>
    <div class="grid">
"""

for t in all_teams_p1:
    html_content_p1 += f"""
        <div class="card">
            <div class="img-container"><img src="{t['filename']}" alt="{t['name']}"></div>
            <div class="team-name">{t['name']}</div>
            <div class="specs">1024 x 1024 PNG</div>
        </div>
"""

html_content_p1 += """
    </div>
    <footer>
        <p>Formatos padronizados com fundo transparente e proporções mantidas.</p>
    </footer>
</body>
</html>
"""

with open(os.path.join(dir_p1, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content_p1)

# Re-generate index.html for Segunda Division
html_content_p2 = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Futebol Espanha - Segunda División (LaLiga Hypermotion)</title>
    <style>
        :root {{
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-color: #f8fafc;
            --accent-color: #ef4444;
            --accent-glow: rgba(239, 68, 68, 0.2);
            --border-color: #334155;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg-color); color: var(--text-color); padding: 2rem 1rem; }}
        header {{ text-align: center; margin-bottom: 3rem; }}
        header h1 {{ font-size: 2.5rem; font-weight: 800; background: linear-gradient(135deg, #ef4444, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem; }}
        header p {{ color: #94a3b8; font-size: 1.1rem; }}
        .stats-badge {{ display: inline-block; background: var(--accent-glow); border: 1px solid var(--accent-color); color: var(--accent-color); padding: 0.4rem 1rem; border-radius: 9999px; font-weight: 600; font-size: 0.9rem; margin-top: 1rem; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1.5rem; max-width: 1400px; margin: 0 auto; }}
        .card {{ background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 1rem; padding: 1.5rem; display: flex; flex-direction: column; align-items: center; transition: all 0.3s ease; }}
        .card:hover {{ transform: translateY(-5px); border-color: var(--accent-color); box-shadow: 0 10px 25px -5px var(--accent-glow); }}
        .img-container {{ width: 140px; height: 140px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; background-image: linear-gradient(45deg, #182234 25%, transparent 25%), linear-gradient(-45deg, #182234 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #182234 75%), linear-gradient(-45deg, transparent 75%, #182234 75%); background-size: 16px 16px; border-radius: 0.75rem; padding: 10px; }}
        .img-container img {{ max-width: 100%; max-height: 100%; object-fit: contain; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.5)); }}
        .team-name {{ font-size: 1.1rem; font-weight: 700; text-align: center; margin-bottom: 0.5rem; }}
        .specs {{ font-size: 0.8rem; color: #64748b; text-align: center; }}
        footer {{ text-align: center; margin-top: 4rem; color: #64748b; font-size: 0.9rem; }}
    </style>
</head>
<body>
    <header>
        <h1>Futebol Espanha - Segunda División (LaLiga Hypermotion)</h1>
        <p>Coleção de imagens e escudos dos 22 times da Segunda División da Espanha em alta resolução</p>
        <div class="stats-badge">22 Imagens Padronizadas (1024x1024 PNG Transparente)</div>
    </header>
    <div class="grid">
"""

for t in all_teams_p2:
    html_content_p2 += f"""
        <div class="card">
            <div class="img-container"><img src="{t['filename']}" alt="{t['name']}"></div>
            <div class="team-name">{t['name']}</div>
            <div class="specs">1024 x 1024 PNG</div>
        </div>
"""

html_content_p2 += """
    </div>
    <footer>
        <p>Formatos padronizados com fundo transparente e proporções mantidas.</p>
    </footer>
</body>
</html>
"""

with open(os.path.join(dir_p2, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content_p2)

print("Saved index.html for Primera and Segunda Division!")
