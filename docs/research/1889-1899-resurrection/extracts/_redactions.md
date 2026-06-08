---
layer: research-prototype
status: draft
created: 2026-06-08
source: PSS Tom 33 redactions (TEI extraction); PSS 33 pp. 329–422 (история писания)
scope: light sampling — redaction survey + church-service scene focus
---

# Resurrection — Redactions & Textual History (light sample)

PSS Tom 33 contains nine holding files for the redaction material. This note (a) inventories them, (b) samples the church-service scene across redactions, and (c) samples the "Notes and questions" file. It is a research prototype, not a full collation.

---

## 1. Redaction table

| Redaction label | PSS pages | Holding file | Extract lines | Stage / what differs |
|---|---|---|---|---|
| 1st unfinished (Pervaja nezakonchennaja) | 3–18 | `v33_003_018_Pervaja_nezakonchennaja_redaktsija_Voskresenija.xml` | 196 | Dec 1889 – early 1890. Earliest draft; no title; protagonist named Valeryán (not Nekhlyudov); Easter scene in village church present; no prison-church service; breaks off early. |
| 2nd unfinished (Nachalo vtoroj) | 19–22 | `v33_019_022_Nachalo_vtoroj_nezakonchennoj_redaktsii_Voskresenija.xml` | 34 | Fragment only (4 pages). Protagonist now Arkadiy Neklyudov; no church service scene. |
| 1st finished redaction (Pervaja zakonchennaja) | 23–94 | `v33_023_094_Pervaja_zakonchennaja_redaktsija_Voskresenija.xml` | 1090 | 1895 resumption. Full draft through Siberia; trial, visits, marriage plan; passing prison-church mention ("острожная церковь") but no described liturgy; Toporov / political prisoners absent. |
| 2nd redaction | 95–135 | `v33_095_135_Voskresenie_2_ja_redaktsija.xml` | 500 | Aug 1898 first pass (pre-3rd). Expanded characterisation of Nekhlyudov; "обедня" mentioned as daily prison routine; no described service; Rozanov → Rozanova change begins. |
| **3rd redaction** | **135–160** | **`v33_135_160_Voskresenie_3_ja_redaktsija.xml`** | **330** | **27–28 Aug 1898 (own-hand dates on mss. 14–18, per история писания). First appearance of detailed prison-church service description (two drafts, PSS variants 57–58). No political prisoners yet. Maslova → separate cell; Fedosya episode. Ending: Maslova marries political Anosov in Siberia; Nekhlyudov does not marry her.** |
| 4th redaction | 161–217 | `v33_161_217_Voskresenie_4_ja_redaktsija.xml` | 1272 | Late 1898. Political prisoners (Simonson etc.) enter; Toporov and Synod confrontation written; church-service description retained and further revised; longest redaction. |
| 5th redaction | 217–261 | `v33_217_261_Voskresenie_5_ja_redaktsija.xml` | 630 | 1898–99. Further reworking; passage of political prisoners stabilised; church scene present (3 church-vocab hits). |
| 6th redaction | 261–321 | `v33_261_321_Voskresenie_6_ja_redaktsija.xml` | 828 | Late 1898 – early 1899. Closest to the Niva serialisation text; church scene condensed vs. 3rd-redaction double draft. |
| Notes and questions | 322–326 | `v33_322_326_Zapisi_i_voprosy_otnosjaschiesja_k_Voskreseniju.xml` | 274 | Research notes and procedural questions, undated. Prison logistics, legal procedure, Siberian dialect glossary; one church-going note (see §3). |

Genesis commentary source: PSS 33, pp. 329–422 (extracted as `v33_329_422_Istorija_pisanija.txt`).

---

## 2. Church-service scene: 3rd redaction sampling

### Confirmed: detailed liturgy first appears here

The история писания states explicitly (PSS 33, p. 405, extract line 155):

> «В конечной стадии работы над третьей редакцией впервые дано подробное описание богослужения в тюремной церкви (см. варианты №№ 57 и 58).»

("In the final stage of work on the third redaction, for the first time a detailed description of the divine service in the prison church was given [see variants nos. 57 and 58].")

The 3rd-redaction extract (`v33_135_160_red3.txt`) contains **two adjacent drafts** of the scene (variants 57 and 58), both present in the extracted text. This is consistent with the TEI encoding of two variant texts within the same holding file.

### Draft A (shorter / variant 57, extract lines ~163–185)

Setup: Maslova is in the cell the night before; a girl sews her dress for «завтрешнюю обедню» ("tomorrow's obednya"). Next morning after roll-call the women are called to service. The account is brief:

> «За обедней опять виделась с Костиненко. Священник читал проповедь. Певчие пели хорошо.»
>
> (working EN: "At the service she again saw Kostinenko. The priest read a sermon. The choir sang well.")

Then immediately the narrative frame:

> «И началась служба. Стояли тысячи измученных и мучимых мущин и женщин, лишенных человеческого образа и охраняемых людьми в мундирах с тесаками, саблями и штыками, и для утешения совершалась христианская молитва — церковная служба, в которой им, хотя и с некоторыми ограничениями, позволялось принять участие.»
>
> (working EN: "And the service began. Thousands of tormented and tormenting men and women stood there, stripped of their human semblance and guarded by men in uniforms with cutlasses, sabres and bayonets, and for their consolation a Christian prayer was performed — a church service in which they were permitted to participate, though with certain restrictions.")

This is followed by a detailed step-by-step description of the proskomedia (preparation of the eucharistic bread, cutting five loaves into prescribed fragments), the vestments, the deacon's chant, the consecration narrative, the distribution of communion, and the kiss of the cross — all rendered in Tolstoy's characteristic defamiliarising voice, naming liturgical actions in secular terms without using their liturgical names.

### Draft B (expanded / variant 58, extract lines ~195–215)

A second, slightly restructured version follows almost immediately in the same file. It opens with a theological framing paragraph:

> «Религия, которую исповедывали и арестанты и те, которые содержали их, была религия Христа, та религия, которая, по словам Христа, состоит в том, чтобы не делать другому чего не хочешь, чтобы тебе делали, в прощении всех...»
>
> (working EN: "The religion professed by the prisoners and by those who held them was the religion of Christ, that religion which, in Christ's own words, consists in not doing to another what you would not wish done to yourself, in forgiving all...")

Then the same detailed liturgical sequence — deacon, priest, proskomedia, five loaves — is re-narrated with slight verbal variants, adding a line about the deacon preparing "ризу и стихарь для священника и дьякона" (vestments for priest and deacon, i.e. a deacon is now explicitly present). The passage ends with Maslova identified as belonging to the non-believing majority: «Маслова принадлежала к первым. Она не верила ни во что и крестилась и кланялась только потому, что все так делали, но оставалась совершенно холодной.» ("Maslova belonged to the first group. She believed in nothing and crossed herself and bowed only because everyone else did, remaining completely cold.")

### Comparison with earlier redactions

**1st unfinished redaction (1889–90):** Contains an Easter church scene (lines 43, 49, 53, 79) set in the village church — the seduction night context — with a brief описание of the service: priest, choir, Christ is Risen. No prison church.

**1st finished redaction (1895):** Church mentions are: a simile ("как после длинной с молебном и водосвятием обедни", line 143), a priest and oath-taking at the trial (lines 97, 127, 171), a passing mention of "острожная церковь" in connection with Maslova's wedding (line 1083). No described liturgy in the prison. A priest walks through the courthouse corridor; Nekhlyudov notes the oath-taking procedure with mild irony — but the extended defamiliarising account of the Liturgy is entirely absent.

**2nd redaction:** Three church-vocab hits, all routine mentions (obednya as prison daily routine). No described service.

**4th–6th redactions:** Church-service vocabulary hits rise (23 in the 4th), confirming the scene is retained and developed in subsequent redactions.

### Comparison with published text

The final published text (v32, Niva serialisation) has the prison-church scene in Part I, chapters 39–40. The 3rd-redaction drafts are recognisably the same scene but in a rawer, more discursive form: the two-draft structure suggests Tolstoy wrote it, then immediately rewrote it with the theological framing moved forward. The final text is more controlled — the defamiliarising catalogue of liturgical gestures is tighter and the explicit authorial commentary on "pagan idolatry" (3rd redaction: «веками выработанное, грубое языческое поклонение») is largely transferred to Nekhlyudov's interiority. The Dunya/Dunicha communion detail (she takes communion because it lets her pass notes to male prisoners) appears in both 3rd-redaction drafts and survives nearly verbatim into the final text.

**Caveat:** This is a light sample based on extracted text. A full collation of the two 3rd-redaction drafts against the final text, and against the 4th-redaction version (which has the highest church-vocab density at 23 hits), has not been done here.

---

## 3. Notes and questions file: church and moral-scheme sampling

The "Notes and questions" file (`v33_322_326_notes.txt`, 274 lines, 8 numbered sections) is a working research document — logistics questions, legal procedure, a Siberian dialect glossary. It does not contain sustained prose.

**Church / prison-routine note (§2):**

> «В церковь ходят попарно, надзиратель впереди. Пьяны не бывают.»
>
> (working EN: "They go to church in pairs, warden in front. They are never drunk.")

This is a factual note from Tolstoy's prison research visit, probably Butyrki, 1895 or 1898. It is the only church note in the document. It confirms the procedural detail that appears in the 3rd-redaction text (Maslova is called from the service by a warder).

**Moral-scheme note (§7, closing entry):**

> «Катюша отвращение получила от половой жизни, потом отдалась ей в форме любви и брака.»
>
> (working EN: "Katyusha developed an aversion to sexual life, then surrendered to it in the form of love and marriage.")

This is a character-arc note sketching Katyusha's trajectory — aversion following the seduction, then re-engagement via legitimate relationship. It maps roughly onto the Simonson storyline of later redactions, though the note is undated and may predate it.

**§8 (final entry):**

> «Ужас того, что непредвидено. Страх, что умерла Маслова и злая надежда, что это она.»
>
> (working EN: "The horror of the unforeseen. The fear that Maslova has died and the malicious hope that it is she.")

This appears to be a psychological note for Nekhlyudov — his ambivalence about Maslova's fate at a moment of uncertainty. Its placement in the novel is unclear from this excerpt alone.

No other church, communion, or Synod-related material appears in the notes file.

---

## Source files (all in `extracts/`)

- `v33_003_018_red1a.txt` — 196 lines
- `v33_019_022_red2a.txt` — 34 lines
- `v33_023_094_red1fin.txt` — 1090 lines
- `v33_095_135_red2.txt` — 500 lines
- `v33_135_160_red3.txt` — 330 lines ← church scene sampled here
- `v33_161_217_red4.txt` — 1272 lines
- `v33_217_261_red5.txt` — 630 lines
- `v33_261_321_red6.txt` — 828 lines
- `v33_322_326_notes.txt` — 274 lines

Extracted with: `extract_tei.py --choice=reg --notes=auto`
