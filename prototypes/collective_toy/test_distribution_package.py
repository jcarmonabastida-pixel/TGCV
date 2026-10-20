#!/usr/bin/env python3
"""Fail-closed structural and provenance checks for the staged distribution."""
from pathlib import Path
import argparse
import re
import sys

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--package-dir", required=True)
    p.add_argument("--source-commit", required=True)
    args = p.parse_args()
    root = Path(args.package_dir)
    required = ["index.html", "README.md", "example-diamond.json", "GUIA_DE_USO.md", "GUIA_DE_USO.html", "VERSION_DISTRIBUCION.txt"]
    missing = [name for name in required if not (root / name).is_file()]
    if missing:
        print("FAIL missing files: " + ", ".join(missing))
        return 1
    readme = (root / "README.md").read_text(encoding="utf-8")
    guide = (root / "GUIA_DE_USO.md").read_text(encoding="utf-8")
    page = (root / "GUIA_DE_USO.html").read_text(encoding="utf-8")
    version = (root / "VERSION_DISTRIBUCION.txt").read_text(encoding="utf-8")
    for link in ["GUIA_DE_USO.md", "GUIA_DE_USO.html", "VERSION_DISTRIBUCION.txt"]:
        if f"]({link})" not in readme or not (root / link).is_file():
            print("FAIL README link missing/broken: " + link)
            return 1
    if "Versión de la guía: 1.0.0" not in guide or "Versión del paquete: 1.0.0" not in guide:
        print("FAIL guide version missing")
        return 1
    if args.source_commit not in guide or args.source_commit not in readme or args.source_commit not in version or args.source_commit not in page:
        print("FAIL source commit not consistently embedded")
        return 1
    if "{{SOURCE_COMMIT}}" in guide or "{{SOURCE_COMMIT}}" in page or not re.search(r"source_commit=[0-9a-f]{40}", version):
        print("FAIL unresolved metadata template")
        return 1
    if "<html lang=\"es\">" not in page or "<main>" not in page or "Tres modalidades de entrada" not in guide:
        print("FAIL HTML/guide structure incomplete")
        return 1
    if re.search(r"https?://(?:cdn\.|unpkg\.com|cdnjs\.)", page, re.I):
        print("FAIL external CDN dependency in offline HTML")
        return 1
    if (root / "example-diamond.json").stat().st_size == 0 or (root / "index.html").stat().st_size == 0:
        print("FAIL empty executable or example")
        return 1
    print("PASS distribution files, relative links, guide/package versions, source SHA, offline HTML")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
