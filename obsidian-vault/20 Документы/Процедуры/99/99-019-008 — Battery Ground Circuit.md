---
aliases:
  - "Цепь массы аккумуляторной батареи"
type: "Процедура"
doc: "99-019-008"
title_en: "Battery Ground Circuit"
title_ru: "Цепь массы аккумуляторной батареи"
modified: "2012-03-21"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "35354607"
  - "35373113"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
  - "71156161"
  - "80141463"
  - "80248213"
  - "85017333"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "K19"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK23"
  - "QSK60"
  - "QSM11"
  - "QST30"
  - "QSX15"
manuals:
  - "3666070"
  - "3666113"
  - "3666184"
  - "3666214"
  - "3666231"
  - "3666266"
  - "3666410"
  - "3666415"
  - "4021419"
  - "4021442"
  - "4021674"
figures: 3
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-008.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-008.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/K19"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QSM11"
  - "двигатель/QST30"
  - "двигатель/QSX15"
  - "группа/99"
---

# Battery Ground Circuit
**Цепь массы аккумуляторной батареи**

> [!abstract] Процедура · `99-019-008`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, K19, NT/NTA855 · ISM/QSM11, QSK23, QSK60, QSM11, QST30, QSX15
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]], [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666231 — Centinel™ Master Repair Manual|3666231]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]], [[3666415 — ICON Idle Control System Master Repair Manual|3666415]], [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19 · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2012-03-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-008.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-008.pdf)

### Resistance Check

Check the Original Equipment Manufacturer harness ground connection for loose, corroded, or broken connections.

![[19803965.png]]

> [!warning] CAUTION · Осторожно
> The leads must fit tightly in the connector without expanding the pins in the connector otherwise the connector will be damaged.

Measure the resistance between the battery supply negative (-) pin of the Original Equipment Manufacturer harness control module connector(s) and engine block ground or chassis ground for each control module. Reference the wiring diagram for connector pin identification. The resistance **must** be 10 ohms or less.

![[19c01148.png]]

If the resistance value is **not** correct, check the batteries, cables, and cable connections.

Repair or replace the parts as required.

![[ee8cos38.png]]
