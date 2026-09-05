---
aliases:
  - "QST30 работает только на одном ряду, активен код 166"
type: "TSB"
doc: "tsb101121"
title_en: "QST30 Only Runs on One Bank and Fault Code 166 is Active."
title_ru: "QST30 работает только на одном ряду, активен код 166"
released: "2011-01-06"
modified: "2011-01-06"
group: "19 - Electronic Engine Controls"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101121.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101121.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2011"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# QST30 Only Runs on One Bank and Fault Code 166 is Active.
**QST30 работает только на одном ряду, активен код 166**

> [!abstract] TSB · `tsb101121`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2011-01-06 · изменён 2011-01-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101121.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101121.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## QST30 работает только на одном ряду, активен код 166

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

Проблема:

При запуске двигателя QST30 он активирует неисправность 166 и **только **работает на одном берегу, если обнаружен всплеск напряжения от CM552 ECM. Когда это происходит, двигатель обычно работает на правом берегу **только**.

Проверка/подтверждение:

Подтвердите, что код 166 ошибки активен и что двигатель работает только на одном банке.

Решение:

В упряжку для проводов двигателя левого берега был добавлен резистор, чтобы предотвратить активацию кода 166 по умолчанию и работу двигателя на одном берегу, если происходит всплеск напряжения от CM552 ECM.

Проверьте, есть ли резистор, установленный между положением стойки общего провода и земли на берегу, который не стреляет. Смотрите прилагаемые фигуры для локаций резисторов. Если резистор не найден, установите резистор в электропроводку или замените электропроводку. См. схему проводов для идентификации местоположения штифта. Если найден резистор, проверьте сопротивление.

- Для приложений для выработки электроэнергии используйте следующую процедуру в руководстве по устранению неполадок и ремонту системы электронного управления QST30 CM850 Power Generation Interface Engine Electronic Control System, Bulletin [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti\|4021674]].[[60-019-043 — Engine Wiring Harness|См. процедуру 019-043 в разделе 19.]]
- Для промышленных применений используйте следующую процедуру в руководстве по устранению неполадок и ремонту промышленной электронной системы управления QST30, в бюллетене [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual\|3666214]] для инструкций по проверке сопротивления.[[87-019-043 — Engine Wiring Harness|См. процедуру 019-043 в разделе 19.]]

В приведенных ниже таблицах кратко излагаются изменения в ремне электропроводки двигателя:

| **QST30 CM552 Промышленные одноплитовые электропроводные упряжки Двигатели** | **Номера деталей** | **Дата начала или начала реализации проекта** |
|---|---|---|
| Один резистор Ом 2,2k (только правый берег) | 4975508 | 3 августа 2009 года |
| Два резистора 2,2k Ohm | 4975755 | 37247268 |

| **Интерфейс QST30 CM850 для генерации электроэнергии** | **Номера деталей** | **Дата начала или начала реализации проекта** |
|---|---|---|
| Один резистор Ом 2,2k (только правый берег) | 4975505 | 25 мая 2009 года |
| Два резистора Ом 2,2k с 12-вольтным реле топливного насоса | 2881121 | 13 декабря 2009 года |
| Два резистора Ом 2,2k с 24-вольтным реле топливного насоса | 4975747 | 37245679 |
| Два резистора Ом 1,3к с 24-вольтным реле топливного насоса | 4975760 | 37246974 |

![[19f00008.png]]

![[19f00009.png]]

![[19f00006.png]]

![[19f00007.png]]

Рисунок 1: Местонахождение резистора для левобережья QST30

Рисунок 2: Местонахождение резистора для промышленного банка QST30

Рисунок 3: Место диссертации для QST30 Power Generation Interface

Рисунок 4: Место диссертации для QST30 Power Generation Interface Right Bank

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## QST30 Only Runs on One Bank and Fault Code 166 is Active.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> Issue:
>
> When starting a QST30 engine it will activate fault 166 and **only** run on one bank if a voltage spike from the CM552 ECM is detected. When this occurs, the engine commonly runs on the right bank **only**.
>
> Verification / Confirmation:
>
> Confirm that Fault Code 166 is active and that the engine is **only** running on one bank.
>
> Resolution:
>
> A resistor has been added to the left bank engine wiring harness to prevent Fault Code 166 from becoming active and the engine from running on one bank if a voltage spike from the CM552 ECM occurs.
>
> Check to see if there is a resistor installed between the rack position common wire and ground on the bank that is **not** firing. See the attached figures for resistor locations. If a resistor is **not** found, install a resistor in the wiring harness or replace the wiring harness. Refer to the wiring diagram for the pin location identification. If a resistor is found, check the resistance.
>
> - For power generation applications, use the following procedure in the QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooting and Repair Manual, Bulletin [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti\|4021674]]. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
> - For industrial applications, use the following procedure in the QST30 Industrial Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual\|3666214]] for resistance check instructions. [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
>
> The tables below summarize changes to the engine wiring harness:
>
> | **QST30 CM552 Industrial One-Piece Harness Engines** | **Part Number** | **ESN First or Plant Implementation Date** |
> |---|---|---|
> | One 2.2k Ohm Resistor (right bank **only**) | 4975508 | 3-August-2009 |
> | Two 2.2k Ohm Resistors | 4975755 | 37247268 |
>
> | **QST30 CM850 Power Generation Interface Engines** | **Part Number** | **ESN First or Plant Implementation Date** |
> |---|---|---|
> | One 2.2k Ohm Resistor (right bank **only**) | 4975505 | 25-May-2009 |
> | Two 2.2k Ohm Resistors with 12 Volt Fuel Pump Relay | 2881121 | 13-December-2009 |
> | Two 2.2k Ohm Resistors with 24 Volt Fuel Pump Relay | 4975747 | 37245679 |
> | Two 1.3k Ohm Resistors with 24 Volt Fuel Pump Relay | 4975760 | 37246974 |
>
> Figure 1: Resistor Location for QST30 Industrial Left Bank
>
> Figure 2: Resistor Location for QST30 Industrial Right Bank
>
> Figure 3: Resistor Location for QST30 Power Generation Interface Left Bank
>
> Figure 4: Resistor Location for QST30 Power Generation Interface Right Bank
>
> ### Document History
