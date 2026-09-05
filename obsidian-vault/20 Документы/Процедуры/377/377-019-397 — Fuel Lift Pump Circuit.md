---
aliases:
  - "Цепь топливоподкачивающего насоса"
type: "Процедура"
doc: "377-019-397"
title_en: "Fuel Lift Pump Circuit"
title_ru: "Цепь топливоподкачивающего насоса"
modified: "2021-02-12"
manuals:
  - "5411181"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-019-397.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-019-397.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Fuel Lift Pump Circuit
**Цепь топливоподкачивающего насоса**

> [!abstract] Процедура · `377-019-397`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 19 - Electrical Controls - Group 19 · Section 19 - Electronic Controls · Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2021-02-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-019-397.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-019-397.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Multimeter, Part Number 3164488

#### Additional Service Items

- Electrical Breakout Harness Cable, Part Number 3163531

### General Information

The fuel lift pump is controlled by the engine control module (ECM). The ECM supplies power to the fuel lift pump without the use of a relay or fuse.

![[25t00001.png]]

### Initial Check

Inspect the engine harness, lift pump power connector, and pins for the following:

- Loose connector
- Corroded pins
- Bent or broken pins
- Pushed back or expanded pins
- Moisture in or on the connector
- Missing or damaged connector seals
- Dirt or debris in or on the connector pins
- Connector shell broken
- Wire insulation damage
- Damaged connector locking tab.

Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection|Refer to Procedure 019-361 in Section 19.]]

Use the following procedure for the proper replacement or repair of connectors, pins, or harness. Refer to Procedure 019-043 in Section 19.

![[19400002.png]]

### Resistance Check

Check for an open circuit in the fuel lift pump circuit. Disconnect the 2 pin fuel lift pump power connector at the fuel lift pump.

Disconnect the engine wiring harness ECM connector.

Measure the resistance of the fuel lift pump circuit between the supply and return at the 2 pin fuel lift pump connector.

Measure the resistance of the fuel lift pump supply and return circuits between these two connectors.

The resistance **must** be 10 ohms or less. If the resistance is greater than 10 ohms, repair or replace the engine harness.

![[00r00985.png]]

### Voltage Check

Turn the keyswitch ON. The circuit **must** be loaded to measure the voltage.

1. Disconnect the fuel lift pump power connector from engine harness connector.
2. Connect electrical breakout harness cable, Part Number 3163531 to the fuel lift pump and engine harness electrical connector.
3. Connect multimeter test leads to the open connector on the cable, electrical breakout harness.
4. Turn engine keyswitch ON and measure voltage drop.
5. The voltage indicated on the multimeter should be within one volt of battery voltage.

: **Only** measure voltage during the first 30 seconds of the keyswitch being ON. If measurements are **not** done within allotted time, the keyswitch **must** be cycled.

| Voltage Drop | Within + 1 VDC of battery voltage |
|---|---|

- If battery voltage is **not** within specified voltage values, then a malfunctioning fuel lift pump has been detected.
- If battery voltage is **not** indicated, check multimeter for a malfunction and retest. If a second check yields no voltage reading, then a malfunctioning wiring harness has been detected.
- Check the ECM for the proper calibration. If calibration is correct and up to date, and there is still **not** battery voltage, contact a Cummins® Authorized Repair Location.

![[00r00984.png]]
