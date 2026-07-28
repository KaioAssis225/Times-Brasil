import urllib.request
import time
import os
from PIL import Image

dir_p1 = r"c:\Users\matheus.cardoso\Desktop\Times Brasil\Futebol Espanha\Primera Division"
dir_p2 = r"c:\Users\matheus.cardoso\Desktop\Times Brasil\Futebol Espanha\Segunda Division"

os.makedirs(dir_p1, exist_ok=True)
os.makedirs(dir_p2, exist_ok=True)

CANVAS_SIZE = (1024, 1024)
TARGET_SIZE = 880

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

teams_p1 = [
    ("01", "real_madrid.png", "Real Madrid", "https://upload.wikimedia.org/wikipedia/lt/thumb/b/b1/MadridoReal.svg/960px-MadridoReal.svg.png"),
    ("02", "barcelona.png", "FC Barcelona", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/FC_Barcelona_%28crest%29.svg/1280px-FC_Barcelona_%28crest%29.svg.png"),
    ("03", "atletico_madrid.png", "Atlético Madrid", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Atletico_Madrid_2017_Logo.svg/1280px-Atletico_Madrid_2017_Logo.svg.png"),
    ("04", "athletic_bilbao.png", "Athletic Bilbao", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Athletic_Club_%28spain%29_logo.svg/1280px-Athletic_Club_%28spain%29_logo.svg.png"),
    ("05", "real_sociedad.png", "Real Sociedad", "https://upload.wikimedia.org/wikipedia/lt/b/b2/Real_sociedad_de_futbol.png"),
    ("06", "real_betis.png", "Real Betis", "https://upload.wikimedia.org/wikipedia/lt/f/f2/Real_Betis_logo.png"),
    ("07", "villarreal.png", "Villarreal CF", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Villarreal_CF_logo.svg/1280px-Villarreal_CF_logo.svg.png"),
    ("08", "valencia.png", "Valencia CF", "https://upload.wikimedia.org/wikipedia/lt/d/de/Valencia_CF_logo_original.png"),
    ("09", "sevilla.png", "Sevilla FC", "https://upload.wikimedia.org/wikipedia/lt/b/b4/Sevilla_cf_logo.png"),
    ("10", "osasuna.png", "CA Osasuna", "https://upload.wikimedia.org/wikipedia/lt/f/f9/Ca_osasuna.gif"),
    ("11", "celta_vigo.png", "RC Celta de Vigo", "https://upload.wikimedia.org/wikipedia/lt/c/c7/Rc_celta_de_vigo.gif"),
    ("12", "rayo_vallecano.png", "Rayo Vallecano", "https://upload.wikimedia.org/wikipedia/lt/6/66/Rayo_vallecano_de_madrid.gif"),
    ("13", "getafe.png", "Getafe CF", "https://upload.wikimedia.org/wikipedia/lt/8/81/Getafe_cf.gif"),
    ("14", "girona.png", "Girona FC", "https://upload.wikimedia.org/wikipedia/lt/9/92/Girona_FC_logo.png"),
    ("15", "mallorca.png", "RCD Mallorca", "https://upload.wikimedia.org/wikipedia/lt/e/ea/Rcd_mallorca.gif"),
    ("16", "alaves.png", "Deportivo Alavés", "https://upload.wikimedia.org/wikipedia/lt/c/cf/Deportivo_Alav%C3%A9s_%282020_m.%29.png"),
    ("17", "espanyol.png", "RCD Espanyol", "https://upload.wikimedia.org/wikipedia/lt/f/fd/Rcd_espanyol_de_barcelona.gif"),
    ("18", "levante.png", "Levante UD", "https://upload.wikimedia.org/wikipedia/lt/d/df/Levante_ud.gif"),
    ("19", "elche.png", "Elche CF", "https://upload.wikimedia.org/wikipedia/lt/7/7d/Elche_Club_de_F%C3%BAtbol.png"),
    ("20", "real_oviedo.png", "Real Oviedo", "https://upload.wikimedia.org/wikipedia/lt/1/1b/Real_Oviedo_CF_emblema.png")
]

teams_p2 = [
    ("01", "racing_santander.png", "Racing de Santander", "https://upload.wikimedia.org/wikipedia/lt/9/9d/R_racing_c_de_santander.gif"),
    ("02", "deportivo_la_coruna.png", "Deportivo La Coruña", "https://upload.wikimedia.org/wikipedia/lt/2/2c/Rc_deportivo_de_la_coruna.gif"),
    ("03", "almeria.png", "UD Almería", "https://upload.wikimedia.org/wikipedia/lt/9/97/Ud_almer%C3%ADa_180px.png"),
    ("04", "malaga.png", "Málaga CF", "https://upload.wikimedia.org/wikipedia/lt/6/6d/Malaga_cf.gif"),
    ("05", "las_palmas.png", "UD Las Palmas", "https://upload.wikimedia.org/wikipedia/lt/e/e2/UD_Las_Palmas_logo.png"),
    ("06", "castellon.png", "CD Castellón", "https://upload.wikimedia.org/wikipedia/lt/b/bb/Club_Deportivo_Castellon.png"),
    ("07", "burgos.png", "Burgos CF", "https://upload.wikimedia.org/wikipedia/lt/c/c4/Burgos_CF.png"),
    ("08", "eibar.png", "SD Eibar", "https://upload.wikimedia.org/wikipedia/lt/a/a6/SD_Eibar_logotipas.png"),
    ("09", "cordoba.png", "Córdoba CF", "https://upload.wikimedia.org/wikipedia/lt/9/93/C%C3%B3rdoba_CF_logo.png"),
    ("10", "sporting_gijon.png", "Sporting de Gijón", "https://upload.wikimedia.org/wikipedia/lt/b/bf/R_sporting_de_gijon.gif"),
    ("11", "ceuta.png", "AD Ceuta FC", "https://upload.wikimedia.org/wikipedia/lt/4/4b/AD_Ceuta_FC.png"),
    ("12", "albacete.png", "Albacete Balompié", "https://upload.wikimedia.org/wikipedia/lt/2/2b/Albacete_balompie.png"),
    ("13", "fc_andorra.png", "FC Andorra", "https://upload.wikimedia.org/wikipedia/lt/9/90/FC_Andorra.png"),
    ("14", "granada.png", "Granada CF", "https://upload.wikimedia.org/wikipedia/lt/c/c2/Granadacf.png"),
    ("15", "real_sociedad_b.png", "Real Sociedad B", "https://upload.wikimedia.org/wikipedia/lt/b/b2/Real_sociedad_de_futbol.png"),
    ("16", "leganes.png", "CD Leganés", "https://upload.wikimedia.org/wikipedia/lt/0/02/Club_Deportivo_Legan%C3%A9s.png"),
    ("17", "real_valladolid.png", "Real Valladolid", "https://upload.wikimedia.org/wikipedia/lt/a/aa/Real_valladolid_cf.gif"),
    ("18", "cadiz.png", "Cádiz CF", "https://upload.wikimedia.org/wikipedia/lt/e/e2/C%C3%A1diz_CF_logo.png"),
    ("19", "mirandes.png", "CD Mirandés", "https://upload.wikimedia.org/wikipedia/lt/8/85/CD_Mirand%C3%A9s.png"),
    ("20", "huesca.png", "SD Huesca", "https://upload.wikimedia.org/wikipedia/lt/1/16/SD_Huesca.png"),
    ("21", "cultural_leonesa.png", "Cultural Leonesa", "https://upload.wikimedia.org/wikipedia/lt/6/62/Cultural_y_Deportiva_Leonesa_logo.png"),
    ("22", "real_zaragoza.png", "Real Zaragoza", "https://upload.wikimedia.org/wikipedia/lt/5/5f/Real_cd_zaragoza.gif")
]

def process_league(teams_list, output_dir, league_title, accent1, accent2):
    processed = []
    print(f"\nProcessing {league_title}...")
    
    for num, filename, name, url in teams_list:
        time.sleep(2.0)
        print(f"[{num}] {name}...", end=" ", flush=True)
        raw_path = os.path.join(output_dir, f"raw_{filename}")
        std_path = os.path.join(output_dir, filename)
        num_path = os.path.join(output_dir, f"{num}_{filename}")
        
        downloaded = False
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=10) as resp, open(raw_path, 'wb') as f:
                    f.write(resp.read())
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
                print("OK!")
                processed.append({"num": num, "name": name, "filename": filename})
            if os.path.exists(raw_path):
                os.remove(raw_path)
        except Exception as e:
            print(f"Error: {e}")
            
    # Clean up temp files
    for f in os.listdir(output_dir):
        if f.startswith("raw_") or f.startswith("temp_"):
            try:
                os.remove(os.path.join(output_dir, f))
            except Exception:
                pass

    # Create index.html
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Futebol Espanha - {league_title}</title>
    <style>
        :root {{
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-color: #f8fafc;
            --accent-color: {accent1};
            --accent-glow: rgba(239, 68, 68, 0.2);
            --border-color: #334155;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg-color); color: var(--text-color); padding: 2rem 1rem; }}
        header {{ text-align: center; margin-bottom: 3rem; }}
        header h1 {{ font-size: 2.5rem; font-weight: 800; background: linear-gradient(135deg, {accent1}, {accent2}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem; }}
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
        <h1>Futebol Espanha - {league_title}</h1>
        <p>Coleção de imagens e escudos dos times da {league_title} de Espanha em alta resolução</p>
        <div class="stats-badge">{len(processed)} Imagens Padronizadas (1024x1024 PNG Transparente)</div>
    </header>
    <div class="grid">
"""

    for t in processed:
        html_content += f"""
        <div class="card">
            <div class="img-container"><img src="{t['filename']}" alt="{t['name']}"></div>
            <div class="team-name">{t['name']}</div>
            <div class="specs">1024 x 1024 PNG</div>
        </div>
"""

    html_content += """
    </div>
    <footer>
        <p>Formatos padronizados com fundo transparente e proporções mantidas.</p>
    </footer>
</body>
</html>
"""

    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved index.html for {league_title} with {len(processed)} teams.")

process_league(teams_p1, dir_p1, "Primera División (La Liga)", "#ef4444", "#eab308")
process_league(teams_p2, dir_p2, "Segunda División (LaLiga Hypermotion)", "#ef4444", "#3b82f6")
