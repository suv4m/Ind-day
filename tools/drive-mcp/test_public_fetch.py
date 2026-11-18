import urllib.request

test_ids = [
    ("troopparade1", "1zcicIDxPTsH4eOURF0Cfx2Oxuy-U2DLe"),
    ("celebrationatnccunit", "1qfEOQGPaxMoD9SYR4jemd8DuchiJazGI"),
    ("groupphotoofficialwithanosir", "1qDeF0JWXZXWxwo6xfHLU_EUQhXz90p-W")
]

for name, fid in test_ids:
    # Test Google Drive thumbnail endpoint
    url1 = f"https://drive.google.com/thumbnail?id={fid}&sz=w1600"
    req1 = urllib.request.Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req1, timeout=10) as resp:
            print(f"[{name}] thumbnail sz=w1600 -> {resp.status}, Content-Type: {resp.headers.get('Content-Type')}, Size: {resp.headers.get('Content-Length')}")
    except Exception as e:
        print(f"[{name}] thumbnail FAILED: {e}")

    # Test lh3 endpoint
    url2 = f"https://lh3.googleusercontent.com/d/{fid}"
    req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req2, timeout=10) as resp:
            print(f"[{name}] lh3/d/ -> {resp.status}, Content-Type: {resp.headers.get('Content-Type')}, Size: {resp.headers.get('Content-Length')}")
    except Exception as e:
        print(f"[{name}] lh3 FAILED: {e}")
