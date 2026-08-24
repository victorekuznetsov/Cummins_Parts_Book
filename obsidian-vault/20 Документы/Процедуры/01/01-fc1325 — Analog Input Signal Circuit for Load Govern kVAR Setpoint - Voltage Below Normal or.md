---
aliases:
  - "Цепь аналогового входа уставки кВАр — напряжение ниже нормы"
type: "Процедура"
doc: "01-fc1325"
title_en: "Analog Input Signal Circuit for Load Govern kVAR Setpoint - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь аналогового входа уставки кВАр — напряжение ниже нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1325.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1325.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Analog Input Signal Circuit for Load Govern kVAR Setpoint - Voltage Below Normal or Shorted to Low Source
**Цепь аналогового входа уставки кВАр — напряжение ниже нормы**

> [!abstract] Процедура · `01-fc1325`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1325.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1325.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1325

### Цепь аналогового входа уставки кВАр — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1325 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Аналоговый входной сигнал для управляемой нагрузкой точки затвора киловольт-ампера занижен. | Модуль управления двигателем не выполняет никаких действий. Возможная потеря производительности. |

![[19802903.png]]

Загрузочный регулятор Kilovolt-Ampere Setpoint - схема дистанционного ввода устройства

### Описание цепи

Нагрузка, управляющая аналоговым входным сигналом точки заданной заданной точки, является внешним входом в модуль управления двигателем, используемый для управления нагрузкой набора двигателя/генератора. Нагрузка регулирует киловольт-амперный заданный аналоговый входной сигнал, посылаемый в модуль управления двигателем с удаленного устройства ввода.

Модуль управления двигателем контролирует напряжение на нагрузке, управляет контактом аналогового входного сигнала с заданной точкой киловольт-ампер и ожидает, что напряжение изменяется между 0,5 и 4,5-VDC во время нормальной работы двигателя.

Низкое напряжение будет сбивать Код 1325 по умолчанию и может быть вызвано шортами в сигнальном проводе, открытым в сигнале или неисправным устройством ввода.

### Расположение компонента

Справочный раздел E для определения местоположения карточной клетки модуля управления двигателем.

Ссылка на клиентскую/факультетскую/установочную документацию для определения местоположения устройства удаленного ввода.

### Практические замечания

Возможные режимы отказа - это открытая схема, короткая к земле и неисправное устройство ввода.

Убедитесь, что щиты и площадки хороши.

Проверьте входной сигнал с помощью электронного инструментария INSITETM.

См. Код устранения неполадок t05-1325.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1325
>
> ### Analog Input Signal Circuit for Load Govern kVAR Setpoint - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1325 PID(P): SPN: FMI: Lamp: Warning SRT: | The analog input signal for the load governed kilovolt-ampere setpoint is shorted low. | No action is taken by the engine control module. Possible loss of performance. |
>
> Load Govern Kilovolt-Ampere Setpoint - Remote Input Device Circuit
>
> ### Circuit Description
>
> The load govern kilovolt-ampere setpoint analog input signal is an external input into the engine control module used for load governing of the engine/generator set. The load govern kilovolt-ampere setpoint analog input signal is sent to the engine control module from the remote input device.
>
> The engine control module monitors the voltage on the load govern kilovolt-ampere setpoint analog input SIGNAL pin and expects to see a voltage vary between 0.5 and 4.5-VDC during normal engine operation.
>
> Low voltage will trip Fault Code 1325 and can be caused by shorts in the signal wire, an open in the signal, or a malfunctioned input device.
>
> ### Component Location
>
> Reference Section E for location of the engine control module card cage.
>
> Reference the customer/facility/installation documentation for the location of the remote input device.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to ground, and failed input device.
>
> Make sure shields and grounds are good.
>
> Check input signal with INSITE™ electronic service tool.
>
> Refer to Troubleshooting Fault Code t05-1325.
