---
aliases:
  - "Цепь аналогового входа уставки мощности (кВт)"
type: "Процедура"
doc: "01-fc1327"
title_en: "Load Governed Kilowatt Setpoint - Analog Input Signal Circuit"
title_ru: "Цепь аналогового входа уставки мощности (кВт)"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1327.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1327.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Load Governed Kilowatt Setpoint - Analog Input Signal Circuit
**Цепь аналогового входа уставки мощности (кВт)**

> [!abstract] Процедура · `01-fc1327`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1327.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1327.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1327

### Цепь аналогового входа уставки мощности (кВт)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1327 P(P): СПН: ФМИ: Лампа: Отключение SRT: | Аналоговый входной сигнал для установки киловатт, регулируемой нагрузкой, находится за пределами допустимых рабочих пределов. | Генератор будет отключен. |

![[19802910.png]]

LoadGovern Kilowatt Setpoint - Параллельный контроллер

### Описание цепи

Аналоговые входные сигналы киловаттной точки управления нагрузкой представляют собой внешние входные сигналы в модуль управления двигателем, используемые для управления нагрузкой двигателя/генератора. Нагрузка регулирует киловаттный аналоговый входной сигнал, посылаемый в модуль управления двигателем от параллельного контроллера.

Модуль управления двигателем контролирует напряжение на нагрузке, управляет заданным аналоговым входным сигналом контакта киловатта и ожидает увидеть, что напряжение изменяется между 0,5 и 4,5-VDC во время нормальной работы двигателя.

Низкое напряжение будет сбивать Код 1327 по умолчанию и может быть вызвано шортами в сигнальном проводе, открытым сигналом, неисправным устройством ввода или неправильной установкой.

### Расположение компонента

См. раздел E для определения местоположения карточной клетки модуля управления двигателем.

См. документацию о клиенте/объекте/установке для определения местоположения параллельного контроллера.

### Практические замечания

Возможные режимы отказа - это открытая схема, короткая к земле и неисправное устройство ввода.

Если источник аналогового входного сигнала ** не** настроен для обеспечения сигнала от 0 до 5-VDC, вы ** должны ** отключить функцию проверки диапазона заданий киловатта, используя инструмент электронного обслуживания INSITETM.

| Load Govern - операционный уровень нагрузки |  |
|---|---|
| VDC | Уровень операционной нагрузки |
| 0 - 0,5 | От текущей нагрузки до ненагруженной |
| 0,5 - 1,0 | Без нагрузки |
| 1,0-4,5 | 0 - 100% от рейтинга ожидания |
| 4.5-5.0 | 100% рейтинг ожидания |

См. Код устранения неполадок t05-1327.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1327
>
> ### Load Governed Kilowatt Setpoint - Analog Input Signal Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1327 PID(P): SPN: FMI: Lamp: Shutdown SRT: | The analog input signal for the load governed kilowatt setpoint is outside the acceptable working limits. | Generator set will shut down. |
>
> Load Govern Kilowatt Setpoint - Paralleling Controller Circuit
>
> ### Circuit Description
>
> The load govern kilowatt setpoint analog input signal is an external input into the engine control module used for load governing of the engine/generator set. The load govern kilowatt setpoint analog input signal is sent to the engine control module from the paralleling controller.
>
> The engine control module monitors the voltage on the load govern kilowatt setpoint analog input signal pin and expects to see a voltage vary between 0.5 and 4.5-VDC during normal engine operation.
>
> Low voltage will trip Fault Code 1327 and can be caused by shorts in the signal wire, an open in the signal, a failed input device, or an improper setup.
>
> ### Component Location
>
> Refer to Section E for location of the engine control module card cage.
>
> Refer to customer/facility/installation documentation for the location of the paralleling controller.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to ground, and failed input device.
>
> If analog input signal source is **not** set up to provide a 0 to 5-VDC signal, you **must** disable load govern kilowatt setpoint range checking enable using INSITE™ electronic service tool.
>
> | Load Govern Operating Load Level |  |
> |---|---|
> | VDC | Operating Load Level |
> | 0 to 0.5 | Ramp from present load to no load |
> | 0.5 to 1.0 | No load |
> | 1.0 to 4.5 | 0 to 100% of standby rating |
> | 4.5 to 5.0 | 100% of standby rating |
>
> Refer to Troubleshooting Fault Code t05-1327.
