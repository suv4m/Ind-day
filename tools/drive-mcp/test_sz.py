import urllib.request

fid = "15kfzTOVQakVcfaibbAeAilA48y_cMkyA"
urls = [
    f"https://drive.google.com/thumbnail?id={fid}&sz=w1600",
    f"https://drive.google.com/thumbnail?id={fid}&sz=w1920",
    f"https://drive.google.com/thumbnail?id={fid}&sz=w1000",
    f"https://lh3.googleusercontent.com/d/{fid}"
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(f"{u} -> {resp.status}, {resp.headers.get('Content-Type')}, size: {resp.headers.get('Content-Length')}")
    except Exception as e:
        print(f"{u} -> ERROR: {e}")
