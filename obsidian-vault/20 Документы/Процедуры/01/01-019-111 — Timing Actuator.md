---
aliases:
  - "Исполнительный механизм опережения впрыска"
type: "Процедура"
doc: "01-019-111"
title_en: "Timing Actuator"
title_ru: "Исполнительный механизм опережения впрыска"
modified: "2004-07-16"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Timing Actuator
**Исполнительный механизм опережения впрыска**

> [!abstract] Процедура · `01-019-111`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-07-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-111.pdf)

### General Information

QSX15

The timing actuators are located on the engine in front of the ECM. There are two of them. The front timing actuator is located on the fuel delivery housing. It is the second actuator from the front of the engine.

The rear timing actuator is located on the fuel delivery housing. It is the second actuator from the rear of the engine.

![[05c00001.png]]

QSK23, QSK45, QSK60, and QSK78

The timing rail actuators are part of the control valve body.

![[19400301.png]]

### Test

> [!note] Note · Примечание
> This test procedure is used **only** for QSX15 series engines.

Perform the INSITE™ electronic service tool cylinder performance test to determine if an actuator has failed. If a bank fails, this could indicate an actuator failure.

If **only** two injectors in a bank fail, repeat the test. Swap the front and rear fueling actuators to determine if the failed bank of cylinders follows the actuator. If so, replace the failed fueling actuator as necessary.

If **not**, swap the front and rear timing actuator to determine if the failed bank of cylinders follows the actuator. If so, replace failed timing actuator as necessary.

![[19800902.png]]

### Remove

QSX15

Clean the area around the timing actuator.

Disconnect the timing actuator connector from the engine harness.

![[19802663.png]]

Remove the three capscrews securing the timing actuator.

![[19802663.png]]

QSK23, QSK45, QSK60, and QSK78

Clean the area around the timing actuator.

Disconnect the timing actuator connectors from the engine harness.

> [!note] Note · Примечание
> The timing rail actuators are part of the control valve body.

![[19400300.png]]

Remove the timing actuator.

![[19400301.png]]

### Install

QSX15

Install new o-rings. Apply grease to the o-ring groove to retain the o-ring during installation.

Install a new timing actuator.

> [!tip] Момент затяжки · Torque Value
> 5.4 n•m [48 in-lb]

Connect the engine harness to the timing actuator.

Start the engine and check for leaks.

![[19802663.png]]

QSK23, QSK45, QSK60, and QSK78

Inspect the new o-ring.

Install a new timing rail actuator.

> [!tip] Момент затяжки · Torque Value
> 25 n•m [18 ft-lb]

Connect the engine harness to the timing rail actuator.

Start the engine and check for leaks.

![[19400302.png]]
