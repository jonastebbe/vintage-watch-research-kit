# Vintage watch research kit

A free, printable worksheet for recording what a vintage watch actually shows, separating observations from claims, and keeping the sources behind an identification.

Published by [The Index](https://theindex.watch), a reference guide to vintage watches. This kit works with any reference source and can be used offline. It is not an authentication or valuation service.

## Download the fillable packet

- [A4 PDF](output/pdf/vintage-watch-research-a4.pdf?raw=true)
- [US Letter PDF](output/pdf/vintage-watch-research-letter.pdf?raw=true)

Each three-page packet contains an observation sheet, a reusable claim-and-evidence page, and a photo request checklist. Download the PDF to type into its 28 fields and checkboxes, or print it. Save a copy and reopen it to check that your PDF reader preserves your entries. The blank packet can be shared freely; keep completed records and full serial numbers private.

Clubs and educators may distribute the blank packet under the MIT licence. No signup or purchase is needed. The Markdown templates below offer more detailed fields for longer research projects.

## Start with the watch

1. Copy [the identification worksheet](identification-worksheet.md) for each watch.
2. Record visible markings exactly, before interpreting them. Keep model references, case serials and movement numbers in separate fields.
3. Use [the evidence log](evidence-log.md) to connect each proposed identification to a source and a visible detail.
4. Keep disagreements and missing photographs explicit. A matching reference or a plausible serial date is only one part of an identification.
5. Use [the photo request checklist](photo-checklist.md) when the available photographs cannot answer a specific question.

Print the Markdown files from your editor or paste them into your notes. Do not publish a seller's private details or a full serial number in a public copy.

## Reference tools

| Research question | Starting point |
| --- | --- |
| Which brand and model family should I investigate? | [Browse vintage watch brands](https://theindex.watch/brands) |
| What does this reference identify? | [Search The Index](https://theindex.watch/watches) |
| Can this number be dated, and what does the date mean? | [Serial checker and coverage notes](https://theindex.watch/serial-check) |
| What does a collector or technical term mean? | [Watch glossary](https://theindex.watch/glossary) |
| Where can I find deeper published research? | [Watch books](https://theindex.watch/books) |

Read the limitations of each tool and follow its underlying sources. An approximate numbering date, delivery date and sale date are different observations. Tools do not establish that every component left the factory together.

## Worked example

This is a **fictional example**, not a record of a real watch:

- Observation: a listing calls a watch “Reference AB123, 1964”; the reference is not legible in its photographs.
- Evidence: the listing is evidence of the seller's claim, not independent evidence of the engraving or date.
- Status: reference unconfirmed; year unconfirmed.
- Next step: request a sharp photograph of the reference and the basis for the year. If movement access is needed, ask a qualified watchmaker to handle it.
- Resolution: retain the original claim alongside the new evidence. Do not silently turn a seller's date into an established production year.

## Sharing and attribution

The original templates in this repository are available under the [MIT licence](LICENSE). You may adapt them for a collecting club, research notes or a watchmaker's intake workflow. Suggested attribution: “Vintage watch research kit — The Index”, with a link to this repository or [theindex.watch](https://theindex.watch).

The licence covers this kit only. It does not license The Index's catalogue, photographs, linked articles or other third-party material. See [The Index's content reuse policy](https://theindex.watch/reuse-policy/v1).

## Rebuild the PDFs

Install Python and `reportlab`, then run `python3 build_printable.py`. Generated files are in `output/pdf/`. The generator and original worksheet text are included so you can adapt page sizes, labels and fields.
