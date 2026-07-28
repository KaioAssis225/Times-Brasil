import os
from PIL import Image

dir_p1 = r"c:\Users\matheus.cardoso\Desktop\Times Brasil\Futebol Espanha\Primera Division"
dir_p2 = r"c:\Users\matheus.cardoso\Desktop\Times Brasil\Futebol Espanha\Segunda Division"

CANVAS_SIZE = (1024, 1024)
TARGET_SIZE = 880

teams_p1 = [
    ("01", "real_madrid.png", "Real Madrid"),
    ("02", "barcelona.png", "FC Barcelona"),
    ("03", "atletico_madrid.png", "Atlético Madrid"),
    ("04", "athletic_bilbao.png", "Athletic Bilbao"),
    ("05", "real_sociedad.png", "Real Sociedad"),
    ("06", "real_betis.png", "Real Betis"),
    ("07", "villarreal.png", "Villarreal CF"),
    ("08", "valencia.png", "Valencia CF"),
    ("09", "sevilla.png", "Sevilla FC"),
    ("10", "osasuna.png", "CA Osasuna"),
    ("11", "celta_vigo.png", "RC Celta de Vigo"),
    ("12", "rayo_vallecano.png", "Rayo Vallecano"),
    ("13", "getafe.png", "Getafe CF"),
    ("14", "girona.png", "Girona FC"),
    ("15", "mallorca.png", "RCD Mallorca"),
    ("16", "alaves.png", "Deportivo Alavés"),
    ("17", "espanyol.png", "RCD Espanyol"),
    ("18", "levante.png", "Levante UD"),
    ("19", "elche.png", "Elche CF"),
    ("20", "real_oviedo.png", "Real Oviedo")
]

teams_p2 = [
    ("01", "racing_santander.png", "Racing de Santander"),
    ("02", "deportivo_la_coruna.png", "Deportivo La Coruña"),
    ("03", "almeria.png", "UD Almería"),
    ("04", "malaga.png", "Málaga CF"),
    ("05", "las_palmas.png", "UD Las Palmas"),
    ("06", "castellon.png", "CD Castellón"),
    ("07", "burgos.png", "Burgos CF"),
    ("08", "eibar.png", "SD Eibar"),
    ("09", "cordoba.png", "Córdoba CF"),
    ("10", "sporting_gijon.png", "Sporting de Gijón"),
    ("11", "ceuta.png", "AD Ceuta FC"),
    ("12", "albacete.png", "Albacete Balompié"),
    ("13", "fc_andorra.png", "FC Andorra"),
    ("14", "granada.png", "Granada CF"),
    ("15", "real_sociedad_b.png", "Real Sociedad B"),
    ("16", "leganes.png", "CD Leganés"),
    ("17", "real_valladolid.png", "Real Valladolid"),
    ("18", "cadiz.png", "Cádiz CF"),
    ("19", "mirandes.png", "CD Mirandés"),
    ("20", "huesca.png", "SD Huesca"),
    ("21", "cultural_leonesa.png", "Cultural Leonesa"),
    ("22", "real_zaragoza.png", "Real Zaragoza")
]

def process_and_build(teams_list, output_dir, league_title, accent1, accent2):
    processed = []
    print(f"\nFinal Processing for {league_title}...")
    
    for num, filename, name in teams_list:
        raw_path = os.path.join(output_dir, f"raw_{filename}")
        std_path = os.path.join(output_dir, filename)
        num_path = os.path.join(output_dir, f"{num}_{filename}")
        
        target_src = raw_path if os.path.exists(raw_path) else (std_path if os.path.exists(std_path) else None)
        
        if target_src:
            try:
                with Image.open(target_src) as img:
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
                    print(f"[{num}] {name} processed 100% OK!")
                    processed.append({"num": num, "name": name, "filename": filename})
            except Exception as e:
                print(f"Error processing {target_src}: {e}")
                
        if os.path.exists(raw_path):
            try:
                os.remove(raw_path)
            except Exception:
                pass

    # Clean up raw_ files
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

process_and_build(teams_p1, dir_p1, "Primera División (La Liga)", "#ef4444", "#eab308")
process_and_build(teams_p2, dir_p2, "Segunda División (LaLiga Hypermotion)", "#ef4444", "#3b82f6")
