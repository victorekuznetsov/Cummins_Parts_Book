---
aliases:
  - "Электронный блок управления двигателем"
type: "Процедура"
doc: "98-019-031"
title_en: "Engine Control Module"
title_ru: "Электронный блок управления двигателем"
modified: "2024-09-23"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 15
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Engine Control Module
**Электронный блок управления двигателем**

> [!abstract] Процедура · `98-019-031`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2024-09-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-031.pdf)

### Inspect

Inspect the ECM connector jack posts for loose or missing jacks.

Flush and clean the connector pins using contact cleaner, Part No. 3824510. Inspect the ECM connector for burnt pins and damage to the ECM housing.

If any of the above conditions are present, replace the ECM.

![[19801120.png]]

### Remove

> [!note] Note · Примечание
> All active fault codes **must** be investigated prior to ECM replacement.

Record the customer's programmable parameters. Refer to the appropriate electronic service tool manual.

![[19800109.png]]

> [!warning] CAUTION · Осторожно
> Do not twist, bend, or pull on the main engine harness.

Remove the three mounting capscrews holding the ECM to the EFC module.

Carefully move the ECM away from the fuel pump.

![[19801900.png]]

> [!warning] CAUTION · Осторожно
> A loose or missing ECM jack post can cause the engine to run erratically, surge, or die unexpectedly, as well as to log any number of different fault codes. Use a 1/4-inch open-end wrench to hold the jack post while loosening the main engine harness ECM connector capscrews.

![[19801121.png]]

Remove the two hold-down capscrews from the main engine harness connector.

Carefully pull the connector from the ECM.

![[19801896.png]]

### Install

> [!warning] CAUTION · Осторожно
> Use only Cummins-recommended lubricant DS-ES, Part No. 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature pin wear.

Apply lubricant to the face of the ECM receptacle.

![[19801885.png]]

Spread the lubricant across the face of the receptacle to make sure it gets into every pin cavity of the connector.

![[19801879.png]]

Install the main engine harness connector into the ECM receptacle. Carefully align the connector guide slots with the receptacle guide slots in the ECM and insert the connector.

![[19801855.png]]

> [!warning] CAUTION · Осторожно
> Do not overtighten the connector capscrews; this can cause the capscrews to break and damage the ECM.

Carefully align and start each connector mounting capscrew by hand. Use inch-pound torque wrench, Part No. 3376592, to tighten each capscrew one turn each until the connector is seated in the receptacle.

> [!tip] Момент затяжки · Torque Value
> 0.7 n•m [6 in-lb]

> [!note] Note · Примечание
> The capscrews will **not** bottom out.

![[19801841.png]]

> [!warning] CAUTION · Осторожно
> Make sure the rear ECM mounting capscrew is Part No. 3067583. The ECM can be internally damaged if a longer capscrew is installed.

Place the ECM over the face of the EFC module, and insert the three mounting capscrews.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19801900.png]]

Program the customer-programmable parameters.

> [!note] Note · Примечание
> When an ECM is replaced, the new ECM **must** be calibrated. Use an electronic service tool to calibrate the ECM. Refer to the appropriate electronic service tool manual.

![[19800109.png]]

### Calibrate

In order to recalibrate the ECM, the specified calibration for the engine model **must** be downloaded.

With the keyswitch OFF, connect the electronic service tool and start ESDN. The window that will appear will ask if the keyswitch is ON. Select No.

Click on the Recalibrate button in ESDN and choose the appropriate ECM part number and calibration you wish to download. Transfer the calibration to the ECM.

![[19400359.png]]

A communication status window will appear that counts the elapsed time the module has tried to establish communication. Because the keyswitch is OFF, communication can **not** be established. Wait until the communication attempt times out, or press the Cancel button.

At this point, another window will appear with the message that INSITE™ for CENTRY™ was unable to connect to the module. You will be prompted to choose whether to continue or cancel the process. Select OK to continue.

![[19a00042.png]]

Turn the keyswitch ON.

The calibration process should cycle through the normal steps.

![[19a00474.png]]

Because the recalibration overwrites the existing calibration in the module, the dataplate information is overwritten as well, once the download is completed.

Use INSITE™ for CENTRY™ to add the dataplate information.

![[19a00042.png]]
