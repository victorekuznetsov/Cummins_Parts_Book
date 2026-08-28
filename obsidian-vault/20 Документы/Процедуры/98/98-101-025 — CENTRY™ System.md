---
type: "Процедура"
doc: "98-101-025"
title_en: "CENTRY™ System"
modified: "2003-03-24"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 10
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-101-025.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-101-025.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# CENTRY™ System

> [!abstract] Процедура · `98-101-025`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-101-025.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-101-025.pdf)

### General Information

The CENTRY™ system is an intelligent electronic engine control system designed to optimize engine control on mining, construction, agriculture, and other off-highway equipment. This system can be applied to all engine models that use the PT® fuel system. The CENTRY™ system controls engine speed and fuel pressure based on input from the electronic throttle and other equipment-specific and/or engine-model-specific features.

The CENTRY™ system consists of hydromechanical and electronic subsystems. The electronic subsystem manages fuel delivery using an electronic fuel control (EFC) valve while the hydromechanical subsystem provides backup maximum engine torque and speed protection.

![[19801556.png]]

### CENTRY™ System Description

Hydromechanical Subsystem

**Hydromechanical Subsystem**

This subsystem contains:

1. Fuel Pump

  1. Electronic Fuel Control Module Assembly
  2. Backup Mechanical Governor
  3. Air-Fuel Control.

1. Fuel Shutoff Valve
2. Fuel Tubes
3. Fuel Block (Rail Pressure Sensor Mount)
4. Step Timing Control
5. Injectors.

![[19801557.png]]

The fuel pump is the main part of the hydromechanical subsystem because it supplies the fuel pressure controlled by the electronic fuel control valve. The mechanical governor for the fuel pump provides backup maximum engine torque and speed control.

![[19801558.png]]

The fuel pump air-fuel control uses a turbocharger boost pressure line to regulate the fuel pressure supplied to the electronic fuel control valve. The air-fuel control reduces black smoke and improves engine performance during low-boost conditions.

![[19801559.png]]

The air-fuel control, NO-AIR setting is the maximum fuel rail pressure that the fuel pump can supply when no boost pressure is detected on the boost pressure sensing line. The following graph shows a typical rail pressure versus boost pressure acceleration transition curve. The air-fuel control allows the maximum available fuel rail pressure to increase as boost pressure increases.

![[19801560.png]]

Many engine models use a fuel shutdown valve having a manual override screw. Turning this screw in overrides the shutdown valve and/or shutdown systems connected to the fuel shutoff valve.

> [!note] Note · Примечание
> This screw does **not** override the electronic fuel control valve in the CENTRY™ system.

![[19801561.png]]

The CENTRY™ system uses a fuel block to provide a solid location for the rail pressure sensor.

![[19801562.png]]

On engine models that use STC, some engines will use a fuel pressure sensing line to control a hydromechanical step timing control switch and other engines will use the CENTRY™ system to switch an electronic step timing control solenoid.

Step Timing Control Identification:

1. Fuel Pressure Sensing Line
2. Oil Line to the Tappets
3. Oil Vent Line
4. Oil Supply Line
5. CENTRY™ STC Actuator Lead Wire.

STC allows the engine to operate in advanced injection timing immediately after start-up and light-duty engine load conditions and to return to normal timing during medium and high engine load conditions. The benefits of this feature include:

1. Improved cold weather idling characteristics
2. Reduced cold weather white smoke
3. Improved light-load fuel economy.

![[19801563.png]]

The hydromechanical STC allows two different injection timing modes based on fuel rail pressure detected on the fuel pressure sensing line. Hysterisis provides the maximum rail pressure for the engine to shift from ADVANCED™ to normal timing and the minimum rail pressure for a shift from normal to ADVANCED™ timing. Hysterisis prevents unstable and rapid switching of STC timing modes when the engine is operating at rail pressures within the hysterisis rail pressure range.

![[19801564.png]]

The CENTRY™ electronic STC also allows two different injection timing modes based on measured rail pressure and engine speed. However, CENTRY™ has the capability to provide two different sets of rail pressure STC switch points above and below a calibrated engine speed point. This provides further optimization of engine performance with STC. The ECM provides 12- or 24-VDC to the electronic STC actuator when it is commanding ADVANCED™ timing mode.

![[19801565.png]]
