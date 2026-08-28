---
aliases:
  - "Измерение прорыва газов в картер"
type: "Процедура"
doc: "101-014-010-tr"
title_en: "Crankcase Blowby, Measure"
title_ru: "Измерение прорыва газов в картер"
modified: "2020-07-21"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 27
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-010-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-010-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/101"
---

# Crankcase Blowby, Measure
**Измерение прорыва газов в картер**

> [!abstract] Процедура · `101-014-010-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2020-07-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-010-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-010-tr.pdf)

### General Information

> [!note] Note · Примечание
> Some illustrations in this procedure do **not** show actual engine configurations. The procedure, however, is the same.

Excessive crankcase blowby can indicate an engine or engine related component malfunction that allows combustion gases or air to enter the crankcase. This results in the buildup of higher than normal crankcase pressure, which results in increased levels of blowby.

This procedure describes how to measure crankcase blowby and how to determine which component is malfunctioning.

Blowby is typically measured for the following situations:

- Verifying engine break-in after an engine rebuild
- Troubleshooting for excessive lubricating oil out of the crankcase breather tube, commonly referred to as oil carryover (for open crankcase ventilation systems)
- Troubleshooting oil in the air intake system (for closed crankcase ventilation systems)
- Troubleshooting high crankcase pressure (for engines equipped with a crankcase pressure sensor)
- Troubleshooting possible internal engine damage (worn piston rings, valve stem seals or guides, turbocharger, air compressor, etc.).

This procedure provides general guidelines for measuring blowby relative to the above situations.

![[pi900ka.png]]

It is important to note that the terms blowby and carryover (oil out of the breather tube) are commonly used interchangeably.

When measuring blowby, if there is an excessive amount of oil coming out of the breather tube, the quantity of oil can affect the blowby measurement.

The blowby measurement is affected by the oil collecting on the orifice of the blowby measurement service tool. This reduces the size of the orifice, which results in higher than actual blowby measurements.

If this occurs, it will be necessary to:

- Find a different location on the engine to measure blowby (oil fill, oil fill cap, unused turbocharger drain location, etc.).
- Clean any oil residue from the breather and dry thoroughly before measuring blowby.
- Determine if there is an issue causing the breather to be flooded with oil, for example:
- Determine if another breather option is available for the engine being serviced.

![[07900050.png]]

The tools used to measure blowby are similar in design. The difference between the tools is in the size of the orifice. Different size orifices are available to more accurately measure blowby and to accommodate the wide variety of engine configurations and ratings. This is due to the fact that engine blowby is dependent on the volume of intake airflow.

For example:

- If measuring blowby on two identically configured and sized engines, but the horsepower ratings and rated speeds are different, the maximum blowby value measured will be different.

The engine with the higher horsepower rating and rated speed will have a higher volume of intake airflow, which will result in higher blowby. This means that if the smaller orifice blowby tool was used on the engine with a higher horsepower rating and rated speed, the measurement can exceed the limits of the pressure measuring tool.

| Heavy Duty 15L Blowby Tool Part Number | Orifice Size |
|---|---|
| 3822567 | 8.99 mm \[0.354 in\] |

| Heavy Duty 11.9L/12L Blowby Tool Part Number | Orifice Size |
|---|---|
| 3822567 | 8.99 mm \[0.354 in\] |

| Heavy Duty 10.9 - 13L (excluding 11.9L and 12L) Blowby Tool Part Number | Orifice Size |
|---|---|
| 3822566 | 7.67 mm \[0.302 in\] |

To measure the crankcase blowby pressure, connect a water manometer, Part Number ST1111-3, or equivalent, pressure gauge, or transducer to the blowby measurement service tool.

> [!note] Note · Примечание
> Water manometer, Part Number ST1111-3, or equivalent, can measure a maximum of 944 mm \[36 in\] of water.

![[eg8toga.png]]

The following chart shows the relationship of measured pressure to flow rate for a 8.99-mm \[0.354-in\] orifice.

| Blowby Conversion Table with 8.99 mm \[0.354 in\] Orifice and Blowby |  |
|---|---|
| mm H 2 O \[in H 2 O\] | Liter \[cfm\] per Minute |
| 25.4 \[1\] | 70 \[2.472\] |
| 50.8 \[2\] | 100 \[3.531\] |
| 76.2 \[3\] | 120 \[4.238\] |
| 101.6 \[4\] | 140 \[4.944\] |
| 127 \[5\] | 158 \[5.580\] |
| 152.4 \[6\] | 172 \[6.074\] |
| 177.8 \[7\] | 185 \[6.533\] |
| 203.2 \[8\] | 198 \[6.992\] |
| 228.6 \[9\] | 210 \[7.416\] |
| 254 \[10\] | 220 \[7.769\] |
| 279.4 \[11\] | 231 \[8.158\] |
| 304.8 \[12\] | 241 \[8.511\] |
| 330.2 \[13\] | 252 \[8.899\] |
| 355.6 \[14\] | 260 \[9.182\] |
| 381 \[15\] | 270 \[9.535\] |
| 406.4 \[16\] | 280 \[9.888\] |
| 431.8 \[17\] | 289 \[10.206\] |
| 457.2 \[18\] | 298 \[10.524\] |
| 482.6 \[19\] | 305 \[10.771\] |
| 508 \[20\] | 312 \[11.018\] |
| 533.4 \[21\] | 320 \[11.301\] |
| 558.8 \[22\] | 328 \[11.583\] |
| 584.2 \[23\] | 335 \[11.830\] |
| 609.6 \[24\] | 341 \[12.042\] |

The following chart shows the relationship of measured pressure to flow rate for a 7.67-mm \[0.302-in\] orifice.

| Blowby Conversion Table with 7.67 mm \[0.302 in\] Orifice and Blowby |  |
|---|---|
| mm H 2 O \[in H 2 O\] | Liter \[cfm\] per Minute |
| 25.4 \[1\] | 50 \[1.766\] |
| 50.8 \[2\] | 84 \[2.966\] |
| 76.2 \[3\] | 103 \[3.637\] |
| 101.6 \[4\] | 119 \[4.202\] |
| 127 \[5\] | 133 \[4.697\] |
| 152.4 \[6\] | 145 \[5.121\] |
| 177.8 \[7\] | 155 \[5.474\] |
| 203.2 \[8\] | 164 \[5.792\] |
| 228.6 \[9\] | 172 \[6.074\] |
| 254 \[10\] | 180 \[6.357\] |
| 279.4 \[11\] | 187 \[6.604\] |
| 304.8 \[12\] | 193 \[6.816\] |
| 330.2 \[13\] | 200 \[7.063\] |
| 355.6 \[14\] | 206 \[7.275\] |
| 381 \[15\] | 211 \[7.451\] |
| 406.4 \[16\] | 217 \[7.663\] |
| 431.8 \[17\] | 222 \[7.840\] |
| 457.2 \[18\] | 226 \[7.981\] |
| 482.6 \[19\] | 229 \[8.087\] |
| 508 \[20\] | 235 \[8.299\] |
| 533.4 \[21\] | 239 \[8.440\] |
| 558.8 \[22\] | 242 \[8.546\] |
| 584.2 \[23\] | 246 \[8.687\] |
| 609.6 \[24\] | 248 \[8.758\] |

> [!note] Note · Примечание
> If internal engine damage is suspected to be the cause of the excessive blowby condition, other steps can be taken to confirm this.

Measuring blowby **must only** be considered when confirming engine break-in after a rebuild, or if another symptom is present. These symptoms can include:

- Excessive carryover (oil out of the crankcase breather tube)
- High crankcase pressure (for engines equipped with a crankcase pressure sensor)
- Low power
- Oil consumption
- Exhaust smoke.

If no other symptom is present, blowby measurements need **not** be taken.

![[pi900ka.png]]

If internal engine damage is suspected to be the cause of the excessive blowby condition, other steps can be taken to confirm this. The steps include:

- Confirm engine maintenance practices
- Cut the oil filter open and check for debris
- Take an oil sample and inspect for contamination. Use the following procedure for ISM engines. [[35-007-044-tr — Lubricating Oil Contamination|Refer to Procedure 007-044 in Section 7.]] Use the following procedure for ISX engines. [[10-007-083 — Lubricating Oil and Filter Analysis|Refer to Procedure 007-083 in Section 7.]]

![[lf9etba.png]]

### Initial Check

> [!note] Note · Примечание
> The location and type of crankcase breathers vary by engine configuration (front gear train or rear gear train) and/or engine application.

Prior to measuring blowby pressure, check the crankcase breather tube for obstructions. Use the following procedure for ISM engines. [[35-003-002-tr — Crankcase Breather (Internal)|Refer to Procedure 003-002 in Section 3.]] Use the following procedure for ISX engines. Refer to Procedure 003-002 in Section 3.

If troubleshooting a complaint of excessive oil out of the breather tube, it can be necessary to remove the breather components to clean and remove any lubricating oil buildup before performing any blowby measurements.

![[03d00059.png]]

Check the engine oil level and, if necessary, proper calibration of the dipstick. If the level is too high, it can cause a higher than normal blowby pressure and/or excessive carryover. Use the following procedure for ISM engines. [[35-007-009-tr — Lubricating Oil Dipstick|Refer to Procedure 007-009 in Section 7.]] Use the following procedure for ISX engines. Refer to Procedure 007-009 in Section 7.

![[lg900wa.png]]

### Measure

Choose the appropriate blowby measurement service tool to use for the engine being serviced.

| Heavy Duty 15L Blowby Tool Part Number | Orifice Size |
|---|---|
| 3822567 | 8.99 mm \[0.354 in\] |

| Heavy Duty 10.9 - 13L Blowby Tool Part Number | Orifice Size |
|---|---|
| 3822566 | 7.67 mm \[0.302 in\] |

![[14900103.png]]

To measure the crankcase blowby pressure, connect a water manometer, Part Number ST1111-3, pressure gauge, or transducer to the blowby measurement service tool.

> [!note] Note · Примечание
> The location of the crankcase breather tube can vary by engine configuration and/or application.

Install the appropriate blowby service tool(s):

- For typical open crankcase breather/ventilation systems, connect the appropriate blowby service tool to the end of the crankcase breather tube. Connect a water manometer pressure gauge or transducer to the blowby service tool.
- For engines with closed crankcase ventilation systems (without a crankcase ventilation filter), disconnect the breather tube and plug the intake manifold or turbocharger compressor housing port. Connect the appropriate blowby service tool to the end of the crankcase breather tube. Connect a water manometer pressure gauge or transducer to the blowby service tool.
- For engines equipped with external coalescent breather elements (CM871, CM876, CM2250, CM2150, and engines equipped with Enviroguard™ filters) connect the appropriate blowby service tool to the crankcase breather tube on the inlet side of the coalescent breather housing.

![[14d00017.png]]

Check the following for engine blowby contributon.

Operate the engine at rated speed and under load by either:

- For engine run-in, a chassis dynamometer or engine dynamometer.
- For engine testing, a chassis dynamometer or engine dynamometer.
- A stall speed test (for engines equipped with automatic transmissions **only**).

![[oi902vk.png]]

> [!warning] CAUTION · Осторожно
> When measuring blowby and there is an excessive amount of oil coming out of the breather tube, the quantity of oil can affect the blowby measurement.

For specific instructions for the appropriate engine test, reference the appropriate procedure number listed below.

- [[101-014-002-tr — Engine Testing (Chassis Dynamometer)|Refer to Procedure 014-002 in Section 14.]]
- [[101-014-003-tr — Engine Run-in (Chassis Dynamometer)|Refer to Procedure 014-003 in Section 14.]]
- [[101-014-004 — Engine Run-in (Without Dynamometer)|Refer to Procedure 014-004 in Section 14.]]
- [[101-014-005-tr — Engine Testing (Engine Dynamometer)|Refer to Procedure 014-005 in Section 14.]]
- [[101-014-006-tr — Engine Run-in (Engine Dynamometer)|Refer to Procedure 014-006 in Section 14.]]
- [[101-014-008 — Engine Testing (In Chassis)|Refer to Procedure 014-008 in Section 14.]]
- [[101-014-009 — Engine Testing (Portable Dynamometer or Load Bank)|Refer to Procedure 014-009 in Section 14.]]

Operate the engine at rated rpm and full load until a steady reading is obtained.

> [!note] Note · Примечание
> When measuring blowby, the value can “spike” initially as the engine reaches peak power and rated speed. Wait for the blowby measurement to stabilize before taking a reading.

> [!note] Note · Примечание
> For engine run-in, if a sudden increase in blowby occurs, or if blowby exceeds the maximum allowable limit during any run-in step, return to the previous step and continue the run-in. If blowby does **not** reach an acceptable level, discontinue the run-in and determine the cause.

Record the steady blowby measurement.

Remove the engine blowby service tool and water manometer or pressure gauge if the blowby is within specification.

Use the following procedure for appropriate blowby specifications. [[35-018-023 — Engine Testing|Refer to Procedure 018-023 in Section V.]]

![[eg8toja.png]]

Check the following for turbocharger blowby contribution.

With the engine blowby service tool and water manometer or pressure gauge still installed:

- Isolate the turbocharger, if equipped, to determine if the high blowby pressure is due to turbocharger seal leakage.
- To measure the turbocharger blowby contribution, disconnect the turbocharger oil drain line. For ISM engines, use the following procedure. [[35-010-045-tr — Turbocharger Oil Drain Line|Refer to Procedure 010-045 in Section 10.]]

![[07200078.png]]

This describes the preferred turbocharger isolation method.

Install a hose assembly with two shutoff valves (A and B), installed as shown in the illustration, between the turbocharger and turbocharger drain line location in the cylinder block. The valves **must** have a minimum inside diameter of 19 mm \[0.75 in\]. Place the other hose in a 8 to 9 liter \[2 to 5 gal\] container.

> [!note] Note · Примечание
> Some turbocharger oil drain tubes are a single one piece tube. It can be necessary to create a turbocharger isolation tool. Use a new or used turbocharger drain line and cut a middle section out of the turbocharger drain line to fit the check valves and hoses.

Close the valve (A) that allows oil to drain into the bucket.

![[eg4toka.png]]

Open the valve (B) that allows oil to drain into the engine.

![[eg4tokb.png]]

Operate the engine at rated speed and under load by either of the following:

- For engine testing, a chassis dynamometer or engine dynamometer
- A stall speed test (for engines equipped with automatic transmissions **only**).

Operate the engine at rated rpm and full load until a steady reading is obtained.

> [!note] Note · Примечание
> When measuring blowby, the value can “spike” initially as the engine reaches peak power and rated speed. Wait for the blowby measurement to stabilize before taking a reading.

![[oi902vk.png]]

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, keep hands, long hair, jewelry, and loose fitting or torn clothing away from fans and other moving parts.

> [!danger] WARNING · Опасно
> Troubleshooting presents the risk of equipment damage, personal injury, or death. Troubleshooting must be performed by trained, experienced technicians.

> [!warning] CAUTION · Осторожно
> Do not operate the engine with valve (A) open and valve (B) closed for more than 1 minute. Monitor the amount of oil accumulating in the bucket. The engine can run out of lubricating engine oil and severe engine damage will occur.

Continue operating at rated speed and load.

Open valve (A) and close valve (B).

Record the blowby pressure reading.

![[tb4tosa.png]]

> [!warning] CAUTION · Осторожно
> Do not operate the engine for more than 1 minute. Monitor the amount of oil accumulating in the container. The engine can be run out of lubricating engine oil and severe engine damage will result.

These steps describe the alternate turbocharger isolation method:

With the turbocharger oil drain line disconnected from the cylinder block, run the turbocharger drain line into a large container.

Plug the turbocharger oil drain port in the cylinder block.

Operate the engine at rated speed and under load by either:

- For engine testing, a chassis dynamometer or engine dynamometer
- A stall speed test (for engines equipped with automatic transmissions **only**).

Record the peak blowby pressure measurement.

![[14800001.png]]

Determine the turbocharger blowby pressure contribution by determining the difference in the blowby pressure measurement with the turbocharger drain isolated, valve (A) open, and turbocharger drain **not** isolated, valve (A) closed.

| Blowby Pressure Differential |  |
|---|---|
| Turbocharger Blowby Contribution | Maximum: 30 percent |

If the turbocharger blowby contribution is out of specification, inspect the compressor and turbine areas of the turbocharger for signs of an oil leak. Replace the turbocharger, if necessary. For ISM engines, use the following procedure. [[35-010-033-tr — Turbocharger|Refer to Procedure 010-033 in Section 10.]] For ISX engines, use the following procedure. [[10-010-033-tr — Turbocharger|Refer to Procedure 010-033 in Section 10.]]

![[tb200kj.png]]

> [!note] Note · Примечание
> The air compressor governor/unloader location can vary on each engine application. The air governor/unloader can be air compressor mounted or chassis mounted.

Disconnect the air signal line from the air compressor governor/unloader air signal port.

Disconnect the air compressor discharge line and air intake hose from the air compressor.

> [!note] Note · Примечание
> On turbocharged air compressors, make sure to plug the air intake hose going to the engine intake manifold or the engine will **not** reach full power during the test.

![[12800073.png]]

To unload the air compressor, determine the pressure needed at the governor/unloader air signal port to start and stop the air compressor from pumping.

> [!note] Note · Примечание
> Typically, 621 kPa \[90 psi\] of air pressure is the set point between starting and stopping of the air compressor pumping. Refer to the original equipment manufacturer (OEM) service manual.

Connect a regulated shop air pressure line, with pressure gauge, to the air compressor governor/unloader air signal port.

> [!note] Note · Примечание
> When performing the test, make sure that the air system pressure does **not** exceed the manufacturer's maximum allowable pressure.

Run the engine and increase the signal pressure to the air governor/unloader to determine when the air compressor will stop pumping (system pressure stops rising at this point). Record the signal line pressure.

Reduce the signal pressure to determine when system pressure starts the air compressor pumping again (system pressure will begin to rise again at this point). Record the signal line pressure.

> [!note] Note · Примечание
> Allow the air compressor to pump long enough to build enough pressure in the system to release and operate the air brakes.

![[nobox.png]]

With the regulated shop air pressure line still connected to the air compressor governor/unloader air signal port, regulate the signal pressure so that the air compressor starts pumping (system pressure will begin to rise again at this point). Use the pressure value recorded previously as a set point.

Operate the engine at rated speed and under load with either:

- For engine testing, a chassis dynamometer or engine dynamometer
- A stall speed test (for engines equipped with automatic transmissions **only**).

> [!note] Note · Примечание
> When measuring blowby, the value can “spike” initially as the engine reaches peak power and rated speed. Wait for the blowby measurement to stabilize before taking a reading.

![[oi902vk.png]]

Continue operating the engine at rated speed and load. Increase the signal pressure (system pressure stops rising at this point). Use the pressure value recorded previously as a set point.

Operate the engine at rated rpm and full load until a steady reading is obtained.

> [!note] Note · Примечание
> When measuring blowby, the value can “spike” initially as the engine reaches peak power and rated speed. Wait for the blowby measurement to stabilize before taking a reading.

![[nobox.png]]

Determine the air compressor blowby pressure contribution by determining the difference in the blowby pressure measurement with the air compressor pumping and the air compressor **not** pumping.

| Blowby Pressure Differential |  |
|---|---|
| Air Compressor Contribution | Maximum: 30 percent |

If the air compressor blowby contribution is out of specification, replace the air compressor. [[35-012-014-tr — Air Compressor|Refer to Procedure 012-014 in Section 12.]]

![[12d00060.png]]

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

With the engine shut OFF, bleed the vehicle's air system down by opening the draincock on the wet tank to release compressed air from the system.

![[ca800wb.png]]

Disconnect the regulated shop air pressure line, with pressure gauge, from the air compressor governor/unloader air signal port.

Connect the air signal line. Refer to the OEM service manual.

Remove the engine blowby service tool and water manometer or pressure gauge if the blowby is within specification.

> [!note] Note · Примечание
> On turbocharged air compressors, make sure to remove the plug previously installed in the air intake hose going to the engine's intake.

Connect the air compressor discharge line and air intake hose from the air compressor.

![[12800073.png]]

Exhaust Brake Blowby Contribution:

> [!note] Note · Примечание
> **Not** all vehicles are equipped with an exhaust brake.

With the engine blowby service tool and water manometer or pressure gauge still installed, measure blowby pressure during exhaust brake operation, if equipped.

Operate the vehicle going down a long inclined road such as a highway or interstate off ramp. Begin exhaust brake operation at rated engine speed while measuring blowby pressure during exhaust brake operation.

![[20900002.png]]

Also, measure exhaust back pressure during exhaust brake operation.

Operate the engine until a steady reading is obtained.

> [!note] Note · Примечание
> When measuring blowby, the value can “spike” initially as the engine reaches peak power and rated speed. Wait for the blowby measurement to stabilize before taking a reading.

If blowby pressure is above specification during exhaust brake operation and exhaust back pressure is above specification, repair or replace the exhaust brake. See the manufacturer's instructions.

If the blowby pressure is above specification during exhaust brake operation and the exhaust back pressure is within specification, check the turbocharger blowby contribution. Reference the turbocharger oil drain isolation step previously in this procedure.

Remove the engine blowby service tool and water manometer or pressure gauge.

Remove the pressure gauge used to measure exhaust back pressure during exhaust brake operation.

Install a plug in the test port.

![[11d00020.png]]
