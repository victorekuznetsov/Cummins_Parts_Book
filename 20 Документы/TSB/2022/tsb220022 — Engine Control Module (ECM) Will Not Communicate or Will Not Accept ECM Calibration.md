---
aliases:
  - "ЭБУ не выходит на связь или не принимает калибровочный код"
type: "TSB"
doc: "tsb220022"
title_en: "Engine Control Module (ECM) Will Not Communicate or Will Not Accept ECM Calibration Code"
title_ru: "ЭБУ не выходит на связь или не принимает калибровочный код"
released: "2022-02-07"
modified: "2024-10-04"
group: "19 - Electronic Engine Controls"
engines:
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41349633"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QST30"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2022/tsb220022.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb220022.pdf"
tags:
  - "документ/tsb"
  - "двигатель/C8.3"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "год/2022"
  - "тема/electronic-engine-controls"
---

# Engine Control Module (ECM) Will Not Communicate or Will Not Accept ECM Calibration Code
**ЭБУ не выходит на связь или не принимает калибровочный код**

> [!abstract] TSB · `tsb220022`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, K38/K50 · QSK38, QSK50, QSK60, QSK19, QST30
> **Даты:** выпущен 2022-02-07 · изменён 2024-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2022/tsb220022.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb220022.pdf)

## Engine Control Module (ECM) Will Not Communicate or Will Not Accept ECM Calibration Code

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

> [!note] Note · Примечание
> ROM Booted CM2180 ECM should **not** attempt to be recovered by recalibrating. See Technical Service Bulletin, INSITE™ Electronic Service Tool Error 5080 - Electronic Control Module (ECM) ROM-Booted or ROM-Booted in a Password Protected State, TSB150120.

All models with Engine Control Modules (ECM) except CM420 (B5.9G, B5.9LPG, C8.3G, L10G), ECM B (CELECT™), CM400 (CENTRY™), CM800 (ISBe, ISB four-cylinder), and CM551D (ISB light-duty Chrysler™).

**Applicable Engine Control Modules:**

- CM2150
- CM2180/CM2380
- CM2220
- CM2250
- CM2330
- CM2350/CM2450
- CM2450
- CM2358A
- CM2620
- CM2670
- CM2880
- CM3230
- CM500
- CM550
- CM552
- CM554
- CM556B
- CM558
- CM570
- CM700
- CM850
- CM870
- CM871
- CM875
- CM876
- ECM C

**Issue Summary**

Some ECMs have been replaced and Cummins Inc. has determined a portion of them were operating properly after being reset and calibrated. Unnecessary replacements of functional ECMs can be avoided by following the ROM boot and calibration procedures listed in this document.

Symptom:

- No communication with ECM
- ECM does **not** accept ECM calibration code

Root Cause:

- ECM calibration was **not** performed correctly
- Power or communication interruption during ECM calibration
- Incorrect ECM calibration code

**Verification**

Verify there is no communication with the ECM or that the ECM will **not** accept a calibration code.

**Resolution**

Before replacing the ECM, reset the ECM using the ROM boot process and attempt to recalibrate the ECM.

- Reset the ECM software using the ROM boot procedures listed in Table 1 and verify that INSITE™ shows a similar message as in Figure 1 below.
- Recalibrate the ECM using the ECM calibration procedures listed in Table 1 below.
- For general tool information, including the correct installation configuration and required cables, see the ECM-specific Bench Calibration Base Harness Service Tool Instruction, Bulletin 3377791.
- If the bench calibration base harness or any of the required hardware is **not** available, follow the technical escalation process.

![[19r99820.png]]

Figure 1, Example of the Error Message From INSITE™ Confirming the ECM Is Rom-Booted and Needs Recalibration.

**Associated Publications**

| Table 1, ECM Associated Publications |  |  |  |  |
|---|---|---|---|---|
| Publication Type | Bulletin Number | Procedure Title | Procedure | Section |
| ECM ROM Boot |  |  |  |  |
| Service Manual | See corresponding Service Manual | Engine Control Module ROM Boot | 019-427 | 19 |
| Electronic Control System Troubleshooting and Repair Manual | See corresponding Electronic Control System Troubleshooting and Repair Manual | Engine Control Module ROM Boot | 019-427 | 19 |
| Technical Service Bulletin | TSB150120 | INSITE™ Electronic Service Tool Error 5080 - Electronic Control Module (ECM) ROM-Booted or ROM-Booted in a Password Protected State | - | - |
| ECM Calibration |  |  |  |  |
| Service Tool Instruction | 3377791 | ECM Bench Calibration Base Harness | - | - |
| Service Manual | See corresponding Service Manual | Engine Control Module Calibration Code | 019-032 | 19 |
| Electronic Control System Troubleshooting and Repair Manual | See corresponding Electronic Control System Troubleshooting and Repair Manual | Engine Control Module Calibration Code | 019-032 | 19 |

### Document History
