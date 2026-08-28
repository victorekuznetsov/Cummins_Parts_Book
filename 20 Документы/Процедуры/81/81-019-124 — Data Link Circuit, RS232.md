---
type: "Процедура"
doc: "81-019-124"
title_en: "Data Link Circuit, RS232"
modified: "2003-08-26"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 21
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-124.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-124.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# Data Link Circuit, RS232

> [!abstract] Процедура · `81-019-124`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-124.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-124.pdf)

### General Information

The RS232 datalink circuit is used by INSITE™ for CENSE™ to communicate with the CENSE™ ECM.

![[19a00042.png]]

The datalink uses a 3-pin Deutsch connector. The wiring positions follow:

1. Pin A: - Ground
2. Pin C: - Datalink Transmit (Tx)
3. Pin B: - Datalink Receive (Rx)
4. Key

The procedures that follow cover the cab-located datalink connector and the engine-side datalink connector.

![[19801472.png]]

### Resistance Check

**Engine Located CENSE™**

Disconnect the OEM harness from the CENSE™ 23-pin OEM connector. Remove the engine-located CENSE™ harness ECM A and B connectors from the ECM. Refer to Procedure 019-043.

Use test leads, Part No. 3822758, on the ECM connector and Part No. 3824811, on the 23-pin Deutsch connector. Turn the keyswitch OFF.

Measure the resistance from pin 33 of the CENSE™ harness ECM A connector to pin L of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400570.png]]

Measure the resistance from pin 22 of the CENSE™ harness ECM A connector to pin M of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400571.png]]

Measure the resistance from pin 13 of the CENSE™ harness ECM B connector to pin N of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure 019-043. If all measurements are within specifications, the OEM harness **must** still be checked. Refer to the OEM manual.

![[19400572.png]]

Disconnect the OEM harness from the CENSE™ 23-pin OEM connector. Remove the engine-located CENSE™ harness ECM A and B connectors from the ECM. Refer to Procedure 019-043.

Use test leads, Part No. 3822758, on the ECM connector and, Part No. 3824811, on the 3-pin Deutsch connector. Turn the keyswitch OFF.

Measure the resistance from pin 33 of the CENSE™ harness ECM A connector to pin C of the 3-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400629.png]]

Measure the resistance from pin 22 of the CENSE™ harness ECM A connector to pin B of the 3-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400630.png]]

Measure the resistance from pin 13 of the CENSE™ harness ECM B connector to pin A of the 3-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure 019-043.

If all measurements are within specifications, the OEM harness **must** still be checked. Refer to the OEM manual.

![[19400631.png]]

### Check for Short Circuit to Ground

**Cab-Located CENSE™**

Use test lead, Part No. 3824811, for the cab located 23-pin Deutsch connector. Disconnect the 23-pin Deutsch OEM connector. Disconnect the ECM A and B connectors.

Measure the resistance from pin L of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400575.png]]

Measure the resistance from pin M of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400576.png]]

Measure the resistance from pin N of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (10 ohms or less).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400577.png]]

**Engine-Located CENSE™**

Use test lead, Part No. 3824811, for the engine-located 3-pin Deutsch connector. Disconnect the ECM A and B connectors.

Measure the resistance from pin A of the 3-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (10 ohms or less).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400628.png]]

Measure the resistance from pin B of the 3-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400626.png]]

Measure the resistance from pin C of the 3-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19400627.png]]

### Check for Short Circuit from Pin to Pin

**Engine Harness Connector**

Disconnect the CENSE™ 40-pin A and B Deutsch connectors from the ECM. Disconnect the 31-pin and 23-pin OEM connectors from the OEM harness.

Use test lead, Part No. 3822758, for the CENSE™ ECM 40-pin Deutsch connectors. Measure the resistance from pin 33 of the ECM B connector to all other pins in the ECM B connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19a00534.png]]

Now measure the resistance from pin 33 of the ECM B connector to all pins **in the ECM A connector**. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19a00534.png]]

Measure the resistance from pin 22 of the ECM A connector to all other pins in the ECM A connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.

![[19a00535.png]]

### Voltage Check

Locate the datalink connector on the CENSE™ harness.

The datalink connector is shown.

![[19400623.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test lead, Part No. 3824811.

Select the VDC function on the multimeter.

Measure the voltage from pin C of the 3-pin Deutsch connector to pin A. The multimeter **must** show -10.0 VDC (minimum -8.5 to maximum -11.0 VDC).

If no voltage is present, the datalink circuit **must** be checked for an open circuit. Verify that the battery voltage is correct.

![[19a00536.png]]

Measure the voltage from pin B of the 3-pin Deutsch connector to pin A.

The multimeter **must** show 0 VDC. If a voltage is present, the datalink **must** be checked for a short circuit from pin to pin.

![[19a00537.png]]

Measure the voltage from pin A of the 3-pin Deutsch connector to the engine block.

The multimeter **must** show 0 VDC.

![[19a00538.png]]
