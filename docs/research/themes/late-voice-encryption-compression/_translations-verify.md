# Translation verification audit

Scope: all 37 finished English translations in `_translations-draft.md`, checked against
the dossier `quoteRu` (locked-quote fidelity), the source `extracts/*.txt` (full-sentence
fidelity, `--choice=reg` normalisation allowed), and for translation accuracy + register.

Method note: all 37 `RU (locked)` spans were compared byte-for-byte against the dossier
`quoteRu` programmatically — **all 37 match exactly**. Every `RU (full sentence)` given in
the draft was located in its extract file and matches (allowing the documented orthography
normalisation and ellipsis at sentence boundaries). No invented sentences found. The
findings below are therefore all about the **English rendering**, not the Russian.

## Verdict: CLEAN-WITH-MINORS  (0 must-fix, 2 minor)

## Per-entry findings (list ONLY entries with an issue)

### comp-krug-genesis — MINOR
- issue: «распространяю» is rendered "I am expanding". The default sense of «распространяю» (impf. of распространять) is "I am circulating / disseminating / spreading" — the word for "enlarging/expanding" would normally be «расширяю». The note acknowledges and defends the "enlarging" reading, but it is a genuine interpretive call, and the more natural reading ("circulating Thoughts of Wise People") also fits the sentence (he lists works he is writing *and* a book he is putting about). Note: this falls in the context-sentence, NOT the locked span — the locked span «Хочу сделать из них Круг чтения на каждый день» → "I want to make of it a Circle of Reading for every day" is accurate.
- current EN: "and I am expanding Thoughts of Wise People"
- suggested EN: "and I am circulating Thoughts of Wise People" (or, if the enlarging sense is kept, footnote the ambiguity rather than assert it)
- why: «распространяю» normally means disseminate/circulate, not expand; the chosen reading is defensible but should not be presented as settled.

### key-sholom-aleichem — MINOR
- issue: «разлада, который поселяется» is rendered "discord that is being sown". «Поселяется» means "settles in / takes root / takes up residence"; "sown" imports a different (agricultural, externally-caused) metaphor and a passive that the Russian (reflexive, the discord settling itself) does not have. Meaning is preserved and the English idiom "sow discord" reads naturally, but it is a small metaphor substitution rather than a literal rendering.
- current EN: "the whole discord that is being sown among a certain small part"
- suggested EN: "the whole discord that is taking root among a certain small part"
- why: closer to «поселяется» (settles in / takes root) and avoids importing an unstated agent.

## Notes (no change required, recorded for the ingestion reader)

### comp-grand-monde-turn — NOTE
- The EN itself — "the need to write for the 'grand monde' [the great world], and for it alone" — is a faithful, literal rendering of «чувствую потребность писать для grand monde, и только для него». No issue with the translation.
- The **note** glosses «grand monde» as «народ» / "the great world of ordinary humanity". That is interpretively contestable: `grand monde` in French normally denotes high society / the fashionable world — the *opposite* of народ. In the diary entry Tolstoy does go on to say the Krishna legend is «превосходно для народа», so the dossier's народ reading is arguable, but the equation is a reading, not a given. Flagged as steer for the ingestion reader, not a translation error.

### enc-inoskazatelno-rejected — NOTE
- Locked span and full sentence both verified against the draft (черновое) passage. The extract prints «au delа» (a Cyrillic-а OCR artefact); the draft correctly normalises to French «au-delà». The draft's full sentence opens with «...признаюсь вам», eliding the extract's «во-2-х,» — a fair truncation, not an invention. The omission of the final standalone «Совестно.» is also fair (it falls outside the cited span). EN is faithful ("I somehow feel ashamed to speak in allegories").

### chan-posthumous-diary — NOTE (metadata, not translation)
- Translation is accurate. Unrelated to the EN: the extract opener reads «4 Фев. 1909» and the filename is `1909_01_04`, while the dossier/draft date the entry 1909-02-04. A date-metadata discrepancy (Feb vs Jan), already comparable to the known TEI diary filename-year gotcha; out of scope for this translation audit but worth a glance before the date drives anything.

## Entries confirmed accurate (id list)
key-sholom-aleichem (see minor above; rest accurate), con-chas-cant-print, con-censored-lit-idle, con-banned-printed-england, con-two-track-strategy, con-tarsakov-samizdat, con-davydov-uncensorable, con-gogol-double-bind, con-bolkvadze-predict, con-kazmichov-full-text, chan-rule-only-through-you, chan-public-sole-node, chan-abroad-rationale, chan-all-or-nothing, chan-posthumous-testament, chan-posthumous-diary, chan-stolypin-ultimatum, chan-router-svobodnoe-slovo, chan-nemogu-molchat, chan-herzen-model, chan-gorbunov-recycle-banned, chan-chertkov-controls-all, enc-inoskazatelno-rejected, comp-mysli-announced, comp-krug-genesis (see minor above; locked span accurate), comp-krug-abroad-uncensored, comp-krug-design-principle, comp-put-like-krug, comp-400-days-obligation, comp-truth-simple-form-hard, comp-only-what-i-published, comp-daily-spiritual-practice, comp-grand-monde-turn, comp-krug-stated-aim, comp-put-drops-attributions, comp-put-three-superstitions, comp-tat-tvam-asi-schopenhauer
