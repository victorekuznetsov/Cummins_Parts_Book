---
type: "Процедура"
doc: "101-101-048"
title_en: "Engine Indicator Lamps"
modified: "2009-09-24"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666251"
  - "4960314"
figures: 13
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-101-048.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-101-048.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/101"
---

# Engine Indicator Lamps

> [!abstract] Процедура · `101-101-048`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666251 — Signature and ISX Operation and Maintenance Manual|3666251]], [[4960314 — ISX Owners Manual|4960314]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2009-09-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-101-048.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-101-048.pdf)

### General Information

The following engine indicator lamps cover **only** the lamps controlled by the engine's ECM. The vehicle manufacturer can provide additional indicator lamps. Please refer to the vehicle's owners manual for additional lamp information.

1. Check engine
2. Check engine
3. Aftertreatment diesel particulate filter
4. Stop engine
5. Aftertreatment diesel exhaust fluid
6. Exhaust high temperature

![[ck800wa.png]]

Engine Operation

#### Malfunction Indicator Lamp (MIL)

- For ISX15 CM2250 engines equipped with On Board Diagnostics (OBD), the emissions control system monitors and reports malfunctions that could cause an increase in exhaust emissions levels. If the OBD system detects such a malfunction, the on-board diagnostic system illuminates the MALFUNCTION INDICATOR LAMP (MIL) to indicate that the engine needs to be serviced at the first available opportunity.

> [!note] Note · Примечание
> **The MALFUNCTION INDICATOR LAMP (MIL) is only used on on-board diagnostic certified products**.

The MALFUNCTION INDICATOR LAMP (MIL) is amber, and can look like:

- A symbol of an engine, similar to the illustration.
- A symbol of exhaust flow featuring an exclamation point, similar to the illustration.

The MALFUNCTION INDICATOR LAMP (MIL) can be illuminated along with any of the engine indicator lamps. It is not used to indicate an engine protection or maintenance required condition.

![[00c00178.png]]

Check Engine Lamp

The CHECK ENGINE lamp illuminates when the engine needs to be serviced at the first available opportunity.

The CHECK ENGINE lamp is amber, and can look like:

- The words WARNING or CHECK ENGINE spelled out
- A symbol of an engine, similar to the illustration.

Another function of the CHECK ENGINE lamp is to flash for 30 seconds at key ON to indicate a maintenance condition. This flashing function is referred to as the MAINTENANCE lamp. The MAINTENANCE lamp could flash for and of the following reasons:

- Maintenance required (if the Maintenance Monitor is enabled)
- Water-in-fuel is detected
- Coolant level is low.

![[00c00181.png]]

Stop Engine Lamp

The STOP ENGINE lamp indicates, when illuminated, the need to stop the engine as soon as it can be safely done. The engine **must** remain shut down until the engine can be repaired.

For engines with the Engine Protection Shutdown feature enabled, if the STOP ENGINE lamp begins to flash, the engine will automatically shut down after 30 seconds. The flashing STOP engine lamp alerts the operator to the impending shutdown.

The STOP ENGINE lamp is red in color, and can look like:

- The words STOP or STOP ENGINE spelled out
- A symbol of an engine with an exclamation point in the center, similar to the illustration.
- A symbol of a stop sign with an engine outline in the center, similar to the illustration

![[00c00179.png]]

Aftertreatment Diesel Particulate Filter Lamp

The AFTERTREATMENT DIESEL PARTICULATE FILTER lamp indicates, when illuminated or flashing, that the aftertreatment diesel particulate filter requires regeneration.

An illuminated AFTERTREATMENT DIESEL PARTICULATE FILTER lamp indicates that the aftertreatment diesel particulate filter needs to be regenerated at the next possible opportunity. This can be accomplished by:

- Changing the duty cycle by increasing the engine parasitics, including activating the vehicle's driving lights and head lights, activating the engine fan (if dash switch equipped),activating the air conditioner (or defroster), driving and maintaining a road speed of 50 mph or greater until the AFTERTREATMENT DIESEL PARTICULATE FILTER lamp deactivates. Continue driving for an additional 20 minutes to provide for adequate aftertreatment diesel particulate filter regeneration.
- Performing a stationary regeneration. Follow the instructions in Unique Operating Characteristics of an Engine with Aftertreatment, in Section 1.

> [!note] Note · Примечание
> Stationary regeneration is considered a normal maintenance practice and is **not** covered by Cummins Inc. warranty.

![[11c00108.png]]

A flashing AFTERTREATMENT DIESEL PARTICULATE FILTER lamp indicates that the aftertreatment diesel particulate filter needs to be regenerated at the next possible opportunity. Engine power may be reduced automatically.

When this lamp is flashing, the operator should:

- Change the duty cycle by increasing the engine parasitics, including activating the vehicle's driving and head lights,activating the engine fan (if dash switch equipped), activating the air conditioner (or defroster), driving and maintaining a road speed of 50 mph or greater until the AFTERTREATMENT DIESEL PARTICULATE FILTER lamp deactivates. Continue driving for an additional 20 minutes to provide for adequate diesel particulate filter regeneration.
- Perform a stationary regeneration. Follow the instructions in Unique Operating Characteristics of an Engine with Aftertreatment, in Section 1.

> [!note] Note · Примечание
> Stationary regeneration is considered a normal maintenance practice and is **not** covered by Cummins Inc. warranty.

![[00c00180.png]]

A flashing AFTERTREATMENT DIESEL PARTICULATE FILTER lamp combined with an illuminated WARNING or CHECK ENGINE lamp indicates that the aftertreatment diesel particulate filter needs be regenerated immediately. Engine power will be reduced automatically.

When these lamps are illuminated, a stationary regeneration is required.

- Follow the instructions in Unique Operating Characteristics of an Engine with Aftertreatment, in Section 1.

> [!note] Note · Примечание
> If a stationary regeneration is **not** performed, the STOP ENGINE lamp will illuminate and the vehicle will need to be taken to a Cummins® Authorized Repair Location.

> [!note] Note · Примечание
> Stationary regeneration is considered a normal maintenance practice and is **not** covered by Cummins Inc. warranty.

![[00c00182.png]]

High Exhaust System Temperature Lamp

The HIGH EXHAUST SYSTEM TEMPERATURE lamp indicates, when illuminated, that exhaust temperatures are high due to regeneration of the aftertreatment diesel particulate filter. This lamp can illuminate during normal engine operation or during stationary regeneration.

> [!note] Note · Примечание
> The OEM determines whether or **not** the HIGH EXHAUST SYSTEM TEMPERATURE lamp is installed on the vehicle. The OEM also specifies the temperatures, vehicle speeds, and other conditions at which the lamp illuminates. Refer to the OEM service manual for additional information regarding this lamp.

When this lamp is illuminated, make sure that the exhaust pipe outlet is **not** directed at any surface or material that can melt, burn, or explode.

> [!danger] WARNING · Опасно
> When this lamp is illuminated, the exhaust gas temperature could reach 800°C \[1500°F\], which is hot enough to ignite or melt common materials, and to burn people.

- Keep the exhaust outlet away from people and anything that can burn, melt, or explode.
- Nothing within 0.6 m \[2 ft\] of the exhaust outlet
- Nothing that can burn, melt, or explode within 1.5 m \[5 ft \] (such as gasoline, wood, paper, plastics, fabric, compressed gas containers, and hydraulic lines).
- In an emergency, turn off the engine to stop the flow of exhaust.

> [!note] Note · Примечание
> The HIGH EXHAUST SYSTEM TEMPERATURE lamp does **not** signify the need for any kind of vehicle or engine service; it merely alerts the vehicle operator to high exhaust temperatures. It will be common for the HIGH EXHAUST SYSTEM TEMPERATURE lamp to illuminate on and off during normal vehicle operation as the engine completes regeneration.

![[11c00107.png]]

Aftertreatment Diesel Exhaust Fluid Lamp

The DIESEL EXHAUST FLUID lamp indicates, when illuminated or flashing, that the diesel exhaust fluid level is low.

An illuminated DIESEL EXHAUST FLUID lamp indicates that the diesel exhaust fluid level has fallen below the initial warning level. This can be corrected by filling the diesel exhaust fluid tank with diesel exhaust fluid.

> [!note] Note · Примечание
> It is recommended that the diesel exhaust fluid tank be filled completely full of diesel exhaust fluid in order to correct any fault conditions.

![[00c00200.png]]

A flashing DIESEL EXHAUST FLUID lamp indicates that the diesel exhaust fluid level has fallen below the critical warning level. This can be corrected by filling the diesel exhaust fluid tank with diesel exhaust fluid.

> [!note] Note · Примечание
> It is recommended that the diesel exhaust fluid tank be filled completely full of diesel exhaust fluid in order to correct any fault conditions.

![[00c00185.png]]

A flashing DIESEL EXHAUST FLUID lamp combined with an illuminated WARNING or CHECK ENGINE lamp indicates that the diesel exhaust fluid level has fallen below the initial derate level. The engine power will be limited automatically. This can be corrected by filling the diesel exhaust fluid tank with diesel exhaust fluid.

> [!note] Note · Примечание
> It is recommended that the diesel exhaust fluid tank be filled completely full of diesel exhaust fluid in order to correct any fault conditions.

![[00c00203.png]]

Allowing the diesel exhaust fluid tank to become empty will cause the aftertreatment diesel exhaust fluid dosing system to lose prime. A loss of prime condition may cause fault codes to become active.

> [!note] Note · Примечание
> On on-board diagnostic certified products, the MIL may become illuminated for a loss of prime condition.

> [!note] Note · Примечание
> It is recommended that the diesel exhaust fluid tank be filled completely full of diesel exhaust fluid in order to correct any fault conditions.

![[00c00203.png]]

If the engine has been shut down or has idled for 20 hours after the tank has been emptied, the STOP ENGINE lamp will also be illuminated along with the flashing DIESEL EXHAUST FLUID lamp and illuminated CHECK ENGINE lamp. The engine power will continue to be limited automatically. The vehicle will also be limited to a 5 Mile per Hour (MPH) speed limit.

> [!note] Note · Примечание
> In order to remove the 5 MPH speed limit, the diesel exhaust fluid tank must be filled to at least 10 percent volume of the tank.

> [!note] Note · Примечание
> It is recommended that the diesel exhaust fluid tank be filled completely full of diesel exhaust fluid in order to correct any fault conditions.

> [!note] Note · Примечание
> On on-board diagnostic certified products, the MALFUNCTION INDICATOR LAMP (MIL) may also be illuminated.

![[00c00184.png]]
