---
aliases:
  - "Электронный блок управления двигателем"
type: "Процедура"
doc: "01-019-031"
title_en: "Engine Control Module"
title_ru: "Электронный блок управления двигателем"
modified: "2015-10-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Control Module
**Электронный блок управления двигателем**

> [!abstract] Процедура · `01-019-031`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2015-10-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-031.pdf)

### Initial Check

Turn the Run/Stop switch to the Run position while monitoring the fault lamps. The fault lamps **must** illuminate for 2 to 3seconds.

If lamps do **not** illuminate, check for burned-out bulbs.

![[19802542.png]]

Turn the Run/Stop switch to the Stop position.

Connect an electronic service tool to the data link.

Select the monitor mode on the electronic service tool. The electronic service tool **must** be able to communicate with the engine control module (ECM). If the ECM will **not** communicate with the service tool, refer to the Communication Error - Electronic Service Tool or Control Device symptom tree.

![[19800902.png]]

### Remove

Record all programmable parameters, features, and calibration information from the old ECM before disconnecting the harness connectors. This information will be needed to program the new ECM. Refer to the INPOWER™ manual under “Save as a Template” for information on how to save and restore these ECM parameters electronically.

Disconnect the extension harness connectors and the generator control harness connectors from the ECM, if they are **not** already removed.

![[19802544.png]]

Remove the capscrews that hold the ECM to its mounted location.

See the equipment manufacturer service information for mounting location of the ECM.

![[19802545.png]]

### Install

Do **not** paint the ECM. Make sure no grease or dirt is between the ECM and the mounting surface.

Install the new ECM.

Install and tighten the mounting capscrews.

> [!tip] Момент затяжки · Torque Value
> 20 n•m [15 ft-lb]

![[19802545.png]]

> [!warning] CAUTION · Осторожно
> Do not blow compressed air into the ECM ports or connectors. Compressed air can contain moisture that may damage the components.

Use quick-dry electrical contact cleaner, Part Number 3824510, to remove all dirt and moisture from the ECM connector ports and the harness connectors.

![[19802490.png]]

Connect the extension harness connectors and generator control harness connectors to the ECM. Tighten the connector capscrews to the ECM.

> [!tip] Момент затяжки · Torque Value
> 2.8 n•m [25 in-lb]

> [!note] Note · Примечание
> Do **not** over-torque as connector damage can occur.

When an ECM is replaced, the new ECM **must** be calibrated. [[01-019-032 — ECM Calibration Code|Refer to Procedure 019-032]].

![[19802544.png]]
