---
aliases:
  - "Диагностика системы охлаждения"
type: "Процедура"
doc: "35-008-020-tr"
title_en: "Cooling System Diagnostics"
title_ru: "Диагностика системы охлаждения"
modified: "2009-01-23"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 16
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-020-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-020-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Cooling System Diagnostics
**Диагностика системы охлаждения**

> [!abstract] Процедура · `35-008-020-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 8 - Cooling System - Group 08
> **Даты:** изменён 2009-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-020-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-020-tr.pdf)

### General Information

This procedure tests the correct operation of the fan, shutter, coolant temperature gauge, and thermostat. It also checks for combustion leaks into the cooling system, coolant flow through the filter, and entrained air in the system. Carefully read and understand all the following steps before beginning the troubleshooting procedure.

![[fn2gaka.png]]

This is a free-running (non-dyno) test. It requires the use of the coolant pressure/temperature/flow analyzer kit, Part Number 3822994, and the proper installation of the cooling system Compuchek® fittings located on the engine.

![[il2tolb.png]]

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

Do **not** drain the coolant to install the fittings. Draining the coolant can introduce air into the system and give false results.

![[ra200wa.png]]

The water pump inlet pressure line of the analyzer kit **must** be installed on the water pump inlet Compuchek® fitting on the rear cover of the water pump.

![[wp200ka.png]]

The thermostat housing pressure line of the analyzer kit can be installed in one of the following Compuchek® fitting locations:

- The heater housing on the rear of the water header plate
- The outlet fitting on the water pump.

This connection will enable the operator to record cylinder block coolant pressure.

The remaining line of the analyzer kit **must** be plugged.

![[bp2cowa.png]]

### Setup

Remove the radiator cap and leave it off for the following test.

All cab heaters and air conditioners **must** be turned off and the engine fan control **must** be turned to the automatic position, if applicable.

![[ra1pcmb.png]]

Install the combustion gas leak test instrument, Part Number 3822985. [[35-008-019-tr — Cooling System - Air or Combustion Gas Test|Refer to Procedure 008-019 in Section 8.]]

![[oi800wi.png]]

Install the analyzer kit, Part Number 3822994.

- Red Line - Plugged
- Yellow Line - Cylinder Block Pressure
- Black Line - Water Pump Inlet.

![[il2tola.png]]

### Test

Turn the pressure selection valve to the position corresponding to the desired reading. Turn the temperature selection valve to the OFF position.

When the cylinder block pressure reading is taken, the valve **must** be turned to the thermostat housing pressure location. This is due to the different hose connection used on M Series engines.

![[oi804vo.png]]

Monitor the sight glass installed on the service tool throughout the test. If air is observed, finish the test, and examine the combustion leak tester. This will determine the origin of the leak. [[35-008-019-tr — Cooling System - Air or Combustion Gas Test|Refer to Procedure 008-019 in Section 8.]]

There will be temperature fluctuations when switching the temperature selection valve. This fluctuation is normal and is caused by temperature loss in the line. The temperature will stabilize after a few seconds.

![[oi801kz.png]]

Fill in the blanks with the test data as the test is being run. Mark when the radiator line gets hot, when the fan starts operating, and when the shutters open.

| Temperature | Pressure |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| Thermostat Housing | Cylinder Block | Cab Gauge | Cylinder Block | Radiator "In Line" Starts Getting Hot | Fan Starts Operating | Shutters Open | Notes |
| 140 |  |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ | Engine at high idle throughout test |
| 145 |  |  |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ | Monitor for air throughout test |
| 150 |  |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |  |
| 155 | \_\_\_\_\_\_ | \_\_\_\_\_\_ |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ | Start monitoring radiator “in line” |
| 160 |  |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |  |
| 165 |  |  |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ | Check water filter |
| 170 |  |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |  |
| 175 |  |  |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |  |
| 180 |  |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |  |
| 185 | \_\_\_\_\_\_ | \_\_\_\_\_\_ |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |  |
| 190 |  |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |  |
| 195 |  |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |  |
| 200 |  |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |  |
| 205 |  |  |  | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ | Cool engine down |

### Analyzing the Data

Check the color of fluid in the combustion gas leak tester. This information, along with the sight glass observations, will help isolate the source of air in the cooling system, if any. [[35-008-019-tr — Cooling System - Air or Combustion Gas Test|Refer to Procedure 008-019 in Section 8.]]

Do **not** rule out combustion gas leaks if the combustion gas leak test does **not** indicate a combustion gas leak. The test kit is **not** sensitive enough to detect very small combustion gas leaks.

![[oi801si.png]]

Check the recorded coolant temperature when the shutters are opened. Compare this value to that which is stamped on the shutter control. Cummins Inc. recommends that the shutters open at 85°C \[185°F\].

![[fn1cnkb.png]]

Check the recorded coolant temperature when the fan is engaged. Compare this value to that which is stamped on the fan control. Cummins Inc. recommends that the fan engage at 95°C \[203°F\].

![[fn8cnkc.png]]

Compare the cab temperature gauge reading with the block temperature. Replace the cab temperature gauge if it is **not** within the manufacturer's specifications of the correct reading. If no manufacturer's specifications are available, replace the gauge if it is **not** ±3.9°C \[7°F\] of the correct reading.

![[eg2gaka.png]]

Read the recorded block pressure at 60°C \[140°F\]. If the block pressure is less than 138 kPa \[20 psi\] at high idle and without a pressure cap, check the following:

- Remove the water pump, and inspect the impeller integrity and for slippage on the shaft.

![[wp200mg.png]]

If there is a drop in block pressure of more than 34 kPa \[5 psi\] during the test, check the following:

- Air in the cooling system. Refer to Procedure Refer to Procedure 008-019.
- Incorrect initial cooling system fill.
- Less than 50/50 antifreeze mixture or the engine is at high altitude.
- Remove the water pump, and inspect the impeller integrity and for slippage on the shaft.

![[il2tolb.png]]
