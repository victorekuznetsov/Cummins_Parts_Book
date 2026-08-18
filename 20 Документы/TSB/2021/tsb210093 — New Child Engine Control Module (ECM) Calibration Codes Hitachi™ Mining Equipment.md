---
aliases:
  - "Новые дочерние калибровки ЭБУ: карьерная техника Hitachi™"
type: "TSB"
doc: "tsb210093"
title_en: "New Child Engine Control Module (ECM) Calibration Codes: Hitachi™ Mining Equipment"
title_ru: "Новые дочерние калибровки ЭБУ: карьерная техника Hitachi™"
released: "2021-04-30"
modified: "2023-09-26"
group: "19 - Electronic Engine Controls"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210093.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb210093.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "год/2021"
  - "тема/electronic-engine-controls"
---

# New Child Engine Control Module (ECM) Calibration Codes: Hitachi™ Mining Equipment
**Новые дочерние калибровки ЭБУ: карьерная техника Hitachi™**

> [!abstract] TSB · `tsb210093`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Даты:** выпущен 2021-04-30 · изменён 2023-09-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210093.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb210093.pdf)

## New Child Engine Control Module (ECM) Calibration Codes: Hitachi™ Mining Equipment

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

Engines:

- QSK50 CM2150
- QSK50 CM850
- QSK60 CM2150
- QSK60 CM850

Original Equipment Manufacturer (OEM)

- Hitachi™

Application

- Mining

**Description of Change**

- New Hitachi™ specific child engine control module (ECM) codes have been released.
- The correct child ECM code is to be installed via INSITE™ electronic service tool depending on: application, fuel rating, fuel efficiency optimized (FEO) calibrations number and spin-on oil filters or eliminator oil filter utilization.

**Reason for Change**

- Parent ECM calibration codes for mining equipment have been updated to enable a technician to select if the engine is operating with spin-on or eliminator oil filters.
- This change is **not** compatible with Hitachi™ OEM equipment as they are unable to read fault codes from the parent ECM. Because of this, customer specific child ECM calibration codes have been created to broadcast the fault codes from the child 1 ECM.

**Customer Communication**

Cummins® distribution and dealers are to inform self-servicing customers of requirement to have INSITE™ electronic service tool with a Pro level subscription to install calibration codes on CM850/2150 ECMs.

**Service Instructions**

QSK50 Instructions:

Select the relevant child ECM codes from Table 1 and 2 below according to the existing parent ECM code and lubricating oil filter type.

| Table 1, QSK50 Spin On Lubricating Oil Filter ECM Calibration Codes |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | FEO ECM Calibration Codes | Tier 2 ECM Calibration Codes |  |  |  |  |  |  |  |  |  |
| Hitachi™ Machine Model | Engine Model | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code |
| EH 3500 | QSK50 | FR6905 | 61204 | AQ60901 | AR60674 | AR60675 | FR6734 | 6976 | AQ60296 | AR60674 | AR60675 |
| EX2500/EX5500 | QSK50 | FR6856 | 61199 | AQ60934 | AR60674 | AR60675 | FR6795 | 6871 | AQ60289 | AR60674 | AR60675 |
| EX2600/5600-6 | QSK50 | FR6858 | 61190 | AQ60911 | AR60674 | AR60675 | FR6790 | 6866 | AQ60288 | AR60674 | AR60675 |
| EX2600/5600-6 T | QSK50 | FR6858 | 61191 | AQ60912 | AR60674 | AR60675 | FR6790 | 61094 | AQ60888 | AR60674 | AR60675 |

| Table 2, QSK50 Eliminator Filter ECM Calibration Codes |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | FEO ECM Calibration Codes | Tier 2 ECM Calibration Codes |  |  |  |  |  |  |  |  |  |
| Hitachi™ Machine Model | Engine Model | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code |
| EH 3500 | QSK50 | FR6905 | 61204 | AQ60901 | AR60676 | AR60677 | FR6734 | 6976 | AQ60296 | AR60676 | AR60677 |
| EX2500/EX5500 | QSK50 | FR6856 | 61199 | AQ60934 | AR60676 | AR60677 | FR6795 | 6871 | AQ60289 | AR60676 | AR60677 |
| EX2600/5600-6 | QSK50 | FR6858 | 61190 | AQ60911 | AR60676 | AR60677 | FR6790 | 6866 | AQ60288 | AR60676 | AR60677 |
| EX2600/5600-6 T | QSK50 | FR6858 | 61191 | AQ60912 | AR60676 | AR60677 | FR6790 | 61094 | AQ60888 | AR60676 | AR60677 |

QSK60 Instructions:

Select the relevant child ECM codes from the Table 3 and 4 below according to the existing parent ECM calibration code and lubricating oil filter type.

| Table 3, QSK60 Spin on Lubricating Oil Filter ECM Calibration Codes |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | FEO ECM Calibration Codes | Tier 2 ECM Calibration Codes |  |  |  |  |  |  |  |  |  |
| Hitachi™ Machine Model | Engine Model | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code |
| EH4000 | QSK60 | FR6898 | DO61215 | AQ60922 | AR60678 | AR60679 | FR6746 | DO6975 | AQ60295 | AR60678 | AR60679 |
| EH5000 | QSK60 | FR6938 | DO61222 | AQ60929 | AR60680 | AR60681 | FR6773 | DO6839 | AQ60238 | AR60680 | AR60681 |
| EH5000 | QSK60 | FR6938 | DO61349 | AQ61003 | AR60680 | AR60681 | FR6773 | DO60198 | AQ60415 | AR60680 | AR60681 |
| EX3600/EX8000 | QSK60 | FR6896 | DO61192 | AQ60913 | AR60678 | AR60679 | FR6796 | DO6872 | AQ60303 | AR60678 | AR60679 |

| Table 4, QSK60 Eliminator Filter ECM Calibration Codes |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | FEO ECM Calibration Codes | Tier 2 ECM Calibration Codes |  |  |  |  |  |  |  |  |  |
| Hitachi™ Machine Model | Engine Model | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code |
| EH4000 | QSK60 | FR6898 | DO61215 | AQ60922 | AR60684 | AR60685 | FR6746 | DO6975 | AQ60295 | AR60684 | AR60685 |
| EH5000 | QSK60 | FR6938 | DO61222 | AQ60929 | AR60682 | AR60683 | FR6773 | DO6839 | AQ60238 | AR60682 | AR60683 |
| EH5000 | QSK60 | FR6938 | DO61349 | AQ61003 | AR60682 | AR60683 | FR6773 | DO60198 | AQ60415 | AR60682 | AR60683 |
| EX3600/EX8000 | QSK60 | FR6896 | DO61192 | AQ60913 | AR60684 | AR60685 | FR6796 | DO6872 | AQ60303 | AR60684 | AR60685 |
| EX3600/EX8000 | QSK60 | FR6896 | DO61080 | AQ60947 | AR60684 | AR60685 |  |  |  |  |  |
| EX3600/EX8000 | QSK60 | FR6896 | DO61164 | AQ60948 | AR60684 | AR60685 |  |  |  |  |  |

**Part Compatibility**

ECM calibration codes **must** be selected correctly for your engine and application. If the incorrect ECM calibration code is selected engine de-rates and shutdowns due to incorrect fault code thresholds can occur.

### Document History
