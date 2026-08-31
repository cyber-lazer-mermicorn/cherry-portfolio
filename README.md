# cherry-portfolio

**Live:** [lazermermicorn.com](https://lazermermicorn.com)

Public gateway for Cyber Lazer Mermicorn — constellation map, hire lanes, Calendly embed.

## Stack

- Static HTML + `cinematic.css` + `cinematic.js`
- Deployed on Vercel (project `cherry-portfolio`)
- Domains: `lazermermicorn.com`, `portfolio.lazermermicorn.com`

## Local setup

```bash
git clone https://github.com/cyber-lazer-mermicorn/cherry-portfolio.git
cd cherry-portfolio
# any static server, e.g.
npx serve .
# open http://localhost:3000
```

No env vars required for the public site.

## Deploy

Push to `main`. Vercel auto-deploys when Git is linked.

Optional:

```bash
./deploy-portfolio.sh
```

## Structure

| File | Role |
|------|------|
| `index.html` | Page structure + content |
| `cinematic.css` | Design system |
| `cinematic.js` | Scroll focus, reveals, soft parallax |
| `sitemap.xml` | SEO |
| `robots.txt` | Crawl rules |
| `vercel.json` | Security + cache headers |

## Status

See [STATUS.md](./STATUS.md). Prefer honest WIP labels over empty claims.
