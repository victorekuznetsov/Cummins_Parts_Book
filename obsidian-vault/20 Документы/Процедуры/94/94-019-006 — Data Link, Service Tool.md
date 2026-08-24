---
aliases:
  - "Шина данных сервисного инструмента"
type: "Процедура"
doc: "94-019-006"
title_en: "Data Link, Service Tool"
title_ru: "Шина данных сервисного инструмента"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 24
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-006.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-006.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Data Link, Service Tool
**Шина данных сервисного инструмента**

> [!abstract] Процедура · `94-019-006`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-006.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-006.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Схема шины данных CAN используется для INSITETM, номер детали. 3825145, для связи с ECM и для электронной связи с другими бортовыми электронными устройствами.

![[19a00043.png]]

Шина данных CAN использует 9-контактный разъем Deutsch. Позиции проводов следуют:

Pin A - DSR

Pin B - RXD

Pin C - TXD

Pin D - DTR

Pin E - двигатель блокирует землю

Pin F - не используется

Pin G - не используется

Pin H - не используется

Pin J - не используется

![[19a00044.png]]

### Проверка сопротивления

Поместите выключатель Stop/Run в положение STOP.

Убедитесь, что контроллер ** не** в диагностическом режиме.

Удалите разъём жгута проводов двигателя из ECM. См. процедуру[[94-019-043 — Engine Wiring Harness|019-043]].

Используйте измерительный щуп, номер детали. 3822758, на разъеме ECM и испытательном щупе, номер детали. 3824811, на 9-контактном разъеме Deutsch.

Измерьте сопротивление от контакта 31 разъёма ремня электропроводки двигателя к контакту А 9-контактного разъема Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

![[19a00026.png]]

Измерьте сопротивление от контакта 32 разъёма ремня электропроводки двигателя к контакту B 9-контактного разъема Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

![[19a00026.png]]

Измерьте сопротивление от контакта 33 разъёма ремня электропроводки двигателя к контакту C 9-контактного разъема Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

![[19a00026.png]]

Измерить сопротивление от контакта 34 разъёма ремня электропроводки двигателя к контакту D 9-контактного разъема Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

![[19a00026.png]]

Измерьте сопротивление от контакта 35 разъёма ремня электропроводки двигателя к контакту E 9-контактного разъема Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если схема ** не*** закрыта на любом из предыдущих этапов, отремонтируйте или замените электропроводку двигателя. См. Процедуры 019-209,[[94-019-240 — Connector, 40-Pin|019-240]]и[[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00026.png]]

### Проверка на замыкание на массу

Используйте измерительный щуп, номер детали. 3824811, для 9-контактного разъема Deutsch.

Измерьте сопротивление от контакта А разъема Deutsch к блоку двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19a00027.png]]

Измерьте сопротивление от контакта B 9-контактного разъема Deutsch к блоку двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19a00027.png]]

Измерьте сопротивление от контакта C 9-контактного разъема Deutsch к блоку двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19a00027.png]]

Измерьте сопротивление от контакта D 9-контактного разъема Deutsch к блоку двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не открыта на любом из предыдущих этапов, отремонтируйте или замените электропроводку двигателя. См. Процедуры 019-209,[[94-019-240 — Connector, 40-Pin|019-240]]и[[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00027.png]]

### Проверка на замыкание между контактами

** Deutsche Connector**

Используйте измерительный щуп, номер детали. 3824811, для 9-контактного разъема Deutsch.

Измерьте сопротивление от контакта А разъёма Deutsch ко всем другим штифтам в разъёме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

> [!missing]- Иллюстрация `19a00028.png` не извлечена — смотрите PDF-оригинал документа

Измерьте сопротивление от контакта B 9-контактного разъема Deutsch ко всем другим разъемам в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

> [!missing]- Иллюстрация `19a00028.png` не извлечена — смотрите PDF-оригинал документа

Измерьте сопротивление от контакта C 9-контактного разъема Deutsch ко всем другим разъемам в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

> [!missing]- Иллюстрация `19a00028.png` не извлечена — смотрите PDF-оригинал документа

Измерьте сопротивление от контакта D 9-контактного разъема Deutsch ко всем другим разъемам в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

> [!missing]- Иллюстрация `19a00028.png` не извлечена — смотрите PDF-оригинал документа

Измерьте сопротивление от контакта E 9-контактного разъема Deutsch ко всем другим разъемам в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не открыта на любом из предыдущих этапов, отремонтируйте или замените электропроводку двигателя. См. процедуры 019-209 и[[94-019-043 — Engine Wiring Harness|019-043]].

> [!missing]- Иллюстрация `19a00028.png` не извлечена — смотрите PDF-оригинал документа

** разъём электропроводки жгута проводов**

Отсоедините электропроводку двигателя от ECM.

Используйте измерительный щуп, номер детали. 3822758, для разъёма ремней электропроводки двигателя.

Измерьте сопротивление от контакта 31 ко всем другим штифтам в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19a00029.png]]

Измерьте сопротивление от контакта 32 ко всем другим штифтам в разъеме.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19a00029.png]]

Измерьте сопротивление от контакта 33 ко всем другим штифтам в разъеме.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19a00029.png]]

Измерьте сопротивление от контакта 34 ко всем другим штифтам в разъеме.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не открыта на любом из предыдущих этапов, отремонтируйте или замените электропроводку двигателя. См. процедуры[[94-019-240 — Connector, 40-Pin|019-240]]и[[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00029.png]]

### Проверка напряжения

Найдите сервисный инструмент CAN для подключения шины данных на ремне электропроводки двигателя.

Показано устройство CAN Data Bus.

> [!missing]- Иллюстрация `19a00030.png` не извлечена — смотрите PDF-оригинал документа

Поместите выключатель Stop/Run в положение STOP.

Поместите контроллер в диагностический режим.

Включите циферблат на мультиметре для измерения напряжения постоянного тока.

При отключении служебной оснастки от проводов двигателя жгута нажмите команду «Подключиться к ECM» на служебной оснастке и одновременно измерьте напряжение, от контакта B до контакта E (наземного), на разъеме кабеля служебной оснастки. Мультиметр **must** показывает -5 до -15 VDC.

> [!missing]- Иллюстрация `19a00068.png` не извлечена — смотрите PDF-оригинал документа

Если показания напряжения неверны, убедитесь, что инструмент настроен правильно.

Если сервисная оснастка настроена правильно, проведите следующие процедуры.

Измерить непрерывность контакта B кабеля INSITETM, номер детали. 3825183. Мультиметр ** должен ** показывать менее 10 Ом.

![[19400225.png]]

Измерить непрерывность контакта C кабеля INSITETM. Мультиметр ** должен ** показывать менее 10 Ом.

Если схема ** не** закрыта на любом из предыдущих этапов, замените кабель INSITETM, номер детали. 3825183.

![[19400225.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The service tool data link circuit is used for INSITE™, Part No. 3825145, to communicate with the ECM and to electronically communicate information with other on-board electronic devices.
>
> The data link uses a 9-pin Deutsch connector. The wiring positions follow:
>
> Pin A - DSR
>
> Pin B - RXD
>
> Pin C - TXD
>
> Pin D - DTR
>
> Pin E - Engine Block ground
>
> Pin F - Not used
>
> Pin G - Not used
>
> Pin H - Not used
>
> Pin J - Not used
>
> ### Resistance Check
>
> Place the Stop/Run switch in the STOP position.
>
> Ensure the controller is **not** in the diagnostic mode.
>
> Remove the engine harness connector from the ECM. Refer to Procedure [[94-019-043 — Engine Wiring Harness|019-043]].
>
> Use test lead, Part No. 3822758, on the ECM connector and use test lead, Part No. 3824811, on the 9-pin Deutsch connector.
>
> Measure the resistance from pin 31 of the engine harness connector to pin A of the 9-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> Measure the resistance from pin 32 of the engine harness connector to pin B of the 9-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> Measure the resistance from pin 33 of the engine harness connector to pin C of the 9-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> Measure the resistance from pin 34 of the engine harness connector to pin D of the 9-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> Measure the resistance from pin 35 of the engine harness connector to pin E of the 9-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed in any of the previous steps, repair or replace the engine harness. Refer to Procedures 019-209, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit to Ground
>
> Use test lead, Part No. 3824811, for the 9-pin Deutsch connector.
>
> Measure the resistance from pin A of the Deutsch connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin B of the 9-pin Deutsch connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin C of the 9-pin Deutsch connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin D of the 9-pin Deutsch connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open in any of the previous steps, repair or replace the engine harness. Refer to Procedures 019-209, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit from Pin to Pin
>
> **Deutsch Connector**
>
> Use test lead, Part No. 3824811, for the 9-pin Deutsch connector.
>
> Measure the resistance from pin A of the Deutsch connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin B of the 9-pin Deutsch connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin C of the 9-pin Deutsch connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin D of the 9-pin Deutsch connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin E of the 9-pin Deutsch connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open in any of the previous steps, repair or replace the engine harness. Refer to Procedures 019-209 and [[94-019-043 — Engine Wiring Harness|019-043]].
>
> **Engine Harness Connector**
>
> Disconnect the engine harness from the ECM.
>
> Use test lead, Part No. 3822758, for the engine harness connector.
>
> Measure the resistance from pin 31 to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin 32 to all other pins in the connector.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin 33 to all other pins in the connector.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin 34 to all other pins in the connector.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open in any of the previous steps, repair or replace the engine harness. Refer to Procedures [[94-019-240 — Connector, 40-Pin|019-240]] and [[94-019-043 — Engine Wiring Harness|019-043]].
>
> ### Voltage Check
>
> Locate the service tool data link connector on the engine harness.
>
> The data link circuit is shown.
>
> Place the Stop/Run switch in the STOP position.
>
> Place the controller in the diagnostic mode.
>
> Turn the dial on the multimeter to measure DC voltage.
>
> With the service tool disconnected from the engine harness, press the “Connect to ECM” command on the service tool and simultaneously measure the voltage, from pin B to pin E (ground), on the service tool cable connector. The multimeter **must** show -5 to -15 VDC.
>
> If the voltage reading is incorrect ensure the tool is setup correctly.
>
> If the service tool is setup correctly, conduct the following procedures.
>
> Measure the continuity for pin B of the INSITE™ cable, Part No. 3825183. The multimeter **must** show less than 10 ohms.
>
> Measure the continuity for pin C of the INSITE™ cable. The multimeter **must** show less than 10 ohms.
>
> If the circuit is **not** closed in any of the previous steps, replace the INSITE™ cable, Part No. 3825183.
