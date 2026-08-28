---
aliases:
  - "Измерение прорыва газов в картер"
type: "Процедура"
doc: "100-014-010"
title_en: "Crankcase Blowby, Measure"
title_ru: "Измерение прорыва газов в картер"
modified: "2026-02-12"
engines:
  - "93047320"
  - "93058669"
  - "93087701"
families:
  - "6B5.9"
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
  - "3666087"
parts:
  - "3089567"
figures: 27
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-014-010.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-014-010.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "двигатель/C8.3"
  - "группа/100"
---

# Crankcase Blowby, Measure
**Измерение прорыва газов в картер**

> [!abstract] Процедура · `100-014-010`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** 6B5.9, C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]], [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 14 - Engine Testing · Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2026-02-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-014-010.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-014-010.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Water manometer, Part Number ST 1111-3, or equivalent
- Blowby tool, Part Number 3822476 or 3822566
- Straight thread plug, Part Number [[3089567]]
- Oil fill adapter, Part Number 3990099.

#### Additional Service Items

- No additional service items required.

### General Information

Excessive crankcase blowby can indicate an engine or engine-related component malfunction that allows combustion gases or air to enter the crankcase. This blowby results in the buildup of higher than normal crankcase pressure, which results in increased levels of blowby.

This procedure describes how to measure crankcase blowby and how to determine what component is malfunctioning.

Blowby is typically measured for the following situations:

- Verifying engine break-in after an engine rebuild
- Troubleshooting for excessive lubricating oil out of the crankcase breather tube, commonly referred to as oil carryover (for open crankcase ventilation systems)
- Troubleshooting oil in the air intake system (for closed crankcase ventilation systems)
- Troubleshooting high crankcase pressure (for engines equipped with a crankcase pressure sensor)
- Troubleshooting possible internal engine damage (worn piston rings, valve stem seals, or guides, etc.).

For specific crankcase gases (blowby) symptom information and direction, see the Crankcase Gases (Blowby) Excessive troubleshooting symptom tree in Section TS of the appropriate engine service manual.

The following measure step will give general guidelines for measuring blowby relative to the above situations.

> [!note] Note · Примечание
> Some illustrations in this procedure do **not** show actual engine configurations. However, the procedure is the same.

![[pi900ka.png]]

The terms blowby and carryover (oil out of the breather tube) are commonly used interchangeably.

When measuring blowby, and there is an excessive amount of oil coming out of the breather tube, the quantity of oil can affect the blowby measurement.

The blowby measurement is affected by the oil collecting on the orifice of the blowby measurement service tool. This oil reduces the size of the orifice, which results in higher than actual blowby measurements.

If this condition occurs,:

- Find a different location on the engine to measure blowby (oil fill, oil fill cap, unused turbocharger drain location, etc.)
- Clean any oil residue from the breather. Dry thoroughly before measuring blowby
- Determine if there is an issue causing the breather to be flooded with oil, for example:
- Incorrect oil level
- Vehicle operation (excessive angularity, excessive engine side-to-side movement)
- Internal engine components deflecting oil toward the breather cavity (piston cooling nozzles, accessory oil drains, etc.)
- Determine if another breather option is available for the engine being serviced.

![[07900050.png]]

The tools used to measure blowby are similar in design. The difference between the tools is in the size of the orifice. Different size orifices are available to more accurately measure blowby by accommodating the wide variety of engine configurations and ratings. Engine blowby is dependent on the volume of intake airflow.

For example:

If measuring blowby on two identically configured and sized engines, but the horsepower ratings and rated speed are different, the maximum blowby values measured will be different.

The engine with the higher horsepower rating and rated speed will have a higher volume of intake airflow, which will result in higher blowby. If the smaller orifice blowby tool was used on the engine with a higher horsepower rating and rated speed, the measurement can exceed the limits of the pressure measuring tool.

| Blowby Tool Part Number | Orifice Size mm \[ in \] |
|---|---|
| 3822476 | 5.61 mm \[ 0.221 in \] |
| 3822566 | 7.67 mm \[ 0.302 in \] |

![[eg8toga.png]]

To measure the crankcase blowby pressure, connect water manometer, Part Number ST1111-3, or equivalent, pressure gauge, or transducer to the blowby tool.

Water manometer, Part Number ST1111-3, can measure a maximum of 944 mm \[ 36 in \] of water.

![[eg8toga.png]]

The following charts show the relationship of measured pressure to flow rate, depending on the blowby tool used.

| Blowby Conversion Table (5.61 mm \[ 0.221 in \] orifice, Blowby Tool, Part Number 3822476) |  |
|---|---|
| mm \[ in \] of H 2 O | Liter \[ cfm \] per Minute |
| 25.4 \[ 1 \] | 27 \[ 0.953 \] |
| 50.8 \[ 2 \] | 40 \[ 1.413 \] |
| 76.2 \[ 3 \] | 48 \[ 1.695 \] |
| 101.6 \[ 4 \] | 58 \[ 2.048 \] |
| 127 \[ 5 \] | 64 \[ 2.260 \] |
| 152.4 \[ 6 \] | 71 \[ 2.507 \] |
| 177.8 \[ 7 \] | 76 \[ 2.684 \] |
| 203.2 \[ 8 \] | 81 \[ 2.860 \] |
| 228.6 \[ 9 \] | 86 \[ 3.037 \] |
| 254 \[ 10 \] | 90 \[ 3.178 \] |
| 279.4 \[ 11 \] | 94 \[ 3.320 \] |
| 304.8 \[ 12 \] | 98 \[ 3.461 \] |
| 330.2 \[ 13 \] | 102 \[ 3.602 \] |
| 355.6 \[ 14 \] | 105 \[ 3.708 \] |
| 381 \[ 15 \] | 109 \[ 3.849 \] |
| 406.4 \[ 16 \] | 112 \[ 3.955 \] |
| 431.8 \[ 17 \] | 115 \[ 4.061 \] |
| 457.2 \[ 18 \] | 118 \[ 4.167 \] |
| 482.6 \[ 19 \] | 121 \[ 4.723 \] |
| 508 \[ 20 \] | 124 \[ 4.379 \] |
| 533.4 \[ 21 \] | 128 \[ 4.520 \] |
| 558.2 \[ 22 \] | 131 \[ 4.626 \] |
| 584.2 \[ 23 \] | 135 \[ 4.767 \] |
| 609.6 \[ 24 \] | 137 \[ 4.838 \] |
| 635 \[ 25 \] | 140 \[ 4.944 \] |
| 660.4 \[ 26 \] | 144 \[ 5.085 \] |
| 685.8 \[ 27 \] | 147 \[ 5.191 \] |
| 711.2 \[ 28 \] | 150 \[ 5.297 \] |
| 736.6 \[ 29 \] | 154 \[ 5.438 \] |
| 762 \[ 30 \] | 157 \[ 5.544 \] |
| 787.4 \[ 31 \] | 160 \[ 5.650 \] |
| 812.8 \[ 32 \] | 163 \[ 5.756 \] |
| 838.2 \[ 33 \] | 166 \[ 5.862 \] |
| 863.6 \[ 34 \] | 169 \[ 5.968 \] |
| 889 \[ 35 \] | 172 \[ 6.074 \] |

| Blowby Conversion Table (7.67 mm \[ 0.302 in \] orifice, Blowby Tool, Part Number 3822566) |  |
|---|---|
| mm \[ in \] of H 2 O | Liter \[ cfm \] per Minute |
| 25.4 \[ 1 \] | 50 \[ 1.766 \] |
| 50.8 \[ 2 \] | 84 \[ 2.966 \] |
| 76.2 \[ 3 \] | 103 \[ 3.637 \] |
| 101.6 \[ 4 \] | 119 \[ 4.202 \] |
| 127 \[ 5 \] | 133 \[ 4.697 \] |
| 152.4 \[ 6 \] | 145 \[ 5.121 \] |
| 177.8 \[ 7 \] | 155 \[ 5.474 \] |
| 203.2 \[ 8 \] | 164 \[ 5.792 \] |
| 228.6 \[ 9 \] | 172 \[ 6.074 \] |
| 254 \[ 10 \] | 180 \[ 6.357 \] |
| 279.4 \[ 11 \] | 187 \[ 6.604 \] |
| 304.8 \[ 12 \] | 193 \[ 6.816 \] |
| 330.2 \[ 13 \] | 200 \[ 7.063 \] |
| 355.6 \[ 14 \] | 206 \[ 7.275 \] |
| 381 \[ 15 \] | 211 \[ 7.451 \] |
| 406.4 \[ 16 \] | 217 \[ 7.663 \] |
| 431.8 \[ 17\] | 222 \[ 7.840 \] |
| 457.2 \[ 18 \] | 226 \[ 7.981 \] |
| 482.6 \[ 19 \] | 229 \[ 8.087 \] |
| 508 \[ 20 \] | 235 \[ 8.299 \] |
| 533.4 \[ 21 \] | 239 \[ 8.440 \] |
| 558.8 \[ 22 \] | 242 \[ 8.546 \] |
| 584.2 \[ 23 \] | 246 \[ 8.687 \] |
| 609.6 \[ 24 \] | 248 \[ 8.758 \] |

The following chart contains general blowby specifications for MidRange engines. Due to the wide variety of engine types, configurations, and ratings, these specifications are intended to **only** be used as a guide to help identify if a problem exists. These specifications are **not** intended to be used as engine condemnation limits.

If internal engine damage is suspected to be the cause of the excessive blowby condition, other steps can be taken to confirm this damage.

Measuring blowby **must only** be considered when confirming engine break-in after a rebuild or if another symptom is present. These symptoms can include:

- Excessive carryover (oil out of the crankcase breather tube)
- High crankcase pressure (for engines equipped with a crankcase pressure sensor)
- Low power
- Oil consumption
- Exhaust smoke.

If no other symptom is present, blowby measurements need **not** be taken.

![[pi900ka.png]]

If internal engine damage is suspected to be the cause of the excessive blowby condition, other steps can be taken to confirm this damage. The steps include:

- Confirm engine maintenance practices
- Cut the oil filter open and check for debris
- Take an oil sample and inspect for contamination.

![[lf9etba.png]]

| MidRange Blowby Specifications Chart |  |  |  |  |
|---|---|---|---|---|
|  | Blowby Specification For New or Rebuild - mm \[ in \] H 2 O | Blowby Specification For Troubleshooting - mm \[ in \] H 2 O |  |  |
| Engine Model | Blowby Tool 3822476-5.61 mm \[ 0.221 in \] Orifice | Blowby Tool 3822566-7.67 mm \[ 0.302 in \] Orifice | Blowby Tool 3822476-5.61 mm \[ 0.221 in\] Orifice | Blowby Tool 3822566-7.67 mm \[ 0.302 in \] Orifice |
| A1400 and A1700 (Naturally Aspirated) | 25.4 \[ 1 \] | - | 25.4 \[ 1 \] | - |
| A2000 and A2300 (Naturally Aspirated) | 25.4 \[ 1 \] | - | 38.1 \[ 1.5 \] | - |
| A2000 and A2300 (Turbocharged) | 38.1 \[ 1.5 \] | - | 50.8 \[ 2 \] | - |
| ISF2.8 | 147.3 \[ 5.8 \] | - | 711.2 \[ 28 \] | - |
| ISF3.8 | - | 71.1 \[ 2.8 \] | - | 254 \[ 10 \] |
| B3.3 Tier 1, 2 | - | 50.8 \[ 2 \] | - | 101.6 \[ 4 \] |
| B3.3, QSB3.3 Tier 3 | - | 101.6 \[ 4 \] | - | 152.04 \[ 6 \] |
| B3.3, QSB3.3 Tier 4 Interim (Less than 74 HP) | - | 50.8 \[ 2 \] | - | 101.6 \[ 4 \] |
| B3.9, QSB3.9-30, B4.5, QSB4.5-30, and B4.5 s (Naturally Aspirated) (Less than 250 hp) | 25.4 \[ 1 \] | - | 76.2 \[ 3 \] | - |
| B3.9, QSB3.9-30, B4.5, QSB4.5-30, and B4.5 s (Turbocharged) (Less than 250 hp) | 101.6 \[ 4 \] | - | 431.8 \[ 17 \] | - |
| B3.9, QSB3.9-30, B4.5, QSB4.5-30, and B4.5 s (Turbocharged) (Greater than 250 hp) | - | 25.4 \[ 1 \] | - | 127 \[ 5 \] |
| B5.9 (Naturally Aspirated) | 50.8 \[ 2 \] | - | 152.4 \[ 6 \] | - |
| B5.9, and QSB5.9-30, (Less than 250 hp) | 228.6 \[ 9 \] | - | 635 \[ 25 \] | - |
| B5.9, and QSB5.9-30, (Greater than 250 hp) | - | 50.8 \[ 2 \] | - | 228.6 \[ 9 \] |
| ISB, ISB e, QSB e, ISD e, QSB5.9-44, ISB6.7, QSB6.7, B6.7 | - | - | - | 254 \[ 10 \] |
| C8.3 | - | 203 \[ 8 \] | - | 457 \[ 18 \] |
| ISB5.9 G CM2180, ISC, ISC e, QSC8.3, ISL, ISL e, L9, L9N, and QSL9 | - | 203.2 \[ 8 \] | - | 304.8 \[ 12 \] |
| B Gas International, B Gas Plus, B LPG Plus, B5.9G, B5.9 LPG | 228.6 \[ 9 \] | - | 889 \[ 35 \] | - |
| C8.3G, C Gas Plus, ISL G, L Gas Plus | - | 203 \[ 8 \] | - | 457 \[ 18 \] |
| ISB4.5 CM2350 B104 | 152.4 \[ 6 \] | - | 330.2 \[ 13 \] | - |

### Initial Check

> [!note] Note · Примечание
> The location and type of crankcase breathers vary by engine configuration (Front Gear Train or Rear Gear Train) and/or engine application (Marine, Industrial, and Automotive).

Prior to measuring blowby pressure, check the crankcase breather tube for obstructions.

- Use the following procedure in the C Series Engines Troubleshooting and Repair Manual, Bulletin [[3666003 — C Troubleshooting and Repair Manual\|3666003]]. [[100-003-018 — Crankcase Breather Tube|Refer to Procedure 003-018 in Section 3.]]
- Use the following procedure in the B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual, Bulletin [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual\|3666087]]. [[40-003-018-tr — Crankcase Breather Tube|Refer to Procedure 003-018 in Section 3.]]
- Use the following procedure in the ISB and QSB5.9-44 Engines Troubleshooting and Repair Manual, Bulletin 3666193. [[100-003-018 — Crankcase Breather Tube|Refer to Procedure 003-018 in Section 3.]]
- Use the following procedure in the ISBe, ISB, and QSB (Common Rail Fuel System) Service Manual, Bulletin 4021271. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the Industrial QSB3.9-30, QSB4.5-30, and QSB5.9-30 Series Engines Troubleshooting and Repair Manual, Bulletin 4021398. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the ISC, ISCe, QSC8.3, ISL, ISLe3, ISLe4 and QSL9 Engines Troubleshooting and Repair Manual, Bulletin 4021418. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the B3.3 and QSB3.3 CM2150 Service Manual, Bulletin 4021540. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the ISC and ISL CM2150 Service Manual, Bulletin 4021569. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the ISB CM2100 and CM2150 Service Manual, Bulletin 4021578. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the ISBe and ISDe CM2150 Service Manual, Bulletin 4021597. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the ISLe CM2150 Service Manual, Bulletin 4021630. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the ISL G CM2180 Service Manual, Bulletin 4021649. Refer to Procedure 003-018 in Section 3.
- Reference the ISF3.8 CM2220, ISF3.8 CM2220 AN and ISF3.8 CM2220 IAN Service Manual, Bulletin 4021704.
- Use the following procedure in the ISB4.5, ISB6.7, ISD4.5 and ISD6.7 CM2150 SN Service Manual, Bulletin 4022188. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the B4.5s and B6.7s Series Engines Troubleshooting and Repair Manual, Bulletin 4095243. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the ISF2.8 CM2220, ISF2.8 CM2220E, ISF2.8 CM2220 AN and ISF2.8 CM2220 IAN Service Manual, Bulletin 4022178. Refer to Procedure 003-024 in Section 3. Refer to Procedure 003-026 in Section 3.
- Use the following procedure in the ISB6.7 CM2250 Service Manual, Bulletin 4022254. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the ISB6.7 CM2350 B101 Service Manual, Bulletin 2883567. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the ISB4.5 CM2350 B104 Service Manual, Bulletin 4332646. Refer to Procedure 003-024 in Section 3.
- Use the following procedure in the ISB6.7 CM2350 B103 Service Manual, Bulletin 4332641. Refer to Procedure 003-024 in Section 3.
- Use the following procedure in the QSB6.7 CM2350 B105 and B6.7 CM2450 B232C Service Manual, Bulletin 4332778. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the QSL9 CM2350 L102 and L9 CM2450 L181C Service Manual, Bulletin 4332796. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the ISF3.8 CM2220 L110 Service Manual, Bulletin 4358480. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the ISL9 CM2350 L101 Service Manual, Bulletin 4310787. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the QSL9 M CM2250 L106 and L9 CM2450 L170M Service Manual, Bulletin 4358343. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the QSB6.7 CM2350 B112 Service Manual, Bulletin 4358498. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the ISB/ISD6.7 CM2880 B126 Service Manual, Bulletin 4383693. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the QSL9 CM2250 L115 Service Manual, Bulletin 4388626. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the L9 CM2350 L116B Service Manual, Bulletin 5411330. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the L9N CM2380 L124B Service Manual, Bulletin 5467492. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the ISB5.9 G CM2180 Service Manual, Bulletin 2883369. Refer to Procedure 003-018 in Section 3.
- Use the following procedure in the F2.8 CM2620 F135B Service Manual, Bulletin 5504616. Refer to Procedure 003-026 in Section 3.
- Use the following procedure in the F2.8 CM2620 F136B Service Manual, Bulletin 5504621. Refer to Procedure 003-026 in Section 3.
- Use the following procedure in the R2.8 CM2220 R102C Service Manual, Bulletin 6457240. Refer to Procedure 003-024 in Section 3.

![[03d00059.png]]

If troubleshooting a complaint of excessive oil out of the breather tube, removing the breather components can be necessary to clean and remove any lubricating oil buildup before performing any blowby measurements.

![[03d00059.png]]

Check the engine oil level and, if necessary, proper calibration of the dipstick. Level too high can cause a higher than normal blowby pressure and/or excessive carryover.

- Use the following procedure in the C Series Engines Troubleshooting and Repair Manual, Bulletin [[3666003 — C Troubleshooting and Repair Manual\|3666003]]. [[100-007-011 — Lubricating Oil Dipstick Tube|Refer to Procedure 007-011 in Section 7.]]
- Use the following procedure in the B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual, Bulletin [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual\|3666087]]. [[40-007-011-tr — Lubricating Oil Dipstick Tube|Refer to Procedure 007-011 in Section 7.]]
- Use the following procedure in the ISB and QSB5.9-44 Engines Troubleshooting and Repair Manual, Bulletin 3666193. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISBe, ISB, and QSB (Common Rail Fuel System) Service Manual, Bulletin 4021271. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the Industrial QSB3.9-30, QSB4.5-30, and QSB5.9-30 Series Engines Troubleshooting and Repair Manual, Bulletin 4021398. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISC, ISCe, QSC8.3, ISL, ISLe3, ISLe4 and QSL9 Engines Troubleshooting and Repair Manual, Bulletin 4021418. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the B3.3 and QSB3.3 CM2150 Service Manual, Bulletin 4021540. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISC and ISL CM2150 Service Manual, Bulletin 4021569. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISB CM2100 and CM2150 Service Manual, Bulletin 4021578. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISBe and ISDe CM2150 Service Manual, Bulletin 4021597. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISLe CM2150 Service Manual, Bulletin 4021630. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISL G CM2180 Service Manual, Bulletin 4021649. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISF3.8 CM2220, ISF3.8 CM2220 AN and ISFF3.8 CM2220 IAN Service Manual, Bulletin 4021704. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISB4.5, ISB6.7, ISD4.5 and ISD6.7 CM2150 SN Service Manual, Bulletin 4022188. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISF2.8 CM2220, ISF2.8 CM2220E, ISF2.8 CM2220 AN, and ISF2.8 CM2220 IAN Service Manual, Bulletin 4022178. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISB6.7 CM2250 Service Manual, Bulletin 4022254. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISB6.7 CM2350 B101 Service Manual, Bulletin 2883567. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISB4.5 CM2350 B104 Service Manual, Bulletin 4332646. [[99-007-043-tr — Lubricating Oil Level|Refer to Procedure 007-043 in Section 7.]]
- Use the following procedure in the ISB6.7 CM2350 B103 Service Manual, Bulletin 4332641. [[99-007-043-tr — Lubricating Oil Level|Refer to Procedure 007-043 in Section 7.]]
- Use the following procedure in the QSB6.7 CM2350 B105 and B6.7 CM2450 B232C Service Manual, Bulletin 4332778. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the QSL9 CM2350 L102 and L9 CM2450 L181C Service Manual, Bulletin 4332796. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISF3.8 CM2220 F110 Service Manual, Bulletin 4358480. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the ISL9 CM2350 L101 Service Manual, Bulletin 4310787. Refer to Procedure 007-037 in Section 7.
- Use the following procedure in the QSL9 M CM2250 L106 and L9 CM2450 L170M Service Manual, Bulletin 4358343. Refer to Procedure 007-037 in Section 7.
- Use the following procedure in the QSB6.7 CM2350 B112 Service Manual, Bulletin 4358498. Refer to Procedure 007-011 in Section 7.
- Use the following procedure in the QSB6.7 CM2350 B112 Service Manual, Bulletin 4358498. Refer to Procedure 007-037 in Section 7.
- Use the following procedure in the ISB/ISD6.7 CM2880 B126 Service Manual, Bulletin 4383693. Refer to Procedure 007-037 in Section 7.
- Use the following procedure in the QSL9 CM2250 L115 Service Manual, Bulletin 4388626. Refer to Procedure 007-037 in Section 7.
- Use the following procedure in the L9 CM2350 L116B Service Manual, Bulletin 5411330. Refer to Procedure 007-037 in Section 7.
- Use the following procedure in the L9N CM2380 L124B Service Manual, Bulletin 5467492. Refer to Procedure 007-037 in Section 7.
- Use the following procedure in the ISB5.9 G CM2180 Service Manual, Bulletin 2883369. [[100-007-037 — Lubricating Oil System|Refer to Procedure 007-037 in Section 7.]]
- Use the following procedure in the F2.8 CM2620 F135B Service Manual, Bulletin 5504616. Refer to Procedure 007-037 in Section 7.
- Use the following procedure in the F2.8 CM2620 F136B Service Manual, Bulletin 5504621. Refer to Procedure 007-037 in Section 7.
- Use the following procedure in the R2.8 CM2220 R102C Service Manual, Bulletin 6457240. Refer to Procedure 007-037 in Section 7.

![[lg900wa.png]]

### Measure

Choose the appropriate blowby measurement service tool to use for the engine being serviced. See the MidRange Blowby Specifications Chart in this procedure. Determine the appropriate blowby measurement service tool to use, based on engine type and/or horsepower.

| Blowby Tool Part Number | Orifice Size mm \[ in \] |
|---|---|
| 3822476 | 5.61 mm \[ 0.221 in \] |
| 3822566 | 7.67 mm \[ 0.302 in \] |

> [!note] Note · Примечание
> Either service tool can be used to measure blowby, as long as the blowby measurement is correctly matched to the correct flow rate. See the flow rate conversion tables in this procedure for the correct orifice.

![[14900103.png]]

To measure the crankcase blowby pressure, connect water manometer, Part Number ST 1111-3, pressure gauge, or transducer to the blowby measurement service tool.

> [!note] Note · Примечание
> The location of the crankcase breather tube can vary by engine configuration (front gear train or rear gear train) and/or application (Marine, Industrial, and Automotive). See Section E for crankcase breather tube locations.

Install the appropriate blowby service tool(s):

- For typical open crankcase breather/ventilation systems, connect the appropriate blowby service tool to the end of the crankcase breather tube. See the MidRange Blowby Specification Chart in this procedure. Connect a water manometer, pressure gauge, or transducer to the blowby service tool.
- For engines with closed crankcase ventilation systems (without a crankcase ventilation filter), disconnect the breather tube and plug the intake manifold or turbocharger compressor housing port. See the MidRange Blowby Specification Chart in this procedure. Connect the appropriate blowby service tool to the end of the crankcase breather tube. Connect a water manometer, pressure gauge, or transducer to the blowby service tool.
- For crankcase breather/ventilation systems with crankcase ventilation filters, follow the proceeding steps on connecting the blowby measurement equipment.

![[14d00017.png]]

For ISB CM2150 engines that have the crankcase ventilation filter located on top of the rocker lever cover, use the following steps to connect the blowby measurement tools.

- Disconnect the crankcase ventilation line from the turbocharger/original equipment manufacturer (OEM) intake plumbing. If the crankcase ventilation line is connected to the turbocharger housing, remove the inlet fitting.

![[14900094.png]]

- If the crankcase ventilation line is connected to the turbocharger housing, install straight thread plug, Part Number [[3089567]]. Plug the crankcase ventilation line with a suitable fitting.

> [!note] Note · Примечание
> If the crankcase ventilation line is connected to the OEM intake plumbing (**not** shown), use a suitable fitting to plug the port in the intake plumbing. Also plug the crankcase ventilation line coming from the engine with a suitable fitting.

![[14900095.png]]

- Remove the oil fill cap from the rocker lever cover. Install oil fill adapter, Part Number 3990099.

![[14900096.png]]

- Connect the appropriate blowby service tool to the outlet of the oil fill adapter. See the MidRange Blowby Specification Chart in this procedure. Connect a water manometer, pressure gauge, or transducer to the blowby service tool.

![[14900097.png]]

For engines that have the crankcase ventilation filter located at the rear of the engine, use the following steps to connect the blowby measurement tools.

- Disconnect the crankcase ventilation line from the crankcase ventilation filter housing. Plug or cap the crankcase ventilation filter housing.

![[14900098.png]]

- Connect the appropriate blowby service tool to the crankcase ventilation line exiting the flywheel housing. See the MidRange Blowby Specifications in this procedure. Connect a water manometer, pressure gauge, or transducer to the blowby service tool.

![[14900099.png]]

For engines that have crankcase ventilation filter located on top of the rocker lever cover, use the following steps to connect blowby measurement tools.

- Remove the oil fill cap from the rocker lever cover. Install oil fill adapter, Part Number 3990099.

![[14900096.png]]

Connect the appropriate blowby service tool to the outlet of the oil fill adapter. See the MidRange Blowby Specification Chart in this procedure. Connect a water manometer, pressure gauge, or transducer to the blowby service tool.

![[14900097.png]]

- Use a suitable fitting to plug the crankcase breather tube.

![[14r00016.png]]

For ISC and ISL CM2150 and QSL CM2250 engines, use the following steps to connect the blowby measurement tools.

- Remove the oil fill cap from the rocker lever cover. Install oil fill adapter, Part Number 3990099.

![[14900100.png]]

- Connect the appropriate blowby service tool to the outlet of the oil fill adapter. See the MidRange Blowby Specification Chart in this procedure. Connect a water manometer, pressure gauge, or transducer to the blowby service tool.

![[14900101.png]]

- Use a suitable fitting to plug the crankcase breather tube.

![[14900102.png]]

Engine Blowby Contribution:

Operate the engine at rated speed and under load by:

- For engine run-in, a chassis dynamometer or engine dynamometer
- For engine testing, a chassis dynamometer or engine dynamometer
- A stall speed test (for engines equipped with automatic transmissions **only**).

![[oi902vk.png]]

> [!warning] CAUTION · Осторожно
> When measuring blowby and there is an excessive amount of oil coming out of the breather tube, the quantity of oil can affect the blowby measurement.

Operate the engine at rated rpm and full load until a steady reading is obtained.

> [!note] Note · Примечание
> When measuring blowby, the value can “spike” initially as the engine reaches peak power and rated speed. Wait for the blowby measurement to stabilize before taking a reading.

> [!note] Note · Примечание
> For engine run-in, if a sudden increase in blowby occurs, or if blowby exceeds the maximum allowable limit during any run-in step, return to the previous step and continue the run-in. If blowby does **not** reach an acceptable level, discontinue the run-in and determine the cause.

Record the steady blowby measurement.

Remove the engine blowby service tool if the blowby is within specification.

![[eg8toja.png]]

Exhaust Brake Blowby Contribution:

> [!note] Note · Примечание
> **Not** all vehicles are equipped with an exhaust brake.

With the engine blowby service tool still installed, measure blowby pressure during exhaust brake operation, if equipped.

Operate the vehicle going down a long inclined road such as a highway or interstate off ramp. Begin exhaust brake operation at rated engine speed while measuring blowby pressure during exhaust brake operation.

![[20900002.png]]

Also, measure exhaust back pressure during exhaust brake operation.

Operate the engine until a steady reading is obtained.

> [!note] Note · Примечание
> When measuring blowby, the value can “spike” initially as the engine reaches peak power and rated speed. Wait for the blowby measurement to stabilize before taking a reading.

If blowby pressure is above specification during exhaust brake operation and exhaust back pressure is above specification, repair or replace the exhaust brake. See manufacturer instructions.

Remove the engine blowby service tool.

Remove the pressure gauge used to measure exhaust back pressure during exhaust brake operation.

Install a plug in the test port.

![[11d00020.png]]

Base Engine Component Blowby Contribution:

Base engine components can also be contributing factors of increased crankcase blowby and higher than normal crankcase pressure. See the Crankcase Gases (Blowby) Excessive troubleshooting symptom tree in Section TS of the appropriate engine service manual to evaluate the remaining possible causes for increased blowby and higher than normal crankcase pressure. The following are listed as possible base engine component causes:

Valve stem clearance is excessive or the valve stem seals are damaged.

- Use the following procedure in the C Series Engines Troubleshooting and Repair Manual, Bulletin [[3666003 — C Troubleshooting and Repair Manual\|3666003]]. [[41-002-004-tr — Cylinder Head|Refer to Procedure 002-004 in Section 2.]]
- Use the following procedure in the B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual, Bulletin [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual\|3666087]]. [[40-002-004-tr — Cylinder Head|Refer to Procedure 002-004 in Section 2.]]
- Use the following procedure in the ISB and QSB5.9-44 Engines Troubleshooting and Repair Manual, Bulletin 3666193. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISBe, ISB, and QSB (Common Rail Fuel System) Service Manual, Bulletin 4021271. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the Industrial QSB3.9-30, QSB4.5-30, and QSB5.9-30 Series Engines Troubleshooting and Repair Manual, Bulletin 4021398. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISC, ISCe, QSC8.3, ISL, ISLe3, ISLe4 and QSL9 Engines Troubleshooting and Repair Manual, Bulletin 4021418. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISC and ISL CM2150 Service Manual, Bulletin 4021569. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB CM2100 and CM2150 Service Manual, Bulletin 4021578. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISBe and ISDe CM2150 Service Manual, Bulletin 4021597. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISLe CM2150 Service Manual, Bulletin 4021630. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISL G CM2180 Service Manual, Bulletin 4021649. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISF3.8 CM2220, ISF3.8 CM2220 AN and ISF3.8 CM2220 IAN Service Manual, Bulletin 4021704. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISF2.8 CM2220, ISF2.8 CM2220 E, ISF2.8 CM2220 AN and ISF2.8 CM2220 IAN Service Manual, Bulletin 4022178. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB4.5, ISB6.7, ISD4.5 and ISD6.7 CM2150 SN Service Manual, Bulletin 4022188. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB6.7 CM2250 Service Manual, Bulletin 4022254. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB6.7 CM2350 B101 Service Manual, Bulletin 2883567. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB4.5 CM2350 B104 Service Manual, Bulletin 4332646. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB6.7 CM2350 B103 Service Manual, Bulletin 4332641. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the QSB6.7 CM2350 B105 and B6.7 CM2450 B232C Service Manual, Bulletin 4332778. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the QSL9 CM2350 L102 and L9 CM2450 L181C Service Manual, Bulletin 4332796. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISF3.8 CM2220 F110 Service Manual, Bulletin 4358480. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISL9 CM2350 L101 Service Manual, Bulletin 4310787. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the QSL9 M CM2250 L106 and L9 CM2450 L170M Service Manual, Bulletin 4358343. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the QSB6.7 CM2350 B112 Service Manual, Bulletin 4358498. Refer to Procedure 002-004 in Section 12.
- Use the following procedure in the ISB/ISD6.7 CM2880 B126 Service Manual, Bulletin 4383693. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the QSL9 CM2250 L115 Service Manual, Bulletin 4388626. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the L9 CM2350 L116B Service Manual, Bulletin 5411330. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the B6.7 CM2350 B121B Service Manual, Bulletin 5411223. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB5.9 G CM2180 Service Manual, Bulletin 2883369. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the R2.8 CM2220 R102C Service Manual, Bulletin 6457240. Refer to Procedure 002-004 in Section 2.

Cylinder head valve guides are excessively worn.

- Use the following procedure in the C Series Engines Troubleshooting and Repair Manual, Bulletin [[3666003 — C Troubleshooting and Repair Manual\|3666003]]. [[41-002-004-tr — Cylinder Head|Refer to Procedure 002-004 in Section 2.]]
- Use the following procedure in the B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual, Bulletin [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual\|3666087]]. [[40-002-004-tr — Cylinder Head|Refer to Procedure 002-004 in Section 2.]]
- Use the following procedure in the ISB and QSB5.9-44 Engines Troubleshooting and Repair Manual, Bulletin 3666193. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISBe, ISB, and QSB (Common Rail Fuel System) Service Manual, Bulletin 4021271. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the Industrial QSB3.9-30, QSB4.5-30, and QSB5.9-30 Series Engines Troubleshooting and Repair Manual, Bulletin 4021398. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISC, ISCe, QSC8.3, ISL, ISLe3, ISLe4 and QSL9 Engines Troubleshooting and Repair Manual, Bulletin 4021418. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISC and ISL CM2150 Service Manual, Bulletin 4021569. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB CM2100 and CM2150 Service Manual, Bulletin 4021578. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISBe and ISDe CM2150 Service Manual, Bulletin 4021597. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISLe CM2150 Service Manual, Bulletin 4021630. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISL G CM2180 Service Manual, Bulletin 4021649. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISF3.8 CM2220, ISF3.8 CM2220 AN and ISF3.8 CM2220 IAN Service Manual, Bulletin 4021704. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISF2.8 CM2220, ISF2.8 CM2220E, ISF2.8 CM2220AN and ISF2.8 CM2220 IAN Service Manual, Bulletin 4022178. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB4.5, ISB6.7, ISD4.5 and ISD6.7 CM2150 SN Service Manual, Bulletin 4022188. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB6.7 CM2250 Service Manual, Bulletin 4022254. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB6.7 CM2350 B101 Service Manual, Bulletin 2883567. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB4.5 CM2350 B104 Service Manual, Bulletin 4332646. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB6.7 CM2350 B103 Service Manual, Bulletin 4332641. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the QSB6.7 CM2350 B105 and B6.7 CM2450 B232C Service Manual, Bulletin 4332778. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the QSL9 CM2350 L102 and L9 CM2450 L181C Service Manual, Bulletin 4332796. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISF3.8 CM2220 F110 Service Manual, Bulletin 4358480. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISL9 CM2350 L101 Service Manual, Bulletin 4310787. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the QSL9 M CM2250 L106 and L9 CM2450 L170M Service Manual, Bulletin 4358343. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the QSB6.7 CM2350 B112 Service Manual, Bulletin 4358498. Refer to Procedure 002-004 in Section 12.
- Use the following procedure in the ISB/ISD6.7 CM2880 B126 Service Manual, Bulletin 4383693. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the QSL9 CM2250 L115 Service Manual, Bulletin 4388626. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the L9 CM2350 L116B Service Manual, Bulletin 5411330. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the B6.7 CM2350 B121B Service Manual, Bulletin 5411223. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the L9N CM2380 L124B Service Manual, Bulletin 5467492. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the ISB5.9 G CM2180 Service Manual, Bulletin 2883369. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the F2.8 CM2620 F135B Service Manual, Bulletin 5504616. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the F2.8 CM2620 F136B Service Manual, Bulletin 5504621. Refer to Procedure 002-004 in Section 2.
- Use the following procedure in the R2.8 CM2220 R102C Service Manual, Bulletin 6457240. Refer to Procedure 002-004 in Section 2.

Air compressor is malfunctioning.

- Use the following procedure in the C Series Engines Troubleshooting and Repair Manual, Bulletin [[3666003 — C Troubleshooting and Repair Manual\|3666003]]. [[100-012-014-tr — Air Compressor|Refer to Procedure 012-014 in Section 2.]]
- Use the following procedure in the B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual, Bulletin [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual\|3666087]]. [[40-012-014-tr — Air Compressor|Refer to Procedure 012-014 in Section 12.]]
- Use the following procedure in the ISB and QSB5.9-44 Engines Troubleshooting and Repair Manual, Bulletin 3666193. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISBe, ISB, and QSB (Common Rail Fuel System) Service Manual, Bulletin 4021271. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the Industrial QSB3.9-30, QSB4.5-30, and QSB5.9-30 Series Engines Troubleshooting and Repair Manual, Bulletin 4021398. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISC, ISCe, QSC8.3, ISL, ISLe3, ISLe4 and QSL9 Engines Troubleshooting and Repair Manual, Bulletin 4021418. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISC and ISL CM2150 Service Manual, Bulletin 4021569. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISB CM2100 and CM2150 Service Manual, Bulletin 4021578. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISBe and ISDe CM2150 Service Manual, Bulletin 4021597. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISLe CM2150 Service Manual, Bulletin 4021630. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISL G CM2180 Service Manual, Bulletin 4021649. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISF3.8 CM2220 Service Manual, Bulletin 4021704. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISB4.5, ISB6.7, ISD4.5 and ISD6.7 CM2150 SN Service Manual, Bulletin 4022188. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISB6.7 CM2250 Service Manual, Bulletin 4022254. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISB6.7 CM2350 B101 Service Manual, Bulletin 2883567. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISB4.5 CM2350 B104 Service Manual, Bulletin 4332646. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISB6.7 CM2350 B103 Service Manual, Bulletin 4332641. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the QSB6.7 CM2350 B105 and B6.7 CM2450 B232C Service Manual, Bulletin 4332778. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the QSL9 CM2350 L102 and L9 CM2450 L181C Service Manual, Bulletin 4332796. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISF3.8 CM2220 F110 Service Manual, Bulletin 4358480. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISL9 CM2350 L101 Service Manual, Bulletin 4310787. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the QSB6.7 CM2350 B112 Service Manual, Bulletin 4358498. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISB/ISD6.7 CM2880 B126 Service Manual, Bulletin 4383693. Refer to Procedure 012-014 in Section 14.
- Use the following procedure in the QSL9 CM2250 L115 Service Manual, Bulletin 4388626. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the L9 CM2350 L116B Service Manual, Bulletin 5411330. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the B6.7 CM2350 B121B Service Manual, Bulletin 5411223. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the L9N CM2380 L124B Service Manual, Bulletin 5467492. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the ISB5.9 G CM2180 Service Manual, Bulletin 2883369. Refer to Procedure 012-014 in Section 12.
- Use the following procedure in the F2.8 CM2620 F135B Service Manual, Bulletin 5504616. Refer to Procedure 012-014 in Section 12.

Piston or piston rings are worn or damaged.

- Use the following procedure in the C Series Engines Troubleshooting and Repair Manual, Bulletin [[3666003 — C Troubleshooting and Repair Manual\|3666003]]. [[100-001-043 — Piston|Refer to Procedure 001-043 in Section 1.]]
- Use the following procedure in the B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual, Bulletin [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual\|3666087]]. [[40-001-043 — Piston|Refer to Procedure 001-043 in Section 1.]]
- Use the following procedure in the ISB and QSB5.9-44 Engines Troubleshooting and Repair Manual, Bulletin 3666193. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISBe, ISB, and QSB (Common Rail Fuel System) Service Manual, Bulletin 4021271. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the Industrial QSB3.9-30, QSB4.5-30, and QSB5.9-30 Series Engines Troubleshooting and Repair Manual, Bulletin 4021398. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISC, ISCe, QSC8.3, ISL, ISLe3, ISLe4 and QSL9 Engines Troubleshooting and Repair Manual, Bulletin 4021418. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISC and ISL CM2150 Service Manual, Bulletin 4021569. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISB CM2100 and CM2150 Service Manual, Bulletin 4021578. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISBe and ISDe CM2150 Service Manual, Bulletin 4021597. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISLe CM2150 Service Manual, Bulletin 4021630. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISL G CM2180 Service Manual, Bulletin 4021649. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISF3.8 CM2220, ISF3.8 CM2220 AN and ISF3.8 CM2220 IAN Service Manual, Bulletin 4021704. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISB4.5, ISB6.7, ISD4.5 and ISD6.7 CM2150 SN Service Manual, Bulletin 4022188. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISF2.8 CM2220, ISF2.8 CM2220 E, ISF2.8 CM2220 AN and ISF2.8 CM2220 IAN Service Manual, Bulletin 4022178. Refer to Procedure 001-043 in Section 1. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISB6.7 CM2250 Service Manual, Bulletin 4022254. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISB6.7 CM2350 B101 Service Manual, Bulletin 2883567. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISB4.5 CM2350 B104 Service Manual, Bulletin 4332646. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISB6.7 CM2350 B103 Service Manual, Bulletin 4332641. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the QSB6.7 CM2350 B105 and B6.7 CM2450 B232C Service Manual, Bulletin 4332778. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the QSL9 CM2350 L102 and L9 CM2450 L181C Service Manual, Bulletin 4332796. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISF3.8 CM2220 F110 Service Manual, Bulletin 4358480. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISL9 CM2350 L101 Service Manual, Bulletin 4310787. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the QSL9 M CM2250 L106 and L9 CM2450 L170M Service Manual, Bulletin 4358343. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the QSB6.7 CM2350 B112 Service Manual, Bulletin 4358498. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISB/ISD6.7 CM2880 B126 Service Manual, Bulletin 4383693. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the QSL9 CM2250 L115 Service Manual, Bulletin 4388626. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the L9 CM2350 L116B Service Manual, Bulletin 5411330. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the B6.7 CM2350 B121B Service Manual, Bulletin 5411223. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the L9N CM2380 L124B Service Manual, Bulletin 5467492. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the ISB5.9 G CM2180 Service Manual, Bulletin 2883369. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the F2.8 CM2620 F135B Service Manual, Bulletin 5504616. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the F2.8 CM2620 F136B Service Manual, Bulletin 5504621. Refer to Procedure 001-043 in Section 1.
- Use the following procedure in the R2.8 CM2220 R102C Service Manual, Bulletin 6457240. Refer to Procedure 001-043 in Section 1.

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3089567]] | THREADED PLUG | Резьбовая пробка |
