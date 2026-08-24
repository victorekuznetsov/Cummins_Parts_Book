---
aliases:
  - "Цепь сигнала положения органа подачи — высокое напряжение"
type: "Процедура"
doc: "07-fc131"
title_en: "Throttle Position Signal Circuit - High Voltage"
title_ru: "Цепь сигнала положения органа подачи — высокое напряжение"
modified: "2012-12-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc131.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc131.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Throttle Position Signal Circuit - High Voltage
**Цепь сигнала положения органа подачи — высокое напряжение**

> [!abstract] Процедура · `07-fc131`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc131.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc131.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 131

### Цепь сигнала положения органа подачи — высокое напряжение

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 131 PID(P): P091 SPN: 91 ФМИ: 3 лампы: Красная СТО: | Высокое напряжение, обнаруженное в цепи сигнала положения дроссельной заслонки. | Сильный дерат (сила и скорость). Слабая домашняя энергия **только ** |

![[19901356.png]]

Схема сигнала дроссельной заслонки

### Описание цепи

Педаль/рычаг ускорителя обеспечивает команду акселератора водителя электронному модулю управления (ECM) через морскую проводку OEM и удлинитель дроссельной заслонки. ECM использует этот сигнал для определения команды заправки для стойки топливного насоса P7100.

### Расположение компонента

Справочный раздел E для подробного описания местоположения компонента. Расположение педали/рычага ускорителя варьируется в зависимости от каждого OEM.

### Практические замечания

Датчик положения педали/рычага ускорителя представляет собой потенциометр. Спецификации сопротивления датчика положения педали/рычага ускорителя следующие:

- Между предложением и возвратом = 2000-3000 Ом

- Между подачей и сигналом: Выпущено = 1500 до 3000 Ом. Депрессировано = 200 до 1500 Ом.

Если педаль/рычаг ускорителя или датчик положения педали/рычага ускорителя изменены или после калибровочной загрузки, цикл педали/рычага ускорителя (переключатель зажигания поворота) через его полное путешествие три раза. Эта процедура калибрует новую педаль/рычажок ускорителя с помощью ECM.

См. Код устранения неполадок t05-131


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 131
>
> ### Throttle Position Signal Circuit - High Voltage
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 131 PID(P): P091 SPN: 91 FMI: 3 Lamp: Red SRT: | High voltage detected at the throttle position signal circuit. | Severe derate (power and speed). Limp home power **only**. |
>
> Throttle Position Signal Circuit
>
> ### Circuit Description
>
> The accelerator pedal/lever provides the driver's accelerator command to the electronic control module (ECM) through the marine OEM harness and the throttle extension harness. The ECM uses this signal to determine the fueling command for the P7100 fuel pump rack.
>
> ### Component Location
>
> Reference Section E for a detailed component location view. The accelerator pedal/lever location varies with each OEM.
>
> ### Shoptalk
>
> The accelerator pedal/lever position sensor is a potentiometer. The resistance specifications of the accelerator pedal/lever position sensor are as follows:
>
> - Between supply and return = 2000 to 3000 ohms
>
> - Between supply and signal:Released = 1500 to 3000 ohmsDepressed = 200 to 1500 ohms
>
> If the accelerator pedal/lever or accelerator pedal/lever position sensor is changed, or after a calibration download, cycle the accelerator pedal/lever (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator pedal/lever with the ECM.
>
> Refer to Troubleshooting Fault Code t05-131
