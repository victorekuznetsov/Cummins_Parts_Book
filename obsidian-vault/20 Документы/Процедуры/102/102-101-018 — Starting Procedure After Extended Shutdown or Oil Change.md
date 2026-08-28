---
aliases:
  - "Порядок пуска после длительной стоянки или замены масла"
type: "Процедура"
doc: "102-101-018"
title_en: "Starting Procedure After Extended Shutdown or Oil Change"
title_ru: "Порядок пуска после длительной стоянки или замены масла"
modified: "2015-03-15"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41349633"
  - "41353297"
  - "85017333"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QSK23"
  - "QSK60"
  - "QST30"
manuals:
  - "3666120"
  - "3666134"
  - "3666260"
  - "3810497"
  - "4021374"
  - "4915528"
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/102/102-101-018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/102-101-018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "группа/102"
---

# Starting Procedure After Extended Shutdown or Oil Change
**Порядок пуска после длительной стоянки или замены масла**

> [!abstract] Процедура · `102-101-018`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19, QSK23, QSK60, QST30
> **Входит в руководства:** [[3666120 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Operation and Maintenance Manual|3666120]], [[3666134 — QST30 Operation and Maintenance Manual|3666134]], [[3666260 — QSK45 and QSK60 Operation and Maintenance Manual|3666260]], [[3810497 — K38, K50, QSK38 and QSK50 Operation and Maintenance Manual|3810497]], [[4021374 — QSK23 Operation and Maintenance Manual|4021374]], [[4915528 — QSK45 and QSK60 Owners Manual|4915528]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2015-03-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/102/102-101-018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/102-101-018.pdf)

### General Information

> [!warning] CAUTION · Осторожно
> Do not allow the engine to run out of fuel. A loss of fuel supply can cause damage to the fuel pump and injectors

> [!note] Note · Примечание
> This procedure will cause fault codes for the unplugged sensors to be logged. They will go inactive and have no effect on engine operation after the sensors are connected.

> [!note] Note · Примечание
> This procedure is intended to be used on engines **not** equipped with a Prelub™ system to make sure all engine components receive adequate oil supply prior to the engine being started. A Prelub™ system accomplishes this automatically regardless of oil change, or extended shutdown.

The following steps **must** be completed after each oil change or after the engine has been shut off for more than 5 days to be sure the engine receives the correct oil flow through the lubricating oil system, and fuel system components have adequate fuel supply for lubrication.

- Disconnect the engine speed sensor and the camshaft position sensor. Engines with mechanical injectors have **only** the engine speed sensor.
- For engines with Modular Common Rail System (MCRS) fuel systems, cycle the keyswitch ON and allow the fuel priming pump to operate for 2 minutes. Repeat this step one time to make sure the fuel system is fully primed.
- Use the starting motor to rotate the crankshaft until the oil pressure is indicated on the gauge or the warning light goes out.

![[14400007.png]]

Connect the sensors.

Start the engine.

> [!note] Note · Примечание
> For engines with MCRS fuel systems which fail to start after completing the above steps, the fuel system may be air-locked or require additional priming. Go to the Prime section in Procedure 006-075 in Section 4 of the appropriate Operation and Maintenance Manual for more information on priming the fuel system.

- Use the following procedure for the QSK19 engine. [[00-101-014-om-ind — Normal Starting Procedure|Refer to Procedure 101-014 in Section 1.]]
- Use the following procedure for the QSK45 and QSK60 engines. [[56-101-014 — Normal Starting Procedure|Refer to Procedure 101-014 in Section 1.]]
- Use the following procedure for the QSK78 engine. Refer to Procedure 101-014 in Section 1.
- Use the following procedure for the QSK78 K104 engine. Refer to Procedure 101-014 in Section 1.

![[19400429.png]]
