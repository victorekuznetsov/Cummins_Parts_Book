---
aliases:
  - "Датчик температуры воды на входе охладителя — замыкание на плюс"
type: "Процедура"
doc: "01-fc2111"
title_en: "Aftercooler Water Inlet Temperature Sensor - Shorted High"
title_ru: "Датчик температуры воды на входе охладителя — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc2111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Aftercooler Water Inlet Temperature Sensor - Shorted High
**Датчик температуры воды на входе охладителя — замыкание на плюс**

> [!abstract] Процедура · `01-fc2111`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc2111.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2111

### Датчик температуры воды на входе охладителя — замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2111 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Схема датчика температуры охлаждающей жидкости двигателя 2 - закороченная высокая. Ранее это называлось датчиком температуры после охлаждения воды. | Отсутствие защиты двигателя для температуры впуска воды после охлаждения. |

![[19803592.png]]

Послеохладитель Вводная Схема Температурного Датчика

### Описание цепи

Датчик температуры впуска воды после охлаждения используется электронным модулем управления (ECM) для мониторинга способности системы охлаждения двигателя охлаждать охлаждающую жидкость двигателя. Температура впуска воды после охлаждения используется ECM для системы защиты двигателя. ECM контролирует напряжение на контакте с температурным сигналом впускного отверстия после охлаждения воды и ожидает, что напряжение будет варьироваться от 0,5 до 4,5 ВДК во время нормальной работы двигателя. Высокое напряжение будет сбивать Код 2111 по умолчанию и может быть вызвано шортами в сигнале или обратными проводами, открытым в обратном проводе или неисправным датчиком.

### Расположение компонента

См. процедуру 100-002 для определения местоположения компонента.

### Практические замечания

Возможные режимы отказа - это открытая схема, короткая до положительной батареи (+), неисправный датчик и потеря напряжения питания внутри ECM. Сопротивление датчика изменяется в зависимости от температуры.

См. Код устранения неисправностей t05-2111


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2111
>
> ### Aftercooler Water Inlet Temperature Sensor - Shorted High
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2111 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine coolant temperature 2 sensor circuit - shorted high. This was formerly called the aftercooler water inlet temperature sensor. | No engine protection for aftercooler water inlet temperature. |
>
> Aftercooler Water Inlet Temperature Sensor Circuit
>
> ### Circuit Description
>
> The aftercooler water inlet temperature sensor is used by the electronic control module (ECM) to monitor the ability of the engine cooling system to cool down the engine coolant. The aftercooler water inlet temperature is used by the ECM for the engine protection system. The ECM monitors the voltage on the aftercooler water inlet temperature signal pin and expects to see a voltage vary between 0.5 to 4.5 VDC during normal engine operation. High voltage will trip Fault Code 2111 and can be caused by shorts in the signal, or return wires, an open in the return wire, or a failed sensor.
>
> ### Component Location
>
> Refer to Procedure 100-002 for the component location.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to battery positive (+), failed sensor, and loss of supply voltage inside the ECM. The resistance of the sensor varies with the temperature.
>
> Refer to Troubleshooting Fault Code t05-2111
