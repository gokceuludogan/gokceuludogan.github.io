#!/usr/bin/env python3
"""Check that the homepage reflects required identity data and has no placeholders."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

CHECKS = {
    "_config.yml": ["Gökçe Uludoğan", "gokce.uludogan@bogazici.edu.tr", "oAiBbasAAAAJ"],
    "_pages/about.md": [
        "PUFFIN",
        "STAR-GO",
        "Boğaziçi University",
        "TURNA",
        "HSD-2Lang",
        'class="pub-tag"',
        "BibTeX",
        'class="education-list"',
        'aria-label="Why is it called PUFFIN?"',
        'aria-label="Why is it called TURNA?"',
        "/assets/images/TURNA.jpg",
    ],
    "_data/navigation.yml": ["#publications", "#research", "#experience"],
    "_includes/scripts.html": ["copy-bibtex.js"],
    "assets/js/copy-bibtex.js": ["Copy BibTeX", "navigator.clipboard", "execCommand"],
}

PLACEHOLDERS = ("Lorem ipsum", "YOUR_GOOGLE_SCHOLAR_ID", "RayeRen")


def main() -> int:
    problems: list[str] = []
    for relative, required in CHECKS.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for value in required:
            if value not in text:
                problems.append(f"{relative}: missing {value!r}")

    site_files = [ROOT / "_config.yml", ROOT / "_pages/about.md", ROOT / "_data/navigation.yml"]
    for path in site_files:
        text = path.read_text(encoding="utf-8")
        for placeholder in PLACEHOLDERS:
            if placeholder in text:
                problems.append(f"{path.relative_to(ROOT)}: placeholder remains: {placeholder!r}")

    if problems:
        print("Academic-site validation failed:")
        print("\n".join(f"- {problem}" for problem in problems))
        return 1

    print("Academic-site content checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
