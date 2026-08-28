---
type: "Процедура"
doc: "300-015-172"
title_en: "Redundant Power Selector"
modified: "2019-09-17"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4332828"
figures: 3
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-015-172.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-015-172.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
---

# Redundant Power Selector

> [!abstract] Процедура · `300-015-172`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2019-09-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-015-172.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-015-172.pdf)

### General Information

The redundant power selector is a power distributor for both the primary and secondary power supply. Its purpose is to effortlessly switch between the primary and secondary power source to provide a constant output voltage. It can communicate with the vessel operator to notify when the power source has changed between the two sources.

![[19c91607.png]]

### Remove

Disconnect all wires connected to the redundant power selector.

Use a flathead screwdriver to pull the latch away from the redundant power selector.

Rotate the redundant power selector upward.

Remove the redundant power selector.

![[19c91608.png]]

### Install

Place the redundant power selector in location to be installed.

Hook the redundant power selector onto the din rail.

Rotate the redundant power selector toward the din rail and press firmly to lock the redundant power selector into position. A click will be heard when the redundant power selector locks in place.

Connect all wiring to the redundant power selector.

![[19c91609.png]]

When replacing the power switch relay with the redundant power selector, the labeled wires will need to be placed in the appropriate locations. See the table below.

| Redundant Power Selector Pin Numbering |  |  |
|---|---|---|
| Pin Number | Description | Wire |
| 1 | Primary 24 volts direct current (VDC) | 14 |
| 2 | Primary 0 VDC | 24 |
| 3 | Not used |  |
| 4 | Non used |  |
| 5 | Not used |  |
| 6 | Secondary 24 VDC | 12 |
| 7 | Secondary 0 VDC | 22 |
| 11 | Not used |  |
| 12 | Not used |  |
| 13 | Not used |  |
| 14 | Not used |  |
| 15 | Not used |  |
| 16 | Power out 0 VDC | 21 |
| 17 | Power out 24 VDC | 11 |

Wires labeled A1 and A2 will **not** be used with the redundant power selector.
