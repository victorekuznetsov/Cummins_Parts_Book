---
aliases:
  - "Индикатор воды в топливе 2 — выше нормы — низший уровень"
type: "Процедура"
doc: "123-fc5932"
title_en: "Water in Fuel Indicator 2 - Data Valid But Above Normal Operating Range - Least Severe Level"
title_ru: "Индикатор воды в топливе 2 — выше нормы — низший уровень"
modified: "2016-12-12"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc5932.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc5932.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# Water in Fuel Indicator 2 - Data Valid But Above Normal Operating Range - Least Severe Level
**Индикатор воды в топливе 2 — выше нормы — низший уровень**

> [!abstract] Процедура · `123-fc5932`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-12-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc5932.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc5932.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 5932

### Индикатор воды в топливе 2 — выше нормы — низший уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 5932 PID(P): СПН: 6301 FMI: 15 ламп: Обслуживание SRT: | Индикатор воды в топливе 2 — выше нормы — низший уровень. В топливном фильтре обнаружена вода. | Возможен белый дым, потеря энергии или жесткий старт. |

![[19r99369.png]]

Вода в топливном индикаторе сенсорной цепи

### Описание цепи

Датчик индикатора 2 для воды в топливе прикреплен к топливному фильтру производителя оригинального оборудования (OEM) Stage 0 для морских применений. Вода в индикаторе 2 топлива датчик посылает сигнал на модуль управления двигателем (ECM), когда в топливном фильтре накопился заданный объем воды. Вода в цепи датчика индикатора 2 топлива содержит два провода; вода в индикаторе топлива возвращает (датчик ВПЕРЕДЕНИЯ 1) наземный провод и вода в индикаторе топлива SIGNAL провод.

### Расположение компонента

Датчик индикатора 2 для воды в топливе устанавливается в качестве опции в корпус топливного фильтра 0 стадии (OEM), который смонтирован вне двигателя. См. сервисную документацию изготовителя оборудования.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения или когда двигатель работает.

### Условия установки кодов неисправностей

Водный фильтр, обнаруженный в ECM, был выше уровня датчика.

### Действия системы при активном коде неисправности

- ECM освещает белую лампу MAINTENANCE или мигает лампой янтарной CHECK ENGINE, указывая на состояние обслуживания, сразу после диагностических прогонов и сбоев.

### Условия сброса кода неисправности

- Для проверки ремонта выполните ключевой цикл, запустите двигатель и запустите его на холостом ходу в течение 1 минуты.

- Состояние кода ошибки, отображаемого инструментами электронного сервиса INSITETM, будет изменено на INACTIVE сразу после запуска и прохождения диагностики.

- ECM отключит мигающую лампу CHECK ENGINE / MAINTENANCE сразу после диагностических прогонов и проходов.

- Команда Reset All Faults в инструменте электронного сервиса INSITETM может использоваться для устранения активных и неактивных ошибок.

### Практические замечания

Вода в топливе может нанести значительный ущерб топливной системе из-за герметичных допусков компонентов топливной системы.

Смывать топливные фильтры стадии 0 и/или дуплекса.

Наливное топливо может быть загрязнено.

Если этот код неисправности активен и в топливном фильтре нет воды, неисправная вода в датчике топлива или вода в разъеме датчика может вызвать неисправность.

См. Код 5932 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 5932
>
> ### Water in Fuel Indicator 2 - Data Valid But Above Normal Operating Range - Least Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 5932 PID(P): SPN: 6301 FMI: 15 Lamp: Maintenance SRT: | Water in Fuel Indicator 2 - Data Valid But Above Normal Operating Range - Least Severe Level. Water has been detected in the fuel filter. | Possible white smoke, loss of power, or hard starting. |
>
> Water in Fuel Indicator Sensor Circuit
>
> ### Circuit Description
>
> The water in fuel indicator 2 sensor is attached to the Stage 0 original equipment manufacturer (OEM) fuel filter for Marine applications. The water in fuel indicator 2 sensor sends a signal to the engine control module (ECM) when a set volume of water has accumulated in the fuel filter. The water in fuel indicator 2 sensor circuit contains two wires; a water in fuel indicator return (sensor RETURN 1) ground wire and a water in fuel indicator SIGNAL wire.
>
> ### Component Location
>
> The water in fuel indicator 2 sensor is installed as an option into the Stage 0 (OEM) fuel filter housing which is mounted off-engine. See equipment manufacturer service information.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The ECM detected water in fuel filter was above the sensor level.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the white MAINTENANCE lamp or flashes the amber CHECK ENGINE lamp, indicating a maintenance condition, immediately after the diagnostic runs and fails.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.
>
> - The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately after the diagnostic runs and passes.
>
> - The ECM will turn off the flashing amber CHECK ENGINE lamp / MAINTENANCE lamp immediately after the diagnostic runs and passes.
>
> - The Reset All Faults command in INSITE™ electronic service tool can be used to clear active and inactive faults.
>
> ### Shoptalk
>
> Water in the fuel can do extensive damage to the fuel system, due to the tight tolerances of the fuel system components.
>
> Drain the Stage 0 and/or duplex fuel filters.
>
> Bulk fuel supply may be contaminated.
>
> If this fault code is active and there is no water in the fuel filter, a malfunctioning water in fuel sensor or water in the sensor connector could be causing the fault.
>
> Refer to Troubleshooting Fault Code 5932.
