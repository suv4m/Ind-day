import urllib.request

test_files = [
    ("cinematicflag", "1t-vcKyRdSP5KBuuAbTYztJnYinCKXv3V"),
    ("troopparade1", "1zcicIDxPTsH4eOURF0Cfx2Oxuy-U2DLe"),
    ("celebrationatnccunit", "1qfEOQGPaxMoD9SYR4jemd8DuchiJazGI")
]

for name, fid in test_files:
    url = f"https://lh3.googleusercontent.com/d/{fid}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[{name}] {url} -> Status {resp.status}, Content-Type: {resp.headers.get('Content-Type')}, Length: {resp.headers.get('Content-Length')}")
    except Exception as e:
        print(f"[{name}] {url} -> FAILED: {e}")
