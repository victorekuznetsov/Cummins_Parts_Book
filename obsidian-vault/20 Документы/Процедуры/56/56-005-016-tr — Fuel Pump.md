---
aliases:
  - "Топливный насос"
type: "Процедура"
doc: "56-005-016-tr"
title_en: "Fuel Pump"
title_ru: "Топливный насос"
modified: "2014-05-22"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "4021530"
figures: 122
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-005-016-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-005-016-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/56"
---

# Fuel Pump
**Топливный насос**

> [!abstract] Процедура · `56-005-016-tr`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2014-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-005-016-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-005-016-tr.pdf)

### Pressure Test

with Mechanically Actuated Injector

Use the vehicle tachometer or an optical tachometer, Part Number 3377462, when checking the fuel pump pressure to the specified engine rpm. [[56-018-016 — Fuel System|Refer to Procedure 018-016 in Section V.]]

![[05500011.png]]

Use a remote starter to crank the engine when checking the cranking pressure.

![[22600212.png]]

Install the pressure gauge, hose, and quick fitting assembly, Part Number 3376859, or equivalent, capable of 0 to 2758 kPa \[0 to 400 psi\] with a quick-disconnect fitting, Part Number ST-437-7, to the fuel pump test connection.

> [!note] Note · Примечание
> The fuel pump that is being pressure tested is **not** the same model shown in the illustration.

![[05500009.png]]

Engine Cranking

Crank the engine to 175 rpm; measure the fuel pressure.

| Engine Cranking Fuel Pressure |  |  |
|---|---|---|
| kpa |  | psi |
| 241 | MIN | 35 |

![[05500009.png]]

Engine Operation

Start the engine and operate at high-idle.

| Fuel Pressure |  |  |  |
|---|---|---|---|
|  | kpa |  | psi |
| 1500 rpm (50 Hz) | 1572 | MIN | 228 |
| 1800 rpm (60 Hz) | 1820 | MIN | 264 |
| 1900 rpm | 1896 | MIN | 275 |
| 2070 rpm | 1896 | MIN | 275 |

The fuel pressure will **not** change significantly with engine load.

If the fuel pump pressure is **not** within specifications, contact a Cummins® Authorized Repair Location.

![[05500009.png]]

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

Disconnect the battery cables. Refer to the original equipment manufacturer (OEM) service manual.

![[ck800wa.png]]

with Electronically Actuated Injector

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!warning] CAUTION · Осторожно
> A very small amount of dirt and debris can be very harmful to the fuel pump. Extra care is required to keep the fuel connections clean during removal and installation. Connections must be covered immediately to keep them clean when components are removed from the fuel pump.

- Disconnect the battery cables. Refer to the OEM service manual.
- Clean the fuel pump and the surrounding area and dry with compressed air
- Remove the fuel drain line from the fuel pump. Use a clean plastic plug to protect the fuel drain line port. [[56-006-013-tr — Fuel Drain Lines|Refer to Procedure 006-013 in Section 6.]]
- Remove the injector supply line from the fuel pump. Use a clean plastic plug to protect the injector supply port. [[56-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section 6]]
- Remove the fuel supply lines from the fuel pump. Use a clean plastic plug to protect the fuel supply ports. [[56-006-024-tr — Fuel Supply Lines|Refer to Procedure 006-024 in Section 6]]
- Remove the intake manifold pressure sensors and intake manifold air temperature sensor that are located above the fuel pump. Use the following two procedure in the QSK38, QSK50 and QSK60 (CM850 Modular Common Rail System) Troubleshooting and Repair Manual, Bulletin 4021533. Refer to Procedure 019-061 in Section 19. Refer to Procedure 019-059 in Section 19.

![[ck800wa.png]]

### Remove

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause serious personal injury.

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!warning] CAUTION · Осторожно
> Cover all engine openings and electrical equipment to reduce the risk of water damage.

Clean the fuel pump and the surrounding area.

Steam is the best method for cleaning a dirty fuel pump or piece of equipment. If steam is **not** available, use a solvent to wash the engine.

![[05600072.png]]

> [!danger] WARNING · Опасно
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

Disconnect the pressure sensor harness connection and the fuel pump actuator harness connection.

Disconnect the fuel inlet line (1).

Disconnect the electronic fuel control valve supply line (2).

Remove the o-rings.

![[05600073.png]]

Remove the four fuel pump mounting capscrews, two mounting bracket capscrews, and the fuel pump.

Remove the jaw coupling spider.

Remove and discard the gasket.

![[05600074.png]]

with Electronically Actuated Injector

Disconnect the wiring harness to the fuel pump pressurizing assembly and injector metering rail 1 pressure sensor.

![[05600233.png]]

Remove the P-clip securing the wiring of the inlet metering valve to the upper fuel pump support.

![[05600236.png]]

Remove the capscrew securing the upper fuel pump support bracket to the cam cover.

![[05600237.png]]

Remove the two capscrews and spacers securing the upper fuel support bracket to the fuel pump. Retain the two spacers.

![[05600238.png]]

Remove the two capscrews (3) securing the fuel pump support bracket (2) to the support bracket (4).

![[05600239.png]]

Remove the four intake manifold capscrews.

![[05600241.png]]

Install the mounting bracket from the fuel pump lifting fixture kit, Part Number 5299015, or equivalent, to the cylinder block.

Install the two spacers and capscrews. Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 68 n•m [50 ft-lb]

![[05600242.png]]

Install the winch onto the mounting bracket. Install the three capscrews, lock washers, and nuts. Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 68 n•m [50 ft-lb]

![[05600243.png]]

Install the lifting bracket on the fuel pump. Install and tighten the two capscrews.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[05600240.png]]

Attach the lifting hook to the lifting bracket.

Turn the winch handle until the lifting cable is tight.

![[05600245.png]]

Attach a 1/2-inch breaker bar in the square notch of the lifting bracket. This will aid in the removal, installation, and maneuvering of the fuel pump.

![[05600246.png]]

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

Remove the six capscrews securing the fuel pump to the fuel pump drive.

Use the 1/2-inch breaker bar to negotiate the fuel pump out of the fuel pump drive. Remove the fuel pump from the engine.

![[05600247.png]]

Lower the fuel pump using the hand winch.

Remove the hook from lifting bracket.

Remove the 1/2-inch breaker bar from the lifting bracket.

![[05600248.png]]

Remove and discard the o-ring used to seal the oil drilling from the fuel pump drive to the fuel pump.

Remove and discard the o-ring used to seal the fuel pump to the fuel pump drive.

![[05600249.png]]

Remove the four capscrews (1) securing the fuel pump support bracket (2) to the engine block.

![[05600250.png]]

### Disassemble

with Mechanically Actuated Injector

Remove the four regulator assembly mounting capscrews and remove the regulator from the pump.

Make certain the bypass plunger does **not** fall out of the regulator assembly.

Discard the gasket.

![[05600090.png]]

Remove the drive coupling.

A Woodruff key is pressed into the coupling.

![[05600092.png]]

Remove the four gear housing mounting capscrews.

Use a screwdriver in the slots on the front cover (1) to separate the gear housing (2) from the front cover (1).

Discard the o-ring.

![[05600093.png]]

> [!warning] CAUTION · Осторожно
> The chamfered-face of gear tooth outside diameter of the ring gear and pinion gear must be installed toward the gear pocket of the gear housing. If not installed correctly, fuel pump damage can result.

Mark the face of the ring gear and pinion gear for correct orientation in the gear housing.

Remove the ring gear.

![[05600094.png]]

The lip seal retaining ring can **not** be removed with the drive coupling installed.

Use external snap ring pliers to remove the lip seal retaining ring from the coupling end of the pump.

![[05600091.png]]

> [!warning] CAUTION · Осторожно
> Do not allow the shaft assembly to fall to the floor. Damage to the shaft can result.

Use a hydraulic press to slowly press the shaft assembly through the pinion gear and the front cover.

Remove the lip seal from the shaft and discard it.

![[05600095.png]]

Remove the mechanical fuel seal by hand with a twisting, pulling motion.

![[05600096.png]]

Use external snap ring pliers to remove the outer retaining ring from the shaft.

![[05600097.png]]

> [!warning] CAUTION · Осторожно
> The ball bearing is not reusable once it is removed from the shaft. It must be replaced. Reuse of the ball bearing can cause damage to the pump.

Use an arbor press to press the ball bearing from the shaft.

![[05600098.png]]

Use external snap ring pliers to remove the inner retaining ring from the shaft.

![[05600099.png]]

Use a screwdriver to remove the check valve locking ring.

Remove the check valve.

![[05600100.png]]

Locate a punch in one of the slots of the stationary seal from the coupling side of the pump.

Lightly tap the punch to remove the seal from the front housing.

![[05600101.png]]

Fuel Pump Regulator

Remove the metering plunger and spring assembly.

![[05600116.png]]

Use the AFC barrel puller, Part Number 3375599, to remove the metering barrel.

![[05600117.png]]

Remove the filter screen cap, spring, and filter screen.

![[05600118.png]]

Remove the control orifice plug.

![[05600119.png]]

Use the injector orifice torque wrench, Part Number 3376177, to remove the control orifice.

![[05600120.png]]

Use a 19-mm socket to remove the pressure regulator from the regulator housing.

![[05600121.png]]

Remove the pressure relief valve.

![[05600122.png]]

Use the injector orifice torque wrench, Part Number 3376177, to remove the relief orifice from the pressure relief valve.

![[05600123.png]]

with Electronically Actuated Injector

> [!note] Note · Примечание
> The fuel pump is manufactured using metric fasteners. Use metric size tools during disassembly of the pump.

Remove the mechanical dump valve (6). [[102-006-061 — Fuel Pressure Relief Valve|Refer to Procedure 006-061 in Section 6.]]

Plug the mechanical dump valve port with a clean plastic plug.

Remove the fuel rail pressure sensor (7).

Use a magnet to remove the sealing washer (8). Discard the sealing washer.

> [!note] Note · Примечание
> Older versions of the fuel pump did **not** use a sealing washer.

Plug the fuel rail pressure sensor port with a clean plastic plug.

Remove the fuel pump pressurizing assembly (5). [[102-005-232 — Fuel Pump Pressurizing Assembly|Refer to Procedure 005-232 in Section 5.]]

Remove the four capscrews and gerotor cover plate (4). Discard the o-ring (3).

Remove the gerotor gear (2).

![[05600277.png]]

### Clean and Inspect for Reuse

with Mechanically Actuated Injector

Clean and inspect the fuel pump and air compressor or accessory drive mounting surfaces for damage.

Inspect the fuel pump body and front support for cracks or other damage.

Inspect the fuel pump assembly for damaged capscrews and damaged or loose fuel fittings.

Inspect the drive coupling lugs for excessive wear or damage.

![[fp200sa.png]]

Inspect the coupling inner diameter for damage.

Measure the inside diameter of the coupling. The coupling inside diameter can **not** exceed 17.34 ± 0.01 mm \[0.683 ± 0.0003 in\].

![[05600102.png]]

Inspect the spider coupling for cracks or other damage.

![[fp8cpca.png]]

Inspect the ring gear for cracks and chipped or broken teeth.

![[05600103.png]]

Inspect for scratches of the bearing sleeve in the front cover assembly.

![[05600136.png]]

Inspect the pinion gear for cracks and chipped or broken teeth.

![[lp6gesf.png]]

Inspect the shaft for wear nicks and cracks.

Scratches are **not** acceptable in the shaft seal areas.

![[dp1shsa.png]]

Fuel Pump Regulator

Inspect the metering plunger for scuffing.

![[05600124.png]]

Inspect the spring for breakage.

Inspect the filter screen for loose wires.

![[05600125.png]]

Inspect the relief orifice for plugging.

Inspect the control orifice for plugging.

![[05600126.png]]

with Electronically Actuated Injector

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

Clean all parts with electrical contact cleaner, Part Number 3824510, or equivalent.

![[05600218.png]]

Inspect the main pump for cracks, leaks, or drive shaft damage.

Replace the pump if damage is found.

![[05600219.png]]

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

Inspect the oil supply and return passages for restrictions, dirt, and debris.

> [!note] Note · Примечание
> Some pumps have seals installed in the two lower oil drain passages. These should **not** be removed.

Clean passages with electrical contact cleaner, Part Number 3824510, or equivalent.

Dry with compressed air.

![[05600220.png]]

Inspect the pressure sensor for cracks, stripped threads, or other damage. Use the following procedure in the QSK38, QSK50 and QSK60 (CM850 Modular Common Rail System) Troubleshooting and Repair Manual, Bulletin 4021533. Refer to Procedure 019-115 in Section 19.

![[05400267.png]]

Inspect the fuel pump pressurizing assembly for damage. [[102-005-232 — Fuel Pump Pressurizing Assembly|Refer to Procedure 005-232 in Section 5.]]

![[05600222.png]]

Inspect the mechanical dump valve. [[102-006-061 — Fuel Pressure Relief Valve|Refer to Procedure 006-061 in Section 6.]]

![[05400269.png]]

Inspect the cover plate for cracks and other damage. The cover plate also contains the regulator for the fuel pump.

Check the regulator for passage restriction.

![[05400270.png]]

> [!note] Note · Примечание
> The pump gears are a matched set. If the pump gears are to be replaced, they **must** be replaced as a set, **not** individual gears.

Inspect the pump gears for wear, cracks, debris, and broken or missing teeth.

Check for torsional play in the inner gear to the drive spline in the pump.

Replace the pump gears if damage is found.

![[05400271.png]]

Inspect the three fuel pump support brackets for corrosion, cracks, wear, and other damage.

Replace if damage is found.

![[05600226.png]]

### Assemble

with Mechanically Actuated Injector

Apply a light coat of clean engine oil to the o-ring and the outside diameter of the new stationary ring.

Assemble the o-ring to the stationary ring.

Place the new stationary ring into the front cover with the polished side of the ring facing up.

Place the cardboard divider that is provided with the seal assembly onto the stationary ring face.

![[05600104.png]]

Press the stationary ring into place, use a 1-5/16-inch 12-point socket until the stationary ring is fully seated in the bore.

Remove and discard the cardboard divider.

Wipe the face of the stationary ring clean with a soft, white, lint-free cloth.

![[05600105.png]]

Apply a light coat of oil to the check valve o-ring.

The check valve has a directional arrow engraved onto it. The arrow **must** point away from the coupling end of the pump.

Install the check valve into the front cover by hand with the o-ring away from the coupling end of the pump. (If necessary, use a light-duty arbor press.)

Install the locking ring into place with the beveled side pointing toward the check valve and press evenly until it is fully seated.

![[05600106.png]]

Use external snap ring pliers to install the inner retaining ring in the inner groove of the shaft.

![[05600099.png]]

> [!warning] CAUTION · Осторожно
> When installing the ball bearing onto the shaft, press on the inner race of the ball bearing to reduce the risk of damage.

Set the new ball bearing onto the shaft and place a 1-5/16-inch 12-point socket onto the bearing inner race.

Use an arbor press to press the ball bearing onto the shaft until it is seated against the inner retaining ring.

![[05600107.png]]

Use external snap ring pliers to install the outer retaining ring in the outer groove on the shaft.

![[05600097.png]]

> [!warning] CAUTION · Осторожно
> Avoid contact with the carbon seal face of the mechanical fuel seal at all times. Contamination of the seal can cause damage.

Slide the spacer onto the shaft until it rests against the shaft inner retaining ring.

Apply a light film of clean engine oil to the inside diameter of the bellows of the mechanical fuel seal to seal the surfaces.

Apply a light film of clean engine oil to the shaft.

Place the mechanical fuel seal on the shaft and slide the seal assembly down the shaft by hand until it rests against the spacer.

![[05600108.png]]

> [!warning] CAUTION · Осторожно
> The seal and shaft assembly must not be allowed to rest more than 10 minutes before installing into the front cover because the seal tends to adhere to the shaft. Seal damage can result if the shaft is not installed in this time frame.

With a clean, lint-free, soft, white cloth, clean the lapped sealing face of the carbon primary ring of the mechanical seal.

Wipe both the primary ring sealing face and the stationary ring sealing face with a clean light oil.

Place the shaft assembly into the front cover.

Place a piece of 60.325-mm \[2-3/8-in\] hollow, round stock onto the outer race of the bearing.

Use an arbor press to press the shaft assembly into the front cover until the bearing is fully seated in the bore.

![[05600109.png]]

Apply a light film of Loctite® Gasket Eliminator Number 505, or equivalent, to the outside diameter of the lip seal.

Place the lip seal onto the front cover with the lip of the seal pointed away from the cover.

Place a piece of 60.325-mm \[2-3/8-in\] round stock onto the outer diameter of the lip seal.

Press the lip seal into place.

![[05600110.png]]

Use snap ring pliers to install the lip seal retaining ring.

![[05600091.png]]

Apply a light film of clean engine oil to the shaft.

Place a piece of 0.0127 mm \[0.0005-inch\] shim stock on the face of the front cover on two sides of the shaft.

![[05600111.png]]

> [!danger] WARNING · Опасно
> To reduce the possibility of severe burns, wear protective gloves when installing the heated ring gear.

> [!warning] CAUTION · Осторожно
> The chamfered-face of gear tooth outside diameter of each gear is installed towards the bottom of the gear housing bore.

Heat the pinion gear to 246°C \[475°F\] for a minimum of 15 minutes.

> [!note] Note · Примечание
> The shaft for the new style of pump has a smaller diameter, approximately two-thirds of the way down, to assist in installation of the pinion gear.

With the bore chamfered-face of the gear down, slide the hot pinion gear over the shaft until it rests on the shim stock.

Press on the pinion gear with a tool and hold it in place for 10 seconds.

Remove the shim stock.

![[05600112.png]]

Place the o-ring into the groove on the gear housing.

Apply a light film of fuel oil onto the ring gear.

Place the ring gear into the housing, with the chamfered-face of gear tooth outside diameter of the ring gear facing the housing.

![[05600113.png]]

Place the gear housing on a workbench.

Assemble the front cover and gear housing meshing to the ring gear and pinion gear. If needed, turn the shaft to allow the pinion and ring gear to mesh together.

Align the dowel pins in the gear housing to the mating holes in the front cover.

Install the capscrews and tighten.

> [!tip] Момент затяжки · Torque Value
> 54 n•m [40 ft-lb]

![[05600114.png]]

> [!warning] CAUTION · Осторожно
> To avoid loading the bearing, the shaft of the gear pump must be supported when installing the coupling. Pressing force must not exceed 2404 kg \[5300 lb\].

Align the coupling and driveshaft with the Woodruff key. Use a hydraulic press to seat the coupling onto the driveshaft.

Turn the pump shaft to be certain that the shaft rotates freely inside the pump.

![[05600092.png]]

Fuel Pump Regulator

Install the relief orifice into the pressure relief valve.

Install the pressure relief valve into the regulator body.

Install the pressure relief valve plug and tighten the plug.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[05600123.png]]

Install new o-rings onto the mechanical regulator.

Use a 19-mm socket to install the mechanical regulator into the regulator housing.

![[05600127.png]]

Use the injector orifice torque wrench, Part Number 3376177, to install the control orifice and tighten.

> [!tip] Момент затяжки · Torque Value
> 1 n•m [9 in-lb]

Use the injector orifice torque wrench, Part Number 3376177, to install the control orifice plug and tighten.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[05600120.png]]

Install the filter screen with the open part of the screen pointing toward the gear pump side of the regulator housing.

Install the filter screen spring and cap, and tighten the cap.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[05600118.png]]

Apply a light coat of clean engine oil to the outside diameter of the regulator barrel.

Press the regulator barrel in by hand until it is fully seated in the bore.

Press in the metering spring and plunger by hand.

![[05600117.png]]

> [!warning] CAUTION · Осторожно
> To avoid pump damage, make certain the metering plunger does not fall out of the regulator when assembling to the gear housing.

Place the new regulator gasket on the gear housing.

While holding the metering plunger in place, slide the regulator over the gear pump.

Install the four regulator mounting capscrews and tighten.

> [!tip] Момент затяжки · Torque Value
> 47 ± 5 n•m [35 ± 4 ft-lb]

![[05600115.png]]

with Electronically Actuated Injector

Install the gerotor gear (2) into the fuel pump (1).

Lubricate the new o-ring (3) with clean engine oil and install the o-ring onto the gerotor cover plate (4).

Install the gerotor cover plate (4) and the four capscrews.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 19 n•m [168 in-lb]

Install the fuel pump pressurizing assembly (5). [[102-005-232 — Fuel Pump Pressurizing Assembly|Refer to Procedure 005-232 in Section 5]].

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

> [!note] Note · Примечание
> The sealing washer (8) is a single use seal and must be replaced when the injector metering rail pressure sensor (7) is removed or loosened.

Install the new sealing washer (8).

> [!note] Note · Примечание
> Older versions of the fuel pump did **not** use a sealing washer. The use of a sealing washer on an older version of the fuel pump will **not** allow proper thread engagement of the pressure sensor.

Install the injector metering rail 1 pressure sensor (7).

> [!tip] Момент затяжки · Torque Value
> 136 n•m [100 ft-lb]

Install the mechanical dump valve (6). [[102-006-061 — Fuel Pressure Relief Valve|Refer to Procedure 006-061 in Section 6.]]

![[05600277.png]]

### Install

with Mechanically Actuated Injector

Install the fuel pump drive coupling, gasket, fuel pump, and four fuel pump mounting capscrews.

Completely install the fuel pump mounting capscrews, but do **not** tighten them.

![[05600074.png]]

Install the fuel pump support bracket to the bottom of the fuel pump and the engine block.

Tighten the support bracket mounting capscrews enough that the support bracket is in alignment.

![[05600134.png]]

Tighten the fuel pump mounting capscrews.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

Tighten the fuel pump mounting bracket capscrews to the fuel pump.

> [!tip] Момент затяжки · Torque Value
> 80 n•m [59 ft-lb]

Tighten the fuel pump bracket mounting capscrews to the engine block.

> [!tip] Момент затяжки · Torque Value
> 80 n•m [59 ft-lb]

![[05600135.png]]

Install new o-rings in the fuel pump inlet hose fitting and the fuel supply hose fitting.

Install the fuel pump inlet hose (1) and the fuel supply hose (2).

Tighten the hoses.

> [!tip] Момент затяжки · Torque Value
> Fuel pump inlet hose 120 n•m [89 ft-lb]

> [!tip] Момент затяжки · Torque Value
> Fuel supply hose 120 n•m [89 ft-lb]

Connect the fuel pump actuator harness connection.

Connect the pressure sensor harness connection.

![[05600073.png]]

with Electronically Actuated Injector

Install the four capscrews (1) and fuel support bracket (2) to the engine block.

Hand-tighten the capscrews. Do **not** tighten at this time.

![[05600250.png]]

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

On a flat level surface, place the pump on its end with the gerotor-side down.

Pour 104 ml \[3.5 oz\] of fresh, clean lubricating oil into one of the eleven available face drillings (1).

![[05600389.png]]

Attach the lifting bracket to the fuel pump using the supplied hardware.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

Attach the lifting hook to the lifting bracket.

![[05600230.png]]

Use clean engine oil to lubricate both new o-rings.

Install the smaller o-ring that is used to seal the oil drilling from the fuel pump drive to the fuel pump.

Install the large o-ring that is used to seal the fuel pump drive to the fuel pump.

![[05600278.png]]

Attach a ½ inch breaker bar or ratchet to the notch in the lifting bracket.

![[05600246.png]]

> [!warning] CAUTION · Осторожно
> Verify that the o-ring on the flange face of the fuel pump is in place. If the o-ring is missing, replace. Failure to do so will cause failure of the fuel pump due to lack of lubrication.

Raise the fuel pump into place using the hand winch.

![[05600229.png]]

Install the fuel pump into the fuel pump drive. Use a breaker bar or ratchet to help guide the fuel pump into place.

Rotate the pump to align the mounting holes and install the six capscrews.

> [!tip] Момент затяжки · Torque Value
> 117 n•m [86 ft-lb]

![[05600247.png]]

Remove the ½ inch breaker bar or ratchet from the lifting bracket.

![[05600246.png]]

Remove the hook from the lifting bracket.

![[05600245.png]]

Remove the capscrews and lifting bracket from the fuel pump.

![[05600240.png]]

Remove the three capscrews, lock washers, and nuts attaching the winch to the winch support bracket.

Remove the winch.

![[05600243.png]]

Remove the capscrews and winch support bracket.

![[05600242.png]]

Install the intake manifold capscrews.

> [!tip] Момент затяжки · Torque Value
> 68 n•m [50 ft-lb]

![[05600241.png]]

Install the two capscrews and spacers securing the upper fuel support bracket to the fuel pump.

Hand-tighten the capscrews.

![[05600238.png]]

Install the capscrew securing the upper fuel support bracket to the camshaft cover.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 180 n•m [133 ft-lb]

![[05600237.png]]

Install the P-clip securing the wiring of the metering valve to the upper fuel pump support.

![[05600236.png]]

Install the two capscrews (3) securing the fuel pump support bracket (4) to the support bracket (2) mounted to the engine block.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 113 n•m [83 ft-lb]

![[05600239.png]]

Connect the wiring harness to the fuel pump pressurizing assembly and injector metering rail 1 pressure sensor.

![[05600233.png]]

Install the intake manifold pressure sensors and intake manifold air temperature sensor that are located above the fuel pump. Use the following procedures in the QSK38, QSK50 and QSK60 (CM850 Modular Common Rail System) Troubleshooting and Repair Manual, Bulletin 4021533.

- Refer to Procedure 019-061 in Section 19.
- Refer to Procedure 019-059 in Section 19.

![[19600479.png]]

### Flush

with Electronically Actuated Injector

Follow these flush steps anytime debris which may contaminate the fuel system is believed to have fallen in the fuel pump.

Two spare U-shaped injector supply lines and a container to catch 3.78 L \[1 gal\], or more, of fuel are required.

![[06400474.png]]

Remove the injector supply lines from the clean bag.

Lubricate the pre-sliced grommets with clean engine oil on the outside and inside diameters.

Install the grommets on the outer wall of the injector supply lines.

Remove the yellow threaded caps from the ends of the injector supply lines and discard the caps.

![[06400461.png]]

Install a new o-ring on one cone end of the injector supply lines.

![[05k00025.png]]

Install the U-shaped injector supply lines into the fuel pump outlets.

Start the first thread of the connector nuts by hand.

Route the injector supply lines into a suitable container that can hold 3.78 L \[1 gal\], or more, of fuel.

![[05k00029.png]]

> [!note] Note · Примечание
> Although the illustration does **not** show tightening the fuel line on the fuel pump, the techniqe is the same.

Tighten the connector nuts with a suitable M27 \[1-1/16 in\] crow's foot and torque wrench.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[06400478.png]]

> [!note] Note · Примечание
> Although the illustration does **not** show tightening the fuel line on the fuel pump, the techniqe is the same.

Install the rectangular grommet nuts onto the connector nuts with a suitable M24 \[15/16 in\] crow's foot and torque wrench. Support the connector nuts with a wrench while tightening the rectangular grommet nuts.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[06400479.png]]

> [!danger] WARNING · Опасно
> Depending on the circumstance, diesel fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting severe personal injury, death, or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.

Confirm the injector supply lines are routed into the container.

Crank the engine for 60 seconds in 15 second increments to flush fuel through the pump.

![[05k00033.png]]

Loosen the rectangular grommet nut on the U-shaped injector supply lines.

Loosen the connector nut and remove the injector supply lines from the fuel pump.

Remove and discard the o-rings.

Immediately after removing the injector supply lines, cap the ends with new yellow threaded caps to prevent debris from entering the line.

![[05k00029.png]]

### Finishing Steps

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the battery cables. Refer to the OEM service manual.
- Paint the exposed portion of the fuel pump to prevent the formation of rust and corrosion.
- Operate the engine and check for leaks.

![[ck800wa.png]]

with Electronically Actuated Injector

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!warning] CAUTION · Осторожно
> A very small amount of dirt and debris can be very harmful to the fuel pump. Extra care is required to keep the fuel connections clean during removal and installation. Connections must be covered immediately to keep them clean when components are removed from the fuel pump.

- Install the fuel supply line to the fuel pump. [[56-006-024-tr — Fuel Supply Lines|Refer to Procedure 006-024 in Section 6.]]
- Install the injector supply line to the fuel pump. [[56-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section 6.]]
- Connect the fuel drain line to the fuel pump. [[56-006-013-tr — Fuel Drain Lines|Refer to Procedure 006-013 in Section 6.]]
- Connect the battery cables. Refer to the OEM service manual.
- Paint the exposed portion of the fuel pump to prevent the formation of rust and corrosion.
- Operate the engine and check for leaks.

![[ck800wa.png]]
