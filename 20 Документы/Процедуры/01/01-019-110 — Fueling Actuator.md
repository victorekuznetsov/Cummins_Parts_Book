---
aliases:
  - "Исполнительный механизм подачи топлива"
type: "Процедура"
doc: "01-019-110"
title_en: "Fueling Actuator"
title_ru: "Исполнительный механизм подачи топлива"
modified: "2004-07-16"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 9
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-110.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-110.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fueling Actuator
**Исполнительный механизм подачи топлива**

> [!abstract] Процедура · `01-019-110`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-07-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-110.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-110.pdf)

### General Information

The fueling actuators control the delivery of fuel to the engine.

On the QSX15 fuel system, the fueling actuators are a part of the fuel delivery housing, located on the left side of the engine in front of the Electronic Control Module (ECM). There are two fueling actuators, one front and one rear.

The front fueling actuator controls the front three cylinders and the rear fuel actuator controls the rear three cylinders.

![[05c00001.png]]

On the QSK23, QSK45, QSK60, and QSK78 fuel system the fuel rail actuator is part of the control valve body.

![[19400369.png]]

### Test

> [!note] Note · Примечание
> This test procedure is used **only** for QSX15 series engines.

Perform the INSITE™ electronic service tool cylinder performance test to determine if an actuator has failed. If a bank fails, this could indicate an actuator failure.

If **only** two injectors in a bank fail, repeat the test. Swap the front and rear fueling actuators to determine if the failed bank of cylinders follows the actuator. If so, replace the failed fueling actuator as necessary.

If **not**, swap the front and rear timing actuator to determine if the failed bank of cylinders follows the actuator. If so, replace failed timing actuator as necessary.

![[19800902.png]]

### Remove

QSX15

Clean the area around the fueling actuator.

Disconnect the fueling actuator connector from the engine harness.

![[19802669.png]]

Remove the three capscrews securing the fueling actuator.

![[19802669.png]]

QSK23, QSK45, QSK60, and QSK78

Clean the area around the actuator.

Disconnect the actuator connector from the engine harness.

![[19400368.png]]

Remove the actuator with a ratchet and 1-¼-inch-deep flange drive socket, Part Number 3823843.

![[19400369.png]]

### Install

QSX15

Install a new o-ring. Apply grease to the o-ring groove to retain the o-ring during installation.

Install a new fueling actuator.

> [!tip] Момент затяжки · Torque Value
> 5.4 n•m [48 in-lb]

Connect the engine harness to the fueling actuator.

Start the engine and check for leaks.

![[19802669.png]]

QSK23, QSK45, QSK60, and QSK78

Inspect the new actuator for o-rings.

Install a new actuator.

> [!tip] Момент затяжки · Torque Value
> 25 n•m [221 in-lb]

Connect the engine harness to the actuator.

Start the engine and check for leaks.

> [!missing]- Иллюстрация `19400370.png` не извлечена — смотрите PDF-оригинал документа
