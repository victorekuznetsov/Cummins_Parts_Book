---
aliases:
  - "Печатная плата ЭБУ"
type: "Процедура"
doc: "01-019-322"
title_en: "ECM Circuit Board"
title_ru: "Печатная плата ЭБУ"
modified: "2003-06-30"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 7
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-322.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-322.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# ECM Circuit Board
**Печатная плата ЭБУ**

> [!abstract] Процедура · `01-019-322`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-322.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-322.pdf)

### General Information

The ECM circuit boards are located in the card cage inside the controls box. The generator set will have at least three boards, the fuel board, base board, and genset board. Both the paralleling board and LonWorks® board are optional.

![[19802869.png]]

### Remove

Base board (other boards similar).

Disconnect the 50-pin D-sub connector from the board.

Disconnect the 25-pin D-sub connector from the board (base board **only**).

![[19802661.png]]

Unscrew the mounting screw at each end of the terminal block. Pull the terminal block off the circuit board. The terminal block wiring does **not** need to be disconnected. (Fuel board does **not** have terminal block.)

![[19802835.png]]

Loosen the screw at each end of the board.

Pull the circuit board straight up until it is free from the card cage. Remove the circuit board.

![[19803034.png]]

### Install

Base board (other boards similar).

Holding the board directly above the slot, align the back edge of the board with the alignment groove in the back of the card cage.

Slowly drop the board down so that the back edge of the board fits inside the alignment groove on the back of the card cage. Slide the board down and into the backplane connector at the bottom of the card cage.

Make sure the board is mounted flush with the top surface of the card cage, and with the other circuit boards. Tighten down the screw on each end of the circuit board.

![[19803034.png]]

Locate the terminal block in position onto the circuit board. Tighten down the mounting screw at each end of the terminal block. (Fuel board does **not** have terminal blocks.)

![[19802835.png]]

Connect the 25-pin D-sub connector to the board. (Base board only.)

Connect the 50-pin D-sub connector to the board.

Connect the electronic service tool and check for any active fault codes.

![[19802661.png]]
