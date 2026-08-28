---
aliases:
  - "Подключения INSITE™"
type: "TSB"
doc: "tsb110046"
title_en: "INSITE™ Electronic Service Tool Connections"
title_ru: "Подключения INSITE™"
released: "2011-03-09"
modified: "2011-03-09"
group: "19 - Electronic Engine Controls"
engines:
  - "33224404"
  - "33239746"
  - "33239899"
  - "41340468"
  - "41349633"
  - "41353297"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QSK50"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110046.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110046.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QSK50"
  - "год/2011"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# INSITE™ Electronic Service Tool Connections
**Подключения INSITE™**

> [!abstract] TSB · `tsb110046`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19, QSK50
> **Даты:** выпущен 2011-03-09 · изменён 2011-03-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110046.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110046.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Подключения INSITE™

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

В этом документе представлена информация по ряду вопросов, связанных с использованием инструментария электронных услуг INSITETM для получения расширенных данных ECM, данных об ошибках снимка, данных о тенденциях и проведения калибровки ECM, когда один порт шины данных OEM J1939 CAN доступен в приложениях с двумя двигателями, оснащенными несколькими.ECM

Как правило, возникают две проблемы:

1. Когда поток данных для двухдвигательных двигателей, оснащенных несколькими ECM, транслируется на общую шину данных CAN, существует ряд ограничений, поскольку стандартная скорость обработки данных для электронного инструментария INSITETM недостаточна для обеспечения надлежащей регистрации данных и функциональности поиска неисправностей.
2. У двухдвигательных двигателей есть калибровки, которые однозначно идентифицируют все шесть ECM на обоих двигателях. Каждый двигатель и модуль идентифицируется по уникальному адресу источника, который присваивается ECM, когда он обнаруживает различные комбинации заземления на многоединичных штифтах синхронизации (MUS) и идентификации (ID) и сравнивает их с калибровкой, установленной в ECM. Если выявлено несоответствие между комбинацией заземления и установленной калибровкой, может быть назначен неправильный адрес источника. Кроме того, если ECM установлены в двигателях/приложениях, которые **не** имеют заземленные штифты MUS, инструмент электронного обслуживания INSITETM может **не** устанавливать связь и может быть активирован Fault Fode 5092.

Функциональность регистрации данных и поиска неисправностей:

При использовании инструментария электронных услуг INSITETM для получения данных Advanced ECM Data, данных по ошибкам и данных о тенденциях из конкретного двигателя с использованием порта шины данных OEM CAN вручную изолируйте двигатель (двигатели), с которыми **не** следует связываться из шины данных CAN. Любые разъемы шины данных CAN, которые были отключены от основной шины, должны быть прекращены с использованием подходящего резистора для придания общему сопротивлению шины данных CAN 60 Ом.

![[19000002.png]]

3-контактный двигатель J1939 CAN Data Bus (1)

> [!note] Примечание
> Неспособность убедиться в правильном сопротивлении окончанию шины данных CAN может привести к повреждению ECM.

С переключателем зажигания в положении ON используйте инструмент электронного обслуживания INSITETM для подключения к двигателю с использованием порта шины данных OEM CAN. Теперь можно создать рабочий процедура. При необходимости также могут использоваться расширенные функции мониторинга данных и двигателей ECM.

После подключения и мониторинга электронного инструментария обслуживания INSITETM необходимая шина данных CAN двигателя может быть подключена так, чтобы не пострадали любые гидравлические износы OEM.

Если требуется одновременное включение нескольких двигателей, подключитесь к любым дополнительным двигателям, подключившись к разъему шины данных CAN с 9-контактным двигателем с использованием кабеля, Части № 3165160, подходящего встроенного адаптера и последовательного кабеля расширения, Части № 3162851. Использование длинного последовательного удлинителя кабеля позволяет запускать его в кабину.

После того, как один двигатель был успешно передан, описанный выше процесс может быть повторен, как это требуется для всех двигателей.

После того, как все двигатели были успешно соединены, резистор (резисторы) остановки  должен быть удален, и все двигатели должны быть повторно подключены к шине данных CAN.

Перебалансировка:

Можно использовать два метода, в зависимости от того, установлены ли правильные заземления штифта на двигателе.

Способ 1

Этот метод предполагает, что идентификатор модуля и MUS-штыри были заземлены правильно, а модули просто требуют калибровки.

1. Изолировать любые двигатели **не**, требующие калибровки, путем отсоединения их от основной шины данных CAN, как описано в процедуре выше.

2. Удалите разъемы питания ECM со всех ECM, не требующих калибровки, см. ниже.

![[19000003.png]]

4-контактный разъём питания ECM (1)

3. Используйте инструмент электронного обслуживания INSITETM для подключения к модулю, требующему калибровки, с использованием порта шины данных OEM CAN.

4. Используйте инструмент для электронного обслуживания INSITETM для калибровки модуля.

5. Повторите процедуру, описанную выше, до тех пор, пока все модули не будут откалиброваны.

6. Подключите все двигатели и модули к основной шине данных CAN.

Способ 2

Этот метод предполагает, что идентификатор модуля и/или MUS-штифы были заземлены неправильно и/или требуется загрузка ROM.

Наиболее надежным методом калибровки является ROM-загрузка каждого ECM в отдельности. Этот подход гарантирует, что установлена правильная калибровка, и каждый ECM принимает правильный адрес источника.

См. Таблицу 1 для получения дополнительной информации о заземлении штифта.

1. Используйте подходящий загрузочный кабель ROM, номер детали 3164185, чтобы заземлить правильные идентификационные контакты для создания правильного адреса источника и позволить инструменту электронной службы INSITETM общаться с ECM (X = заземленным), как показано в таблице 1.

| Таблица 1: Pin Allocation для правильного назначения адреса источника |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  | калибровка | Источник адреса | Модуль ID Input 1 | Модуль ID Input 2 | Модуль ID Input 3 | Контакты 3 | Контакты 1 | Контакты 2 |  |
| Декларация | Шеф | Контакт 08 | Контакт 07 | Контакт 12 | Контакт 02 | Контакт 03 | Контакт 17 |  |  |
| Левый двигатель | родитель | 0 | 00 |  | X | X | X | X | X |
| Ребенок 1 | 1 | 01 | X |  | X | X | X | X |  |
| Ребенок 2 | 144 | 90 | X | X |  | X | X | X |  |
| Правый двигатель | родитель | 145 | 91 |  | X | X | X | X |  |
| Ребенок 1 | 146 | 92 | X |  | X | X | X |  |  |
| Ребенок 2 | 147 | 93 | X | X |  | X | X |  |  |

2. Используйте инструмент для электронного обслуживания INSITETM для подключения к модулю, требующему калибровки.

> [!note] Примечание
> Все заземляющие соединения должны быть подключены до включения ECM.

> [!note] Примечание
> ECM **должен быть отключен в течение 30 секунд, а затем включен,** каждый раз, когда основания ID-пина изменены. Это позволяет ECM сбрасывать.

> [!note] Примечание
> Узлы OEM-проводов уже должны иметь заземленные штифты.

3. Используйте инструмент для электронного обслуживания INSITETM для калибровки модуля.

4. Повторите процедуру, описанную выше, до тех пор, пока все модули не будут откалиброваны.

5. Подключите все модули к двигателю.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## INSITE™ Electronic Service Tool Connections
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> This document provides information on a number of issues associated with using INSITE™ electronic service tool to obtain Advanced ECM Data, Fault Snapshot Data, Trend Data, and carry out ECM calibration when a single OEM J1939 data link port is available in applications with twin engines equipped with multiple.ECMs
>
> Typically, two issues are experienced:
>
> 1. When the data stream for twin engines equipped with multiple ECMs is broadcast to a common data link, a number of limitations are experienced, because the industry standard baud rate for INSITE™ electronic service tool is insufficient to allow adequate data logging and fault finding functionality.
> 2. Twin engine equipped applications have calibrations which uniquely identify all six ECMs on both engines. Each engine and module is identified by a unique source address that is assigned by the ECM when it detects different combinations of grounding on the Multi-Unit Synchronisation (MUS) and Identification (ID) pins and compares these to the calibration installed in the ECM. If a mismatch between the grounding combination and the calibration installed is identified, an incorrect source address can be assigned. Also, if the ECMs are installed in engines/applications which do **not** have the MUS pins grounded, INSITE™ electronic service tool may **not** be able to establish communication and Fault Fode 5092 can be activated.
>
> Data logging and fault finding functionality:
>
> When using INSITE™ electronic service tool to obtain Advanced ECM Data, Fault Snapshot Data, and Trend Data from a specific engine using the OEM data link port, manually isolate the engine(s) which are **not** to be communicated with from the data link. Any data link connectors which have been disconnected from the main bus should be terminated using a suitable resistor to give a total data link resistance of 60 ohms.
>
> 3-pin J1939 engine data link (1)
>
> **Note · Примечание**
> Failure to make sure of the correct data link termination resistance can result in damage to the ECM.
>
> With the keyswitch in the ON position, use INSITE™ electronic service tool to connect to the engine using the OEM data link port. A work order can now be created. Advanced ECM Data and Engine Monitoring functions can also be used, if required.
>
> Once INSITE™ electronic service tool is connected and monitoring, the required engine data link can be connected so that any OEM hydraulic derates are unaffected.
>
> If simultaneous data logging of multiple engines is required, connect to any additional engines by connecting to the on-engine 9-pin data link connector using cable, Part Number 3165160, a suitable inline adapter, and extension serial cable, Part Number 3162851. The use of a long extension serial cable allows it to be run into the cab.
>
> Once one engine has been successfully communicated with, the process described above can be repeated as required for all engines.
>
> Once all engines have been successfully communicated with, the termination resistor(s) **must** be removed and all engines reconnected to the data link bus.
>
> Recalibration:
>
> Two methods can be used, depending on whether the correct pin groundings are in place on the engine.
>
> Method 1
>
> This method assumes the module ID and MUS pins have been grounded correctly and the modules simply require calibrating.
>
> 1. Isolate any engines **not** requiring calibration by disconnecting them from the main data link bus, as described in the procedure above.
>
> 2. Remove the ECM power supply connectors from all ECMs **not** needing calibration, see below.
>
> 4-pin ECM power supply connector (1)
>
> 3. Use INSITE™ electronic service tool to connect to the module requiring calibration using the OEM data link port.
>
> 4. Use INSITE™ electronic service tool to calibrate the module.
>
> 5. Repeat the procedure above, as required, until all modules have been calibrated.
>
> 6. Connect all engines and modules to the main data link bus.
>
> Method 2
>
> This method assumes the module ID and/or MUS pins have been grounded incorrectly and/or a ROM boot is required.
>
> The most reliable method for calibration is to ROM boot each ECM individually. This approach makes sure the correct calibration is installed and each ECM assumes the correct source address.
>
> See Table 1 for further information on pin grounding.
>
> 1. Use a suitable ROM boot cable, Part Number 3164185, to ground the correct ID pins to create the correct source address and allow INSITE™ electronic service tool to communicate with the ECM (X=grounded), as shown in Table 1.
>
> | Table 1: Pin Allocation for Correct Source Address Assignment |  |  |  |  |  |  |  |  |  |
> |---|---|---|---|---|---|---|---|---|---|
> |  | Calibration | Source Address | Module ID Input 1 | Module ID Input 2 | Module ID Input 3 | MUS Pin 3 | MUS Pin 1 | MUS Pin 2 |  |
> | Dec | Hex | Pin 08 | Pin 07 | Pin 12 | Pin 02 | Pin 03 | Pin 17 |  |  |
> | Left Engine | Parent | 0 | 00 |  | X | X | X | X | X |
> | Child 1 | 1 | 01 | X |  | X | X | X | X |  |
> | Child 2 | 144 | 90 | X | X |  | X | X | X |  |
> | Right Engine | Parent | 145 | 91 |  | X | X | X | X |  |
> | Child 1 | 146 | 92 | X |  | X | X | X |  |  |
> | Child 2 | 147 | 93 | X | X |  | X | X |  |  |
>
> 2. Use INSITE™ electronic service tool to connect to the module requiring calibration.
>
> **Note · Примечание**
> All grounding connections **must** be connected prior to powering up the ECM.
>
> **Note · Примечание**
> The ECM **must** be keyed OFF for 30 seconds and then keyed ON, **every** time the ID pin grounds are changed. This allows the ECM to reset.
>
> **Note · Примечание**
> OEM harnesses should already have the pins grounded.
>
> 3. Use INSITE™ electronic service tool to calibrate the module.
>
> 4. Repeat the procedure above, as required, until all modules have been calibrated.
>
> 5. Connect all modules to the engine.
>
> ### Document History
