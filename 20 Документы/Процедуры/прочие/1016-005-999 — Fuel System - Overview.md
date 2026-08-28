---
aliases:
  - "Топливная система — обзор"
type: "Процедура"
doc: "1016-005-999"
title_en: "Fuel System - Overview"
title_ru: "Топливная система — обзор"
modified: "2022-12-14"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-005-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-005-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
---

# Fuel System - Overview
**Топливная система — обзор**

> [!abstract] Процедура · `1016-005-999`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2022-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-005-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-005-999.pdf)

### General Information

> [!danger] WARNING · Опасно
> Natural gas is explosive and flammable. Always be sure to maintain adequate ventilation in the work area. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas with shared ventilation to reduce the possibility of severe personal injury or death when working on a natural gas system.

#### Vehicle Liquefied Natural Gas (LNG) System

- LNG system consists of components including LNG tank (provided by Original Equipment Manufacturer (OEM)), fuel pressure regulator (integrated with fuel shutoff valves), low-pressure filters, fuel metering valve, and so forth. [[1016-200-001 — Flow Diagram, Fuel System|Refer to Procedure 200-001 in Section F.]]
- From LNG tank, the gas flow is directed through the high-pressure regulators, which will typically reduce the pressure from the storage tanks to less than 10 bar \[ 145 psi \].

#### Vehicle Compressed Natural Gas (CNG) System

- CNG system consists of components including CNG tank (provided by OEM), two fuel pressure regulators (integrated with fuel shutoff valves), low-pressure filters, fuel metering valve, and so forth. [[1016-200-001 — Flow Diagram, Fuel System|Refer to Procedure 200-001 in Section F.]]
- From CNG tank, the gas flow is directed through the high-pressure regulators (1), which will typically reduce the pressure from the storage tanks to less than 10 bar \[ 145 psi \]. The gas flow for the two regulators is connected in parallel.
- The rapid expansion of the gas through the regulators absorbs heat and can cause icing. To prevent icing, the high-pressure regulators can be heated with engine coolant. The coolant ports (2) in the two regulators are connected in series.

![[05s00078.png]]

- The fuel shutoff valve (integrated with fuel pressure regulators) is closed in the un-powered position.
- In the event of a fuel leakage or component malfunction during vehicle operation, the valve is de-energized to isolate the leak or malfunction.

![[05s00026.png]]

- Low-pressure filter is a coalescent-type filter that will capture oil contaminations and moisture typically found in the fuel.

![[05n00045.png]]

- Fuel metering valve is a manifold containing eight injectors and an inlet fuel pressure and temperature sensor. Every injector is controlled separately by pulse width modulation signals.

![[05s00027.png]]

#### Fuel System Gas Flow

- The LNG, supplied from OEM LNG tank, is plumbed through the fuel pressure regulator (integrated with fuel shutoff valves) and fuel filter, then into the fuel metering valve.
- The CNG, supplied from OEM CNG tank, is plumbed through the fuel pressure regulators (integrated with fuel shutoff valves) and fuel filter, then into the fuel metering valve.
- From the fuel metering valve housing, the gas passes into the air fuel mixer housing, where it is introduced into the charge air flow.
