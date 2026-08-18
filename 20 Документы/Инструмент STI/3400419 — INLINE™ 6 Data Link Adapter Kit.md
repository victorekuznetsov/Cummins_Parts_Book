---
aliases:
  - "Комплект адаптера шины данных INLINE™ 6"
type: "Инструкция по инструменту"
doc: "3400419"
title_en: "INLINE™ 6 Data Link Adapter Kit"
title_ru: "Комплект адаптера шины данных INLINE™ 6"
released: "2012-08-15"
modified: "2014-02-19"
revision: "2"
engines:
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41349633"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK19"
  - "QST30"
figures: 3
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/sti/3400419.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/sti/3400419.pdf"
tags:
  - "документ/инструмент"
  - "двигатель/C8.3"
  - "двигатель/K38/K50"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK19"
  - "двигатель/QST30"
---

# INLINE™ 6 Data Link Adapter Kit
**Комплект адаптера шины данных INLINE™ 6**

> [!abstract] Инструкция по инструменту · `3400419`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, K38/K50 · QSK38, QSK50, QSK60, NT/NTA855 · ISM/QSM11, QSK19, QST30
> **Даты:** выпущен 2012-08-15 · изменён 2014-02-19 · ревизия 2
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/sti/3400419.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/sti/3400419.pdf)

### Description

INLINE™ 6 Data Link Adapter Kit

### Purpose

This document provides information for the INLINE™ 6 Data Link Adapter Kit, Part Number 2892092, and the associated cables to connect a personal computer to the data link adapter. The INLINE™ 6 data link adapter is designed for use with the SAE J1708 and J1939 standard protocols. The INLINE™ 6 data link adapter is used with software applications such as INSITE™ Electronic Service Tool 7.5 and later versions. The INLINE™ 6 supports all Cummins Inc. electronic engines.

![[22100120.png]]

| Table 1, INLINE™ 6 Data Link Adapter Kit, Part Number 2892092 |  |  |  |
|---|---|---|---|
| Item Number | Part Number | Description | Quantity |
| 1 | 2892093 | INLINE™ 6 data link adapter | 1 |
| 2 | 2892176 | USB cable, (4.3 m \[14 feet\]) | 1 |
| 3 | 3163096 | J1939 backbone adapter | 1 |
| 4 | 3163597 | J1939 gender change adapter | 1 |
| 5 | 4919780 | Data link cable (DB25F 9-Pin Deutsch™ connector) | 1 |
| 6 | 4918713 | Storage case | 1 |
| 7 | 2892095 | INLINE™ 6 software compact disc | 1 |
| 8 | 2892096 | INLINE™ 6 ruggedized protective boot | 1 |
| 9 | 3165141 | DB25F/2-pin Weather-Pack™/2-pin Weather-Pack™/3-pin Deutsch™ cable | 1 |

| Table 2, Items Used with INLINE™ 6 Data Link Adapter Kit, Part Number 2892092, Purchased Separately |  |  |  |
|---|---|---|---|
| Item Number | Part Number | Description | Quantity |
| **Not** Shown | 4919797 | DB25F/3-pin Deutsch™/3-pin Deutsch™/2-pin Weather-Pack™ cable | 1 |
| **Not** Shown | 3824440 | DB25F 8-Pin AMP™ connector | 1 |
| **Not** Shown | 4918418 | DB9F-DB9M serial cable | 1 |
| **Not** Shown | 3165160 | DB25F/6-pin Deutsch™ cable | 1 |

![[22000084.png]]

> [!note] Note · Примечание
> A fully populated USB cable, Part Number 2892176, or DB9F-DB9M, serial cable, Part Number 4918418, **must** be used.

Connect the DB9F-DB9M serial cable, Part Number 4918418, or the USB cable, Part Number 2892176 to the RS-232 serial port or the USB port of the computer and to the INLINE™ 6 data link adapter, Part Number 2892093.

![[22000085.png]]

The INLINE™ 6 data link adapter requires +8-VDC to +50-VDC at 250mA that can be supplied through the OEM connector or by a separate power source.

Connect the appropriate data link cable to the INLINE™ 6 data link adapter, Part Number 2892093.

With the data link cable connected to the INLINE™ 6 data link adapter, connect the other end of the data link cable to the vehicle cab or engine compartment data link connector.

Launch the electronic service tool application software.

The following are the INLINE™ 6 Adapter Indicator Lamp Functions:

#### Power Lamp

- When the power lamp is lighted green continuously, this means DC power is being supplied to the adapter at the proper voltage level. The INLINE™ 6 adapter requires +8-VDC to +50-VDC at 250 mA that can be supplied through the OEM connector or by a separate power source.
- When the power lamp is lighted red continuously, this means that either the INLINE™ 6 adapter is receiving a low power supply voltage (less than 8-VDC) or is **only** receiving power from the USB port.
- When the power lamp is off, this means that the INLINE™ 6 is receiving no power.

#### CAN 1 Port Lamp

- A CAN 1 red flashing lamp indicates that the INLINE™ 6 adapter is physically connected to a CAN data link. However, it is **not** communicating with an ECM on the CAN data link. A CAN 1 green flashing lamp indicates that the INLINE™ 6 adapter is communicating with an ECM on the CAN data link.

#### CAN 2 Port Lamp

- A CAN 2 red flashing lamp indicates that the INLINE™ 6 adapter is physically connected to a CAN data link. However, it is **not** communicating with an ECM on the CAN data link. A CAN 2 green flashing lamp indicates that the INLINE™ 6 adapter is communicating with an ECM on the CAN data link.

#### J1708 Port Lamp

- A J1708 red flashing lamp indicates that the INLINE™ 6 adapter is physically connected to a J1708 data link. However, it is **not** communicating with an ECM on the J1708 data link. A J1708 green flashing lamp indicates that the INLINE™ 6 adapter is communicating with an ECM on the J1708 data link.

#### RS‐232 Port Lamp

- An RS-232 green flashing lamp indicates that the INLINE™ 6 adapter is connected to an active RS-232 port and exchanging communications. An RS-232 lamp in the OFF state indicates that the INLINE™ 6 adapter is **not** communicating over the RS-232 port.

#### USB Port Lamp

- A USB green flashing lamp indicates that the INLINE™ 6 adapter is connected to an active USB port and is exchanging communications. A USB lamp in the OFF state indicates that the INLINE™ 6 adapter is **not** communicating over the USB port.

### Document History
