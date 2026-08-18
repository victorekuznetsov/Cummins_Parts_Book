---
aliases:
  - "Нет нормального горячего пуска — решение: обратный клапан с меньшим сопротивлением"
type: "TSB"
doc: "tsb200144"
title_en: "“No Normal Hot Restart” condition – Solution Less Restrictive Check Valve"
title_ru: "Нет нормального горячего пуска — решение: обратный клапан с меньшим сопротивлением"
released: "2020-07-20"
modified: "2020-07-20"
group: "07 - Lubricating Oil Systems"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
parts:
  - "3089240"
  - "5416292"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2020/tsb200144.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb200144.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2020"
  - "тема/lubricating-oil-systems"
---

# “No Normal Hot Restart” condition – Solution Less Restrictive Check Valve
**Нет нормального горячего пуска — решение: обратный клапан с меньшим сопротивлением**

> [!abstract] TSB · `tsb200144`
> **Раздел Cummins:** 07 - Lubricating Oil Systems
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2020-07-20 · изменён 2020-07-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2020/tsb200144.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb200144.pdf)

## “No Normal Hot Restart” condition – Solution Less Restrictive Check Valve

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- QST30 CM552\*
- QST30 CM2350 T101\*

> [!note] Note · Примечание
> \*Rolling Prelube and CM850 Applications not affected by this change

**Issue**

Symptoms: After a normal operating shut down mode (\>90 C) a restart condition occurs and

customer may experience no restart or hard restart.

**Failure Mode:**

After investigation, it has been determined pre-lube pump is unable to meet the pressure demands of the prelube pressure switch by using the graphs developed from ECM images. The current pressure switch appears to be set on the high end of the tolerance at 30-34 kPa or 4.35-4.93 psi. Due to oil viscosity low after engine reaches \>85 deg C, prelube pressure is lower than 4 psi, switch never closes to energize the starter circuit for the starter to engage flywheel, and turn over the engine.

When engine is cold, oil viscosity is high, and pressure is high enough to elevate above the 4psi threshold, and engine starter engages flywheel to turn over the engine.

If the engine is equipped with a prelub (prelube) system, the engine doesn't restart when hot and startup times seem longer than normal, there may be a tolerance or factor threshold value preventing the engine from starting faster. Before searching for resolution, ensure no fault codes present and follow Tc t044 before proceeding to resolution below.

**Resolution**

If verification of the part and or situation has been completed, replace current prelube check valve with corresponding part number in the chart below. The new check valve is an improvement to the current design and does not call for a warranty change out of the current design if the application is working. If the application is not running properly (QST30 CM2350 only), contact Service Engineering for the proper campaign to follow.

Prelube check valve changed to a less restrictive valve that allows 20 gallons per min (gpm) flow rate from current 12 gpm flow rate. With the added flow, the pressure intern stays relatively high above 4 psi so the current pressure switch closes to complete the circuit and energize the starter for engine turnover to occur.

Service parts are available. See Table 1 for part numbers.

| Table 1, Service Parts |  |  |  |  |
|---|---|---|---|---|
| Part Description | Existing Part Number | Obsolete | Superseded | New Part Number |
| Valve, Check (O Ring included) | 4371676 | Yes | Yes | [[5416292]] |
| -Seal, O Ring | [[3089240]] | No | No | Doesn't Apply |

Implemented for production. See Table 2.

| Table 2, Production Information |  |  |
|---|---|---|
| ESN First | Build Date 1 | Plant |
| 37280938 (CM2350 only) | 16 Dec 2019 | Seymour Engine Plant |
| 1 Engine build date can be found on the engine dataplate. |  |  |

### Document History

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3089240]] | O RING SEAL | Уплотнительное кольцо |
| [[5416292]] | CHECK VALVE | Обратный клапан |
