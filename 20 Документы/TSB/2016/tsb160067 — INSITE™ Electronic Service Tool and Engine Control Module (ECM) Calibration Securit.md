---
aliases:
  - "Изменения защиты калибровок ЭБУ и INSITE™"
type: "TSB"
doc: "tsb160067"
title_en: "INSITE™ Electronic Service Tool and Engine Control Module (ECM) Calibration Security Changes"
title_ru: "Изменения защиты калибровок ЭБУ и INSITE™"
released: "2016-07-06"
modified: "2018-10-04"
group: "22 - Service Tools"
engines:
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QST30"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2016/tsb160067.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb160067.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "год/2016"
  - "тема/service-tools"
---

# INSITE™ Electronic Service Tool and Engine Control Module (ECM) Calibration Security Changes
**Изменения защиты калибровок ЭБУ и INSITE™**

> [!abstract] TSB · `tsb160067`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19, QST30
> **Даты:** выпущен 2016-07-06 · изменён 2018-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2016/tsb160067.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb160067.pdf)

## INSITE™ Electronic Service Tool and Engine Control Module (ECM) Calibration Security Changes

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- All products supported by INSITE™ electronic service tool

**Description of Change**

INSITE™ electronic service tool version 8.1.4 has an improved level of security for engine control module (ECM) calibrations. These security changes in INSITE™ are aligned with security changes in all upcoming Cummins® ECM calibrations. These security changes **only** affect the ECM calibration download capability of INSITE™ Pro and Road Speed Governor Restricted (RSGR)/Industrial Pro™ version 8.1.4.

**Reason for Change**

This improved security is intended to make certain **only** authentic Cummins® ECM calibrations are downloaded into electronic control modules and programmable datalink devices.

**Customer Communication**

Beginning 26 July 2016, INSITE™ Pro version 8.1.4 will be needed for all ECM calibrations released on 26 July 2016 and thereafter. This free update will be pushed to all licensed users of INSITE™ Pro. Older versions of INSITE™ Pro will **not** recognize ECM calibrations released after this date. Cummins Inc. recommends updating to the existing version of INSITE™ Pro (8.1.3) now so updates beginning on 26 July 2016 are **not** as time consuming. This update will provide the option to delay the install up to three times before commencing with an automatic update.

INSITE™ users will be notified through an automated pop-up window when INSITE™ 8.1.4 is available for installation. For seamless customer support, Cummins Inc. recommends INSITE™ be updated to the new version when prompted.

**Service Instructions**

If INSITE™ is **not** updated, previous versions of INSITE™ will **only** download ECM calibrations on old INCAL™ DVDs that have **not** expired. Once INCAL™ DVDs have expired, INSITE™ will no longer be able to download any ECM calibration until updated to INSITE™ version 8.1.4.

> [!note] Note · Примечание
> If issues are encountered with the INSITE™ update or ECM calibration process, call (800) 433-9341 and select option 2. The hotline will be operating 24 hours a day during this update period between 26 July 2016 and 15 August 2016.

Beginning July 26 th, **only** these new ECM calibrations with improved embedded security will be available from QuickServe® Online (QSOL) and from the ECM Code Search and Save feature within INSITE™. Between 26 July 2016 and 15 August 2016, older versions of INSITE™ will still be able to download older ECM calibrations from the INCAL™ DVDs and http://care.cummins.com. However, INCAL™ DVDs will expire seven months after publication. The next release of INCAL™ DVD on 26 July 2016 will contain **only** the new ECM calibrations with improved embedded security and can **only** be downloaded with INSITE™ version 8.1.4.

**Part Compatibility**

| Table 1, INSITE™ Electronic Service Tool Version and ECM Calibration Compatibility Chart: Before Embedded Security |  |  |  |
|---|---|---|---|
| ECM Calibration Source | QuickServe® Online and ECM Code Search | http://care.cummins.com | INCAL™ DVD |
| Date | Before 26 July 2016 | Between 26 July 2016 and 15 August 2016 | Before 26 July 2016 |
| INSITE™ Version 8.1.4 and newer | - | - | **Not** Compatible |
| INSITE™ Version 8.1.3 and older | Compatible | Compatible | Compatible |

| Table 2, INSITE™ Electronic Service Tool Version and ECM Calibration Compatibility Chart: After Embedded Security |  |  |  |
|---|---|---|---|
| ECM Calibration Source | QuickServe® Online and ECM Code Search | http://care.cummins.com | INCAL™ DVD |
| Date | After 26 July 2016 | After 15 August 2016 | After 26 July 2016 |
| INSITE™ Version 8.1.4 and newer | Compatible | - | Compatible |
| INSITE™ Version 8.1.3 and older | **Not** Compatible | - | **Not** Compatible |

### Document History
