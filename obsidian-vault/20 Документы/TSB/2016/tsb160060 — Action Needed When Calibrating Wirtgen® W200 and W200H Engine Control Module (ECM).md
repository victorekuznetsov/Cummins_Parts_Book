---
type: "TSB"
doc: "tsb160060"
title_en: "Action Needed When Calibrating Wirtgen® W200 and W200H Engine Control Module (ECM) to Retain Low Idle Speed and Grid Heater Parameter Settings"
modified: "2016-07-06"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2016/tsb160060.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb160060.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSX15"
---

# Action Needed When Calibrating Wirtgen® W200 and W200H Engine Control Module (ECM) to Retain Low Idle Speed and Grid Heater Parameter Settings

> [!abstract] TSB · `tsb160060`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Даты:** изменён 2016-07-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2016/tsb160060.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb160060.pdf)

## Action Needed When Calibrating Wirtgen® W200 and W200H Engine Control Module (ECM) to Retain Low Idle Speed and Grid Heater Parameter Settings

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

Engine:

- QSX15 CM570

Original Equipment Manufacturer (OEM):

- Wirtgen®

Models:

- W200
- W200H

**Issue**

- Select engine control module (ECM) calibration codes have different default values for the Low Idle Speed and Grid Heater parameters than those required by the original equipment manufacturer OEM.
- If the ECM is replaced or ECM save and restore function is not used or is interrupted during ECM calibration download, ECM parameter settings will **not** be restored to the correct values. This can result in incorrect idle speed and impair grid heater function.

**Verification**

For affected ECM calibration codes, see Table 1.

| Table 1, ECM Calibration Codes Affected |  |  |  |  |  |
|---|---|---|---|---|---|
| ECM Calibration Code | Generic/Custom | DO Option | SC Option | FR Option | Availability |
| N12028 | Generic | DO1684 | SC11374 | FR10577 | Service Only |
| N11835 | Generic | DO1412 | SC11374 | FR10577 | Service Only |

**Resolution**

- If the ECM is replaced or ECM save and restore function is **not** used or is interrupted during ECM calibration code download, technicians **must** verify that the parameters are correct. For default Wirtgen® parameters settings, See Table 2 below.
- If an ECM calibration code update is required, ECM calibration codes **must** be updated on a like-for-like basis, with no change in the ECM base calibration code.

| Table 2, Default Wirtgen® ECM Parameters |  |
|---|---|
| Parameter | Nominal Wirtgen® Setting |
| Low Idle Speed | 950 rpm |
| Grid Heater | On |

**Production Status**

All engines built after 7 March 2016 will be loaded with ECM calibration code N12213.

### Document History
