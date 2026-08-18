---
aliases:
  - "Электронный блок управления двигателем"
type: "Процедура"
doc: "123-019-031"
title_en: "Engine Control Module"
title_ru: "Электронный блок управления двигателем"
modified: "2014-04-17"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 6
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-019-031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-019-031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# Engine Control Module
**Электронный блок управления двигателем**

> [!abstract] Процедура · `123-019-031`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section 19 - Electronic Controls
> **Даты:** изменён 2014-04-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-019-031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-019-031.pdf)

### Initial Check

Turn the keyswitch to the ON position while monitoring the fault lamps. The fault lamps **must** illuminate for 2 to 3 seconds.

If the lamps do **not** illuminate, check for burned-out bulbs.

![[gp8swkb.png]]

Turn the keyswitch to the OFF position.

Connect an electronic service tool to the vehicle data link.

Turn the keyswitch to the ON position.

With INSITE™ electronic service tool, select the appropriate connection for the data link being used and attempt to connect to the ECM. The electronic service tool **must** be able to communicate with engine control module (ECM). If the ECM will **not** communicate with the service tool, refer to the Communication Error - Electronic Service Tool or Control Device symptom tree.

![[19c01217.png]]

### Remove

> [!warning] CAUTION · Осторожно
> Record all programmable parameters, features, and calibration information from the old ECM before disconnecting the harness connectors. This information will be needed to program the new ECM.

Remove the ECM ground strap from the ECM on Marine engine applications.

Disconnect the 4-pin power connector and both 60-pin connectors from the ECM, if they are **not** already removed.

![[19c01218.png]]

Remove the capscrews that secure the ECM to the engine.

![[19600713.png]]

### Install

> [!warning] CAUTION · Осторожно
> Do not paint the back side of the ECM. Make sure no grease or dirt is between the ECM and the cooling plate. Failure to do so can result in ECM damage.

Install the new ECM to the cooling plate.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 18 n•m [159 in-lb]

![[19600713.png]]

> [!warning] CAUTION · Осторожно
> Do not blow compressed air into the ECM ports or connectors. Compressed air can contain moisture due to condensation.

> [!note] Note · Примечание
> When an ECM is replaced, the new ECM **must** be calibrated. Refer to Procedure 019-032.

Connect the ECM ground strap to the ECM on Marine engine applications.

Use quick-dry electrical contact cleaner, Part Number 3824510, or equivalent, to remove all dirt and moisture from the ECM connector ports and the harness connectors. Connect all harness connectors.

Connect the 4-pin power connector and both 60-pin connectors to the ECM.

Tighten the connector capscrews to the ECM.

Use an inch-pound torque wrench, Part Number 3376592, with 4 mm \[5/32 in\] hex head adapter to tighten the connector jackscrew.

> [!tip] Момент затяжки · Torque Value
> 2.8 n•m [25 in-lb]

> [!note] Note · Примечание
> Do **not** over-torque connector as damage can occur.

![[19900518.png]]
