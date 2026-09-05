---
aliases:
  - "Цепь датчика давления коллектора — напряжение ниже нормы"
type: "Процедура"
doc: "07-fc123"
title_en: "Intake Manifold Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика давления коллектора — напряжение ниже нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc123.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc123.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Intake Manifold Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика давления коллектора — напряжение ниже нормы**

> [!abstract] Процедура · `07-fc123`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc123.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc123.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 123

### Цепь датчика давления коллектора — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 123 P(P): P102 SPN: 102 FMI: 4 лампы: Янтарная СРТ: | Цепь датчика давления коллектора — напряжение ниже нормы. Низкое напряжение сигнала, обнаруженное в цепи давления впускного коллектора. | Отклонение зависит от калибровки. |

![[19900354.png]]

Цепь датчика давления во впускном коллекторе

### Описание цепи

Датчик давления впускного коллектора контролирует давление повышения и передает информацию электронному модулю управления (ECM) через контакт сигнала давления впускного коллектора проводов двигателя.

### Расположение компонента

Справочный раздел E для подробного описания местоположения компонента. На двигателе 480C E установлен один датчик давления впускного коллектора. Он расположен рядом с воздухозаборником, за ECM.

### Практические замечания

- Датчик давления впускного коллектора измеряет давление в манометре. Подтвердите, что датчик читает правильно, сравнивая показания, наблюдаемые в ECM, с показаниями, взятыми с помощью механического калибра. Датчик должен читать -38 до 38 мм рт.ст. \[1,5 до 1,5 рт.ст.] с помощью INSITETM, при этом переключатель зажигания поворачивается в положение Включения, но двигатель **не** работает.

- Проверьте наличие высокого ограничения в впускном коллекторе из-за засорения воздушных фильтров или выключателя в коллекторе (если судно оборудовано одним). Не удаляйте это устройство. Если двигатель работает в легковоспламеняющейся атмосфере, устройство является важной функцией безопасности.

- Убедитесь, что турбокомпрессор работает правильно. Проверьте положительное давление коллектора потребления.

См. Устранение неполадок код t05-123


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 123
>
> ### Intake Manifold Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 123 PID(P): P102 SPN: 102 FMI: 4 Lamp: Amber SRT: | Intake Manifold Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source. Low signal voltage detected at the intake manifold pressure circuit. | Derate dependant on calibration. |
>
> Intake Manifold Pressure Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold pressure sensor monitors boost pressure and passes information to the electronic control module (ECM) through the intake manifold pressure signal pin of the engine harness.
>
> ### Component Location
>
> Reference Section E for a detailed component location view. There is one intake manifold pressure sensor on the 480C E engine. It is located next to the air intake heater, behind the ECM.
>
> ### Shoptalk
>
> - The intake manifold pressure sensor measures gauge pressure. Confirm the sensor is reading properly by comparing the reading seen in the ECM with a reading taken with a mechanical gauge. The sensor should read -38 to 38 mm Hg \[-1.5 to 1.5 in Hg\] using INSITE™, with the keyswitch turned to the ON position, but the engine **not** running.
>
> - Check for high restriction in the intake manifold due to clogged air filters or a shutdown device in the manifold (if the vessel is equipped with one). Do **not** remove this device. If the engine is operated in a flammable atmosphere, the device is an essential safety feature.
>
> - Make sure the turbocharger is working correctly. Check for a positive intake manifold pressure.
>
> Refer to Troubleshooting Fault Code t05-123
