---
aliases:
  - "Система сжатого воздуха — обзор"
type: "Процедура"
doc: "41-012-999"
title_en: "Compressed Air System - Overview"
title_ru: "Система сжатого воздуха — обзор"
modified: "2003-05-13"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-012-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-012-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
---

# Compressed Air System - Overview
**Система сжатого воздуха — обзор**

> [!abstract] Процедура · `41-012-999`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-05-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-012-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-012-999.pdf)

### General Information

The compressed air system normally consists of a gear-driven air compressor, an air governor, air tanks, and all necessary plumbing.

![[ca901gc.png]]

The Holset® QE296 single-cylinder air compressor is an engine-driven, piston-type compressor that supplies compressed air to operate air-activated devices. The compressor runs continuously but has loaded and unloaded operating modes. The operating mode is controlled by a pressure-activated governor and the compressor unloading assembly.

The QE296 air compressor used on C Series engines uses an (E-type) unloader. The economy (E-type) unloader system was designed to reduce pumping losses and engine boost pressure losses through the compressor intake valve while operating in unloading mode.

When the air system reaches a predetermined pressure, the governor applies an air signal to the air compressor unloader assembly, causing the unloader cap to seal off incoming air at the intake valve, and compressed air stops flowing into the air system.

> [!note] Note · Примечание
> System pressure **must** be maintained on the outlet side of the discharge valve to keep the discharge valve closed.

As the air in the air system is used, the pressure drops. At a predetermined pressure, the governor exhausts the air signal to the compressor unloader assembly, allowing the compressor to again pump compressed air into the air system.

> [!warning] CAUTION · Осторожно
> Vehicles equipped with air dryers vented to atmosphere during unloaded compressor operation, using the Holset® (E-type) air compressor, require the installation of an Econ valve to prevent excessive oil consumption.

If the air system pressure is **not** maintained on the discharge valve during unloaded operation, air will be pumped out of the compressor cylinder causing a low pressure (vacuum) condition to form in the cylinder. With the intake valve sealed off by the unloader cap and the exhaust valve being a one-way pressure actuated valve, no air will be allowed to enter the cylinder. When the air compressor cylinder pressure falls below crankcase pressure, oil will be drawn past the piston rings and pumped into the air system.

Other brands of air compressors can be used on C Series engines. Troubleshooting procedures are very similar for these air compressors compared to the Holset® QE296. Refer to the specific air compressor manufacturer's manual for detailed repair information and torque specifications.

The Holset® heavy-duty (HD) air compressors was designed for the C Series engine. Applications include industrial markets, such as transit buses, refuse trucks, on-off highway construction vehicles, and other.

The Holset® heavy-duty model air compressor is a continuous pump version of the QE model already released for the C Series engines. The air compressor crank housing and head are the same; however, the Holset® heavy-duty model does **not** have an integral unloader. Unloading is controlled at the air dryer by way of an internal or external air governor. A discharge line unloader is required for installations **without** air dryers.

The advantage of this air compressor is that the downstream plumbing is simplified because of the elimination of the unloader valve. Standard valves have been replaced with Reed valves to enable the air compressor to run continuously without valve endurance issues.

During unloaded operations, the air compressor's discharge air is continuously vented to the atmosphere through the air dryer's purge port.

The Holset® heavy-duty air compressors can **not** use turbocharged air and **must** be naturally aspirated to prevent loss of engine power. Inlet air for the air compressor **must** be sourced directly from the engine air cleaner, as close to the air cleaner as possible.

The Holset® heavy-duty model air compressors will be designated as the HD650 (QE296 derivative), and HD850 (QE338 derivative). The Holset® heavy-duty models will use the same coolant plumbing as the corresponding QE model.

The following table shows what Holset® heavy-duty model air compressor and part number that will replace the current QE model air compressor:

| HD Model | Part No. | New Option No. | Replaces QE Model |
|---|---|---|---|
| HD650B | 3558127 | CP9202 | 3558049 |
| HD650B | 3558128 | CP9203 | 3558097 |
| HD850B | 3558120 | CP9204 | 3558050 |
| HD850 | 3558121 | CP9209 | 3558098 |
| HD650C | 3558129 | CP9205 and CP9206 | 3558052 |
| HD850C | 3558122 | CP9207 and CP9208 | 3558051 |

> [!note] Note · Примечание
> The QE model air compressor is **not** becoming obsolete. The Holset® heavy-duty model will be available where the QE is **not** capable of supplying sufficient air quality on specific applications.
