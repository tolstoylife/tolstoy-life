# Handoff — draft the 3 held-back evidence-quote corrections

**Date:** 2026-06-07 · **Branch:** `feat/corpus-dive-skill`
**Mission:** finish the 3 evidence quotes deliberately *held back* from the note-tail / pre-reform extract backfill, because correcting them is editorial + translation work (re-derive `quoteRu`, re-translate the working-English, update the `index.md` mirror, and — for one — resolve a TEI-vs-print variance). **These are judgment calls: propose, then get Johan's nod before finalising.**

> Note on location: handoffs normally live untracked in `_generated/sessions/`. This one is committed under `docs/research/` at Johan's request so it's durable next to the dives. Move it if you prefer the convention.

---

## What already happened (don't redo)

`extract_tei.py`'s `normalise_paragraph` wiped each inline `<note>`'s `.tail` via `lxml`'s `.clear()`, silently dropping the Tolstoy prose after footnote anchors. Fix (preserve `.tail`) is already in HEAD (`docs/research/lib/extract_tei.py:55-64`). Separately, `--choice=reg` resolves pre-reform `<choice><orig>/<reg>` pairs the legacy default dropped.

A repo-wide backfill re-ran `extract_tei.py --choice=reg --notes=auto` over every committed dive extract:
- **`c527a46b`** — 229 extracts refreshed across 18 dives (verified strict supersets; all dossiers `verify_quotes` green) + a clean trivial quote fix (`christian/diary_1889`).
- **`0a057635`** — resolved `fire-metaphor/diary-1903-divine-spark` (a pre-reform `<choice>` drop of «человѣка»).

The method, classification, and the full list of refreshed / excluded / skipped files are in those two commits' messages — read them first (`git show c527a46b --stat`, `git log -1 c527a46b`).

**Why these 3 were held:** refreshing their extracts breaks `verify_quotes`, because the dossier quote itself was transcribed from the *buggy* extract — the quote straddles a dropped passage. So fixing them couples extract ↔ `quoteRu` ↔ `quoteEn` ↔ `index.md`. Their extracts are currently **left at the committed (gapped) state** so the repo stays green; nothing is broken.

---

## The 3 items

| # | dossier id | dossier row | extract (source) | index.md mirror |
|---|---|---|---|---|
| 1 | `vanderveer_1896_cannot_not_be` | `docs/research/christian/dossier.yaml:94` | `extracts/v69_102_DzhonuVanderVeruVanderVeerJohn.txt` | `christian/index.md:131` |
| 2 | `zdziechowski_1895_i_try` | `docs/research/christian/dossier.yaml:118` | `extracts/v68_159_M_E_Zdzexovskomu.txt` | `christian/index.md:122` |
| 3 | `letter-chertkov-1886` | `docs/research/fire-metaphor/dossier.yaml:820` | `extracts/v85_125_a17_18.txt` | `fire-metaphor/index.md:242` (+ Method note `:300`) |

Source XML for all three is under `primary-sources/tolstoydigital-TEI/texts/letters/<id>.xml`.

### Get the byte-exact corrected Russian (don't hand-copy)
For each, regenerate and read the corrected paragraph straight from the source — this is the canonical, byte-faithful text:
```
python3 docs/research/lib/extract_tei.py \
  primary-sources/tolstoydigital-TEI/texts/letters/<id>.xml --choice=reg --notes=auto
```

### Item 1 — vanderveer_1896 (~30 dropped words)
- Gapped quote glues `…командиру полка,³` directly to `По этому письму…`.
- The fix restores, between them: `…командиру полка,³ доставленное мне г-ном Вандейлем, я вас знаю лучше, и вы мне ближе, чем многие лица, живущие около меня, и которых я вижу каждый день. По этому письму…`
- Current `quoteEn` only translates the *latter* part ("You say in your letter…"); the restored opening (Van Dyle/Вандейль delivering the letter) is untranslated.
- **Decision:** include the restored passage (and translate it) **or** mark it `[…]`. Then update `quoteRu`, `quoteEn`, **and** the verbatim block quote at `christian/index.md:131`.

### Item 2 — zdziechowski_1895 (a dropped sentence)
- Gapped quote opens with a stray anchor `⁹` then jumps to `В данном случае…`.
- The fix restores, between them, a full sentence: `…⁹ Но я не вижу этого. … нужно только быть христианином. В данном случае…` (get exact wording from the command above).
- Current `quoteEn` is already elided (`…`).
- **Decision:** drop the stray leading `⁹` and/or fold in the restored sentence. Update `quoteRu`, `quoteEn`, and the block quote at `christian/index.md:122`.

### Item 3 — letter-chertkov-1886 (genuine TEI-vs-print variance)
- Gapped quote: `среди тьмы теперь загораются искры. Я вижу и радуюсь.`
- Fixed **TEI** reads: `…Я их вижу и радуюсь им.`
- **Print** (PDF-collated, vol44 p.421, recorded in this dive's `needsReview`): `…Я ихъ вижу и радуюсь` → modern `Я их вижу и радуюсь` — **no «им»**.
- So TEI carries an «им» the print lacks. `quoteEn` already restored «их» ("I see them and rejoice"); «им» would add "in them".
- **Decision:** quote the TEI verbatim (`радуюсь им`, consistent with the dive's stated "verbatim against TEI" policy) **or** follow the print collation (`радуюсь`). Whichever you pick, also update the dive's apparatus that documents this entry: the `significance` note (`fire-metaphor/dossier.yaml:832-837`), the `needsReview` (2) clause (`:1471-1474`), and the Method paragraph `fire-metaphor/index.md:300`. The Tom-85 table row `fire-metaphor/index.md:242` is English-only — likely no change.

> This dive (`fire-metaphor`) has a deliberate PDF-collation apparatus that intentionally kept `quoteRu` verbatim against the *gapped* TEI and logged print readings in `needsReview`. Don't silently overwrite it — reconcile it with whatever decision is made.

---

## Guardrails
- **Byte-fidelity:** after each fix, `quoteRu` must appear verbatim in its refreshed extract. Author elisions only as bracketed `[…]`/`[...]` (honoured by the verifier).
- **Working English** stays labelled `(working English)`; minimal-editorial voice; foreign titles verbatim. See memory `feedback_voice_target`, `feedback_ingestion_accuracy_both_directions`.
- **Ground in primary, not mainstream** (memory `corpus-dive-ground-in-primary-not-mainstream`).
- Keep edits to these 3 rows + their mirrors; don't touch the 229 already-backfilled extracts.

## Verify, then commit
```
python3 docs/research/lib/verify_quotes.py docs/research/christian/dossier.yaml
python3 docs/research/lib/verify_quotes.py docs/research/fire-metaphor/dossier.yaml
```
Both must end `PASS`. Re-run `python3 docs/serve.py --build-only` only if any `index.md` changed (regenerates the git-ignored `.html`). Commit the touched extracts + dossier + index.md together; **do not push** — Johan pushes himself (memory `reference_push_command_sequence`).

## Suggested skills for the next session
- **`corpus-dive`** — owns the extraction recipe (`--choice=reg`), the dive voice, and the verify gate.
- Escalate the two translations + the «им» variance to Johan (editorial judgment); these are not mechanical.
