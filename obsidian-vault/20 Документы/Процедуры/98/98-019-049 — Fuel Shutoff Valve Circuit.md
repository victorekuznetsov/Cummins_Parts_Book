---
aliases:
  - "Цепь клапана отсечки топлива"
type: "Процедура"
doc: "98-019-049"
title_en: "Fuel Shutoff Valve Circuit"
title_ru: "Цепь клапана отсечки топлива"
modified: "2012-11-14"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-049.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-049.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Fuel Shutoff Valve Circuit
**Цепь клапана отсечки топлива**

> [!abstract] Процедура · `98-019-049`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2012-11-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-049.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-049.pdf)

### General Information

The fuel shutoff valve circuit is a SIGNAL wire connected to the switch battery SUPPLY wire. The valve is grounded through the engine.

> [!note] Note · Примечание
> If the fuel shutoff valve is connected to the auxiliary shutdown wire, check the shutdown wire circuit. [[98-019-179 — Auxiliary Shutdown Circuit|Refer to Procedure 019-179 in Section 19.]]

![[nobox.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> To avoid damage to the solenoid, hold the terminal nut closest to the solenoid with the proper wrench when disconnecting the solenoid wire nut.

Disconnect the main engine harness from the engine control module (ECM).

Flush and clean the connector pins. Use contact cleaner, Part Number 3824510. Inspect the ECM and main engine harness connectors for damaged pins.

Disconnect the solenoid wire from the solenoid terminal.

Disconnect the C5 and C6 connectors.

![[19801708.png]]

Touch one of the multimeter leads to pin 22 of the main engine harness connector. Touch the other multimeter lead to the ring terminal on the end of the fuel shutoff solenoid wire.

Make sure the ring terminal on the end of the solenoid wire is **not** touching anything that is grounded.

![[19801717.png]]

Measure the resistance.

The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is an open circuit in the fuel shutoff solenoid SUPPLY wire.

Repair or replace the main engine harness.

- Refer to Procedure 019-228 in Section 19.
- [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]

![[19801619.png]]

### Check for Short Circuit to Ground

Touch one of the multimeter leads to pin 22 of the main engine harness connector. Touch the other multimeter lead to the engine block ground. Make sure the solenoid wire ring terminal is **not** touching anything that is grounded.

Measure the resistance. The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short to ground in the wire connected to pin 22.

Repair or replace the main engine harness.

- Refer to Procedure 019-228 in Section 19.
- [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]

![[19801714.png]]

### Check for Short Circuit from Pin to Pin

Check for a short circuit between pin 22 of the main engine harness connector and all other pins in the connector except pin 23.

Touch one of the multimeter leads to pin 22 of the connector. Touch the other multimeter lead to all other pins in the connector except pin 23. Make sure the solenoid ring terminal wire is **not** touching anything that is grounded.

![[19801715.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short between the wires connected to pin 22 of the main engine harness connector and **any** other pin that measured less than 100k ohms.

Repair or replace the main engine harness.

- Refer to Procedure 019-228 in Section 19.
- [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]

![[19801621.png]]

### Voltage Check

Check the voltage at the fuel shutoff valve.

Make sure the voltage SUPPLY wire is disconnected.

Turn keyswitch ON.

Select the DC voltage function on the multimeter. Touch one of the multimeter leads to the solenoid wire ring terminal. Touch the other multimeter lead to a good, clean surface on the engine block.

![[19801710.png]]

Measure the voltage.

The voltage **must** be the same as the battery voltage. If the voltage is **not** correct, then inspect the terminal for corrosion.

If the terminal is clean, then inspect the main engine harness and keyswitch.

Check the SIGNAL wire for short to ground or short from pin-to-pin.

![[19801711.png]]
