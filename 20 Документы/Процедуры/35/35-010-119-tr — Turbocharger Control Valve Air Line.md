---
type: "Процедура"
doc: "35-010-119-tr"
title_en: "Turbocharger Control Valve Air Line"
modified: "2009-01-23"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 5
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-010-119-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-010-119-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Turbocharger Control Valve Air Line

> [!abstract] Процедура · `35-010-119-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2009-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-010-119-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-010-119-tr.pdf)

### General Information

A new turbocharger control valve has been introduced to maximize the performance of the engine without impacting the emissions level.

The new high mount turbocharger control valve is located on the fuel pump side of the engine mounted to the cylinder head. The new high mount turbocharger control valve serves dual roles, replacing the low mount turbocharger control valve and the air filter shutoff assembly as previously utilized on the ISM CM870 engine. The new turbocharger control valve will **not** require an air filter. However, the vehicle **must** be equipped with an air dryer to meet engine installation requirements.

The vehicle air supply will be plumbed directly to the high mount turbocharger control valve at the inlet port identified as port 1. The turbocharger control valve outlet port to the VGT turbocharger is identified as port 2. This information is located on the high mount turbocharger control valve label.

As with previous ISM CM870 engines, the electronic control module (ECM) sends a pulse width modulated (PWM) signal to the turbocharger control valve to control the variable geometry actuator by modulating air pressure. As the signal increases, more air pressure is applied to the variable geometry actuator.

Two new fault codes are associated with the new high mount turbocharger control valve.

- Fault Code 2384 - VGT Actuator - Voltage Below Normal, or Shorted to Low Source
- Fault Code 2385 - VGT Actuator - Voltage Above Normal, or Shorted to High Source

### Preparatory Steps

- Turn the keyswitch to the OFF position.

![[ck800wa.png]]

### Remove

> [!warning] CAUTION · Осторожно
> The turbocharger control valve is very sensitive to contamination. Failure to prevent contamination from entering the turbocharger control valve air lines will cause damage to the turbocharger control valve.

Disconnect the air line at the turbocharger control valve.

Use masking tape to cover the end of the air line and turbocharger control valve to prevent contamination.

Remove the P-clips holding the air line to the engine.

Disconnect the air line at the turbocharger control shutoff valve.

Use masking tape to cover the end of the air line and the turbocharger control shutoff valve to prevent contamination.

Remove the turbocharger control valve air supply line.

![[19202572.png]]

### Inspect for Reuse

Inspect the air line connections for damage or cracks.

Inspect the air line for wear or damage.

Inspect the o-rings for signs of damage or distortion. Replace if damage is found.

![[10c00120.png]]

### Install

> [!warning] CAUTION · Осторожно
> The turbocharger control valve is very sensitive to contamination. Failure to prevent contamination from entering the turbocharger control valve air lines will cause damage to the turbocharger control valve.

> [!warning] CAUTION · Осторожно
> Do not use thread sealant. Use of thread sealant will cause damage to the turbocharger control valve.

Remove the masking tape from the ends of the turbocharger control valve air supply lines before installing.

Connect the air supply line to the turbocharger control valve.

> [!tip] Момент затяжки · Torque Value
> 16 n•m [142 in-lb]

Connect the p-clip to the engine.

> [!tip] Момент затяжки · Torque Value
> 20 n•m [177 in-lb]

Connect the air supply line to the turbocharger control shutoff valve.

> [!tip] Момент затяжки · Torque Value
> 16 n•m [142 in-lb]

![[19202572.png]]

### Finishing Steps

- Turn the keyswitch to the ON position.
- Start and run the engine.
- Verify proper operation.
- Check for fault codes and air leaks.

![[ck800wa.png]]
