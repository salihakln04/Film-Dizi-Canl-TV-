import requests

SOURCES = [
    "https://raw.githubusercontent.com/salihakln04/Film-Dizi-Canl-TV-/refs/heads/main/filmdizitv.m3u",
    "https://raw.githubusercontent.com/salihakln04/film-dizi-arsiv/refs/heads/main/KekikAkademi.m3u.txt",
    "https://raw.githubusercontent.com/salihakln04/film-dizi-arsiv/refs/heads/main/D%C3%BCnya%20Kupas%C4%B1%204K%20-%20TRT%20(1440p).m3u.txt",
    "https://raw.githubusercontent.com/salihakln04/film-dizi-arsiv/refs/heads/main/jetfilm_tum.m3u.txt",
    "https://raw.githubusercontent.com/salihakln04/film-dizi-arsiv/refs/heads/main/filmmodu_tum.m3u.txt",
    "https://raw.githubusercontent.com/salihakln04/film-dizi-arsiv/refs/heads/main/power-sinema.m3u.txt",
    "https://raw.githubusercontent.com/salihakln04/film-dizi-arsiv/refs/heads/main/fhdfi_tum.m3u.txt",
    "https://raw.githubusercontent.com/salihakln04/film-dizi-arsiv/refs/heads/main/filmmakinesi_tum.m3u.txt",
    "https://github.com/salihakln04/film-dizi-arsiv/raw/refs/heads/main/filmler_full.m3u.txt"
]

def fetch(url):
    try:
        r = requests.get(url, timeout=20)
        return r.text if r.status_code == 200 else ""
    except:
        return ""

all_items = set()

for url in SOURCES:
    print("indiriliyor:", url)
    data = fetch(url)

    for line in data.splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            all_items.add(line)

with open("filmdizitv.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for i in sorted(all_items):
        f.write(i + "\n")

print("bitti")
