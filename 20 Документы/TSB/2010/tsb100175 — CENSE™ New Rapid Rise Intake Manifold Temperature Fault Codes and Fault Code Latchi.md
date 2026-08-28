---
type: "TSB"
doc: "tsb100175"
title_en: "CENSE™ New Rapid Rise Intake Manifold Temperature Fault Codes and Fault Code Latching"
modified: "2002-12-03"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100175.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb100175.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60"
---

# CENSE™ New Rapid Rise Intake Manifold Temperature Fault Codes and Fault Code Latching

> [!abstract] TSB · `tsb100175`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Даты:** изменён 2002-12-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100175.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb100175.pdf)

## CENSE™ New Rapid Rise Intake Manifold Temperature Fault Codes and Fault Code Latching

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

The purpose of This Technical Service Bulletin is to inform the field of a new CENSE™ fault code and to describe how certain fault codes will be latched 'active' when logged by the ECM.

A new CENSE™ diagnostic has been created to detect a rapid rise in intake manifold temperature. This feature can help detect intake valve failures. Four new fault codes are being activated for this diagnostic.

| Rapid Rise Intake Manifold Temperature Fault Code |  |
|---|---|
| Fault Code | Description |
| 783 | Rapid rise in intake manifold temperature - Left bank, front quadrant |
| 2157 | Rapid rise in intake manifold temperature - Left bank, rear quadrant |
| 2158 | Rapid rise in intake manifold temperature - Right bank, front quadrant |
| 2159 | Rapid rise in intake manifold temperature - Right bank, rear quadrant |

The new calibrations can be found on the September 2002 INCAL™ CD ROM for all QSK45 and QSK60 Industrial applications with the CENSE™ option.

To improve the engine protection feature, certain fault codes will be latched on once they become active. This means that once the fault code a has been logged, the fault code will remain active until the fault code has been cleared using the INSITE™ CENSE™ electronic service tool. **Only** applications with the CENSE™ option will have this feature. Engines without the CENSE™ option will **not** have latched fault codes.

| Fault Code Latching (Only the following fault codes will be latched) |  |  |  |
|---|---|---|---|
| Fault Code | Description | Effect on Engine\* | Approximate Release Date |
| 783 | Rapid rise intake manifold temperature | Engine protection lamp lighted | September 2002 |
| 2157 | Rapid rise intake manifold temperature | Engine protection lamp lighted | September 2002 |
| 2158 | Rapid rise intake manifold temperature | Engine protection lamp lighted | September 2002 |
| 2159 | Rapid rise intake manifold temperature | Engine protection lamp lighted | September 2002 |
| 612 | Oil filter restriction | Non engine protection lamp lighted | September 2002 |
| 555 | High blowby pressure | Engine derate | September 2002 |
| 143 | Low oil pressure | Engine derate | September 2002 |
| 415 | Very low oil pressure | Engine derate | September 2002 |

\* If the application is an electric-drive haul truck, then the truck will be kicked out of propel as well as an engine derate when the fault is active.

> [!note] Note · Примечание
> There is a software issue with the June/July/August CENSE™ Calibration CD. Do **not** use the June/July/August CD to recalibrate CENSE™ ECMs.

This issue is due to a software bug. This results in a derate occurring when intake manifold temperature is greater than 77° C \[170° F\] although no fault code is logged. The software issue has been resolved on the September CENSE™ Calibration CD.

Description of Symptoms

- Operator claims engine is **only** running at 1675 rpm or less
- Technician can **not** find a fault code which causes derate
- Trouble occurs during high ambient temperatures.
