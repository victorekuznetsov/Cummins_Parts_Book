---
aliases:
  - "Цепь аналогового входа уставки мощности (кВт) — напряжение выше нормы"
type: "Процедура"
doc: "01-fc1322"
title_en: "Analog Input Signal Circuit for Load Govern Kilowatt Setpoint - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь аналогового входа уставки мощности (кВт) — напряжение выше нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1322.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1322.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Analog Input Signal Circuit for Load Govern Kilowatt Setpoint - Voltage Above Normal or Shorted to High Source
**Цепь аналогового входа уставки мощности (кВт) — напряжение выше нормы**

> [!abstract] Процедура · `01-fc1322`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1322.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1322.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1322

### Цепь аналогового входа уставки мощности (кВт) — напряжение выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1322 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Аналоговый входной сигнал для регулируемой нагрузки Киловатта заданной точки закорочен высоко. | Никакого влияния на производительность. |

![[19802902.png]]

LoadGovern Kilowatt Set Point - схема устройства с удаленным входом

### Описание цепи

Нагрузка управляет аналоговым входным сигналом точки заданной точки заданного значения, который является внешним входом в модуль управления двигателем, используемый для управления и изменения выходного сигнала генератора киловатт, в то время как генераторный набор параллелен утилите. Нагрузка регулирует киловаттный заданный аналоговый входной сигнал, посылаемый в модуль управления двигателем с удаленного устройства ввода.

Модуль управления двигателем контролирует напряжение на нагрузке, управляет контактом аналогового входного сигнала в заданной точке киловатта и ожидает увидеть, что напряжение изменяется между 0,5 и 4,5-VDC во время нормальной работы двигателя.

Высокое напряжение будет сбивать Код 1322 по умолчанию и может быть вызвано шортами в проводе SIGNAL или неисправным устройством ввода.

### Расположение компонента

Справочный раздел E для определения местоположения карточной клетки модуля управления двигателем.

Ссылка на клиентскую/факультетскую/установочную документацию для определения местоположения устройства удаленного ввода.

### Практические замечания

Возможные режимы отказа - это открытая схема, короткая до положительной батареи (+) и неисправное устройство ввода.

Убедитесь, что нормальный рабочий диапазон устройства ввода составляет от 0,1 до 5,0-VDC.

Убедитесь, что щиты и площадки хороши.

Удалённое устройство ввода ** должно быть настроено так, чтобы обеспечивать сигнал от 0 до 5-VDC. Если это устройство настроено на обеспечение сигнала от 0 до 24-VDC, контрольная точка диапазона нагрузки ** должна быть отключена с помощью инструментария электронного обслуживания INSITETM.

См. Код устранения неполадок t05-1322.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1322
>
> ### Analog Input Signal Circuit for Load Govern Kilowatt Setpoint - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1322 PID(P): SPN: FMI: Lamp: Warning SRT: | The analog input signal for the load governed Kilowatt set point is shorted high. | No effect on performance. |
>
> Load Govern Kilowatt Set Point - Remote Input Device Circuit
>
> ### Circuit Description
>
> The load govern kilowatt set point analog input signal is an external input into the engine control module used to control and vary the alternator kilowatt output while the generator set is parallel to the utility. The load govern kilowatt set point analog input signal is sent to the engine control module from the remote input device.
>
> The engine control module monitors the voltage on the load govern kilowatt set point analog input SIGNAL pin and expects to see a voltage vary between 0.5 and 4.5-VDC during normal engine operation.
>
> High voltage will trip Fault Code 1322 and can be caused by shorts in the SIGNAL wire or a failed input device.
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
> Verify that normal operating range of input device is 0.1 to 5.0-VDC.
>
> Make sure shields and grounds are good.
>
> The remote input device **must** be set up to provide a 0 to 5-VDC signal. If this device is set up to provide a 0 to 24-VDC signal, the load govern range checking set point **must** be disabled using INSITE™ electronic service tool.
>
> Refer to Troubleshooting Fault Code t05-1322.
