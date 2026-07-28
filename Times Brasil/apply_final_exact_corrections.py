import os
import sys
import time
import urllib.request
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base_dirs = [
    r"Z:\Kaio\Times Brasil",
    r"c:\Users\matheus.cardoso\Desktop\Times Brasil"
]

CANVAS_SIZE = (1024, 1024)
TARGET_SIZE = 880

headers = {'User-Agent': 'AntigravityFixBot/3.0 (https://example.org; bot@example.org) Python/3.14'}

corrections = [
    # 1. King Cup (Saudi)
    ("Futebol Arabia Saudita", "02", "kings_cup.png", "King Cup (Copa do Rei)", "https://upload.wikimedia.org/wikipedia/en/thumb/2/2f/Saudi_Arabian_Football_Federation_logo.svg/500px-Saudi_Arabian_Football_Federation_logo.svg.png"),
    # 2. Taça de Portugal (Icon Trophy Taça de Portugal)
    ("Futebol Portugal", "02", "taca_de_portugal.png", "Taça de Portugal", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Icon_Trophy_Ta%C3%A7a_de_Portugal_%28Cup_of_Portugal%29.svg/500px-Icon_Trophy_Ta%C3%A7a_de_Portugal_%28Cup_of_Portugal%29.svg.png"),
    # 3. Egyptian Super Cup (EFA Emblem)
    ("Futebol Egito", "03", "egyptian_super_cup.png", "Egyptian Super Cup", "https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Egyptian_Football_Association_logo.svg/500px-Egyptian_Football_Association_logo.svg.png"),
    # 4. Copa Bicentenario (FPF Emblem)
    ("Futebol Peru", "02", "copa_bicentenario.png", "Copa Bicentenario", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Federaci%C3%B3n_Peruana_de_F%C3%BAtbol_logo.svg/500px-Federaci%C3%B3n_Peruana_de_F%C3%BAtbol_logo.svg.png"),
    # 5. Bolivia Primera Division & Copa Division Profesional (FBF Emblem)
    ("Futebol Bolivia", "01", "primera_division_bolivia.png", "Primera División de Bolivia", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Federaci%C3%B3n_Boliviana_de_F%C3%BAtbol_%28FBF%29_logo.svg/500px-Federaci%C3%B3n_Boliviana_de_F%C3%BAtbol_%28FBF%29_logo.svg.png"),
    ("Futebol Bolivia", "02", "copa_division_profesional.png", "Copa División Profesional", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Federaci%C3%B3n_Boliviana_de_F%C3%BAtbol_%28FBF%29_logo.svg/500px-Federaci%C3%B3n_Boliviana_de_F%C3%BAtbol_%28FBF%29_logo.svg.png")
]

raw_tmp = "temp_corr.png"

for country_folder, num, fn, name, url in corrections:
    print(f"[{country_folder}] Updating {name}...", end=" ", flush=True)
    time.sleep(1.0)
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp, open(raw_tmp, 'wb') as f:
            f.write(resp.read())
            
        if os.path.exists(raw_tmp) and os.path.getsize(raw_tmp) > 2000:
            with Image.open(raw_tmp) as img:
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
                
                for b_dir in base_dirs:
                    target_dir = os.path.join(b_dir, country_folder, "Torneios")
                    if os.path.exists(os.path.dirname(target_dir)):
                        os.makedirs(target_dir, exist_ok=True)
                        std_p = os.path.join(target_dir, fn)
                        num_p = os.path.join(target_dir, f"{num}_{fn}")
                        canvas.save(std_p, "PNG", optimize=True)
                        canvas.save(num_p, "PNG", optimize=True)
                print("100% FIXED & UPDATED!")
            if os.path.exists(raw_tmp):
                os.remove(raw_tmp)
        else:
            print("Download failed / size small")
    except Exception as e:
        print(f"Error: {e}")

# Regenerate index.html galleries for affected folders across both base_dirs
affected_folders = set(item[0] for item in corrections)
affected_folders.update(["Futebol Argentina", "Futebol Belgica", "Futebol Chile", "Futebol Colombia", "Futebol Escocia", "Futebol Italia", "Futebol Portugal"])

for b_dir in base_dirs:
    for country_folder in affected_folders:
        target_dir = os.path.join(b_dir, country_folder, "Torneios")
        if not os.path.exists(target_dir):
            continue
            
        pngs = [f for f in sorted(os.listdir(target_dir)) if f.endswith(".png") and not f.startswith("raw_") and not (f[0:2].isdigit() and f[2] == "_")]
        
        html_title = f"{country_folder} - Logos dos Torneios e Copas"
        html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html_title}</title>
    <style>
        :root {{
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-color: #f8fafc;
            --accent-color: #38bdf8;
            --accent-glow: rgba(56, 189, 248, 0.2);
            --border-color: #334155;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg-color); color: var(--text-color); padding: 2rem 1rem; }}
        header {{ text-align: center; margin-bottom: 3rem; }}
        header h1 {{ font-size: 2.5rem; font-weight: 800; background: linear-gradient(135deg, #38bdf8, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem; }}
        header p {{ color: #94a3b8; font-size: 1.1rem; }}
        .stats-badge {{ display: inline-block; background: var(--accent-glow); border: 1px solid var(--accent-color); color: var(--accent-color); padding: 0.4rem 1rem; border-radius: 9999px; font-weight: 600; font-size: 0.9rem; margin-top: 1rem; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 1.5rem; max-width: 1400px; margin: 0 auto; }}
        .card {{ background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 1rem; padding: 1.5rem; display: flex; flex-direction: column; align-items: center; transition: all 0.3s ease; }}
        .card:hover {{ transform: translateY(-5px); border-color: var(--accent-color); box-shadow: 0 10px 25px -5px var(--accent-glow); }}
        .img-container {{ width: 160px; height: 160px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; background-image: linear-gradient(45deg, #182234 25%, transparent 25%), linear-gradient(-45deg, #182234 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #182234 75%), linear-gradient(-45deg, transparent 75%, #182234 75%); background-size: 16px 16px; border-radius: 0.75rem; padding: 10px; }}
        .img-container img {{ max-width: 100%; max-height: 100%; object-fit: contain; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.5)); }}
        .team-name {{ font-size: 1.1rem; font-weight: 700; text-align: center; margin-bottom: 0.5rem; }}
        .specs {{ font-size: 0.8rem; color: #64748b; text-align: center; }}
        footer {{ text-align: center; margin-top: 4rem; color: #64748b; font-size: 0.9rem; }}
    </style>
</head>
<body>
    <header>
        <h1>{html_title}</h1>
        <p>Coleção oficial de escudos e logos das competições e torneios (PNG 1024x1024 Transparente)</p>
        <div class="stats-badge">{len(pngs)} Logotipos Padronizados</div>
    </header>
    <div class="grid">
"""

        for t in pngs:
            name = t.replace(".png", "").replace("_", " ").title()
            html_content += f"""
        <div class="card">
            <div class="img-container"><img src="{t}" alt="{name}"></div>
            <div class="team-name">{name}</div>
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

        with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)

print("\nUpdated all galleries and completed all corrections!")
