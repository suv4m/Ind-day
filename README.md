# Cadence · Interactive 15th Aug Showcase

An interactive, scroll-driven visual story celebrating the 80th Independence Day (15 August 2026) at **VSSUT Burla** and the **3 (O) BN NCC** battalion.

The goal was simple: bring the energy, rhythm, and pride of the parade ground to life on screen—the sound of boots marching in unison, the salute of ceremonial swords, the flag unfurling into the morning sky, and the quiet camaraderie shared among cadets back at the unit.

---

## The Core Challenge: Everything in a Single HTML File

From the start, we gave ourselves one strict constraint: **the entire experience had to live inside a single, self-contained `index.html` file.**

Building a media-rich website with 150+ high-resolution photographs and over a dozen parade video clips is already demanding. Packing all of that—plus custom animations, audio synthesis, smooth physics, and dynamic video streaming—into one file without any server-side framework or runtime dependencies was the real engineering puzzle.

Why do it this way?
* **Zero Deployment Friction:** It runs anywhere. You can double-click it on your desktop, host it for free on GitHub Pages, or copy-paste it directly as an embed code into Google Sites.
* **No Fragile Dependencies:** There is no heavy `node_modules` folder to maintain, no complicated build chain, and no backend server that can fail.

---

## How It Came Together

### Sifting Through Media Chaos with Antigravity & MCP
After the celebration, we had hundreds of gigabytes of raw DSLR photographs and heavy 4K parade videos sitting in Google Drive folders—unnamed, unorganized, and mixed together.

Instead of spending days manually downloading, renaming, and sorting through files, we connected **Antigravity** using a custom **Google Drive MCP (Model Context Protocol)** skill:
* Antigravity crawled our Google Drive folders directly through MCP.
* It scanned every photo and video, read metadata and aspect ratios, and analyzed image orientations.
* It helped us curate the best shots for every moment—from tight telephoto closeups of commanders to wide-angle shots of the full contingent—and organized them into a structured catalog (`catalog.json`) ready for the web.

```text
┌───────────────────────────┐      ┌───────────────────────────┐      ┌───────────────────────────┐
│     Google Drive MCP      │      │   catalog.json Pipeline   │      │         build.py          │
│  (Automated asset crawler │ ───► │  (Aspect-ratio indexing,  │ ───► │   (Deterministic Python   │
│   & metadata extractor)   │      │   tagging & CDN mapping)  │      │    compiler + SHA check)  │
└───────────────────────────┘      └───────────────────────────┘      └─────────────┬─────────────┘
                                                                                    │
                                                                                    ▼
                                                                      ┌───────────────────────────┐
                                                                      │        index.html         │
                                                                      │   (Self-contained 65KB    │
                                                                      │    production showcase)   │
                                                                      └───────────────────────────┘
```

---

## Engineering Challenges & How We Solved Them

* **Static Video Hosting & Bitrate Engineering:** Autoplaying 12+ HD parade clips without expensive streaming servers meant avoiding Dropbox bandwidth caps and GitHub download prompts. We re-encoded clips to balanced web bitrates (~4.5 Mbps for 1080p, ~2.2 Mbps for 720p), hosted them on GitHub Pages with a jsDelivr CDN backup, and built an adaptive fallback that steps down to 720p on slower connections.
* **Connection Bottlenecks & First-Impression Stalls:** Browsers cap concurrent downloads at 6 connections per domain. Firing all assets at once initially choked the network and stalled the hero video. We built a custom priority manager (`VM` & `IQ`) that reserves 100% of bandwidth for the hero clip first (synced with the loader bar), pauses background image downloads during video fetches, and preloads upcoming clips nearest-first into memory (Blob URLs) for instant playback.
* **From Stacked Layouts to a Single Fixed Stage:** Early stacked sections felt generic and suffered from overlapping text. We moved the entire experience into a single fixed viewport container (`#stage`) driven by a master GSAP scroll timeline, with strict visibility culling (`visibility: hidden` for off-screen scenes) to keep memory usage low across all 14 scenes.
* **Eliminating Premature Animation & Layer Glitches:** A timeline initialization glitch initially caused future photos and titles to bleed through before their cues arrived. Isolating layer starting states and cleaning up timeline trigger boundaries ensured every wipe, accordion, and reveal fires in exact choreographed sequence.
* **Preserving Natural Framing & Aspect Ratios:** Fixed cropping containers were cutting people and ceremonial swords out of group photos. By programmatically measuring image dimensions upfront, balancing masonry columns by natural proportions, and applying custom focal points (`object-position`), all cadets and dignitaries stay properly framed.
* **Mobile Responsiveness & Google Sites Embed Compatibility:** Desktop headlines wrapped awkwardly over faces on mobile screens, and custom scroll hijacking broke inside embedded iframes like Google Sites. We resolved this by adopting native touch scrolling (`touch-action: pan-y`), responsive single-line typographic scaling (`clamp`), and smooth scroll synchronization via Lenis that behaves reliably inside iframes.

---

## Project Structure & How to Run

```text
.
├── index.html       # The complete, standalone single-file showcase
├── build.py         # Python builder that compiles and verifies index.html
├── README.md        # The project story and documentation
├── .gitignore       # Keeps private Drive API tokens and caches safe
└── tools/
    └── drive-mcp/   # Google Drive MCP tools, scrapers, and asset catalog
```

### Running Locally
You don't need Node.js, npm, or any external packages. Simply open `index.html` in your browser.

If you want to run a local server:
```bash
python -m http.server 8000
```
Open [http://localhost:8000](http://localhost:8000) to view the site.

### Rebuilding from Source
If you ever want to rebuild or verify `index.html`, run:
```bash
python build.py
```
The script will assemble the HTML and check its cryptographic SHA-256 hash to ensure a 100% exact match with the production version.

---

## Deployment

* **GitHub Pages:** Push to GitHub, go to **Settings → Pages**, and choose **Deploy from branch (`main` / root)**.
* **Google Sites:** Open your Google Site editor, choose **Insert → Embed → Embed Code**, and paste the contents of `index.html`.

---

**Tech Stack:** GSAP 3 (ScrollTrigger) · Lenis Smooth Scroll · Web Audio API · Google Drive MCP · GitHub Pages & jsDelivr CDN · Python 3

*Visual flow and cinematic pacing inspired by [Zendetta](https://www.zendetta.com/) on Awwwards.*
