#!/usr/bin/env python3
"""Deterministically validate and copy the exact HIVE V2 R01-R20 frozen master.

This tool performs no Markdown parsing or rewriting. It reads source bytes,
verifies fixed identity hashes/size, then writes the same bytes to the archive
path. Git commit/push/review remain separate governed operations.
"""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path

EXPECTED_SIZE = 1_334_369
EXPECTED_SHA256 = "990c441d5797ee3f8ec81a1f3337f83bb0516fcc0c2a79ef0ef9f4a150b020ee"
EXPECTED_GIT_BLOB_SHA = "6e2620854cb3180e02ac4c18fe21c93bb5dffdcd"
EXPECTED_PREFIX = b"# HIVE \xe2\x80\x94 MASTER SOURCE V2.0 \xe2\x80\x94 FROZEN ARCHITECTURE EDITION\n"

def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("repo_root", type=Path)
    args = parser.parse_args()

    source = args.source.resolve()
    repo_root = args.repo_root.resolve()
    target = repo_root / "docs/archive/HIVE-MASTER-SOURCE-V2.0-FROZEN.md"

    data = source.read_bytes()
    size = len(data)
    sha256 = hashlib.sha256(data).hexdigest()
    blob_sha = git_blob_sha(data)

    failures = []
    if size != EXPECTED_SIZE:
        failures.append(f"size {size} != {EXPECTED_SIZE}")
    if sha256 != EXPECTED_SHA256:
        failures.append(f"sha256 {sha256} != {EXPECTED_SHA256}")
    if blob_sha != EXPECTED_GIT_BLOB_SHA:
        failures.append(f"git blob {blob_sha} != {EXPECTED_GIT_BLOB_SHA}")
    if not data.startswith(EXPECTED_PREFIX):
        failures.append("frozen master header mismatch")
    if b"\r\n" in data:
        failures.append("unexpected CRLF transformation detected")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 2

    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        existing = target.read_bytes()
        if existing != data:
            print("FAIL: target exists with different bytes")
            return 3
        print("PASS: target already contains exact source bytes")
    else:
        target.write_bytes(data)
        print(f"PASS: copied exact bytes to {target}")

    copied = target.read_bytes()
    if hashlib.sha256(copied).hexdigest() != EXPECTED_SHA256:
        print("FAIL: post-copy SHA-256 mismatch")
        return 4
    if git_blob_sha(copied) != EXPECTED_GIT_BLOB_SHA:
        print("FAIL: post-copy Git blob SHA mismatch")
        return 5

    print(f"SIZE={len(copied)}")
    print(f"SHA256={EXPECTED_SHA256}")
    print(f"GIT_BLOB_SHA={EXPECTED_GIT_BLOB_SHA}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
