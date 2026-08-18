---
aliases:
  - "Жгут проводов двигателя"
type: "Процедура"
doc: "87-019-043"
title_en: "Engine Wiring Harness"
title_ru: "Жгут проводов двигателя"
modified: "2018-08-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 49
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-043.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-043.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Engine Wiring Harness
**Жгут проводов двигателя**

> [!abstract] Процедура · `87-019-043`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2018-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-043.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-043.pdf)

### General Information

The QST30 Industrial engines use three separate wiring harnesses to control the engine and some of the vehicle operations:

1. Left bank engine harness (primary)
2. Right bank engine harness (secondary)
3. SAE J1939 backbone harness.

![[nobox.png]]

Replace a harness if there is an open circuit or a short circuit found under the protective covering of the harness body.

![[19400386.png]]

### Test

Start the engine and run at low idle. With the engine running, cut out the left bank by removing the RP39 harness connector from the left bank harness. If the engine dies, the right bank is **not** operating correctly, as the engine should run on one bank at low idle.

Repeat the above test cutting out the right bank by removing the RP39 harness connector from the right bank harness. If the engine dies, the left bank is **not** operating correctly, as the engine should run on one bank at low idle.

If the engine runs at low idle during both of the above tests, any engine problems are unique to specific cylinders, **not** one complete bank.

![[19a00338.png]]

If one bank is identified as **not** functioning, begin by verifying that the engine control module (ECM) is receiving unswitched and keyswitch power. [[99-019-064 — Key Switch Power Supply Circuit|Refer to Procedure 019-064 in Section 19.]] Refer to Procedure 019-087 in Section 19.

Verify that the Bosch® EHAB fuel shutoff valve is functioning correctly. [[87-019-050 — Fuel Shutoff Valve|Refer to Procedure 019-050 in Section 19]]. Check for any electronic fault codes indicating a closed or stuck fueling rack. Troubleshoot any active fault codes accordingly.

![[19a00338.png]]

### Remove

Left Bank

> [!note] Note · Примечание
> The left bank engine harness is the primary engine harness.

Disconnect the engine harness from the coolant pressure sensor (if present).

Remove the engine harness clamps.

![[19801065.png]]

Disconnect the coolant temperature sensor and the coolant level sensor.

![[19a00334.png]]

Cut the ties on the thermostat housing bracket, aftercooler tube, and fuel tube.

![[19801067.png]]

Disconnect the intake manifold temperature sensor.

![[19a00247.png]]

Disconnect the two 6-pin or one 9-pin data link connector(s) from the harness support bracket by removing the capscrews.

![[19a00273.png]]

Disconnect the oil pressure sensor.

![[19a00254.png]]

Disconnect the ambient air pressure sensor and intake manifold pressure sensor.

![[19a00335.png]]

Disconnect the fuel pump connector.

![[19a00274.png]]

Disconnect the EHAB (fuel shutoff valve).

![[19a00249.png]]

Disconnect the engine speed sensor.

![[19a00245.png]]

Disconnect the engine block ground from the block.

![[19400393.png]]

Disconnect the 21-pin and 31-pin connectors.

![[19a00258.png]]

Disconnect the 21-pin primary/secondary harness disconnect connector.

![[19a00276.png]]

Use a 4-mm \[5/32-in\] hex head wrench to disconnect the engine harness Deutsch™ connector from the ECM.

![[19900781.png]]

Right Bank

> [!note] Note · Примечание
> The right bank engine harness is the secondary engine harness.

Remove the engine harness clamps.

![[19801065.png]]

Disconnect the intake manifold temperature sensor.

![[19a00277.png]]

Disconnect the engine position sensor.

![[19a00261.png]]

Disconnect the fuel pump.

![[19a00338.png]]

Disconnect the EHAB (fuel shutoff valve).

![[19a00339.png]]

Disconnect the engine block ground from the block.

![[19400393.png]]

Use a 4-mm \[5/32-in\] hex head wrench to disconnect the engine harness Deutsch™ connector from the ECM.

![[19900787.png]]

### Install

Left Bank

> [!note] Note · Примечание
> The left bank engine harness is the primary engine harness.

Connect the coolant pressure sensor (if present).

Install the engine harness clamps.

![[19801065.png]]

Connect the coolant temperature sensor.

Connect the coolant level sensor.

![[19a00334.png]]

Install ties on the thermostat housing bracket, aftercooler tube, and fuel tube.

![[19801067.png]]

Connect the intake manifold temperature sensor.

![[19a00247.png]]

Connect the two 6-pin or one 9-pin data link connector(s) to the harness support bracket and install the capscrews.

![[19a00273.png]]

Connect the oil pressure sensor.

![[19a00254.png]]

Connect the ambient air pressure sensor and the intake manifold pressure sensor.

![[19a00335.png]]

Connect the fuel pump.

![[19a00274.png]]

Connect the EHAB (fuel shutoff valve).

![[19a00249.png]]

Connect the engine speed sensor.

![[19a00245.png]]

Connect the engine block ground to the block.

![[19400393.png]]

Connect the 21-pin and 31-pin connectors.

Connect the 12-pin advance engine monitor connector.

![[19a00275.png]]

Use a 4-mm \[5/32-in\] hex head wrench to connect the engine harness Deutsch™ connector to the ECM.

![[19900781.png]]

Right Bank

> [!note] Note · Примечание
> The right bank engine harness is the secondary engine harness.

Install the engine harness clamps.

![[19801065.png]]

Connect the intake manifold temperature sensor.

![[19a00277.png]]

Connect the engine position sensor.

![[19a00261.png]]

Connect the intake manifold pressure sensor.

![[19a00278.png]]

Connect the fuel pump.

![[19a00338.png]]

Connect the EHAB (fuel shutoff valve).

![[19a00339.png]]

Connect the engine block ground to the block.

![[19400393.png]]

Connect the 21-pin primary/secondary harness disconnect connector.

![[19a00276.png]]

Use a 4-mm \[5/32-in\] hex head wrench to connect the engine harness Deutsch™ connector to the ECM.

![[19900787.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

Disconnect the right bank and left bank ECM connectors.

![[19900515.png]]

Measure the resistance from the rack position common wire to the ground wire on the right bank engine harness ECM connector. Refer to the wiring diagram for connector pin identification.

Measure the resistance from the rack position common wire to the ground wire on the left bank engine harness ECM connector. Refer to the wiring diagram for connector pin identification.

> [!note] Note · Примечание
> Left bank resistance does **not** need to be checked on engine wiring harness, Part Number 4975508.

The resistance **must** be between 2134 and 2266 ohms.

If the harness resistance value between the harness connector pins is within the specification, consult the fault code or symptom based troubleshooting procedures.

If the harness resistance value does **not** meet the specification, replace the resistor and check the resistance value again.

If the harness resistance still does **not** meet specification, replace the harness.

![[19c01215.png]]
