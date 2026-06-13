# Run report — 1908-a-letter-to-a-hindu

**Dive:** A Letter to a Hindu (Письмо к индусу), Tolstoy's 1908 open letter to Tarak Nath Das. Work-subject dive, interactive (not `--auto`), not `--novel`. Record-creating workRecord.
**Date:** 2026-06-13. **Effective model:** Opus (main loop); sonnet sub-agents (scholarship, visuals); opus verifier.
**Gates:** `extract_tei.py --choice=reg --notes=auto`; `verify_quotes.py` → **29/29 PASS, exit 0**; separate-pass verifier (`_verifier-report.md`).

## Scope contract (as run)

- **Question:** the letter's genesis, its argument (India held captive by Indian consent to violence; non-resistance as the lever of liberation), and the Gandhi-centred reception. Marquee tested as a hypothesis.
- **Corpus surface:** the letter (works/v37, PSS Tom 37) + the «История писания» commentary (comments/v37_444_446) + 1908 diaries (Tom 56) + Tolstoy→Gandhi letters (Toms 80/81/82) + the Chitale letter (Tom 78). Companion cluster located but not dived: Letter to a Chinese (Tom 36, 1906), Address to the Chinese People (Tom 34, 1900).
- **Keyword anchors:** индус / Письмо к индусу / Das / Gandhi / Chitale / Bharati / Вивекананда / непротивление / Трансвааль.
- **Stop condition:** the letter's own argument fully read; genesis chronology witnessed; the three Gandhi letters extracted; scholarship triangulated. Met.

## Coverage ledger

| Surface | Status |
|---|---|
| Genesis & composition | covered |
| What the work says | covered |
| The people around the work | covered |
| Redactions & textual history | partial (aggregate only; 29 variants not collated) |
| Publication, censorship & translation | covered |
| Reception — the Gandhi story | covered |
| Reception — Russian society & church | partial (little reaction; not padded) |
| Place in the cluster | covered |
| The author's later verdict | covered |
| Visual & manuscript record | covered (no MS facsimile openly available) |

## Entity work-order (for the separate LLM wiki-ingestion step — this dive writes no vault pages)

**Priority 1 (central):**
- `Mohandas Gandhi` (person) — MISSING. The reception; 3 Tolstoy letters + the *Indian Opinion* reprint.
- `Tarak Nath Das` (person) — MISSING. The addressee; the rejection ("Open Letter," 16 Oct 1909). Correct the PSS garbling (Tarak Nath Das, not "Tarakuatta Das"; *Free Hindustan*).
- `A Letter to a Hindu` (work) — MISSING. Depends on Gandhi + Das pages. See workRecord below.

**Priority 2 (supporting):**
- `Vladimir Chertkov` (person) — EXISTS (`wiki/Vladimir Chertkov.md`). Add the translation role.
- `Baba Premananda Bharati` (person) — MISSING. Source of the Krishna epigraphs *and* a named target.
- `Non-resistance` (concept) — STUB. The colonial application of the doctrine.

**Priority 3 (peripheral):** `Swami Vivekananda`, `Dushan Makovitsky`, `Nikolai Gusev`, `Albert Škarvan` (all persons, MISSING); `Free Hindustan` (concept/reference, MISSING). Confirm vault transliterations before creating (gotcha).

## Work-record work-order (proposed fills for a NEW `works/` record; human applies)

Target: `website/src/works/non-fiction/essays-and-criticism/a-letter-to-a-hindu/A Letter to a Hindu.md` (does not exist yet).
- **High confidence:** titleEn/titleRu, titleAlternatives (Hindoo / Brief an einen Hindu), mainCategory Non-Fiction, language ru, completionStatus complete, publishedDuringLifetime true, dateWritingStarted 1908-06-20 (OS 06-07), dateWritingCompleted 1908-12-27 (OS 12-14), firstPublishedVenue (Kievskie Vesti / Russkie Vedomosti), epigraph/epigraphAuthor, themes, samizdatCirculation true, jubileeEdition vol 37.
- **Medium confidence:** subcategory "Essays and Criticism", genre essay, publishedInRussiaDuringLifetime true (excerpts 1909; full text 1911 — nuance), dateFirstPublished 1909-05-02 (OS 04-19), relatedWorks (kingdom-of-god = source [live record]; law-of-violence / letter-to-a-chinese / address-to-chinese-people = companion [forward refs]), bans [] (no formal ban found).

## notCovered / needsReview (resume queue)

See `dossier.yaml` (`notCovered`, `needsReview`). Headlines: individual redaction collation; Das's rebuttals as primary texts (SAADA, not in corpus); Krishna-epigraph page-collation against Bharati 1904; exact English-text page range in PSS Tom 37; whether a Free Age Press English printing preceded *Indian Opinion*; vault transliterations.

## Visuals work-order

6 PD/CC images cached in the git-ignored `visuals/` (Tolstoy 1908; Gandhi 1906; Das 1937; Chertkov ×2; *Indian Opinion* press). To acquire/request: a manuscript or first-edition facsimile (GTM, Moscow); a period *Indian Opinion* masthead/page scan (National Library of South Africa / Gandhi Heritage Portal). The *Indian Opinion* press image is CC-BY-SA (attribution required if ever published).

## Self-assessment (interactive — recorded for parity with --auto)

- Interlocutor sweep yielded people: **yes** (Das, Gandhi, Chitale, Bharati, Vivekananda, Chertkov, Makovitsky, Gusev, Škarvan).
- Russian society/church reception: **honestly partial** (the letter drew little; not padded).
- workRecord fill accurate/provenanced: **yes** (every field evidence-anchored; nuances flagged).
- Coverage honest: **yes** (two `partial`s are real, not disguised gaps).
- `--choice=reg` extracted cleanly: **yes**.
- Spine stayed bare: **yes** (contested labels attributed to the outside, linked to sibling dives).

## Outputs

`index.md` (+ generated `index.html`), `dossier.yaml`, `extracts/*.txt` (+ `_scholarship.md`), `session-log.md`, draft note `website/src/posts/notes/2026-06-13-a-letter-to-a-hindu.md`. Committed, not pushed. Wiki ingestion is a separate human-in-the-loop step — the dossier is the pointer, not the writer.
