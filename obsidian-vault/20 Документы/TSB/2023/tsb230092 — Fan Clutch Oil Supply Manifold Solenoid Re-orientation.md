---
aliases:
  - "Переориентация электромагнита коллектора подачи масла муфты вентилятора"
type: "TSB"
doc: "tsb230092"
title_en: "Fan Clutch Oil Supply Manifold Solenoid Re-orientation"
title_ru: "Переориентация электромагнита коллектора подачи масла муфты вентилятора"
released: "2023-06-07"
modified: "2023-06-07"
group: "07 - Lubricating Oil Systems"
engines:
  - "33224404"
  - "33239746"
  - "33239899"
  - "41340468"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK50"
parts:
  - "3008466"
  - "3037536"
  - "3037537"
  - "3046202"
  - "3089240"
  - "3348871"
  - "3627695"
  - "3630740"
  - "3640889"
  - "3641305"
  - "3650106"
  - "3922794"
  - "6414133"
  - "6468466"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2023/tsb230092.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb230092.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK50"
  - "год/2023"
  - "тема/lubricating-oil-systems"
---

# Fan Clutch Oil Supply Manifold Solenoid Re-orientation
**Переориентация электромагнита коллектора подачи масла муфты вентилятора**

> [!abstract] TSB · `tsb230092`
> **Раздел Cummins:** 07 - Lubricating Oil Systems
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK50
> **Даты:** выпущен 2023-06-07 · изменён 2023-06-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2023/tsb230092.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb230092.pdf)

## Fan Clutch Oil Supply Manifold Solenoid Re-orientation

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- QSK50 CM2150 MCRS
- QSK50 CM850 MCRS
- QSK50 CM2350 K108
- QSK50 CM2350 K130

**Issue**

Fan clutch oil solenoid coil malfunction causes permanent cooling fan engagement. Fault codes 245 and 2377 become active. Permanent full fan speed can cause over-cooling and excessive noise.

**Verification**

- Engine cooling fan runs constantly
- Fault codes 245 and 2377 become active

**Resolution**

A new fan clutch oil manifold has been designed to improve oil cooling on the oil control solenoid coil. This fan clutch oil manifold is released in a parts kit (part number [[6468466]]). The parts kit contains all the required components to upfit the new manifold and separately available solenoid (part number [[3641305]]) to the engine.

Existing design oil manifold:

![[16r00150.png]]

Figure 1, Existing Oil Manifold Installation.

New design oil manifold:

![[16r00151.png]]

Figure 2, New Design Oil Manifold Installation.

**Reason for Change**

The new design oil manifold rotates the solenoid mounting location by 180°. In this orientation, cooling oil is gravity fed to the solenoid coil, reducing coil temperature and therefore the risk of malfunction.

**Service Instructions**

Order upfit kit, Part Number [[6468466]] and solenoid valve, Part Number [[3641305]], before attempting to carry out this repair. Check part quantities delivered in the parts kit, as per Table 1, Service Parts. Remove the five male – male unions/ adapters from the existing manifold. Re-use these unions/ connectors. O-rings will be provided in the parts kit.

To replace the fan clutch oil control manifold and solenoid, see corresponding Service Manual. Reference Procedure 007-125 in Section 7.

- GTA38, K38, K50 QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]
- QSK50 CM2350 K108 Service Manual, Bulletin 4332823
- QSK50 CM2350 K130 Service Manual, Bulletin 5504180

Following installation of the fan clutch oil control manifold and solenoid, the solenoid wiring harness **must** be re-routed to allow connector alignment with the new solenoid position. This process differs for Tier 2 and Tier 4 engines. Verify the route required and re-route as shown in Figure 5.

QSK50 CM2150 MCRS Engines:

- Remove the solenoid harness from the shared P-clip, holding the solenoid harness and the engine harness, to the rocker cover (circled yellow). Cut the cable tie securing the solenoid harness to the existing engine harness. Figure 3 shows the existing route for Tier 2 engines.

![[16r00152.png]]

Figure 3, Tier 2 Engine Wiring Harness Routing.

QSK50 CM2350 K108/ K130 Engines:

- Figure 4 shows the exisiting Tier 4 solenoid harness route, which has an engine harness P-clipped to it on the rocker cover. Remove the solenoid harness from the engine harness P-clip.

![[16r00153.png]]

Figure 4, Tier 4 Engine Wiring Harness Route.

All Engines:

- Secure existing Tier 2 and Tier 4 non-solenoid harnesses as per the original installation.
- Re-route the solenoid harness to the new solenoid position. Figure 6 shows the required new route using two P-clips (part number 68152A) on existing gear cover capscrew locations across both Tier 2 and Tier 4 engines.
- Remove two gear cover capscrews and install the solenoid harness through the P-clips, vertically upwards as shown.
- Install the capscrews.

> [!tip] Момент затяжки · Torque Value
> 75 n•m [55 ft-lb]

![[16r00154.png]]

Figure 5, New Solenoid Harness Routing.

- Connect the wiring harness to the solenoid plug. Verify a positive “click” as the connector fork slots over the plug and locks in position to avoid backing out.

**Service Parts Availability**

Service parts are available in kit form. See Table 1 for part numbers contained within the parts kit.

| Table 1, Service Parts |  |  |  |  |  |
|---|---|---|---|---|---|
| Part Description | Existing Part Number | Obsolete | Superseded | New Part Number | Part Quantity |
| MANIFOLD, OIL | [[3640889]] | Yes | Yes | [[6414133]] | 1 |
| SCREW, SOCKET HEAD CAP | S143B | No | No | - | 2 |
| WASHER, LOCK | S604 | No | No | - | 2 |
| GASKET, CORROSION RESISTOR | [[3650106]] | No | No | - | 1 |
| PLUG, PIPE | [[3008466]] | No | No | - | 2 |
| PLUG, THREADED | [[3046202]] | No | No | - | 2 |
| PLUG, THREADED | [[3037536]] | No | No | - | 1 |
| CLIP | 68152A | No | No | - | 2 |
| SEAL, O RING | [[3348871]] | No | No | - | 2 |
| SEAL, O RING | [[3627695]] | No | No | - | 2 |
| SEAL, O RING | [[3089240]] | No | No | - | 2 |
| SEAL, O RING | [[3630740]] | No | No | - | 2 |
| SEAL, O RING | [[3922794]] | No | No | - | 1 |
| SEAL, O RING | [[3037537]] | No | No | - | 1 |

**Part Compatibility**

The new oil manifold is common across the QSK50 Tier 2 and Tier 4, as was the existing design. New and existing oil manifolds are backwards compatible. The new manifold is advised for expected fan solenoid operation and service life.

**Part Identification**

The new oil manifold is different in shape to the existing part, allowing the oil control solenoid to sit upside down. The new part number is stamped in the location shown in Figure 6 The existing part number is stamped exactly 180° opposite to this on the bottom face. Both part numbers are stamped on the face opposite to the solenoid when viewed as installed.

![[16r00155.png]]

Figure 6, Part Number Stamping Location on New Fan Clutch Oil Manifold.

**Part Inventory Action**

Obsolete part numbers in stock are **not** to be used.

**Production Status**

Implemented for production. See Table 2.

| Table 2, Production Information |  |  |
|---|---|---|
| ESN First | Build Date 1 | Plant |
| 33231741 | 8 April 2023 | Daventry Engine Plant |
| 1 Engine build date can be found on engine dataplate. |  |  |

**Publications Affected**

| Table 3, Publications Affected |  |  |  |  |  |
|---|---|---|---|---|---|
| Manual Type | Engine | Bulletin Number | Procedure Title | Procedure | Section |
| Service Manual | QSK50 CM2150 MCRS | [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] | Fan Clutch Lubricating Oil Manifold | [[28-007-125 — Fan Clutch Lubricating Oil Manifold\|Refer to Procedure 007-125]] | 7 |
| Service Manual | QSK50 CM2350 K130 | 5504180 | Fan Clutch Lubricating Oil Manifold | Refer to Procedure 007-125 | 7 |
| Service Manual | QSK50 CM2350 K108 | 4332823 | Fan Clutch Lubricating Oil Manifold | Refer to Procedure 007-125 | 7 |

### Document History

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3008466]] | PIPE PLUG | Трубная пробка |
| [[3037536]] | THREADED PLUG | Резьбовая пробка |
| [[3037537]] | O RING SEAL | Уплотнительное кольцо |
| [[3046202]] | THREADED PLUG | Резьбовая пробка |
| [[3089240]] | O RING SEAL | Уплотнительное кольцо |
| [[3348871]] | O RING SEAL | Уплотнительное кольцо |
| [[3627695]] | O RING SEAL | Уплотнительное кольцо |
| [[3630740]] | O RING SEAL | Уплотнительное кольцо |
| [[3640889]] | OIL MANIFOLD | Масляный коллектор |
| [[3641305]] | SOLENOID VALVE | Электромагнитный клапан |
| [[3650106]] | CORROSION RESISTOR GASKET | Прокладка антикоррозионного фильтра |
| [[3922794]] | O RING SEAL | Уплотнительное кольцо |
| [[6414133]] | OIL MANIFOLD | Масляный коллектор |
| [[6468466]] | Upfit Kit | Комплект дооснащения |
