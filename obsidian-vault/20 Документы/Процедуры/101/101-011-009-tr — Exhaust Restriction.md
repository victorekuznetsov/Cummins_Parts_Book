---
aliases:
  - "Сопротивление выпускной системы"
type: "Процедура"
doc: "101-011-009-tr"
title_en: "Exhaust Restriction"
title_ru: "Сопротивление выпускной системы"
modified: "2012-11-21"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-011-009-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-011-009-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/101"
  - "перевод/машинный"
---

# Exhaust Restriction
**Сопротивление выпускной системы**

> [!abstract] Процедура · `101-011-009-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 11 - Exhaust System - Group 11
> **Даты:** изменён 2012-11-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-011-009-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-011-009-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Для двигателей CM871 и CM876 удалите датчик температуры выхлопных газов после обработки из впуска после обработки и отсоедините его от проводной ремни. Установите адаптер калибра давления, номер детали 4918576. Подсоедините манометр или калибр давления, номер детали ST-1273, к адаптеру калибра давления.

Защитите шланг от жары. Используйте 305 мм \[12 в \] минимальную длину металлической трубки, ведущей от соединения выхлопной трубы.

> [!note] Примечание
> Отключение датчика температуры входного входа DOC после обработки вызовет код поломки 1666. не устраняйте неисправности кода во время этого измерения ограничения выхлопных газов.

![[11d00112.png]]

Работайте с двигателем при номинальной оборотах и нагрузке. Запишите показания на манометр.

| Сопротивление выпускной системы |  |  |  |  |
|---|---|---|---|---|
|  | хг | в хг | в ч 2 o |  |
| Без послеоперационного лечения | Макс | 75.0 | 3.0 | 40.8 |
| После лечения | Макс | 305.0 | 12.0 | 163.3 |

![[pe200kb.png]]

Если давление выхлопных газов превышает технические характеристики, проверьте трубопроводы выхлопных газов на предмет повреждения. См. руководство изготовителя машины по диагностике и ремонту.

Если транспортное средство оснащено системой послеоперационной обработки, проверьте систему послеоперационной обработки на наличие DPF и/или DOC послеоперационной заглубленной системы.

Расширенная работа двигателя с высоким ограничением выхлопных газов может привести к повреждению уплотнений масла турбокомпрессора. Используйте следующую процедуру для проверки турбокомпрессора на прогрессирующее повреждение.[[10-010-033-tr — Turbocharger|См. процедуру 010-033 Iin Section 10.]]

![[pe200kc.png]]

Удалите испытательное оборудование и установите датчик температуры впуска DOC после обработки. Управляйте двигателем и проверяйте, что все коды неисправностей неактивны.

![[11d00112.png]]

### Подготовительные операции

- По возможности, выполняйте стационарную регенерацию, чтобы убедиться, что последующая обработка чиста до проведения испытания на ограничение выхлопных газов.[[101-014-013-tr — Aftertreatment Testing|См. процедуру 014-013 в разделе 14.]]

> [!note] Примечание
> Некоторые коды неисправностей могут препятствовать запуску/завершению стационарной регенерации. Если это так, то переходим к следующему шагу.

![[ck800wa.png]]

### Измерение

Удалите датчик температуры выхлопных газов после обработки. См. процедуру 019-449 в разделе 19.

Установите адаптер калибра давления, номер детали 4918576.

Подсоедините манометр или калибр давления, номер детали ST-1273, к адаптеру калибра давления.

Защитите шланг от жары. Используйте 305 мм \[12 в \] минимальную длину металлической трубки, ведущей от соединения выхлопной трубы.

> [!note] Примечание
> Отключение датчика температуры входного отверстия DOC после обработки вызовет код 3314 по умолчанию. Не устранять неисправности кода во время этой процедуры ограничения выхлопных газов.

![[11d00112.png]]

> [!note] Примечание
> Для достижения точного испытания на ограничение выхлопных газов убедитесь, что перед проведением испытания на ограничение выхлопных газов была проведена стационарная регенерация.

Управляйте двигателем с номинальной скоростью и нагрузкой и записывайте ограничение выхлопных газов. См. процедуру 018-020 в разделе V.

![[pe200kb.png]]

Если ограничение выхлопных газов превышает технические характеристики, проверьте трубопроводы выхлопных газов на предмет повреждения. См. сервисное руководство изготовителя машины.

Если ограничение на выхлоп превышает технические характеристики:

1. Проверьте наличие заглушенного фильтра для дизельных частиц (DPF).
2. Проверьте наличие DOC.
3. Проверить наличие поврежденной или ограниченной селективной каталитической редукционной (SCR) трубки разложения и катализатора SCR.

Расширенная работа двигателя с высоким ограничением выхлопных газов может привести к повреждению уплотнений масла турбокомпрессора. Используйте следующую процедуру для проверки турбокомпрессора на прогрессирующее повреждение. См. процедуру 010-033 в разделе 10.

![[pe200kc.png]]

### Завершающие операции

- Удалите испытательное оборудование и установите датчик температуры выхлопных газов после обработки. См. процедуру 019-449 в разделе 19.
- Управляйте двигателем и проверяйте, что все коды неисправностей неактивны.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> For CM871 and CM876 engine remove the aftertreatment exhaust gas temperature sensor from the aftertreatment inlet and disconnect it from the wiring harness. Install the pressure gauge adapter, Part Number 4918576. Connect a manometer or pressure gauge, Part Number ST-1273, to the pressure gauge adapter.
>
> Protect the hose from heat. Use a 305 mm \[12 in\] minimum length of metal tubing leading from the exhaust pipe connection.
>
> **Note · Примечание**
> Disconnecting the aftertreatment DOC inlet temperature sensor will trigger Fault Code 1666. Do **not** troubleshoot this fault code during this exhaust restriction measurement.
>
> Operate the engine at rated rpm and load. Record the reading on the manometer.
>
> | Exhaust Restriction |  |  |  |  |
> |---|---|---|---|---|
> |  | mm-hg | in-hg | in-h 2 o |  |
> | Without Aftertreatment | MAX | 75.0 | 3.0 | 40.8 |
> | With Aftertreatment | MAX | 305.0 | 12.0 | 163.3 |
>
> If the exhaust pressure exceeds the specifications, inspect the exhaust piping for damage. Refer to the OEM troubleshooting and repair manual.
>
> If the vehicle is equipped with an aftertreatment system, inspect the aftertreatment system for a plugged aftertreatment DPF and/or a plugged aftertreatment DOC.
>
> Extended engine operation with high exhaust restriction can lead to damaged turbocharger oil seals. Use the following procedure to inspect the turbocharger for progressive damage. [[10-010-033-tr — Turbocharger|Refer to Procedure 010-033 Iin Section 10.]]
>
> Remove the test equipment and install the aftertreatment DOC inlet temperature sensor. Operate the engine and verify that all fault codes are inactive.
>
> ### Preparatory Steps
>
> - Perform a stationary regeneration, if possible, to make sure the aftertreatment is clean prior to performing the exhaust restriction test. [[101-014-013-tr — Aftertreatment Testing|Refer to Procedure 014-013 in Section 14.]]
>
> **Note · Примечание**
> Some fault codes may prevent a stationary regeneration from being started/completed. If that is the case, move on to the next step.
>
> ### Measure
>
> Remove the aftertreatment exhaust gas temperature sensor. Refer to Procedure 019-449 in Section 19.
>
> Install the pressure gauge adapter, Part Number 4918576.
>
> Connect a manometer or pressure gauge, Part Number ST-1273, to the pressure gauge adapter.
>
> Protect the hose from heat. Use a 305 mm \[12 in\] minimum length of metal tubing leading from the exhaust pipe connection.
>
> **Note · Примечание**
> Disconnecting the aftertreatment DOC inlet temperature sensor will trigger Fault Code 3314. Do **not** troubleshoot this fault code during this exhaust restriction procedure.
>
> **Note · Примечание**
> To achieve an accurate exhaust restriction test, be sure a stationary regeneration was performed prior to conducting the exhaust restriction test.
>
> Operate the engine at rated speed and load and record the exhaust restriction. Refer to Procedure 018-020 in Section V.
>
> If the exhaust restriction exceeds the specifications, inspect the exhaust piping for damage. Refer to the OEM service manual.
>
> If the exhaust restriction exceeds the specifications:
>
> 1. Check for a plugged aftertreatment diesel particulate filter (DPF).
> 2. Check for a plugged DOC.
> 3. Check for a damaged or restricted selective catalytic reduction (SCR) decomposition tube and SCR catalyst.
>
> Extended engine operation with high exhaust restriction can lead to damaged turbocharger oil seals. Use the following procedure to inspect the turbocharger for progressive damage. Refer to Procedure 010-033 in Section 10.
>
> ### Finishing Steps
>
> - Remove the test equipment and install the aftertreatment exhaust gas temperature sensor. Refer to Procedure 019-449 in Section 19.
> - Operate the engine and verify that all fault codes are inactive.
