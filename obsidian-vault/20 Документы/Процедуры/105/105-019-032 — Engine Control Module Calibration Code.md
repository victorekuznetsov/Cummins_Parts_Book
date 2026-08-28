---
aliases:
  - "Калибровочный код ЭБУ"
type: "Процедура"
doc: "105-019-032"
title_en: "Engine Control Module Calibration Code"
title_ru: "Калибровочный код ЭБУ"
modified: "2025-08-08"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33239746"
  - "33239899"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41349633"
  - "41353297"
  - "41370103"
  - "85017333"
  - "93948840"
families:
  - "K19"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK19"
  - "QSK23"
  - "QSK60"
  - "QST30"
  - "QSZ13"
manuals:
  - "3666070"
  - "3666113"
  - "3666214"
  - "3666231"
  - "3666266"
  - "4021674"
  - "4022094"
  - "4022102"
  - "4358369"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-019-032.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/105-019-032.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "двигатель/K38/K50"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "двигатель/QSZ13"
  - "группа/105"
  - "перевод/машинный"
---

# Engine Control Module Calibration Code
**Калибровочный код ЭБУ**

> [!abstract] Процедура · `105-019-032`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** K19, K38/K50 · QSK38, QSK50, QSK60, NT/NTA855 · ISM/QSM11, QSK19, QSK23, QSK60, QST30, QSZ13
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]], [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666231 — Centinel™ Master Repair Manual|3666231]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]], [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]], [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]], [[4358369 — QSZ13 CM2150 Z102 Service Manual|4358369]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19 · Section 19 - Electronic Engine Controls — Group 19
> **Даты:** изменён 2025-08-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-019-032.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/105-019-032.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Cummins® электронный инструмент или эквивалент

#### Дополнительные сервисные позиции

- Никаких дополнительных предметов обслуживания не требуется.

### Общие сведения

> [!note] Примечание
> Из-за количества различных конфигураций модуля управления двигателем (ECM) эта процедура была написана, чтобы быть общей. Не все иллюстрации в рамках этой процедуры будут представлять собой приложение, над которым ведется работа.

Калибровку ECM можно выполнить с помощью рекомендованной электронной сервисной оснастки Cummins® или эквивалентной.

Инструменты для электронных услуг Cummins® используют процесс управления калибровкой служб (SCM), который использует базу данных вместе с дополнительной логикой для оценки того, одобрен ли запрашиваемый код ECM для установки в ECM. См. Service Bulletin, Engine Control Module (ECM) Calibration Download with Cummins® Electronic Service Tools, Bulletin 6643906.

После замены или калибровки ECM фактические часы работы двигателя / расстояние должны быть правильно введены в ECM.

Записывайте значения ECM Distance Offset, ECM Time Offset, Engine Distance Offset и Engine Time Offset перед заменой или калибровкой ECM. Эти параметры можно найти в разделе «Информация о поездке» функций и параметров.

![[19t00005.png]]

### Первичная проверка

Если инструмент будет **не*** взаимодействовать с выключателем зажигания в положении Включения, зациклите замок зажигания и попробуйте снова.

Процесс калибровки ECM происходит при включенном переключателе зажигания. Всегда следуйте инструкциям на экранах инструментов сервиса.

![[19800470.png]]

### Подготовительные операции

Подключите инструмент электронного сервиса к шине данных CAN, которая расположена на двигателе или в кабине.

После замены или калибровки ECM фактические часы работы двигателя / расстояние должны быть правильно введены в ECM.

Введите значения ECM Distance Offset, ECM Time Offset, Engine Distance Offset и Engine Time Offset перед заменой или калибровкой ECM. Эти параметры можно найти в разделе «Информация о поездке» функций и параметров.

Проверить, что одометр транспортного средства равен значению, зарегистрированному до удаления ECM. Свяжитесь с OEM-сервисом, если значения неверны.

![[19t00005.png]]

### Осмотр

Установите, правильно ли работает подозреваемая функция, создающая проблему. Ссылка на соответствующую "Электронную систему управляемого топлива" (Процедура 101-007) в разделе 1 соответствующего Руководства по эксплуатации и техническому обслуживанию.

Чтобы получить доступ к разделу «Настраиваемые функции двигателя», выберите «Справка» -> «Содержимое» из панели меню или нажмите F1 с отдельной функцией в разделе «Особенности и параметры» в инструменте электронного обслуживания.

Просмотрите раздел «Настраиваемые характеристики двигателя», чтобы определить, вызвана ли предполагаемая ошибка неправильно установленной регулируемой функцией двигателя.

![[19t00005.png]]

Используйте QuickServe Online для проверки истории пересмотра калибратона.

1. Зарегистрируйтесь в QuickServeTM Online
2. Выберите «Мои приложения»
3. Выберите «ECM Calibraton Revisions»
4. Введите калибровочный код и выберите «Поиск»
5. Просмотрите информацию о калибровке.

История калибровочных изменений содержит информацию, касающуюся изменений, вносимых в калибровку каждый раз, когда выпускается новая версия. Эта информация может быть использована для установления, существует ли общность между изменениями, внесенными в калибровку, и наблюдаемыми симптомами. Историю калибровочного пересмотра можно также загрузить в формате Excel, выбрав «Справочник» в поле фильтрации записи.

Чем больше число параметров, тем медленнее скорость, с которой они могут быть зарегистрированы. Поэтому * регистрирует минимальное количество параметров, если важна частота выборки.

Если с помощью перечисленных выше шагов не удается выявить проблему, то для ее включения в цепочку технической эскалации необходимо собрать следующую информацию:

1. Серийный номер двигателя (ESN), его применение, рейтинг, часы работы двигателя, история технического обслуживания и т. Д.
2. коды ECM (коды до и после, включая номера версий);
3. ECM изображения (до и после калибровки)
4. Журналы данных (используют существующие, предварительно определенные группы параметров или используют соответствующую схему проводов для определения того, используют ли несколько цепей общий источник питания или землю, или контролируют параметры, которые логически будут связаны - т.е. Состояние топлива пользователя, скорость двигателя, командное давление на топливных рельсах, измеренное давление на топливных рельсах и т. Д.

![[19t00005.png]]


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Cummins® electronic service tool or equivalent
>
> #### Additional Service Items
>
> - No additional service items required.
>
> ### General Information
>
> **Note · Примечание**
> Due to the number of various engine control module (ECM) configurations, this procedure has been written to be common. **Not** all illustrations within this procedure will represent the application that is being worked on.
>
> ECM calibrations can be performed by the recommended Cummins® electronic service tool or equivalent.
>
> Cummins ® electronic service tool uses a Service Calibration Management (SCM) process which uses a database along with additional logic to evaluate if a requested ECM code is approved for installation into the ECM. See Service Bulletin, Engine Control Module (ECM) Calibration Download with Cummins ® Electronic Service Tools, Bulletin [[6643906 — Engine Control Module (ECM) Calibration Download with Cummins® Electronic Service Too|6643906]].
>
> After an ECM is replaced or calibrated, the actual engine hours / distance **must** be entered correctly into the ECM.
>
> Record the values of ECM Distance Offset, ECM Time Offset, Engine Distance Offset, and Engine Time Offset prior to replacement or calibration of the ECM. These parameters can be found in the Trip Information section of Features and Parameters.
>
> ### Initial Check
>
> If the tool will **not** communicate with the keyswitch in the ON position, cycle the keyswitch and try again.
>
> The ECM calibration process occurs with the keyswitch turned ON. **Always** follow the instructions on the service tool screens.
>
> ### Preparatory Steps
>
> Connect the electronic service tool to the service tool data link, which is located on the engine or in the cab.
>
> After an ECM is replaced or calibrated, the actual engine hours / distance **must** be entered correctly into the ECM.
>
> Input the values of ECM Distance Offset, ECM Time Offset, Engine Distance Offset, and Engine Time Offset prior to replacement or calibration of the ECM. These parameters can be found in the Trip Information section of Features and Parameters.
>
> Verify vehicle odometer is equal to the value recorded before ECM removal. Contact OEM service location if values are incorrect.
>
> ### Inspect
>
> Establish if the suspected feature creating the problem is operating correctly. Reference the relevant “Electronic Controlled Fuel System” (Procedure 101-007) in Section 1 of the appropriate Operation and Maintenance Manual.
>
> To access the “Adjustable Engine Features” section, either select Help -\> Contents from the menu bar, or press F1 with an individual feature within the Features and Parameters section in the electronic service tool.
>
> Review the "Adjustable Engine Features” section to determine if the suspected error is due to an incorrectly set adjustable engine feature.
>
> Use QuickServe™ Online to inspect the calibraton revision history.
>
> 1. Log into QuickServe™ Online
> 2. Select "My Applications"
> 3. Select "ECM Calibraton Revisions"
> 4. Enter the calibration code and select "Search"
> 5. Review the calibration revision information.
>
> The calibration revision history provides information relating to changes made to a calibration each time a new revision is released. This information can be used to establish if there is a commonality between changes made to the calibration and the symptoms being observed. The calibration revision history can also be downloaded in Excel format by selecting “Spreadsheet” in the record filter box.
>
> The greater the number of parameters, the slower the rate at which they can be logged. Therefore, **only** log the minimum number of parameters if sample rate is important.
>
> If no issue can be identified using the steps listed above, the following information should be collected to allow the issue to enter the technical escalation chain:
>
> 1. Engine specifics engine serial number (ESN), application, rating, engine hours, maintenance history, etc.)
> 2. ECM codes (the codes before and after, including revision numbers)
> 3. ECM images (before and after calibration downloads)
> 4. Data logs (utilize existing, pre-defined parameter groups, or use the relevant wiring diagram to identify if multiple circuits utilize a common supply or ground, or monitor parameters which logically would be linked - i.e. User Fuelling State, Engine Speed, Commanded Fuel Rail Pressure, Measured Fuel Rail Pressure, etc.).
