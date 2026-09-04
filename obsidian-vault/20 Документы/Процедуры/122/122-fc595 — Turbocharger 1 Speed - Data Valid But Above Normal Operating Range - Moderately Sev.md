---
aliases:
  - "Частота вращения турбокомпрессора 1 выше нормы — умеренный уровень"
type: "Процедура"
doc: "122-fc595"
title_en: "Turbocharger 1 Speed - Data Valid But Above Normal Operating Range - Moderately Severe Level"
title_ru: "Частота вращения турбокомпрессора 1 выше нормы — умеренный уровень"
modified: "2017-10-09"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "4022102"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc595.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc595.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Turbocharger 1 Speed - Data Valid But Above Normal Operating Range - Moderately Severe Level
**Частота вращения турбокомпрессора 1 выше нормы — умеренный уровень**

> [!abstract] Процедура · `122-fc595`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-10-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc595.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc595.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 595

### Частота вращения турбокомпрессора 1 выше нормы — умеренный уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 595 PID(P): P103 SPN: 103 FMI: 0/16 лампа: Янтарная СРТ: | Частота вращения турбокомпрессора 1 выше нормы — умеренный уровень. Высокая скорость турбокомпрессора была обнаружена модулем управления двигателем (ECM). | Возможно снижение производительности двигателя. |

![[19204167.png]]

Турбокомпрессор Speed Sensor Circuit

### Описание цепи

Датчик скорости турбокомпрессора является датчиком скорости переменного нежелания. Он состоит из катушки из проволоки и железного сердечника. Цель на вале турбокомпрессора — наземная ровная в центре вала. Когда плоскость на вале турбокомпрессора вращается мимо датчика скорости, генерируется сигнал. ECM интерпретирует этот сигнал и преобразует его в показания скорости турбокомпрессора.

### Расположение компонента

Датчик скорости турбокомпрессора установлен в центральной обшивке турбокомпрессора.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

ECM обнаружил, что скорость турбокомпрессора была больше 150 000 об/мин в течение более 5 секунд.

### Действия системы при активном коде неисправности

- ECM освещает лампу CHECK ENGINE и/или индикатор неисправности (MIL) сразу же после запуска и выхода из строя диагностического устройства.

- ECM будет оценивать скорость турбокомпрессора.

### Условия сброса кода неисправности

Чтобы проверить ремонт, запустите двигатель и используйте педаль акселератора, чтобы ускорить скорость двигателя до высокого холостого хода (100 процентов). Держите двигатель на высокой скорости не менее 20 секунд.

- Состояние кода ошибки, отображаемого инструментами электронного сервиса INSITETM, будет изменено на INACTIVE сразу после запуска и прохождения диагностики.

- ECM отключит лампу янтарного CHECK ENGINE после диагностических прогонов и проходов.

- Для бортовых диагностических (OBD) двигателей ECM погасит MIL после трех последовательных поездок, где проходит диагностика.

- Команда «Сбросить все ошибки» в инструменте электронного обслуживания INSITETM может использоваться для устранения активных и неактивных ошибок, а также для устранения MIL для приложений OBD.

### Практические замечания

Возможные причины этого кода неисправности:

- Поврежденный датчик скорости турбокомпрессора

- Поврежденная электропроводка двигателя

- Повреждённый ECM.

Если неисправность возникает периодически, ищите причины прерывистых открытых или коротких замыканий в цепи датчика скорости турбокомпрессора (включая коннектор с косичками датчика скорости).

См. Код устранения неполадок t05-595.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 595
>
> ### Turbocharger 1 Speed - Data Valid But Above Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 595 PID(P): P103 SPN: 103 FMI: 0/16 Lamp: Amber SRT: | Turbocharger 1 Speed - Data Valid But Above Normal Operating Range - Moderately Severe Level. High turbocharger speed has been detected by the engine control module (ECM). | Possible reduced engine performance. |
>
> Turbocharger Speed Sensor Circuit
>
> ### Circuit Description
>
> The turbocharger speed sensor is a variable reluctance speed sensor. It consists of a coil of wire and an iron core. The target on the turbocharger shaft is a ground flat in the center of the shaft. As the flat on the turbocharger shaft spins past the speed sensor, a signal is generated. The ECM interprets this signal and converts it to a turbocharger speed reading.
>
> ### Component Location
>
> The turbocharger speed sensor is mounted in the center housing of the turbocharger.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the engine is operating.
>
> ### Conditions For Setting The Fault Codes
>
> The ECM detected the turbocharger speed was greater than 150,000 rpm for more than 5 seconds.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE lamp and/or the malfunction indicator lamp (MIL) immediately when the diagnostic runs and fails.
>
> - The ECM will estimate turbocharger speed.
>
> ### Conditions For Clearing The Fault Code
>
> To validate the repair, start the engine and use the accelerator pedal to accelerate the engine speed to high idle (100 percent). Hold the engine speed at high idle for at least 20 seconds.
>
> - The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately after the diagnostic runs and passes.
>
> - The ECM will turn off the amber CHECK ENGINE lamp after the diagnostic runs and passes.
>
> - For On-Board Diagnostics (OBD) engines, the ECM will extinguish the MIL after three consecutive trips where the diagnostic runs and passes.
>
> - The “Reset All Faults” command in INSITE™ electronic service tool can be used to clear active and inactive faults, as well as extinguish the MIL for OBD applications.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Damaged turbocharger speed sensor
>
> - Damaged engine harness
>
> - Damaged ECM.
>
> If the fault occurs intermittently, look for causes of intermittent open or short circuits in the turbocharger speed sensor circuit (including the speed sensor pigtail connector).
>
> Refer to Troubleshooting Fault Code t05-595.
