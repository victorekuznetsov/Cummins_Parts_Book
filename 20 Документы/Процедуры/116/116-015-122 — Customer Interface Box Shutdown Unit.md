---
aliases:
  - "Блок останова интерфейсной коробки заказчика"
type: "Процедура"
doc: "116-015-122"
title_en: "Customer Interface Box Shutdown Unit"
title_ru: "Блок останова интерфейсной коробки заказчика"
modified: "2026-04-14"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
figures: 12
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-015-122.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-015-122.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Customer Interface Box Shutdown Unit
**Блок останова интерфейсной коробки заказчика**

> [!abstract] Процедура · `116-015-122`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2026-04-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-015-122.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-015-122.pdf)

### Component Diagram

![[15c01538.png]]

Customer Interface Box Shutdown Unit Component Diagram

1. SDU 410 (safety control)
2. Status indicator lamps
3. Shutdown indicator lamps
4. Fault indicator lamps
5. **Acknowledge** button
6. **Overspeed Test** button

### Select Service Tools

#### Recommended Cummins® Service Tools

- Contact cleaner, Part Number 3824510, or equivalent

#### Additional Service Items

- No additional service items required.

### General Information

The SDU 410 is located within the customer interface box (CIB) and provides engine protection by shutting down engine if critical parameter thresholds are exceeded.

**Indicator Lamps**

Status indicator lamps are described in the following table.

| SDU 410 Status Indicator Lamps |  |  |
|---|---|---|
| Lamp Name | Lamp State | Status Description |
| Power | On | Power supply voltage to SDU 410 above 23 VDC. |
|  | Flashing | Power supply voltage to SDU 410 below 23 VDC. |
| Crank Cutoff | On | Engine speed above set threshold to indicate cranking complete. |
| Running | On | Engine speed above set threshold to indicate engine is running. |
| Tacho 1 | On | Engine speed above 5 rpm measured by engine speed sensor connected to channel. |
|  | Flashing | Circuit fault detected on channel. |
| Tacho 2 | On | Engine speed above 5 rpm measured by engine speed sensor connected to channel. |
|  | Flashing | Circuit fault detected on channel. |
| Shutdown Override | On | Shutdown override active. |
| Buzzer | On | SDU 410 audible alarm active. |
| COM 1 | Flashing | Active communication between SDU 410 and DCU 410E. |
| COM 2 | Flashing | Active communication between SDU 410 and another device on RS-485 Modbus channel. |
| COM 3 | Flashing | Active communication between SDU 410 and another device on Ethernet channel. |

Red shutdown indicator lamps are described in the following table. A flashing lamp indicates the condition has **not** been acknowledged by the operator.

| SDU 410 Shutdown Indicator Lamps (Red) |  |
|---|---|
| Lamp Name | Shutdown Description |
| Switch 1 - 8 | Engine shutdown caused by circuit with lamp illuminated. |
| Shutdown | Engine shutdown commanded by SDU 410. Illuminates in addition to switch lamp or overspeed lamp indicating cause of shutdown. |
| Overspeed | Engine shutdown due to overspeed. If rapidly flashing, Overspeed Test is active. See Test section in this procedure. |

Amber fault indicator lamps are described in the following table. A flashing lamp indicates the condition has **not** been acknowledged by the operator.

| SDU 410 Fault Indicator Lamps (Amber) |  |
|---|---|
| Lamp Name | Fault Description |
| Switch 1 - 8 | Switch circuit fault. |
| Shutdown Coil | Shutdown coil circuit fault. |
| Shutdown Override | Shutdown override circuit fault. |

If engine shutdown is caused by the SDU 410, the **Acknowledge** button on the SDU 410 **must** be pressed before the engine can be started.

An audible alarm will sound when shutdown or fault lamps are illuminated. The alarm can be configured to turn off automatically after 5 seconds or remain on until the **Acknowledge** button is pressed on the SDU 410.

**Shutdown Override**

Shutdown override can be enabled using the DCU 410E or an optional customer-provided switch connected to the CIB. When shutdown override is enabled, some SDU 410 engine protection shutdowns are disabled depending on configuration. Engine overspeed protection can **not** be disabled.

**Overspeed Test**

Overspeed Test is used during troubleshooting or equipment certification testing. The engine overspeed threshold will be temporarily lowered to within the normal engine operating range to cause engine shutdown. The red overspeed lamp will flash rapidly when Overspeed Test is active. See Test section of this procedure.

**SDU 410 Switch Channels**

The SDU 410 receives input from up to eight normally open switches. When a switch closes, that SDU 410 channel will be activated and engine shutdown will occur. Six of the channels are defined by Cummins Inc. The remaining channels are available for additional equipment switches, if equipped. See equipment manufacturer service information. The following settings can be configured for each channel:

- **On Run Only** - Channel monitored **only** when engine is running.
- **Shutdown Override Disabled** - Channel will cause engine shutdown regardless of shutdown override status.
- **Enable Speed Dependency** - Channel monitored **only** when engine speed is above set threshold.
- **Delay** - Time before shutdown is commanded after condition is detected.

The following table describes each SDU 410 channel.

| SDU 410 Input Switch Channels |  |
|---|---|
| Switch | Channel Description |
| 1 | High temperature cooling system coolant temperature |
| 2 | High temperature cooling system coolant pressure |
| 3 | Low speed lubricating oil pressure |
| 4 | High speed lubricating oil pressure |
| 5 | Remote emergency stop switch |
| 6 | Optional equipment switch |
| 7 | Emergency stop switch on CIB |
| 8 | Optional equipment switch |

All components handled in this procedure weigh less than 23 kg \[ 50 lb \].

### Test

> [!note] Note · Примечание
> Engine overspeed threshold will be temporarily lowered to within normal engine operating range to cause engine shutdown with engine overspeed fault messages.

Open CIB door. [[116-015-023 — Customer Interface Box|Refer to Procedure 015-023 in Section 15.]]

Perform Overspeed Test.

- Confirm there are no active fault messages on DCU 410E.
- Operate engine at following conditions:
- Hold **Overspeed Test** button on SDU 410 for 2 seconds.
- SDU 410 overspeed red lamp will flash rapidly when Overspeed Test is active.

Overspeed Test will terminate automatically after:

- Engine shutdown due to overspeed
- Five minutes without engine shutdown.

If test is **not** successful, see appropriate troubleshooting trees in Section TT.

![[15200528.png]]

Manually stop Overspeed Test.

- Hold Overspeed Test button on SDU 410 for 2 seconds.
- SDU 410 overspeed red lamp will stop flashing to indicate Overspeed Test terminated.

![[15200529.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect batteries and power supplies. See equipment manufacturer service information.
- Open CIB door. [[116-015-023 — Customer Interface Box|Refer to Procedure 015-023 in Section 15.]]
- Remove conduit box covers, as necessary. [[116-015-137 — Electrical Panel Conduit Box Cover(s)|Refer to Procedure 015-137 in Section 15.]]

### Remove

> [!warning] CAUTION · Осторожно
> Tag wires and install in original location. Electrical damage can occur if wires are installed in incorrect location.

Tag electrical connectors with location on SDU 410.

Remove electrical connectors.

![[15200530.png]]

Remove SDU 410.

- Push SDU 410 down.
- Rotate bottom of SDU 410 off of mounting rail.

![[15200531.png]]

### Disassemble

> [!warning] CAUTION · Осторожно
> Tag wires and install in original location. Electrical damage can occur if wires are installed in incorrect location.

Remove wires from electrical connectors.

- Tag each wire with terminal location.
- Loosen terminal. Use screwdriver.
- Remove wire from terminal.

![[15200551.png]]

### Clean and Inspect for Reuse

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

Clean SDU 410. Use clean, lint-free cloth.

Clean electrical connectors. Use contact cleaner, Part Number 3824510, or equivalent.

![[15200533.png]]

Inspect SDU 410.

Replace if:

- Cracked
- Terminals damaged
- Otherwise damaged.

![[15200534.png]]

Inspect each electrical connector.

Replace if:

- Cracked
- Terminals damaged
- Otherwise damaged.

Inspect wires. [[116-015-138 — Customer Interface Box Electrical Wires|Refer to Procedure 015-138 in Section 15.]]

![[15200554.png]]

### Assemble

> [!warning] CAUTION · Осторожно
> Install wires in original location. Electrical damage can occur if wires are installed in incorrect location.

Install wires in electrical connectors.

- Insert wires in correct location.
- Tighten terminals.
- Lightly pull on each wire to make sure it is properly connected.

![[15200551.png]]

### Install

Install SDU 410.

- Place top of SDU 410 on mounting rail.
- Push SDU 410 down. Rotate bottom of SDU 410 onto mounting rail, as shown.

![[15200536.png]]

> [!warning] CAUTION · Осторожно
> Install wires in original location. Electrical damage can occur if wires are installed in incorrect location.

Install electrical connectors on SDU 410.

![[15200530.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Install conduit box covers. [[116-015-137 — Electrical Panel Conduit Box Cover(s)|Refer to Procedure 015-137 in Section 15.]]
- Close CIB door. [[116-015-023 — Customer Interface Box|Refer to Procedure 015-023 in Section 15.]]
- Connect batteries and power supplies. See equipment manufacturer service information.
