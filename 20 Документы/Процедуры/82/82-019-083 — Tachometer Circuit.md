---
aliases:
  - "Цепь тахометра"
type: "Процедура"
doc: "82-019-083"
title_en: "Tachometer Circuit"
title_ru: "Цепь тахометра"
modified: "2002-06-27"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 6
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-083.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-083.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Tachometer Circuit
**Цепь тахометра**

> [!abstract] Процедура · `82-019-083`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-083.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-083.pdf)

### General Information

The ECM can supply an output signal to operate the vehicle tachometer. The circuit is the output signal, wire No. 11, and a tachometer internal ground in the OEM harness.

![[19c00345.png]]

### Resistance Check

Disconnect the OEM harness connector from the ECM. Disconnect the tachometer from the OEM harness.

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part No. 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the connector pins.

Insert one test lead into pin 11 of the OEM harness connector and connect the test lead to the multimeter probe.

![[19c00346.png]]

Locate the tachometer connector in the OEM harness.

Connect the other test lead to the other multimeter probe and touch it to the appropriate tachometer connector pin. Consult the OEM troubleshooting and repair manual for wiring schematics.

Set the multimeter to the resistance setting and measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, there is an open circuit or the wires in the tachometer connector are reversed. Repair or replace the wire connected to pin 11 in the OEM harness according to the vehicle manufacturer's procedures.

![[19c00347.png]]

### Check for Short Circuit to Ground

Disconnect the tachometer from the OEM harness.

Insert the test lead into pin 11 of the OEM harness connector, and connect it to the multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open in either of the previous tests, repair the wires which have incorrect readings, according to the vehicle manufacturer's procedures.

![[19c00342.png]]

### Check for Short Circuit from Pin to Pin

Disconnect the tachometer from the OEM harness.

Insert the test lead into pin 11 of the OEM harness connector, and connect it to the multimeter probe. Insert the other test lead into pin 10 of the OEM harness connector and attach it to the other probe. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19200334.png]]

Remove the multimeter lead from pin 10, and test all pins in the connector. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) at all pins. If the multimeter registers a closed circuit at any pin, a short circuit exists between pin 11 and that pin.

Repair the OEM harness. Refer to Procedure 019-250.

![[19c00344.png]]
