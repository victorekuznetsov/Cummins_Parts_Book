---
type: "Процедура"
doc: "81-019-081"
title_en: "Sensor Wiring Harness"
modified: "2007-10-30"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 51
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-081.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-081.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# Sensor Wiring Harness

> [!abstract] Процедура · `81-019-081`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2007-10-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-081.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-081.pdf)

### General Information

CENSE™-equipped engines use three separate wiring harnesses:

- CENSE™ harness, main/left bank sensors

![[19802602.png]]

- CENSE™ harness, right bank sensors

![[19802606.png]]

- J1939 communication harness (backbone harness).

![[19802603.png]]

### Remove

Left Bank

Remove the left bank harness covers.

![[19601202.png]]

Disconnect the main/left bank CENSE™ harness from the oil temperature sensor (1).

![[19801294.png]]

Disconnect the 23-pin OEM harness connector.

![[19800837.png]]

Disconnect the 40-pin A and B ECM connectors.

![[19800828.png]]

Disconnect the 23-pin and the 33-pin right bank sensor harness connectors.

![[19800847.png]]

Disconnect all of the left bank exhaust temperature sensors.

![[19801442.png]]

Disconnect the left bank rear turbocharger compressor inlet temperature sensor.

![[19800845.png]]

Disconnect the 2-pin left bank rear intake manifold temperature sensor.

![[19400436.png]]

Disconnect the engine block ground from the engine block. There may be one or more ring terminals to disconnect.

> [!note] Note · Примечание
> Some harnesses have one common ground.

![[19400393.png]]

Disconnect the QSK45/60 2-way interharness connector (data link) from the engine control system harness.

- Remove the capscrews.
- Slide the data link connector out of the mounting slot in the bracket.

> [!note] Note · Примечание
> The bracket may differ from the illustration.

![[19801069.png]]

Disconnect the RS232 3-pin data link connector from the support bracket.

![[19801208.png]]

Disconnect the warning lamps connector from the QSK45/60 lamp connector.

![[19a00484.png]]

Disconnect the 3-pin Deutsch™ J1939 data link from the communication harness (backbone).

![[19802604.png]]

Disconnect the 6-pin Deutsch™ connectors from the QSK45/60 6-way interharness connectors.

![[19801070.png]]

Remove the main/left bank harness (1) and backbone harness (2) from the support bracket.

Cut all of the nylon wire ties from the CENSE™ main/left bank harness.

Remove the harnesses from the support brackets.

![[19601203.png]]

Remove the harness support brackets.

![[19601204.png]]

Right Bank

Remove the right bank harness covers.

![[19601205.png]]

Disconnect the 23-pin and the 33-pin Deutsch™ connectors on the right bank sensor harness.

![[19800838.png]]

Disconnect the pre-filter lubricating oil pressure sensor and the post-filter lubricating oil pressure sensor.

> [!note] Note · Примечание
> This step **only** applies for engines with pre-filter and post-filter lubricating oil pressure sensors on the right bank.

![[19800840.png]]

Disconnect all of the right bank exhaust temperature sensors.

![[19801442.png]]

Disconnect the right bank front and right bank rear intake manifold temperature sensor 2-pin connectors.

![[19400436.png]]

Disconnect the right bank boost pressure sensor 3-pin connector.

The right bank boost pressure sensor is located in the right bank rear intake manifold.

![[19400452.png]]

Remove the harness t-pieces and p-clips from the support brackets.

Cut all of the nylon wire ties from the CENSE™ right bank harness.

![[19601206.png]]

Remove the right bank harness support brackets.

![[19601207.png]]

### Install

Left Bank

Attach the harness support brackets to the intake manifolds in the locations shown.

Apply Loctite® 243, or equivalent, to the capscrews.

Insert and tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 23 n•m [204 in-lb]

![[19601204.png]]

Attach the main/left bank harness (1) and backbone harness (2) to the support bracket. Insert the mounting nuts and tighten.

> [!tip] Момент затяжки · Torque Value
> 10 n•m [89 in-lb]

Use nylon wire ties, where required, to secure the harness to the engine.

![[19601203.png]]

> [!warning] CAUTION · Осторожно
> Use only Cummins®-recommended lubricant DS-ES, Part Number 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector wear.

Apply a small amount of lubricant to the connector terminals. Before installing, fill the entire connector cavity with lubricant.

Lubricate all harness connectors.

![[cel28.png]]

Install the 23-pin and the 33-pin right bank sensor harness connectors on the mounting plate.

> [!tip] Момент затяжки · Torque Value
> 20 n•m [177 in-lb]

Connect the 23-pin and the 33-pin connectors.

![[19800847.png]]

Connect the 40-pin A and B ECM connectors.

![[19800828.png]]

Connect the 2-pin left bank rear intake manifold temperature sensor.

![[19400436.png]]

Connect all of the left bank exhaust temperature sensors.

[[81-019-013 — Exhaust Temperature Sensor|Refer to Procedure 019-013 (Exhaust Temperature Sensor) in Section 19.]]

![[19801442.png]]

Install the RS232 3-pin data link connector into the support bracket.

![[19801208.png]]

Connect the left bank rear turbocharger compression inlet temperature sensor.

![[19800845.png]]

Connect the 23-pin OEM harness connector.

![[19800837.png]]

Connect the 6-pin Deutsch™ connectors to the QSK45/60 6-way interharness connectors.

![[19801073.png]]

Connect the 3-pin Deutsch™ J1939 data link to the communication harness (backbone).

![[19802604.png]]

Connect the warning lamp connector to the QSK45/60 lamp connector.

![[19a00484.png]]

Connect the QSK45/60 2-way interharnsss connector (data link).

- Slide the connector into the support bracket.
- Secure the connector with screws.

> [!tip] Момент затяжки · Torque Value
> 1.2 n•m [11 in-lb]

> [!note] Note · Примечание
> The bracket may differ from the illustration.

![[19802605.png]]

Connect the oil temperature sensor (1).

![[19801294.png]]

Attach the left bank harness covers.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[19601202.png]]

Right Bank

Attach the harness support brackets to the intake manifolds in the locations shown.

Apply Loctite® 243, or equivalent, to the capscrews.

Insert and tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 23 n•m [204 in-lb]

![[19601207.png]]

Attach the harness t-pieces and p-clips to the support brackets.

> [!tip] Момент затяжки · Torque Value
> 10 n•m [89 in-lb]

Insert the mounting nuts and tighten.

Use nylon wire ties, where required, to secure the harness to the engine.

![[19601206.png]]

Connect the pre-filter lubricating oil pressure sensor and the post-filter lubricating oil pressure sensor.

![[19800840.png]]

Connect the 23-pin and the 33-pin Deutsch™ connectors on the right bank sensor harness.

![[19800838.png]]

Connect the right bank boost pressure sensor 3-pin connector, located in the right bank rear intake manifold.

![[19400452.png]]

Connect the right bank front and the right bank rear intake manifold temperature sensor 2-pin connectors.

![[19400436.png]]

Connect the right bank exhaust temperature sensors.

[[81-019-013 — Exhaust Temperature Sensor|Refer to Procedure 019-013 (Exhaust Temperature Sensor) in Section 19.]]

![[19801442.png]]

Attach the right bank harness covers.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[19601205.png]]
