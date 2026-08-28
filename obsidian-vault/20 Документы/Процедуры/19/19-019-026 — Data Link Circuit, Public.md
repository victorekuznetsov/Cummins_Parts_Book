---
aliases:
  - "Цепь общедоступной шины данных"
type: "Процедура"
doc: "19-019-026"
title_en: "Data Link Circuit, Public"
title_ru: "Цепь общедоступной шины данных"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 21
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Data Link Circuit, Public
**Цепь общедоступной шины данных**

> [!abstract] Процедура · `19-019-026`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-026.pdf)

### General Information

The public datalink circuit is used for INSITE™, Part Number 3824801, to communicate with the ECM. The public datalink can also be used to electronically communicate information with other on-board electronic devices such as electronic dashboards and other equipment.

![[19400260.png]]

The datalink is powered and uses a 9-pin Deutsch datalink connector. The wiring positions are as follows:

Position A - Block Ground

Position B - Battery (12/24 VDC)

Position C - J1939 (+)

Position D - J1939 (-)

Position E - J1939 shield

Position F - Datalink (+)

Position G - Datalink (-)

Position H - Open

Position J - Open

![[19400743.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> To reduce the possibility of connector damage, do not use probes or leads other than Part Number 3822758, on the 40-pin engine harness connector and Part Number 3824812, on the 9-pin datalink connector. The leads must fit tightly in the connector without expanding the pins in the connector.

Disconnect the engine harness from the ECM.

Turn the keyswitch to the OFF position.

Measure the resistance from pin 14 of the engine harness connector to pin F of the 9-pin datalink connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure 019-240, 019-206, or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19400744.png]]

Measure the resistance from pin 15 of the engine harness connector to pin G of the 9-pin datalink connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure 019-240, 019-206, or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19400745.png]]

Measure the resistance from pins 7 and 8 of the engine harness connector to pin A of the 9-pin datalink connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure 019-240, 019-206, or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19400746.png]]

Disconnect the +24-VDC battery supply from the battery.

Measure the resistance from the +24-VDC battery supply terminal to pin B of the 9-pin datalink connector. The multimeter **must** show a closed circuit (10 ohms or less)

If the circuit is **not** closed, repair or replace the OEM +24-VDC supply circuit. Refer to the manufacturer's instructions.

If the values are correct, the circuit **must** still be checked for short circuits to ground and short circuits from pin to pin.

![[19400747.png]]

### Check for Short Circuit to Ground

Measure the resistance from pin F of the 9-pin datalink connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19400748.png]]

Measure the resistance from pin G of the 9-pin datalink connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19400749.png]]

Disconnect the +24-VDC battery supply from the battery.

Disconnect the OEM interface harness from the ECM.

Measure the resistance from pin B of the 9-pin datalink connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19400750.png]]

### Check for Short Circuit from Pin to Pin

Measure the resistance from pin F of the 9-pin datalink connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19400751.png]]

Measure the resistance from pin G to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19400752.png]]

Measure the resistance from pin B to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19400753.png]]

Measure the resistance from pin A to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19400754.png]]

Disconnect the engine harness from the ECM.

Measure the resistance from pin 14 of the engine harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-240 or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19400279.png]]

Measure the resistance from pin 15 to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-240 or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19400280.png]]

### Voltage Check

Locate the datalink connector on the OEM harness. The location will depend on the OEM installation procedures.

The datalink circuit is shown. A public and engine side datalink are available.

![[19400475.png]]

Turn the keyswitch to the ON position.

Set the multimeter to measure VDC.

Measure the voltage from pin F of the 9-pin datalink connector to the engine block.

The multimeter **must** show 4.0 to 5.0 VDC.

![[19400758.png]]

Measure the voltage from pin G of the 9-pin datalink connector to the engine block.

The multimeter **must** show 0 to 1.0 VDC.

![[19400759.png]]

Measure the voltage from pin B of the 9-pin datalink connector to the engine block.

The multimeter **must** show 18.0 to 27.0 VDC.

![[19400755.png]]

Measure the voltage from pin A of the 9-pin datalink connector to the engine block.

The multimeter **must** show 0 VDC.

![[19400756.png]]

If the voltage at pin F measures 0 to 1.0 VDC and the voltage at pin G measures 4.0 to 5.0 VDC, then the pins in the 9-pin datalink connector are improperly installed and **must** be reversed.

If the voltage and polarity are correct, the datalink circuit **must** be checked for a short circuit to ground and a short circuit from pin to pin.

If no voltage is present, the datalink circuit **must** be checked for an open circuit. Verify the battery voltage is correct.

If the voltage at pin A is 18.0 to 27.0 VDC and the voltage at pin B is 0 VDC, then the pins in the 9-pin datalink connector are improperly installed and **must** be reversed.

![[19400757.png]]
