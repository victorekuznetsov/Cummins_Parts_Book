---
aliases:
  - "Информационные коды неисправностей"
type: "Процедура"
doc: "82-ifctabl"
title_en: "Information fault Codes"
title_ru: "Информационные коды неисправностей"
modified: "2002-06-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-ifctabl.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-ifctabl.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Information fault Codes
**Информационные коды неисправностей**

> [!abstract] Процедура · `82-ifctabl`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2002-06-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-ifctabl.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-ifctabl.pdf)

> [!note] Note · Примечание
> - Information Fault Codes have simple, corrective actions and no fault code troubleshooting tree. - SRT 00-394 applies to all of the Information Fault Codes listed below. - After correcting the condition that caused the fault, let the engine warm up; then let the engine run for 1 minute to inactivate the fault code. Then, use INSITE™ to clear the fault code.

CODE:

143

LAMP:

Yellow

REASON:

Oil pressure signal indicates oil pressure is below the low-pressure engine protection limit.

EFFECT:

Progressive power and speed derate with increasing time after alert. If engine protection shutdown feature is enabled, engine will shut down 30 seconds after the red lamp starts flashing.

ACTION:

Refer to the Low Oil Pressure symptom troubleshooting procedure in the ISM/QSM11 Series Engines, Troubleshooting and Repair Manual, Bulletin No. 3666322-00.

CODE:

151

LAMP:

Red

REASON:

Coolant temperature signal indicates temperature is above 104°C (220°F).

EFFECT:

Progressive power derate with increasing time after alert. If engine protection shutdown feature is enabled, engine will shut down 30 seconds after the red lamp starts flashing.

ACTION:

Refer to the High Coolant Temperature symptom troubleshooting procedure in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. 3666322-00.

CODE:

155

LAMP:

Red

REASON:

Intake manifold temperature signal indicates temperature is above 93°C (200°F).

EFFECT:

Progressive power derate with increasing time after alert. If engine protection shutdown feature is enabled, engine will shut down 30 seconds after the red lamp starts flashing.

ACTION:

Refer to the High Intake Manifold Temperature symptom troubleshooting procedure in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. 3666322-00.

CODE:

211

LAMP:

None

REASON:

Additional OEM or vehicle diagnostic codes have been logged. Check other ECMs for diagnostic codes.

EFFECT:

None on engine performance.

ACTION:

Refer to the appropriate OEM manual for assistance in troubleshooting this fault.

CODE:

214

LAMP:

Red

REASON:

Oil temperature signal indicates oil temperature is above 123.9°C (255°F).

EFFECT:

Progressive power derate with increasing time after alert. If engine protection shutdown feature is enabled, engine will shut down 30 seconds after the red lamp starts flashing.

ACTION:

Refer to the High Oil Temperature symptom troubleshooting procedure in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. 3666322-00.

CODE:

219

LAMP:

Maintenance

REASON:

Low oil level was detected in the Centinel™ makeup oil tank.

EFFECT:

None on performance. Centinel™ system deactivated.

ACTION:

Add engine oil to the Centinel™ makeup oil tank. If fault remains active with a full oil tank, remove and clean the oil level sensor.

CODE:

287

LAMP:

Red

REASON:

The OEM vehicle electronic control unit (VECU) detected a fault with its throttle pedal.

EFFECT:

The engine will only idle.

ACTION:

Refer to the OEM troubleshooting and repair manual. Troubleshoot the accelerator pedal connected to the OEM supplied vehicle electronic control unit (VECU).

CODE:

288

LAMP:

Red

REASON:

The OEM vehicle electronic control unit (VECU) detected a fault with its remote throttle.

EFFECT:

The engine will NOT respond to the remote throttle.

ACTION:

Refer to the OEM Troubleshooting and Repair Manual. Troubleshoot the remote throttle pedal connected to the OEM supplied vehicle electronic control unit (VECU).

CODE:

295

LAMP:

Yellow

REASON:

An error in the ambient air pressure sensor signal was detected by the ECM.

EFFECT:

Engine is derated to no-air setting.

ACTION:

Verify ambient air pressure value is from 25.0 in Hg to 30.5 in Hg using INSITE™. Replace ambient air pressure sensor if necessary.

CODE:

299

LAMP:

Yellow

REASON:

The engine was shut down by a device other than the keyswitch before the proper engine cool down resulting in a filtered load factor above the maximum shutdown threshold.

EFFECT:

No action taken by the ECM.

ACTION:

CODE:

415

LAMP:

Red

REASON:

Oil pressure signal indicates oil pressure below the very low oil pressure engine protection limit.

EFFECT:

Progressive power derate with increasing time after alert. If engine protection shutdown feature is enabled, engine will shut down 30 seconds after the red lamp starts flashing.

ACTION:

Refer to the Low Oil Pressure symptom troubleshooting procedure in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. 3666322-00.

CODE:

418

LAMP:

Maintenance

REASON:

Water has been detected in the fuel filter.

EFFECT:

Possible white smoke, loss of power, or hard starting.

ACTION:

Drain water from fuel filter. Refer to the Water in Fuel symptom troubleshooting procedure in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. 3666322-00, if fault reoccurs frequently.

CODE:

419

LAMP:

Yellow

REASON:

An error in the intake manifold pressure sensor signal was detected by the ECM.

EFFECT:

Engine is derated to no-air setting.

ACTION:

Verify intake manifold pressure value is from -2.5 in Hg to 2.5 in Hg using INSITE™. Replace intake manifold pressure/temperature sensor if necessary.

CODE:

435

LAMP:

Yellow

REASON:

An error in the oil pressure sensor signal was detected by the ECM.

EFFECT:

None on performance. No engine protection for oil pressure.

ACTION:

Verify oil pressure valve is from -1.5 psi to 4.0 psi when the engine is stopped using INSITE™. Replace oil pressure/temperature sensor if necessary.

CODE:

471

LAMP:

Yellow

REASON:

Low crankcase oil level was detected by the ECM.

EFFECT:

None on performance. Centinel™ system is deactivated.

ACTION:

CODE:

595

LAMP:

Yellow

REASON:

Turbocharger overspeed protection fault.

EFFECT:

The engine will run derated.

ACTION:

Refer to the High Turbocharger Speed symptom troubleshooting procedure in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. 3666322-00.

CODE:

611

LAMP:

None

REASON:

Engine shutdown by operator before the proper engine cool down, resulting in filtered load factor above maximum shutdown threshold.

EFFECT:

No action taken by the ECM.

ACTION:

Refer to the Hot Shutdown symptom troubleshooting procedures.

CODE:

775

LAMP:

Maintenance

REASON:

A slow leak has been detected in the air system.

EFFECT:

None on performance.

ACTION:

Check the vehicle air system for leaks. Refer to Section 012-019 in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. 3666322-00.

CODE:

776

LAMP:

Yellow

REASON:

A fast leak has been detected in the air system.

EFFECT:

None on performance.

ACTION:

Check the vehicle air system for leaks. Refer to Section 012-019 in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. 3666322-00.

CODE:

951

LAMP:

None

REASON:

A power imbalance between cylinders was detected by the ECM.

EFFECT:

Engine can possibly have rough idle or misfire.

ACTION:

Check fuel quality. Check for air being ingested by the fuel. It is normal to have an inactive Fault Code 951 after a service procedure introduced air into the fuel system, such as a filter change. Perform Cylinder Performance Test to determine if a particular cylinder or cylinders are high or low on power. Refer to Procedure 014-008 Cylinder Performance Test in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. 3666322-00.
