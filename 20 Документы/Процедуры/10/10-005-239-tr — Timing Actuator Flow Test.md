---
type: "Процедура"
doc: "10-005-239-tr"
title_en: "Timing Actuator Flow Test"
modified: "2013-03-27"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-005-239-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-005-239-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Timing Actuator Flow Test

> [!abstract] Процедура · `10-005-239-tr`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2013-03-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-005-239-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-005-239-tr.pdf)

### General Information

This test measures the drain flow from the injectors for one bank. Virtually all of the drain flow during this test is supplied from that bank's timing actuator.

During the test, a graduated cylinder will be used to determine if the timing actuator is delivering too much timing fuel to the injectors on the bank being measured.

### Flow Test

Operate the engine until the coolant temperature is at least 71°C \[160°F\].

Turn the engine OFF.

![[00c00077.png]]

> [!danger] WARNING · Опасно
> Depending on the circumstance, diesel fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting severe personal injury, death, or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.

Connect a hose to the integrated fuel system module (IFSM) drain line fitting.

Place the opposite end of the hose into a clean bucket.

![[05a00164.png]]

Turn the keyswitch ON and operate engine at idle at 800 rpm.

> [!note] Note · Примечание
> Turn off the fan and air conditioning for the tests.

The idle speed may need to be adjusted to perform this test. Toggle the cruise control increment/decrement switch to see if the idle speed can be adjusted. If **not**, use INSITE™ electronic service tool to either enable the "Adjustable Low Idle Speed" feature or adjust the low idle speed.

When engine is running disconnect the fueling and timing actuators on the opposite bank of the timing actuator that is currently being tested.

> [!note] Note · Примечание
> Two fault codes (2311 and 2312 or 2313 and 2314) will become active when the fueling and timing actuators are unplugged. The active fault codes have no effect on the test results.

Do **not** operate the engine with the actuators unplugged for any longer than needed for this test. Running the engine with no fuel being supplied to the injectors on one bank can eventually lead to damage of the fuel system.

![[05a00165.png]]

Obtain a clear graduated cylinder that is marked in cubic centimeters. Use graduated cylinder, Part Number 4919139, or equivalent. A measurement cup that is marked in milliliters (ml) or ounces (oz) can also be used.

The measuring device **must** be capable of measuring between 0 ml \[0.0 oz\] and 500 ml \[17.0 oz\] in 10 ml \[0.34 oz\] increments.

![[05o00096.png]]

Transfer the end of the hose that is in the bucket into the graduated cylinder.

Let fuel flow into the graduated cylinder for 10 seconds; Use a stopwatch.

Record the volume of fuel then dump the entire contents into the bucket.

Perform the test 3 times and average the values.

If the average of the 3 tests is 260 ml \[8.79 oz\] or above, the timing actuator **must** be replaced.

Remove the test equipment after the test is complete.

![[05a00166.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Depending on the circumstance, diesel fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting severe personal injury, death, or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.

- Install the drain hose onto the IFSM fitting.
- Connect the engine harness to the fueling and timing actuators.
- Pour the fuel from the bucket into the fuel tank.
- Operate the engine and check for leaks.

![[ck800wa.png]]
