#!/usr/bin/env python3
"""Build a reproducible, self-contained Full Chain distribution guide and package."""
from __future__ import annotations
import argparse
import html
import os
from pathlib import Path
import re
import subprocess
import sys
import markdown

GUIDE_VERSION = "1.0.0"
PACKAGE_VERSION = "1.0.0"
ROOT = Path(__file__).resolve().parent
WEB = ROOT / "web"
SOURCE_GUIDE = ROOT / "GUIA_DE_USO.md"
README_SOURCE = ROOT / "DISTRIBUTION_README_001.md"
EXAMPLE_SOURCE = ROOT / "examples" / "full-chain-diamond-001.json"

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-commit", default=os.environ.get("SOURCE_COMMIT", ""))
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    source_commit = args.source_commit.strip()
    if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        print("ERROR: --source-commit must be the full 40-character checked-out Git SHA", file=sys.stderr)
        return 2
    out = Path(args.output_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)
    guide = SOURCE_GUIDE.read_text(encoding="utf-8")
    guide = guide.replace("{{GUIDE_VERSION}}", GUIDE_VERSION)
    guide = guide.replace("{{PACKAGE_VERSION}}", PACKAGE_VERSION)
    guide = guide.replace("{{SOURCE_COMMIT}}", source_commit)
    if "{{" in guide or "}}" in guide:
        print("ERROR: unresolved template marker in guide", file=sys.stderr)
        return 2
    (out / "GUIA_DE_USO.md").write_text(guide, encoding="utf-8", newline="\n")
    body = markdown.markdown(guide, extensions=["extra", "sane_lists"])
    document = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="guide-version" content="%s">
<meta name="package-version" content="%s">
<meta name="source-commit" content="%s">
<title>Guía de uso — Demostrador Full Chain TGCV</title>
<style>
:root { color-scheme: light dark; font-family: system-ui, -apple-system, "Segoe UI", sans-serif; line-height: 1.6; }
body { max-width: 900px; margin: 0 auto; padding: 2rem 1.25rem 4rem; }
h1, h2, h3 { line-height: 1.25; margin-top: 1.7em; }
code { overflow-wrap: anywhere; }
pre { overflow: auto; padding: 1rem; border: 1px solid #8886; border-radius: .5rem; }
a { text-underline-offset: .15em; }
</style>
</head>
<body>
<main>
%s
</main>
</body>
</html>
""" % (GUIDE_VERSION, PACKAGE_VERSION, source_commit, body)
    (out / "GUIA_DE_USO.html").write_text(document, encoding="utf-8", newline="\n")
    readme = README_SOURCE.read_text(encoding="utf-8").rstrip() + """

## Guía de uso incluida

- [Guía completa en Markdown (descargable)](GUIA_DE_USO.md)
- [Guía en HTML (se puede abrir sin conexión)](GUIA_DE_USO.html)

## Identidad de esta distribución

- Versión del paquete: `%s`
- Versión de la guía: `%s`
- Commit fuente exacto: `%s`
- Identidad legible por máquina: [VERSION_DISTRIBUCION.txt](VERSION_DISTRIBUCION.txt)

La guía y el HTML se incluyen en este paquete; los enlaces anteriores son relativos a esta carpeta.
""" % (PACKAGE_VERSION, GUIDE_VERSION, source_commit)
    (out / "README.md").write_text(readme + "\n", encoding="utf-8", newline="\n")
    version = (
        "package_version=%s\n"
        "guide_version=%s\n"
        "source_commit=%s\n"
        "markdown_renderer=Python-Markdown %s\n"
    ) % (PACKAGE_VERSION, GUIDE_VERSION, source_commit, markdown.__version__)
    (out / "VERSION_DISTRIBUCION.txt").write_text(version, encoding="utf-8", newline="\n")
    import shutil
    shutil.copy2(WEB / "index.html", out / "index.html")
    shutil.copy2(EXAMPLE_SOURCE, out / "example-diamond.json")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
