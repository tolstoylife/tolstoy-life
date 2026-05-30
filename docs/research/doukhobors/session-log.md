# Doukhobors dive — session log

Append-only record of what each session covered. The resume queue is the dossier's `notCovered`
and `needsReview` lists.

## 2026-05-26 — original survey (pre-corpus-dive)
Hand-written survey `index.md` in the copyright-renunciation companion style: the full
Tolstoy–Doukhobor arc with byte-faithful RU quotes + working EN, letters/diaries/works cluster
tables, the Biryukov-biography treatment, and a primary-vs-conventional section. No machine-readable
dossier, no visual record, no dev-blog note (these predate the corpus-dive skill). The Biryukov
Vol. III (and later Vol. IV) Russian capture + English translation live under `biryukov-vol3/`,
`biryukov-vol4/`.

## 2026-05-30 — structured corpus-dive re-run (this session)
Revisited the dive to add the three coordinated corpus-dive outputs the original lacked, per the
confirmed Phase-0 contract: **full relationship, state/authorities handling foregrounded, heavy
visuals; post-1880, all genres; fan-out sweep.**

Added / produced:
- **`dossier.yaml`** — 13 evidence rows (all byte-faithful, re-read from `extracts/` this session),
  18 entities (vaultStatus checked against `website/src/wiki` + `website/src/works`), 26 visuals
  (rights logged), 5 scholarship triangulations, contradictions/notCovered/needsReview/archives.
- **Visual sweep** — 55 images cached to the git-ignored `visuals/` (Commons 30 + Canada 25;
  Russian-museum channel returned nothing reachable headless). Rights gate confirmed
  (`git check-ignore` passes). Keystone facsimile rendered to `extracts/v39_209_215_p209_facsimile.png`
  (PD; PDF page 252 of local vol08).
- **`index.md`** — left the 2026-05-26 narrative + quotes intact; added §2.8 "How the state handled
  it" (new byte-faithful quotes: the three-ways passage v71_081, the state-weapons inventory v31,
  the "let us go" petition v71_107, the four-demands draft v72_426), expanded §7 into
  "Visual & manuscript record" with ~20 embedded figures, and added dossier/note pointers.
- **Draft note** — `website/src/posts/notes/2026-05-30-doukhobors.md` (`draft: true`).
- Regenerated `index.html` via `docs/serve.py --build-only` (exit 0).

Verification: an independent opus verifier pass was dispatched (byte-fidelity sample, rights gate,
vaultStatus, scholarship attribution, voice).

### Resume queue (next sessions)
- Tom 31 → local PDF unresolved (pss-volume-mapping TODO): byte-fidelity PDF cross-check for
  *Two Wars* and *К итальянцам* still deferred.
- 1900 letter to Nicholas II (Tom 72, letter 426): TEI lacunose; verify final-text wording against
  printed vol36 (the quoted four-demands span is from the legible pre-reform first-redaction draft).
- Russian-museum visual channel (GMT/KAMIS, Goskatalog): not reachable headless — manuscript
  facsimiles + Russian-held portraits (Verigin in exile, the Caucasus persecution) remain a
  rights-request item.
- Confirm rights on the BC-Archives/doukhobor.org images (Cyprus, the two ships, rail/quarantine)
  before any move to `website/src/`.
- The ~538 letters in full (esp. ~116 to Chertkov, Toms 85–89) — sampled, not read through.
- Wiki ingestion of the entity work-order (separate, human-in-the-loop step).
