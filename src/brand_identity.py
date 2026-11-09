"""Responsive Maxine identity, using only the existing authentic family portrait."""
from html import escape


def brand_markup(brand, prefix, name, footer=False):
    if brand != 'maxine':
        return escape(name)
    loading = 'lazy' if footer else 'eager'
    return (
        '<span class="maxine-brand' + (' maxine-brand--footer' if footer else '') + '">'
        '<span class="maxine-brand__frame" aria-hidden="true">'
        '<img src="' + escape(prefix, quote=True) + 'assets/maxine-portrait.webp" '
        'alt="" width="400" height="475" loading="' + loading + '" decoding="async">'
        '</span><span class="maxine-brand__type">'
        '<span class="maxine-brand__the">The </span>'
        '<span class="maxine-brand__name">Maxine </span>'
        '<span class="maxine-brand__project">Project</span>'
        '</span></span>'
    )
