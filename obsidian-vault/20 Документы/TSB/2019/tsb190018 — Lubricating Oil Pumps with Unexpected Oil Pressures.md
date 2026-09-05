---
type: "TSB"
doc: "tsb190018"
title_en: "Lubricating Oil Pumps with Unexpected Oil Pressures"
modified: "2019-03-25"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
parts:
  - "5532492"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190018.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSX15"
  - "перевод/машинный"
---

# Lubricating Oil Pumps with Unexpected Oil Pressures

> [!abstract] TSB · `tsb190018`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Даты:** изменён 2019-03-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190018.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Насосы моторного масла с неожиданным давлением

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- ISX CM570
- ISX CM870
- ISX CM871
- ISX CM871 E
- ISX15 CM2250
- ISX15 CM2250 SN
- ISX15 CM2350 X101
- QSX15 CM2250
- QSX15 CM2250 ECF
- QSX15 CM2250 X115
- QSX15 CM2350 X105
- QSX15 CM2350 X106
- QSX15 CM570
- QSX15 CM2350 X118
- X15 CM2350 X116B

**Проблема**

Симптом:

- Неожиданно высокое или низкое давление масла, которое не создает один из следующих кодов неисправности:

Первопричина:

- Новый насос для моторного масла был выпущен в производство с различными характеристиками потока, которые не влияют на функцию системы моторного масла.

**Проверка**

Давление моторного масла может быть ± 41 кПа [6 psi], отличное от ожидаемого в нормальных условиях эксплуатации. Определите, генерируются ли коды неисправностей, связанные с давлением масла.

**Решение**

Если не генерируются коды неисправностей, не требуется никаких действий. Если код неисправности генерируется, следуйте обычному дереву устранения неисправностей кода неисправности.

**Причина изменения**

Новый насос для моторного масла из чугуна, часть номер[[5532492]], был выпущен для замены существующего алюминиевого насоса моторного масла, номер детали 3687527, и чугунного насоса моторного масла Номер детали 3687528, для некоторых двигателей 15L. Новый номер детали[[5532492]]имеет различные характеристики потока, которые не влияют на функцию системы моторного масла, но могут привести к различным значениям давления масла, чем ожидалось. Номер детали[[5532492]]не использует стрелки для установки зубчатой ресницы, как существующие насосы моторного масла Части № 3687528 и 3687527.

**Совместимость частей**

Новый насос для моторного масла обратно совместим и взаимозаменяем на двигателях с использованием существующих насосов для моторного масла. Новый насос не использует шимс для установки ресниц. Инструкции по измерению и установке ресниц см. в соответствующих руководствах по обслуживанию. Справочный раздел 007-031.

**Идентификация детали**

Насосы моторного масла могут быть идентифицированы по стилю регуляторной пробки на дне смазочного насоса. Новый насос имеет резьбовую пробку. Существующие насосы имеют защемленную пробку. Насосы также можно отличить по номерам деталей на корпусах насосов. См. рисунки 1 и 2 ниже.

![[07y00022.png]]

Рисунок 1, существующий насос моторного масла с подвесным регуляторным блоком.

![[07y00021.png]]

Рисунок 2, Новый насос моторного масла с регулировщиком точечного патрубка.

**Статус в производстве**

| Таблица 1 Производственная информация |  |  |
|---|---|---|
| ESN First | Постройте дату 1 | растение |
| 80137579 | 14 января 2019 | Джеймстаунский двигательный завод |
| 1 Дата сборки двигателя можно найти на табличке с данными двигателя. |  |  |

**Публикации затронуты**

| Таблица 2, Обновленные процедуры обслуживания |  |  |  |  |  |
|---|---|---|---|---|---|
| Тип ручного | Наименование | Номер бюллетеня | Название процедуры | Процедура | Раздел |
| Руководство по обслуживанию | Подпись, ISX и QSX15 | [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]] | Масляный насос | См. процедуру 007-031 | 7 |
| ISX15 CM2250 | 4022250 |  |  |  |  |
| QSX15 CM2250 | 2883557 |  |  |  |  |
| ISX15 CM2350 X101 | 4310641 |  |  |  |  |
| Power Gen QSX15 CM2250 ECF | 4310661 |  |  |  |  |
| Мощность генератора QSX15 CM2250 | 4310664 |  |  |  |  |
| ISX15 CM2250 SN | 4310736 |  |  |  |  |
| QSX15 CM2350 X105 | 4332667 |  |  |  |  |
| QSX15 CM2350 X106 | 4332712 |  |  |  |  |
| QSX15 CM2250 X115 | 4388739 |  |  |  |  |
| X15 CM2350 X116B | 5411186 |  |  |  |  |
| QSX15 CM2350 X118 | 5467247 |  |  |  |  |
| QSX15 CM2350 X118 | 5467249 |  |  |  |  |

| Таблица 3, Обновленные спецификации системы моторного масла |  |  |  |
|---|---|---|---|
| Тип ручного | Наименование | Номер бюллетеня | Процедура |
| Руководство по обслуживанию | Подпись, ISX и QSX15 | [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]] | 018-017 |
| ISX15 CM2250 | 4022250 |  |  |
| QSX15 CM2250 | 2883557 |  |  |
| ISX15 CM2350 X101 | 4310641 |  |  |
| Power Gen QSX15 CM2250 ECF | 4310661 |  |  |
| Мощность генератора QSX15 CM2250 | 4310664 |  |  |
| ISX15 CM2250 SN | 4310736 |  |  |
| QSX15 CM2350 X105 | 4332667 |  |  |
| QSX15 CM2350 X106 | 4332712 |  |  |
| QSX15 CM2250 X115 | 4388739 |  |  |
| X15 CM2350 X116B | 5411186 |  |  |
| QSX15 CM2350 X118 | 5467247 |  |  |
| QSX15 CM2250 ECF | 2883560 |  |  |
| Руководство по эксплуатации и техническому обслуживанию | Подпись TM/ISX | [[3666251 — Signature and ISX Operation and Maintenance Manual\|3666251]] |  |
| ISX15 CM2250 | 2883361 |  |  |
| QSX15 Промышленная и энергетическая генерация | [[3666423 — QSX15 Operation and Maintenance Manual\|3666423]] |  |  |
| ISX15 CM2350 X101 | 4310640 |  |  |
| PowerGen QSX15 CM2250 ECF | 4310663 |  |  |
| PowerGen QSX15 CM2250 | 4310666 |  |  |
| ISX15 CM2250 SN | 4310735 |  |  |
| QSX15 CM2350 X105 | 4332668 |  |  |
| QSX15 CM2350 X106 | 4332713 |  |  |
| QSX15 CM2250 X115 | 4388740 |  |  |
| X15 CM2350 X116B - серия производительности | 5411187 |  |  |
| QSX15 CM2350 X118 | 5467248 |  |  |
| QSX15 CM2250 ECF | 2883559 |  |  |
| Руководство владельца | Подпись TM/ISX | [[4960314 — ISX Owners Manual\|4960314]] |  |
| ISX15 CM2250 | 2883360 |  |  |
| QSX15 Промышленная и энергетическая генерация | [[4915540 — QSX15 Owners Manual\|4915540]] |  |  |
| ISX15 CM2350 X101 | 4310639 |  |  |
| PowerGen QSX15 CM2250 ECF | 4310662 |  |  |
| PowerGen QSX15 CM2250 | 4310665 |  |  |
| ISX15 CM2250 SN | 4310734 |  |  |
| QSX15 CM2350 X105 | 4332669 |  |  |
| QSX15 CM2350 X106 | 4332714 |  |  |
| QSX15 CM2250 X115 | 4388741 |  |  |
| X15 CM2350 X114B - Серия эффективности, X15 CM2350 X116B - Серия производительности | [[5411183 — X15 CM2350 X114B - Efficiency Series and X15 CM2350 X116B - Performance Series Owners\|5411183]] |  |  |
| QSX15 CM2350 X118 | 5467249 |  |  |

### История изменений документа

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[5532492]] | LUBRICATING OIL PUMP | Масляный насос |

> [!quote]- Original (English) · английский оригинал
> ## Lubricating Oil Pumps with Unexpected Oil Pressures
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - ISX CM570
> - ISX CM870
> - ISX CM871
> - ISX CM871 E
> - ISX15 CM2250
> - ISX15 CM2250 SN
> - ISX15 CM2350 X101
> - QSX15 CM2250
> - QSX15 CM2250 ECF
> - QSX15 CM2250 X115
> - QSX15 CM2350 X105
> - QSX15 CM2350 X106
> - QSX15 CM570
> - QSX15 CM2350 X118
> - X15 CM2350 X116B
>
> **Issue**
>
> Symptom:
>
> - Unexpectedly high or low oil pressures that do **not** generate one of the following fault codes:
>
> Root Cause:
>
> - A new lubricating oil pump was released to production with different flow characteristics that do **not** affect function of the lubricating oil system.
>
> **Verification**
>
> Lubricating oil pressures may be ± 41 kPa \[ 6 psi \] different than expected during normal operating conditions. Determine if any oil pressure related fault codes are being generated.
>
> **Resolution**
>
> If no fault codes are generated no action is required. If a fault code is generated follow the normal fault code troubleshooting tree.
>
> **Reason for Change**
>
> A new cast iron lubricating oil pump, Part Number [[5532492]], was released to replace an existing aluminum lubricating oil pump, Part Number 3687527, and cast iron lubricating oil pump Part Number 3687528, for some 15L engines. New Part Number [[5532492]] has different flow characteristics that do **not** affect lubricating oil system function, but can result in different oil pressure values than expected. Part Number [[5532492]] does **not** use shims to set gear lash like existing lubricating oil pump Part Numbers 3687528 and 3687527.
>
> **Part Compatibility**
>
> New lubricating oil pump is backwards compatible, and interchangeable on engines using existing lubricating oil pumps. New pump does **not** use shims to set gear lash. For instructions on measuring and setting gear lash, see corresponding Service Manuals. Reference section 007-031.
>
> **Part Identification**
>
> Lubricating oil pumps can be identified by the style of the regulator plug on the bottom of the lube pump. The new pump has a threaded plug. Existing pumps have a pinned plug. Pumps can also be distinguished by part numbers on the pump housings. See Figures 1 and 2 below.
>
> Figure 1, Existing Lubricating Oil Pump with Pinned Regulator Plug.
>
> Figure 2, New Lubricating Oil Pump with Threaded Regulator Plug.
>
> **Production Status**
>
> | Table 1, Production Information |  |  |
> |---|---|---|
> | ESN First | Build Date 1 | Plant |
> | 80137579 | 14 January 2019 | Jamestown Engine Plant |
> | 1 Engine build date can be found on engine dataplate. |  |  |
>
> **Publications Affected**
>
> | Table 2, Updated Service Procedures |  |  |  |  |  |
> |---|---|---|---|---|---|
> | Manual Type | Description | Bulletin Number | Procedure Title | Procedure | Section |
> | Service Manual | Signature, ISX and QSX15 | [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]] | Lubricating Oil Pump | Refer to Procedure 007-031 | 7 |
> | ISX15 CM2250 | 4022250 |  |  |  |  |
> | QSX15 CM2250 | 2883557 |  |  |  |  |
> | ISX15 CM2350 X101 | 4310641 |  |  |  |  |
> | Power Gen QSX15 CM2250 ECF | 4310661 |  |  |  |  |
> | Power Gen QSX15 CM2250 | 4310664 |  |  |  |  |
> | ISX15 CM2250 SN | 4310736 |  |  |  |  |
> | QSX15 CM2350 X105 | 4332667 |  |  |  |  |
> | QSX15 CM2350 X106 | 4332712 |  |  |  |  |
> | QSX15 CM2250 X115 | 4388739 |  |  |  |  |
> | X15 CM2350 X116B | 5411186 |  |  |  |  |
> | QSX15 CM2350 X118 | 5467247 |  |  |  |  |
> | QSX15 CM2350 X118 | 5467249 |  |  |  |  |
>
> | Table 3, Updated Lubricating Oil System Specifications |  |  |  |
> |---|---|---|---|
> | Manual Type | Description | Bulletin Number | Procedure |
> | Service Manual | Signature, ISX and QSX15 | [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]] | 018-017 |
> | ISX15 CM2250 | 4022250 |  |  |
> | QSX15 CM2250 | 2883557 |  |  |
> | ISX15 CM2350 X101 | 4310641 |  |  |
> | Power Gen QSX15 CM2250 ECF | 4310661 |  |  |
> | Power Gen QSX15 CM2250 | 4310664 |  |  |
> | ISX15 CM2250 SN | 4310736 |  |  |
> | QSX15 CM2350 X105 | 4332667 |  |  |
> | QSX15 CM2350 X106 | 4332712 |  |  |
> | QSX15 CM2250 X115 | 4388739 |  |  |
> | X15 CM2350 X116B | 5411186 |  |  |
> | QSX15 CM2350 X118 | 5467247 |  |  |
> | QSX15 CM2250 ECF | 2883560 |  |  |
> | Operations and Maintenance Manual | Signature TM /ISX | [[3666251 — Signature and ISX Operation and Maintenance Manual\|3666251]] |  |
> | ISX15 CM2250 | 2883361 |  |  |
> | QSX15 Industrial and Power Generation | [[3666423 — QSX15 Operation and Maintenance Manual\|3666423]] |  |  |
> | ISX15 CM2350 X101 | 4310640 |  |  |
> | PowerGen QSX15 CM2250 ECF | 4310663 |  |  |
> | PowerGen QSX15 CM2250 | 4310666 |  |  |
> | ISX15 CM2250 SN | 4310735 |  |  |
> | QSX15 CM2350 X105 | 4332668 |  |  |
> | QSX15 CM2350 X106 | 4332713 |  |  |
> | QSX15 CM2250 X115 | 4388740 |  |  |
> | X15 CM2350 X116B - Performance Series | 5411187 |  |  |
> | QSX15 CM2350 X118 | 5467248 |  |  |
> | QSX15 CM2250 ECF | 2883559 |  |  |
> | Owner's Manual | Signature TM /ISX | [[4960314 — ISX Owners Manual\|4960314]] |  |
> | ISX15 CM2250 | 2883360 |  |  |
> | QSX15 Industrial and Power Generation | [[4915540 — QSX15 Owners Manual\|4915540]] |  |  |
> | ISX15 CM2350 X101 | 4310639 |  |  |
> | PowerGen QSX15 CM2250 ECF | 4310662 |  |  |
> | PowerGen QSX15 CM2250 | 4310665 |  |  |
> | ISX15 CM2250 SN | 4310734 |  |  |
> | QSX15 CM2350 X105 | 4332669 |  |  |
> | QSX15 CM2350 X106 | 4332714 |  |  |
> | QSX15 CM2250 X115 | 4388741 |  |  |
> | X15 CM2350 X114B - Efficiency Series, X15 CM2350 X116B - Performance Series | [[5411183 — X15 CM2350 X114B - Efficiency Series and X15 CM2350 X116B - Performance Series Owners\|5411183]] |  |  |
> | QSX15 CM2350 X118 | 5467249 |  |  |
>
> ### Document History
