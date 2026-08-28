---
aliases:
  - "Обкатка двигателя (на стенде с беговыми барабанами)"
type: "Процедура"
doc: "20-014-003"
title_en: "Engine Run-in (Chassis Dynamometer)"
title_ru: "Обкатка двигателя (на стенде с беговыми барабанами)"
modified: "2006-06-30"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 13
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-014-003.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-014-003.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Engine Run-in (Chassis Dynamometer)
**Обкатка двигателя (на стенде с беговыми барабанами)**

> [!abstract] Процедура · `20-014-003`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2006-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-014-003.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-014-003.pdf)

### General Information

> [!warning] CAUTION · Осторожно
> The lubricating oil system must be primed before operating the engine after rebuild to avoid internal component damage. Do not prime the system from the bypass filter, as the filter will be damaged.

Remove the large plug from the oil cooler housing.

![[14400011.png]]

Use a pump capable of supplying 207 kPa \[30 psi\] continuous pressure. Connect the pump to the front of the engine oil cooler as shown.

Use a supply of clean oil. Turn the pump to the ON position. Check the engine oil pressure gauge. When the gauge indicates oil pressure, begin monitoring the oil level in the oil pan.

![[pl4hoha.png]]

Check the engine lubricating oil level to be sure it is filled to the proper level.

![[oi8dsva.png]]

Check the engine coolant level to make sure it is filled to the proper level. Refer to Procedure [[20-008-018-tr — Cooling System|008-018]].

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or system steam can cause personal injury.

> [!warning] CAUTION · Осторожно
> Do not add cold coolant to a hot engine. This can cause engine casting damage. Allow the engine to cool to below 50°C \[120°F\] before adding coolant.

![[ra200sa.png]]

Use a known source of good quality Number 2 diesel fuel.

This is very important since Number 1 diesel fuels, along with most other alternate fuels, are lighter (lower specific gravity, higher API gravity) than Number 2 diesel fuel. The lighter the fuel, the lower the energy content (BTU) per gallon (liter, etc.).

![[nobox.png]]

### Run-In Instructions

Refer to Chassis Dynamometer - Operation, Procedure [[20-014-002-tr — Engine Testing (Chassis Dynamometer)|014-002]], for general operating procedures and safety precautions.

![[oi100vo.png]]

Use this chart to determine the test load.

Example: The test load for a 475 HP engine rated at 2000 rpm with a 15 percent torque rise is 225 ft-lb.

> [!note] Note · Примечание
> This chart assumes the dynamometer constant is 5252. If the dynamometer constant is **not** 5252, use the following formula to determine the correct test load:

Correct test load = (Dynamometer constant) x (Test load) /d 5252.

Example: The dynamometer constant for testing the engine in the above example is 4000.

Correct test load = (4000 x 225) /d 5252 = 171 ft-lb.

> [!note] Note · Примечание
> This chart assumes vehicle run-in on a chassis dynamometer.

| Rated RPM | Rated Horsepower | Torque Rise | Test Load |
|---|---|---|---|
| 1200 | All | All | 305 N•m \[225 ft-lb\] |
| 1500 | All | All | 305 N•m \[225 ft-lb\] |
| 1800 | 0 to 499 | All | 305 N•m \[225 ft-lb\] |
| 1800 | 500 and ABOVE | All | 380 N•m \[280 ft-lb\] |
| 1900 | 0 to 474 | All | 305 N•m \[225 ft-lb\] |
| 1900 | 475 and ABOVE | All | 380 N•m \[280 ft-lb\] |
| 2000 | 0 to 499 | 0 to 24% | 305 N•m \[225 ft-lb\] |
| 2000 | 0 to 499 | 25% and ABOVE | 380 N•m \[280 ft-lb\] |
| 2000 | 500 and ABOVE | All | 380 N•m \[280 ft-lb\] |
| 2100 | 0 to 474 | 0 to 32% | 305 N•m \[225 ft-lb\] |
| 2100 | 0 to 474 | 33% Plus | 305 N•m \[225 ft-lb\] |
| 2100 | 475 to 530 | 0 to 15% | 305 N•m \[225 ft-lb\] |
| 2100 | 475 to 530 | 16% and ABOVE | 380 N•m \[280 ft-lb\] |
| 2100 | 531 to 649 | All | 380 N•m \[280 ft-lb\] |
| 2100 | 650 and ABOVE | All | 405 N•m \[300 ft-lb\] |

Adjust the engine rpm to 1200 rpm. Adjust the dynamometer load to the test load as previously determined. Operate the engine at this setting until the coolant temperature indicates 71°C \[160°F\].

Check for leaks. Fix all leaks.

Check all of the gauges and record the readings.

Do **not** proceed to the next step until the blowby becomes stable within specifications.

![[oi800vk.png]]

Adjust the engine rpm to the torque peak rpm. Adjust the dynamometer load to equal two times the test load.

Operate the engine at this load for 2 minutes.

Check all the gauges and record the readings.

Do **not** proceed to the next step until the blowby becomes stable within specifications.

![[oi800vl.png]]

Maintain the engine rpm at torque peak rpm. Increase the dynamometer load to equal three times the test load.

Operate the engine at this load for 2 minutes.

Check all the gauges and record the readings.

Do **not** proceed to the next step until the blowby becomes stable within specifications.

![[oi800vm.png]]

Move the throttle lever to the FULL OPEN position. Increase the load until the engine rpm is at torque peak rpm.

Operate the engine at this setting for 10 minutes or until the blowby becomes stable within specifications.

Check all the gauges and record the readings.

![[oi800vn.png]]

Decrease the dynamometer load until the engine rpm increases to the rated RPM.

Operate the engine at this load for 5 minutes.

Check all the gauges and record the readings.

![[oi800vo.png]]

Decrease the dynamometer load completely.

> [!warning] CAUTION · Осторожно
> Do not turn the engine OFF immediately. The engine must be allowed to cool or damage to the turbocharger may result.

Move the throttle lever to the LOW IDLE position. Operate the engine at this setting for 3 to 5 minutes. This will allow the turbocharger and the other engine components to cool.

> [!warning] CAUTION · Осторожно
> Do not operate the engine at IDLE longer than specified. Excessive carbon formation can cause engine damage.

![[oi800vj.png]]

Turn the engine OFF.

![[oi800vp.png]]
