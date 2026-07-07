#!/usr/bin/env python3
"""Standalone anchor verifier (Python stdlib only).

Usage:
    python3 verify_anchor.py anchors/2020-02-27.json

Recomputes the SHA-256 of the anchor's canonical_body and confirms it equals
the published anchor_hash. Exit 0 on match, 1 on mismatch.
"""

import hashlib
import json
import sys


def main(path: str) -> int:
    anchor = json.loads(open(path).read())
    recomputed = hashlib.sha256(anchor["canonical_body"].encode("utf-8")).hexdigest()
    ok = recomputed == anchor["anchor_hash"]
    print(f"ref_date      : {anchor['ref_date']}")
    print(f"published hash: {anchor['anchor_hash']}")
    print(f"recomputed    : {recomputed}")
    print("MATCH" if ok else "MISMATCH")
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
