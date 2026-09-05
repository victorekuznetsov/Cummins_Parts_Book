---
type: "TSB"
doc: "tsb101032"
title_en: "Boost Pressure Sensor Adapter Harness Resulting in Fault Codes 122/123"
modified: "2015-07-09"
engines:
  - "85017333"
families:
  - "QSK23"
parts:
  - "4096901"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101032.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101032.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK23"
  - "перевод/машинный"
---

# Boost Pressure Sensor Adapter Harness Resulting in Fault Codes 122/123

> [!abstract] TSB · `tsb101032`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Даты:** изменён 2015-07-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101032.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101032.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Усилить датчик давления Адаптер проводов ремня, в результате чего коды 122/123

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Проблема**

Клиенты сообщили о низкой мощности или прерывистой низкой мощности вместе с контрольной лампой двигателя. Устранение неполадок позволяет обнаружить несколько записей кодов 122 и 123 ошибок. Двигатели, которые видели проблему, имеют датчик давления наддува и адаптерную проводку, установленную в сборке, часть 4096902.

**Затронутая продукция**

- QSK23 CM500

**Проверка**

Вышеупомянутый вопрос относится к двигателям с датой сборки двигателя до 29 июля 2010 года.

Двигатели с датой сборки после 29 июля 2010 года с меньшей вероятностью будут испытывать проблему, описанную выше, потому что эти двигатели имеют следующие детали, которые были выпущены в производство для предотвращения кодов неисправностей датчика давления.

- Проводная проводная упряжка двигателя, часть номер[[4096901]]
- Усилить датчик давления и адаптер проводов жгута сборки, номер детали 4096902 (рисунок 1)

3-контактный разъем DeutschTM включается в комплект с датчиком давления наддува и адаптерной проводкой, чтобы обеспечить подключение к основной проводах двигателя.

![[19r99307.png]]

Рисунок 1 Наращивание датчика давления и адаптера проводов сборки, номер детали 4096902

1. 3-контактный DeutschTM Connector и проводная упряжка.
2. Расположение ленты между адаптерной проводкой и датчиком давления.
3. Датчик давления, номер детали 3408589.

**Решение**

Части в Таблице 1 были выпущены в производство для предотвращения кодов неисправностей датчика давления. Части были выпущены согласно Таблице 2.

| Таблица 1, Выпущенные части |  |
|---|---|
| Номер детали | Часть описание |
| 4096902 | Усилить датчик давления и адаптер проводов жгута сборки |
| 4096903 | Адаптерная проводка жгута номер детали |
| [[4096901]] | Упряжка для проводов двигателя (заменяет упряжку для проводов двигателя, номер детали 4096634) |

| Таблица 2, Информация о производстве |  |
|---|---|
| Серийный номер двигателя (ESN) | Дата постройки |
| 00321406 | 29 июля 2010 |

Для двигателей с датой сборки двигателя до 29 июля 2010 года должны быть выполнены следующие шаги.

**Решение 1**

Для полевого обслуживания можно избежать замены жгута проводов двигателя, отрезав текущий разъем PackardTM на жгуте проводов двигателя и сплайсируя на его месте новый разъем типа подключаемой кабины DeutschTM. Для этого раствора следует использовать части в Таблице 3.

| Таблица 3, Решение 1 Части |  |
|---|---|
| Номер детали | Часть описание |
| 4096902 | Сборка датчиков и адаптерная проводка жгута |
| 3164509 | 3 Pin DeutschTM разъем (штыревой) |

Для помощи в методах сплайсинга используйте следующую процедуру в руководстве по устранению неполадок и ремонту электронной системы управления QSK19, QSK23, QSK45, QSK60 и QSK78, в бюллетене [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R\|3666113]].[[99-019-206 — Deutsch DTM and DTP Connector Series|См. процедуру 019-206 в разделе 19.]]

При замене разъема PackardTM пометьте каждый провод идентификатором терминала (A, B и C) и где провод соединен перед удалением из разъема PackardTM. Терминалы обозначены на задней стороне разъема PackardTM, как показано на рисунке 2.

![[19h00001.png]]

Рисунок 2, Идентификация терминала на PackardTM Connector.

**Решение 2**

Если датчик давления наддува и адаптерный узел электропроводки, Часть Номер 4096902, не доступны, детали в Таблице 4 могут быть использованы для сборки прыгунной электропроводки для подключения к датчику давления наддува, Часть Номер 3408589.

- Прикрепить 3-контактный разъем разъема DeutschTM (рисунок 3, пункт С) к 3-контактному разъему PackardTM (рисунок 3, пункт В).
- Включить разъем 3 pin PackardTM в датчик давления наддува (рисунок 3, пункт А).
- Теплоусадочный уплотнитель должен быть применен вокруг электропроводки и подключения датчика для предотвращения движения.

![[19r99308.png]]

Рисунок 3, Жумпер проводка жгут и повысить давление датчик

| Таблица 4, Решение 2 Части |  |  |
|---|---|---|
| Вызов | Номер детали | Часть описание |
| А. | 3408589 | Повысить давление сенсора |
| B | 3824256 | 3-контактный разъем PackardTM |
| C | 3163256 | 3 Pin DeutschTM разъем (гнездовой) |
| D | 3164509 | 3-контактный разъем DeutschTM (штыревой) (**только** необходим, если двигатель не имеет электропроводки, часть номер)[[4096901]]) |

### История изменений документа

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[4096901]] | WIRING HARNESS | Жгут проводов |

> [!quote]- Original (English) · английский оригинал
> ## Boost Pressure Sensor Adapter Harness Resulting in Fault Codes 122/123
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Issue**
>
> Customers have reported low power or intermittent low power along with a check engine lamp. Troubleshooting the issue finds multiple records of fault codes 122 and 123. Engines that have seen the issue have boost pressure sensor and adapter harness assembly, part number 4096902, installed.
>
> **Product Affected**
>
> - QSK23 CM500
>
> **Verification**
>
> The issue highlighted above applies to engines with an engine build date prior to 29 July 2010.
>
> Engines with a build date after 29 July 2010 are less likely to experience the issue highlighted above because these engines have the following parts that were released into production to prevent boost pressure sensor fault codes.
>
> - Engine wire harness, Part Number [[4096901]]
> - Boost pressure sensor and adapter harness assembly, Part Number 4096902 (Figure 1)
>
> A 3 pin Deutsch™ connector is included with the boost pressure sensor and adapter harness assembly to allow connection to the main engine harness.
>
> Figure 1, Boost Pressure Sensor and Adapter Harness Assembly, Part Number 4096902
>
> 1. 3 pin Deutsch™ Connector and harness.
> 2. Tape location between adapter harness and boost pressure sensor.
> 3. Boost pressure sensor, Part Number 3408589.
>
> **Resolution**
>
> The parts in Table 1 were released into production to prevent boost pressure sensor fault codes. The parts were released according to Table 2.
>
> | Table 1, Parts Released |  |
> |---|---|
> | Part Number | Part Description |
> | 4096902 | Boost pressure sensor and adapter harness assembly |
> | 4096903 | Adapter harness part number |
> | [[4096901]] | Engine wiring harness (replaces engine wiring harness, Part Number 4096634) |
>
> | Table 2, Production Information |  |
> |---|---|
> | Engine Serial Number (ESN) First | Build Date |
> | 00321406 | 29 July 2010 |
>
> For engines with an engine build date prior to 29 July 2010, the steps below should be performed.
>
> **Solution 1**
>
> For field service, it is possible to avoid replacing the engine wiring harness by cutting off the current Packard™ connector on the engine harness and splicing a new male Deutsch™ connector in its place. For this solution, the parts in Table 3 should be used.
>
> | Table 3, Solution 1 Parts |  |
> |---|---|
> | Part Number | Part Description |
> | 4096902 | Sensor assembly and adapter harness |
> | 3164509 | 3 Pin Deutsch™ connector (male) |
>
> For assistance with splicing methods, use the following procedure in the QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R\|3666113]]. [[99-019-206 — Deutsch DTM and DTP Connector Series|Refer to Procedure 019-206 in Section 19.]]
>
> When replacing the Packard™ connector, tag each wire with the terminal identification (A, B, and C) and where the wire is connected before removing from the Packard™ connector. The terminals are marked on the backside of the Packard™ connector, as shown in Figure 2.
>
> Figure 2, Terminal Identification on Packard™ Connector.
>
> **Solution 2**
>
> If the boost pressure sensor and adapter harness assembly, Part Number 4096902, is **not** available, the parts in Table 4 can be used to assemble a jumper harness to connect to boost pressure sensor, Part Number 3408589.
>
> - Attach 3 pin Deutsch™ female connector (Figure 3, Item C) to the 3 pin Packard™ connector (Figure 3, Item B).
> - Insert the 3 pin Packard™ connector into boost pressure sensor (Figure 3, Item A).
> - Heat shrink **must** be applied around the harness and sensor connection to prevent movement.
>
> Figure 3, Jumper Harness and Boost Pressure Sensor
>
> | Table 4, Solution 2 Parts |  |  |
> |---|---|---|
> | Callout | Part Number | Part Description |
> | A | 3408589 | Boost Pressure Sensor |
> | B | 3824256 | 3 pin Packard™ connector |
> | C | 3163256 | 3 Pin Deutsch™ connector (female) |
> | D | 3164509 | 3 pin Deutsch™ connector (male) (**only** needed if engine does **not** have engine wiring harness, Part Number [[4096901]]) |
>
> ### Document History
