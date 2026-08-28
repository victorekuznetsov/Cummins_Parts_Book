---
type: "Процедура"
doc: "35-005-054-tr"
title_en: "Stall Speed Test"
modified: "2009-01-23"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 14
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-005-054-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-005-054-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Stall Speed Test

> [!abstract] Процедура · `35-005-054-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2009-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-005-054-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-005-054-tr.pdf)

### Stall Speed Check

Converter Transmissions Stall Speed

The stall speed is the engine speed (rpm) obtained at full throttle when the converter output shaft is locked.

> [!note] Note · Примечание
> It is possible the vehicle brakes will **not** hold an electronically controlled transmission.

![[oi800kf.png]]

> [!warning] CAUTION · Осторожно
> Do not exceed 120°C \[250°F\] converter oil temperature. Overheating can result and converter damage can occur. If the oil temperature exceeds 120°C \[250°F\], put the transmission in neutral and operate the engine until the oil temperature is below 120°C \[250°F\]. Check the converter oil level.

![[oi8gakh.png]]

The following equipment is needed for this check:

- Stopwatch
- Cummins electronic service tool
- Equipment manufacturer's stall speed and time to stall specifications.

![[oi8gaki.png]]

Place the gear selector in the highest gear or full forward.

![[oi800ch.png]]

Make sure the vehicle has good brakes and air pressure in the brake system.

The brakes **must** prevent the vehicle from moving when the engine is at full throttle.

Engage the vehicle brakes to keep the vehicle from moving.

![[oi800ks.png]]

Operate the engine until the converter temperature is 80°C \[180°F\] or above.

![[oi800cj.png]]

Bring the engine speed back to low idle.

![[oi800ck.png]]

> [!warning] CAUTION · Осторожно
> Do not exceed 120°C \[250°F\] converter oil temperature. Overheating and damage to the converter can occur.

Quickly move the throttle to the full OPEN position.

![[oi800cl.png]]

Check the engine speed (rpm) at the point of stall:

- **Always** hold the speed until it is stable
- Take several readings
- Make sure the readings are accurate.

![[oi8gakk.png]]

Check the speed (rpm) against the specifications for the equipment, converter, or automatic transmission.

The stall speed for the engine and converter/transmission can vary ±8 percent from the manufacturer's specifications.

![[oi800cm.png]]

If the stall speed is **not** within the specifications, refer to the Stall Speed Check List at the end of this section.

Check the equipment manufacturer's troubleshooting procedures for other reasons for stall speed problems.

![[oi800kw.png]]

### Time Speed Check

Perform the previous Stall Speed Check procedure through the “check the engine speed (rpm) at the point of stall” step; then:

- Quickly move the throttle to the full OPEN position and start the stopwatch at the same time

![[oi800cn.png]]

- When the engine speed is 90 percent of the stall speed rpm, stop the stopwatch

- Stall speed 2089 \[2089 X 0.90 = 1880 rpm\]

The type of unit and the stall speed rpm can make the stall speed time a maximum of ten seconds.

![[oi8gakl.png]]

Check the equipment manufacturer's specifications for the time to stall or the acceleration time.

![[oi800co.png]]

### Stall Speed Check List

If the stall speed is too low, Check the following:

|  | Yes | No |  |
|---|---|---|---|
| 1. |  |  | The vehicle tachometer is in error. |
| 2. |  |  | The engine is up to or above 70°C \[160°F\]. |
| 3. |  |  | The converter oil is up to temperature 80°C \[180°F\] |
| 4. |  |  | The stall has been held long enough for the engine to accelerate to full power. |
| 5. |  |  | The match curve stall speed was recorded correctly. |
| 6. |  |  | The converter oil is to the converter manufacturer's recommendation (SAE 30 instead of SAE 10, for instance). |
| 7. |  |  | The engine-driven accessory power requirements exceed 10 percent of the gross engine power. Check for abnormal accessory horsepower losses, such as hydraulic pumps, large fans, oversize compressors, and so on. Either remove the accessory or accurately determine the power requirement and adjust accordingly. |
| 8. |  |  | The converter charging pressure is correct. |
| 9. |  |  | The tailshaft governor is interfering with and preventing a full-throttle opening. Disconnect the tailshaft governor. Do **not** exceed the manufacturer's maximum output speed. |
| 10. |  |  | The converter blading is interfering or in a stage of failure. Check the sump or filter for particles. |
| 11. |  |  | The converter blading is interfering, or in a stage of failure. Check the sump or filter for particles. |
| 12. |  |  | The engine is set for power other than that specified on the power curve. |
| 13. |  |  | The converter is wrong due to improper build or rebuild of the unit. |
| 14. |  |  | The converter is performing to the published absorption curve. |
| 15. |  |  | The engine and converter match is correct. Check the engine and converter models for proper match. |
| 16. |  |  | The engine is matched to too large of a converter. If this condition is believed to exist, report the engine-converter-accessory information to the factory. |
| 17. |  |  | The engine power is down. Refer to the Engine Power Output Low performance tree. |

If the stall speed is too high, check the following:

|  | Yes | No |  |
|---|---|---|---|
| 1. |  |  | The accessory power requirements are less than 10 percent of the gross engine power. |
| 2. |  |  | The converter oil is aerating or foaming. Check for low oil level, air leaks in suction line, lack of foam inhibitor in the oil, or suction screen or filter. It is accompanied by a noticeable loss of machine performance. |
| 3. |  |  | The converter is benign held at full stall. Check for slipping front disconnect clutch or a rotating output shaft. On the converter-transmission package, this can be impossible to check. |
| 4. |  |  | The converter turbine element is beginning to fail and lose blades, or the converter was originally built with the wrong size element. |
| 5. |  |  | The engine and converter match is correct, due to a revision in the engine rating or the converter performance. |
| 6. |  |  | If the oil level is too high on the transmission-converter units with the oil sump in the transmission, it can cause severe aeration due to parts dipping into the oil. |
| 7. |  |  | The converter is performing to the published absorption curve. |
| 8. |  |  | The converter charging pressure is correct. |

The reasons for abnormal stall speeds listed above are some that have been encountered by Cummins representatives and possibly do **not** include all causes. The correction of the problem is either covered in the vehicle service manual, the converter service manual, or is self-explanatory.
