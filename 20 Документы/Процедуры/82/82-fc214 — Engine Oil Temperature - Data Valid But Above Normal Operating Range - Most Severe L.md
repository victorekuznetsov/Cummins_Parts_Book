---
aliases:
  - "Температура моторного масла выше нормы — наивысший уровень"
type: "Процедура"
doc: "82-fc214"
title_en: "Engine Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Температура моторного масла выше нормы — наивысший уровень"
modified: "2019-06-21"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc214.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc214.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level
**Температура моторного масла выше нормы — наивысший уровень**

> [!abstract] Процедура · `82-fc214`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-06-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc214.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc214.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 214

### Температура моторного масла выше нормы — наивысший уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 214 PID(P): P175 SPN: ФМИ: 0/0 лампа: Красная СТО: | Сигнал температуры масла двигателя указывает температуру масла двигателя выше порога для высокой температуры масла. | Двигатель отключится. |

![[19a00956.png]]

Схема датчика температуры моторного масла

### Описание цепи

Датчик температуры моторного масла является датчиком переменного резистора и используется для измерения температуры моторного масла. Модуль управления двигателем (ECM) подает 5 вольт в схему сигнала температуры масла двигателя. ECM контролирует изменение напряжения, вызванное изменениями сопротивления датчика, для определения температуры масла двигателя. Когда температура масла холодная, сопротивление датчика или термистора высокое. Напряжение сигнала ECM **только **тянет небольшое количество через датчик к земле. Поэтому ECM ощущает высокое напряжение сигнала или низкую температуру. Когда температура масла теплая, сопротивление датчика низкое. Сигнальное напряжение тянет вниз большую величину. Поэтому ECM ощущает низкое напряжение сигнала или высокую температуру.

### Расположение компонента

Комбинированный датчик давления масла и температуры масла расположен на блоке цилиндров непосредственно над приводом аксессуара.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что температура масла двигателя была выше предела защиты двигателя.

### Действия системы при активном коде неисправности

ECM освещает красную лампу STOP ENGINE сразу после диагностических прогонов и выходит из строя.

При этом крутящий момент двигателя будет уменьшен, если двигатель работает в течение длительного периода времени с этим активным разломом.

### Условия сброса кода неисправности

- Для проверки ремонта выполните ключевой цикл, запустите двигатель и запустите его на холостом ходу в течение 1 минуты.

- Состояние кода ошибки, отображаемого рекомендуемой электронной сервисной оснасткой Cummins, или эквивалент, изменится на INACTIVE сразу после диагностических запусков и проходов.

- ECM выключит красную лампу STOP ENGINE сразу после диагностических прогонов и проходов.

- Команда «Сбросить все ошибки» в рекомендуемой электронной сервисной оснастке Cummins® или эквивалентной ей может использоваться для устранения активных и неактивных ошибок.

### Практические замечания

Этот код неисправности указывает на то, что температура моторного масла превысила максимальный предел защиты двигателя для температуры масла. Неисправности устраняют причину высокой температуры моторного масла.

Устранение неполадок Код 214


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 214
>
> ### Engine Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 214 PID(P): P175 SPN: FMI: 0/0 Lamp: Red SRT: | Engine oil temperature signal indicates engine oil temperature above threshold for high oil temperature. | Engine will shut down. |
>
> Engine Oil Temperature Sensor Circuit
>
> ### Circuit Description
>
> The engine oil temperature sensor is a variable resistor sensor and is used to measure the temperature of the engine oil. The engine control module (ECM) supplies 5 volts to the engine oil temperature signal circuit. The ECM monitors the change in voltage caused by changes in the resistance of the sensor to determine the engine oil temperature. When the oil temperature is cold, the sensor or thermistor resistance is high. The ECM signal voltage **only** pulls down a small amount through the sensor to a ground. Therefore, the ECM senses a high signal voltage or low temperature. When the oil temperature is warm, the sensor resistance is low. The signal voltage pulls down a large amount. Therefore, the ECM senses a low signal voltage or high temperature.
>
> ### Component Location
>
> The combination oil pressure and oil temperature sensor is located on the cylinder block directly above the accessory drive.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The engine control module (ECM) detected the engine oil temperature was greater than the engine protection limit.
>
> ### Action Taken When The Fault Code Is Active
>
> The ECM illuminates the red STOP ENGINE lamp immediately after the diagnostic runs and fails.
>
> Engine torque will be reduced if the engine is operated for an extended period of time with this fault active
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, perform a key cycle, start the engine, and let it idle for 1 minute.
>
> - The fault code status displayed by the recommended Cummins electronic service tool, or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.
>
> - The ECM will turn off the red STOP ENGINE lamp immediately after the diagnostic runs and passes.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool, or equivalent, can be used to clear active and inactive faults.
>
> ### Shoptalk
>
> This fault code indicates that the engine oil temperature has exceeded the maximum engine protection limit for oil temperature. Troubleshoot the cause of high engine oil temperature.
>
> Refer to Troubleshooting Fault Code 214
