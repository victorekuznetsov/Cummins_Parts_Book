---
aliases:
  - "Идентификация шин данных SAE J1939"
type: "TSB"
doc: "tsb110086"
title_en: "Identification of SAE J1939 Datalinks"
title_ru: "Идентификация шин данных SAE J1939"
released: "2011-03-23"
modified: "2011-03-24"
group: "19 - Electronic Engine Controls"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "QSK60"
  - "QSM11"
  - "QSX15"
figures: 3
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110086.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110086.pdf"
tags:
  - "документ/tsb"
  - "двигатель/C8.3"
  - "двигатель/QSK60"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "год/2011"
  - "тема/electronic-engine-controls"
---

# Identification of SAE J1939 Datalinks
**Идентификация шин данных SAE J1939**

> [!abstract] TSB · `tsb110086`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, QSK60, QSM11, QSX15
> **Даты:** выпущен 2011-03-23 · изменён 2011-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110086.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110086.pdf)

## Identification of SAE J1939 Datalinks

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

This document was originally released between 1994 and 2001. It has been added to QSOL for informational purposes

This document provides information for identifying what type of SAE J1939 datalink is on an engine.

In all the following cases, standard communication cable, Part Number 3162847, will need to be connected to the INSITE™ adapter.

![[19802394.png]]

SAE J1939 is an OEM option on ISM and ISX engines.

If the OEM has supplied a SAE J1939 datalink, a triangular Deutsch 3–pin connector will be found within 0.66 m \[2.16 ft\] of the engine ECM. If this datalink is a receptacle (female connector), the harness does **not** have a backbone; A minibackbone adapter cable (illustrated), Part Number 3163096, is needed between the communication cable and the datalink in order to communicate.

![[19803444.png]]

If the datalink is a plug (male connector), the resistance between pins A and B **must** to be measured.

If the resistance value is 60 ohms, the backbone is installed and the minibackbone cable is **not** needed.

If the resistance across the pins is greater than 100k ohms, a backbone has **not** been installed and cable, Part Number 3163597, is needed in addition to the minibackbone adapter cable, Part Number 3163096.

> [!note] Note · Примечание
> Disconnect the 50–pin OEM harness from the engine ECM before performing the resistance check.

![[19802397.png]]

If the resistance across pins A and B is 120 ohms, one of the termination resistor caps (1) is missing in the OEM wiring harness plugs (2) and **must** be replaced for correct communication on the datalink.

### Document History
