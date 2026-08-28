---
type: "Процедура"
doc: "98-019-181"
title_en: "Step Timing Control Valve Solenoid"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-181.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-181.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Step Timing Control Valve Solenoid

> [!abstract] Процедура · `98-019-181`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-181.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-181.pdf)

### Remove

Disconnect the STC oil supply hose from the control valve.

Disconnect the oil hose connected to the oil manifold and the oil tube connected to the cam follower housing.

![[19802023.png]]

> [!note] Note · Примечание
> Removing the capscrews allows all of the valve pieces to separate.

Remove the four capscrews (3) from the bracket. Remove all of the following parts:

- Four capscrews (3)
- Cover (4)
- Valve body (5)
- Oil inlet fitting (1)
- Check valve (2).

Remove the check ball (6) and the o-ring (7) from the valve body.

![[19802022.png]]

Clean the parts in solvent and dry with compressed air. Inspect the parts for damage. Replace the valve if necessary.

![[19802025.png]]

### Install

Use clean engine oil to lubricate the o-ring (7). Install the o-ring (7) and the check ball (6) into the valve body. Install the following parts onto the bracket:

- Valve body (5)
- Cover (4)
- Four capscrews (3).

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

Install the check valve (2) and the oil inlet fitting (1).

![[19802022.png]]

Connect all of the hoses and tubes to the control valve.

![[19802023.png]]

Operate the engine to normal operating temperature and check for leaks.

![[19802028.png]]

### Resistance Check

Disconnect the STC driver wire from the solenoid on the oil control valve.

Select the resistance function on the multimeter. Touch one of the multimeter leads to the solenoid terminal. Touch the other multimeter lead to a good, clean surface on the engine block.

![[19801624.png]]

Measure the resistance. The resistance **must** fall within the ranges shown below. If the resistance is **not** within range, then replace the solenoid. Refer to the Fuel Pump Rebuild Manual, Bulletin No. 3379084.

| Solenoid P/N | Voltage and Type | Coil Resistance MIN | Coil Resistance MAX |
|---|---|---|---|
| 196066 | 24-VDC Single Terminal | 26 | 40 |
| 109940 | 12-VDC Single Terminal | 6 | 10 |

![[19801625.png]]
