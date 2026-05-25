#!/usr/bin/env python3
"""Scan Indonesian text for common AI-sounding phrases.

This helper is intentionally simple. It surfaces likely tone problems so an
editor can review them; it does not decide whether a phrase is always wrong.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


PATTERNS = {
    "overblown_opener": [
        r"\bdi era digital yang terus berkembang\b",
        r"\bdalam lanskap\b",
        r"\bseiring dengan perkembangan\b",
        r"\bdi tengah pesatnya perkembangan\b",
        r"\bpada era modern ini\b",
    ],
    "vague_importance": [
        r"\bmemainkan peran penting\b",
        r"\bmenjadi kunci\b",
        r"\baspek krusial\b",
        r"\bsangat vital\b",
        r"\bmendorong transformasi\b",
        r"\bdampak signifikan\b",
    ],
    "marketing_mush": [
        r"\bsolusi inovatif\b",
        r"\bpengalaman yang mulus\b",
        r"\bsecara komprehensif\b",
        r"\bsecara optimal\b",
        r"\bmemberdayakan pengguna\b",
        r"\bmenghadirkan nilai\b",
        r"\bekosistem digital\b",
    ],
    "english_calque": [
        r"\bmenavigasi tantangan\b",
        r"\blanskap kompetitif\b",
        r"\bberesonansi dengan\b",
        r"\bmengorkestrasi\b",
        r"\bmengkurasi\b",
        r"\bmendorong keterlibatan\b",
        r"\bdapat ditindaklanjuti\b",
    ],
    "bureaucratic_padding": [
        r"\bdalam rangka\b",
        r"\bguna melakukan\b",
        r"\bmelaksanakan kegiatan\b",
        r"\bterkait dengan\b",
        r"\bsehubungan dengan hal tersebut\b",
        r"\bmelakukan optimalisasi\b",
        r"\bmelakukan pemantauan\b",
        r"\bmelakukan koordinasi\b",
    ],
    "formulaic_contrast": [
        r"\btidak hanya\b.*\btetapi juga\b",
        r"\bbukan sekadar\b.*\bmelainkan\b",
        r"\blebih dari sekadar\b",
    ],
    "weak_conclusion": [
        r"\bpada akhirnya\b",
        r"\bdengan demikian\b",
        r"\bsecara keseluruhan\b",
        r"\bhal ini menunjukkan bahwa\b",
    ],
}


def read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def scan(text: str) -> dict:
    findings = []
    lower = text.lower()

    for category, patterns in PATTERNS.items():
        for pattern in patterns:
            for match in re.finditer(pattern, lower, flags=re.DOTALL):
                snippet = text[match.start() : match.end()]
                findings.append(
                    {
                        "category": category,
                        "line": line_number(text, match.start()),
                        "match": snippet,
                    }
                )

    words = re.findall(r"\b[\w'-]+\b", lower, flags=re.UNICODE)
    repeated = [
        {"word": word, "count": count}
        for word, count in Counter(words).most_common()
        if count >= 8 and len(word) > 4
    ][:20]

    return {
        "summary": {
            "findings": len(findings),
            "repeated_words": len(repeated),
        },
        "findings": findings,
        "repeated_words": repeated,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan Indonesian text for common AI-sounding phrases."
    )
    parser.add_argument("path", nargs="?", help="Text file to scan. Reads stdin if omitted.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    args = parser.parse_args()

    result = scan(read_text(args.path))
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
