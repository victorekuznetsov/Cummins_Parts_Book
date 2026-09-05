---
aliases:
  - "Цепь датчика дистанционного органа подачи — замыкание на плюс"
type: "Процедура"
doc: "07-fc133"
title_en: "Remote Throttle Position Sensor Circuit - Shorted High"
title_ru: "Цепь датчика дистанционного органа подачи — замыкание на плюс"
modified: "2012-12-18"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc133.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc133.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Remote Throttle Position Sensor Circuit - Shorted High
**Цепь датчика дистанционного органа подачи — замыкание на плюс**

> [!abstract] Процедура · `07-fc133`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc133.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc133.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 133

### Цепь датчика дистанционного органа подачи — замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 133 P(P): P029 SPN: 974 FMI: 3 лампы: Красная СТО: | Датчик положения резервного дросселя высоко закорочен. | Ни один из них не работает, если используется удаленный дроссел **не**. |

![[19901355.png]]

Цепь датчика положения дистанционного органа управления

### Описание цепи

Педаль/рычаг удаленного ускорителя обеспечивает вторую команду ускорителя электронному модулю управления (ECM) через морскую проводку OEM и основную проводку расширения. ECM использует этот сигнал вместо педали/рычага основного ускорителя для определения команды заправки стойки топливного насоса P7100.

### Расположение компонента

Справочный раздел E для подробного описания местоположения компонента. Местоположение педали/рычага ускорителя удаления зависит от каждого OEM.

### Практические замечания

Датчик положения педали/рычага ускорителя представляет собой потенциометр. Спецификации сопротивления датчика положения педали/рычага ускорителя следующие:

- Между предложением и возвратом = 2000-3000 Ом

- Между подачей и сигналом: Выпущено = 1500 до 3000 Ом. Депрессировано = 200 до 1500 Ом.

Если педаль/рычаг ускорителя или датчик положения педали/рычага ускорителя изменены или после калибровочной загрузки, цикл педали/рычага ускорителя (переключатель зажигания поворота) через его полное путешествие три раза. Эта процедура калибрует новую педаль/рычажок ускорителя с помощью ECM.

Устранение неполадок код t05-133


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 133
>
> ### Remote Throttle Position Sensor Circuit - Shorted High
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 133 PID(P): P029 SPN: 974 FMI: 3 Lamp: Red SRT: | Backup throttle position sensor shorted high. | None on performance if remote throttle is **not** used. |
>
> Remote Throttle Position Sensor Circuit
>
> ### Circuit Description
>
> The remote accelerator pedal/lever provides a second accelerator command to the electronic control module (ECM) through the marine OEM harness and the main extension harness. The ECM uses this signal in place of the primary accelerator pedal/lever to determine the fueling command for the P7100 fuel pump rack.
>
> ### Component Location
>
> Reference Section E for a detailed component location view. The remove accelerator pedal/lever location varies with each OEM.
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
> Refer to Troubleshooting Fault Code t05-133
