---
type: "TSB"
doc: "tsb130149"
title_en: "Next Generation CENSE™ CM2330 - INSITE™ Electronic Service Tool, Image/Trend Log Collection Instructions"
modified: "2013-10-22"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
figures: 5
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2013/tsb130149.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb130149.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60"
---

# Next Generation CENSE™ CM2330 - INSITE™ Electronic Service Tool, Image/Trend Log Collection Instructions

> [!abstract] TSB · `tsb130149`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Даты:** изменён 2013-10-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2013/tsb130149.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb130149.pdf)

## Next Generation CENSE™ CM2330 - INSITE™ Electronic Service Tool, Image/Trend Log Collection Instructions

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

The Next Generation CENSE™ CM2330 module is a diagnostic module and will interface with different engine control modules, depending on the specific application. The process for connecting to the Next Generation CENSE™ CM2330 module will **not** be the same as connecting to the CENSE™ CM530 module.

To connect to the Next Generation CENSE™ CM2330 module, follow these steps:

Step 1:

Connect INSITE™ electronic service tool. You will get a dropdown menu to choose between your main system (e.g. CM500 for HPI products or CM700 for certain gas engines) and the BEB system as illustrated below:

![[19500167.png]]

Step 2:

You can choose the system you would like to connect, as shown above. If you do **not** see a dropdown as described, restart INSITE™ electronic service tool and and the Powercycle INLINE™ adapter and thereafter when you try to connect INSITE™ electronic service tool, INSITE™ electronic service tool should give you a dropdown as expected.

To download engine control module (ECM) images and AEM data from the Next Generation CENSE™ CM2330 module:

Step 1:

Connect INSITE™ electronic service tool and create a work order, as shown below, with all the possible details. INSITE™ electronic service tool has the ability to create two images, initial and final.

![[19500168.png]]

> [!note] Note · Примечание
> When you initialize a work order, it creates an initial image and prompts you to save a final image when exiting INSITE™ electronic service tool.

Step 2:

Click on “Advanced ECM Data” and collect the AEM logs as soon as they are displayed by clicking the “Get Log” and “Save” buttons in each specific log screen, as illustrated below.

> [!note] Note · Примечание
> These logs will **not** be saved when you exit INSITE™ electronic service tool and can **not** be retrieved via ECM image either.

![[19500169.png]]

Screen image for the “Get Log” window.

![[19500170.png]]

Screen image for the “Save” window.

![[19500171.png]]

Step 3:

After you have collected the ECM image and all four logs from the Advanced ECM Data section in INSITE™ electronic service tool, you can “Disconnect from ECM” and take a final ECM image, if required.

### Document History
