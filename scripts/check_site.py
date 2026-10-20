"""Check the real Jekyll output before publishing this personal site."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROUTES = (
    "/", "/posts/", "/categories/", "/tags/", "/projects/", "/about/",
    "/projects/recorded-lore/", "/projects/recorded-lore/devlog/",
    "/projects/recorded-lore/worldbuilding/",
)
SITE_HOST = "lasorie95.github.io"


class Page(HTMLParser):
    def __init__(self, source: str):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.text = []
        self.hidden_depth = 0
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hidden_depth += 1
        for key, value in attrs:
            if key in ("href", "src") and value:
                self.links.append(value)

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden_depth = max(0, self.hidden_depth - 1)

    def handle_data(self, value):
        if not self.hidden_depth:
            self.text.append(value)


def route_file(site_dir: Path, route: str) -> Path:
    path = site_dir / unquote(urlsplit(route).path).lstrip("/")
    return path / "index.html" if not path.suffix else path


def read_page(site_dir: Path, route: str) -> str:
    return route_file(site_dir, route).read_text(encoding="utf-8")


def check_site(site_dir: Path) -> list[str]:
    errors = []
    root = site_dir.resolve()
    sources = {}
    for route in ROUTES:
        try:
            sources[route] = read_page(root, route)
        except (FileNotFoundError, IsADirectoryError):
            errors.append(f"Missing page: {route}")

    expected_text = {
        "/": ("Lasorie RPG World",),
        "/about/": ("TA를 지향하는 일반인 입니다.", "C#", "Godot", "2D dot Graphic"),
        "/projects/recorded-lore/": ("Recorded Lore", "개발일지", "세계관"),
        "/projects/recorded-lore/devlog/": ("Recorded Lore", "개발일지"),
        "/projects/recorded-lore/worldbuilding/": ("Recorded Lore", "세계관"),
    }
    for route, words in expected_text.items():
        if route in sources:
            text = " ".join(Page(sources[route]).text)
            for word in words:
                if word not in text:
                    errors.append(f"Missing visible content at {route}: {word}")

    for route, source in sources.items():
        page = Page(source)
        for link in page.links:
            url = urlsplit(link)
            if url.scheme == "mailto":
                errors.append(f"Unprovided contact link at {route}")
            if url.scheme not in ("", "http", "https") or (url.netloc and url.netloc != SITE_HOST):
                continue
            if not url.path or not url.path.startswith("/"):
                continue
            target = route_file(root, url.path)
            if not target.resolve().is_relative_to(root):
                errors.append(f"Internal link leaves output directory: {link}")
            elif not target.is_file():
                errors.append(f"Broken internal link at {route}: {link}")

    for excluded in (".vscode", "docs", "scripts", "README.md", "Gemfile", "Gemfile.lock"):
        if (root / excluded).exists():
            errors.append(f"Development file is published: {excluded}")
    for required in (
        "sitemap.xml", "feed.xml", "assets/css/main.css", "assets/js/main.min.js",
        "assets/fonts/Galmuri11.woff2", "assets/fonts/PretendardVariable.woff2",
        "assets/fonts/Galmuri-OFL.md", "assets/fonts/Pretendard-LICENSE.txt",
    ):
        if not (root / required).is_file():
            errors.append(f"Missing generated asset: {required}")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", required=True, type=Path)
    args = parser.parse_args()
    problems = check_site(args.site_dir)
    if problems:
        print("FAIL\n" + "\n".join(problems))
        raise SystemExit(1)
    print(f"PASS: {len(ROUTES)} pages, links, profile, and publication boundaries")
