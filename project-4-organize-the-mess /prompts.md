# Prompts Used — Organize the Mess

## Step 1 — Backup (done manually, before any AI involvement)
```
cp -r Downloads Downloads-backup
diff -r Downloads Downloads-backup   # confirm identical
```

## Step 2 — The Brief (see brief.md)
Given to the AI as plain language, no technical terms:
> "Clean up my Downloads folder: find true duplicate files (by content, not
> just name), flag anything unusually large for me to review, and group
> everything else into Documents / Images / Installers / Archives folders.
> Never touch my backup folder. Never delete anything — move duplicates
> into a _duplicates folder instead so I can review them myself."

## Step 3 — Demand the dry run (critical safety prompt)
> "Do NOT change anything yet. Show me your full plan first — every file
> you would move, old location -> new location — and wait for my approval
> before touching anything."

## Step 4 — Plan review (where the real catch happened)
While reading the returned plan, I noticed the large file
(`big_video_render.mp4`) was listed as being moved into a type folder, even
though my brief said large files should only be flagged, not moved. I sent:
> "This contradicts the brief — large files should be flagged for review,
> not moved automatically. Fix this and show me the corrected plan."

## Step 5 — Approval
> "This plan looks correct now. Go ahead and execute it exactly as shown."

## Step 6 — Verification
> "Confirm the backup folder is untouched (same file count as before), and
> show me the new folder structure."

## Result
The corrected plan executed cleanly on the first attempt after the fix: 15
files sorted, 4 true duplicates safely quarantined (not deleted), 1 large
file correctly left in place and flagged, and the backup folder verified
untouched (16 files, identical to before).
