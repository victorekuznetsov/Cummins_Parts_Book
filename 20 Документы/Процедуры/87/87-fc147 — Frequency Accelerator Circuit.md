---
aliases:
  - "Цепь частотного задания акселератора"
type: "Процедура"
doc: "87-fc147"
title_en: "Frequency Accelerator Circuit"
title_ru: "Цепь частотного задания акселератора"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
parts:
  - "3659399"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc147.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc147.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Frequency Accelerator Circuit
**Цепь частотного задания акселератора**

> [!abstract] Процедура · `87-fc147`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc147.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc147.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 147

### Цепь частотного задания акселератора

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 147 PID(P): P091 SPN: 091 ФМИ: 8 ламп: Красная СТО: | Чрезмерно низкая частота была обнаружена при частотном ускорительном сигнале контакта 14 проводов двигателя. | Калибровочная зависимость мощности и скорости снижается. |

![[19a00199.png]]

Цепь частотного задания акселератора

### Описание цепи

Педаль акселератора обеспечивает команду акселератора водителя электронному модулю управления (ECM) через OEM-проводник и OEM-интерфейс. ECM использует этот сигнал для определения команды заправки для привода положения стойки.

### Расположение компонента

Расположение педали ускорителя варьируется в зависимости от каждого OEM. См. руководство по OEM.

### Практические замечания

Частотный ускоритель может использоваться либо в сочетании с ускорителем напряжения, либо сам по себе. Промышленная левобережная электропроводка QST30 содержит небольшой треугольный разъем, который содержит диод и резистор, номер детали[[3659399]], который находится примерно в 1 футе от левобережной ЕКМ. Цель этого компонента - для приложений, использующих частотный ускоритель. Этот компонент используется во всех промышленных электропроводках QST30, независимо от того, использует ли приложение частотный ускоритель или нет.

Сигнал подачи частотного ускорителя генерируется тем же OEM-устройством, и этот сигнал отправляется на ускоритель и/или ECM при контакте 14 с проводкой двигателя. Устранение неполадок в устройстве подачи частотного сигнала для обеспечения правильной подачи сигнала на ускоритель/ECM.

Устранение неполадок код t05-147

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3659399]] | ELECTRICAL CONNECTOR | Электрический разъём |

> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 147
>
> ### Frequency Accelerator Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 147 PID(P): P091 SPN: 091 FMI: 8 Lamp: Red SRT: | An excessively low frequency has been detected at frequency accelerator signal pin 14 of the engine harness. | Calibration-dependent power and speed derate. |
>
> Frequency Accelerator Circuit
>
> ### Circuit Description
>
> The accelerator pedal provides the driver's accelerator command to the electronic control module (ECM) through the OEM harness and the OEM interface harness. The ECM uses this signal to determine the fueling command for the rack position actuator.
>
> ### Component Location
>
> The accelerator pedal location varies with each OEM. Refer to the OEM manual.
>
> ### Shoptalk
>
> The frequency accelerator can be used either in conjunction with a voltage accelerator or by itself. The QST30 industrial left-bank engine harness contains a small triangular connector that contains a diode and resistor, Part Number [[3659399]], which is located about 1 foot from the left-bank ECM. The purpose of this component is for applications that use a frequency accelerator. This component is used in all QST30 industrial left-bank engine harnesses, whether or **not** the application uses a frequency accelerator.
>
> The frequency accelerator supply signal is generated by the same OEM device, and that signal is sent to the accelerator and/or ECM on pin 14 of the engine harness. Troubleshoot the frequency signal supply device to be sure that the signal is being supplied correctly to the accelerator/ECM.
>
> Refer to Troubleshooting Fault Code t05-147
