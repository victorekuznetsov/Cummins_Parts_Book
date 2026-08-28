---
aliases:
  - "Устройство EHAB"
type: "Процедура"
doc: "57-005-083"
title_en: "EHAB Device"
title_ru: "Устройство EHAB"
modified: "2022-07-06"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021539"
figures: 12
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/57/57-005-083.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/57-005-083.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/57"
---

# EHAB Device
**Устройство EHAB**

> [!abstract] Процедура · `57-005-083`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021539 — QST30 Service Manual|4021539]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2022-07-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/57/57-005-083.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/57-005-083.pdf)

### General Information

The Bosch® “EHAB” device is used on **only** the industrial version of the QST30. It serves as a fuel control device by controlling the fuel flow (on/off) and the direction of flow. The EHAB device consists of a housing, electrical solenoid, actuator, and spool valve assembly.

![[05a00046.png]]

With the keyswitch on, the Bosch® EHAB device is energized and the spool valve moves to allow fuel flow from the tank to the fuel lift pump and from the filters into the injection pump gallery.

1. Fuel inlet from tank
2. Fuel overflow from injection pump gallery
3. Fuel outlet to lift pump
4. Filtered fuel in
5. Injection pump inlet (filtered fuel).

![[05a00058.png]]

When the keyswitch is turned off, the Bosch® EHAB device is de-energized and the spool valve moves in the opposite direction. This prevents the flow of fuel into the injection pump gallery and opens a path, causing the lift pump to pump fuel out of the gallery and back to the tank.

1. Gallery overflow port
2. Fuel overflow
3. Fuel from gallery to lift pump
4. Filtered fuel in
5. Filtered fuel returned to tank inlet
6. Fuel pump overflow valve.

![[05a00059.png]]

### Test

> [!note] Note · Примечание
> This test checks the Bosch® EHAB internal solenoid.

Turn the vehicle keyswitch OFF.

Disconnect the 9-pin Deutsch fuel injection pump electrical connector. Do **not** disconnect the 2-pin EHAB device connector.

![[19a00338.png]]

Listen closely to the EHAB device and have someone turn the keyswitch to the ON position. You should here a clicking sound as the internal solenoid energizes. If a clicking sound is **not** heard, cycle the keyswitch three or four times. If a clicking sound is still **not** heard, check the resistance as described below.

![[05a00098.png]]

Turn the keyswitch OFF.

Disconnect the 2-pin EHAB device connector from the engine harness.

![[19a00339.png]]

Measure the resistance between both pins of the EHAB device connector.

The EHAB internal resistance **must** read between 38.5 to 43.5Ohms.

If the Bosch® EHAB device fails either test, it **must** be serviced by an authorized Bosch® repair location or replaced. At the moment, the Bosch® EHAB device is **only** replaceable as an assembly.

![[19a00753.png]]

### Remove

> [!warning] CAUTION · Осторожно
> Do not remove the solenoid/actuator from the Bosch® “EHAB” device housing. At the moment, the Bosch® “EHAB” device is only replaceable as an assembly.

![[05a00046.png]]

Remove four capscrews and the Bosch® “EHAB” device from the fuel injection pump housing.

![[05a00062.png]]

### Clean

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!warning] CAUTION · Осторожно
> Use a cleaning solvent that will not harm aluminum.

Use a brush and solvent to clean the Bosch® “EHAB” device, fittings, lines, and surrounding area.

Dry with compressed air.

![[05a00060.png]]

### Inspect for Reuse

Inspect the Bosch® “EHAB” device for dents, cracks, and other damage to the housing.

Inspect the device for separation, frays, cuts, or other damage to the electrical cable.

Inspect for loose or missing solenoid/actuator capscrews.

![[05a00061.png]]

### Install

Position two o-rings on the Bosch® “EHAB” device.

Install the Bosch® EHAB device and position on the injection pump housing.

> [!note] Note · Примечание
> Use Loctite 242 on the four mounting capscrews before installation.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

![[05a00062.png]]
