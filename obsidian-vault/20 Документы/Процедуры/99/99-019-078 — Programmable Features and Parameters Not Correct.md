---
aliases:
  - "Программируемые функции и параметры заданы неверно"
type: "Процедура"
doc: "99-019-078"
title_en: "Programmable Features and Parameters Not Correct"
title_ru: "Программируемые функции и параметры заданы неверно"
modified: "2020-02-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-078.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-078.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Programmable Features and Parameters Not Correct
**Программируемые функции и параметры заданы неверно**

> [!abstract] Процедура · `99-019-078`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2020-02-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-078.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-078.pdf)

### General Information

This procedure was developed due to the increasing number of parameters and features offered which can affect vehicle performance. Use the following table to troubleshoot performance complaints by locating the appropriate symptom in the left column. Then follow the probable cause and corrective action in the adjacent columns.

Adjust the features or parameters with the recommended Cummins® electronic service tool or equivalent.

![[19803969.png]]

### Adjust

| Programmable Feature/Parameters Not Correct |  |  |
|---|---|---|
| Symptom | Probable Cause | Correction |
| Exceeding road speed governor set speed down hills | Cruise control or road speed governor lower droop is set too high. | Change the cruise control or road speed governor lower droop to a lower value. If the problem continues, change the cruise control engine brake activation to a lower value. |
| Poor acceleration up hills | Cruise control and/or road speed governor upper droop is set too high. | Change the cruise control or road speed governor upper droop to a lower value. |
| Cruise control turns on automatically. | Cruise control auto-resume feature is enabled. | Turn off the cruise control auto-resume feature. |
| Exhaust brakes turn on automatically. | Cruise control auto engine brake feature is enabled or exhaust brake switch is failed. | Turn off the cruise control auto engine brake feature or repair the switch. |
| Unable to obtain maximum vehicle speed. | Gear-down protection feature is enabled. | Turn off or adjust the gear-down protection parameters. |
| Poor clutch engagement | The low idle speed is set too low for the application. | Increase the low-idle speed using the idle adjust switch. [[99-019-052 — Idle Adjust Switch\|Refer to Procedure 019-052]]. Increase the low-idle speed parameter. |
| Speedometer on the dashboard is **not** correct or vehicle exceeding road speed governor set speed. | Vehicle speed parameters are **not** set properly. | Make sure the following are correct: tire size, rear axle ratio, vehicle speed sensor type, and gear teeth per revolution. |
| Trip information mileage readings are **not** correct. | The tire size parameter was changed without resetting the trip information system. | Set the trip information system again whenever the tire size parameter is changed. |
| Can **not** obtain maximum vehicle speed with semiautomatic transmission. | The gear-down protection parameters are **not** set properly. | Change the top gear ratio parameter to be equal to the first gear-down ratio, **not** the top gear ratio. For example, on a transmission with a 0.75, 0.87, and 1.0 ratio set, the top gear ratio parameter **must** be set to 0.87. |
| Engine won't start. | Antitheft password is active. | Enter antitheft personal identification number (PIN) using RoadRelay™ or delete password with Zap-It. |
| Low power in lower gears or top gear | Power train protection parameters are set too low. | Change power train protection torque limits to match torque capability of the vehicle's transmission. |
| Semiautomatic transmission will **not** shift into top gear. | Top gear ratio setting does **not** match top gear of transmission. | Set the proper top gear ratio. |
| Centinel™ feature has been turned on but vehicle has a Spicer Top 2™ transmission. | Feature and parameters are **not** set properly. | Turn off the Centinel™ feature and turn on the Top 2 feature. |
| Engine recently started overheating because the fan will **not** turn on. | Fan control feature is **not** set properly. | Verify all fan control feature parameters are properly set for the vehicle. |
| Fan will **not** turn off. | Fan control feature is **not** set properly. | Verify all fan control feature parameters are properly set for the vehicle. |
| Fan control switch will **not** turn on the fan. | Fan control 1 accessory switch control is turned off. | Turn on fan control 1 accessory switch control. |
| Unable to obtain maximum vehicle speed. | Cruise control maximum vehicle speed or accelerator maximum vehicle speed is **not** set high enough. | Verify or change settings. |
| Driver reward system is penalizing the driver with reduced top vehicle speed or cruise control maximum speed for poor fuel economy or extended idle time. | Driver is unfamiliar with feature or feature and parameters are **not** set properly. | Explain feature to the driver or change parameter settings to more appropriate values. |
| Accelerator pedal has no effect on engine speed. | Vehicle is in PTO mode and PTO accelerator override is turned on in the ECM. | Turn off PTO accelerator override. |
| Accelerator pedal has no effect on engine speed. | Vehicle has a multiplexed throttle pedal and the multiplexing feature is turned off. | Verify that the throttle pedal is multiplexed. Turn on the multiplexing feature for the throttle pedal. |
| Remote accelerator control has no effect on engine speed. | Remote accelerator feature is turned off. | Turn on the remote accelerator feature. |
| Remote accelerator control has no effect on engine speed. | Vehicle has a multiplexed remote accelerator control and the multiplexing feature is turned off. | Verify that the remote accelerator control is multiplexed. Turn on the multiplexing feature for the remote throttle control. |
| Lamps do **not** operate. | Fuse is failed. | Check fuses and verify the ECM is getting power on the keyswitch wire. |
| Lamps do **not** operate. | Vehicle has multiplexed lamps and the multiplexing feature is turned off. | Verify that the lamps are multiplexed. Turn on the multiplexing feature for the lamps. |
| Engine brakes do **not** operate. | Vehicle has multiplexed engine brake switches and the multiplexing feature is turned off. | Verify that the engine brake switches are multiplexed. Turn on the multiplexing feature for the engine brake switches. |
| Engine will **not** respond to one or all of the operator's switch(es). | Vehicle has multiplexed switches and the multiplexing feature is turned off. | Verify that the switches are multiplexed. Turn on the multiplexing feature for the switches. |
