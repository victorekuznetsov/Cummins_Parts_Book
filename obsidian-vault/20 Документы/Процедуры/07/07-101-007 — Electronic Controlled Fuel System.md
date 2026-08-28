---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "07-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2003-12-01"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 20
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `07-101-007`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-12-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-101-007.pdf)

### Fault Lamp Sequencing

General Information

The ENGINE FAULT AND MAINTENANCE lamps are illuminated when the keyswitch is turned to the ON position.

After 2 seconds, the red STOP ENGINE lamp will turn off. After an additional ½ of a second, the amber CHECK ENGINE lamp will turn off. After an additional ½ of a second, the amber ENGINE MAINT lamp will turn off.

The lamps will remain off until a fault is detected.

> [!note] Note · Примечание
> This is a self-test feature of the lamp wiring and lamps.

> [!note] Note · Примечание
> The names and colors of the lamps can vary with vessel manufacturer if non-Cummins panels are used.

![[15200041.png]]

Engine Fault and Maintenance System Familiarization

The following chart summarizes the different lamps and their operation.

| Feature | Operator Message | Lamp Operation |  |  |
|---|---|---|---|---|
| Check Engine | Stop Engine | Engine Maint. |  |  |
| Lamp Display | Power-up lamp test | On then off | On then off | On then off |
| Diagnostics | Fault code flash-out | Flash once/code | Flash code number |  |
| Engine Protection | System problem |  | Slow flash |  |
| Maintenance Monitor | Interval expired |  |  | 3x5 fast flash |
| Maintenance Monitor | Interval rest |  |  | 3x5 fast flash |
| Diagnostics | Nonfatal system error | On steady |  |  |
| Diagnostics | Fatal system error |  | On steady |  |
| Diagnostics | Maintenance required |  |  | On steady |

If the STOP or CHECK ENG lamp comes on when the engine is running, it means a fault code has been recorded. The lamp will remain on as long as the fault exists. The severity of the fault will determine which lamp is illuminated.

### Diagnostic Fault Codes

Stop Engine Lamp

The STOP ENGINE lamp is a red lamp. This lamp indicates that the engine needs to be shut down before permanent damage occurs to the engine.

> [!note] Note · Примечание
> The engine **must** be shut off as soon as it can be shut off safely. The engine **must not** be run until the fault is corrected.

This lamp is also used to flash out the fault code number in the diagnostics mode.

![[15200042.png]]

Check Engine Lamp

The CHECK ENGINE lamp comes on during a nonfatal system error. The engine can still be run, but the fault **must** be corrected as soon as possible.

> [!note] Note · Примечание
> In the diagnostics mode, the CHECK ENGINE lamp completes the three-digit fault code.

![[15200043.png]]

Engine Maintenance Lamp

The ENGINE MAINT lamp comes on when engine maintenance is required.

![[15200044.png]]

Wait to Start Lamp

The WAIT TO START lamp is **only** used on engines with an intake air heater system such as C Series engines.

![[15200051.png]]

Engine Diagnostics

When a fault or maintenance lamp is lit, the engine diagnostics switch allows the operator to view the fault codes. The receptacle to the right of the switch is for the technician's computer connection, using either INSITE™ or Echek™ service tool.

Active fault codes can be viewed using the stop engine warning lamp as described below.

![[13200054.png]]

To view the fault codes:

1. The engine **must** be shut off (**not** running).
2. The keyswitch **must** be in the ON position.
3. The ENG DIAG switch (1) **must** be in the ON position.

![[15200045.png]]

The CHECK ENGINE and STOP ENGINE lamps flash if there are any fault codes to display.

If there are no fault codes to display, the CHECK ENGINE and STOP ENGINE lamps will remain lit.

![[15200046.png]]

If there are fault codes to be displayed, the check engine lamp will flash momentarily. Then the stop engine lamp will flash the first, second, and third digits of the fault code.

Example:

Fault Code 432

4 flashes, pause

3 flashes, pause

2 flashes

> [!note] Note · Примечание
> The check engine lamp will flash between each fault code.

The pattern repeats itself until the fault is cleared or the switch is turned off.

![[15200047.png]]

To view the next fault code, press the RPM ± switch (4) in the plus (+) direction.

To view the previous fault code, press the RPM ± switch (4) in the minus (-) direction.

![[15200048.png]]

The audible alarm (8) sounds anytime the warning or caution symbols are illuminated.

![[13200066.png]]

The alarm silence button (6) will temporarily silence the audible alarm.

> [!note] Note · Примечание
> The alarm will be silenced for up to 2 minutes. As long as the fault condition exists, the alarm will “chirp” every 2 minutes to remind the operator that a fault exists.

![[13200066.png]]

The alarm silence button (6) is also used to test the warning and caution symbol lamps (1) and the gauges.

To test the gauges and symbol lamps, press the alarm silence button (6) while turning on the keyswitch. The alarm will come on for 5 seconds and for 25 seconds all symbols will illuminate and the gauge needles will move from the lowest position to the highest position and back to the lowest position.

> [!note] Note · Примечание
> The voltmeter will **not** display a system test.

![[13200066.png]]

### Engine Monitoring System

General Information

The indicator symbols (1) provide additional information on the type of fault that the ECM has detected. The individual symbols will flash during a fault condition.

> [!note] Note · Примечание
> Pressing the alarm cancel button (6) when the keyswitch is turned on will illuminate the symbols for a self-test.

![[13200088.png]]

Low Engine Oil Pressure

The low engine oil pressure lamp (7) comes on when the engine oil pressure is below specification. Refer to Section V of the operation and maintenance manual for the oil pressure specifications.

![[13200079.png]]

High Intake Manifold Temperature

The high intake manifold temperature lamp (1) comes on when the intake manifold temperature is above specification.

![[13200073.png]]

Water in Fuel

The water-in-fuel lamp (3) interfaces with the optional water-in-fuel sensor in the primary fuel filter. It comes on when there is water in the fuel filter. This feature is **not** presently available.

![[13200075.png]]

High Coolant Temperature

The high coolant temperature lamp (4) comes on when the engine coolant temperature is above specification.

![[13200076.png]]

Low Battery Voltage

> [!note] Note · Примечание
> This voltage lamp **only** applies to marine applications.

The low battery voltage lamp (6) comes on when the battery voltage is below specification.

![[13200078.png]]

### Circuit Breakers

The electronically controlled marine engine is equipped with two circuit breakers located on the ECM side of the engine.

A 5-amp circuit breaker (1) is used for keyswitched power to the ECM and a 10-amp circuit breaker (2) is used for non-keyswitched power to the panel. The circuit breaker panel also houses a 40-pin OEM connector (3).

![[13200057.png]]
