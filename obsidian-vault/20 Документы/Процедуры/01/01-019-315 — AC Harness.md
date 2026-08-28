---
aliases:
  - "Жгут переменного тока"
type: "Процедура"
doc: "01-019-315"
title_en: "AC Harness"
title_ru: "Жгут переменного тока"
modified: "2003-06-30"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 11
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-315.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-315.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# AC Harness
**Жгут переменного тока**

> [!abstract] Процедура · `01-019-315`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-315.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-315.pdf)

### General Information

The AC harness carries the voltage and current sensing signals into the PT/CT board, carries the PMG excitation voltage to the voltage regulator, and then carries the field excitation from the voltage regulator back to the alternator.

The AC harness is located in the controls box and extends out over the alternator.

![[nobox.png]]

### Remove

Disconnect wires P2, P3, and P4 from the PMG connector wires.

Disconnect wires F1 and F2 from field wiring to alternator.

![[19802831.png]]

Disconnect wiring to each current transformer. Remove nuts and lock washer. Each current transformer will have a CT and a CT COM (common) wire that **must** be removed.

![[19802832.png]]

Disconnect voltage sensing wiring GEN L1, L2, L3, and NEUTRAL from output leads.

![[19802839.png]]

Disconnect 12-pin AMP connector 09 from the PT/CT board.

![[19802840.png]]

Disconnect 6-pin AMP connector 10 from the voltage regulator.

Remove any harness supports.

Slowly pull the AC harness out of the controls box, making sure there is no binding or tangling.

![[19802833.png]]

### Install

> [!note] Note · Примечание
> On some generator sets, installation can vary.

Route the AC harness through the back of the controls box so that the alternator and PMG connections are close to the output leads.

Feed the other end of the harness with connections 09 and 10 into the controls box and down and behind the terminal blocks.

Connect 6-pin AMP connector 10 to the voltage regulator.

![[19802833.png]]

Connect 12-pin AMP connector 09 to the PT/CT board.

![[19802840.png]]

Connect voltage sensing wiring GEN, L1, L2, L3, and NEUTRAL to output leads.

![[19802839.png]]

Connect wiring to each current transformer. Install nut and lock washer. Each current transformer will have a CT and a CT COM (common) wire that **must** be installed.

![[19802832.png]]

Connect wires P2, P3, and P4 to the PMG connector wires.

Connect wires F1 and F2 to the alternator field wiring connectors.

![[19802831.png]]
