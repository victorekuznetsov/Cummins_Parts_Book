---
aliases:
  - "Детектор металлических частиц"
type: "TSB"
doc: "tsb250144"
title_en: "Metal Particle Detector"
title_ru: "Детектор металлических частиц"
released: "2026-01-06"
modified: "2026-01-06"
group: "05 - Fuel Systems (Pumps)"
engines:
  - "33224404"
  - "33239746"
  - "33239899"
  - "41340468"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK50"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2025/tsb250144.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb250144.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK50"
  - "год/2026"
  - "тема/fuel-systems-pumps"
---

# Metal Particle Detector
**Детектор металлических частиц**

> [!abstract] TSB · `tsb250144`
> **Раздел Cummins:** 05 - Fuel Systems (Pumps)
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK50
> **Даты:** выпущен 2026-01-06 · изменён 2026-01-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2025/tsb250144.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb250144.pdf)

## Metal Particle Detector

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- QSK50 CM2150 MCRS
- QSK50 CM2350 K108
- QSK50 CM850 MCRS

**Description of Change**

A new metal particle detector is offered which detects metal debris in the engine lubricating oil.

**Reason for Change**

The new metal particle detector can detect metal debris within the fuel pump and provide advanced warning to prevent progressive damage. After initial installation, the metal particle detector is serviceable on engine without having to remove the fuel pump.

**Service Parts**

| Table 1, Service Parts |  |  |  |  |
|---|---|---|---|---|
| Part Description | Existing Part Number | Obsolete | Superseded | New Part Number |
| KIT,SERVICE | - | No | No | 6536874 |
| HARNESS,WIRING\* (optional) | - | No | No | 6568490 |
| \* Extension wiring harness only required for non-fracturing rig applications. |  |  |  |  |

**Installation Instructions**

Tools Required:

- Blind hole puller for removing cup plug. See Figure 1.
- Recommend the following or equivalent:

![[01r00478.png]]

Figure 1, Blind Hole Puller.

> [!warning] CAUTION · Осторожно
> Do not use heel bars or punches to drive cup plug in and attempt removal; damage can occur to the camshaft lobe.

1. Initial metal particle detector installation requires removing fuel pump from engine. For removal and installation instructions, see corresponding Service Manual. Reference Procedure 005-016 in Section 5.

2. Use blind hole puller to remove center cup plug from bottom of fuel pump. See Figure 2 for cup plug location. Insert blind hole tool into cup plug until blind hole tool bottoms out. Hold expansion collet with wrench and turn actuator pin to expand collet. Tighten the actuator pin until there is firm resistance; do **not** overtighten. The collet should firmly lock into cup plug. Use slide hammer to extract cup plug.

![[01r00479.png]]

Figure 2, Cup Plug Location.

3. Inspect cylinder block to confirm cylinder block lubricating oil pan rail is chamfered. See Figure 3. If chamfered edge is missing, follow Step 4 for field modification. Chamfer is required for metal particle detector removal and install clearance without removing fuel pump.

![[01r00480.png]]

Figure 3, Chamfer.

4. If chamfered edge is missing, locate third capscrew on cylinder block lubricating oil pan rail back from fuel pump mount. Use die grinder with metal cutting bit to create chamfer. Chamfer cylinder block just above third bolt – 25 mm \[ 1 in \] wide and 6 mm \[ 1/4 in \] deep. Cover fuel pump drive to prevent debris ingress. Clean any metal debris thoroughly to prevent metal particle detector contamination, as the sensor is magnetic.

5. Use thread restorer or bottom tap to clean caprscrew hole threads before fuel pump install. Metal particle detector mounting hole **must** be clean of debris to allow proper ground bond for sensor operation.

6. Install fuel pump. Reference Procedure 005-016 in Section 5. With cup plug removed, the step for adding lubricating oil to pre-lube the pump during installation will **not** be possible. Follow recommended fuel pump pre-lube process in Step 8.

7. Insert metal particle detector into number 3 cup plug cavity, see Figure 4. Install supplied spacer between metal particle detector and cylinder block. Install capscrew with washer and torque.

> [!tip] Момент затяжки · Torque Value
> 54 n•m [40 ft-lb]

![[01r00481.png]]

Figure 4, Metal Particle Detector Installed

![[17r02483.png]]

Figure 5, Side View Showing Removal Clearance from Chamfer

8. Before starting engine, fuel pump **must** be pre-lubed with engine oil. If a factory pre-lube system is installed, cycle before starting the engine. If there is no pre-lube system, disconnect injector wiring harnesses at the 8-pin connectors to disable fueling and crank engine to build oil pressure. Once engine oil pressure is observed, reconnect the 8-pin connectors.

9. Many fracturing units already have a wiring interface. Before installing the metal particle detector in other applications, contact your HHP CFSE for wiring interface options.

An extension wiring harness is available for non-Frac rig applications, see Table 1. The extension harness connects to the current engine wiring harness at the connector for the ambient air pressure sensor. There is a branch on the extension harness to reconnect the ambient air pressure sensor, as well as a branch to connect to the metal particle detector.

10. The OEM/Customer is responsible for integration of the sensor signal into their controls for notification of metal particle detector activation when debris is present. The metal particle detector lead provides a ground reference when metallic debris is present on sensor.

Once connected, the electronic chip detector will set off Fault Code 221 or 222. There is **not** a dedicated fault code or lamp within the engine software for the electronic chip detector.

Various forms of integration have been observed for oil and gas applications. Examples are shutting down engine or driving transmission to instant neutral to notify operator of sensor activation. If the OEM/Customer wants the engine or vehicle to automatically respond, the response will need to be programmed into the vehicle controls.

11. The metal particle detector can be field removed and inspected when activated. The sensor face should **not** contain metallic debris buildup. Any metal debris that bridges the gap between the sensing washer and body will activate a ground reference signal.

![[17r02484.png]]

Figure 6, Removed Metal Particle Detector

Metal Particle Detector Operation and Maintenance:

- A single piece of metal debris can activate the metal particle detector. This can be classified as a false activation, but repeated activation indicates a metal debris generating condition has occurred within the engine. **Not** all metal particle detector activations are indication of just fuel pump malfunction, any debris circulation in lube system can be detected by metal particle detector. Repeated activation of metal particle detector will require diagnostics to determine source of debris.
- Metal particle detector surface can be wiped clean or cleaned with a non-metallic brush. Once the metal particle detector is clean, test using resistance function on multimeter. Metal particle detector can be installed or removed for testing. Test should reference metal particle detector lead to metal particle detector body. A clean metal particle detector will read greater than 10 MΩ.

### Document History
