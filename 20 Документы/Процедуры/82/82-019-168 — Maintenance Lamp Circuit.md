---
aliases:
  - "Цепь лампы напоминания об обслуживании"
type: "Процедура"
doc: "82-019-168"
title_en: "Maintenance Lamp Circuit"
title_ru: "Цепь лампы напоминания об обслуживании"
modified: "2005-01-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 4
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-168.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-168.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Maintenance Lamp Circuit
**Цепь лампы напоминания об обслуживании**

> [!abstract] Процедура · `82-019-168`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-168.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-168.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test lead Part Number 3822758.

Turn the vehicle keyswitch to the OFF position. Disconnect the OEM harness connector from the ECM. Disconnect the OEM harness at the main dashboard connector (driver interface panel) beyond the bulkhead connector, in the vehicle cab.

> [!note] Note · Примечание
> Depending on the OEM and the vehicle, the wiring could be run to individual switches instead of a main multi-pin connector. Check the OEM troubleshooting and repair manual for procedures.

![[19200217.png]]

Measure the resistance from pin 5 of the OEM harness connector to the back of the lamp.

The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure 019-071.

![[19200217.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test lead Part Number 3822758.

Turn the vehicle keyswitch to the OFF position. Disconnect the OEM harness connector from the ECM. Disconnect the OEM harness at the main dashboard connector (driver interface panel), beyond the bulkhead connector, in the vehicle cab.

> [!note] Note · Примечание
> Depending on the OEM and the vehicle, the wiring could be run to individual switches, instead of a main multi-pin connector. Check the OEM troubleshooting and repair manual for procedures.

Measure the resistance from pin 5 of the OEM harness connector to the engine block ground.

The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, repair or replace the OEM harness. Refer to Procedure 019-071.

![[19c00891.png]]

### Voltage Check

Turn the vehicle keyswitch to the ON position.

Adjust the multimeter to measure voltage. Touch the positive (+) multimeter probe to the buzzer or lamp terminal and the negative (-) multimeter probe to chassis ground.

Measure the voltage. The multimeter **must** show battery voltage. If the proper voltage is **not** present, there is a problem with the keyswitch wire or the lamp (or buzzer) has failed. Refer to the OEM troubleshooting and repair manual for repair procedures.

Repeat this check for the other terminal of the buzzer or fault lamp.

![[19200217.png]]
