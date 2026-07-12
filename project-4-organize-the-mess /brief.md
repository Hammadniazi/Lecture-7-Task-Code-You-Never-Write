# Brief: Organize the Mess — Downloads Folder Cleanup

## Goal
Clean up my cluttered Downloads folder: find true duplicate files, flag
oversized files worth reviewing, and group everything else by type — safely,
without risking any real data loss.

## Input
The Downloads folder, containing roughly 16 files: documents, images,
installers, archives, and one large video file. A backup copy
(Downloads-backup) already exists and must never be modified.

## Output
1. A full plan of every proposed operation (old location -> new location),
   shown BEFORE any file is touched.
2. After approval only: files grouped into subfolders by type (Documents,
   Images, Installers, Archives, Other).
3. True duplicates (identical content, regardless of filename) moved into a
   Downloads/_duplicates folder — never deleted.
4. Any file over a defined size threshold flagged in a separate report,
   not moved automatically.

## Rules
- Never read from or write to Downloads-backup under any circumstances.
- Never delete any file. Only move files within Downloads (or into
  Downloads/_duplicates).
- "Duplicate" means identical file content (verified by content, not just
  matching filenames — e.g. "resume_v2.docx.txt" and
  "resume_v2 (1).docx.txt" count if their contents match).
- Files over 4 MB are flagged as "large, review before keeping" (a stand-in
  for the real-world 100 MB threshold, scaled down for this demo).

## Edge cases
- If a file can't be read (permissions, in use, etc.), skip it and list it
  separately rather than failing the whole run.
- If two files have the same name but DIFFERENT content, they are NOT
  duplicates — keep both, grouped normally by type.
- Do nothing destructive until the dry-run plan has been explicitly
  approved.
