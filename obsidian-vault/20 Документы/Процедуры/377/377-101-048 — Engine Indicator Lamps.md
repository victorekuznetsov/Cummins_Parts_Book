---
type: "Процедура"
doc: "377-101-048"
title_en: "Engine Indicator Lamps"
modified: "2026-05-21"
manuals:
  - "5411182"
  - "5411183"
figures: 13
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-101-048.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-101-048.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Engine Indicator Lamps

> [!abstract] Процедура · `377-101-048`
> **Входит в руководства:** [[5411182 — X15 CM2350 X114B - Efficiency Series Operation and Maintenance Manual|5411182]], [[5411183 — X15 CM2350 X114B - Efficiency Series and X15 CM2350 X116B - Performance Series Owners|5411183]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2026-05-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-101-048.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-101-048.pdf)

### General Information

Overview

The following engine indicator lamps cover **only** the lamps controlled by the engine control module (ECM). The vehicle manufacturer can provide additional indicator lamps. Reference the vehicle owners manual for additional lamp information.

- Check engine
- Aftertreatment diesel particulate filter (DPF)
- Stop engine
- Aftertreatment diesel exhaust fluid (DEF)
- Exhaust high temperature.

Engine Operation

#### Malfunction Indicator Lamp (MIL)

- Cummins® Environmental Protection Agency (EPA) 2017 heavy duty on-highway engines are equipped with On-Board Diagnostics (OBD). The OBD system monitors and reports malfunctions that impact the emissions control devices. If the OBD system detects such a malfunction, the OBD system illuminates the MIL. Service **must** be scheduled at earliest convenience. Vehicle may still be operated until scheduled service.

> [!note] Note · Примечание
> The MIL is **only** used on OBD certified products.

The MIL is amber, and can look like:

- A symbol of an engine, similar to the illustration.
- A symbol of exhaust flow featuring an exclamation point, similar to the illustration.

The MIL can be illuminated along with any of the engine indicator lamps. It is **not** used to indicate an engine protection or maintenance required condition.

![[00c00178.png]]

Check Engine Lamp

The CHECK ENGINE lamp illuminates to indicate the driver must arrange for service soon. Vehicle may still be operated until the end of shift.

The CHECK ENGINE lamp is amber, and can look like:

- The words WARNING or CHECK ENGINE spelled out
- A symbol of an engine, similar to the illustration.

![[00c00181.png]]

Engine Maintenance Lamp

Another function of the CHECK ENGINE lamp is to flash for 30 seconds at key ON to indicate a maintenance condition. This flashing function is referred to as the MAINTENANCE lamp. The MAINTENANCE lamp could flash for the following reasons:

- Maintenance required, if the Maintenance Monitor feature is enabled
- Water in fuel detected
- Coolant level low
- DEF tank level low
- Fuel filter restricted
- Aftertreatment regeneration inhibit switch activated and preventing regeneration
- Maintenance of the crankcase breather element required, if enabled in the calibration
- Maintenance of the aftertreatment DPF require, if enabled in calibration.

The lamp will turn off if no other condition exists.

![[19t00137.png]]

Stop Engine Lamp

The STOP ENGINE lamp indicates, when illuminated, the need to stop the engine as soon as it can be safely done. The engine **must** remain shut down until the engine can be repaired.

For engines with the Engine Protection Shutdown feature enabled, if the STOP ENGINE lamp begins to flash, the engine will automatically shut down after 30 seconds. The flashing STOP engine lamp alerts the operator to the impending shutdown.

The STOP ENGINE lamp is red in color, and can look like:

- The words STOP or STOP ENGINE
- A symbol of an engine with an exclamation point in the center, similar to the illustration.
- A symbol of a stop sign with an engine outline in the center, similar to the illustration.

![[00c00179.png]]

Aftertreatment Diesel Particulate Filter Lamp

The AFTERTREATMENT DIESEL PARTICULATE FILTER lamp indicates, when illuminated or flashing, that the aftertreatment DPF requires regeneration.

An illuminated AFTERTREATMENT DIESEL PARTICULATE FILTER lamp indicates that the aftertreatment DPF needs to be regenerated at the next possible opportunity. This can be accomplished by:

- Changing the duty cycle by increasing the engine parasitics, including activating the vehicle's driving lights and head lights, activating the engine fan, if dash switch equipped, activating the air conditioner or defroster, driving and maintaining a road speed of 50 mph or greater until the AFTERTREATMENT DIESEL PARTICULATE FILTER lamp deactivates. Continue driving for an additional 20 minutes to provide for adequate aftertreatment DPF regeneration.
- Performing a stationary regeneration. Follow the instructions in Unique Operating Characteristics of an Engine with Aftertreatment, in Section 1.

> [!note] Note · Примечание
> Stationary regeneration is considered a normal maintenance practice and is **not** covered by Cummins Inc. warranty.

![[11c00108.png]]

A flashing AFTERTREATMENT DIESEL PARTICULATE FILTER lamp indicates that the aftertreatment diesel particulate filter needs to be regenerated at the next possible opportunity. Engine power may be reduced automatically.

When this lamp is flashing, the operator should:

- Change the duty cycle by increasing the engine parasitics, including activating the vehicle's driving and head lights, activating the engine fan, if dash switch equipped, activating the air conditioner or defroster, driving and maintaining a road speed of 50 mph or greater until the AFTERTREATMENT DIESEL PARTICULATE FILTER lamp deactivates. Continue driving for an additional 20 minutes to provide for adequate DPF regeneration.
- Performing a stationary regeneration. Follow the instructions in Unique Operating Characteristics of an Engine with Aftertreatment, in Section 1.

> [!note] Note · Примечание
> Stationary regeneration is considered a normal maintenance practice and is **not** covered by Cummins Inc. warranty.

![[00c00180.png]]

A flashing AFTERTREATMENT DIESEL PARTICULATE FILTER lamp combined with an illuminated WARNING or CHECK ENGINE lamp indicates that the aftertreatment DPF needs be regenerated immediately. Engine power will be reduced automatically.

When these lamps are illuminated, a stationary regeneration is required.

- Follow the instructions in Unique Operating Characteristics of an Engine with Aftertreatment, in Section 1.

> [!note] Note · Примечание
> If a stationary regeneration is **not** performed, the STOP ENGINE lamp will illuminate and the vehicle will need to be taken to a Cummins® Authorized Repair Location.

> [!note] Note · Примечание
> Stationary regeneration is considered a normal maintenance practice and is **not** covered by Cummins Inc. warranty.

![[00c00182.png]]

High Exhaust System Temperature Lamp

> [!danger] WARNING · Опасно
> When this lamp is illuminated, the exhaust gas temperature could reach 800°C \[1500°F\], which is hot enough to ignite or melt common materials, and to burn people.

The HIGH EXHAUST SYSTEM TEMPERATURE lamp indicates, when illuminated, that exhaust temperatures are high due to regeneration of the aftertreatment DPF. This lamp can illuminate during normal engine operation or during stationary regeneration.

> [!note] Note · Примечание
> The equipment manufacturer service information determines whether or **not** the HIGH EXHAUST SYSTEM TEMPERATURE lamp is installed on the vehicle. The equipment manufacturer service information also specifies the temperatures, vehicle speeds, and other conditions at which the lamp illuminates. Reference the equipment manufacturer service information for additional information regarding this lamp.

When this lamp is illuminated, make sure that the exhaust pipe outlet is **not** directed at any surface or material that can melt, burn, or explode.

- Keep the exhaust outlet away from people and anything that can melt, burn, or explode.
- Nothing within 0.6 m \[2 ft\] of the exhaust outlet
- Nothing that can melt, burn, or explode within 1.5 m \[5 ft \], such as gasoline, wood, paper, plastics, fabric, compressed gas containers, and hydraulic lines.
- In an emergency, turn the engine OFF to stop the flow of exhaust.

> [!note] Note · Примечание
> The HIGH EXHAUST SYSTEM TEMPERATURE lamp does **not** signify the need for any kind of vehicle or engine service; it merely alerts the vehicle operator to high exhaust temperatures. It will be common for the HIGH EXHAUST SYSTEM TEMPERATURE lamp to illuminate on and off during normal vehicle operation as the engine completes regeneration.

![[11c00107.png]]

Aftertreatment Diesel Exhaust Fluid Lamp

The DIESEL EXHAUST FLUID lamp indicates, when illuminated or flashing, that the DEF level is low.

An illuminated DIESEL EXHAUST FLUID lamp indicates that the DEF level has fallen below the initial warning level. This can be corrected by filling the DEF tank with DEF.

![[00c00200.png]]

A flashing DIESEL EXHAUST FLUID lamp indicates that the DEF level has fallen below the critical warning level. The engine power will have a mild derate. This can be corrected by filling the DEF tank with DEF.

Other events that can cause the flashing DIESEL EXHAUST FLUID lamp are incorrect DEF type or tampering of the SCR system have been detected for more than one hour. The engine power will have a mild derate.

> [!note] Note · Примечание
> It is recommended that the DEF tank be filled completely full of DEF in order to correct any fault conditions.

![[00c00185.png]]

An illuminated or flashing DIESEL EXHAUST FLUID lamp combined with an illuminated WARNING or CHECK ENGINE lamp indicates that the DEF level has fallen below the initial derate level. The engine power will be limited automatically. This can be corrected by filling the DEF tank with DEF.

Other events that can cause an illuminated or flashing DIESEL EXHAUST FLUID lamp combined with an illuminated WARNING or CHECK ENGINE lamp are incorrect DEF type or tampering has been detected for more than five hours.

> [!note] Note · Примечание
> It is recommended that the DEF tank be filled completely full of DEF in order to correct any fault conditions.

![[00c00203.png]]

Allowing the DEF tank to become empty will cause the aftertreatment DEF dosing system to lose prime. A loss of prime condition may cause fault codes to become active.

> [!note] Note · Примечание
> On OBD certified products, the MIL may become illuminated for a loss of prime condition.

> [!note] Note · Примечание
> It is recommended that the DEF tank be filled completely full of DEF in order to correct any fault conditions.

![[00c00203.png]]

If the engine has been shut down or has idled for an extended period of time after the tank has been emptied, the STOP ENGINE lamp will also be illuminated along with the flashing DIESEL EXHAUST FLUID lamp and illuminated CHECK ENGINE lamp. The engine power will continue to be limited automatically. The vehicle speed will also be limited.

> [!note] Note · Примечание
> Some emergency vehicles may perform differently from the description above.

The DEF tank **must** be filled to at least 10 percent volume of the tank in order to remove the speed limit.

It is recommended that the DEF tank be filled completely full of DEF in order to correct any fault conditions.

> [!note] Note · Примечание
> On OBD certified products, the MIL may also be illuminated.

![[00c00184.png]]

Battery Power Required Lamp

The ECM requires that battery power be constantly connected anytime the keyswitch is in the ON position and for some time after the keyswitch is turned to the OFF position. The ECM will turn the BATTERY POWER REQUIRED lamp on when the keyswitch is ON, and for the entire duration that the battery is required after the keyswitch is turned OFF. Reference the equipment manufacturer service information for details on lamp configuration.
