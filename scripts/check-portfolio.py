"""Check that every local page, image, stylesheet, and font reference resolves."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
import re

root = Path(__file__).resolve().parents[1]
errors = []
checked = 0

class Check(HTMLParser):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.base = 'https://example.test/' + str(page.relative_to(root))

    def handle_starttag(self, tag, attrs):
        global checked
        attrs = dict(attrs)
        if tag == 'base':
            self.base = urljoin(self.base, attrs['href'])
            return
        for attr in ('href', 'src'):
            value = attrs.get(attr)
            if not value:
                continue
            url = urlparse(urljoin(self.base, value))
            if url.netloc != 'example.test' or url.scheme not in ('http', 'https'):
                continue
            target = root / unquote(url.path).lstrip('/')
            if target.is_dir():
                target /= 'index.html'
            checked += 1
            if not target.is_file():
                errors.append(f'{self.page.relative_to(root)}: missing {value}')

pages = list(root.rglob('*.html'))
for page in pages:
    Check(page).feed(page.read_text())
for css in root.rglob('*.css'):
    for value in re.findall(r'url\(([^)]+)\)', css.read_text()):
        checked += 1
        if not (css.parent / value.strip('\"\'')).is_file():
            errors.append(f'Missing CSS asset: {value}')
assert len(pages) == 7, f'Expected seven pages; found {len(pages)}'
assert not errors, '\n'.join(errors)
print(f'PASS: {len(pages)} pages, {checked} local references; no missing files.')
