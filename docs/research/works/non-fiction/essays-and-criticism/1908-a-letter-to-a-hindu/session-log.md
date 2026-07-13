# Session log — 1908-a-letter-to-a-hindu

## Session 1 — 2026-06-13 (work-subject dive, in-session, NOT --novel)

Subject: Tolstoy's open letter «Письмо к индусу» / "A Letter to a Hindu" (1908), reply to Tarak Nath Das, editor of *Free Hindustan*. Reception centre = Gandhi.

**Phase 0–2 — corpus locked.** Main text `works/v37_245_272_Letter_to_a_Hindoo_Pismo_k_indusu.xml` (PSS Tom 37, pp. 245–272) carries BOTH the authorized contemporary English (Chertkov, revised by Tolstoy) *and* the full Russian original (extract line 169+). Extracted `--choice=reg --notes=auto`. Composition history from `comments/v37_444_446_…Istorija_pisanija…`. Genesis diary entries (Tom 56): 10 Jun, 30 Oct, 28 Nov, 6 Dec, 14 Dec 1908 (all OS). Gandhi correspondence: v80_149 (25 Sep/7 Oct 1909, confirmation+permission+reincarnation), v81_318 (25 Apr 1910, on *Hind Swaraj*), v82_178 (7 Sep 1910, the last long non-resistance letter — "most central, most important of all the affairs being done now in the world"). Companion: Chitale letter v78_023 (Jan 1908, Bhagavad-Gita). Cluster siblings located: Letter to a Chinese (v36, 1906), Address to the Chinese People (v34, 1900).

**Phase 3 — scholarship sweep** (sonnet subagent → `extracts/_scholarship.md`, 4.5k words). Key: *Indian Opinion* serialized the letter 25 Dec 1909 / 1 Jan / 8 Jan 1910 (resolves the 1909-vs-1910 split). Das REJECTED the letter ("Open Letter to Count Leo Tolstoy…", 16 Oct 1909) — wanted endorsement of armed struggle, got non-resistance. Hazama (2023): the letter shaped Gandhi's S. Africa phase but ahimsa/satyagraha framing came later — "shaped" ≠ "produced." Krishna epigraphs = from Baba Premananda Bharati, *Sree Krishna: The Lord of Love* (1904). Several agent needs-review items RESOLVED by primary evidence (Spencer epigraph in text line 265; Chertkov-translated-Tolstoy-revised stated in PSS commentary; "most important work" phrasing in v82).

**Phase 2 visuals** (sonnet subagent → `visuals/_visuals.md`, 6 images downloaded). Keystone = Prokudin-Gorsky 1908 colour photo (80th birthday, same year). No manuscript/first-edition facsimile openly available → GTM request. No local Russian PSS Tom 37 facsimile: `jubilee-edition/vol37/` is mislabelled (actually Tom 73). Facsimile → needsReview.

Tooling: lxml/PyYAML installed in `/tmp/tolstoy-dive-venv`.

Entity vault: Chertkov EXISTS (`wiki/Vladimir Chertkov.md`); Gandhi, Tarak Nath Das, Makovitsky, Gusev, Vivekananda, Baba Premananda Bharati, Krishna, Škarvan/Schmitt all MISSING.

**Phase 4–5 — built + verified.** dossier (29 evidence rows, verify_quotes 29/29 PASS), index.md (full work-dive spine + marquee + Gandhi reception), draft note, serve.py rendered. Separate-pass opus verifier → **CLEAN-WITH-MINORS**, 1 must-fix applied (Non-resistance entity vaultStatus stub→missing) + 1 nit (work-typed entity note clarified). Report: `_verifier-report.md`.

**Phase 6** — `run-report.md` written (coverage ledger + entity/work-record/visuals work-orders + self-assessment).

Done: dossier ✓ verify_quotes ✓ index.md ✓ note ✓ serve.py ✓ verifier ✓ Phase 6 ✓. Remaining: Phase 7 handoff skill → commit (no push).
