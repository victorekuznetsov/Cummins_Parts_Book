---
type: "Процедура"
doc: "10-014-027"
title_en: "Aftertreatment Diesel Particulate Filter Regeneration Analyzer"
modified: "2023-09-07"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-014-027.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-014-027.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
  - "перевод/машинный"
---

# Aftertreatment Diesel Particulate Filter Regeneration Analyzer

> [!abstract] Процедура · `10-014-027`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 12 - Compressed Air System - Group 12 · Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2023-09-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-014-027.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-014-027.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Электронный сервисный инструмент Cummins® или его эквивалент.

#### Дополнительные сервисные позиции

- Никаких дополнительных предметов обслуживания не требуется.

### Общие сведения

Последующий фильтр для очистки дизельных частиц (DPF) Regeneration Analyzer Test - это диагностический тест, используемый для выявления неисправных компонентов производительности двигателя. Тест расположен в электронном сервисном оборудовании INSITETM под вкладкой «Диагностические тесты».

Статус теста будет отображаться в окне состояния.

1. Окно описания испытаний
2. Окно инструкций
3. Окно состояния
4. Статусная планка – показывает ход теста (исчезнет, когда тест будет завершен).

![[19204201.png]]

### Системные требования

После обработки дизельного фильтра для регенерации фильтра требуются:

- Инситем электронного сервисного инструментария версии 8.5.2 или более поздней.
- Минимум 250 МБ свободного места на жестком диске перед началом теста.

Последующий анализ фильтра для регенерации дизельных частиц (Diesel Particulate Filter Regeneration Analyzer Test) используется только при направлении опубликованного устранения неполадок.

![[19803969.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Во время испытаний температура выхлопных газов может достигать 800 ° C \[1500 ° F \], а температура поверхности выхлопной системы может превышать 700° C \[1300° F \], которая достаточно горячая, чтобы воспламенить или расплавить обычные материалы и сжечь людей. Выхлопные и выхлопные компоненты могут оставаться горячими после того, как транспортное средство перестанет двигаться. Чтобы избежать риска пожара, повреждения имущества, ожогов или других серьезных травм, позвольте выхлопной системе остыть перед началом этой процедуры или ремонта и убедитесь, что горючие материалы не находятся там, где они могут вступать в контакт с горячими выхлопными газами или компонентами выхлопных газов.

Перед проведением анализатора регенерации дизельного фильтра твердых частиц после обработки выполните следующие действия:

1. Выберите подходящее место для парковки автомобиля.
2. Припаркуйте грузовик надежно.
3. Установите безопасную зону выхлопа.
4. Проверьте поверхности выхлопной системы.
5. Готовьтесь к изменениям скорости двигателя во время регенерации.
6. Чтобы начать тест:

После завершения испытаний на регенерацию дизельного фильтра для твердых частиц температура выхлопных газов и поверхности выхлопных газов будет оставаться повышенной в течение 3-5 минут. Держите двигатель в режиме холостого хода, пока температура выхлопных газов не снизится.

### Проверка

> [!note] Примечание
> Если соединение между электронным сервисным оборудованием INSITETM и модулем управления двигателем (ECM) по какой-либо причине будет потеряно, появится всплывающее сообщение. Испытание можно возобновить после выключения выключателя зажигания на 90 секунд, а затем снова включить.

1. Начните последующую обработку анализатором регенерации дизельного фильтра твердых частиц.
2. Следите за районом.

Лог-файл будет автоматически создан и сохранен на компьютере. Вас могут попросить предоставить лог-файл Cummins® CARE, если требуется техническая помощь.

После обработки дизельного фильтра для регенерации анализатора частиц будет **не** начаться или будет прервано, если:

- Педаль акселератора находится в депрессии
- Педаль сцепления находится в депрессии
- Тормозная педаль подавлена
- Стояночный тормоз **не** установлен
- Передача помещается в передачу
- Вовлеченный
- Скорость автомобиля обнаружена
- Активная защита двигателя
- Регенерация, ингибирующая код неисправности, становится активной
- Высокие температурные перепады после обработки становятся активными.

Если после обработки дизельный фильтр для регенерации твердых частиц аннулирует или будет **не** активирован, будет отображаться сообщение. Исправить вопрос, выявленный до начала разбирательства. Для получения дополнительной информации о сообщениях об абортах и связанных с ними действиях по ремонту см. раздел Устранение неполадок этой процедуры.

### устранение неполадок

Этот раздел используется для устранения неполадок в сообщениях об абортах из окна состояния.

Сообщения об абортах будут отображаться в окне состояния. Последнее сообщение появится внизу.

![[19204202.png]]

| Сообщение Status Window | Меры |
|---|---|
| Тест был остановлен, так как было недостаточно достоверных данных. | Проверка на наличие утечек выхлопных коллекторов. См. процедуру 010-024 в разделе 10. Очистите и проверьте клапан рециркуляции выхлопных газов (EGR). См. процедуру 011-022 в разделе 11. Проверьте после обработки дизельного катализатора окисления (DOC) на затылке лица. Очистка и проверка при повторном использовании. См. процедуру 011-049 в разделе 11. Очистить и осмотреть послеочистку топливного форсунка. См. процедуру 011-042 в разделе 11. Выполните тест потока топлива после обработки. См. процедуру 011-054 в разделе 11. Проверьте вентилятор охлаждения на предмет повреждений. См. процедуру 008-040 в разделе 8. Проверьте термостат охлаждающей жидкости. См. процедуру 008-013 в разделе 8. |
|  Требуется минимум 250 Мб. | Для проведения этого теста требуется минимум 250 МБ памяти. |
| Инструменты электронного обслуживания INSITETM могут **не** в настоящее время считывать параметры ECM от подключенной ECM. Контактная техническая поддержка. | Следите за процессом локальной эскалации. |
| Файлы данных не доступны. Продолжайте публикацию с устранением неполадок. | Продолжайте публикацию с устранением неполадок. |
| Пользователь не имеет достаточных разрешений доступа для создания выходного файла. Свяжитесь с местным ИТ-администратором. | Свяжитесь с местным ИТ-администратором. |
| Испытание завершилось и провалилось. | Прочитайте и запишите сообщение о статусе. |
| Тест остановился или может не начаться, потому что соединение шины данных CAN было потеряно. | Проверьте кабели между компьютером CAN шины данных адаптер для правильного подключения и состояния. См. процедуру 019-165 в разделе 19 Руководства по устранению неполадок и ремонту электронной системы управления SignatureTM, ISX и QSX15, Bulletin 3666259. |

### Завершающие операции

- Не выключайте зажигание до завершения теста и пока не будут показаны результаты.
- Проверьте наличие активных кодов неисправностей. Если присутствуют активные коды неисправностей, следуйте опубликованной устранению неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Cummins® electronic service tool or equivalent.
>
> #### Additional Service Items
>
> - No additional service items required.
>
> ### General Information
>
> The Aftertreatment Diesel Particulate Filter (DPF) Regeneration Analyzer Test is a diagnostic used to identify malfunctioning engine performance components. The test is located in INSITE™ electronic service tool under the Diagnostic Tests tab.
>
> The test status will be shown in the status window.
>
> 1. Test description window
> 2. Instructions window
> 3. Status window
> 4. Status bar - shows progress of the test (will disappear when the test is complete).
>
> ### System Requirements
>
> The Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test requires:
>
> - INSITE™ electronic service tool version 8.5.2 or later.
> - Minimum of 250 MB of available computer hard drive space before starting the test.
>
> The Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test is **only** to be used when directed by published troubleshooting.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> During testing, exhaust gas temperature could reach 800°C \[1500°F\] and exhaust system surface temperature can exceed 700°C \[1300°F\], which is hot enough to ignite or melt common materials, and to burn people. The exhaust and exhaust components can remain hot after the vehicle stops moving. To avoid the risk of fire, property damage, burns or other serious personal injury, allow the exhaust system to cool before beginning this procedure or repair and make sure that no combustible materials are located where they are likely to come in contact with hot exhaust or exhaust components.
>
> Before the Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test, follow the steps listed below:
>
> 1. Select an appropriate location to park the vehicle.
> 2. Park the truck securely.
> 3. Set up a safe exhaust area.
> 4. Check exhaust system surfaces.
> 5. Prepare for engine speed changes during regeneration.
> 6. To begin the test:
>
> Once the Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test is complete, exhaust gas and exhaust surface temperatures will remain elevated for 3 to 5 minutes. Keep the engine running at idle until the exhaust temperatures are reduced.
>
> ### Test
>
> **Note · Примечание**
> If the connection between INSITE™ electronic service tool and the engine control module (ECM) is lost for any reason, a pop-up message will appear. The test can be restarted after cycling the keyswitch OFF for 90 seconds and then back ON.
>
> 1. Begin the Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test.
> 2. Monitor the area.
>
> A logfile will be automatically created and saved to the computer. You may be asked to provide the logfile by Cummins® CARE if technical assistance is required.
>
> The Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test will **not** start or will be aborted if:
>
> - Accelerator pedal is depressed
> - Clutch pedal is depressed
> - Brake pedal is depressed
> - Parking brake **not** set
> - Transmission is put into gear
> - PTO engaged
> - Vehicle speed detected
> - Engine protection state active
> - Regeneration inhibiting fault code becomes active
> - High aftertreatment temperature faults become active.
>
> If the Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test aborts or will **not** activate, a message will be displayed. Correct the issue identified before proceeding. For more information on abort messages and associated repair action, see the Troubleshooting section of this procedure.
>
> ### Troubleshooting
>
> This section is used to assist troubleshooting abort messages from the Status Window.
>
> Abort messages will be displayed in the Status Window. The most recent message will appear at the bottom.
>
> | Status Window Message | Action |
> |---|---|
> | The test was stopped as there was **not** enough valid data. | Inspect for exhaust manifold leaks. Refer to Procedure 010-024 in Section 10. Clean and inspect the exhaust gas recirculation (EGR) valve. Refer to Procedure 011-022 in Section 11. Check for aftertreatment diesel oxidation catalyst (DOC) face plugging. Clean and inspect for reuse. Refer to Procedure 011-049 in Section 11. Clean and inspect the aftertreatment fuel injector. Refer to Procedure 011-042 in Section 11. Perform the Aftertreatment Fuel Injector Flow Test. Refer to Procedure 011-054 in Section 11. Inspect the cooling fan for damage. Refer to Procedure 008-040 in Section 8. Check the coolant thermostat. Refer to Procedure 008-013 in Section 8. |
> | There is **not** enough available storage space. A minimum of 250 MB is required. | Minimum of 250 MB memory space is required to run this test. |
> | INSITE™ electronic service tool can **not** currently read the ECM parameters from the connected ECM. Contact technical support. | Follow local escalation process. |
> | Data files are **not** available. Proceed with published troubleshooting. | Proceed with published troubleshooting. |
> | The user does **not** have sufficient access permissions to create the output file. Contact the local IT administrator. | Contact the local IT administrator. |
> | The test has completed and failed. | Read and record status message. |
> | The test has stopped or could **not** start because the data link connection was lost. | Check the cables between the computer data link adapter for proper connection and condition. Refer to Procedure 019-165 in Section 19 of the Signature™, ISX, and QSX15 Electronic Control System Troubleshooting and Repair Manual, Bulletin 3666259. |
>
> ### Finishing Steps
>
> - Do not turn the keyswitch off until the test has completed and results are displayed.
> - Check for any active fault codes. If active fault codes are present, follow published troubleshooting.
