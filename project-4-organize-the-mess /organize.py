"""
Organize the Mess — Downloads folder cleanup
-----------------------------------------------
What this does:
  Scans the Downloads folder and, following the rules in brief.md:
    1. Finds true duplicates by comparing file CONTENT (not just names).
    2. Flags oversized files for manual review (doesn't move them).
    3. Plans where every other file should go, grouped by type.
  Runs in two modes:
    --dry-run   : only PRINTS the plan, touches nothing.
    --execute   : actually performs the moves shown in the last dry run.

Expects: a Downloads folder in the same directory as this script, and a
Downloads-backup folder that must NEVER be read from or written to.

Rules encoded: see brief.md.
"""

import hashlib
import os
import shutil
import sys

SOURCE = "Downloads"
BACKUP = "Downloads-backup"
LARGE_FILE_THRESHOLD_MB = 4

TYPE_MAP = {
    ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents",
    ".jpg": "Images", ".png": "Images", ".jpeg": "Images",
    ".exe": "Installers",
    ".zip": "Archives",
    ".mp4": "Other",
}


def file_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def guess_type_folder(filename):
    # handle compound extensions like .pdf.txt by checking the true suffix
    lower = filename.lower()
    for ext, folder in TYPE_MAP.items():
        if lower.endswith(ext):
            return folder
    return "Other"


def build_plan():
    assert os.path.isdir(SOURCE), f"{SOURCE} folder not found"
    files = [f for f in os.listdir(SOURCE) if os.path.isfile(os.path.join(SOURCE, f))]

    hashes = {}
    duplicates = []
    large_files = []
    moves = []
    skipped = []

    for fname in sorted(files):
        full_path = os.path.join(SOURCE, fname)
        try:
            size_mb = os.path.getsize(full_path) / (1024 * 1024)
            h = file_hash(full_path)
        except Exception as e:
            skipped.append((fname, str(e)))
            continue

        if size_mb > LARGE_FILE_THRESHOLD_MB:
            # Rule: large files are flagged for manual review, NOT auto-moved
            large_files.append((fname, round(size_mb, 2)))
            continue

        if h in hashes:
            # true content duplicate of an earlier file
            duplicates.append((fname, hashes[h]))
            moves.append((fname, f"{SOURCE}/_duplicates/{fname}"))
        else:
            hashes[h] = fname
            dest_folder = guess_type_folder(fname)
            moves.append((fname, f"{SOURCE}/{dest_folder}/{fname}"))

    return moves, duplicates, large_files, skipped


def print_plan(moves, duplicates, large_files, skipped):
    print("=== DRY RUN: PROPOSED PLAN (nothing has been changed yet) ===\n")
    print(f"{'OLD LOCATION':<45} -> NEW LOCATION")
    for old, new in moves:
        print(f"{SOURCE}/{old:<40} -> {new}")

    print(f"\n--- TRUE DUPLICATES DETECTED (by content, not just filename) ---")
    if duplicates:
        for dup, original in duplicates:
            print(f"'{dup}' is identical in content to '{original}' -> will move to _duplicates, NOT deleted")
    else:
        print("None found.")

    print(f"\n--- LARGE FILES FLAGGED FOR REVIEW (> {LARGE_FILE_THRESHOLD_MB} MB) ---")
    if large_files:
        for fname, size in large_files:
            print(f"'{fname}' is {size} MB -- flagged, will NOT be auto-moved without review")
    else:
        print("None found.")

    if skipped:
        print(f"\n--- SKIPPED (could not read) ---")
        for fname, err in skipped:
            print(f"'{fname}': {err}")

    print(f"\nDowntown-backup folder: NOT touched, NOT read from, NOT written to.")
    print(f"\nTotal files to be moved: {len(moves)}")
    print("\nNo files have been changed. Re-run with --execute to apply this exact plan.")


def execute_plan(moves):
    for old, new in moves:
        old_path = os.path.join(SOURCE, old)
        new_path = new
        os.makedirs(os.path.dirname(new_path), exist_ok=True)
        shutil.move(old_path, new_path)
    print(f"Executed. {len(moves)} files moved. Nothing deleted, nothing touched in {BACKUP}.")


if __name__ == "__main__":
    moves, duplicates, large_files, skipped = build_plan()
    if "--execute" in sys.argv:
        execute_plan(moves)
    else:
        print_plan(moves, duplicates, large_files, skipped)
