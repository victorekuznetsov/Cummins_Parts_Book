---
type: "TSB"
doc: "tsb110145"
title_en: "Header File Change"
modified: "2011-06-01"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110145.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110145.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
---

# Header File Change

> [!abstract] TSB · `tsb110145`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Даты:** изменён 2011-06-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110145.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110145.pdf)

## Header File Change

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

Engines using CM500 ECMs containing Phase 2 or Phase 3 software lose any accumulated Engine Hours when recalibrated.

This issue has been identified as CM500 Phase 2 and Phase 3 software storing the Engine Hours parameter in the wrong area of the memory. As a result, Engine Hours is reset as the ECM gets recalibrated.

This issue has been resolved by amending the calibration command file to force the INSITE™ electronic tool to save Engine Hours before download and to restore Engine Hours automatically after download.

After recalibration, Engine Hours will be set to either approximately 230,000 hours or zero hours, depending on if a speed signal has been detected by the module since recalibration.

Recalibrate the engine ECMs using the updated calibrations from QuickServe™ Online. Please note the calibration revision numbers have **not** changed since **only** one calibration command within the calibration files has been added. This will prevent Engine Hours from being reset during recalibration.

The updated calibrations will be available on QuickServe™ Online from May 23, 2011.

The updated calibrations will also be available on the June 2011 INCAL™ Calbration DVD-ROM.

> [!note] Note · Примечание
> Engine Hours can be amended after recalibration using the Engine Hour Offset function in INSITE™ electronic service tool. This may be required if Engine Hours have previously been reset and an alternative means of determining the total accumulated time for the engine is available (e.g. transmission hours).

> [!note] Note · Примечание
> The “Save and Restore” function in INSITE™ electronic service tool should **not** be used during recalibration.

> [!note] Note · Примечание
> If Calterm is used for recalibration, please make sure the most recent calibration command file is used when assembling the calibration file.

### Document History
