---
aliases:
  - "Высокая температура воды на входе охладителя — предупреждение"
type: "Процедура"
doc: "01-fc2113"
title_en: "Aftercooler Water Inlet Temperature High - Warning"
title_ru: "Высокая температура воды на входе охладителя — предупреждение"
modified: "2010-07-29"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2113.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc2113.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Aftercooler Water Inlet Temperature High - Warning
**Высокая температура воды на входе охладителя — предупреждение**

> [!abstract] Процедура · `01-fc2113`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2113.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc2113.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2113

### Высокая температура воды на входе охладителя — предупреждение

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2113 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Температура охлаждающей жидкости двигателя 2 высокая - предупреждение. Сигнал напряжения указывает, что температура входа воды после охлаждения превысила пороговое значение для высокой температуры входа воды после охлаждения. | Калибровка зависима. Никаких действий не предпринимается ECM или отключение двигателя. |

![[19803592.png]]

Послеохладитель Вводная Схема Температурного Датчика

### Описание цепи

Датчик температуры впуска воды после охлаждения используется электронным модулем управления (ECM) для мониторинга способности системы охлаждения двигателя охлаждать охлаждающую жидкость двигателя. Значение температуры впускного отверстия воды после охлаждения используется ECM для системы защиты двигателя. ECM контролирует напряжение на контакте с температурным сигналом впускного отверстия после охлаждения воды и ожидает, что напряжение будет варьироваться от 0,5 до 4,5 ВДК во время нормальной работы двигателя.

### Расположение компонента

См. процедуру 100-002 для определения местоположения компонента.

### Практические замечания

Убедитесь, что впускной поток воды ** не ограничен. Сопротивление датчика изменяется в зависимости от температуры.

См. Код устранения неполадок t05-2113


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2113
>
> ### Aftercooler Water Inlet Temperature High - Warning
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2113 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine coolant temperature 2 high - warning. Voltage signal indicates aftercooler water inlet temperature has exceeded the warning threshold for high aftercooler water inlet temperature. | Calibration-dependent. No action is taken by the ECM, or engine shutdown. |
>
> Aftercooler Water Inlet Temperature Sensor Circuit
>
> ### Circuit Description
>
> The aftercooler water inlet temperature sensor is used by the electronic control module (ECM) to monitor the ability of the engine cooling system to cool down the engine coolant. The aftercooler water inlet temperature value is used by the ECM for the engine protection system. The ECM monitors the voltage on the aftercooler water inlet temperature signal pin and expects to see a voltage vary between 0.5 and 4.5 VDC during normal engine operation.
>
> ### Component Location
>
> Refer to Procedure 100-002 for the component location.
>
> ### Shoptalk
>
> Make sure that the water inlet flow is **not** restricted. The resistance of the sensor varies with the temperature.
>
> Refer to Troubleshooting Fault Code t05-2113
