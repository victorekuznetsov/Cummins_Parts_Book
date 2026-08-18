---
aliases:
  - "Руководство по установке индикатора воды в топливе"
type: "Сервисный бюллетень"
doc: "3666212"
title_en: "Aftermarket Water in Fuel Indicator Installation Guide"
title_ru: "Руководство по установке индикатора воды в топливе"
released: "1998-04-01"
modified: "2020-02-06"
group: "19 - Electronic Engine Controls"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
figures: 12
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/3666212.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/3666212.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "тема/electronic-engine-controls"
---

# Aftermarket Water in Fuel Indicator Installation Guide
**Руководство по установке индикатора воды в топливе**

> [!abstract] Сервисный бюллетень · `3666212`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Даты:** выпущен 1998-04-01 · изменён 2020-02-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/3666212.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/3666212.pdf)

## Aftermarket Water in Fuel Indicator Installation Guide

This bulletin provides instructions for installing and testing the Aftermarket Water in Fuel Indicator kit, Part Number 3804810. The aftermarket kit is used on CELECT™, CELECT™ Plus, and Quantum™ engines.

- The Aftermarket Water in Fuel Indicator kit will alert the driver when water is detected in the bottom of the Fleetguard™ 10 micron Aftermarket Water in Fuel Indicator fuel filter. If water is detected, then the engine warning light will flash until the water is drained from the fuel filter. Water is drained from the filter by turning the drain valve in a clockwise direction looking down on the filter. Once the water is purged, tighten the valve. The drain valve and sensor are integral to the filter. The sensor will rotate in the filter but it is **not** removable.
- The Aftermarket Water in Fuel Indicator kit requires a coolant level sensor or coolant level sensor shorting plug. The coolant level sensor diagnostics are used to detect water in the fuel filter and the coolant level. Fault Code 422 will be identified by following the procedure for reading active fault codes in the engine's Operation and Maintenance Manual.
- An optional diagnostic lamp is available for installation, that detects water in fuel **only**. This diagnostic lamp is supplied with the Aftermarket Water in Fuel Indicator kit. The lamp lets the driver know immediately that water has been detected. This eliminates the need for the driver to interpret the exact cause of a flashing engine warning lamp.
- The Aftermarket Water in Fuel Indicator circuitry and associated diagnostics require CELECT™, CELECT™ Plus, and Quantum™ trained technicians to install, diagnose, repair, or test. Contact your local Cummins Authorized Repair Location for assistance.

Engine has a coolant level sensor and 4-pin Weather-Pack

Disconnect the 4-pin Weather-Pack shroud from the 4-pin Weather-Pack tower between the coolant level sensor and the OEM connector.

> [!note] Note · Примечание
> The gender of a connector will need to be changed to fit a Aftermarket Water in Fuel Indicator harness connector. If two connectors are the same gender, change the connector that is **not** part of the Aftermarket Water in Fuel Indicator harness. Changing a Aftermarket Water in Fuel Indicator harness connector will compromise Aftermarket Water in Fuel Indicator's circuit operation.

![[19900989.png]]

Engine has a coolant level sensor but no 4-pin Weather-Pack

If the engine does **not** have a 4-pin Weather-Pack tower connector between the coolant level sensor and the 9- or 21-pin OEM connector, one **must** be installed. The coolant level sensor requires a 4-pin Weather-Pack tower to connect to the 4-pin shroud connector of the Aftermarket Water in Fuel Indicator harness. Alternately, the OEM requires a 4-pin shroud to connect to the 4-pin tower connector of the Aftermarket Water in Fuel Indicator harness. See Table 1, to wire a 4-pin tower connector to the coolant level sensor. See Table 2, to wire a 4-pin shroud to a specific OEM connector.

Coolant level sensor pinouts will differ by manufacturer. Use the following guidelines in Table 1, to confirm that the coolant level sensor is wired to the 4-pin Weather-Pack shroud connector of the Aftermarket Water in Fuel Indicator harness:

| Table 1, Coolant Level Sensor Pinouts |  |  |
|---|---|---|
| Coolant Level Sensor | Robert Shaw Coolant Level Sensor | Aftermarket Water in Fuel Indicator Harness Shroud Connector Pin |
| 5 VDC | C | A |
| GND | B | B |
| CL Low | A | D |
| CL High | D | C |

![[19400417.png]]

If your engine has a 4-pin Weather-Pack shorting plug but no coolant level sensor

Unplug the coolant level sensor shorting plug connection.

> [!note] Note · Примечание
> The gender of a connector may need to be changed to fit a Aftermarket Water in Fuel Indicator harness connector. If two connectors are the same gender, change the connector that is not part of the Aftermarket Water in Fuel Indicator harness. Changing a Aftermarket Water in Fuel Indicator harness connector may compromise Aftermarket Water in Fuel Indicator's circuit operation.

![[19900990.png]]

Weather-Pack tower shorting plug configuration for CELECT™, CELECT™ Plus, and Quantum™ without a coolant level sensor.

![[19801554.png]]

Table 2, A 4-pin Weather-Pack tower (shorting plug) connector connects to a 4-pin Weather-Pack shroud connector of the Aftermarket Water in Fuel Indicator harness. One jumper wire connects pins D and B and another connects pins C and A in the tower connector.

| Table 2 |  |
|---|---|
| Coolant Level | Aftermarket Water in Fuel Indicator Harness Pinout (Tower/Shroud) |
| +5 VDC | A |
| Return | B |
| High Signal | C |
| Low Signal | D |

| Table 2, Continued |  |  |  |
|---|---|---|---|
|  | OEM Connector Pinout |  |  |
| Coolant Level | CELECT™ Plus (21-pin) | CELECT™ (9-pin) | Quantum™ (21-pin) |
| +5 VDC | J | A | U |
| Return | K | J | V |
| High Signal | L | C | S |
| Low Signal | M | B | T |

![[19801553.png]]

If your engine has neither a 4-pin Weather-Pack shorting plug nor a coolant level sensor.

Check for the following:

- If the coolant level sensor jumpers are completed in the 9- or 21-pin OEM connector (i.e., a 4-pin Weather-Pack tower/shroud connector does **not** exist), then see Table 2, to make a 4-pin tower shorting plug
- Connect the shorting plug to the 4-pin shroud connector of the Aftermarket Water in Fuel Indicator harness. Refer to Procedure Refer to Procedure 019-341 in the CELECT™ Fuel System Troubleshooting and Repair Manual, Bulletin Number 3666084, or Procedure [[99-019-204 — Deutsch DRC Connector Series|Refer to Procedure 019-204]] in the CELECT™ Plus Fuel System Troubleshooting and Repair Manual, Bulletin Number 3666130
- Wire a 4-pin shroud connector to the 9- or 21-pin OEM connector, is connected to the 4-pin tower connector of the Aftermarket Water in Fuel Indicator harness for the specific OEM connector type (see Table 2).

![[19900989.png]]

Separate the Aftermarket Water in Fuel Indicator harness, Part Number 3160424, from the rest of the kit. The harness **must** be installed to specific connectors to for the circuit to operate correctly.

Install the harness:

- Connect the Aftermarket Water in Fuel Indicator harness 4-pin Weather-Pack tower connector to the 4-pin Weather-Pack shroud connector on the 9- or 21-pin OEM connector
- Connect the 4-pin shroud connector of the Aftermarket Water in Fuel Indicator harness to the 4-pin tower connector on the coolant level sensor harness.

> [!note] Note · Примечание
> The gender of a connector will need to be changed to fit a Aftermarket Water in Fuel Indicator harness connector. If two connectors are the same gender, change the connector that is **not** part of the Aftermarket Water in Fuel Indicator harness. Changing a Aftermarket Water in Fuel Indicator harness connector will compromise Aftermarket Water in Fuel Indicator's circuit operation.

Identify the connection between the coolant level sensor and the 9- or 21-pin OEM connector.

![[19400417.png]]

> [!warning] CAUTION · Осторожно
> Mechanical overtightening of the filter will distort the threads or the filter element seal.

Install the fuel filter with Aftermarket Water in Fuel Indicator probe assembly, Fleetguard™ FS1003, Part Number 3406889:

- Clean the area around the fuel filter and filter head
- Install a new thread adaptor sealing ring. The ring is supplied with the filter
- Apply a thin coat of clean engine oil to the gasket's surface
- Fill the filter. Use **only** clean fuel
- Install a new 10-micron Fleetguard™ fuel filter on the filter head. Hand tighten the filter an additional 1/2 to 3/4 of a turn after the gasket contacts the filter head surface
- Rotate the probe assembly on the bottom of the filter. Turn the probe away from any area that will expose it to tire spray.

![[ff8bdaa.png]]

> [!note] Note · Примечание
> The filter assembly includes an non-removable Aftermarket Water in Fuel Indicator probe.

> [!note] Note · Примечание
> Unplug the 2-pin connector on the Aftermarket Water in Fuel Indicator harness from the probe assembly before removing the old filter.

Plug the 2-pin connector of the Aftermarket Water in Fuel Indicator harness into the probe connector on the bottom of the filter.

![[19901093.png]]

Dash Lamp Installation

This an optional installation. To install the dash lamp follow the steps below:

- Drill a 7/16 diameter hole in which to mount the lamp. The lamp is almost always mounted in the dash board. Secure the lamp in the dash with the jam nut
- Provide 12 VDC to the lamp using a 12 VDC vehicle key-switched supply. If the ignition switch for the vehicle is used, do **not** wire to the same ignition key switch post that ECM pin 26 (key switch input) is wired to **or** to the fuel shutoff valve. Either method causes potential ECM damage. The 12 VDC supply wire on the lamp is without a terminal in order to accommodate individual preference
- Run the 1-pin Weather-Pack connector of the lamp assembly through the bulkhead and into the engine compartment.

> [!note] Note · Примечание
> Seal wire openings to prevent toxic fumes from seeping into the cab. Sealing wire openings also protects the wire from abrasion.

![[19801552.png]]

Connect the Aftermarket Water in Fuel Indicator 1-pin tower female connector of the lamp, Part Number 3622056, to the 1-pin male shroud connector of the Aftermarket Water in Fuel Indicator harness.

> [!note] Note · Примечание
> A protective cap has been installed on the shroud connector in case the optional lamp is not used.

![[19900988.png]]

Aftermarket Water in Fuel Indicator Circuitry

Test the circuitry:

- Key switch in the OFF position
- Unplug the 2-pin connector from the Aftermarket Water in Fuel Indicator probe
- Key switch in the ON position
- Short circuit from pins A to B in the 2-pin connector of the Aftermarket Water in Fuel Indicator harness for at least 10 seconds
- Verify the engine warning lamp flashes
- Verify the optional dash lamp lights
- Remove the short
- Verify the engine warning lamp does **not** flash
- Verify the optional dash lamp does **not** light
- Reconnect the 2-pin connector of the Aftermarket Water in Fuel Indicator harness to the Aftermarket Water in Fuel Indicator probe
- Review installation procedure and wiring for improper circuit operation.

![[19901093.png]]

### Document History
