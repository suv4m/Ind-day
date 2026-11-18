import json

# Load all files
with open("all_drive_media_recursive.json", "r", encoding="utf-8") as f:
    drive_data = json.load(f)

# The user's dropbox video links:
video_links = {
    "celebrationatunit": "https://www.dropbox.com/scl/fi/k3w9ntw1xev11up9302zg/celebrationatnccunit.mp4?rlkey=zb0b6yiiftax85yq5lc70ytp6&st=2h4wwhep&raw=1",
    "arrivalofchiefguest": "https://www.dropbox.com/scl/fi/esi8bajsc6hulrjf9yr3g/arrivalofchiefguest.mp4?rlkey=h6ah453jls6gruguwo5r9ijdn&st=uxzre2oz&raw=1",
    "chiefguestspeech": "https://www.dropbox.com/scl/fi/zi5mm26x0r6v8f0fv26ml/chiefguestspeech.mp4?rlkey=f0qucga9ogz7zqz9vc47vjrci&st=qx60wnsz&raw=1",
    "cinematicflag": "https://www.dropbox.com/scl/fi/ctse6jiz6e81s9nvmzt62/cinematicflag.mp4?rlkey=l2870jumraqz3wvi1e5sw0vj5&st=v87waim1&raw=1",
    "drill": "https://www.dropbox.com/scl/fi/a90rp1hnqokcucvtegg6j/drill.mp4?rlkey=nkwp83mvcwb0tf88fin4vi2lr&st=qha7ytvs&raw=1",
    "drill1": "https://www.dropbox.com/scl/fi/7n2f4w5ajt67l3rg44hns/drill1.mp4?rlkey=nwcnlmwoz5hghz449p18ygfxs&st=5xalb67d&raw=1",
    "drill2": "https://www.dropbox.com/scl/fi/xbi4h23h4cho7lu0iqzen/drill2.mp4?rlkey=4es6xk63z5xk1gmnyxhy8msd1&st=pewb1v3c&raw=1",
    "drill3": "https://www.dropbox.com/scl/fi/6cmcs3zgw1ewdxrgj0daf/drill3.mp4?rlkey=90gjb69bykt84e0k4wnmwgdrb&st=raln0c2x&raw=1",
    "drill4": "https://www.dropbox.com/scl/fi/jdfdwcldg16f4gem3kqck/drill4.mp4?rlkey=u5zb0b1lonfk8uoyb6fuwtmpj&st=mcob049k&raw=1",
    "drill5": "https://www.dropbox.com/scl/fi/u13q9xrp1b7b18cvv69zq/drill5.mp4?rlkey=wzzsy17k1xrofkvxbuc9ubvbk&st=z21m1thw&raw=1",
    "flaghoisting": "https://www.dropbox.com/scl/fi/dzy3vigcx18bynb6vf3gk/flaghoisting.mp4?rlkey=edrd9nycnxtsyp9v6nuy105za&st=iuo7vo4b&raw=1",
    "nationalanthem": "https://www.dropbox.com/scl/fi/ym14pjfcq4dmlgbaplz4g/nationalanthem.mp4?rlkey=hdrz1tdhiqnr0053aaa26fwn6&st=9g0qjeru&raw=1",
    "nirikshanoftroops": "https://www.dropbox.com/scl/fi/naq97cgkh8wuhvgau5ydr/nirikshanoftroops.mp4?rlkey=io0r82hgf5e8vzwemsgocowe4&st=8elbq75a&raw=1",
    "permissionfornirikshan": "https://www.dropbox.com/scl/fi/f2dsqkoo96c8k9tnnx4ru/permissionfornirikshan.mp4?rlkey=txww5zhr5ap2yxkpe392ggepk&st=npw6r7b0&raw=1",
    "songperformance": "https://www.dropbox.com/scl/fi/0zqa3uy62ciluvmvva8v3/songperformance.mp4?rlkey=kgiqws5g3mjxaa6hxiwjr2o9v&st=3e1ef3tq&raw=1",
    "visarjan": "https://www.dropbox.com/scl/fi/ryhd2xqnzia7plnbf223o/visarjan.mp4?rlkey=d6awphsipjiwdmahqpy0wl81l&st=88wza8ih&raw=1",
}

# Video metadata dictionary
video_meta = {
    "drill2": {"title": "Synchronized March Past & Drill Cadence", "desc": "Contingent cadence in full stride across the VSSUT Parade Ground", "tag": "HERO DRILL"},
    "drill3": {"title": "Cadet Precision Maneuvers", "desc": "Flawless squad alignment and synchronous boot-stomps", "tag": "MARCH PAST"},
    "permissionfornirikshan": {"title": "Reporting for Nirikshan", "desc": "Contingent Commander SUO reports with ceremonial sword salute", "tag": "COMMAND"},
    "nirikshanoftroops": {"title": "Inspection of Contingent", "desc": "Chief Guest Prof. Jaydev Rana accompanied by Lt. Birendra Kumar Barik inspects troops", "tag": "NIRIKSHAN"},
    "arrivalofchiefguest": {"title": "Arrival of the Chief Guest", "desc": "Formal reception and Guard of Honour for Prof. Jaydev Rana", "tag": "CEREMONY"},
    "flaghoisting": {"title": "Rashtriya Dhwaj Unfurling", "desc": "The Tricolor unfurls amidst floral petals over VSSUT Burla", "tag": "HONOUR"},
    "nationalanthem": {"title": "Rashtragaan & General Salute", "desc": "Jana Gana Mana echoes across the ground as the contingent presents arms", "tag": "SALUTE"},
    "drill": {"title": "Troop Formations & Stride", "desc": "SD & SW troops marching in cohesive unison", "tag": "DRILL"},
    "drill1": {"title": "Squad Turning Movements", "desc": "Sharp military pivots executed with regimental discipline", "tag": "PRECISION"},
    "drill4": {"title": "Rifle Squad & Guard Cadence", "desc": "Rifle squad maneuvering with fixed-bayonet posture", "tag": "RIFLE SQUAD"},
    "drill5": {"title": "Final Company Advance", "desc": "Contingent moving forward in review order", "tag": "REVIEW ORDER"},
    "chiefguestspeech": {"title": "Chief Guest Address", "desc": "Inspiring address by Prof. Jaydev Rana on youth and national duty", "tag": "ADDRESS"},
    "songperformance": {"title": "Patriotic Symphony", "desc": "Cultural vocal tribute celebrating India's independence", "tag": "CULTURAL"},
    "visarjan": {"title": "Ceremonial Visarjan", "desc": "The contingent completes the march-off with pride and thunderous applause", "tag": "VISARJAN"},
    "cinematicflag": {"title": "The Tiranga Flutter", "desc": "Slow-motion 4K study of the National Flag in the morning breeze", "tag": "TRICOLOR"},
    "celebrationatunit": {"title": "3 (O) BN NCC Unit Celebrations", "desc": "Cadets and Officers at Battalion HQ marking 78th Independence Day", "tag": "UNIT HQ"},
}

# Process all files
catalog = {
    "videos": [],
    "featured_ceremony": [],
    "featured_drill": [],
    "featured_unit": [],
    "archive_all": []
}

# 1. Process Videos
for key, url in video_links.items():
    meta = video_meta.get(key, {"title": key.title(), "desc": "4K Video Record", "tag": "CEREMONY"})
    item = {
        "id": f"vid_{key}",
        "key": key,
        "type": "video",
        "title": meta["title"],
        "desc": meta["desc"],
        "tag": meta["tag"],
        "src": url,
        "category": "video"
    }
    catalog["videos"].append(item)

# 2. Process Photos
for root, items in drive_data.items():
    for f in items:
        mime = f.get('mimeType', '')
        if not mime.startswith('image/'):
            continue
        fid = f.get('id')
        name = f.get('name', '')
        size = f.get('size', 0)
        path = f.get('folder_path', '')
        
        # Categorization logic
        cat = "archive"
        title = name.replace(".jpg", "").replace(".jpeg", "").replace("_", " ")
        lens = "Standard"
        
        lower_name = name.lower()
        if "commander" in lower_name or "sword" in lower_name:
            cat = "commanders"
            title = "Commanders with Ceremonial Sword"
            lens = "Telephoto 85mm"
        elif "nirikshan" in lower_name:
            cat = "nirikshan"
            title = "Contingent Inspection (Nirikshan)"
            lens = "Wide 24mm"
        elif "parade" in lower_name or "drill" in lower_name:
            cat = "drill"
            title = "Cadet March Past & Drill Cadence"
            lens = "Telephoto 135mm"
        elif "sd_troop" in lower_name:
            cat = "troops"
            title = "Senior Division (SD) Troop"
            lens = "Standard 50mm"
        elif "sw_troop" in lower_name:
            cat = "troops"
            title = "Senior Wing (SW) Troop"
            lens = "Standard 50mm"
        elif "rifle" in lower_name:
            cat = "rifle_squad"
            title = "Ceremonial Rifle Squad"
            lens = "Telephoto 85mm"
        elif "band" in lower_name or "drum" in lower_name or "song" in lower_name:
            cat = "cultural"
            title = "Military Band & Drummers Detachment"
            lens = "Standard 50mm"
        elif "chiefguest" in lower_name or "speech" in lower_name or "stage" in lower_name or "delegate" in lower_name:
            cat = "dignitaries"
            title = "Dignitaries & Chief Guest Address"
            lens = "Wide 35mm"
        elif "unit" in lower_name or "jco" in lower_name or "anosir" in lower_name:
            cat = "unit"
            title = "3 (O) BN NCC Unit Fellowship"
            lens = "Wide 24mm"
        elif "security" in lower_name:
            cat = "security"
            title = "Security Guards Troop"
            lens = "Standard 50mm"
        elif "group" in lower_name:
            cat = "group"
            title = "Contingent Official Portrait"
            lens = "Ultra-Wide 16mm"
        else:
            cat = "candid"
            title = "Battalion Cadet Memory"
            lens = "Candid 35mm"

        photo_item = {
            "id": fid,
            "filename": name,
            "title": title.title(),
            "category": cat,
            "lens": lens,
            "thumb": f"https://drive.google.com/thumbnail?id={fid}&sz=w800",
            "full": f"https://drive.google.com/thumbnail?id={fid}&sz=w1920",
            "path": path,
            "size": size
        }
        
        catalog["archive_all"].append(photo_item)

print(f"Catalog generated: {len(catalog['videos'])} videos, {len(catalog['archive_all'])} photos.")

with open("catalog.json", "w", encoding="utf-8") as out:
    json.dump(catalog, out, indent=2)
