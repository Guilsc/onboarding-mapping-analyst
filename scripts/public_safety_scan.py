#!/usr/bin/env python3
"""Safety checks for the public Onboarding Mapping Analyst repository/package."""

from __future__ import annotations

import argparse
import io
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath

SELF = Path(__file__).resolve()

TEXT_SUFFIXES = {
    ".md", ".txt", ".yml", ".yaml", ".py", ".csv", ".svg", ".xml",
    ".json", ".html", ".htm", ".toml",
}
OFFICE_SUFFIXES = {".docx", ".xlsx", ".pptx"}
ARCHIVE_TEXT_SUFFIXES = TEXT_SUFFIXES | {".rels"}

FORBIDDEN_PATTERNS = [
    ("client name", re.compile(r"\bEquifax\b", re.IGNORECASE)),
    ("client acronym", re.compile(r"\bEWS\b", re.IGNORECASE)),
    ("internal channel", re.compile(r"\bUCIF\b", re.IGNORECASE)),
    ("internal channel", re.compile(r"\bMCIF\b", re.IGNORECASE)),
    ("internal service", re.compile(r"eqx-onboarding", re.IGNORECASE)),
    ("internal service", re.compile(r"efx-onboarding", re.IGNORECASE)),
    ("internal service", re.compile(r"apis-eqx-gcp", re.IGNORECASE)),
    ("internal identifier", re.compile(r"\bInternal EFX\b", re.IGNORECASE)),
    ("internal identifier", re.compile(r"\bHIREtech\b", re.IGNORECASE)),
    ("internal identifier", re.compile(r"\bCDH EFX\b", re.IGNORECASE)),
]

REQUIRED_PACKAGE_ENTRIES = {
    "00_START_HERE.md",
    "MANIFEST.md",
    "README.md",
    "01_Agent_Core/01_AGENT_IDENTITY.md",
    "01_Agent_Core/03_ROUTER.md",
    "02_Skills/00_SKILL_CATALOG.md",
    "03_Registries/Onboarding_Mapping_Agent_Knowledge_Registries.xlsx",
    "08_Interface_Setup/GEM_SETUP.md",
    "08_Interface_Setup/BOOTSTRAP_CHECKLIST.md",
    "docs/Onboarding_Mapping_Analyst_Confluence_Solution_Guide.docx",
}
FORBIDDEN_PACKAGE_PREFIXES = (".github/", "scripts/", ".git/", "dist/")


def find_forbidden(text: str, location: str) -> list[str]:
    hits: list[str] = []
    for label, pattern in FORBIDDEN_PATTERNS:
        match = pattern.search(text)
        if match:
            hits.append(f"{location}: {label} -> {match.group(0)!r}")
    return hits


def scan_office_bytes(data: bytes, location: str) -> list[str]:
    hits: list[str] = []
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as office:
            for member in office.infolist():
                suffix = PurePosixPath(member.filename).suffix.lower()
                if suffix not in ARCHIVE_TEXT_SUFFIXES:
                    continue
                try:
                    text = office.read(member).decode("utf-8", errors="ignore")
                except Exception:
                    continue
                hits.extend(find_forbidden(text, f"{location}!{member.filename}"))
    except zipfile.BadZipFile:
        hits.append(f"{location}: invalid Office/OpenXML archive")
    return hits


def scan_repo(root: Path) -> list[str]:
    hits: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts or "dist" in path.parts:
            continue
        if path.resolve() == SELF:
            continue

        suffix = path.suffix.lower()
        if suffix in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8", errors="ignore")
            hits.extend(find_forbidden(text, str(path)))
        elif suffix in OFFICE_SUFFIXES:
            hits.extend(scan_office_bytes(path.read_bytes(), str(path)))
    return hits


def scan_package(path: Path) -> list[str]:
    hits: list[str] = []
    try:
        with zipfile.ZipFile(path) as package:
            names = set(package.namelist())

            missing = sorted(REQUIRED_PACKAGE_ENTRIES - names)
            for item in missing:
                hits.append(f"{path}: missing required package entry {item}")

            for name in sorted(names):
                if name.endswith("/"):
                    continue
                if any(name.startswith(prefix) for prefix in FORBIDDEN_PACKAGE_PREFIXES):
                    hits.append(f"{path}: repository/build-only content must not ship -> {name}")
                    continue

                suffix = PurePosixPath(name).suffix.lower()
                data = package.read(name)
                if suffix in TEXT_SUFFIXES:
                    text = data.decode("utf-8", errors="ignore")
                    hits.extend(find_forbidden(text, f"{path}!{name}"))
                elif suffix in OFFICE_SUFFIXES:
                    hits.extend(scan_office_bytes(data, f"{path}!{name}"))
    except zipfile.BadZipFile:
        hits.append(f"{path}: invalid deployment ZIP")
    return hits


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--repo", action="store_true", help="Scan repository source/generated files")
    group.add_argument("--package", type=Path, help="Validate and scan deployment ZIP")
    args = parser.parse_args()

    hits = scan_repo(Path(".")) if args.repo else scan_package(args.package)

    if hits:
        print("Public-safety validation failed:", file=sys.stderr)
        for hit in hits:
            print(f"  - {hit}", file=sys.stderr)
        return 1

    target = "repository" if args.repo else str(args.package)
    print(f"Public-safety validation passed: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
