---
type: "Процедура"
doc: "10-019-443"
title_en: "Aftertreatment Diesel Particulate Filter Differential/Outlet Pressure Sensor"
modified: "2023-01-24"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 5
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-019-443.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-019-443.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Aftertreatment Diesel Particulate Filter Differential/Outlet Pressure Sensor

> [!abstract] Процедура · `10-019-443`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2023-01-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-019-443.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-019-443.pdf)

### General Information

The aftertreatment diesel particulate filter differential pressure sensor measures pressure across the aftertreatment diesel particulate filter.

Due to the number of various differential pressure sensor mounting arrangements, this procedure has been written to be generic. **Not** all illustrations within this procedure will represent the application that is being serviced.

### Test Initial Conditions

In INSITE™ electronic service tool, add the following parameter to the Data Monitor/Logger screen:

1. Aftertreatment DPF differential pressure sensor signal voltage.

Verify the aftertreatment DPF differential pressure sensor signal voltage at keyswitch ON, engine OFF.

At ambient temperature 25°C \[77°F\] and below, the reading should be between 0.61 and 0.77 VDC.

At ambient temperature 26°C \[78°F\] and above, the reading should be between 0.642 and 0.738 VDC.

If the aftertreatment DPF differential pressure sensor signal voltage does **not** meet specification, replace the aftertreatment DPF differential pressure sensor.

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> Do not allow the wire harness or electrical connectors to make contact with the outside of the aftertreatment canister. Contact with the outside or the canister can result in damage to the wire harness or connectors.

- Disconnect the vehicle batteries. Refer to the OEM service manual.
- Remove the differential pressure sensor tubes. Reference the following procedure in the Signature™, ISX and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[101-011-047-tr — Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Tubes|Refer to Procedure 011-047 in Section 11]].
- Squeeze the locking tab and pull the connector apart to disconnect the pressure sensor wiring harness connector.

![[ck800wa.png]]

### Remove

> [!note] Note · Примечание
> On some applications, one of the flexible hoses will remain on the aftertreatment diesel particulate filter differential pressure sensor when it is removed. This hose is attached with a non-reusable clamp. Do **not** remove the non-reusable clamp.

Remove the two bolts holding the aftertreatment diesel particulate filter differential pressure sensor from the differential pressure sensor mounting bracket.

Remove the differential pressure sensor with the L-shaped bracket and heat shield attached, if applicable.

![[19803868.png]]

### Clean and Inspect for Reuse

Inspect the hoses for cuts or holes. Replace the hoses if damage is found.

Inspect the inside of the hoses for plugging or soot accumulation. If plugging or soot accumulation is seen, the tubes **must** be cleaned. Reference the following procedure in the Signature™, ISX and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]], for cleaning instructions. [[101-011-047-tr — Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Tubes|Refer to Procedure 011-047 in Section 11.]]

Inspect the aftertreatment DPF differential pressure sensor for the following:

- Cracked or broken connector
- Missing or damaged connector seals
- Dirt, debris, or moisture in or on the connector pins
- Corroded, bent, broken, pushed back, or expanded pins
- Chipped, cracked, extruded, or damaged sensor.

Replace the differential/outlet pressure sensor if damage is found.

![[19803869.png]]

### Install

Install the aftertreatment diesel particulate filter differential pressure sensor and the two mounting capscrews.

Tighten the two mounting capscrews.

> [!tip] Момент затяжки · Torque Value
> 10 n•m [89 in-lb]

![[19803868.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Do not allow the wire harness or electrical connectors to make contact with the outside of the aftertreatment canister. Contact with the outside or the canister can result in damage to the wire harness or connectors.

- Squeeze the locking tab and pull the connector apart to disconnect the pressure sensor wire harness connector.
- Install the differential pressure sensor tubes. Reference the following procedure in the Signature™, ISX and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[101-011-047-tr — Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Tubes|Refer to Procedure 011-047 in Section 11.]]
- Connect the vehicle batteries. Refer to the OEM service manual.

![[ck800wa.png]]
