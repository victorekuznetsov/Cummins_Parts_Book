---
aliases:
  - "Требование стендовой калибровки модуля CENSE™ CM2330"
type: "TSB"
doc: "tsb150029"
title_en: "Next Generation CENSE™ Module CM2330 Bench Calibration Requirement"
title_ru: "Требование стендовой калибровки модуля CENSE™ CM2330"
released: "2015-03-12"
modified: "2015-03-12"
group: "19 - Electronic Engine Controls"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33224404"
  - "33239746"
  - "33239899"
  - "41340468"
families:
  - "K38/K50 · QSK38, QSK50"
  - "QSK50"
  - "QSK60"
  - "QSK60 CM2150 MCRS"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150029.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150029.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK50"
  - "двигатель/QSK60"
  - "двигатель/QSK60CM2150MCRS"
  - "год/2015"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# Next Generation CENSE™ Module CM2330 Bench Calibration Requirement
**Требование стендовой калибровки модуля CENSE™ CM2330**

> [!abstract] TSB · `tsb150029`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK50, QSK60, QSK60 CM2150 MCRS
> **Даты:** выпущен 2015-03-12 · изменён 2015-03-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150029.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150029.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Требование стендовой калибровки модуля CENSE™ CM2330

### Суть проблемы

Модуль CM2330 следующего поколения CENSETM, поставляемый дистрибьюторами Cummins®, не имеет соответствующей калибровки. Клиенты, которые не имеют электронных инструментов обслуживания INSITETM с подпиской Pro уровня, не могут установить необходимую калибровку CM2330 модуля Next Generation CENSETM, что может привести к длительному простою.

### Подтверждение

**Пострадал продукт: **Все двигатели повышенной мощности с использованием CENSETM следующего поколения CM2330

Клиенты, которые самостоятельно обслуживают свои устройства, ранее могли устанавливать калибровки на новые модули CM530 CENSETM, используя INSITETM для электронного сервисного инструментария CENSETM.

Калибровка CENSETM Module CM2330 следующего поколения может быть установлена с помощью **только** электронного сервисного инструментария INSITETM с подпиской уровня Pro со стандартным адаптером INLINETM через разъем для разъема службы J1939. См. TSB130133.

### Решение

Дистрибьюторы и дилеры Cummins® должны информировать клиентов, предоставляющих услуги самообслуживания, о требовании иметь электронный сервис INSITETM с подпиской уровня Pro для установки калибровок на модулях CM2330 следующего поколения CENSETM.

Если клиенты не имеют доступа к электронному сервисному оборудованию INSITETM с подпиской Pro уровня, калибровка модуля CM2330 следующего поколения CENSETM должна быть установлена до того, как клиент получит модуль CM2330 следующего поколения CENSETM.

Калибровка испытательного стенда CM2330 следующего поколения CENSETM возможна с использованием модуля управления двигателем (ECM) испытательного стенда калибровочной проводов ремня Cummins®, номер детали 5298707. См. Инструкцию по обслуживанию инструментария № 3377791-22.

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Next Generation CENSE™ Module CM2330 Bench Calibration Requirement
>
> ### Core Issue
>
> The Next Generation CENSE™ Module CM2330 supplied by Cummins® distribution and dealers does **not** have the appropriate calibration installed. Self-servicing customers without INSITE™ electronic service tool with a Pro level subscription are **not** able to install the required Next Generation CENSE™ Module CM2330 calibration, which may result in extended downtime.
>
> ### Confirmation
>
> **Product Affected:** All High Horsepower Engines Using Next Generation CENSE™ Module CM2330
>
> Self-servicing customers were previously able to install calibrations on new replacement CM530 CENSE™ Modules using INSITE™ for CENSE™ electronic service tool.
>
> The Next Generation CENSE™ Module CM2330 calibration can be installed using **only** INSITE™ electronic service tool with a Pro level subscription with the standard INLINE™ adapter via the J1939 service connector socket. See TSB130133.
>
> ### Resolution
>
> Cummins® distribution and dealers should inform self-servicing customers of the requirement to have INSITE™ electronic service tool with a Pro level subscription to install calibrations on Next Generation CENSE™ Modules CM2330.
>
> If customers do **not** have access to INSITE™ electronic service tool with a Pro level subscription, the Next Generation CENSE™ Module CM2330 calibration will need to be installed prior to the customer taking possession of Next Generation CENSE™ Module CM2330.
>
> The Next Generation CENSE™ Module CM2330 bench calibration is possible using the engine control module (ECM) bench calibration harness, Cummins® part number 5298707. See Service Tool Instruction Number 3377791-22.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Document History
