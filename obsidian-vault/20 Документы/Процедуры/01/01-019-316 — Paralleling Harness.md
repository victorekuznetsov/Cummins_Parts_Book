---
aliases:
  - "Жгут параллельной работы"
type: "Процедура"
doc: "01-019-316"
title_en: "Paralleling Harness"
title_ru: "Жгут параллельной работы"
modified: "2003-06-30"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 13
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-316.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-316.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Paralleling Harness
**Жгут параллельной работы**

> [!abstract] Процедура · `01-019-316`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-316.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-316.pdf)

### General Information

The paralleling harness is used when the generator set is in a paralleling application with other generator sets. The paralleling harness connects the parallel board with the PT/CT board, the bus PT module, power distribution module, and several terminal blocks at TB3 for customer connections.

![[19802742.png]]

### Remove

Disconnect the 50-pin D-sub connector 04 from the parallel board in the card cage.

![[19802661.png]]

> [!note] Note · Примечание
> Some QSK60 generator sets will **not** have this power module and connector.

Disconnect the 4-pin AMP connector 27 from the power module in the controls box.

![[19802819.png]]

Disconnect the 23-pin AMP connector 08 from the PT/CT board.

There will also be another 23-pin AMP connector 08 from the generator control harness that will remain unused.

![[19802834.png]]

Remove the paralleling harness wiring from the bus PT module at TB2.

Remove each of the six wires by loosening the corresponding screw on the bus PT module.

![[19802826.png]]

Remove customer wiring to TB3 from terminal blocks 21 to 32.

Remove TB3 terminal blocks 21 to 32.

Remove the screw in the lower clip that holds the lower terminal blocks in place. Remove the clip.

![[19802823.png]]

Slide the terminal blocks down and off the terminal rail. **Only** remove terminal blocks that are part of the paralleling harness.

Remove any harness supports.

Make sure that all connections made by the paralleling harness are disconnected and untangled.

Slowly pull the paralleling harness out of the controls box, making sure that there is no binding or tangling.

![[19802824.png]]

### Install

Replace any harness support brackets.

Route the harness through the necessary supports and routing locations.

Install TB3 terminal blocks 21 to 32.

Slide the terminal blocks up and onto the terminal rail.

![[19802824.png]]

Install the lower clip and tighten the screw to hold the terminal blocks in place.

Install customer wiring to appropriate terminal blocks on TB3.

![[19802823.png]]

Install the paralleling harness wiring to the bus PT module at TB2.

Install each of the six wires by tightening down the corresponding screw on the bus PT module.

![[19802826.png]]

Connect the 23-pin AMP connector 08 to the PT/CT board.

Be careful **not** to connect the identical 23-pin AMP connector 08 from the generator control harness. This connector will **not** be used when the paralleling harness is being used.

![[19802834.png]]

> [!note] Note · Примечание
> Some QSK 60 generator sets will **not** have this power module and connector.

Connect the 4-pin AMP connector 27 to the power module in the controls box.

![[19802819.png]]

Connect the 50-pin D-sub connector 04 to the parallel board in the card cage. Tighten down jackscrews.

Double-check that all paralleling control harness connections are secure.

Connect the electronic service tool and check for any fault codes.

![[19802661.png]]
