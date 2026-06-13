# Visual Materials — «Смерть Ивана Ильича» (The Death of Ivan Ilyich)

**Intensity:** light (~4–6 items)  
**Channels consulted:** local `primary-sources/jubilee-edition/`; Wikimedia Commons API (`generator=search`, `categorymembers`, `prop=imageinfo&iiprop=url|extmetadata`); archive.org advancedsearch  
**Date of sweep:** 2026-06-07

---

## Items

| id | type | subject | relatedEntity | holding | archiveId / url | access | rights | licence | usable | localPath | note |
|----|------|---------|---------------|---------|-----------------|--------|--------|---------|--------|-----------|------|
| V01 | photo | Leo Tolstoy, half-length portrait, facing right, c. 1880 | Tolstoy (author) | Library of Congress / Wikimedia Commons | [LCCN99615676](https://lccn.loc.gov/99615676) · [Commons](https://commons.wikimedia.org/wiki/File:Count_Leo_Tolstoy,_half-length_portrait,_facing_right_LCCN99615676.jpg) | open | PD-US / PD-old | PD | yes | `visuals/commons-tolstoy-lccn-1880.jpg` | Cabinet-card photograph, 1880. Tolstoy aged ~52; composition of Ivan Ilyich began 1884. Best pre-composition portrait available with clear LCCN provenance. Artist: PPOC/LoC. |
| V02 | photo | Leo Tolstoy portrait, 1887 | Tolstoy (author) | Wikimedia Commons | [Commons](https://commons.wikimedia.org/wiki/File:Leo_Tolstoi_1887.jpg) | open | PD-old-100 | PD | yes | `visuals/commons-leo-tolstoi-1887.jpg` | Photograph by Thomas Johnson / Шерер и Набгольц, 1887 — one year after first publication of the novella; closest dated Commons photo to the 1884–1886 composition window. |
| V03 | portrait | Élie Metchnikoff (Илья Ильич Мечников), portrait c. 1905 | Ilya Ilyich Mechnikov (brother of prototype Ivan Ilyich Mechnikov) | Wikimedia Commons (via Victor Fraitot, 1906 monograph) | [Commons](https://commons.wikimedia.org/wiki/File:%C3%89lie_Metchnikoff-portrait.jpg) | open | PD-old | PD | yes | `visuals/commons-metchnikoff-portrait-1905.jpg` | Portrait from Fraitot's *Une page d'histoire du XIX^e siècle — Pasteur*, dated 1905. PD (artist Fraitot d. 1906, >100 yr). Useful for Genesis section: Élie Metchnikoff was Nobel laureate (1908) and brother of the real-life model for Ivan Ilyich Mechnikov, the Tula prosecutor. |
| V04 | photo | Leo Tolstoy and Ilya Ilyich Mechnikov together, 1909 | Tolstoy + Mechnikov | Wikimedia Commons (source: журнал *Огонёк* №24, 1909) | [Commons](https://commons.wikimedia.org/wiki/File:Leo_Tolstoy_%26_Ilya_Mechnikov.jpg) | open | PD-RusEmpire | PD | yes | `visuals/commons-tolstoy-mechnikov-1909.jpg` | Outdoor photograph, summer 1909, published in *Ogonyok*. Shows the two men together — a striking document that Tolstoy and the brother of his novella's real-life model actually met. |
| V05 | facsimile | PSS Tom 26 (90-vol. academic edition), p. 61 — opening of «Смерть Ивана Ильича» | Tolstoy (text) | Local: `primary-sources/jubilee-edition/vol86/vol86.pdf` (= PSS Tom 26, Гослитиздат 1936) | local only | PD (pre-1928 Russian scholarly edition) | PD | yes | `extracts/pss-tom26-p61-ivan-ilyich-opening.png` | Rendered at 220 dpi from PDF page 72 of vol86.pdf (= printed p. 61, PSS Tom 26) and converted to PNG (committed). Text confirmed: «СМЕРТЬ ИВАНА ИЛЬИЧА. I. В большом здании судебных учреждений…». |
| V06 | title-page | 1886 first edition — «Сочинения графа Л. Н. Толстого», Часть 12, Moscow 1886 (S. A. Tolstaya ed.) | Tolstoy (first publication) | **GAP** | not located | — | — | — | — | — | Searched Commons (no hit), archive.org (no hit for this specific vol.), RNB/RSL/runivers not queried. The 1886 vol. 12 title-page facsimile was not found in any open digital repository during this sweep. Recommend checking RSL (РГБ) digital catalogue and runivers.ru directly. |

---

## Notes

- **Keystone portrait (V02)** is the 1887 photograph — one year post-publication, composition period effectively closed. If a clearly-dated 1884–1885 photograph surfaces, it would supersede V01 (1880) as the closer keystone. V01 (1880, LCCN) remains the best pre-composition candidate with full provenance.
- **Metchnikoff brother note:** Élie Metchnikoff (1845–1916) = Nobel 1908 (Physiology/Medicine). His brother **Ivan Ilyich Mechnikov** (1836–1881) was a Tula provincial prosecutor — widely cited as one model for the protagonist. The V04 joint photo (1909) is an exceptional find: it documents that Tolstoy and Élie actually met, well after the novella was written.
- **First-edition gap (V06):** The 1886 «Сочинения», Ч. 12 is the correct bibliographic target. No digital facsimile was located in this sweep. The PSS Tom 26 (V05) is the authoritative scholarly text and serves as a functional substitute for the textual facsimile.
- **Local PSS facsimile:** The local repo uses a non-obvious path mapping (`vol86/` = PSS Tom 26). The file is confirmed Russian academic edition (Гослитиздат, «Весь Толстой в один клик» digitisation). PNG render committed to `extracts/` (`pss-tom26-p61-ivan-ilyich-opening.png`).
- **Illustration (optional target):** No clearly-PD standalone illustration of the novella was found on Commons in this sweep. The `File:Tolstoy (IA tolstoy00noye).pdf` on Commons is a different Tolstoy work. Target deferred.
