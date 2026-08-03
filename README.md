# Portfolio — Daniel Yewenu

A Flask-based personal portfolio site. Home, About, Projects, and Contact pages, styled as an
engineering blueprint/schematic — dark technical blue, monospace data labels, and a signature
"title block" (the drawn-by/sheet-number stamp real engineering drawings use) anchoring every page.

Live projects are pulled from `server.py` — edit the `PROJECTS` list there to add, remove, or
update anything without touching the templates.

## Running locally

```
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 server.py
```

Visit `http://127.0.0.1:5000`.

## Before you deploy — two things to fill in

1. **`templates/contact.html`** — replace the placeholder LinkedIn link (currently `href="#"`)
   with your real profile URL.
2. **`server.py`** — the `PROJECTS` list currently features ENSOP, the Adaptive Firewall, the
   SIEM Dashboard, and the Web Vuln Scanner. Swap in different projects or reorder as your
   portfolio evolves.

## Deploying to Render (free)

1. Push this repo to GitHub.
2. Go to [render.com](https://render.com), sign up/log in with GitHub.
3. **New → Web Service**, select this repo.
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn server:app`
6. Deploy. Render gives you a free `your-app-name.onrender.com` URL.

## Tech

Flask, vanilla CSS (no framework), Google Fonts (Space Grotesk, Inter, JetBrains Mono).
