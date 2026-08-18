---
aliases:
  - "Цепь топливоподкачивающего насоса"
type: "Процедура"
doc: "60-019-397"
title_en: "Fuel Lift Pump Circuit"
title_ru: "Цепь топливоподкачивающего насоса"
modified: "2021-02-12"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 4
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-397.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-397.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Fuel Lift Pump Circuit
**Цепь топливоподкачивающего насоса**

> [!abstract] Процедура · `60-019-397`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Controls · Section 19 - Electronic Controls - Group 19 · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2021-02-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-397.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-397.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Multimeter, Part Number 3164488

#### Additional Service Items

- Cable, Electrical Breakout Harness, Part Number 3163531

### General Information

The fuel lift pump is controlled by the engine control module (ECM). The ECM supplies power to the fuel lift pump without the use of a relay or fuse.

![[25t00001.png]]

### Initial Check

Inspect the engine harness, lift pump power connector, lift pump relay power connector, and the lift pump relay pins for the following:

- loose connector
- corroded pins
- bent or broken pins
- pushed back or expanded pins
- moisture in or on the connector
- missing or damaged connector seals
- dirt or debris in or on the connector pins
- connector shell broken
- wire insulation damage
- damaged connector locking tab.

Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection|Refer to Procedure 019-361 in Section 19]]

Use the following procedure for the properly replace or repair the connectors, pins, or harness. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]

![[19400002.png]]

### Resistance Check

Check for an open circuit in the fuel lift pump return circuit. Disconnect the 2 pin fuel lift pump power connector at the fuel lift pump.

Disconnect the engine wiring harness ECM connector.

Measure the resistance of the fuel lift pump circuit between the supply and return at the 2 pin fuel lift pump connector.

Measure the resistance of the fuel lift pump supply and return circuits between these two connectors.

The resistance **must** be 10 ohms or less. If the resistance is greater than 10 ohms, repair or replace the engine harness.

![[00r00985.png]]

### Voltage Check

Turn the keyswitch ON, the circuit **must** be loaded to measure the voltage.

1. Disconnect the fuel lift pump power connector from engine harness connector (1).
2. Connect cable, electrical breakout harness, Part Number 3163531 to the fuel lift pump and engine harness electrical connector.
3. Connect multimeter test leads (2) to the open connector on the cable, electrical breakout harness
4. .Turn engine keyswitch ON and measure voltage drop.
5. The voltage indicated on the multimeter (2) should be within one volt of battery voltage.

**Only** measure voltage during the first 30 seconds of the keyswitch being ON. If measurements are **not** done within allotted time, the keyswitch **must** be cycled.

| Voltage Drop | Within + 1 VDC of battery voltage |
|---|---|

- If battery voltage is **not** within specified voltage values, then a malfunctioning fuel lift pump has been detected.
- If battery voltage is **not** indicated, check multimeter for a malfunction and retest, if a second check yields no voltage reading, then a malfunctioning wiring harness has been detected.
- Check the ECM for the proper calibration. If calibration is correct and up to date, and there is still **not** battery voltage, contact a Cummins® Authorized Repair Location.

![[00r00984.png]]
