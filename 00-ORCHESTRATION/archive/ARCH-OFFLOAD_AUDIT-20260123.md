# Offload Audit Report
## Generated: 2026-01-23

## Purpose
Audit of 04-SOURCES and 03-QUEUE directories for potential Google Drive offload to reduce repository size.

---

## 04-SOURCES Analysis

### Summary Statistics
- **Total files**: 281
- **Total size**: 9.9M
- **Largest category**: Markdown (156 files)
- **Raw transcripts**: 115 .txt files

### File Type Breakdown
| Extension | Count | Notes |
|-----------|-------|-------|
| .md | 156 | Processed sources with frontmatter |
| .txt | 115 | Raw transcripts (offload candidates) |
| .jpeg | 4 | Images |
| .csv | 3 | Reference/mapping files |
| .DS_Store | 2 | System files (should be gitignored) |

### Offload Candidates
**Raw transcripts** (115 .txt files in `04-SOURCES/raw/`):
- These are YouTube auto-generated transcripts
- Already processed into .md files in `04-SOURCES/processed/`
- Can be offloaded to Google Drive for archival
- Estimated space savings: ~3-4M

**Strategy**:
1. Upload all `04-SOURCES/raw/*.txt` to Google Drive folder "Syncrescendence/Sources/Raw-Transcripts/"
2. Create manifest CSV with filename → Google Drive link mapping
3. Delete local .txt files after verification
4. Update sources.csv to reference Google Drive URLs

### Protected Files (Keep in Repo)
- `04-SOURCES/processed/*.md` — Working processed sources (keep)
- `04-SOURCES/DYN-SOURCES.csv` — Canonical ledger (keep)
- `04-SOURCES/REF-*.csv` — Reference mappings (keep)
- `04-SOURCES/REF-CREATOR_BIOS.md` — Creator reference (keep)

---

## 03-QUEUE Analysis

### Summary Statistics
- **Total files**: 9
- **Total size**: 96K
- **Primary content**: Modal 2 visual/VFX articles

### File Breakdown
| File | Size | Type | Disposition |
|------|------|------|-------------|
| QUEUE_DISPOSITION.md | 4.8K | Meta | Keep |
| README.md | 782B | Meta | Keep |
| .DS_Store | 6.1K | System | Gitignore |
| modal2/QUEUE-36200-SCREENPLAY_ORCHESTRATION.md | 3.9K | Queue item | Process or archive |
| modal2/AI_Workflows_in_Video_and_VFX.md | 11K | Queue item | Process or archive |
| modal2/The_Next_Wave_in_AI_Video_and_VFX.md | 16K | Queue item | Process or archive |
| modal2/AI_3D_VFX.md | 9K | Queue item | Process or archive |
| modal2/Physical_AI.md | 10K | Queue item | Process or archive |
| modal2/AI_Image_Generators.md | 14K | Queue item | Process or archive |

### Offload Assessment
**Not recommended for offload**:
- Total size is only 96K (negligible)
- Active queue items need local access
- Better to process or archive than offload

**Recommendation**: Triage modal2 items:
- Strategic → Process to SOURCES
- Tactical → Archive
- Noise → Delete

---

## 05-MEMORY Analysis

### Summary Statistics
- **Total files**: 113
- **Total size**: 3.2M
- **Duplicates**: 0 (md5 verification complete)

### Offload Candidates
Archive is already compressed. No immediate offload needed.

**Future consideration**: If archive grows >10M, consider offloading:
- Pre-2025 execution logs
- Superseded directives
- Historical snapshots

---

## Offload Implementation Plan

### Phase 1: Sources Raw Transcripts (Immediate)
1. Create Google Drive folder structure:
   ```
   Syncrescendence/
   └── Sources/
       └── Raw-Transcripts/
   ```

2. Upload all .txt files from `04-SOURCES/raw/`

3. Generate manifest:
   ```csv
   filename,google_drive_url,size_bytes,upload_date
   20250926-youtube_video-dwarkesh-richard_sutton.txt,https://drive.google.com/...,12345,2026-01-23
   ```

4. Verify uploads complete

5. Delete local .txt files

6. Update .gitignore to exclude future .txt in raw/

### Phase 2: Queue Triage (Deferred)
- Requires Sovereign decision on modal2 items
- Not urgent (only 96K)

### Phase 3: Archive Management (Future)
- Monitor archive growth
- Offload when >10M or when historical items >6 months old

---

## Space Savings Estimate

| Action | Space Saved | Effort |
|--------|-------------|--------|
| Offload raw transcripts | ~3-4M | 2 hours |
| Gitignore .DS_Store | negligible | 5 minutes |
| Total immediate savings | ~4M | ~2 hours |

---

## Manifests Generated

- `/tmp/sources_manifest.tsv` — All 281 files with size and date
- `/tmp/queue_manifest.tsv` — All 9 files with size and date

These manifests can be used for upload automation and verification.

---

## Recommendations

1. **Immediate**: Offload `04-SOURCES/raw/*.txt` to Google Drive
2. **Immediate**: Add .DS_Store to .gitignore
3. **Near-term**: Triage 03-QUEUE/modal2/ items
4. **Ongoing**: Monitor 05-MEMORY growth, offload when >10M

---

## Next Actions

- [ ] Create Google Drive folder structure
- [ ] Upload raw transcripts
- [ ] Generate manifest CSV
- [ ] Verify uploads
- [ ] Delete local .txt files
- [ ] Update .gitignore
- [ ] Update sources.csv with Google Drive URLs

---

**Status**: Audit complete. Offload plan ready for execution pending Sovereign approval.
