---
type: "TSB"
doc: "tsb150099"
title_en: "Advanced Dynamic Efficient Powertrain Technology (ADEPT™)"
modified: "2023-06-19"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150099.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150099.pdf"
tags:
  - "документ/tsb"
---

# Advanced Dynamic Efficient Powertrain Technology (ADEPT™)

> [!abstract] TSB · `tsb150099`
> **Даты:** изменён 2023-06-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150099.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150099.pdf)

## Advanced Dynamic Efficient Powertrain Technology (ADEPT™)

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

The purpose of this document is to announce the availability of Advanced Dynamic Efficient Powertrain Technology (ADEPT™ technology) on select Cummins® engines. See Table 1 below.

**Product Affected**

| Table 1, Product Affected |  |  |
|---|---|---|
| Engine Model | Model Year | CPL |
| ISX15 CM2350 X101 | 2013 | 3937 |
| 2015 | 4583 |  |
| 2016 | 4586 |  |
| 2016 | 4761 |  |
| X15 CM2350 X114B | 2017 | 4342 |
| 2018 |  |  |
| 2019 |  |  |
| X15 CM2450 X124B | 2020 | 5348 |
| 2021 | 5535/5779 |  |
| 2022 | 5881 |  |
| 2023 | 5881 |  |
| X12 CM2350 X119B | 2018 | 4814 |
| 2019 |  |  |
| 2020 | 5580 |  |
| ISX15 CM2250 SN | E4 | 3566 |
| 3567 |  |  |
| E5 | 3574 |  |
| 3575 |  |  |

**Compatibility**

| **Table 2, Compatible OEMs** |  |  |  |  |
|---|---|---|---|---|
| Freightliner® Trucks | International™ Trucks | Kenworth™ Trucks | Peterbilt™ Trucks | Volvo® Trucks |

| Table 3, Compatible Eaton™ Transmissions |  |
|---|---|
| Advantage® Series EA3 | UltraShift® PLUS VAS |
| Advantage® Series EC3 (SmartAdvantage) | UltraShift® PLUS VCS |
| UltraShift® PLUS LAS | UltraShift® PLUS VHP |
| UltraShift® PLUS LSE | UltraShift® PLUS VMS |
| UltraShift® PLUS MHP | UltraShift® PLUS VXP |
| UltraShift® PLUS MXP | Endurant TM |

**Table 4, Compatible Adaptive Cruise Control System**

Bendix® Wingman®

Wabco™ OnGuard™

Adaptive cruise control is **not** required to enable ADEPT™ technology.

See X15 CM2450 X124B Service Manual, Bulletin 5504583. Refer to Procedure 019-665 in Section 19.

**Description of Change**

ADEPT™ technology is a set of electronic features including SmartTorque2 and SmartCoast™, Predictive Gear Shifting, Predictive Engine Braking, On-ramp Boost, Predictive Road Speed Governor, Dynamic Power and Hill Roll Out.

Predictive Gear Shifting, Predictive Engine Braking, and On-ramp Boost require an ADEPT™ Technology ECM Calibration Code. See ADEPT column in Table 6 below.

Dynamic Power and Hill Roll Out are available **only** for X15 CM2450 X124B engine ratings that have ECM calibration codes starting with 'KW' located in Table 6 in the ADEPT™ Technology ECM Calibration Code column.

SmartTorque2 senses the selected gear, road grade, and overall engine load. As these conditions vary, SmartTorque2 determines the exact amount of torque required to maintain road speed and eliminate unnecessary downshifts.

SmartCoast™ has been added to improve the efficiency of coasting events. SmartCoast™ will disengage the driveline on moderate downhill grades or when the operator lifts off the accelerator pedal, allowing the engine to return to idle.

Predictive Gear Shifting improves vehicle speed tracking performance during cruise control. The feature will utilize vehicle characteristics and road grade profile information to determine the proper transmission gear when the engine is power limited on hills.

Predictive Engine Braking aims to enhance the vehicle speed limiting capability of existing engine brake features based on the upcoming road grade. The features to which this predictive functionality can apply are Cruise Control and Engine Brake Interaction or Maximum Vehicle Speed Control.

On-ramp Boost is a performance feature that improves vehicle acceleration on an on-ramp leading to an interstate which increases the merging speeds and assists in an easier merging maneuver. It allows the vehicle to operate in a fuel-efficient mode during regular operation and allows better performance during critical situations.

Predictive Road Speed Governor improves efficiency of the vehicle by adjusting the Road Speed Governor within programmable offsets based on current and upcoming road grade.

Dynamic Power aims to improve overall engine efficiency by limiting use of excessive torque when it is **not** required. Utilizing similar references as SmartTorque2, Dynamic Power modulates available engine torque to reflect current vehicle operation & environmental influence.

Hill Roll Out is a powertrain efficiency feature which allows early disengagement of engine brakes and allows a temporary vehicle speed increase when the vehicle is approaching end of downhill moderate grades. This predictive functionality allows the vehicle to harness momentum to traverse upcoming terrain. Hill Roll Out can request SmartCoast™ events to increase efficiency based on the operating mode enabled for SmartCoast™. Reference SmartCoast™ section for more information on SmartCoast™ operation.

> [!note] Note · Примечание
> Predictive Gear Shifting, Predictive Engine Braking, On-ramp Boost, Dynamic Power, Predictive Road Speed Governor, and Hill Roll Out require either a Connectivity Module, Cummins® Route Parameter Manager (RPM) or an OEM Predictive Cruise Control module to get look-ahead road information.

**Reason for Change**

Fuel economy and performance improvement option

**Service Instructions**

Electronic Tools Required:

- INSITE™ Pro electronic service tool for engine calibration update
- ServiceRanger™ 4 for transmission software update (if required)

1. Check engine, transmission, and adaptive cruise control system compatibility. See Table 1, Table 2, Table 3, and Table 4 for applicability.

2. Review ADEPT™ technology documentation on cumminsengines.com and communicate modification charge to customer.

- The customer will incur a fleet count charge as well as the stated modification charge.

3. Verify that transmission software meets minimum software requirement. See Table 5 below.

| Table 5, Transmission Software Version |  |  |
|---|---|---|
| Transmission Type | Advantage® or Ultrashift® | Endurant™ |
| Software Version | 5569960 or newer | 5516018 or newer |
| SmartTorque2 | Supported | Supported |
| Predictive Gear Shifting | **Not** Supported | Supported |
| SmartCoast (Cruise Control) | Supported | Supported |
| SmartCoast (Accelerator Control) | **Not** Supported | Supported |
| SmartCoast (Cruise Control and Accelerator Control) | **Not** Supported | Supported |
| SmartCoast (Maximum Economy) | **Not** Supported | Supported |
| Predictive Engine Braking | **Not** Supported | Supported |
| On-Ramp Boost | **Not** Supported | Supported |
| Predictive Road Speed Governor | Supported | Supported |
| Dynamic Power | **Not** Supported | Supported |
| Hill Roll Out | **Not** Supported | Supported |

- If necessary, update the transmission using the Eaton™ ServiceRanger™ 4 service tool.
- If minimum transmission software requirement is **not** met, ADEPT™ features will **not** function properly and fault codes can be triggered.

4. Update the engine calibration to ADEPT™ technology calibration using selection matrix in Table 6 below. See the ISX15 CM2350 X101 Service Manual, Bulletin 4310641. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032]] in section 19. See the X15 CM2350 X114B - Efficiency Series Service Manual, Bulletin [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual\|5411181]]. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032]] in section 19. See the X15 CM2450 X124B Service Manual, Bulletin 5504583. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032]] in Section 19.

> [!note] Note · Примечание
> Dynamic Power and Hill Roll Out are available **only** for X15 CM2450 X124B engine ratings that have ECM calibration codes starting with 'KW' located in Table 6 in the ADEPT™ Technology ECM Calibration Code column.

5. Clear resulting fault codes

- Depending on the download sequence an inactive fault code 5297 can be logged in the ECM after the upgrade as a result of transmission and ECM communication loss during calibration event.

6. Verify ADEPT™ features are turned on in the ECM. Under the Features and Parameters section in INSITE™ electronic service tool:

For Ultrashift® or Advantage® Transmissions:

- Adjust “SmartCoast” to “Enabled” if set to “Disabled” (May be located in the Cruise Control section or as a separate featured called SmartCoast). The Advantage or Ultrashift transmissions **only** support Smart Coast in cruise control.
- Adjust “Load Based Torque Control” to “Smart Torque 2” if set to “Base”.
- Adjust “Road Speed Governor Type” from “Traditional” to “Predictive”. If Predictive Road Speed Governor is unavailable in the calibration, “Road Speed Governor Type” will be Read **Only**.

For Endurant™ Transmissions:

- Adjust “SmartCoast” to “Enabled” if set to “Disabled”. The Endurant transmission supports Smart Coast in accelerator control, cruise control, or cruise and accelerator control.

- For CM2450 (ECM calibration code starting with 'KW' located in Table 6 in the Existing ECM Calibration Code column) and CM2350 ECMs, Adjust “Load Based Torque Control” to “Smart Torque 2” if set to “Base”.
- Adjust “Predictive Gear Shifting” to “Enabled” if set to “Disabled”.
- Adjust “Predictive Engine Braking” to “Enabled” if it is set to “Disabled”.
- Adjust “On-ramp Boost” to “Enabled” if it is set to “Disabled”.
- Adjust “Road Speed Governor Type” from “Traditional” to “Predictive”. If Predictive Road Speed Governor is unavailable in the calibration, “Road Speed Governor Type” will be Read **Only**.
- Adjust “Hill Roll Out Enable” to “Enabled” if it is set to “Disabled”.

> [!note] Note · Примечание
> Predictive Gear Shifting, Predictive Engine Braking, On-ramp Boost, Dynamic Power, Predictive Road Speed Governor, and Hill Roll Out features are **only** applicable if the vehicle has a Connectivity Module, Cummins® Route Parameter Manager or OEM predictive cruise control system.

7. Set upper and lower cruise control droops to customer desired settings.

- Default settings are 3 miles per hour (mph) upper and 6 mph lower.
- The Cruise Control Lower Droop controls the range of cruise control based SmartCoast™. SmartCoast™ will **not** function with a 0 mph Cruise Control Lower Droop. Maximum fuel economy is achieved using 6 mph, and a minimum of 3 mph is recommended.

8. Set Road Speed Control maximum speed to customer desired settings.

- The RSG Maximum Vehicle Speed sets the maximum coasting speed for Accelerator Control operating mode. A minimum of 3 mph greater than maximum Accelerator Vehicle Speed is recommended.
- If the Maximum Vehicle Speed Control feature is used, the start braking speed will also set the maximum coasting speed. A start braking speed that is a minimum of 3 mph greater than Maximum Accelerator Speed is recommended.

9. Adjust the Predictive Road Speed Governor Maximum Positive and Maximum Negative Offsets to customer desired settings.

- Input both parameters as positive values.
- “Road Speed Governor Type” must be set to “Predictive” for the maximum offsets to be visible.

10. Adjust the Hill Roll Out Maximum Offset to customer desired settings.

- The recommended setting is a value that when added with Cruise Control Lower Droop, the resulting value is greater than 6 miles per hour (mph). If Maximum Vehicle Speed Control is enabled, the Hill Roll Out Maximum Offset will **not** exceed the Maximum Vehicle Speed Control Start Maximum Engine Braking Speed. Hill Roll Out Maximum Offset will be applied above the minimum of Maximum Vehicle Speed Control Start Minimum Engine Braking speed and Road Speed Governor Maximum Vehicle Speed when Hill Roll Out disengages the engine brake early.

11. If any fault codes or symptoms remain, reference the standard troubleshooting procedures. If Fault Code 5297 is active, review the transmission type and features in Table 5 above to determine what was incorrectly enabled.

| Table 6, Engine Control Module (ECM) Calibration Code |  |
|---|---|
| Existing ECM Calibration Code | ADEPT™ Technology ECM Calibration Code |
| EF10044 | EF10680 |
| EF10047 | EF10662 |
| EF10048 | EF10664 |
| EF10049 | EF10666 |
| EF10050 | EF10668 |
| EF10051 | EF10670 |
| EF10052 | EF10672 |
| EF10053 | EF10674 |
| EF10054 | EF10676 |
| EF10055 | EF10678 |
| EF10078 | EF10682 |
| EF10079 | EF10684 |
| EF10081 | EF10270 |
| EF10082 | EF10272 |
| EF10083 | EF10274 |
| EF10084 | EF10276 |
| EF10085 | EF10278 |
| EF10086 | EF10280 |
| EF10087 | EF10282 |
| EF10088 | EF10284 |
| EF10089 | EF10286 |
| EF10090 | EF10288 |
| EF10112 | EF10290 |
| EF10113 | EF10292 |
| EF10154 | EF10686 |
| EF10156 | EF10294 |
| EF10214 | EF10663 |
| EF10215 | EF10665 |
| EF10216 | EF10667 |
| EF10217 | EF10669 |
| EF10218 | EF10671 |
| EF10219 | EF10673 |
| EF10220 | EF10675 |
| EF10221 | EF10677 |
| EF10222 | EF10679 |
| EF10223 | EF10681 |
| EF10238 | EF10271 |
| EF10239 | EF10273 |
| EF10240 | EF10275 |
| EF10241 | EF10277 |
| EF10242 | EF10279 |
| EF10243 | EF10281 |
| EF10244 | EF10283 |
| EF10245 | EF10285 |
| EF10246 | EF10287 |
| EF10247 | EF10289 |
| EF10263 | EF10683 |
| EF10264 | EF10685 |
| EF10266 | EF10291 |
| EF10267 | EF10293 |
| EF10268 | EF10687 |
| EF10269 | EF10295 |
| EF10298 | EF10299 |
| EF10301 | EF10300 |
| EF10302 | EF10303 |
| EF10307 | EF10305 |
| EF10308 | EF10309 |
| EF10313 | EF10311 |
| EF10314 | EF10315 |
| EF10319 | EF10317 |
| EF10320 | EF10321 |
| EF10325 | EF10323 |
| EF10326 | EF10327 |
| EF10331 | EF10329 |
| EF10332 | EF10333 |
| EF10337 | EF10335 |
| EF10338 | EF10339 |
| EF10343 | EF10341 |
| EF10344 | EF10345 |
| EF10349 | EF10347 |
| EF10350 | EF10351 |
| EF10355 | EF10353 |
| EF10356 | EF10357 |
| EF10361 | EF10359 |
| EF10405 | EF10404 |
| EF10409 | EF10407 |
| EF10411 | EF10410 |
| EF10415 | EF10413 |
| EF10416 | EF10417 |
| EF10421 | EF10419 |
| EF10504 | EF10688 |
| EF10505 | EF10689 |
| EF10507 | EF10506 |
| EF10511 | EF10509 |
| EF10512 | EF10513 |
| EF10515 | EF10514 |
| EF10516 | EF10517 |
| EF10519 | EF10518 |
| EF10521 | EF10520 |
| EF10525 | EF10523 |
| EF10527 | EF10526 |
| EF10531 | EF10529 |
| EF10532 | EF10533 |
| EF10534 | EF10535 |
| EF10536 | EF10537 |
| EF10538 | EF10539 |
| EF10540 | EF10541 |
| EF10542 | EF10543 |
| EF10544 | EF10545 |
| EF10546 | EF10547 |
| EF10548 | EF10549 |
| EF10550 | EF10551 |
| EF10567 | EF10568 |
| EF10569 | EF10570 |
| EF10571 | EF10572 |
| EF10574 | EF10575 |
| EF10576 | EF10577 |
| EF10578 | EF10579 |
| EF10693 | EF10692 |
| EF10697 | EF10695 |
| EF10698 | EF10699 |
| EF10704 | EF10702 |
| EF10709 | EF10708 |
| EF10713 | EF10711 |
| EF10714 | EF10715 |
| EF10720 | EF10718 |
| EF10722 | EF10723 |
| EF10728 | EF10726 |
| EF10730 | EF10731 |
| EF10736 | EF10734 |
| EF10738 | EF10739 |
| EF10744 | EF10742 |
| EF10746 | EF10747 |
| EF10752 | EF10750 |
| EF10757 | EF10756 |
| EF10761 | EF10759 |
| HD10001 | HD10072 |
| HD10002 | HD10057 |
| HD10005 | HD10075 |
| HD10011 | HD10054 |
| HD10012 | HD10060 |
| HD10014 | HD10078 |
| HD10030 | HD10126 |
| HD10031 | HD10129 |
| HD10032 | HD10132 |
| HD10036 | HD10144 |
| HD10037 | HD10147 |
| HD10038 | HD10150 |
| HD10055 | HD10056 |
| HD10058 | HD10059 |
| HD10061 | HD10062 |
| HD10073 | HD10074 |
| HD10076 | HD10077 |
| HD10079 | HD10080 |
| HD10127 | HD10128 |
| HD10130 | HD10131 |
| HD10133 | HD10134 |
| HD10145 | HD10146 |
| HD10148 | HD10149 |
| HD10151 | HD10152 |
| HD10169 | HD10171 |
| HD10170 | HD10172 |
| HD10173 | HD10175 |
| HD10174 | HD10176 |
| HD10177 | HD10179 |
| HD10178 | HD10180 |
| HD10181 | HD10183 |
| HD10182 | HD10184 |
| HD10185 | HD10050 |
| HD10186 | HD10048 |
| HD10199 | HD10164 |
| HD10200 | HD10162 |
| HD10201 | HD10203 |
| HD10202 | HD10204 |
| HD10205 | HD10207 |
| HD10206 | HD10208 |
| HD10209 | HD10210 |
| HD10211 | HD10212 |
| HD10213 | HD10214 |
| HD10215 | HD10216 |
| HD10217 | HD10089 |
| HD10218 | HD10087 |
| HD10221 | HD10222 |
| HD10223 | HD10224 |
| HD10225 | HD10226 |
| HD10227 | HD10228 |
| HD10229 | HD10230 |
| HD10231 | HD10232 |
| HD10233 | HD10234 |
| HD10235 | HD10236 |
| HD10237 | HD10238 |
| HD10239 | HD10240 |
| HD10241 | HD10242 |
| HD10243 | HD10244 |
| HD10247 | HD10246 |
| HD10248 | HD10245 |
| HD10251 | HD10250 |
| HD10252 | HD10249 |
| HD10279 | HD10280 |
| HD10281 | HD10282 |
| HD10283 | HD10284 |
| HD10285 | HD10286 |
| HD10287 | HD10288 |
| HD10289 | HD10290 |
| HD10291 | HD10292 |
| HD10293 | HD10294 |
| HD10295 | HD10296 |
| HD10297 | HD10298 |
| HD10299 | HD10300 |
| HD10301 | HD10302 |
| HD10305 | HD10304 |
| HD10306 | HD10303 |
| HD10331 | HD10332 |
| HD10333 | HD10334 |
| HD10335 | HD10336 |
| HD10337 | HD10338 |
| HD10343 | HD10344 |
| HD10345 | HD10346 |
| HD10347 | HD10348 |
| HD10349 | HD10350 |
| HD10351 | HD10352 |
| HD10353 | HD10354 |
| HD10355 | HD10356 |
| HD10357 | HD10358 |
| HD10359 | HD10360 |
| HD10361 | HD10362 |
| HD10363 | HD10364 |
| HD10365 | HD10366 |
| HD10369 | HD10368 |
| HD10370 | HD10367 |
| HD10373 | HD10372 |
| HD10374 | HD10371 |
| HD10401 | HD10402 |
| HD10403 | HD10404 |
| HD10405 | HD10406 |
| HD10407 | HD10408 |
| HD10409 | HD10410 |
| HD10411 | HD10412 |
| HD10413 | HD10414 |
| HD10415 | HD10416 |
| HD10417 | HD10418 |
| HD10419 | HD10420 |
| HD10421 | HD10422 |
| HD10423 | HD10424 |
| HD10427 | HD10426 |
| HD10428 | HD10425 |
| HD10441 | HD10442 |
| HD10443 | HD10444 |
| HD10445 | HD10446 |
| HD10447 | HD10448 |
| KW10001 | KW10062 |
| KW10002 | KW10063 |
| KW10009 | KW10047 |
| KW10010 | KW10048 |
| KW10010 | KW10049 – required for 40K Axle |
| KW10011 | KW10050 |
| KW10012 | KW10051 |
| KW10012 | KW10052– required for 40K Axle |
| KW10013 | KW10053 |
| KW10014 | KW10054 |
| KW10014 | KW10055– required for 40K Axle |
| KW10017 | KW10056 |
| KW10018 | KW10057 |
| KW10021 | KW10056 |
| KW10022 | KW10058– required for 40K Axle |
| KW10023 | KW10059 |
| KW10024 | KW10060 |
| KW10025 | KW10059 |
| KW10026 | KW10061– required for 40K Axle |
| KW10029 | KW10062 |
| KW10030 | KW10064– required for 40K Axle |
| KW10033 | KW10128 |
| KW10034 | KW10129 |
| KW10093 | KW10097 |
| KW10094 | KW10098 |
| KW10094 | KW10099– required for 40K Axle |
| KW10095 | KW10100 |
| KW10096 | KW10101 |
| KW10096 | KW10102– required for 40K Axle |
| KW10108 | KW10118 |
| KW10109 | KW10119 |
| KW10110 | KW10121 |
| KW10111 | KW10122 |
| KW10114 | KW10118 |
| KW10115 | KW10120– required for 40K Axle |
| KW10116 | KW10121 |
| KW10117 | KW10123– required for 40K Axle |
| KW10126 | KW10128 |
| KW10127 | KW10130– required for 40K Axle |
| KW10161 | KW10103 |
| KW10162 | KW10104 |
| KW10162 | KW10105– required for 40K Axle |

### Document History
