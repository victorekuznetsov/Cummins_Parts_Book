---
aliases:
  - "Цепь датчика давления масла в главной магистрали 1 — напряжение ниже нормы"
type: "Процедура"
doc: "98-fc141"
title_en: "Engine Oil Rifle Pressure 1 Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика давления масла в главной магистрали 1 — напряжение ниже нормы"
modified: "2021-09-08"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Oil Rifle Pressure 1 Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика давления масла в главной магистрали 1 — напряжение ниже нормы**

> [!abstract] Процедура · `98-fc141`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc141.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 141

### Цепь датчика давления масла в главной магистрали 1 — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 141 PID(P): P100 SPN: ФМИ: 4 лампы: На SRT: 00-625 | Низкое напряжение сигнала или открытая цепь, обнаруженная в цепи давления масла двигателя. | Ни одного на выступление. |

![[19802312.png]]

Цепь датчика давления масла

### Описание цепи

Датчик давления масла в двигателе - это датчик переменного сопротивления, используемый ECM для мониторинга давления моторного масла. Датчик давления масла в двигателе имеет три схемы: 5-вольтная цепь подачи, возврата и сигнала. Напряжение цепи сигнала указывает на давление масла в масляной винте.

### Расположение компонента

Расположение датчика давления масла может варьироваться и зависит от OEM.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала давления масла двигателя было вне диапазона низкого.

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

- Неисправный или поврежденный датчик давления масла в двигателе.

Устранение неполадок код t05-141


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 141
>
> ### Engine Oil Rifle Pressure 1 Sensor Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 141 PID(P): P100 SPN: FMI: 4 Lamp: On SRT: 00-625 | Low signal voltage or open circuit detected at the engine oil pressure circuit. | None on performance. |
>
> Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The engine oil pressure sensor is a variable resistance sensor used by the ECM to monitor the lubricating oil pressure. The engine oil pressure sensor has three circuits: 5 volt supply, return, and signal circuits. The signal circuit voltage indicates the oil pressure in the oil rifle.
>
> ### Component Location
>
> The oil pressure sensor location may vary and is OEM dependent.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the engine oil pressure signal voltage was out of range low.
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
> - Malfunctioning or damaged engine oil pressure sensor.
>
> Refer to Troubleshooting Fault Code t05-141
