---
aliases:
  - "Цепь потенциометра регулировки частоты генератора — напряжение выше нормы"
type: "Процедура"
doc: "60-fc1411"
title_en: "Generator Output Frequency Adjust Potentiometer Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь потенциометра регулировки частоты генератора — напряжение выше нормы"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1411.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1411.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Generator Output Frequency Adjust Potentiometer Circuit - Voltage Above Normal or Shorted to High Source
**Цепь потенциометра регулировки частоты генератора — напряжение выше нормы**

> [!abstract] Процедура · `60-fc1411`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1411.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1411.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1411

### Цепь потенциометра регулировки частоты генератора — напряжение выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1411 PID(P): S151 SPN: 4182 FMI: 3/3 лампы: Янтарная СРТ: | Высокое напряжение сигнала, обнаруженное на выходной частоте генератора, регулирует схему потенциометра. | Нет. |

![[19a00875.png]]

Генератор выходной частоты регулирует цепь потенциометра.

### Описание цепи

Потенциометр регулирования выходной частоты генератора представляет собой потенциометр, используемый ECM для регулирования частоты генератора. Это частота, на которой выходное напряжение генераторной установки начинает падать. Потенциометр имеет три схемы: 5-вольтная цепь подачи, возврата и сигнала. Напряжение цепи сигнала указывает на то, что выходная частота генератора регулирует вход потенциометра в ECM.

### Расположение компонента

Генератор выходной частоты регулировки потенциометра расположен на панели управления генератором.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда контроллер генераторного набора активен.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала регулятора выходной частоты генератора было вне диапазона.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Грязный генератор частот регулирует потенциометр.

- Неисправный частотный регулятор генератора потенциометр.

- Неисправный или повреждённый жгут проводов двигателя.

- Неисправность или повреждение OEM-проводов.

См. Код 1411 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1411
>
> ### Generator Output Frequency Adjust Potentiometer Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1411 PID(P): S151 SPN: 4182 FMI: 3/3 Lamp: Amber SRT: | High signal voltage detected at the generator output frequency adjust potentiometer circuit. | None. |
>
> Generator Output Frequency Adjust Potentiometer Circuit.
>
> ### Circuit Description
>
> The generator output frequency adjust potentiometer is a potentiometer used by the ECM to regulate the generator frequency. This is the frequency at which the generator set output voltage starts to drop. The potentiometer has three circuits: 5 volt supply, return, and signal circuits. The signal circuit voltage indicates the generator output frequency adjust potentiometer input to the ECM.
>
> ### Component Location
>
> The generator output frequency adjust potentiometer is located on the generator control panel.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the generator output frequency adjust potentiometer signal voltage was out of range high.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, start the engine and let it run for 1 minute at no load.
>
> - The generator set controller will turn off the warning indicator immediately after the user presses reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - A dirty generator frequency adjust potentiometer.
>
> - Malfunctioning generator frequency adjust potentiometer.
>
> - Malfunctioning or damaged engine wiring harness.
>
> - Malfunctioning or damaged OEM wiring harness.
>
> Refer to Troubleshooting Fault Code 1411.
