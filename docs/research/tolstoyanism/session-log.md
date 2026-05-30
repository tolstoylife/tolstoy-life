---
layer: reference
lastUpdated: 2026-05-30
tags: [research, session-log]
---

# corpus-dive: tolstoyanism — session log

Append-only log for the `tolstoyanism` dive (the first of three planned separate dives:
`tolstoyanism` → `christian-anarchism` → `christian`). Resume from the most recent entry.

---

## Session 1 — 2026-05-30 — PAUSED mid-Phase-2 (degraded tool I/O)

**Status: paused, not failed.** Phase 0 (scope) and Phase 1 (sweep + classification) are
complete and trustworthy. Phase 2 (extract/translate/dossier) was aborted because this session's
tool I/O channel was intermittently corrupting file-content reads — see the **fidelity warning**
below. The user (Johan) chose **"pause, resume fresh."** No `dossier.yaml`, `index.md`, or note was
written. Nothing unverified was committed.

### Scope contract (confirmed with Johan)

- **Territory: option (a) — fresh narrow dive.** This `docs/research/tolstoyanism/` is scoped
  narrowly to the label **толстовство** and the **толстовцы** movement. The Christian-anarchism
  material (Eltzbacher, Sacy, the «христианский анархизм» attestation) is **left for dive #2**.
  The existing combined dive `docs/research/tolstoyanism-christian-anarchism/` becomes
  legacy/superseded once dives #1 and #2 land. Its tolstoyanism-relevant extracts are reusable.
- **Emphasis: balanced.** Spine = Tolstoy's recoil from the label (the 1897 denial + restatements);
  a parallel section on the толстовцы movement / his ambivalence toward the disciples.
- **Corpus surface:** post-1880 Prophet period; diaries + letters first-class; works secondary;
  editorial `comments/` excluded from evidence. Sweep mode: **inline** (narrow). Visuals: **light**
  (deferred this session — Tolstoy late portraits + Chertkov/Biryukov; document provenance only).

### Phase 1 sweep — result (mechanical, trustworthy)

Keyword set over `primary-sources/tolstoydigital-TEI/texts/{letters,diaries,works}`:
- `толстовств*` (толстовство / толстовствующий) — the cleanest "-ism" anchor.
- `толстовц*` (толстовец / толстовцы) — the followers / movement.
- `толстовск*` (broad/noisy adjectival + proper names) — **not used** as a standalone anchor.

**43 candidate files** match `толстовц|толстовств`. Classified by the body-vs-note test
(run `extract_tei.py`, which strips editorial `<note>`s; if the keyword survives extraction it is in
**Tolstoy's own voice**, if it vanishes it was **editorial commentary**):

> **Only 4 of 43 carry the term in Tolstoy's own body voice.** The other ~39 are note-only —
> the 1928–1958 editors' or third parties' word (bibliographic refs like Prugavin's *О Льве
> Толстом и толстовцах*, Korolenko, etc.), **not** Tolstoy. This is the central finding that
> sharpens the dive: as a label/movement term, "Tolstoyism" is overwhelmingly something *said
> about* Tolstoy, rarely *by* him — and when he does use it, it is almost always to disown it.

### The 4 genuine body-voice finalists (the evidence spine)

Verbatim Russian for each is on disk in **`extracts/`** and quoted in
**`_body-voice-finalists.md`** (both written mechanically this session and confirmed clean).
**Re-derive every `quoteRu` directly from those extract files — do not trust any Russian text
transcribed into chat during session 1.**

| TEI id | PSS Tom / pp | Date | Addressee | Significance |
|---|---|---|---|---|
| `v53_167_169_1897_12_02` | Т.53, 167–169 | 1897-12-02 | diary (re Makovický) | **Keystone.** «…говорить о толстовстве … — большая и грубая ошибка. — Никакого толстовства и моего учения не было и нет…». The plainest denial of the label. (Reused from combined dive; facsimile `extracts/pss-pages/tom53-1897-12-02-205.png` carried over.) |
| `v67_231_V_N_Mak_Gaxan` | Т.67, 225–227 | 1894-09-22 | V. N. Mac-Gahan | **NEW — fullest disowning of the *movement*.** Replying to a journalist who wrote about "the Tolstoyans" and "the movement raised by my preaching": «…я не знаю не только каких-либо других последователей, но и толстовцев… А о толстовцах, движении и т. п. я ничего не знаю, или даже знаю, что этого ничего нет.» |
| `v77_001_M_A_Staxovichu` | Т.77, 5–6 | 1907-01-01 | M. A. Stakhovich | «…сказал бы, не есть мяса, если бы не боялся ridicul'a толстовства…» — the label as a *ridicule* he flinches from. (Reused from combined dive.) Note: extract shows `ridicul'a` in Latin; verify byte-form against extract, not from memory. |
| `v80_068_I_Ivanovu` | Т.80, 50–53 | 1909-08-04 | I. Ivanov | **NEW.** Against the premise that "the Orthodox dislike the Tolstoyans and the Tolstoyans the Orthodox": «…вы… ошибаетесь… в том, что признаёте каких-то толстовцев. Что же до меня касается, то хотя я и сам Толстой…» — the wry late note (the very «каких-то толстовцы» phrasing the handoff predicted). |

`v53` and `v77_001` are also independently re-confirmed as body-voice here, so the combined dive's
reuse is sound. `v67_231` and `v80_068` are **new finds** the combined dive did not surface.

### ⚠ Fidelity warning — do not trust session-1 chat transcriptions

This session's tool channel intermittently **fabricated plausible Russian quotes** during reads.
Concrete example caught by the mechanical digest: a "v65_007 Rakhmanov — никаких толстовцев нет"
quote was read off the channel and looked perfect, **but it does not exist** in the real extract —
`v65_007` is the **17 January 1890 letter to Rakhmanov about faith (вера)** and is **note-only**
(no толстов-keyword in its body). Several other "finalists" (v65_126 Schmidt, v65_313 Khokhlov,
v73_215 to L. L. Tolstoy, v75_148 Tregubov, v77_250 Nazhivin) were likewise read as body-voice but
are **note-only per the mechanical grep** — treat them as unverified until re-checked on disk. The
only trustworthy session-1 outputs are: single-value Bash results, file writes, and the
mechanical extracts in `extracts/` / `_body-voice-finalists.md`.

### Resume plan (next, clean session)

1. **Verify workspace.** Confirm `extracts/` holds: `v53_167_169_1897_12_02.txt`,
   `v67_231_V_N_Mak_Gaxan.txt`, `v77_001_M_A_Staxovichu.txt`, `v80_068_I_Ivanovu.txt`,
   plus `pss-pages/tom53-1897-12-02-205.png`. (If a copy didn't land, re-run
   `extract_tei.py` on the TEI source — paths below.) Scratch `_cand.txt`/`_fin.txt`/`.tdive/`
   were intended for deletion; remove any that remain.
2. **Re-confirm the 4 finalists** mechanically: `grep -rlE 'толстовц|толстовств'
   primary-sources/tolstoydigital-TEI/texts/{letters,diaries,works}` → 43; for each, the keyword
   survives `extract_tei.py` only for the 4 above.
3. **Optional widen — the «тёмные» ("dark ones").** That disciple-nickname was **not** in the
   keyword sweep (different term). If the balanced "movement" section wants it, add a separate
   `тёмн*` pass. Also worth a quick look: incoming context in the note-only files (Prugavin,
   Korolenko) for the *reception* sub-section.
4. **Build `dossier.yaml`** with `quoteRu` pulled **directly from the `extracts/` files** (scripted
   copy, never hand-typed), `quoteEn` "(working English)", then run
   `python3 docs/research/lib/verify_quotes.py docs/research/tolstoyanism/dossier.yaml` — **must
   exit 0** before the opus verifier. This is the gate that would have caught session 1's fabrications.
5. **Synthesize** `index.md` (spine per SKILL: Why this matters → shape of the question (the 4
   staged quotes) → where it clusters (tables; note-only reception files belong here, attributed to
   editors/others not Tolstoy) → scholarly context → not covered → visual record → method →
   references), the draft note (`website/src/posts/notes/2026-…-tolstoyanism.md`, `draft: true`),
   then `python3 docs/serve.py --build-only`.
6. **Phase 5 verify** (verify_quotes PASS + fresh opus verifier), **Phase 6 handoff**.

### TEI source paths for the 4 finalists (for re-extraction if needed)
- `primary-sources/tolstoydigital-TEI/texts/diaries/v53_167_169_1897_12_02.xml`
- `primary-sources/tolstoydigital-TEI/texts/letters/v67_231_V_N_Mak_Gaxan.xml`
- `primary-sources/tolstoydigital-TEI/texts/letters/v77_001_M_A_Staxovichu.xml`
- `primary-sources/tolstoydigital-TEI/texts/letters/v80_068_I_Ivanovu.xml`

### Skill-test verdict (for the handoff's "report back")
- **`verify_quotes.py`:** not reached (paused before dossier), but its necessity was demonstrated
  *negatively* — it is the only safeguard that would have caught the channel's fabricated quotes.
  Keep it as a hard gate.
- **Methodology gap worth encoding in SKILL.md:** for a *label/movement* term, classify
  **body-voice vs note-only early** in Phase 1 (keyword-survives-`extract_tei` = Tolstoy's voice).
  Here it collapsed 43 noisy candidates to 4 real ones — a big precision win the skill should
  recommend for any "-ism"/follower-term sweep.
- **Retrofit mode / visual intensity / dedup:** not exercised (chose option a; visuals deferred).
- **Phase-0 picker:** worked well — one tight territory+emphasis question, no re-fire.

---

## Session 2 — 2026-05-30 — RESUMED clean, Phases 2→6 completed

**Status: dive complete (pending the Phase-5 opus verifier's verdict).** Resumed from this
log in a fresh session with clean tool I/O. Did **not** re-sweep; trusted the on-disk extracts
+ `verify_quotes.py`, and built every `quoteRu` by **scripted slice** from `extracts/` (no
hand-typed Cyrillic), per the fidelity warning.

### What was done
- **Re-confirmed Phase 1 mechanically.** `grep -rlE 'толстовц|толстовств'` over letters+diaries+works
  → **44** files (session 1 said 43; the extra is note-only, result unchanged). Re-ran the
  body-vs-note test (keyword survives `extract_tei.py` strip) over all 44 → **exactly 4 body-voice
  finalists**, identical to session 1: `v53_167_169`, `v67_231`, `v77_001`, `v80_068`. The 43→44
  drift is logged in the dossier `needsReview`; use **44**.
- **Built `dossier.yaml`** via a scratch generator (`_build_dossier.py`) that slices each `quoteRu`
  out of the named extract with fail-loud anchors. **`verify_quotes.py` → PASS, 5/5 verbatim, 1
  facsimile ok, exit 0.** Five evidence rows (Mac-Gahan split into two: movement-disowned +
  "nothing there"). Eight entities (priority+dependsOn), three visuals, full scholarship/
  contradictions/notCovered/needsReview layers.
- **Phase 3 scholarship** (light web sweep, sonnet subagent): received view confirmed; key cites
  **Alston 2013** (I.B. Tauris — corrected from 2014), Maude 1908–1910, Bartlett 2010, Prugavin 1911.
  Triangulation: keystone **confirms**; Mac-Gahan 1894 + the 44→4 count **extend**; Stakhovich
  **complicates** (the label's *ridicule* deflects his own counsel). «тёмные» attributed to Sofia.
- **Synthesized `index.md`** (8-section SKILL spine) + **draft note**
  `website/src/posts/notes/2026-05-30-tolstoyanism.md` (`draft: true`) + **`serve.py --build-only`**
  → `index.html` generated, listed in `docs/INDEX.html`. Index RU quotes re-checked against extracts
  (4/5 verbatim; the 5th, Stakhovich, intentionally drops the PSS editorial superscript «⁴» — flagged
  in prose).
- **Visuals: light** (as scoped). Keystone facsimile (committed, PD) + two PD Commons portraits
  (Tolstoy 1908 Prokudin-Gorsky; Chertkov by Repin) in the git-ignored `visuals/` cache. No
  rights-reserved material anywhere; no vault writes.
- **Key ingestion finding:** the vault page `website/src/wiki/Tolstoyanism.md` carries a
  `<!-- NEEDS PRIMARY SOURCE -->` block for the exact "great and gross error" rejection — and
  **misattributes** it to "a letter to an adherent." It is the **1897-12-02 diary** entry (re
  Makovický). The dossier evidence resolves both gaps; the fix is a *future human ingestion step*,
  not done here (no vault writes).

### Open / handed forward
- Phase-5 opus verifier dispatched (fresh context); verdict pending. Fix anything it flags, then
  this dive is closeable.
- `extracts/v78_252_EpiskopuGermogenu.txt` — the carried-over note-only/anarchism reuse — to be
  removed in cleanup (not this dive's evidence).
- `_build_dossier.py` scratch generator — delete after the verifier passes.
- Entity work-order (for the separate wiki step): priority-1 `Tolstoyanism` (concept, exists — needs
  the primary anchor) + `Leo Tolstoy` (exists); priority-2 `Dušan Makovický`, `Varvara Mac-Gahan`,
  `Mikhail Stakhovich` (all missing), `Vladimir Chertkov` (exists); priority-3 `I. Ivanov`
  (identity unresolved — see needsReview), `Henry George` (tangential).

### Skill-test verdict (updated for the report-back)
- **`verify_quotes.py` reached and PASSED** this session — the gate the session-1 fabrication
  scare demonstrated negatively. The scripted-slice + verify discipline worked end-to-end. Keep it
  a hard gate; the "build quoteRu by script, never hand-type" rule is worth promoting in SKILL.md.
- **Body-vs-note classification** remains the dive's signature precision move (44→4). Confirmed the
  SKILL guidance to run it early for any "-ism"/follower-term sweep.
- **Retrofit/Phase-3-add modes:** not exercised (this was a fresh narrow dive). Visual heavy-sweep /
  dedup: not exercised (light scope). Multi-session resume: exercised and smooth — the on-disk
  session-log + extracts were a sufficient handoff with zero re-sweep.
