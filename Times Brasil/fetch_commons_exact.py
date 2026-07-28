import urllib.request
import urllib.parse
import json
import os
import sys
import time
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base_dirs = [
    r"Z:\Kaio\Times Brasil",
    r"c:\Users\matheus.cardoso\Desktop\Times Brasil"
]

CANVAS_SIZE = (1024, 1024)
TARGET_SIZE = 880

headers = {'User-Agent': 'AntigravityCommonsBot/1.0 (https://example.org; bot@example.org) Python/3.14'}

targets = [
    ("Futebol Egito", "03", "egyptian_super_cup.png", "Egyptian Super Cup", "File:Egyptian Football Association logo.svg"),
    ("Futebol Peru", "02", "copa_bicentenario.png", "Copa Bicentenario", "File:Federación Peruana de Fútbol logo.svg"),
    ("Futebol Bolivia", "01", "primera_division_bolivia.png", "Primera División de Bolivia", "File:Federación Boliviana de Fútbol (FBF) logo.svg"),
    ("Futebol Bolivia", "02", "copa_division_profesional.png", "Copa División Profesional", "File:Federación Boliviana de Fútbol (FBF) logo.svg")
]

raw_tmp = "temp_commons_exact.png"

for country_folder, num, fn, name, wiki_file in targets:
    print(f"[{country_folder}] {name}...", end=" ", flush=True)
    time.sleep(1.0)
    
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(wiki_file)}&prop=imageinfo&iiprop=url&iiurlwidth=500&format=json"
    img_url = None
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get("query", {}).get("pages", {})
            for p_id, p_val in pages.items():
                ii = p_val.get("imageinfo", [])
                if ii:
                    img_url = ii[0].get("thumburl") or ii[0].get("url")
                    break
    except Exception as e:
        print(f"API Error: {e}", end=" ")
        
    if img_url:
        try:
            dl_req = urllib.request.Request(img_url, headers=headers)
            with urllib.request.urlopen(dl_req, timeout=10) as dl_resp, open(raw_tmp, 'wb') as f:
                f.write(dl_resp.read())
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
                    print("100% FIXED!")
                if os.path.exists(raw_tmp):
                    os.remove(raw_tmp)
            else:
                print("Download failed / size small")
        except Exception as e:
            print(f"Error processing: {e}")
    else:
        print("No API URL found")
