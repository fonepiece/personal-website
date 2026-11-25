# Reyhan Taze portfolio migration

The repository contains a standalone static version of the public portfolio at reyhantaze.com, recovered on November 25, 2026. The earlier portfolio remains recoverable in Git history.

## Included

- Homepage, About page, and all five public case studies.
- Local copies of the portfolio images, résumé PDF, and Work Sans fonts.
- Relative links compatible with both `/personal-website/` and the custom domain.
- Original case-study paths under `p/`.
- Responsive layouts and keyboard-accessible navigation.

The layout was rebuilt from public content; it is not an exact export of UXfolio. Device mockups are shown as images without decorative device frames. Galleries use horizontal scrolling. Figma prototypes and social links remain external services. Review the layouts and prototype availability before replacing the current site.

## Publish with GitHub Pages

1. In this repository, open **Settings → Pages**.
2. Choose **Deploy from a branch**, branch **main**, folder **/(root)**, and save.
3. Review the published site at `https://fonepiece.github.io/personal-website/`.
4. When satisfied, save `reyhantaze.com` as the custom domain in Pages settings, then update DNS.
5. Enable **Enforce HTTPS** after the certificate is available.

This commit does not change DNS or enable Pages automatically.

## Edit or preview

Edit the HTML pages directly. Shared styling is in `assets/site.css`.

To preview locally, run `python3 -m http.server 8765` and open `http://localhost:8765/`.

Run `python3 scripts/check-portfolio.py` to check local links and asset references.
