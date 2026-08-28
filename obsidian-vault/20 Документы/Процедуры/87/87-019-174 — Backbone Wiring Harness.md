---
aliases:
  - "Магистральный жгут проводов"
type: "Процедура"
doc: "87-019-174"
title_en: "Backbone Wiring Harness"
title_ru: "Магистральный жгут проводов"
modified: "2003-02-10"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 14
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-174.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-174.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Backbone Wiring Harness
**Магистральный жгут проводов**

> [!abstract] Процедура · `87-019-174`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-174.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-174.pdf)

### General Information

The J1939 backbone harness connects the left- and right-bank ECMs in addition to providing a service tool interface connector.

![[19a00542.png]]

The J1939 backbone harness is required to have two terminating resistors (120 ohms each) in parallel with the J1939 datalink positive (+) and J1939 datalink negative lines. These terminating resistors are on each end of the backbone harness.

![[19a00728.png]]

In addition, the backbone harness is shielded to reduce electrical interference on the datalink. This shielded line is grounded to the engine block.

![[19a00545.png]]

The QST30 backbone harness consists of four interface connectors, which are triangular 3-pin Deutsch plugs. One of the plug connectors is inserted into the left-bank engine harness and one is inserted into the right-bank harness. The other two are capped and provide the service tool interface connection (one on each bank).

The QST30 backbone harness also consists of two terminating resistor plugs. The resistors are inserted into the cap and connect through to the datalink circuit when plugged into a terminal.

![[19a00542.png]]

To determine if a capped plug is a service tool interface plug or a terminating resistor plug, remove the cap and examine the inside. The terminating resistor caps are blue in color, with two pins visible on the inside.

The service tool interface terminal caps are orange in color and have no pins in the cap. This is the proper place to connect the service tool to communicate with the ECMs.

> [!note] Note · Примечание
> By plugging into either of the two service tool interface connectors, you have communication with both ECMs, left- and right-bank.

![[19802397.png]]

The two 6-pin engine-side datalink connectors are **not** used with the service tool. They are J1587/1708 datalink ports and are **only** used for a generic tool. INSITE™ for QST30 engines requires a J1939 communication protocol with an INLINE II adapter.

On engines with a 9-pin engine-side datalink connector, the service tool interface terminals on the J1939 backbone have been removed. Use this 9-pin datalink connector with the service tool to communicate with both ECMs.

> [!note] Note · Примечание
> Engines with two round 6-pin Deutsch connectors **must** use the triangular 3-pin Deutsch service tool interface connector. The 6-pin connectors will **not** work with the INSITE™ service tool.

![[19802393.png]]

### Remove

Disconnect the 3-pin J1939 backbone harness connectors from the J1939 datalink harness.

![[19a00546.png]]

Disconnect the engine block ground from the block.

![[19a00545.png]]

Cut the ties on the J1939 backbone harness.

Remove the J1939 backbone harness from the engine.

![[19a00547.png]]

### Inspect for Reuse

Repair or replace the engine harness if there is an open circuit or a short circuit found under the protective covering of the harness body.

![[19a00542.png]]

### Install

Install the J1939 backbone harness onto the engine.

![[19a00542.png]]

Connect the 3-pin J1939 backbone harness connectors to the left- and right-bank harnesses.

![[19a00546.png]]

Connect the engine block ground to the block.

![[19a00545.png]]

Secure the J1939 backbone harness to the engine using coated wire ties.

![[19a00547.png]]
