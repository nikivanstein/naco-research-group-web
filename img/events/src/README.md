Event banners, all made from one HTML template.

- `banner.html`: the template (card 1200x628 and wide 1180x200 layouts, background motifs).
- `banners.js`: texts, colours and logos per conference and per event.
- `logos/`: conference logos.

Render with the preinstalled Playwright (optionally pass a name filter):

    node img/events/src/render.js img/events [name-filter]

Each event gets `<key>.png` (card, used on the events grid and as social preview)
and `<key>-wide.png` (banner on top of the event page, `largeimage`).

Then shrink the PNGs (keeps them visually identical):

    python img/events/src/compress.py img/events/*.png
