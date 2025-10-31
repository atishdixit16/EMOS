# EMOS Website Deployment

This repository automatically deploys to GitHub Pages at: `https://aprilaihub.github.io/EMOS`

## Setup Instructions

1. **Enable GitHub Pages** (one-time setup):
   - Go to your repository Settings → Pages
   - Set Source to "GitHub Actions"
   - The site will be available at `https://aprilaihub.github.io/EMOS`

2. **Automatic Deployment**:
   - Every push to `master` branch triggers automatic deployment
   - GitHub Actions builds Sphinx docs and deploys the complete site
   - Check the Actions tab to monitor deployment status

## Local Development

To test locally before deploying:

```bash
# Build Sphinx documentation
cd docs
sphinx-build -b html . _build/html
cd ..

# Serve locally (Python)
python -m http.server 8000

# Or serve locally (Node.js)
npx http-server . -p 8000
```

Visit `http://localhost:8000` to preview the site.

## Site Structure

- **Main Pages**: `index.html`, `about.html`, `team.html`, `documentation.html`
- **Styles**: `styles.css`, `navigation.css`, `navigation.js`
- **Documentation**: Built from `docs/` using Sphinx
- **Images**: `images/` folder with logos and team photos

## Deployment Workflow

The GitHub Actions workflow (`.github/workflows/deploy-site.yml`):

1. Builds Sphinx documentation from `docs/` folder
2. Copies main website files to `_site/`
3. Copies built docs to `_site/docs/`
4. Deploys to GitHub Pages

## Backend Note

GitHub Pages only hosts static files. The Flask backend (`backend/app.py`) cannot run on GitHub Pages and would need separate hosting (e.g., Render, Railway, Heroku) if required for future features.