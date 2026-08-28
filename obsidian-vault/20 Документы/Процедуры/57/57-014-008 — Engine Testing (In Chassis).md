---
aliases:
  - "Испытание двигателя на машине"
type: "Процедура"
doc: "57-014-008"
title_en: "Engine Testing (In Chassis)"
title_ru: "Испытание двигателя на машине"
modified: "2015-10-27"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021539"
figures: 17
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/57/57-014-008.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/57-014-008.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/57"
---

# Engine Testing (In Chassis)
**Испытание двигателя на машине**

> [!abstract] Процедура · `57-014-008`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021539 — QST30 Service Manual|4021539]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2015-10-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/57/57-014-008.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/57-014-008.pdf)

### Stall Speed Check

The stall speed is the engine speed (rpm) obtained at full throttle when the converter output shaft is locked.

The vehicle brakes do **not always** hold an electronically controlled transmission.

![[00600065.png]]

> [!warning] CAUTION · Осторожно
> Do not exceed 120°C \[250°F\] converter oil temperature. If the oil temperature exceeds 120°C \[250°F\], put the transmission in neutral, and operate the engine until the oil temperature is below 120°C \[250°F\]. Check the converter oil level.

![[oi8gakh.png]]

The following equipment is needed for this check:

- Stopwatch
- INSITE™ electronic service tool or a handheld optical tachometer, Part Number ST-3377462
- Equipment manufacturer's stall speed and time-to-stall specifications.

![[oi8gaki.png]]

Monitor the engine rpm with the INSITE™ electronic service tool.

![[fp8gahb.png]]

Put the gear selector in the highest gear or full forward.

In some types of equipment, it is also necessary to engage the hydraulics.

![[oi800ch.png]]

Be sure the vehicle has good brakes and air pressure in the brake system.

The brakes **must** prevent the vehicle from moving when the engine is at full throttle.

Engage the vehicle brakes or keep the vehicle from moving.

![[oi800ks.png]]

Operate the engine until the coolant temperature is up to 70°C \[158°F\] and the converter temperature is 80°C \[180°F\] or above.

Alternately, shift from neutral to the highest speed gear possible and operate at partial throttle. This will warm the entire system uniformly.

![[oi800cj.png]]

Bring the engine speed back to low idle.

![[oi800ck.png]]

> [!warning] CAUTION · Осторожно
> Do not exceed 120°C \[250°F\] converter oil temperature. If the oil temperature exceeds 120°C \[250°F\], put the transmission in neutral, and operate the engine until the oil temperature is below 120°C \[250°F\]. Check the converter oil level.

Move the throttle to the full-open position. Do **not** perform this test for more than 15 seconds. If the engine speed continues to slowly increase, the torque converter fluid is being overheated.

![[oi800cl.png]]

Check the engine speed (rpm) at the point of stall.

**Always** hold the speed until it is stable.

Take several readings. Be sure the reading is accurate.

![[oi8gakk.png]]

Check the stall speed (rpm) against the specifications that are for the equipment, converter, or automatic transmission.

> [!note] Note · Примечание
> The stall speed for the engine and converter/transmission can vary ±8 percent from the manufacturer's specifications.

![[oi800cm.png]]

If the stall speed is **not** within the specifications, refer to the Stall Speed Check Lists at the end of this section.

Check the equipment manufacturer service information for other reasons for stall speed problems.

![[oi800kw.png]]

After performing the Stall Speed Check through the torque converter fluid being overheated, calculate the engine stall speed.

Stall Speed Reference Point Calculation

Stall Speed x 90 percent = Stall Speed Reference Point

Example: 2,089 rpm x 0.90 = 1880 rpm

![[nobox.png]]

If the cause for the stall speed being too low is low engine power output, refer to the Engine Power Output Low troubleshooting symptom tree in Section TS. Make the correct repair based on the fuel rate, fuel pressure, and intake manifold pressure readings.

![[oi801ka.png]]

### Time Speed Check

Quickly move the throttle to the full-open position and start the stopwatch at the same time.

![[oi800cn.png]]

When the engine speed is 90 percent of the stall speed rpm, stop the stopwatch.

> [!note] Note · Примечание
> The type of unit and the stall speed rpm will be different for different types of equipment. Most types have a stall speed between 8 and 12 seconds.

![[oi8gakl.png]]

Check the equipment manufacturer's specifications for the time to stall or the acceleration time.

If the time is excessive, refer to the Engine Acceleration/Response Poor troubleshooting symptom tree in Section TS.

![[oi800co.png]]

If the stall speed is too low, check the following:

| Stall Speed Too Low Check List |  |  |  |
|---|---|---|---|
| Order of Check | Yes | No | Check |
| 1. |  |  | The tachometer is in error. |
| 2. |  |  | The engine is up to or above 70°C \[160°F\]. |
| 3. |  |  | The converter oil is up to temperature 80°C \[180°F\]. |
| 4. |  |  | The stall has been held long enough for the engine to accelerate to full power. |
| 5. |  |  | The match curve stall speed was recorded correctly. |
| 6. |  |  | The converter oil is to the converter manufacturer's recommendation. Society of Automotive Engineers SAE (example: SAE 30 instead of SAE 10). |
| 7. |  |  | The engine-driven accessory power requirements exceed 10 percent of the gross engine power. Check for abnormal accessory horsepower losses such as hydraulic pumps, large fans, oversize compressors, etc. Either remove the accessory or accurately determine the power requirement and adjust accordingly. |
| 8. |  |  | The unit is operating at an altitude high enough to affect the engine power. |
| 9. |  |  | The converter charging pressure is correct. |
| 10. |  |  | The tailshaft governor is interfering with and preventing a full-throttle opening. (Disconnect the tailshaft governor.) |
| 11. |  |  | The converter blading is interfering or in a stage of failure. Check the sump or filter for metal particles. |
| 12. |  |  | The converter stators are free-wheeling instead of locking. |
| 13. |  |  | The engine is set for power other than that specified on the power curve. |
| 14. |  |  | The converter is wrong due to improper build or rebuild of unit. |
| 15. |  |  | The converter is performing to the published absorption curve. |
| 16. |  |  | The engine and converter match is correct. Check the engine and converter models for the proper match. |
| 17. |  |  | The engine is matched to an oversize converter. (If this condition is believed to exist, please report the engine-converter-accessory information to the factory.) |
| 18. |  |  | The engine power is down. (The engine torque rise could be less than shown on the standard engine curve.) See the fuel setting adjustments and the turbocharger air manifold pressure check. |

It is sometimes easier to change the engine fuel rate than to determine the true cause for low stall speed, but the customer ends up with an overfueled engine that will also reduce durability. Do **not** increase the fuel rate as a cure-all.

If the stall speed is too high, check the following:

| Stall Speed Too High Check List |  |  |  |
|---|---|---|---|
| Order of Check | Yes | No | Check |
| 1. |  |  | The engine is high in power. |
| 2. |  |  | The tachometer is in error. |
| 3. |  |  | The accessory power requirements are less than 10 percent of the gross engine power. |
| 4. |  |  | The converter oil is aerating (foaming) - check for low oil level, air leaks in suction line, and oil that does **not** contain a foam inhibitor, or suction screen or filter. (It should be accompanied by a noticeable loss of machine performance.) |
| 5. |  |  | The converter is being held at full stall. Check for a slipping front disconnect clutch or a rotating output shaft. On the converter-transmission package, this can be impossible to check. |
| 6. |  |  | The converter turbine element is beginning to fail and lose blades, or the converter was originally built with the wrong-size element. |
| 7. |  |  | The engine and converter match is correct (due to a revision in the engine rating or the converter performance). |
| 8. |  |  | On transmission-converter units with an oil sump in the transmission: If the oil level is too high, it can cause severe aeration due to parts dipping in the oil. |
| 9. |  |  | The converter is performing to the published absorption curve. |
| 10. |  |  | The converter charging pressure is correct. |

The reasons for abnormal stall speeds listed above are some which have been encountered by Cummins Inc. representatives and probably do **not** include **all** possible causes. The correction of the problem is either covered in the vehicle service manual, the converter service manual, or is self-explanatory.
