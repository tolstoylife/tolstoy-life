# Handoff — scope & run a corpus work-dive: **What Is Art?** (Что такое искусство?)

**For:** a fresh Claude session on the Tolstoy Research Platform (`/Volumes/Graugear/Tolstoy`).
**Goal:** run a **single-work corpus dive** on Tolstoy's aesthetics treatise *What Is Art?* — a Prophet-period treatise with no dedicated dive yet (the [Prophet-period work-dive programme](../../docs/research/) has done Confession, Examination of Dogmatic Theology, What I Believe, What Then Must We Do?, On Life, The Kingdom of God — this fills the biggest remaining gap after the Gospels).
**Skill to use:** `corpus-dive` — run `/corpus-dive What Is Art?` (or `--auto` to run unattended). The skill owns the whole pipeline (Phase 0 scope → sweep → extract → dossier → synthesize → verify → handoff); read its SKILL at `.claude/skills/corpus-dive/SKILL.md` first. This is a **work dive**, so the `workRecord:` block + the standing spine sections apply. Hard gate before the verifier: `python3 docs/research/lib/verify_quotes.py docs/research/<slug>/dossier.yaml` must exit 0.

---

## 1. Slug, window, and the one boundary that matters

- **Proposed slug:** `1897-1898-what-is-art` (the treatise dates itself «1897—1898»). Long gestation though — art notes from ~1882, an 1889 draft «Об искусстве», the 1894 Maupassant preface, the 1896 «О том, что называют искусством». If you fold those in as composition, use `1896-1898-what-is-art`. Confirm the window in Phase 0 from the works record + the Tom 30 textual-history commentary (below).
- **This is NOT the [tolstoy-in-art](../../docs/research/tolstoy-in-art/) dive.** That one is the *visual record* — portraits/paintings/sculpture **of** Tolstoy and his circle (Repin, Ge, Kramskoy, the Orlov peasant album). *What Is Art?* is Tolstoy's *aesthetic theory* — the definition of art, the rejection of "beauty", the infection theory. The only overlap is that the treatise extract `v30_027_203` was quoted in tolstoy-in-art to source Tolstoy's opinions of specific artists/Wagner/the Decadents; the **theory itself is unexamined there**. Own the theory here; cross-link tolstoy-in-art only for the visual-circle people. Don't re-do its visual sweep.

## 2. Where the work lives in the corpus — Tom 30 (a whole cluster)

All under `primary-sources/tolstoydigital-TEI/texts/`. Extract with `extract_tei.py <xml> --choice=reg --notes=auto` (pre-1918 text — `--choice=reg` mandatory). Read the treatise **structurally**, chapter by chapter, not just by grep (work-dive rule).

**The work + its prefaces (`works/`):**
- `works/v30_027_203_Chto_takoe_iskusstvo.xml` — the treatise. **20 chapters (I–XX) + Прибавления.**
- `works/v30_204_206_Predislovie_k_anglijskomu_izdaniju_traktata_Chto_takoe_iskusstvo.xml` — **the preface Johan flagged** (see §4). The famous one.
- `works/v30_003_024_Predislovie_k_sochinenijam_Gjui_de_Mopassana.xml` — the 1894 Maupassant preface, the aesthetic precursor (sincerity; the author's moral relation to subject).

**The long gestation — precursor art-essays (the "Redactions & textual history" gold, `works/`):**
- `v30_213_215_Ob_iskusstve...`, `v30_216_225_O_tom_chto_est_i_chto_ne_est_iskusstvo...`, `v30_226_230_Ob_iskusstve_V_mire_tak_nazyvaemyh...`, `v30_231_239_Nauka_i_iskusstvo`, `v30_240_242_O_nauke_i_iskusstve`, `v30_243_270_O_tom_chto_nazyvajut_iskusstvom` (1896).
- Variants: `v30_303_426_Chto_takoe_iskusstvo_Varianty`, `v30_273_302_..._Mopassana_Varianty`, and the per-essay `*_Varianty` files.

**Editorial textual-history commentary (`comments/` — the genesis + censorship narrative, treat as secondary/editorial, attribute):**
- `comments/v30_509_555_Istorija_pisanija_i_pechatanija_statej_ob_iskusstve...` — history of writing & printing the art articles.
- `comments/v30_487_504_Istorija_pisanija_i_pechatanija_Predislo...`, `comments/v30_555_570_..._Opisanie_rukopisej` (MS description), `comments/v30_571_582_Tekstologicheskie_kommentarii`.

PSS print for facsimile/collation: locate the Tom 30 PDF via `docs/research/pss-volume-mapping.md` (render the single keystone page at 220 dpi into `extracts/`; note the gap in `needsReview` if the PDF isn't held).

## 3. The special structure Johan wants — a concept/philosopher juxtaposition

The treatise's spine (Chs III–V especially) is a **survey-and-demolition of Western aesthetics**: Tolstoy catalogues ~70 definitions of beauty/art to reject «красота» (beauty) as the criterion, then offers his own — **art = the "infection" (заражение) / transmission of feeling; good art unites people in the highest religious consciousness of the age; the rest are "counterfeits".**

Confirmed cast present in the treatise (raw counts): **Вагнер 33, Кант 37, Баумгартен 15, Бодлер 14, Шеллинг 11, Шопенгауэр 7, Гюйо 6, Спенсер 5, Ницше 4, Дарвин 4, Тэн 3, Гартман 3, Верон 3, Гельмгольц 2, Кузен, Гегель.** (Baumgarten coined "aesthetics"; Wagner & Baudelaire are the bad-art exhibits; Kant/Schopenhauer/Hegel the beauty-metaphysicians.)

**Build a dedicated standing section — "Mainstream aesthetics vs Tolstoy: the concept/philosopher map"** — as a table: each thinker/concept → **the received reading** (mainstream/scholarly, attributed) → **Tolstoy's reading and verdict** (his own words, cited verbatim from Chs III–V). The value is the *juxtaposition*: show where Tolstoy summarises a philosopher faithfully vs where he flattens/caricatures them (e.g. Kant on disinterested beauty, Schopenhauer, Guyau's "art as expansion of life"). Concepts to track: красота/beauty, заражение/infection, the religious consciousness criterion, sincerity, "counterfeits of art" (borrowing, imitation, strikingness, interest), the kinds of feeling united vs divided. This is more central than the usual Phase-3 "Scholarly context" divergence map — make it a first-class spine section, but keep the voice rule: **primary (Tolstoy's own catalogue) leads; mainstream is the attributed foil**, never asserted as the baseline he "confirms".

## 4. The preface — a keystone

`v30_204_206` (preface to the English edition) is the dive's likely keystone. In it Tolstoy says the book "comes out for the first time in its true form" — every Russian edition was «изуродован цензурою» (mangled by the censor). The story: he gave it to N. Ya. Grot for «Вопросы философии и психологии»; Grot softened it (replaced «всегда»→«иногда», «все»→«некоторые», «церковное»→«католическое», «богородица»→«мадонна», «патриотизм»→«лжепатриотизм», «дворцы»→«палаты»); then the **spiritual censor** cut whole sentences and inserted the redemption dogma Tolstoy rejected (changed Christ dying "for the truth he professed" → "for the human race"). He tells the whole episode as proof that **any compromise with an institution against your conscience drags you into its harm.** This anchors both the *Publication/censorship/translation* section and the censorship-as-theme thread; quote it verbatim. (Note: the work's own internal preface, if separate from this English-edition one, is also worth a structural read.)

## 5. Genesis & composition + the people (work-dive witness sweep)

Composition window ~1896–1898 (concentrated 1897). Sweep the window's **diaries and letters** for (a) Tolstoy's own genesis/strain while writing, (b) the people around the work — each surfaced as a `person` entity with `ingestionPriority`. Resolve exact Toms via `docs/research/pss-volume-mapping.md`; expect **letters Tom 69 (1896) – Tom 71 (1898)** and **diaries Tom 53 (1895–1899)** — verify, don't assume.

Likely interlocutors to chase (the dive discovers; these are leads):
- **Aylmer Maude** — translator of the first complete (English) edition; visited Yasnaya Polyana; later biographer. Central to the publication + the English preface.
- **N. Ya. Grot (Николай Грот)** — editor of «Вопросы философии и психологии»; the compromise/censorship story names him.
- **V. V. Stasov (Владимир Стасов)** — critic who supplied Tolstoy with the aesthetics bibliography he demolishes; a key research helper for the survey chapters.
- **S. I. Taneyev (Сергей Танеев)** — composer at Yasnaya Polyana 1895–96; the music-as-art question (Beethoven/Wagner), entangled with the Sofia/Taneyev domestic tension.
- **V. G. Chertkov** — the abroad-publishing channel. **N. N. Strakhov** — earlier art/philosophy exchange (d. Jan 1896).

## 6. Standing work-dive sections (evidence-scaled; drop+log any the corpus can't support)

- **Genesis & composition** (§5) — incl. the people.
- **What the work says** — structural map of the keystone passages (the infection theory; the beauty critique; good vs bad art; the religious criterion; the verdicts on Wagner/Beethoven/Shakespeare/the Decadents; Tolstoy condemning his own earlier art).
- **Mainstream aesthetics vs Tolstoy** (§3) — the concept/philosopher juxtaposition.
- **Redactions & textual history** — the long gestation (§2 precursors + variants); what each redaction added.
- **Publication, censorship & translation** — the Grot/spiritual-censor mangling (§4); first complete text = Maude's English (1898); the Russian censored serial in «Вопросы философии и психологии» 1898; later legal Russian printing. **Correct the works-record stub** (it currently says `publishedInRussiaDuringLifetime: false`, which the censored 1898 serial appears to contradict — verify and fix in the `workRecord` proposal).
- **Reception & afterlife — Russian society & church first** — the aesthetic establishment's reaction (Stasov et al.), then the international reception (it became Tolstoy's most-read aesthetics text in the West via Maude).
- **Place in the cluster** — cross-link siblings via the rendered `.html`: [tolstoy-in-art](../../docs/research/tolstoy-in-art/index.html) (visual record), [fire-metaphor](../../docs/research/fire-metaphor/index.html) (art-as-transmission of religious feeling overlaps the infection theory), [What I Believe](../../docs/research/1882-1884-what-i-believe/) (the religious consciousness that grounds "good art").
- **The author's later verdict** — Tolstoy's own later judgments on the book.

## 7. workRecord (fill the stub)

Record: `website/src/works/non-fiction/essays-and-criticism/what-is-art/What Is Art?.md` — **exists but is an empty stub** (all date/venue fields `""`). The dive's `workRecord:` block can propose fills for: `dateWritingStarted/Completed` (+ OldStyle/Approximate sub-flags), `dateFirstPublished` + venue, `dateFirstPublishedInRussia` + venue, `publishedDuringLifetime`/`publishedInRussiaDuringLifetime` (re-check — likely both true, via Maude EN + the censored 1898 serial), `titleAlternatives`, `bans`/censorship, `relatedWorks`. Shape list-typed fields to `tolstoy-works-schema.md`; the dive **proposes**, ingestion applies (no `works/` write).

## 8. Mechanics & guardrails

- **Extraction:** `python3 docs/research/lib/extract_tei.py <xml> --choice=reg --notes=auto` → `docs/research/<slug>/extracts/<tei-id>.txt`. (The note-tail bug is fixed in HEAD; the whole corpus was backfilled 2026-06-07.)
- **Verify gate:** `verify_quotes.py docs/research/<slug>/dossier.yaml` exits 0 before the human-judgment verifier.
- **Voice:** simple/factual, minimal editorial; working-English translations labelled `(working English)`; foreign titles verbatim; attribute mainstream, don't assert (memories `feedback_voice_target`, `corpus-dive-ground-in-primary-not-mainstream`, `feedback_ingestion_accuracy_both_directions`).
- **Hard boundaries:** WRITE only under `docs/research/<slug>/` (+ the draft note `website/src/posts/notes/`); never touch `primary-sources/**` or the vault (`website/src/wiki|works/**`). The dive plans pages; it never creates them.
- **Render:** `python3 docs/serve.py --build-only` after `index.md` is final (HTML is git-ignored).
- **Don't push** — Johan pushes himself (memory `reference_push_command_sequence`).

## 9. Definition of done

`docs/research/<slug>/` with: `index.md` (+ rendered `index.html`), `dossier.yaml` (evidence + entities + the concept/philosopher juxtaposition in scholarship/triangulation + workRecord + coverage), `extracts/`, a `draft:true` dev-blog note, a clean `verify_quotes` pass, and a clean verifier verdict. Then Phase-6 research handoff + Phase-7 session handoff.

---
*Created 2026-06-07 after the note-tail/pre-reform extract backfill. Companion: [docs/research/_handoff-held-quote-corrections-2026-06-07.md](../../docs/research/_handoff-held-quote-corrections-2026-06-07.md) (unrelated open task).*
