---
type: "Процедура"
doc: "19-019-186"
title_en: "In-Range Pressure Sensor"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-186.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-186.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# In-Range Pressure Sensor

> [!abstract] Процедура · `19-019-186`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-186.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-186.pdf)

### Pressure Test

Turn the engine off.

Relieve the pressure in the fuel system by opening the fuel lines or pulling out the pressure sensors or actuators.

![[19400307.png]]

Connect INSITE™ to the vehicle datalink.

![[19a00042.png]]

Turn the keyswitch to the ON position.

> [!note] Note · Примечание
> Rail and timing pressure are displayed in units of psia. Ambient air pressure is displayed in units of in-Hg. To convert from psia to in-Hg, multiply the psia reading by two (15 psia = 30 in-Hg, for example).

Use INSITE™ to monitor the rail pressure, timing pressure, ambient air pressure, pump pressure, and intake manifold pressure in English units.

- Rail pressure, timing pressure, and pump pressure should all be the same.
- Rail, timing, and pump pressure should be equal to the ambient air pressure.
- Intake manifold pressure should be equal to zero.

> [!note] Note · Примечание
> The above measures should be accurate to within ±4 psia or ±8 in-Hg.

![[19800978.png]]

If the rail, timing, and pump pressures are equal, but are **not** equal to the ambient air pressure, then refer to Fault Codes 221, 222, and 318.

If the intake manifold pressure is greater than 0.5 in-Hg, then refer to Fault Codes 122 and 123.

![[19800978.png]]

If the rail, timing, and pump pressures are **not** equal, compare each to the ambient air pressure.

- If the rail pressure is **not** equal to the ambient air pressure, refer to Fault Codes 451 and 452.
- If the timing pressure is **not** equal to the ambient air pressure, refer to Fault Codes 116 and 117.
- If the pump pressure is **not** equal to the ambient air pressure, refer to Fault Code 316.

![[19800978.png]]

If any sensors were removed, install them back into the electronic control valve assembly.

Start the engine and let it idle.

Measure the rail pressure, timing pressure, ambient air pressure, pump pressure, and intake manifold pressure.

- If the ambient air pressure does **not** equal the ambient air pressure with the engine off, refer to Fault Codes 221 and 222.
- If the intake manifold pressure is greater than 1 in-Hg, refer to Fault Codes 122 and 123.

![[19800979.png]]

Connect a pressure gauge to the fuel rail quick-disconnect.

- If the gauge pressure is **not** the same as the electronic measurement, refer to Fault Codes 451 and 452.

![[19400633.png]]

Connect a pressure gauge to the timing rail quick-disconnect.

- If the gauge pressure is **not** the same as the electronic measurement, refer to Fault Codes 116 and 117.

![[19400633.png]]

Connect a pressure gauge to the fuel pump outlet quick-disconnect.

- If the gauge pressure is **not** the same as the electronic measurement, refer to Fault Code 316.

![[19400633.png]]
