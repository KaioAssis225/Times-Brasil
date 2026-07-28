import os
from PIL import Image
import urllib.request
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

dir_p1 = r"c:\Users\matheus.cardoso\Desktop\Times Brasil\Futebol Belgica\Primera Division"
CANVAS_SIZE = (1024, 1024)
TARGET_SIZE = 880

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

final_6 = [
    ("standard_liege.png", "07", "Standard Liège", ["https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Standard_Li%C3%A8ge_logo.svg/330px-Standard_Li%C3%A8ge_logo.svg.png"]),
    ("charleroi.png", "08", "Sporting Charleroi", ["https://upload.wikimedia.org/wikipedia/fr/thumb/0/02/RSC_Charleroi_logo.svg/300px-RSC_Charleroi_logo.svg.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/RSC_Charleroi_logo.svg/300px-RSC_Charleroi_logo.svg.png"]),
    ("stvv.png", "10", "Sint-Truidense VV", ["https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/STVV_logo.svg/300px-STVV_logo.svg.png"]),
    ("westerlo.png", "11", "KVC Westerlo", ["https://upload.wikimedia.org/wikipedia/en/1/17/K.V.C._Westerlo_logo.png"]),
    ("cercle_brugge.png", "12", "Cercle Brugge", ["https://upload.wikimedia.org/wikipedia/commons/b/bd/Logo_Cercle_Brugge_2022.png"]),
    ("dender.png", "15", "FC Dender EH", ["https://upload.wikimedia.org/wikipedia/en/9/98/FCVDenderEH.png"])
]

for fn, num, name, urls in final_6:
    std_path = os.path.join(dir_p1, fn)
    num_path = os.path.join(dir_p1, f"{num}_{fn}")
    raw_path = os.path.join(dir_p1, f"raw_{fn}")
    
    downloaded = False
    for url in urls:
        time.sleep(1.0)
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp, open(raw_path, 'wb') as f:
                f.write(resp.read())
            if os.path.getsize(raw_path) > 2500:
                downloaded = True
                print(f"[{num}] {name} downloaded OK from {url}")
                break
        except Exception as e:
            print(f"Failed {name} on {url}: {e}")
            
    if downloaded:
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
                print(f"[{num}] {name} 100% OK!")
            if os.path.exists(raw_path):
                os.remove(raw_path)
        except Exception as e:
            print(f"Error processing {name}: {e}")

all_belgium = [
    ("01", "club_brugge.png", "Club Brugge"), ("02", "anderlecht.png", "RSC Anderlecht"),
    ("03", "genk.png", "KRC Genk"), ("04", "gent.png", "KAA Gent"),
    ("05", "antwerp.png", "Royal Antwerp FC"), ("06", "union_sg.png", "Royale Union Saint-Gilloise"),
    ("07", "standard_liege.png", "Standard Liège"), ("08", "charleroi.png", "Sporting Charleroi"),
    ("09", "mechelen.png", "KV Mechelen"), ("10", "stvv.png", "Sint-Truidense VV"),
    ("11", "westerlo.png", "KVC Westerlo"), ("12", "cercle_brugge.png", "Cercle Brugge"),
    ("13", "oh_leuven.png", "OH Leuven"), ("14", "kortrijk.png", "KV Kortrijk"),
    ("15", "dender.png", "FC Dender EH"), ("16", "beerschot.png", "K. Beerschot V.A.")
]

processed = []
for num, filename, name in all_belgium:
    if os.path.exists(os.path.join(dir_p1, filename)):
        processed.append({"num": num, "name": name, "filename": filename})

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Futebol Bélgica - Primera División (Belgian Pro League)</title>
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
        <h1>Futebol Bélgica - Primera División (Belgian Pro League)</h1>
        <p>Coleção de imagens e escudos dos 16 times da Belgian Pro League em alta resolução</p>
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

with open(os.path.join(dir_p1, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Saved final index.html for Belgian Pro League with {len(processed)} teams!")
