# Project 4 — Organize the Mess (The Files You Forgot)

## The Problem
My Downloads folder had accumulated clutter: duplicate files saved under
different names (browser auto-renaming), forgotten documents, screenshots,
installers, and a large video file. Unlike the other three projects, this
one involves real file operations — moving files — where a careless script
could do real damage. This project follows the safety discipline required
before letting code touch real files.

## AI Tool Used
Claude (Claude.ai / Claude Sonnet), using its code-execution ("write and run
code") capability, in a sandboxed folder built to mirror a realistic messy
Downloads folder.

## The Brief I Gave the AI
See `brief.md`. Key rules:
- Never touch the backup folder, under any circumstance.
- Never delete anything — duplicates get moved to `_duplicates/`, not
  removed.
- "Duplicate" means identical file CONTENT, not just similar filenames.
- Oversized files are flagged for manual review, never auto-moved.

## The Safety Ritual (followed in order)
1. **Copy first** — the entire Downloads folder was copied to
   `Downloads-backup` before anything else happened, and verified identical
   with a diff.
2. **Wrote the brief** — plain-language definition of "clean," see above.
3. **Demanded a dry run** — the script's `--dry-run` mode lists every
   proposed move (old location -> new location) and changes nothing.
4. **Reviewed the plan** — see "What Worked / What Didn't" below: I caught
   a real bug at this step, before any file was touched.
5. **Approved and executed** — only after the corrected plan looked right
   did I run `--execute`.
6. **Verified and kept** — confirmed the backup folder still has all 16
   original files, and the live folder is now organized as expected.

## How I Verified the Result
- Confirmed the backup folder file count is still 16 (unchanged) after
  execution — proof nothing in the backup was touched.
- Manually reviewed the dry-run's duplicate list: I had deliberately built
  4 true content-duplicates into the test data (e.g.
  `vacation-photo1.jpg` and `IMG_2044.jpg`, same content, different names)
  and the script correctly found all 4, including cases where the filenames
  didn't look alike at all — the known-answer test for this project.

## Result / Catch
- **4 true duplicate files found** (identified by content, not filename)
  and safely moved to `_duplicates/` for manual review — no data deleted.
- **1 oversized file flagged** (a stand-in for a real large video/render
  file) for manual review instead of being silently moved or ignored.
- **15 files correctly sorted** into Documents / Images / Installers /
  Archives.
- **A real bug caught during plan review**: my first version of the script
  moved the large file into a type folder anyway, contradicting my own
  brief's rule that large files should only be flagged, not moved. I caught
  this by actually reading the dry-run output before approving — exactly
  the habit this task is meant to teach — and fixed it before executing.

## What Worked / What Didn't
- Worked well: building the dry-run as a separate mode (`--dry-run` vs.
  `--execute`) made the safety ritual concrete instead of just a promise —
  the same script literally cannot execute without a separate explicit step.
- Caught a real mistake: the plan-review step is not just theater — it
  found an actual contradiction between the brief and the first version of
  the code, before any files moved.
- Content-based duplicate detection (hashing file contents) was
  essential — filename-based matching alone would have missed
  `vacation-photo1.jpg` / `IMG_2044.jpg`, a real duplicate with no
  filename similarity at all.

## Files in This Folder
- `organize.py` — the final script (supports `--dry-run` and `--execute`)
- `brief.md` — the 5-part brief given to the AI
- `prompts.md` — the prompts used
- `screenshots/` — screenshots of the dry-run plan and final result
