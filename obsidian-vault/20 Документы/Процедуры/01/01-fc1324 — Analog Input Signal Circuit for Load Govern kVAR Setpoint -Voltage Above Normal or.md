---
aliases:
  - "Цепь аналогового входа уставки кВАр — напряжение выше нормы"
type: "Процедура"
doc: "01-fc1324"
title_en: "Analog Input Signal Circuit for Load Govern kVAR Setpoint -Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь аналогового входа уставки кВАр — напряжение выше нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1324.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1324.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Analog Input Signal Circuit for Load Govern kVAR Setpoint -Voltage Above Normal or Shorted to High Source
**Цепь аналогового входа уставки кВАр — напряжение выше нормы**

> [!abstract] Процедура · `01-fc1324`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1324.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1324.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1324

### Цепь аналогового входа уставки кВАр — напряжение выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1324 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Аналоговый входной сигнал для управляемой нагрузкой точки затвора киловольт-ампер высоко закорочен. | Модуль управления двигателем не выполняет никаких действий. Возможная потеря производительности. |

![[19802903.png]]

Загрузочный регулятор Kilovolt-Ampere Setpoint - схема дистанционного ввода устройства

### Описание цепи

Нагрузка управляет аналоговым входным сигналом точки заданной заданной точки киловольта-ампера, который является внешним входом в модуль управления двигателем, используемым для управления и изменения выходного сигнала киловольта-ампера генератора, в то время как генераторный набор параллелен утилите. Нагрузка регулирует киловольт-амперный аналоговый входной сигнал, посылаемый в модуль управления двигателем с удаленного устройства, обычно ПЛК, который контролирует другой источник для определения количества мощности, предоставляемой генератором.

Модуль управления двигателем контролирует напряжение на нагрузке, управляет контактом аналогового входного сигнала с заданной точкой киловольт-ампер и ожидает, что напряжение изменяется между 0,5 и 4,5-VDC во время нормальной работы двигателя.

Высокое напряжение будет сбивать Код 1324 по умолчанию и может быть вызвано шортами в сигнальном проводе или неисправным устройством ввода.

### Расположение компонента

Справочный раздел E для определения местоположения карточной клетки модуля управления двигателем.

Ссылка на клиентскую/факультетскую/установочную документацию для определения местоположения устройства удаленного ввода.

### Практические замечания

Возможные режимы отказа - это открытая схема, короткая до положительной батареи (+) и неисправное устройство ввода.

Убедитесь, что щиты и площадки хороши.

Проверьте входное напряжение с помощью электронного инструментария обслуживания INSITETM.

Может свести киловольт-амперы к нулю и запустить агрегат при единстве ПФ.

См. Код устранения неполадок t05-1324.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1324
>
> ### Analog Input Signal Circuit for Load Govern kVAR Setpoint -Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1324 PID(P): SPN: FMI: Lamp: Warning SRT: | The analog input signal for the load governed kilovolt-ampere setpoint is shorted high. | No action is taken by the engine control module. Possible loss of performance. |
>
> Load Govern Kilovolt-Ampere Setpoint - Remote Input Device Circuit
>
> ### Circuit Description
>
> The load govern kilovolt-ampere setpoint analog input signal is an external input into the engine control module used to control and vary the kilovolt-ampere output of the alternator while the generator set is paralleled to the utility. The load govern kilovolt-ampere setpoint analog input signal is sent to the engine control module from a remote device, usually a PLC that is monitoring another source to determine the amount of power to be provided by the generator.
>
> The engine control module monitors the voltage on the load govern kilovolt-ampere setpoint analog input signal pin and expects to see a voltage vary between 0.5 and 4.5-VDC during normal engine operation.
>
> High voltage will trip Fault Code 1324 and can be caused by shorts in the signal wire or a failed input device.
>
> ### Component Location
>
> Reference Section E for location of the engine control module card cage.
>
> Reference the customer/facility/installation documentation for the location of the remote input device.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to battery positive (+), and failed input device.
>
> Make sure shields and grounds are good.
>
> Check input voltage using INSITE™ electronic service tool.
>
> Can reduce kilovolt-amperes to zero and run the unit at a unity PF.
>
> Refer to Troubleshooting Fault Code t05-1324.
