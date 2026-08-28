---
aliases:
  - "Проверка системы охлаждения на воздух и отработавшие газы"
type: "Процедура"
doc: "35-008-019-tr"
title_en: "Cooling System - Air or Combustion Gas Test"
title_ru: "Проверка системы охлаждения на воздух и отработавшие газы"
modified: "2013-08-22"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 24
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-019-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-019-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Cooling System - Air or Combustion Gas Test
**Проверка системы охлаждения на воздух и отработавшие газы**

> [!abstract] Процедура · `35-008-019-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 8 - Cooling System - Group 08
> **Даты:** изменён 2013-08-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-019-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-019-tr.pdf)

### Initial Check

Air in Cooling System

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

Allow the engine to cool, and remove the radiator cap.

![[ra800qa.png]]

Install a radiator pressure cap that has had the spring and pressure relief valve removed.

The pressure cap **must** make a tight seal.

Attach a rubber hose to the radiator overflow connection.

Place the free end of the hose in a container of water.

![[oi802ka.png]]

Operate the engine at rated rpm until it reaches a temperature of 80°C \[180°F\] with the thermostat open.

Check for a continuous flow of air bubbles from the hose in the water container.

![[oi802kb.png]]

A continuous flow of air bubbles can be caused by one of the following:

- Fan, shutter, or heater air control thermostat valve leaking air.
- An air compressor cylinder head leak.

![[oi802kc.png]]

If one of the air control valves or the air compressor was **not** the source of air entering the cooling system, perform the Combustion Gas Leak Test in this section.

![[oi800wo.png]]

If no air is found in the cooling system, do the following:

- Remove the test equipment
- Check the coolant level and fill, if necessary
- Install the radiator pressure cap
- Operate the engine until it reaches a temperature of 80°C \[180°F\] and check for coolant leaks.

![[rp800ka.png]]

### Leak Test

Fan, Shutter, or Heater Air Control Valve

> [!warning] CAUTION · Осторожно
> The engine can overheat with the fan control or the shutter air control valve disconnected. Monitor the engine coolant temperature while performing this test. The coolant temperature must not exceed 100°C \[212°F\].

![[ra800gb.png]]

Disconnect the vehicle air supply hose to the fan, the shutter, and the heater air control valve.

Install a plug in the air supply hose.

If the vehicle is equipped with more than one air control valve, check **only** one valve at a time.

![[fn2cnkb.png]]

Start the engine and run for 5 minutes before testing for air in the coolant. This will purge any trapped air from the system.

Repeat the test for air in the cooling system as previously described. If no air is found in the cooling system with the air control valve(s) isolated, install a new control valve.

![[fn2cnka.png]]

Air Compressor

> [!warning] CAUTION · Осторожно
> The air compressor discharge line must be disconnected at the compressor to allow the compressor to discharge air to the atmosphere to prevent the compressor from overheating during this next test. Do not run the engine over 5 minutes with components isolated from the cooling system. Component damage can occur.

![[cp2homa.png]]

Disconnect the coolant supply and the return tubes from the air compressor. Use a short piece of hose to connect the tubes together to prevent coolant loss during engine operation.

![[cp2cofa.png]]

Repeat the test for air in the cooling system as previously described. If no air is found in the cooling system with the air compressor isolated, repair or replace the air compressor. [[35-012-014-tr — Air Compressor|Refer to Procedure 012-014 in Section 12.]]

![[cp200ka.png]]

Combustion Gas Leak

Use combustion gas leak test kit, Part Number 3822985 or equivalent, to test for combustion gases in the cooling system.

It is recommended that the cooling system contain a mixture of 50-percent antifreeze and 50-percent water during the combustion gas leak test. The use of **only** water can result in a color change in the test fluid from blue to turquoise or light green during the test. This is **not** an indication of a combustion gas leak.

![[oi800wq.png]]

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

Drain the coolant level down approximately 50 mm \[2 in\] below the radiator cap seal ledge in the radiator fill neck.

![[ra1dcvb.png]]

Pour the test fluid into the combustion gas leak test instrument until it is up to the yellow fill line on the instrument.

![[oi800wm.png]]

Insert the rubber tip of the combustion gas leak test instrument in the radiator fill neck. Hold the instrument down firmly while turning back and forth to make sure that an airtight seal is formed between the tester and radiator fill neck.

![[oi800wi.png]]

Start the engine and run at high idle for approximately 30 minutes. Monitor the engine temperature and color of the test fluid during engine operation. Do **not** allow the engine temperature to exceed 100°C \[212°F\] during the test.

![[oi800wo.png]]

> [!note] Note · Примечание
> Color changes of blue to yellow indicate the presence of carbon dioxide. Color changes of blue to green indicate the presence of sulfur.

If the color of the test fluid changes from blue to yellow anytime during the test, combustion gases are leaking into the cooling system. Discontinue the test if the color of the test fluid changes from blue to yellow.

If the color of the test fluid changes from blue to green anytime during the test, combustion gases are leaking into the cooling system. Discontinue the test if the color of the test fluid changes from blue to green.

![[oi800wu.png]]

If the color of the test fluid does **not** change during the 30-minute test period, return the engine to low idle.

![[oi8toka.png]]

Check the test instrument to make sure that it is firmly sealed in the radiator fill neck.

![[oi800wj.png]]

> [!note] Note · Примечание
> Color changes of blue to yellow indicate the presence of carbon dioxide. Color changes of blue to green indicate the presence of sulfur.

Insert the tip of the rubber ball into the hole in the top of the test instrument. Squeeze the rubber ball 2 to 3 minutes to draw air from the radiator through the test fluid.

If the color of the test fluid remains blue, combustion gases are **not** entering the cooling system.

If the color of the test fluid changes from blue to yellow, or blue to green, combustion gases are entering the cooling system.

Further investigation is required to determine the source of the combustion leak.

![[oi800wn.png]]

As the cooling system warms up to operating temperature, air will be expelled through the combustion gas tester in the form of bubbles in the test fluid. This is due to normal expansion of the coolant.

Do **not** mistake the presence of air bubbles in the tester as combustion gases or air leaks into the cooling system.

A change in the color of the test fluid from blue to yellow or green is the **only** indication of combustion gas in the cooling system.

![[oi800wr.png]]

A positive result from the combustion gas leak tester indicates the following:

- EGR cooler leakage. [[35-011-019-tr — EGR Cooler|Refer to Procedure 011-019 in Section 11.]]
- Cylinder liner protrusion incorrect. [[35-001-028-tr — Cylinder Liner|Refer to Procedure 001-028 in Section 1.]]
- Cylinder head gasket or cylinder head casting leakage. [[35-002-004-tr — Cylinder Head|Refer to Procedure 002-004 in Section 2.]]
- Injector sleeve leakage. [[35-002-004-tr — Cylinder Head|Refer to Procedure 002-004 in Section 2.]]
- Cracked cylinder liner. [[35-001-028-tr — Cylinder Liner|Refer to Procedure 001-028 in Section 1.]]

> [!note] Note · Примечание
> Discard the test fluid if it has indicated positive.

![[oi8cyka.png]]

A negative result from the combustion gas leak tester coupled with a continuous flow of air bubbles from the previous test indicate the following:

- Damaged fan, shutter, or heater air control valve
- Air compressor head or head gasket leakage
- Air entrained due to a bad radiator check valve or incorrect fill.

![[oi800wx.png]]
