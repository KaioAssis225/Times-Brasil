import urllib.request
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

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

exact_fix = [
    # King Cup Arabia
    ("Futebol Arabia Saudita", "02", "kings_cup.png", "King Cup (Copa do Rei)", [
        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/King_Cup_Saudi_Arabia_logo.svg/800px-King_Cup_Saudi_Arabia_logo.svg.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/King_Cup_Saudi_Arabia_logo.svg/800px-King_Cup_Saudi_Arabia_logo.svg.png"
    ]),
    # Taça de Portugal
    ("Futebol Portugal", "02", "taca_de_portugal.png", "Taça de Portugal", [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Ta%C3%A7a_de_Portugal_logo.svg/800px-Ta%C3%A7a_de_Portugal_logo.svg.png",
        "https://upload.wikimedia.org/wikipedia/en/thumb/2/26/Ta%C3%A7a_de_Portugal_logo.svg/800px-Ta%C3%A7a_de_Portugal_logo.svg.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Portuguese_shield.svg/800px-Portuguese_shield.svg.png"
    ]),
    # Egyptian Super Cup
    ("Futebol Egito", "03", "egyptian_super_cup.png", "Egyptian Super Cup", [
        "https://upload.wikimedia.org/wikipedia/en/thumb/7/7d/Egyptian_Super_Cup_logo.svg/800px-Egyptian_Super_Cup_logo.svg.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Egyptian_Super_Cup_logo.svg/800px-Egyptian_Super_Cup_logo.svg.png"
    ]),
    # Copa Bicentenario Peru
    ("Futebol Peru", "02", "copa_bicentenario.png", "Copa Bicentenario", [
        "https://upload.wikimedia.org/wikipedia/commons/3/3d/Copa_Bicentenario_logo.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Copa_Bicentenario_logo.png/800px-Copa_Bicentenario_logo.png"
    ]),
    # Bolivia (FBF Logo)
    ("Futebol Bolivia", "01", "primera_division_bolivia.png", "Primera División de Bolivia", [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Federaci%C3%B3n_Boliviana_de_F%C3%BAtbol_%28FBF%29_logo.svg/800px-Federaci%C3%B3n_Boliviana_de_F%C3%BAtbol_%28FBF%29_logo.svg.png"
    ]),
    ("Futebol Bolivia", "02", "copa_division_profesional.png", "Copa División Profesional", [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Federaci%C3%B3n_Boliviana_de_F%C3%BAtbol_%28FBF%29_logo.svg/800px-Federaci%C3%B3n_Boliviana_de_F%C3%BAtbol_%28FBF%29_logo.svg.png"
    ])
]

raw_tmp = "temp_vector_fix.png"

for country_folder, num, fn, name, urls in exact_fix:
    print(f"[{country_folder}] {name}...", end=" ", flush=True)
    time.sleep(2.0)
    
    downloaded = False
    for u in urls:
        try:
            req = urllib.request.Request(u, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp, open(raw_tmp, 'wb') as f:
                f.write(resp.read())
            if os.path.exists(raw_tmp) and os.path.getsize(raw_tmp) > 2000:
                downloaded = True
                print(f"Downloaded from {u}", end=" -> ", flush=True)
                break
        except Exception as e:
            pass
            
    if downloaded:
        try:
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
        except Exception as e:
            print(f"Image error: {e}")
    else:
        print("Download failed")
