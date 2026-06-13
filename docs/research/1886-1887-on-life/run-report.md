# Run-report — `1886-1887-on-life`

Work-dive on Tolstoy's *On Life* (О жизни), the philosophical capstone of the Prophet period and the metaphysic beneath the social ethic of *What Then Must We Do?*. Run 2026-06-06, in-session unattended (the A-Confession-pilot model), medium visual intensity. Followed the handoff from the *What Then Must We Do?* session (which flagged On Life as the not-covered "philosophical successor").

## Scope contract (Phase 0)

- **Subject (work dive):** *On Life* (О жизни; working title «О жизни и смерти»; French *De la vie*; English *Life*). Slug `1886-1887-on-life` — year-prefixed, slots after `1882-1886-what-then-must-we-do`.
- **Corpus surface:** PSS Tom 26 — work «О жизни» pp. 313–442 (`v26_313_442_O_zhizni.xml`); the genesis lecture «Понятие жизни» pp. 881–885; variants pp. 578–634 and the «Неделя» 1889 last-chapters variants pp. 451–456; Chertkov's simplified «Об истинной жизни» pp. 885–926; commentary pp. 748–844. Composition-window **diaries** Tom 49 (1886–87); **letters** Tom 64 (1887–88) + Tom 63 tail. Composition window **1886–1887** (genesis summer–autumn 1886; finished Aug 1887; printed Jan 1888).
- **Works record:** missing — the dive is the source-grounded basis to create it.
- **Mode:** in-session unattended; no `AskUserQuestion` gating; judgment calls → `needsReview`; note `draft: true`; medium visual intensity.

## Deviation from plan (spend limit)

The three planned background sweep agents (diaries / letters / visuals) and the Phase-5 verifier were dispatched as subagents, but a **mid-session monthly spend limit** returned them empty (0 tool-uses). All of that work was therefore done **in the main context**: the diary extraction and read, the letter sweep (Tom 64, reusing the WTMWD-extracted Strakhov and Alekseev letters and adding the Ozmidov genesis letter), the visual sweep (a main-context Commons fetcher), and the scholarship web sweep. The independent opus **verifier did run** later in the session (a foreground dispatch succeeded after the limit window) — see Verification.

## What was covered

- **Deep read** of the introduction, all 35 chapters, the conclusion and 3 addenda, using Tolstoy's own «Обзор содержания по главам» as the spine; keystone passages extracted byte-faithful (the mill parable; the fundamental contradiction; the world-teachers' definitions of life; reason as the law of life; renunciation of the animal personality; the body as the "instrument of life"; the **refutation of Schopenhauer and Hartmann**; love as «единственная разумная деятельность человека» and as self-sacrifice; «нет смерти»; death as a new relation to the world; the conclusion).
- **Genesis triply grounded:** the summer-1886 near-fatal leg illness and the A. K. Dieterichs reply-letter (commentary); the **19 June 1886 diary that drafts the whole argument before that letter** (the dive's one intra-corpus contradiction of the received genesis); and the Grot / Moscow Psychological Society lecture «Понятие жизни» (14 March 1887), with the Ozmidov, Alekseev and Strakhov letters. The reply-letter → «О жизни и смерти» → lecture → book chronology reconstructed from the apparatus; the title-change («вычеркнул „и смерти"») documented from Tolstoy's own letter.
- **Redaction history** (seven redactions incl. the heavy "proof redaction" of Aug–Dec 1887; the «и смерти» dropped on 3 Aug 1887; Grot's proofs) summarized from the commentary.
- **Publication/suppression** (the most violent of the Prophet books): the 1888 Mamontov first edition (Часть 13, 600 copies) **banned and destroyed by the Holy Synod on 5 April 1888** (Censorship-Committee report «не слово Божие, а единственно… человеческий разум» → Synod destroy order, via Apostolov/Synod file No. 2264); first legal Russian partial in «Неделя» 1889 («Мысли о жизни»); French *De la vie* (S. A. Tolstaya & Tastevin, 1889); English *Life* (Hapgood, 1888); Geneva (Elpidine) 1891; Christchurch («Свободное слово») 1903.
- **Reception** grounded in both the Church (Synod ban; Archbishop Nikanor) and the philosophical society (Grot; the Psychological-Society debate; Strakhov's Fichte comparison; Tsertelev's sympathetic account and Kozlov's polemic, both 1890) — the corpus's analytical point being that the Church banned the book for *rationalism*, not mysticism.
- **Scholarship triangulation** (6 entries) against the modern critical edition (Medzhibovskaya & Denner 2019), Gustafson (1986) and Soina; the headline finding is that the primary text *contradicts* the "woolly mysticism" and "restatement of Schopenhauer" framings.
- **Visuals:** 7 PD images cached (keystone = Repin's 1887 Tolstoy portrait; Grot, Strakhov, Chertkov, A. K. Dieterichs, S. A. Tolstaya; Ge's 1884 Tolstoy).

## Coverage ledger

| Surface | Status |
|---|---|
| Genesis & composition | covered |
| What the work says | covered |
| Redactions & textual history | partial (1.2 MB variants file + «Неделя» variants not collated) |
| Publication, censorship & translation | covered |
| Reception & afterlife (society + Church) | covered (wider lay reception only sketched) |
| Place in the cluster | covered |
| The author's later verdict | partial (the 19 Mar 1889 De la vie diary verdict only) |
| Visual & manuscript record | covered (1888 + De la vie title-pages not openly found) |

## Entity work-order (ingestion priority → dependency)

**Priority 1 (central; write first):** Reason as the law of life (разум) [concept]; The animal personality and true life (животная личность / истинная жизнь) [concept]; Love as the activity of true life (любовь) [concept]; N. Ya. Grot [person]; A. K. Chertkova (Dieterichs) [person]. Leo Tolstoy EXISTS.
**Priority 2:** Death as a new relation to the world («нет смерти») [concept]; Moscow Psychological Society [institution]; «Понятие жизни» lecture, 14 March 1887 [event]; Holy Synod ban of On Life (1888) [event]; N. N. Strakhov [person]; P. I. Biryukov [person — **EXISTS** as `Pavel Birukoff.md`, link there]. V. G. Chertkov, S. A. Tolstaya EXIST.
**Priority 3:** N. L. Ozmidov; V. I. Alekseev; L. E. Obolensky; Isabel F. Hapgood; M. K. Elpidine (all MISSING). Yasnaya Polyana EXISTS.

## Visuals work-order

Cached (PD, usable): Repin 1887 *Tolstoy* (keystone); Ge 1884 *Tolstoy*; Grot; Strakhov; Chertkov (Kramskoy); A. K. Dieterichs (Shapiro); S. A. Tolstaya (1875).
**To acquire (request from holdings):** a title-page facsimile of the **banned 1888 first edition** (RGB / State Tolstoy Museum — only 3 copies survive; the keystone publication artefact); a title-page of the French ***De la vie*** (1889, Marpon & Flammarion — check Gallica/BnF); an 1880s photograph of S. A. Tolstaya closer to the translation period.

## Work-record work-order (proposed fills for a NEW record)

**High confidence:** titleRu «О жизни»; titleEn "On Life"; titleAlternatives (working «О жизни и смерти»; *De la vie* fr; *Life* en; «Мысли о жизни» the «Неделя» title); firstPublishedVenue (Часть 13, Mamontov 1888, banned/destroyed); bans[] (1 schema-clean event: holy-synod / complete-ban / 1888-04-17 NS = 1888-04-05 OS; destroy order of all 600 copies); publishedDuringLifetime / publishedInRussiaDuringLifetime = true; samizdatCirculation true; identifiers.jubileeEdition.volumes 26.
**Medium/low:** dateWritingStarted ~1886 (approximate); dateWritingCompleted ~1887 (approximate); genre essay; dateFirstPublished 1888 (which event — see needsReview); dateFirstPublishedInRussia ~1889 (Неделя, partial); censoredVersionExists false (see needsReview); relatedWorks [what-then-must-we-do, what-i-believe, confession]; excommunicationRelated false (see needsReview). Folder (treatises) → human decision.

## needsReview (deferred human judgment)

1. `dateFirstPublished` — which event the field carries (1888 banned-destroyed Mamontov ed. / 1888 English / 1889 French / 1889 «Неделя» partial / 1891 Geneva complete). No clean first publication: the only complete authorized edition was destroyed.
2. `bans[].scope` encoded as `complete-ban`; whether to add a second `confiscation` entry for the destroy order.
3. `censoredVersionExists` (proposed false) given the partial-but-unaltered «Неделя» 1889 legal selection.
4. `excommunicationRelated` (proposed false) — 1901 edict names no works; the 1888 Synod ban is a precedent, not a direct tie.
5. New record folder (treatises) + filename.
6. The Censorship-Committee / Synod quotations and the genesis details (Dieterichs as "instigator"; Grot's proofs) are drawn from the PSS Tom 26 commentary / Apostolov, not from byte-extracted PD primary documents — attribute, don't byte-claim.

## Verification

- `verify_quotes.py` → **23/23 verbatim PASS** (re-confirmed after the verifier fixes). No superscript-marker or elision issues; the Schopenhauer/Hartmann quote (`onlife-text-07`) preserves the source's `( Шопенгауэр` spacing exactly.
- Phase-5 verifier (opus, fresh context) → **PASS-WITH-NITS, 1 must-fix**, all resolved before commit. **Must-fix:** P. I. Biryukov was marked `missing` though the vault holds `Pavel Birukoff.md` — corrected to `exists` / `wikilinkTarget: Pavel Birukoff` (the project's Birukoff transliteration; my earlier grep missed it). **Nits (all applied):** dropped an endorsing "rightly" before Soina (voice); changed `bans[].scope` to the schema value `complete-ban` and removed a "Schema-clean" overclaim; added the un-swept-wider-reception hedge to the index.md prose. The verifier independently re-derived the byte-fidelity sample and confirmed the headline Schopenhauer-refutation claim against the extract. Report: `_verifier-report.md` (with a resolution footer).

## Evaluation self-assessment (work-dive gate)

- Interlocutor sweep yielded people? **Yes** — Grot and A. K. Dieterichs (the two new central figures), Strakhov, Ozmidov, Obolensky, Biryukov, the Moscow Psychological Society, plus Hapgood/Elpidine/Tastevin and S. A. Tolstaya as translators, all carried into `entities`.
- Russian society/Church reception covered? **Yes** — the Synod ban (with the Committee's stated reason and Nikanor's letter) and the philosophical reception (Grot, Strakhov, Tsertelev, Kozlov); wider lay reception honestly marked as only sketched.
- `workRecord` fill accurate & provenanced? **Yes** — every field evidence/commentary-anchored; the ban encoded with schema-clean vocab (verifier-confirmed OS→NS date); uncertain fields → `needsReview`.
- `coverage` honest? **Yes** — Redactions and later-verdict marked `partial`; Reception graded `covered` with the lay-reception limit disclosed in prose and dossier (verifier-accepted).
- `--choice=reg` extracted cleanly? **Yes** — pre-reform resolved across the work, lecture, diaries and letters; diary/letter bodies needed `--notes=auto`. The diary witness for 1886–87 is **rich** for this work (unlike the thin witness the economic treatise found in the same window) — the 19 June 1886 entry drafts the whole book.
- Spine stayed bare? **Yes after the NIT fix** — "mysticism" attributed and rejected via the primary text; Schopenhauer named as the refuted party, not adopted as a label; commentary facts attributed throughout.

## Models & rough cost

Main loop: Opus (in-session) — did all the deep read, the diary/letter/visual sweeps and the synthesis after the subagent spend limit hit. Subagents: 3× attempted background sweeps (returned empty under the spend limit, 0 useful tokens) + 1× Opus verifier (~97k tokens, ran foreground). Web sweeps: scholarship (2 searches + 2 fetches) and the Commons visual fetcher (8 API calls, 7 downloads). No licence-gated downloads to `website/src/`.

## Output paths

- `docs/research/1886-1887-on-life/index.md` (+ rendered `index.html`, git-ignored)
- `docs/research/1886-1887-on-life/dossier.yaml`
- `docs/research/1886-1887-on-life/extracts/` (PD primary extracts — work, «Понятие жизни» lecture, 6 composition-window diaries, 3 cited letters)
- `docs/research/1886-1887-on-life/visuals/` (git-ignored cache; 7 PD images)
- `website/src/posts/notes/2026-06-06-on-life.md` (draft)
- `session-log.md`, `_verifier-report.md`, this `run-report.md`

Wiki ingestion is a separate, human-in-the-loop step — this dossier is the pointer, not the writer.
