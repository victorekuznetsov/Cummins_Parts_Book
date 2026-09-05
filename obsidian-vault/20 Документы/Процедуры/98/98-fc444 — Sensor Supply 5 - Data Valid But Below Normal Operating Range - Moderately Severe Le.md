---
type: "Процедура"
doc: "98-fc444"
title_en: "Sensor Supply 5 - Data Valid But Below Normal Operating Range - Moderately Severe Level"
modified: "2021-09-10"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc444.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc444.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Sensor Supply 5 - Data Valid But Below Normal Operating Range - Moderately Severe Level

> [!abstract] Процедура · `98-fc444`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc444.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc444.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 444

### Датчик 5 - данные действительны, но ниже нормального диапазона работы - умеренно тяжелый уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 444 PID(P): S254 SPN: ФМИ: 4 лампы: На SRT: 00-638 | Низкое напряжение, обнаруженное при подаче датчика давления на рельсах. | Мощность и скорость двигателя снижаются. |

![[19802313.png]]

Схема датчика давления на железной дороге

![[19802312.png]]

Цепь датчика давления масла

### Описание цепи

Датчик давления в рельсах представляет собой датчик переменного сопротивления, используемый ECM для мониторинга давления в рельсах топлива. Этот датчик имеет три схемы: 5-вольтная цепь подачи, возврата и сигнала. Этот датчик давления рельса сигнализирует о изменении напряжения на основе давления в топливной рельсе. Датчик давления масла в двигателе - это датчик переменного сопротивления, используемый ECM для мониторинга давления моторного масла. Датчик давления масла в двигателе имеет три схемы: 5-вольтная цепь подачи, возврата и сигнала. Напряжение цепи сигнала указывает на давление масла в масляной винте.

### Расположение компонента

Расположение датчика давления в рельсах может варьироваться и зависит от двигателя. Расположение датчика давления масла может варьироваться и зависит от OEM.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение питания датчика давления в рельсах было за пределами диапазона.

### Действия системы при активном коде неисправности

- ECM освещает янтарный свет CHECK ENGINE, когда диагностика проходит и не удается.

- Отсутствие защиты двигателя от давления масла.

Для приложений генерации электроэнергии:

- Контроллер генераторной установки отображает неисправность сразу же, когда диагностика работает и выходит из строя.

- Отсутствие защиты двигателя от давления масла.

### Условия сброса кода неисправности

- Для проверки ремонта выполните ключевой цикл, запустите двигатель и запустите его на холостом ходу в течение 1 минуты.

- Состояние кода ошибки, отображаемого рекомендованным электронным сервисным инструментом Cummins® или его эквивалентом, будет изменено на INACTIVE сразу после диагностических запусков и проходов.

- ECM выключит лампу янтарного CHECK ENGINE сразу после диагностических прогонов и проходов.

- Команда «Сбросить все ошибки» в рекомендуемой электронной сервисной оснастке Cummins® или эквиваленте может использоваться для устранения активных и неактивных ошибок.

Для приложений генерации электроэнергии:

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки выключит индикатор сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

- Неисправность или повреждение OEM-проводов.

- Поврежденные или рыхлые разъемы.

- Неисправный или поврежденный датчик давления в рельсах.

- Неисправный или поврежденный датчик давления масла в двигателе.

Устранение неполадок код t05-444


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 444
>
> ### Sensor Supply 5 - Data Valid But Below Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 444 PID(P): S254 SPN: FMI: 4 Lamp: On SRT: 00-638 | Low voltage detected at rail pressure sensor supply. | Power and engine speed derate. |
>
> Rail Pressure Sensor Circuit
>
> Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The rail pressure sensor is a variable resistance sensor used by the ECM to monitor the fuel rail pressure. This sensor has three circuits: 5 volt supply, return and signal circuits. This rail pressure sensor signal voltage changes based on the pressure in the fuel rail. The engine oil pressure sensor is a variable resistance sensor used by the ECM to monitor the lubricating oil pressure. The engine oil pressure sensor has three circuits: 5 volt supply, return, and signal circuits. The signal circuit voltage indicates the oil pressure in the oil rifle.
>
> ### Component Location
>
> The rail pressure sensor location may vary and is dependent on the engine. The oil pressure sensor location may vary and is OEM dependent.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the rail pressure sensor supply voltage was out of range low.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE light when the diagnostic runs and fails.
>
> - No engine protection for engine oil pressure.
>
> For Power Generation Applications:
>
> - The generator set controller displays the fault immediately when the diagnostics runs and fails.
>
> - No engine protection for engine oil pressure.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.
>
> - The fault code status displayed by the recommended Cummins® electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.
>
> - The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active and inactive faults.
>
> For Power Generation Applications:
>
> - To validate the repair, start the engine and let it run for 1 minute at no load.
>
> - The generator set controller will turn off the indicator immediately after the user presses reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged engine wiring harness.
>
> - Malfunctioning or damaged OEM wiring harness.
>
> - Damaged or loose connectors.
>
> - Malfunctioning or damaged rail pressure sensor.
>
> - Malfunctioning or damaged engine oil pressure sensor.
>
> Refer to Troubleshooting Fault Code t05-444
