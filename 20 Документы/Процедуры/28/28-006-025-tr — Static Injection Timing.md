---
aliases:
  - "Статическая установка угла опережения впрыска"
type: "Процедура"
doc: "28-006-025-tr"
title_en: "Static Injection Timing"
title_ru: "Статическая установка угла опережения впрыска"
modified: "2021-06-10"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4021528"
figures: 20
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-006-025-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/28-006-025-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/28"
---

# Static Injection Timing
**Статическая установка угла опережения впрыска**

> [!abstract] Процедура · `28-006-025-tr`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4021528 — K38, K50, QSK38, and QSK50 Service Manual|4021528]]
> **Секции:** Section 6 - Injectors and Fuel Lines · Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2021-06-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-006-025-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/28-006-025-tr.pdf)

### General Information

The injection timing is the relative measurement of the distance remaining between the injector plunger and the injector cup when the piston is 5.16 mm \[0.2032 in\], or 19 degrees before top dead center on the compression stroke.

Injector timing is expressed by the amount of push tube travel remaining.

![[it800wa.png]]

The injection timing code appears on the engine dataplate. Codes are alphabetic letters that relate to a numerical specification.

Specifications can be found in the Control Part List (CPL) Manual, Bulletin 4021328.

![[it800wb.png]]

The next six illustrations are a brief review of the injection timing and how it can be adjusted.

Advanced timing means the fuel is injected earlier into the cylinder during the compression stroke. Retarded timing means the fuel injection occurs closer to top dead center in the cylinder.

![[06600442.png]]

The amount of push rod travel determines the time of fuel injection in relation to the piston position.

The high numerical value of push rod travel remaining indicates a greater degree of retarded or slow timing.

The low numerical value of push rod travel remaining indicates a greater degree of advanced or fast timing.

![[06600442.png]]

Injection timing changes are accomplished by advancing or retarding the camshaft follower action in relation to the piston position.

This is accomplished by changing the orientation of the camshaft lobe to the camshaft follower, using different camshaft gear keys.

Gear train timing (index mark alignment) **always** remains the same.

![[06600440.png]]

The camshaft key provides a means of indexing the camshaft with the gear.

Offset keys allow the camshaft profile to be rotated slightly while the gear train timing remains the same.

A camshaft gear offset in the direction of normal camshaft rotation (1 and 3) will result in retarded injection timing. The push rod travel numerical value will increase.

A camshaft gear offset in the direction opposite of camshaft normal rotation (2 and 4) will result in advanced injection timing. The push rod travel numerical value will decrease.

> [!note] Note · Примечание
> This applies to all Cummins® engines that have injectors actuated by the rocker levers.

> [!note] Note · Примечание
> The direction of normal rotation on a K38 or K50 engine crankshaft is **clockwise** as viewed from the front.

![[06600441.png]]

Offset keys can be identified by measuring the offset and referring to table "A" in the injection timing key worksheet at the end of this procedure.

> [!note] Note · Примечание
> Each 0.025 mm \[0.001 in\] of offset will cause a 0.0127 mm \[0.0005 in\] change in the push rod travel from a straight key.

> [!warning] CAUTION · Осторожно
> Always re-check the engine timing when a camshaft key, camshaft gear, or camshaft have been removed.

Below is the list of recommended keys if the camshaft, camshaft gear, camshaft key, or timing code has been changed. For codes without a recommended key, start with a straight key (S-302) and use the injection timing key worksheet at the end of this procedure to determine the correct timing. Also, use the injection timing key worksheet at the end of this procedure if the timing is incorrect after a recommended key is used.

If checking or setting the injection timing, it is recommended to use a testing gear. A testing gear is a camshaft gear that has been modified to provide a slip-fit on the camshaft.

Testing gears are **not** available from Cummins Inc. They can be made locally, using spare camshaft gears, by increasing the camshaft gear inner diameter.

| Measurements |  |  |
|---|---|---|
|  | mm | in |
| Testing Gear Inside Diameter: | 57.244 | 2.254 |

| Timing Code | Recommended Key | Direction of Offset |
|---|---|---|
| AE | 216782 | Opposite camshaft rotation |
| AJ | S-302 | None |
| AL | 3000493 | Opposite camshaft rotation |
| AM | 216782 | Opposite camshaft rotation |
| BL | S-302 | None |
| CL | S-302 | None |
| CV | 200704 | With camshaft rotation |
| GQ | 200709 | Opposite camshaft rotation |
| HE | S-302 | None |
| HR | S-302 | None |
| HQ | 3000493 | With camshaft rotation |
| IC | S-302 | None |
| IQ | S-302 | None |
| IR | S-302 | None |
| IV | 216782 | With camshaft rotation |
| JE | 200708 | Opposite camshaft rotation |
| JS | None | None |
| JT | 200708 | With camshaft rotation |
| JU | 200708 | With camshaft rotation |
| JZ | None | None |
| KA | 200708 | With camshaft rotation |
| KK | None | None |
| LK | None | None |
| LN | None | None |

![[it4kega.png]]

Install one camshaft follower on each bank.

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!warning] CAUTION · Осторожно
> The older camshaft follower mounting capscrews are special. They have a slot that allows the oil to flow to the camshaft follower assembly. The oil drilling intersects with the right capscrew hole. The use of standard capscrews can result in failure.

> [!note] Note · Примечание
> The reason for installing **only** one camshaft follower assembly on each bank is to save time if the camshaft must be removed to adjust the injection timing.

Service replacement camshaft followers are covered with a heavy preservative to prevent rust. This preservative must be removed completely, using solvent, before the parts are installed on the engine.

Install the Number 1 "RB" and Number 6 "LB" camshaft followers on the K38.

Install the Number 1 "RB" and Number 1 "LB" camshaft followers on the K50.

The shaft **must** fit correctly on both ring dowels. Install the capscrews.

| Camshaft Follower Capscrew Torque Value (Excluding K2000E and K1800E) |  |  |
|---|---|---|
| n.m |  | ft-lb |
| 39 | MIN | 29 |
| 42 | MAX | 31 |

![[kf400ha.png]]

K2000E and K1800E Capscrews

The camshaft follower shaft mounting capscrews were changed to a 12 point, grade 12.9 flange head capscrew, and do **not** have a slot.

> [!note] Note · Примечание
> This capscrew is required to make sure the shaft to cylinder block joint integrity is maintained, through higher capscrew torque.

![[kf6csna.png]]

> [!warning] CAUTION · Осторожно
> Do not use the original Grade 5 hex head capscrews. Use of these parts with the increased torque can result in capscrew failure and engine damage.

> [!note] Note · Примечание
> Do **not** use a washer with the flange head capscrew. The use of a washer will result in interference between the head of the capscrew and the camshaft follower cover.

> [!tip] Момент затяжки · Torque Value
> 65 n•m [48 ft-lb]

![[kf6csna.png]]

### Measure

> [!note] Note · Примечание
> In order to prevent incorrect readings the camshaft thrust plates **must** be tightened prior to taking measurements. Refer to Procedure 001-008 in Section 1.

> [!note] Note · Примечание
> The injection timing **must** be measured on at least one cylinder on each engine bank.

Use the injection timing tool, Part Number 3824942. The indicators (1) and (2) are identical.

1. Push tube travel indicator
2. Piston travel indicator
3. Piston plunger support assembly
4. Push rod plunger support assembly
5. Hold-down adapter
6. Extension assembly
7. Indicator stem extension

![[it8toga.png]]

The push rod plunger support assembly alignment is critical.

Install the push rod plunger support (4) in the outer slot of the piston plunger support (3).

Align the push rod plunger support with the mark. Tighten the capscrew.

Install the indicators (1) and (2) on the posts. Turn the indicators so they are **not** over the plungers.

Install the stem extension on the piston travel indicator.

![[it800sa.png]]

Install the injector push rod (8) for cylinder Number 1 "RB".

Install the timing tool in the injector bore for Number 1 "RB". Install the hold-down adapters.

Align the push rod plunger and the rod to be sure they are straight.

Tighten the support lock (9).

![[it4toha.png]]

> [!warning] CAUTION · Осторожно
> Use only the crankshaft to rotate the engine. The use of the gears will result in false measurements. Gear lash must be closed up in the direction of normal rotation (crankshaft clockwise).

> [!note] Note · Примечание
> The use of three guide bolts equally spaced in front of the crankshaft will help to rotate the engine when engine rotation is required prior to installation of the flywheel housing and barring mechanism. Do **not** use this method to rotate the engine against compression (i.e. after injectors are installed).

Turn the crankshaft in the direction of normal rotation while observing both of the timing tool plungers. Both plungers will begin moving up when the cylinder is on the compression stroke.

If both plungers are **not** moving up (one up and one down), the engine is on the exhaust stroke. Rotate the crankshaft 1 revolution (360 degrees) to set it at the compression stroke.

> [!missing]- Иллюстрация `it600sa.png` не извлечена — смотрите PDF-оригинал документа

Slowly rotate the crankshaft in the direction of normal rotation while observing the piston plunger (10). The plunger will move up, stop, and then begin to move down. The stop point of the plunger is top dead center. Rotate the engine opposite the direction of normal rotation until the plunger begins to move down. The cylinder is now slightly before top dead center.

> [!note] Note · Примечание
> In order to prevent incorrect readings the camshaft thrust plates **must** be tightened prior to taking measurements. Refer to Procedure 001-008 in Section 1.

Turn the indicator so that the stem is touching the plunger. Carefully move the indicator down until the needle has turned a minimum of five revolutions \[0.500 in\]. "LOCK" the indicator in position.

Slowly turn the crankshaft in the direction of normal rotation until the indicator needle stops turning **clockwise** (top dead center). Move the indicator down until there is **only** one revolution \[0.100 in\] of travel remaining until the indicator bottoms. Lock the indicator into position.

Adjust the indicator to "0".

Slowly and carefully rotate the crankshaft clockwise and counterclockwise checking that the indicator needle always stops at "0" before reversing direction. Readjust the indicator to "0" if required.

When rotating the crankshaft in the direction of normal operation and the indicator needle starts to reverse direction this indicates the piston is after top dead center.

> [!note] Note · Примечание
> Always "0" at top dead center with the crankshaft having just rotated in the direction of normal rotation.

![[it800sc.png]]

ZERO "0" Setting of the Push Rod Indicator

With the piston at top dead center, turn the push rod indicator so that the stem touches the plunger.

Carefully lower the indicator unit until it bottoms. Raise the indicator until the needle has turned a minimum of 3 revolutions \[0.300 in\]. Lock the indicator in position.

![[it800sd.png]]

Slowly turn the crankshaft in the direction of normal rotation. The push rod indicator will turn in the clockwise direction. Continue to turn the crankshaft in the direction of normal rotation until the push rod indicator stops (1), momentarily reverses direction (2) and stops again (3). The camshaft follower is now on the outer base circle of the camshaft.

Carefully lower the push rod travel indicator until it bottoms. Raise the indicator approximately 1/2 of a revolution \[0.050 in\]. "LOCK" the indicator in position.

Set the indicator at "0".

Record the amount of travel remaining in the push rod travel indicator for future reference.

![[it800se.png]]

Set the piston at \[0.2032 in\] before top dead center

Observe the piston travel indicator as you slowly rotate the crankshaft opposite the direction of normal rotation.

Stop rotating the crankshaft when the piston travel indicator indicates the piston is at top dead center.

![[it800sf.png]]

The crankshaft **must** be turned slowly to accurately count the indicator revolutions.

Turn the crankshaft opposite the direction of normal rotation until the indicator needle moves 2 1/2-revolutions \[0.250 in\].

The piston is now \[0.250 in\] before top dead center.

![[it800sg.png]]

> [!note] Note · Примечание
> Only move the piston to \[0.2032 in\] before top dead center by turning the crankshaft in the direction of normal rotation. If you accidently turn the crankshaft too far, you **must** turn the crankshaft opposite the direction of normal rotation MORE than \[0.2032 in\] before top dead center. Then very slowly turn the crankshaft in the direction of normal rotation until the indicator shows that the piston is \[0.2032 in\] before top dead center.

> [!note] Note · Примечание
> All K38 and K50 injection timing specifications are more than 1 indicator revolution \[0.100 in\].

Read the push rod travel indictor **counterclockwise** from "0". This is the injection timing measurement to compare to the specification. An example of \[0.118 in\] is shown.

If you are **not** sure of the number of push rod indicator revolutions, check by carefully raising the indicator stem until the indicator has bottomed. Lower the stem the amount of excess travel you set in the third preceding step. Lower the stem to the plunger. Read the indicator.

If the injection timing is within specification and you are using a testing gear, install the standard gear. Refer to Procedure 001-012 in Section 1. Repeat the injection timing procedure after the camshaft gear has cooled.

If the injection timing is **not** within specification, repeat the measurement procedure to check the tool set-up and the "0" settings.

If the timing is still **not** within specification, the camshaft key **must** be changed. Refer to Procedure 001-012 (Camshaft Gear (Camshaft Installed)) in Section 1, for instructions to remove the camshaft gear.

Record the orientation of any offset of the key. Use the following worksheet to determine an alternate key.

> [!note] Note · Примечание
> The timing measurement **must** be verified after changing the key.

> [!note] Note · Примечание
> When using a testing gear, the camshaft timing will tend to drop by \[0.002 in\] after the standard gear is installed. Target the camshaft timing upper limit to prevent the need to repeat the process.

![[it800sh.png]]

Answer each of the following questions in the spaces provided. The answers to the questions and the use of Tables A, B, and C will determine the timing key required to correct the injection timing.

A working example is attached for your review to illustrate the use of this worksheet.

| 1. | What is the current timing? | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
|---|---|---|
| 2. | What is the timing code? | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 3. | What is the timing specification for this code (± 0.002 in)? | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 4. | Is the current timing a larger or smaller number than the specification? If larger, advance the timing. If smaller, retard the timing. | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 5. | What is the difference between the current timing (answer to question 1) and the specification (answer to question 3)? | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 6. | Does the offset of the current key point in the same or opposite direction that the camshaft normally rotates? | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 7. | Use Table A to determine the current key part number. What is the amount of the offset of the current key? What is the part number of the current key? | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

| Table A |  |  |
|---|---|---|
| Timing Key Part Number | Offset |  |
| mm | in |  |
| S302 | None | None |
| 216294 | 0.09 | 0.004 |
| 200711 | 0.18 | 0.007 |
| 216782 | 0.28 | 0.011 |
| 200709 | 0.38 | 0.015 |
| 200704 | 0.51 | 0.020 |
| 200708 | 0.54 | 0.021 |
| 3000491 | 0.69 | 0.027 |
| 200706 | 0.83 | 0.033 |
| 3000492 | 0.91 | 0.036 |
| 200714 | 0.99 | 0.039 |
| 3000493 | 1.09 | 0.043 |
| 3000494 | 1.10 | 0.047 |
| 3000495 | 1.30 | 0.051 |

| 8. | Use Table B to determine how to use Table C. Circle or check the appropriate answer. |  |
|---|---|---|

| Table B |  |  |  |
|---|---|---|---|
| Answer to Question 4 | Answer to Question 6 | Beginning Point on Table C |  |
| Advance | Same | Top of column | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Advance | Opposite | Bottom of column | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Retard | Same | Bottom of column | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Retard | Opposite | Top of column | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

| 9. | Answer the following questions BEFORE using Table C to determine the new timing key part number. Find the current key part number listed at the top of the column on Table C. Move up or down the column (the answer to question 8). Do not pass 0.000 (zero). |  |
|---|---|---|

If you pass 0.000 (zero), you will be choosing a key that does the opposite of what you want it to do.

Stop when you locate the number nearest (± 0.002 in) to the required change in push rod travel (answer to question 5). Remain in this row. Move you finger to the right. The result is the new key part number and direction of offset the timing key **must** point.

- What is the part number of the new key?

> [!note] Note · Примечание
> Each column on Table C indicates the change in the push rod travel. The change will result if the key at the top of the column is removed and the new key indicated in the second column from the right is installed. The direction of offset will be pointing as indicated in the last column to the right on Table C.

| Table C |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S-302 | 200704 | 200706 | 200708 | 200709 | 200711 | 200714 | 216294 | 216782 | 3000491 | 3000492 | 3000493 | 3000494 | 3000495 | Part Number | Direction of Offset |
| 0.0256 | 0.0351 | 0.0411 | 0.0366 | 0.0326 | 0.0289 | 0.0441 | 0.0273 | 0.0311 | 0.0391 | 0.0436 | 0.0471 | 0.0491 | 0.0512 | 3000495 | Opposite |
| 0.0235 | 0.033 | 0.039 | 0.0345 | 0.0305 | 0.0268 | 0.042 | 0.0252 | 0.029 | 0.037 | 0.0415 | 0.045 | 0.0471 | 0.0491 | 3000494 | Opposite |
| 0.0215 | 0.031 | 0.037 | 0.0325 | 0.0285 | 0.0248 | 0.040 | 0.0232 | 0.027 | 0.035 | 0.0395 | 0.043 | 0.0441 | 0.0471 | 3000493 | Opposite |
| 0.0185 | 0.028 | 0.034 | 0.0295 | 0.0255 | 0.0218 | 0.037 | 0.0202 | 0.024 | 0.032 | 0.0365 | 0.040 | 0.042 | 0.0441 | 200714 | Opposite |
| 0.018 | 0.0275 | 0.0335 | 0.029 | 0.025 | 0.0213 | 0.0365 | 0.0197 | 0.0235 | 0.0315 | 0.036 | 0.0395 | 0.0415 | 0.0436 | 3000492 | Opposite |
| 0.0155 | 0.025 | 0.031 | 0.0265 | 0.0225 | 0.0188 | 0.034 | 0.0172 | 0.021 | 0.029 | 0.0335 | 0.037 | 0.039 | 0.0411 | 200706 | Opposite |
| 0.0135 | 0.023 | 0.029 | 0.0245 | 0.0205 | 0.0168 | 0.032 | 0.0152 | 0.019 | 0.027 | 0.0315 | 0.035 | 0.037 | 0.0391 | 3000491 | Opposite |
| 0.011 | 0.0205 | 0.0265 | 0.022 | 0.018 | 0.0143 | 0.0295 | 0.0127 | 0.0165 | 0.0245 | 0.029 | 0.0325 | 0.0345 | 0.0066 | 200708 | Opposite |
| 0.0095 | 0.019 | 0.025 | 0.0205 | 0.0165 | 0.0128 | 0.028 | 0.0112 | 0.015 | 0.023 | 0.0275 | 0.031 | 0.033 | 0.0351 | 200704 | Opposite |
| 0.007 | 0.0165 | 0.0225 | 0.018 | 0.014 | 0.0103 | 0.0255 | 0.0087 | 0.0125 | 0.0205 | 0.025 | 0.0285 | 0.0305 | 0.0326 | 200709 | Opposite |
| 0.0055 | 0.015 | 0.021 | 0.0165 | 0.0125 | 0.009 | 0.024 | 0.0072 | 0.011 | 0.019 | 0.0235 | 0.027 | 0.029 | 0.0311 | 216782 | Opposite |
| 0.0033 | 0.0128 | 0.0188 | 0.0143 | 0.0103 | 0.006 | 0.0218 | 0.005 | 0.009 | 0.0168 | 0.0213 | 0.0248 | 0.0268 | 0.0289 | 200711 | Opposite |
| 0.0017 | 0.0112 | 0.0172 | 0.0127 | 0.0087 | 0.0051 | 0.0202 | 0.0034 | 0.002 | 0.0152 | 0.0197 | 0.0232 | 0.0252 | 0.0273 | 216294 | Opposite |
| 0.000 | 0.0095 | 0.0155 | 0.011 | 0.007 | 0.003 | 0.0185 | 0.0017 | 0.006 | 0.0136 | 0.018 | 0.0205 | 0.0235 | 0.0256 | S-302 | N/A |
| 0.0017 | 0.0112 | 0.0172 | 0.0093 | 0.0053 | 0.0016 | 0.0168 | 0.000 | 0.0038 | 0.0118 | 0.0163 | 0.0198 | 0.0218 | 0.0239 | 216294 | Same |
| 0.0033 | 0.0062 | 0.0122 | 0.0077 | 0.0037 | 0.00 | 0.00152 | 0.0016 | 0.002 | 0.0102 | 0.0147 | 0.0182 | 0.0202 | 0.0223 | 200711 | Same |
| 0.0055 | 0.004 | 0.010 | 0.0055 | 0.0015 | 0.002 | 0.013 | 0.0038 | 0.000 | 0.008 | 0.0125 | 0.016 | 0.018 | 0.0201 | 216782 | Same |
| 0.007 | 0.0025 | 0.0085 | 0.004 | 0.00 | 0.0037 | 0.0115 | 0.0053 | 0.0015 | 0.0065 | 0.011 | 0.0145 | 0.0165 | 0.0186 | 200709 | Same |
| 0.0095 | 0.00 | 0.006 | 0.0015 | 0.0025 | 0.0062 | 0.009 | 0.0078 | 0.004 | 0.004 | 0.0085 | 0.012 | 0.014 | 0.0161 | 200704 | Same |
| 0.011 | 0.0015 | 0.0045 | 0.000 | 0.004 | 0.0077 | 0.0075 | 0.0093 | 0.0055 | 0.0025 | 0.007 | 0.0105 | 0.0125 | 0.0146 | 200708 | Same |
| 0.0095 | 0.000 | 0.006 | 0.0015 | 0.0025 | 0.0062 | 0.009 | 0.0078 | 0.004 | 0.004 | 0.0085 | 0.012 | 0.014 | 0.0161 | 200704 | Same |
| 0.011 | 0.0015 | 0.0045 | 0.00 | 0.004 | 0.0077 | 0.0075 | 0.0093 | 0.0055 | 0.0025 | 0.007 | 0.0105 | 0.0125 | 0.0146 | 200708 | Same |
| 0.0135 | 0.004 | 0.002 | 0.0025 | 0.0065 | 0.0102 | 0.005 | 0.0118 | 0.008 | 0.00 | 0.0045 | 0.008 | 0.010 | 0.0121 | 3000491 | Same |
| 0.0155 | 0.006 | 0.00 | 0.0045 | 0.0085 | 0.012 | 0.003 | 0.0138 | 0.010 | 0.002 | 0.0025 | 0.006 | 0.008 | 0.0101 | 200706 | Same |
| 0.018 | 0.0085 | 0.0025 | 0.007 | 0.011 | 0.0147 | 0.0005 | 0.0163 | 0.0125 | 0.0045 | 0.00 | 0.0035 | 0.0055 | 0.0076 | 3000492 | Same |
| 0.0185 | 0.009 | 0.003 | 0.0075 | 0.0115 | 0.0152 | 0.00 | 0.0168 | 0.013 | 0.005 | 0.0005 | 0.003 | 0.005 | 0.0071 | 200714 | Same |
| 0.0215 | 0.012 | 0.006 | 0.0105 | 0.0145 | 0.0182 | 0.003 | 0.0198 | 0.016 | 0.008 | 0.0035 | 0.000 | 0.002 | 0.0041 | 3000493 | Same |
| 0.0235 | 0.014 | 0.008 | 0.0125 | 0.0165 | 0.0202 | 0.005 | 0.0218 | 0.018 | 0.010 | 0.0055 | 0.002 | 0.000 | 0.0021 | 3000494 | Same |
| 0.0256 | 0.0161 | 0.010 | 0.0146 | 0.0186 | 0.0223 | 0.0071 | 0.0239 | 0.0020 | 0.0121 | 0.0076 | 0.0041 | 0.0021 | 0.000 | 3000495 | Same |

Answer each of the following questions in the spaces provided. The answers to the questions and the use of Tables A, B, and C will determine the timing key required to correct the injection timing.

A working example is attached for your review to illustrate the use of this worksheet.

| 1. | What is the current timing? | \_\_\_\_\_0.267\_\_\_\_\_\_\_\_\_\_ |
|---|---|---|
| 2. | What is the timing code? | \_\_\_\_\_\_JF\_\_\_\_\_\_\_\_\_\_\_\_ |
| 3. | What is the timing specification for this code (± 0.002 in)? | \_\_\_\_\_0.279\_\_\_\_\_\_\_\_\_\_ |
| 4. | Is the current timing a larger or smaller number than the specification? If larger, advance the timing. If smaller, retard the timing. | \_\_\_\_Smaller\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_Retard\_\_\_\_\_\_\_\_\_\_ |
| 5. | What is the difference between the current timing (answer to question 1) and the specification (answer to question 3)? | \_\_\_\_0.012\_\_\_\_\_\_\_\_\_\_\_ |
| 6. | Does the offset of the current key point in the same or opposite direction that the camshaft normally rotates? | \_\_\_\_Same\_\_\_\_\_\_\_\_\_\_\_\_ |
| 7. | Use Table A to determine the current key part number. What is the amount of the offset of the current key? What is the part number of the current key? | \_\_\_\_0.007\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_200711\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

| Table A |  |  |
|---|---|---|
| Timing Key Part Number | Offset |  |
| mm | in |  |
| S302 | None | None |
| 216294 | 0.09 | 0.004 |
| 200711 | 0.18 | 0.007 |
| 216782 | 0.28 | 0.011 |
| 200709 | 0.38 | 0.015 |
| 200704 | 0.51 | 0.020 |
| 200708 | 0.54 | 0.021 |
| 3000491 | 0.69 | 0.027 |
| 200706 | 0.83 | 0.033 |
| 3000492 | 0.91 | 0.036 |
| 200714 | 0.99 | 0.039 |
| 3000493 | 1.09 | 0.043 |
| 3000494 | 1.10 | 0.047 |
| 3000495 | 1.30 | 0.051 |

| 8. | Use Table B to determine how to use Table C. Circle or check the appropriate answer. |  |
|---|---|---|

| Table B |  |  |  |
|---|---|---|---|
| Answer to Question 4 | Answer to Question 6 | Beginning Point on Table C |  |
| Advance | Same | Top of column | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Advance | Opposite | Bottom of column | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Retard | Same | Bottom of column | \_\_\_\_\_\_\_\_\_\_\_X\_\_\_\_\_\_\_\_ |
| Retard | Opposite | Top of column | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

| 9. | Answer the following questions BEFORE using Table C to determine the new timing key part number. Find the current key part number listed at the top of the column on Table C. Move up or down the column (the answer to question 8). Do not pass 0.000 (zero). |  |
|---|---|---|

If you pass 0.000 (zero), you will be choosing a key that does the opposite of what you want it to do.

Stop when you locate the number nearest (± 0.002 in) to the required change in push rod travel (answer to question 5). Remain in this row. Move you finger to the right. The result is the new key part number and direction of offset the timing key **must** point.

- What is the part number of the new key? **200706**

> [!note] Note · Примечание
> Each column on Table C indicates the change in the push rod travel. The change will result if the key at the top of the column is removed and the new key indicated in the second column from the right is installed. The direction of offset will be pointing as indicated in the last column to the right on Table C.

| Table C |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S-302 | 200704 | 200706 | 200708 | 200709 | **200711** | 200714 | 216294 | 216782 | 3000491 | 3000492 | 3000493 | 3000494 | 3000495 | Part Number | Direction of Offset |
| 0.0256 | 0.0351 | 0.0411 | 0.0366 | 0.0326 | 0.0289 | 0.0441 | 0.0273 | 0.0311 | 0.0391 | 0.0436 | 0.0471 | 0.0491 | 0.0512 | 3000495 | Opposite |
| 0.0235 | 0.033 | 0.039 | 0.0345 | 0.0305 | 0.0268 | 0.042 | 0.0252 | 0.029 | 0.037 | 0.0415 | 0.045 | 0.0471 | 0.0491 | 3000494 | Opposite |
| 0.0215 | 0.031 | 0.037 | 0.0325 | 0.0285 | 0.0248 | 0.040 | 0.0232 | 0.027 | 0.035 | 0.0395 | 0.043 | 0.0441 | 0.0471 | 3000493 | Opposite |
| 0.0185 | 0.028 | 0.034 | 0.0295 | 0.0255 | 0.0218 | 0.037 | 0.0202 | 0.024 | 0.032 | 0.0365 | 0.040 | 0.042 | 0.0441 | 200714 | Opposite |
| 0.018 | 0.0275 | 0.0335 | 0.029 | 0.025 | 0.0213 | 0.0365 | 0.0197 | 0.0235 | 0.0315 | 0.036 | 0.0395 | 0.0415 | 0.0436 | 3000492 | Opposite |
| 0.0155 | 0.025 | 0.031 | 0.0265 | 0.0225 | 0.0188 | 0.034 | 0.0172 | 0.021 | 0.029 | 0.0335 | 0.037 | 0.039 | 0.0411 | 200706 | Opposite |
| 0.0135 | 0.023 | 0.029 | 0.0245 | 0.0205 | 0.0168 | 0.032 | 0.0152 | 0.019 | 0.027 | 0.0315 | 0.035 | 0.037 | 0.0391 | 3000491 | Opposite |
| 0.011 | 0.0205 | 0.0265 | 0.022 | 0.018 | 0.0143 | 0.0295 | 0.0127 | 0.0165 | 0.0245 | 0.029 | 0.0325 | 0.0345 | 0.0066 | 200708 | Opposite |
| 0.0095 | 0.019 | 0.025 | 0.0205 | 0.0165 | 0.0128 | 0.028 | 0.0112 | 0.015 | 0.023 | 0.0275 | 0.031 | 0.033 | 0.0351 | 200704 | Opposite |
| 0.007 | 0.0165 | 0.0225 | 0.018 | 0.014 | 0.0103 | 0.0255 | 0.0087 | 0.0125 | 0.0205 | 0.025 | 0.0285 | 0.0305 | 0.0326 | 200709 | Opposite |
| 0.0055 | 0.015 | 0.021 | 0.0165 | 0.0125 | 0.009 | 0.024 | 0.0072 | 0.011 | 0.019 | 0.0235 | 0.027 | 0.029 | 0.0311 | 216782 | Opposite |
| 0.0033 | 0.0128 | 0.0188 | 0.0143 | 0.0103 | 0.006 | 0.0218 | 0.005 | 0.009 | 0.0168 | 0.0213 | 0.0248 | 0.0268 | 0.0289 | 200711 | Opposite |
| 0.0017 | 0.0112 | 0.0172 | 0.0127 | 0.0087 | 0.0051 | 0.0202 | 0.0034 | 0.002 | 0.0152 | 0.0197 | 0.0232 | 0.0252 | 0.0273 | 216294 | Opposite |
| 0.000 | 0.0095 | 0.0155 | 0.011 | 0.007 | 0.003 | 0.0185 | 0.0017 | 0.006 | 0.0136 | 0.018 | 0.0205 | 0.0235 | 0.0256 | S-302 | N/A |
| 0.0017 | 0.0112 | 0.0172 | 0.0093 | 0.0053 | 0.0016 | 0.0168 | 0.000 | 0.0038 | 0.0118 | 0.0163 | 0.0198 | 0.0218 | 0.0239 | 216294 | Same |
| 0.0033 | 0.0062 | 0.0122 | 0.0077 | 0.0037 | 0.00 | 0.00152 | 0.0016 | 0.002 | 0.0102 | 0.0147 | 0.0182 | 0.0202 | 0.0223 | 200711 | Same |
| 0.0055 | 0.004 | 0.010 | 0.0055 | 0.0015 | 0.002 | 0.013 | 0.0038 | 0.000 | 0.008 | 0.0125 | 0.016 | 0.018 | 0.0201 | 216782 | Same |
| 0.007 | 0.0025 | 0.0085 | 0.004 | 0.00 | 0.0037 | 0.0115 | 0.0053 | 0.0015 | 0.0065 | 0.011 | 0.0145 | 0.0165 | 0.0186 | 200709 | Same |
| 0.0095 | 0.00 | 0.006 | 0.0015 | 0.0025 | 0.0062 | 0.009 | 0.0078 | 0.004 | 0.004 | 0.0085 | 0.012 | 0.014 | 0.0161 | 200704 | Same |
| 0.011 | 0.0015 | 0.0045 | 0.000 | 0.004 | 0.0077 | 0.0075 | 0.0093 | 0.0055 | 0.0025 | 0.007 | 0.0105 | 0.0125 | 0.0146 | 200708 | Same |
| 0.0095 | 0.000 | 0.006 | 0.0015 | 0.0025 | 0.0062 | 0.009 | 0.0078 | 0.004 | 0.004 | 0.0085 | 0.012 | 0.014 | 0.0161 | 200704 | Same |
| 0.011 | 0.0015 | 0.0045 | 0.00 | 0.004 | 0.0077 | 0.0075 | 0.0093 | 0.0055 | 0.0025 | 0.007 | 0.0105 | 0.0125 | 0.0146 | 200708 | Same |
| 0.0135 | 0.004 | 0.002 | 0.0025 | 0.0065 | 0.0102 | 0.005 | 0.0118 | 0.008 | 0.00 | 0.0045 | 0.008 | 0.010 | 0.0121 | 3000491 | Same |
| 0.0155 | 0.006 | 0.00 | 0.0045 | 0.0085 | **0.012** | 0.003 | 0.0138 | 0.010 | 0.002 | 0.0025 | 0.006 | 0.008 | 0.0101 | **200706** | **Same** |
| 0.018 | 0.0085 | 0.0025 | 0.007 | 0.011 | 0.0147 | 0.0005 | 0.0163 | 0.0125 | 0.0045 | 0.00 | 0.0035 | 0.0055 | 0.0076 | 3000492 | Same |
| 0.0185 | 0.009 | 0.003 | 0.0075 | 0.0115 | 0.0152 | 0.00 | 0.0168 | 0.013 | 0.005 | 0.0005 | 0.003 | 0.005 | 0.0071 | 200714 | Same |
| 0.0215 | 0.012 | 0.006 | 0.0105 | 0.0145 | 0.0182 | 0.003 | 0.0198 | 0.016 | 0.008 | 0.0035 | 0.000 | 0.002 | 0.0041 | 3000493 | Same |
| 0.0235 | 0.014 | 0.008 | 0.0125 | 0.0165 | 0.0202 | 0.005 | 0.0218 | 0.018 | 0.010 | 0.0055 | 0.002 | 0.000 | 0.0021 | 3000494 | Same |
| 0.0256 | 0.0161 | 0.010 | 0.0146 | 0.0186 | 0.0223 | 0.0071 | 0.0239 | 0.0020 | 0.0121 | 0.0076 | 0.0041 | 0.0021 | 0.000 | 3000495 | Same |
