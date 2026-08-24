---
aliases:
  - "Индикатор воды в топливе выше нормы — умеренный уровень"
type: "Процедура"
doc: "123-fc1852"
title_en: "Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Moderately Severe Level"
title_ru: "Индикатор воды в топливе выше нормы — умеренный уровень"
modified: "2015-09-24"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc1852.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc1852.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Moderately Severe Level
**Индикатор воды в топливе выше нормы — умеренный уровень**

> [!abstract] Процедура · `123-fc1852`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-09-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc1852.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc1852.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1852

### Индикатор воды в топливе выше нормы — умеренный уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1852 PID(P): СПН: 97 ФМИ: 16 ламп: Янтарная СРТ: | Индикатор воды в топливе выше нормы — умеренный уровень. В топливном фильтре обнаружена вода. | Возможен белый дым, потеря энергии или жесткий старт. Упадок двигателя будет происходить на морских двигателях, если включена дополнительная функция защиты двигателя. |

![[19401834.png]]

QSK19 CM2150 Industrial - Вода в топливном индикаторе

![[19401835.png]]

QSK19 CM2150 Морской - Вода в топливном индикаторе Сенсорная схема

![[r8f00016.png]]

QSK19 CM2150 Электрогенерация - Вода в топливном индикаторе Сенсорная схема

### Описание цепи

Вода в датчике индикатора топлива прикрепляется к топливному фильтру первой ступени. Датчик индикатора воды в топливе посылает сигнал модулю управления двигателем (ECM), когда в топливном фильтре накопился заданный объем воды. Вода в топливной цепи содержит два провода; наземный провод и SIGNAL провод.

### Расположение компонента

Вода в датчике индикатора топлива интегрирована в дно топливного фильтра первой ступени. Первый топливный фильтр ступени расположен на впускной стороне двигателя.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Водный фильтр, обнаруженный ECM, был выше уровня датчика.

### Действия системы при активном коде неисправности

- ECM освещает лампу янтарного CHECK ENGINE сразу же, когда диагностика проходит и выходит из строя.

- На двигателях морского движения, если включена дополнительная функция защиты двигателя, произойдет снижение крутящего момента.

### Условия сброса кода неисправности

- Для проверки ремонта выполните ключевой цикл, запустите двигатель и запустите его на холостом ходу в течение 1 минуты.

- Состояние кода ошибки, отображаемого инструментами электронного сервиса INSITETM, будет изменено на INACTIVE сразу после запуска и прохождения диагностики.

- ECM выключит лампу янтарного CHECK ENGINE сразу после диагностических прогонов и проходов.

- Команда Reset All Faults в инструменте электронного сервиса INSITETM может использоваться для устранения активных и неактивных ошибок.

### Практические замечания

Вода в топливе может нанести значительный ущерб топливной системе из-за герметичных допусков компонентов топливной системы.

Смывать топливные фильтры 1-й стадии и/или дуплекса.

Наливное топливо может быть загрязнено.

Если этот код неисправности активен и в топливном фильтре нет воды, то неисправная вода в датчике топлива или вода в разъеме датчика может вызвать неисправность.

См. Troubleshooting Fault Code t05-1852.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1852
>
> ### Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1852 PID(P): SPN: 97 FMI: 16 Lamp: Amber SRT: | Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Moderately Severe Level. Water has been detected in the fuel filter. | Possible white smoke, loss of power, or hard starting. Engine derate will occur on Marine engines if optional engine protection feature is enabled. |
>
> QSK19 CM2150 Industrial - Water In Fuel Indicator Sensor Circuit
>
> QSK19 CM2150 Marine - Water In Fuel Indicator Sensor Circuit
>
> QSK19 CM2150 Power Generation - Water In Fuel Indicator Sensor Circuit
>
> ### Circuit Description
>
> The water in fuel indicator sensor is attached to the first stage fuel filter. The water in fuel indicator sensor sends a signal to the engine control module (ECM) when a set volume of water has accumulated in the fuel filter. The water in fuel circuit contains two wires; a ground wire and SIGNAL wire.
>
> ### Component Location
>
> The water in fuel indicator sensor is integrated into the bottom of the first stage fuel filter. The first stage fuel filter is located on the intake side of the engine.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The ECM detected water in the fuel filter was above the sensor level.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.
>
> - On Marine Propulsion engines, if the optional engine protection feature has been enabled, a torque derate will occur.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.
>
> - The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately after the diagnostic runs and passes.
>
> - The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.
>
> - The Reset All Faults command in INSITE™ electronic service tool can be used to clear active and inactive faults.
>
> ### Shoptalk
>
> Water in the fuel can do extensive damage to the fuel system, due to the tight tolerances of the fuel system components.
>
> Drain the Stage 1 and/or duplex fuel filters.
>
> Bulk fuel supply may be contaminated.
>
> If this fault code is active and there is no water in the fuel filter then a malfunctioning water in fuel sensor or water in the sensor connector could be causing the fault.
>
> Refer to Troubleshooting Fault Code t05-1852.
