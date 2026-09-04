---
aliases:
  - "Устранение проблем с калибровкой"
type: "TSB"
doc: "tsb110297"
title_en: "Calibration Issue Resolution"
title_ru: "Устранение проблем с калибровкой"
released: "2011-10-28"
modified: "2011-11-07"
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
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110297.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110297.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK50"
  - "двигатель/QSK60"
  - "двигатель/QSK60CM2150MCRS"
  - "год/2011"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# Calibration Issue Resolution
**Устранение проблем с калибровкой**

> [!abstract] TSB · `tsb110297`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK50, QSK60, QSK60 CM2150 MCRS
> **Даты:** выпущен 2011-10-28 · изменён 2011-11-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110297.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110297.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Устранение проблем с калибровкой

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

Проблема заключается в том, что при устранении неполадок электронного модуля управления (ECM) при установке новой калибровки или ECM потенциально определяется проблема калибровки. Стандартные деревья устранения неполадок исчерпаны до того, как будет определена первопричина.

Для проверки будут верны следующие утверждения:

1. Существующий или заменяющий модуль был загружен калибровкой, которая ранее не была установлена.
2. Возникает новая проблема, которая была **не** при использовании предыдущего модуля или калибровке.
3. Уже проверено, что установленная калибровка подходит для двигателя, оборудования и применения.

Используйте следующее для разрешения.

1. Установите, правильно ли работает подозреваемая функция, создающая проблему. Ссылка на соответствующую процедуру 101-007 «Электронная контролируемая топливная система» в разделе F соответствующего руководства по устранению неполадок и ремонту электронной системы управления на QuickServeTM Online (QSOL) или в инструменте электронного обслуживания INSITETM «Информационная система неисправностей» (рисунки 1 и 2) для получения дополнительной информации.

![[19e01007.png]]

Рисунок 1

- INSITETM (Особенности и параметры), выберите Индекс деревьев неисправностей

.

![[19e01008.png]]

Рисунок 2

- Выберите систему электронного топлива (101-007) для двигателя.

Аналогичным образом, просмотрите раздел «Настраиваемые функции двигателя» для файлов помощи электронного сервиса INSITETM, чтобы определить, вызвана ли предполагаемая ошибка неправильно установленной регулируемой функцией двигателя. Ссылка на рисунки 3 и 4.

![[19e01009.png]]

Рис. 3

- INSITETM (Особенности и параметры), выберите содержимое.

![[19e01010.png]]

Рис. 4

- Выберите Настраиваемые функции двигателя.

2. Используйте QSOL для проверки истории калибровки. Справочные рисунки 5 и 6 для следующего:

1. Войдите в QSOL
2. Выберите «Мое приложение»
3. Выберите «ECM калибровочные изменения»
4. Введите калибровочный код и выберите «Поиск»
5. Просмотрите информацию о калибровке.

![[19e01011.png]]

Рис. 5

- Выполняйте шаги с 1 по 3.

![[19e01012.png]]

Рис.

- Выполняйте шаги 4 и 5.

История калибровочных ревизий содержит информацию об изменениях, вносимых в калибровку каждый раз, когда выпускается новая редакция. Эта информация может быть использована для установления, существует ли общность между изменениями, внесенными в калибровку, и наблюдаемыми симптомами, что помогает определить, существует ли проблема калибровки.

> [!note] Примечание
> История калибровочного пересмотра также может быть загружена в формате Excel, нажав «Справочник» в поле фильтра записи.

3. Проведите необходимые исследования, чтобы проверить, испытывается ли известная проблема, и требуются ли конкретные шаги по устранению неполадок, ремонту и отчетности.

4. Если с помощью вышеуказанных шагов невозможно выявить проблему, то для ее включения в цепочку технической эскалации необходимо собрать следующую информацию:

1. Специфика двигателя (серийный номер двигателя (ESN), приложение, рейтинг, часы работы двигателя, история технического обслуживания и т. Д.)
2. Коды ECM (коды до и после, включая номера изменений, будут необходимы)
3. Изображения ECM (до и после калибровки)
4. Журналы данных (существующие предварительно определенные группы параметров можно найти в инструменте электронного обслуживания INSITETM, в противном случае используйте соответствующую схему проводов для определения того, имеют ли несколько цепей общий источник питания и/или наземные или контрольные параметры, которые логически были бы связаны, например. Состояние топлива пользователя, скорость двигателя, командное давление на топливных рельсах, измеренное давление на топливных рельсах и т. Д.

> [!note] Примечание
> Чем больше число параметров, тем медленнее скорость, с которой они могут быть зарегистрированы. Поэтому регистрирует минимальное количество параметров, если важна частота выборки.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Calibration Issue Resolution
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> The issue is, during troubleshooting of the electronic control module (ECM), a calibration issue is potentially identified when a new calibration or ECM is installed. Standard troubleshooting trees are exhausted before the root cause is determined.
>
> For verification, the following statements will be true:
>
> 1. The existing or replacement module has just been loaded with a calibration which was **not** previously installed.
> 2. A new issue is experienced, which was **not** present when using the previous module or calibration.
> 3. It has already been verified that the installed calibration is appropriate for the engine, equipment, and application.
>
> Use the following for resolution.
>
> 1. Establish if the suspected feature creating the problem is operating correctly. Reference the relevant “Electronic Controlled Fuel System” procedure 101-007 in Section F of the appropriate Electronic Control System Troubleshooting and Repair Manual on QuickServe™ Online (QSOL) or in INSITE™ electronic service tool, “Fault Information System” (Figures 1 and 2) for further information.
>
> Figure 1
>
> - INSITE™ - (Features and Parameters), select Fault Trees Index
>
> .
>
> Figure 2
>
> - Select the Electronic Controlled Fuel System (101-007) for the affected engine.
>
> Similarly, review INSITE™ electronic service tool help files, “Adjustable Engine Features” section to determine if the suspected error is due to an incorrectly set adjustable engine feature. Reference to Figures 3 and 4.
>
> Figure 3
>
> - INSITE™ - (Features and Parameters), select contents.
>
> Figure 4
>
> - Select Adjustable Engine Features.
>
> 2. Use QSOL to inspect the calibration revision history. Reference Figures 5 and 6 for the following:
>
> 1. Log onto QSOL
> 2. Select "My Application"
> 3. Select "ECM Calibration Revisions"
> 4. Enter the calibration code and select "Search"
> 5. Review the calibration revision information.
>
> Figure 5
>
> - Perform steps 1 through 3.
>
> Figure 6
>
> - Perform steps 4 and 5.
>
> The Calibration Revision History provides information relating to changes made to a calibration each time a new revision is released. This information can be used to establish if there is commonality between changes made to the calibration and the symptoms being observed, thus helping determine if a calibration issue exists.
>
> **Note · Примечание**
> The Calibration Revision History can also be downloaded in Excel format by clicking “Spreadsheet” in the record filter box.
>
> 3. Perform the necessary research to verify if a known issue is being experienced and whether specific troubleshooting, repair, and reporting steps are required.
>
> 4. If no issue can be identified using the above steps, the following information should be collected to allow the issue to enter the technical escalation chain:
>
> 1. Engine specifics (engine serial number (ESN), application, rating, engine hours, maintenance history, etc.)
> 2. ECM codes (the codes before and after, including the revision numbers, will be required)
> 3. ECM images (before and after calibration download)
> 4. Data logs (existing pre-defined parameter groups can be found in INSITE™ electronic service tool, otherwise use the relevant wiring diagram to identify if multiple circuits share a common supply and/or ground or monitor parameters which logically would be linked e.g. User Fuelling State, Engine Speed, Commanded Fuel Rail Pressure, Measured Fuel Rail Pressure, etc.)
>
> **Note · Примечание**
> The greater the number of parameters, the slower the rate at which they can be logged. Therefore, **only** log the minimum number of parameters if sample rate is important.
>
> ### Document History
