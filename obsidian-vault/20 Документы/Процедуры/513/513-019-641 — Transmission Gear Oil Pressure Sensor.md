---
type: "Процедура"
doc: "513-019-641"
title_en: "Transmission Gear Oil Pressure Sensor"
modified: "2019-09-27"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-019-641.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-019-641.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Transmission Gear Oil Pressure Sensor

> [!abstract] Процедура · `513-019-641`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2019-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-019-641.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-019-641.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Multimeter, Part Number 3164489

#### Additional Service Items

- No additional service items required.

### General Information

The transmission gear oil pressure sensor is used to measure the pressure of the transmission oil and is located on the marine gear oil cooler.

> [!note] Note · Примечание
> The content of this procedure is for the Cummins Inc.-supplied sensor. The sensor may be supplied by the original equipment manufacturer (OEM), therefore the Cummins® service tools listed in this procedure may **not** fit. See equipment manufacturer service information.

### Initial Check

Use the ED-4 to monitor the value of the transmission pressure sensor with the key in the ON position and the engine off.

The gear oil pressure displayed on the ED-4 data screen is in absolute atmospheric pressure at the current elevation when the engine is **not** running.

The transmission pressure sensor value should meet the following specification.

- On the ED-4 data screen, the transmission pressure sensor should read between 47.6 kPa \[6.9 psi\] and 105.5 kPa \[15.3 psi\] at ambient conditions with lower values corresponding to exposure to higher elevations.

Use the following procedure to troubleshoot sensor issues using the ED-4. [[513-015-035 — Display(s) and Instrumentation|Refer to Procedure 015-035 in Section 15]]. If the pressure value is out of specification, replace the pressure sensor.

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. See equipment manufacturer service information.
- Clean the area around the sensor.
- Drain the marine gear oil cooler. Use the following procedure in the Marine QSB6.7 CM2250 Service Manual, Bulletin 4310611. Refer to Procedure 008-041 in Section 8.
- Drain the marine gear oil cooler. Use the following procedure in the Marine QSL9 M CM2250 L106 Service Manual, Bulletin 4358343. Refer to Procedure 008-041 in Section 8.
- Drain the marine gear oil cooler. Use the following procedure in the Marine QSC8.3 CM850 Troubleshooting and Repair Manual, Bulletin 4021418. Refer to Procedure 008-041 in Section 8.
- Drain the marine gear oil cooler. Use the following procedure in the Marine QSM11 CM570 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 008-084 in Section 8.

### Remove

Disconnect the sensor connector from the harness.

Remove the sensor from the marine gear oil cooler.

![[19a00948.png]]

### Clean and Inspect for Reuse

Inspect the harness connector and sensor for the following:

- Cracked or broken connector shell
- Missing or damaged connector seals
- Dirt, debris, or moisture in or on the connector pins
- Corroded, bent, broken, pushed back, or expanded pins
- Chipped, cracked, extruded, or damaged sensor.

Repair or replace parts as necessary.

![[19a00949.png]]

Inspect the sensor for the following:

- Swollen o-ring
- Nicks or cuts in or on the o-ring.

![[19a00950.png]]

### Install

Check to be sure the sensor has an o-ring installed.

Lubricate the o-ring with clean engine oil before installation.

Install the sensor into the marine gear oil cooler.

Tighten the sensor.

> [!tip] Момент затяжки · Torque Value
> 15 ±3 n•m [133 ±27 in-lb]

Connect the harness connector to the sensor.

![[19a00948.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Fill the marine gear oil cooler. Use the following procedure in the Marine QSB6.7 CM2250 Service Manual, Bulletin 4310611. Refer to Procedure 008-041 in Section 8.
- Fill the marine gear oil cooler. Use the following procedure in the Marine QSL9 M CM2250 L106 Service Manual, Bulletin 4358343. Refer to Procedure 008-041 in Section 8.
- Fill the marine gear oil cooler. Use the following procedure in the Marine QSC8.3 CM850 Troubleshooting and Repair Manual, Bulletin 4021418. Refer to Procedure 008-041 in Section 8.
- Fill the marine gear oil cooler. Use the following procedure in the Marine QSM11 CM570 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 008-084 in Section 8.
- Connect the batteries. See equipment manufacturer service information.
- Operate the engine. Check for leaks.
- Perform system test to verify proper function. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15.]]
