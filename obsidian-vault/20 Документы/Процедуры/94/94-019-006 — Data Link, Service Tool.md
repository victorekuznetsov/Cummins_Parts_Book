---
aliases:
  - "Шина данных сервисного инструмента"
type: "Процедура"
doc: "94-019-006"
title_en: "Data Link, Service Tool"
title_ru: "Шина данных сервисного инструмента"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 24
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-006.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-006.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Data Link, Service Tool
**Шина данных сервисного инструмента**

> [!abstract] Процедура · `94-019-006`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-006.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-006.pdf)

### General Information

The service tool data link circuit is used for INSITE™, Part No. 3825145, to communicate with the ECM and to electronically communicate information with other on-board electronic devices.

![[19a00043.png]]

The data link uses a 9-pin Deutsch connector. The wiring positions follow:

Pin A - DSR

Pin B - RXD

Pin C - TXD

Pin D - DTR

Pin E - Engine Block ground

Pin F - Not used

Pin G - Not used

Pin H - Not used

Pin J - Not used

![[19a00044.png]]

### Resistance Check

Place the Stop/Run switch in the STOP position.

Ensure the controller is **not** in the diagnostic mode.

Remove the engine harness connector from the ECM. Refer to Procedure [[94-019-043 — Engine Wiring Harness|019-043]].

Use test lead, Part No. 3822758, on the ECM connector and use test lead, Part No. 3824811, on the 9-pin Deutsch connector.

Measure the resistance from pin 31 of the engine harness connector to pin A of the 9-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

![[19a00026.png]]

Measure the resistance from pin 32 of the engine harness connector to pin B of the 9-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

![[19a00026.png]]

Measure the resistance from pin 33 of the engine harness connector to pin C of the 9-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

![[19a00026.png]]

Measure the resistance from pin 34 of the engine harness connector to pin D of the 9-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

![[19a00026.png]]

Measure the resistance from pin 35 of the engine harness connector to pin E of the 9-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed in any of the previous steps, repair or replace the engine harness. Refer to Procedures 019-209, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00026.png]]

### Check for Short Circuit to Ground

Use test lead, Part No. 3824811, for the 9-pin Deutsch connector.

Measure the resistance from pin A of the Deutsch connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).

![[19a00027.png]]

Measure the resistance from pin B of the 9-pin Deutsch connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).

![[19a00027.png]]

Measure the resistance from pin C of the 9-pin Deutsch connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).

![[19a00027.png]]

Measure the resistance from pin D of the 9-pin Deutsch connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open in any of the previous steps, repair or replace the engine harness. Refer to Procedures 019-209, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00027.png]]

### Check for Short Circuit from Pin to Pin

**Deutsch Connector**

Use test lead, Part No. 3824811, for the 9-pin Deutsch connector.

Measure the resistance from pin A of the Deutsch connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

![[19a00028.png]]

Measure the resistance from pin B of the 9-pin Deutsch connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

![[19a00028.png]]

Measure the resistance from pin C of the 9-pin Deutsch connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

![[19a00028.png]]

Measure the resistance from pin D of the 9-pin Deutsch connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

![[19a00028.png]]

Measure the resistance from pin E of the 9-pin Deutsch connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open in any of the previous steps, repair or replace the engine harness. Refer to Procedures 019-209 and [[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00028.png]]

**Engine Harness Connector**

Disconnect the engine harness from the ECM.

Use test lead, Part No. 3822758, for the engine harness connector.

Measure the resistance from pin 31 to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

![[19a00029.png]]

Measure the resistance from pin 32 to all other pins in the connector.

The multimeter **must** show an open circuit (100k ohms or more).

![[19a00029.png]]

Measure the resistance from pin 33 to all other pins in the connector.

The multimeter **must** show an open circuit (100k ohms or more).

![[19a00029.png]]

Measure the resistance from pin 34 to all other pins in the connector.

The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open in any of the previous steps, repair or replace the engine harness. Refer to Procedures [[94-019-240 — Connector, 40-Pin|019-240]] and [[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00029.png]]

### Voltage Check

Locate the service tool data link connector on the engine harness.

The data link circuit is shown.

![[19a00030.png]]

Place the Stop/Run switch in the STOP position.

Place the controller in the diagnostic mode.

Turn the dial on the multimeter to measure DC voltage.

With the service tool disconnected from the engine harness, press the “Connect to ECM” command on the service tool and simultaneously measure the voltage, from pin B to pin E (ground), on the service tool cable connector. The multimeter **must** show -5 to -15 VDC.

![[19a00068.png]]

If the voltage reading is incorrect ensure the tool is setup correctly.

If the service tool is setup correctly, conduct the following procedures.

Measure the continuity for pin B of the INSITE™ cable, Part No. 3825183. The multimeter **must** show less than 10 ohms.

![[19400225.png]]

Measure the continuity for pin C of the INSITE™ cable. The multimeter **must** show less than 10 ohms.

If the circuit is **not** closed in any of the previous steps, replace the INSITE™ cable, Part No. 3825183.

![[19400225.png]]
