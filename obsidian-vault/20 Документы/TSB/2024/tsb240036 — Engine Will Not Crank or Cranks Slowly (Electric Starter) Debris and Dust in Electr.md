---
aliases:
  - "Двигатель не проворачивается или вращается медленно: грязь и пыль в стартере"
type: "TSB"
doc: "tsb240036"
title_en: "Engine Will Not Crank or Cranks Slowly (Electric Starter): Debris and Dust in Electric Starting Motor"
title_ru: "Двигатель не проворачивается или вращается медленно: грязь и пыль в стартере"
modified: "2024-02-19"
engines:
  - "85017333"
families:
  - "QSK23"
parts:
  - "4396011"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2024/tsb240036.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb240036.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK23"
---

# Engine Will Not Crank or Cranks Slowly (Electric Starter): Debris and Dust in Electric Starting Motor
**Двигатель не проворачивается или вращается медленно: грязь и пыль в стартере**

> [!abstract] TSB · `tsb240036`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Даты:** изменён 2024-02-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2024/tsb240036.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb240036.pdf)

## Engine Will Not Crank or Cranks Slowly (Electric Starter): Debris and Dust in Electric Starting Motor

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- QSK23 CM500
- QSK23 CM500 K157G
- QSK23 CM2250 K109

**Issue Summary**

Symptom:

- Engine will **not** crank
- Engine cranks slowly

Root Cause:

- Nose bushing of electric starting motor contamination causing nose bushing and drive end bushing wear.

**Verification**

Visual inspection of electric starting motor can confirm if dust and debris has collected in nose cone of electric starting motor where slow cranking or no cranking of the engine is experienced.

**Resolution**

- If dust and debris has collected in the nose cone of the electric starting motor, a noseless electric starting motor option is available. See Table 1 for part number information.
- For proper wiring and connection, reference Service Instructions section below.

**Service Instructions**

- For more information on the M128 starting motor and installation, reference the Prestolite™ TSBs found in Table 2.

> [!note] Note · Примечание
> Changes in OEM starter wiring, and connector lug sizes may be required when upfitting from the Komatsu® starting motor to the new M128 starting motor. See Table 1 for M128 lug sizes.

![[13r00267.png]]

Figure 1, Dual-Starting Motor M128 Wiring Diagram.

| Table 1, Figure 1 Wiring Diagram Callouts |  |  |
|---|---|---|
| Callout | Description | Lug Size |
| 1 | BATT. + | M12 x 1.75 |
| 2 | BATT. - | M12 x 1.75 |
| 3 | IGNITION | M5 x 0.8 |
| 4 | Balance Lead \* | M5 x 0.8 |
| 5 | Sensing Lead \*\* | M12 x 1.75 |
| \* Install an ignition input balancing wire connecting the two starter ignition input terminals. Wire size **must** be at least 16 awg. |  |  |
| \*\* Some dual start applications have voltage sense functionality. This is specific to special customer applications and starters. Ignore if system is not equipped with this feature. Prestolite™ recommends the customer connects a sensing terminal so that the operator can observe if both starters have achieved meshing. If no lead is present, this may void warranty. Contact technical service if unsure. |  |  |

| Table 2, Related Prestolite™ Publications |  |
|---|---|
| Prestolite Description | TSB Number |
| 24V M128R Starters - Wiring / Terminal Identification | TSB-1171 |
| M128 – Dual Starter Wiring Procedure | TSB-1172 |
| MS7 – M128 Supersession Fitment Information | TSB 4079 |

**Service Parts**

Service parts are offered. See Table 3 for part numbers.

| Table 3, Service Parts |  |  |  |  |
|---|---|---|---|---|
| Part Description | Existing Part Number | Obsolete | Superseded | New Part Number |
| Motor, Starting | [[4396011]] | No | No | 5593352 |

**Part Compatibility**

- When upfitting dual-starter installations, both starting motors **must** be the new available part number. Mismatch starting motors are **not** supported.
- **Never** remove or bypass the integrated magnetic switch (IMS) on the M128 starting motor. This integrated starting relay is part of the starter soft start feature.

### Document History

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[4396011]] | STARTING MOTOR | Стартер |
