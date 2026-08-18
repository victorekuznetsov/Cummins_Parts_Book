---
aliases:
  - "Топливный насос"
type: "Процедура"
doc: "20-005-016-tr"
title_en: "Fuel Pump"
title_ru: "Топливный насос"
modified: "2017-10-27"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 81
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-005-016-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-005-016-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Fuel Pump
**Топливный насос**

> [!abstract] Процедура · `20-005-016-tr`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 5 - Fuel System · Section 5 - Fuel System - Group 05 · Section 5 - Fuel System - Group 5
> **Даты:** изменён 2017-10-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-005-016-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-005-016-tr.pdf)

### Pressure Test

with Mechanically Actuated Injector

Use the vehicle tachometer or an optical tachometer, Part Number 3377642, along with reflective tape, Part Number 3377464, or equivalent, while checking the fuel pump pressure to determine if the specified engine rpm is reached. [[20-018-016 — Fuel System|Refer to Procedure 018-016 in Section V.]]

![[05500011.png]]

A remote starter, Part Number 3376506, can be used to crank the engine when measuring the cranking pressure.

![[05500007.png]]

Use a pressure gauge and hose assembly, Part Number 3824877, or equivalent, capable of 0 to 2800 kPa \[0 to 400 psi\] with a quick-disconnect fitting, Part Number ST-437-7, or equivalent.

![[05500009.png]]

Engine Cranking

Crank the engine and measure the fuel pressure.

Measure the fuel pressure at 150 rpm.

| Measurements |  |  |
|---|---|---|
|  | kpa | psi |
| Fuel Pressure | 172 | 25 |

![[05500009.png]]

> [!note] Note · Примечание
> Fuel pressure will **not** change significantly with engine load.

Start the engine and operate at specified rpm.

| Minimum Fuel Pressure |  |  |
|---|---|---|
| Engine (rpm) | kPa | psi |
| 1500 rpm | 1344 | 195 |
| 1800 rpm | 1551 | 225 |
| 2100 rpm | 1724 | 250 |
| 2350 rpm | 1827 | 265 |

![[05500009.png]]

If the fuel pump pressure is **not** within specifications, check the fuel pump on a fuel pump test stand.

![[fi8vasd.png]]

If the fuel pump pressure is within specifications when checked on a fuel pump test stand, then check the injector o-rings for damage. [[20-006-026-tr — Injector|Refer to Procedure 006-026 in Section 6.]]

![[06400008.png]]

### General Information

with Electronically Actuated Injector

A chemical streak or buildup at the weep hole is **not** justification for fuel pump replacement. If a steady flow of oil or fuel is observed, replace the fuel pump. Contact a Cummins® Authorized Repair Location.

![[05u00007.png]]

> [!danger] WARNING · Опасно
> The pressure of the fuel in the line is sufficient to penetrate the skin and cause serious personal injury. Wear gloves and protective clothing.

> [!note] Note · Примечание
> The pressure from the fuel system **MUST** be relieved before removing the rail pressure sensor, mechanical dump valve, or injector supply lines.

Cover the plug with a lint-free cloth. Slowly loosen the plug on the last injector of the high-pressure fuel lines 1/4 to 1/2 of a turn. The plug does **not** need to be removed to relieve the pressure.

Connect INSITE™ electronic service tool and monitor the fuel rail pressure to verify the fuel pressure has bled down.

![[19601936.png]]

### Preparatory Steps

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

- Disconnect the battery cables. See equipment manufacturer service information.
- Clean the fuel pump and the surrounding area.

![[ea8coha.png]]

with Electronically Actuated Injector

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!warning] CAUTION · Осторожно
> A very small amount of dirt and debris can be very harmful to the fuel pump. Extra care is required to keep the fuel connections clean during removal and installation. Connections must be covered immediately to keep them clean when components are removed from the fuel pump.

- Disconnect the battery cables. See equipment manufacturer service information.
- Clean the fuel pump and surrounding area and dry with compressed air.
- Disconnect the fuel drain line from the fuel pump. Use a clean plastic plug to protect the fuel drain line port. [[20-006-013-tr — Fuel Drain Lines|Refer to Procedure 006-013 in Section 6.]]
- Disconnect the injector supply line from the fuel pump. Use a clean plastic plug to protect the injector line supply port. [[20-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section 6.]]
- Disconnect the fuel supply lines from the fuel pump. Use a clean plastic plug to protect the fuel supply line port. [[20-006-024-tr — Fuel Supply Lines|Refer to Procedure 006-024 in Section 6.]]

![[ck800wa.png]]

### Remove

with Mechanically Actuated Injector

Disconnect the fuel inlet hose (1).

Disconnect the electronic fuel control valve supply hose (2).

Remove and discard the o-rings.

![[06400007.png]]

Remove the four mounting capscrews and the fuel pump.

Install the fuel pump drive coupling (3).

Remove and discard the gasket.

![[05400320.png]]

Rail Applications

The lubricating oil scavenge pump (A) **must** be removed prior to removing the fuel pump (B) to allow access to the fuel pump mounting capscrews. [[20-007-060 — Oil Scavenge Pump|Refer to Procedure 007-060 in Section 7.]]

![[17400021.png]]

with Electronically Actuated Injector

Disconnect the wiring harness from the fuel pump pressurizing assembly 1 and the injector metering rail 1 pressure sensor.

![[05400248.png]]

Remove the two capscrews securing the fuel pump support bracket (2) to the support bracket (3) located on the engine block.

![[05400290.png]]

Do **not** remove the support bracket (1) from the fuel pump unless the fuel pump needs to be replaced.

![[05400252.png]]

Attach the fuel pump removal and installation service tool, Part Number 4918227, or equivalent.

The fuel pump removal and installation service tool consists of the following:

1. Small lifting connector
2. Lifting bracket
3. Large lifting connector
4. Lifting connector
5. Stop.

Use the small lifting bracket connector (1) to attach the chain to the top hole of the lifting bracket.

Attach one large lifting connector (3) to approximately the third link of the chain above the bracket. Attach the second lifting connector to the last link of the chain.

![[05400291.png]]

Install the bracket onto the fuel pump using two M10 capscrews.

![[05400255.png]]

Place the bottom large lifting connector over the fitting boss on the top of the fuel pump. Screw the stop (1) into the fitting on top of the fuel pump until it is hand-tight.

![[05400256.png]]

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

Attach the top large lifting connector to a suitable lifting device (capable of lifting at least 227 kg \[500 lb\]).

Raise the lifting device until there is no slack in the chain.

![[05400257.png]]

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

Remove the five capscrews securing the fuel pump.

Remove the fuel pump from the engine with a lifting device. Discard the o-rings which seal the oil supply port (1) and fuel pump to the fuel pump drive.

Plug the oil supply port (1) with a clean plastic plug.

![[05400258.png]]

Remove the four capscrews securing the fuel pump support bracket to the engine block.

![[05400251.png]]

### Disassemble

with Electronically Actuated Injector

> [!note] Note · Примечание
> The fuel pump is manufactured using metric fasteners. Use metric size tools during disassembly and assembly of the fuel pump.

Remove the fuel delivery pressure sensor from the fuel pump.

> [!note] Note · Примечание
> Older versions of the fuel pump did **not** use a sealing washer.

Plug the port in the fuel pump with a clean plastic plug.

Remove the sealing washer using a magnet, and then discard it.

![[05400321.png]]

Remove the mechanical dump valve from the fuel pump. Discard the o-ring.

Plug the port in the fuel pump with a clean plastic plug.

![[05400260.png]]

Remove the fuel pump pressurizing assembly 1.

Plug the port in the fuel pump with a clean plastic plug.

![[05400261.png]]

Remove the four capscrews securing the cover plate.

Remove the cover plate and pump. Discard the o-ring.

![[05400262.png]]

Remove the two capscrews securing the fuel pump support bracket (2).

![[05400293.png]]

Remove the two capscrews securing the fuel pump support bracket (1) from the fuel pump.

![[05400292.png]]

### Clean and Inspect for Reuse

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!warning] CAUTION · Осторожно
> Put plastic cup plugs or tape on all the openings. If dirt enters the fuel pump, it can cause equipment damage.

> [!warning] CAUTION · Осторожно
> Use a cleaning solvent that will not harm aluminum.

Use a brush and solvent to clean the pump exterior.

Dry with compressed air.

![[05400072.png]]

Inspect the mounting surfaces for damage.

![[gr8gkea.png]]

Inspect the fuel pump body and front support for cracks or other damage.

Inspect the fuel pump assembly for damaged capscrews and damaged or loose fuel fittings.

Inspect the drive coupling lugs for excessive wear or damage.

![[fp200sa.png]]

Inspect the spider coupling for cracks or other damage.

![[fp8cpca.png]]

with Electronically Actuated Injector

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

Clean all parts with electrical contact cleaner, Part Number 3824510, or equivalent.

![[05400264.png]]

Inspect the main pump for signs of damage, cracks, leaks, or drive shaft damage. Replace the pump, if damaged.

![[05400265.png]]

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

Inspect the oil supply and return passages for restrictions, dirt, and debris.

Clean with electrical contact cleaner, Part Number 3824510, or equivalent.

Dry with compressed air.

![[05400266.png]]

Inspect the fuel delivery pressure sensor for cracks, stripped threads or other damage. Use the following procedure in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850, Modular Common Rail System Engine, Bulletin 4021493. Refer to Procedure 019-115 in Section 19.

![[05400267.png]]

Inspect the fuel pump pressurizing assembly 1 for damage. Use the following procedure in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850, Modular Common Rail System Engine, Bulletin 4021493. Refer to Procedure 019-117 in Section 19.

![[05400268.png]]

Inspect the mechanical dump valve for stripped threads, damage, restricted passage, or cracks. Replace the valve, if damaged.

![[05400269.png]]

Inspect the cover plate for damage and cracks. The cover plate also contains the regulator for the fuel pump.

Check the regulator for passage restriction.

![[05400270.png]]

> [!note] Note · Примечание
> The pump gears are a matched set. The pump gears are to be replaced as a set and **not** as individual gears.

Inspect the pump gears for wear, cracks, debris, and broken and missing teeth.

Check for torsional play of the inner gear to the drive spline in the pump. Replace the pump gears, if damaged.

![[05400271.png]]

Inspect the fuel pump support brackets for damage, corrosion, cracks, and wear. Replace if damaged.

![[05400296.png]]

### Calibrate

with Mechanically Actuated Injector

The control parts list (CPL), Bulletin 3379133, is a listing of the basic parts and timing specifications.

![[lt800gd.png]]

> [!note] Note · Примечание
> Calibration of the fuel pump **must** be performed at a Cummins® Authorized Repair Location.

When removing the fuel pump from the engine, check the CPL number on the fuel pump dataplate (1), which is located on the top of the fuel pump. The CPL number on the fuel pump dataplate (2) **must** be the same as the CPL number on the engine dataplate (4).

If the numbers do **not** match, do **not** install the fuel pump again until the fuel pump calibration code (3) has been changed to match the requirements of the engine dataplate rating. If the fuel pump calibration is changed, the fuel pump dataplate **must** be changed to indicate the new calibration code and the CPL number.

![[fp8plwa.png]]

> [!note] Note · Примечание
> The throttle shaft is locked in the closed position. Rotation of the shaft is **not** necessary for pressure checks.

Drain the fuel pump of diesel fuel as completely as possible to avoid contaminating the test stand calibration fluid. Rotation of the drive coupling in a **counterclockwise** direction will aid in removing fluid held within the pump housing.

![[05400070.png]]

Mount the fuel pump on the test stand. Reference the test stand manufacturer's operating and service manual for pump instructions.

![[05400068.png]]

Set the stand pump to drive to 2100 rpm and purge any air from the fuel pump and test stand.

> [!note] Note · Примечание
> The fuel pump test stand fluid **must** be 32° to 38°C \[90° to 100°F\] during the check procedure.

At 2100 rpm, set the flow volume to obtain 1157 pounds per hour (Pph). Adjust the inlet restriction according to the following:

> [!note] Note · Примечание
> The 178 mm-Hg (7 in-Hg) inlet restriction value **must** be used for all test stands where the vacuum gauge is above the gear pump inner fitting. Use 127 mm-Hg (5 in-Hg) for vacuum gauges at the same level as the inlet fitting.

![[05400068.png]]

Check point one:

- Adjust the test stand drive to obtain 2100 rpm.
- Adjust the flow to obtain 1157 Pph.
- Record the rpm, flow, and inlet restriction.
- Read and record the pressure gauge value.
- The gauge **must** read 250 to 300 psi

Check point two:

- Reduce the test stand drive speed to 1300 rpm.
- Adjust the flow volume to obtain 712 Pph.
- Record the rpm, flow, and inlet restriction.
- The pressure valve **must** read 170 to 200 psi.

Check point three:

- Reduce the test stand drive speed to 600 rpm.
- Adjust the flow volume to obtain 286 Pph.
- Record the rpm, flow, and inlet restriction.
- Read and record the pressure gauge valve.
- The pressure valve **must** read 55 to 70 psi.

> [!note] Note · Примечание
> The fuel pump can **not** be serviced in the field. If the pressure values are **not** within specification, a replacement pump **must** be obtained.

![[05400068.png]]

### Assemble

with Electronically Actuated Injector

Install the pump gears into the fuel pump. Lubricate the o-ring with clean engine oil.

Install the new o-ring on the cover plate and attach the cover plate to the fuel pump.

> [!tip] Момент затяжки · Torque Value
> 19 n•m [168 in-lb]

![[05400262.png]]

Install the fuel pump pressurizing assembly 1 on the fuel pump with three capscrews.

> [!tip] Момент затяжки · Torque Value
> 6.5 n•m [58 in-lb]

![[05400261.png]]

Install the new o-ring on the mechanical dump valve.

Install the mechanical dump valve on the fuel pump.

[[20-006-061 — Fuel Pressure Relief Valve|Refer to Procedure 006-061 in Section 6.]]

![[05400260.png]]

> [!warning] CAUTION · Осторожно
> Older versions of the fuel pump did not use a sealing washer. Do not use a sealing washer on an older version of the fuel pump. The sealing washer will not allow proper thread engagement of the fuel delivery pressure sensor causing damage to the fuel pump.

> [!note] Note · Примечание
> The sealing washer is a single use seal and must be replaced when the injector metering rail pressure sensor is removed or loosened.

Install the new sealing washer, if equipped, and fuel delivery pressure sensor on the fuel pump.

> [!tip] Момент затяжки · Torque Value
> 136 n•m [100 ft-lb]

![[05400321.png]]

### Install

with Mechanically Actuated Injector

All QSK19 engines use a light green fuel pump drive coupling.

Install the fuel pump drive coupling (3), gasket, fuel pump, and four capscrews.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[05400320.png]]

Check for the proper installation of the o-rings in both locations.

Install the fuel pump inlet hose and the fuel supply hose.

Tighten the hoses.

> [!tip] Момент затяжки · Torque Value
> Fuel Pump Inlet Hose 88 n•m [65 ft-lb]

> [!tip] Момент затяжки · Torque Value
> Fuel Supply Hose 60 n•m [44 ft-lb]

![[06400007.png]]

with Electronically Actuated Injector

Install the fuel pump support bracket (1) to the fuel pump with two capscrews.

> [!tip] Момент затяжки · Torque Value
> 113 n•m [83 ft-lb]

![[05400292.png]]

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

On a flat level surface, place the pump on end, with the gerotor-side down.

Pour 104 ml \[3.5 oz\] of fresh, clean lubricating oil into one of the eleven available face drillings (1).

![[05600389.png]]

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

Use clean engine oil to lubricate both new o-rings.

Install the smaller o-ring (1) to seal the oil drilling from the fuel pump drive to the fuel pump.

Install the larger o-ring to seal the fuel pump drive to the fuel pump.

![[05400258.png]]

Install the bracket onto the fuel pump using two M10 capscrews.

![[05400255.png]]

Place the bottom large lifting connector over the fitting boss on the top of the fuel pump. Screw the stop (1) into the fitting on top of the fuel pump until it is hand-tight.

![[05400256.png]]

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

Attach the top large lifting connector to a suitable lifting device (capable of lifting at least 227 kg \[500 lb\].

Raise the lifting device until there is no slack in the chain.

Install the fuel pump onto the engine. The lifting tool has a provision for installing a breaker bar to aid in aligning the fuel pump.

Secure the fuel pump with five capscrews.

> [!tip] Момент затяжки · Torque Value
> 113 n•m [83 ft-lb]

Remove the fuel pump installation and removal service tool.

![[05400257.png]]

Install the fuel pump support bracket (3) to the engine. Hand tighten the capscrews.

The fuel pump support bracket holes are enlarged to aid in alignment. Final tightening will occur when all the brackets are installed and aligned.

![[05400294.png]]

Secure the fuel pump support bracket (2) to the support bracket (3) and the fuel pump with capscrews. Tighten the capscrews finger-tight.

The bracket holes are enlarged to aid in alignment. Final tightening will occur when all the brackets are installed and aligned.

With all the capscrews in place and finger tight, tighten all the capscrews.

| Thread | Socket Size | N•m | \[ft-lb\] |
|---|---|---|---|
| 3/8-16 | 9/16 | 40 | 30 |
| 1/2-13 | 3/4 | 130 | 95 |
| 5/8-11 | 15/16 | 255 | 190 |

![[05400295.png]]

Install a clamp on the injector supply line vent to the fuel pump and on the engine block where the injector supply line attaches.

![[05400249.png]]

Connect the wiring harness to the fuel pump actuator and fuel pump pressure sensor.

![[05400248.png]]

### Flush

with Electronically Actuated Injector

Follow these flush steps anytime debris which may contaminate the fuel system is believed to have fallen into the fuel pump.

A spare U-shaped injector supply line and a container to catch 3.78 L \[1 gal\], or more, fuel are required.

![[06400474.png]]

Remove the injector supply line from the clean bag.

Lubricate the pre-sliced grommets with clean engine oil on the outside and inside diameters.

Install the grommets on the outer wall of the injector supply line.

Remove the yellow threaded caps from the ends of the injector supply line and discard the caps.

![[06400461.png]]

Install a new o-ring on one cone end of the injector supply line.

![[05k00025.png]]

Install the U-shaped injector supply line into the fuel pump outlet.

Start the first thread of the connector nut by hand.

Route the injector supply line into a suitable container that can hold 3.78 L \[1 gal\], or more, of fuel.

![[05k00026.png]]

> [!note] Note · Примечание
> Although the illustration does **not** show tightening the fuel line on the fuel pump, the techniqe is the same.

Tighten the connector nut with a suitable M27 \[1-1/16 in\] crow's foot and torque wrench.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[06400478.png]]

> [!note] Note · Примечание
> Although the illustration does **not** show tightening the fuel line on the fuel pump, the techniqe is the same.

Install the rectangular grommet nuts onto the connector nuts with a suitable M24 \[15/16 in\] crow's foot and torque wrench. Support the connector nut with a wrench while tightening the rectangular grommet nut.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[06400479.png]]

> [!danger] WARNING · Опасно
> Depending on the circumstance, diesel fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting severe personal injury, death or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.

Confirm the injector supply line is routed into the container.

Crank the engine for 60 seconds in 15 second increments to flush fuel through the pump.

> [!missing]- Иллюстрация `05k00032.png` не извлечена — смотрите PDF-оригинал документа

Loosen the rectangular grommet nut on the U-shaped injector supply line.

Loosen the connector nut and remove the injector supply line from the fuel pump.

Remove and discard the o-rings.

Immediately after removing the injector supply line, cap the ends with new yellow threaded caps to prevent debris from entering the line.

![[05k00026.png]]

### Finishing Steps

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the battery cables. See equipment manufacturer service information.
- Operate the engine to normal operating temperature and check for leaks.

![[ck800wa.png]]

with Electronically Actuated Injector

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Install the fuel supply line. [[20-006-024-tr — Fuel Supply Lines|Refer to Procedure 006-024 in Section 6.]]
- Install the injector supply line. [[20-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section 6.]]
- Install the fuel return line. [[20-006-013-tr — Fuel Drain Lines|Refer to Procedure 006-013 in Section 6.]]
- Connect the battery cables. See equipment manufacturer service information.
- Operate the engine and check for leaks.

![[ck800wa.png]]

### Prime

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!note] Note · Примечание
> This procedure is normally **only** required when the fuel pump has been changed, the fuel filters are dry, or the fuel system has been drained.

To reduce engine cranking time, depress the quick-disconnect fitting at the fuel pump outlet until fuel is present while cranking the engine.

> [!note] Note · Примечание
> If the fuel supply pump is dirty, clean the outside of the pump near the fuel inlet and outlet.

![[05400032.png]]

While the engine is cranking, loosen the fuel control supply line at the top of the fuel pump. If fuel does **not** come out of the connection, the pump **must** be primed.

Tighten the fuel supply line.

> [!tip] Момент затяжки · Torque Value
> 60 n•m [44 ft-lb]

![[06400068.png]]

Remove the fuel inlet hose.

![[06400046.png]]

Loosen the fuel pump inlet fitting. Rotate the inlet fitting 180 degrees to point the inlet fitting upward.

![[05400029.png]]

Fill the fuel pump with clean fuel.

![[05400031.png]]

Rotate the fuel pump inlet fitting to its original position.

Tighten the inlet fitting.

> [!tip] Момент затяжки · Torque Value
> 23 n•m [204 in-lb]

![[05400030.png]]

Install the fuel inlet hose to the fuel pump.

> [!tip] Момент затяжки · Torque Value
> 88 n•m [65 ft-lb]

![[06400046.png]]
