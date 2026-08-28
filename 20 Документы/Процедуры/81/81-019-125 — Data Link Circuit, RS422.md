---
type: "Процедура"
doc: "81-019-125"
title_en: "Data Link Circuit, RS422"
modified: "2003-08-26"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 17
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-125.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-125.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# Data Link Circuit, RS422

> [!abstract] Процедура · `81-019-125`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-125.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-125.pdf)

### General Information

The RS422 datalink circuit is used by vehicle systems to communicate with the CENSE™ ECM.

![[cent337.png]]

### Resistance Check

Remove the CENSE™ harness ECM A connector from the ECM. Refer to Procedure 019-043. Disconnect the OEM harness from the CENSE™ 23-pin OEM connector.

Use test leads, Part No. 3822758, on the ECM connector and Part No. 3824811 on the 23-pin Deutsch connector. Turn the keyswitch OFF.

Measure the resistance from pin 23 of the engine harness connector to pin C of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400593.png]]

Measure the resistance from pin 24 of the CENSE™ harness connector to pin F of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400594.png]]

Measure the resistance from pin 28 of the CENSE™ harness connector to pin D of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400595.png]]

Measure the resistance from pin 29 of the CENSE™ harness connector to pin E of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

If all measurements are within specifications, the OEM harness **must** be checked. Refer to the OEM manual.

![[19400596.png]]

### Check for Short Circuit to Ground

Turn the keyswitch OFF. Disconnect the 23-pin Deutsch OEM connector. Disconnect the ECM A and B connectors.

Use test lead Part No. 3824811 for the 23-pin Deutsch connector.

Measure the resistance from pin C of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400597.png]]

Measure the resistance from pin D of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400598.png]]

Measure the resistance from pin E of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400599.png]]

Measure the resistance from pin F of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400600.png]]

### Check for Short Circuit from Pin to Pin

**Deutsch Connector**

Turn the keyswitch OFF. Disconnect the 23-pin Deutsch connector from the OEM harness.

Use test lead, Part No. 3824811, for the 23-pin Deutsch connector.

Measure the resistance from pin C to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400601.png]]

Measure the resistance from pin D to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400602.png]]

Measure the resistance from pin E to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400603.png]]

Measure the resistance from pin F to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

If all measurements are within specifications, the OEM harness **must** be checked for a short circuit from pin to pin. Refer to the OEM manual.

![[19400604.png]]

### Voltage Check

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test lead, Part No. 3824811.

Disconnect the 23-pin Deutsch connector from the OEM harness.

Select the VDC function on the multimeter. Turn the keyswitch ON.

Measure the voltage from pin D of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show 0 to 3 VDC.

![[19400605.png]]

Measure the voltage from pin F of the 23-pin Deutsch connector to the engine block ground.

The multimeter **must** show 0 to 3 VDC.

![[19400606.png]]

Measure the voltage from pin C to pin D on the 23-pin Deutsch connector.

The multimeter **must** show 0 to 3 VDC.

![[19400607.png]]

Measure the voltage from pin E to pin F on the 23-pin Deutsch connector.

The multimeter **must** show 2 to 8 VDC.

If all measurements are within specifications, the OEM harness **must** be checked. Refer to the OEM manual.

![[19400608.png]]
