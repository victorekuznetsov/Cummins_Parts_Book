---
type: "TSB"
doc: "tsb101032"
title_en: "Boost Pressure Sensor Adapter Harness Resulting in Fault Codes 122/123"
modified: "2015-07-09"
engines:
  - "85017333"
families:
  - "QSK23"
parts:
  - "4096901"
figures: 3
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101032.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101032.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK23"
---

# Boost Pressure Sensor Adapter Harness Resulting in Fault Codes 122/123

> [!abstract] TSB · `tsb101032`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Даты:** изменён 2015-07-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101032.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101032.pdf)

## Boost Pressure Sensor Adapter Harness Resulting in Fault Codes 122/123

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Issue**

Customers have reported low power or intermittent low power along with a check engine lamp. Troubleshooting the issue finds multiple records of fault codes 122 and 123. Engines that have seen the issue have boost pressure sensor and adapter harness assembly, part number 4096902, installed.

**Product Affected**

- QSK23 CM500

**Verification**

The issue highlighted above applies to engines with an engine build date prior to 29 July 2010.

Engines with a build date after 29 July 2010 are less likely to experience the issue highlighted above because these engines have the following parts that were released into production to prevent boost pressure sensor fault codes.

- Engine wire harness, Part Number [[4096901]]
- Boost pressure sensor and adapter harness assembly, Part Number 4096902 (Figure 1)

A 3 pin Deutsch™ connector is included with the boost pressure sensor and adapter harness assembly to allow connection to the main engine harness.

![[19r99307.png]]

Figure 1, Boost Pressure Sensor and Adapter Harness Assembly, Part Number 4096902

1. 3 pin Deutsch™ Connector and harness.
2. Tape location between adapter harness and boost pressure sensor.
3. Boost pressure sensor, Part Number 3408589.

**Resolution**

The parts in Table 1 were released into production to prevent boost pressure sensor fault codes. The parts were released according to Table 2.

| Table 1, Parts Released |  |
|---|---|
| Part Number | Part Description |
| 4096902 | Boost pressure sensor and adapter harness assembly |
| 4096903 | Adapter harness part number |
| [[4096901]] | Engine wiring harness (replaces engine wiring harness, Part Number 4096634) |

| Table 2, Production Information |  |
|---|---|
| Engine Serial Number (ESN) First | Build Date |
| 00321406 | 29 July 2010 |

For engines with an engine build date prior to 29 July 2010, the steps below should be performed.

**Solution 1**

For field service, it is possible to avoid replacing the engine wiring harness by cutting off the current Packard™ connector on the engine harness and splicing a new male Deutsch™ connector in its place. For this solution, the parts in Table 3 should be used.

| Table 3, Solution 1 Parts |  |
|---|---|
| Part Number | Part Description |
| 4096902 | Sensor assembly and adapter harness |
| 3164509 | 3 Pin Deutsch™ connector (male) |

For assistance with splicing methods, use the following procedure in the QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R\|3666113]]. [[99-019-206 — Deutsch DTM and DTP Connector Series|Refer to Procedure 019-206 in Section 19.]]

When replacing the Packard™ connector, tag each wire with the terminal identification (A, B, and C) and where the wire is connected before removing from the Packard™ connector. The terminals are marked on the backside of the Packard™ connector, as shown in Figure 2.

![[19h00001.png]]

Figure 2, Terminal Identification on Packard™ Connector.

**Solution 2**

If the boost pressure sensor and adapter harness assembly, Part Number 4096902, is **not** available, the parts in Table 4 can be used to assemble a jumper harness to connect to boost pressure sensor, Part Number 3408589.

- Attach 3 pin Deutsch™ female connector (Figure 3, Item C) to the 3 pin Packard™ connector (Figure 3, Item B).
- Insert the 3 pin Packard™ connector into boost pressure sensor (Figure 3, Item A).
- Heat shrink **must** be applied around the harness and sensor connection to prevent movement.

![[19r99308.png]]

Figure 3, Jumper Harness and Boost Pressure Sensor

| Table 4, Solution 2 Parts |  |  |
|---|---|---|
| Callout | Part Number | Part Description |
| A | 3408589 | Boost Pressure Sensor |
| B | 3824256 | 3 pin Packard™ connector |
| C | 3163256 | 3 Pin Deutsch™ connector (female) |
| D | 3164509 | 3 pin Deutsch™ connector (male) (**only** needed if engine does **not** have engine wiring harness, Part Number [[4096901]]) |

### Document History

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[4096901]] | WIRING HARNESS | Жгут проводов |
