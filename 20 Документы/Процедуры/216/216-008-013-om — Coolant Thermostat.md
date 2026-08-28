---
aliases:
  - "Термостат системы охлаждения"
type: "Процедура"
doc: "216-008-013-om"
title_en: "Coolant Thermostat"
title_ru: "Термостат системы охлаждения"
modified: "2017-02-09"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326167"
figures: 15
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/216/216-008-013-om.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/216-008-013-om.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/216"
---

# Coolant Thermostat
**Термостат системы охлаждения**

> [!abstract] Процедура · `216-008-013-om`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326167 — QSB6.7 CM2150 B109 Operation and Maintenance Manual|4326167]]
> **Секции:** Section A - Adjustment, Repair, and Replacement
> **Даты:** изменён 2017-02-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/216/216-008-013-om.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/216-008-013-om.pdf)

### General Information

The thermostat controls the engine coolant temperature. When the coolant temperature is below the operating range, engine coolant is bypassed back to the inlet of the water pump. When the engine coolant temperature reaches the operating range, the thermostat opens, seals off the bypass, and forces engine coolant to flow to the radiator or the heat exchanger.

An incorrect or malfunctioning thermostat can cause the engine to run too hot or too cold.

![[08900038.png]]

> [!warning] CAUTION · Осторожно
> Never operate the engine without a thermostat. Without a thermostat, the path of least resistance for the coolant is through the bypass to the water pump inlet. This can cause the engine to overheat.

![[08d00078.png]]

> [!warning] CAUTION · Осторожно
> A missing check ball can cause the engine to run cold, resulting in engine damage.

The thermostat contains two check balls to vent air past the thermostat when it is closed. This helps to vent air during the cooling system fill process.

> [!note] Note · Примечание
> Some off-highway applications use a thermostat with one check ball. When replacing a thermostat, always be sure to use the same part number. Though an incorrect thermostat will physically fit, it will lead to improper engine operation.

![[08d00094.png]]

### Leak Test

If the thermostat is suspected to be leaking, the following steps can be performed to check for leakage.

The following check **must** be performed with the thermostat closed for 1 minute of engine operation.

Use an electronic service tool to monitor the coolant temperature. The coolant temperature should be less than 38°C \[100°F\] to make sure the thermostat does **not** open during the test.

![[08d00099.png]]

Disconnect the radiator top hose from the water outlet connection.

Install a hose of the same size on the water outlet connection. It must be long enough to reach a remote, dry container that will be used to collect coolant.

Install and tighten a hose clamp on the outlet connection.

Place the other end of the hose in the dry container.

![[08900049.png]]

The coolant temperature should be monitored during this test to determine if the coolant temperature reaches the nominal opening temperature of the thermostat. See the Measurement section of this procedure for nominal opening temperature. If the thermostat opens during this test, the test is invalid and **must** be repeated.

Operate the engine at rated rpm for 1 minute.

Stop the engine and measure the amount of coolant collected in the container.

The amount of coolant **must not** be more than 100 cc \[3.3 fl oz\].

If more than 100 cc \[3.3 fl oz\] of coolant is collected, the thermostat is leaking and **must** be replaced.

![[08d00100.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!warning] CAUTION · Осторожно
> Use caution when draining coolant that coolant is not spilled or drained into the bilge area. Do not pump the coolant overboard. If the coolant is not reused, it must be discarded in accordance with local environmental regulations.

- Disconnect the batteries. Refer to the original equipment manufacturer (OEM) service manual.
- Drain the coolant below the level of the thermostat. Refer to Procedure 008-018 in Sections 5 and 7.
- Disconnect the upper radiator hose from the water outlet connection. Refer to the OEM service manual.

![[ck800wa.png]]

### Remove

Remove the water outlet connection capscrews.

Remove the water outlet connection.

Remove the thermostat.

![[08x00055.png]]

### Clean and Inspect for Reuse

> [!warning] CAUTION · Осторожно
> Do not let any debris fall into the thermostat cavity when cleaning the gasket surfaces. Damage to the cooling system and engine can occur.

Clean the mating surfaces with an abrasive pad, Part Number 3823258, or equivalent, and a clean cloth.

![[08d00369.png]]

Inspect the thermostat for external damage. Also inspect for cracks, embedded debris, missing check balls, damaged seat, and other damage.

Replace the thermostat if any damage is found.

![[08900044.png]]

### Measure

If the thermostat is suspected to be malfunctioning, the opening temperature of the thermostat should be measured to determine if the thermostat is functioning properly.

> [!note] Note · Примечание
> Do **not** allow the thermostat or thermometer to touch the container.

Suspend the thermostat and a 100°C \[212°F\] thermometer in a container of water.

![[08900045.png]]

Heat the water and check the thermostat as follows:

The thermostat **must** meet the following criteria:

82.2°C \[180°F\] Nominal Temperature Thermostat

| Thermostat Opening Temperature |  |  |  |
|---|---|---|---|
|  | celsius |  | fahrenheit |
| Initial Opening | 79.4 | MIN | 175 |
| 83.3 | MAX | 182 |  |
| Fully Opened | 95 | MAX | 203 |

> [!note] Note · Примечание
> The fully open clearance between the thermostat flow valve and flange must be 9.1 mm \[0.36 in\] minimum.

![[08d00054.png]]

### Install

> [!warning] CAUTION · Осторожно
> Always use the correct thermostat and do not operate the engine without a thermostat installed. The engine can overheat if operated without a thermostat because the path of least resistance for the coolant is through the bypass to the pump inlet. An incorrect thermostat can cause the engine to overheat or run too cold.

> [!note] Note · Примечание
> If a previously installed thermostat is being used, make sure a new thermostat seal is used.

Install the thermostat into the thermostat housing.

![[08d00101.png]]

Install the water outlet connection and mounting capscrews.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 10 n•m [89 in-lb]

![[08x00055.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> Always vent the engine during filling to remove air from the coolant system, or overheating can result.

- Connect the upper radiator hose to the water outlet connection. Refer to the OEM service manual.
- Connect the batteries. Refer to the OEM service manual.
- Fill the cooling system. Refer to Procedure 008-018 in Sections 5 and 7.
- Operate the engine and check for leaks.

![[ck800wa.png]]
