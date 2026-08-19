---
aliases:
  - "Высокое давление топлива"
type: "Процедура"
doc: "01-fc449"
title_en: "High Fuel Pressure"
title_ru: "Высокое давление топлива"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc449.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc449.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# High Fuel Pressure
**Высокое давление топлива**

> [!abstract] Процедура · `01-fc449`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc449.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc449.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 449

### Высокое давление топлива

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 449 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Высокое давление подачи топлива было обнаружено на датчике давления топлива. | Никаких действий со стороны ЕКМ не предпринимается. Возможен черный дым. |

![[05c00120.png]]

Труба топливной системы

### Описание цепи

Переключающий насос извлекает топливо из топливного бака через топливный фильтр и противоусадочный клапан. Переключающий насос развивает давление топлива от 689 до 2206 кПа[100 до 320 psi]. Топливо течет через экран топливного фильтра и клапан отключения топлива к исполнительным механизмам заправки и синхронизации и датчику давления топлива. Регулятор 1724 кПа[250 psi] контролирует давление топлива.

### Расположение компонента

| Компоненты схемы гидравлической топливной системы |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| 1 | Быстро отсоединяемый кран давления - всасывающая сторона | 5 | Запуск топлива | 9 | Запорный клапан топлива соленоид | 13 | Привод передней синхронизации |
| 2 | 2206 кПа[320 psi] регулятор давления | 6 | Топливный фильтр/водоотделитель | 10 | Быстро отсоединяемый кран давления - сторона давления | 14 | Задний привод |
| 3 | 6.2.1.3 Оборудование линии возврата топлива | 7 | Сливной клапан сепаратора топлива/воды/датчик с водой в топливе | 11 | Датчик давления топлива | 15 | Задний привод для измерения |
| 4 | 36-микронный фильтр | 8 | 1724 кПа[250 psi] регулятор давления | 12 | Передний привод для измерения |  |  |

### Практические замечания

Давление топлива контролируется ECM. Если давление топлива находится за пределами допустимого диапазона, то код неисправности активируется.

Устранение неполадок код t05-449


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 449
>
> ### High Fuel Pressure
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 449 PID(P): SPN: FMI: Lamp: Warning SRT: | High fuel supply pressure was detected at the fuel pressure sensor. | No action is taken by the ECM. Possible black smoke. |
>
> Fuel System Circuit
>
> ### Circuit Description
>
> The gear pump draws fuel from the fuel tank through the fuel filter and anti-drainback valve. The gear pump develops 689 to 2206 kPa \[100 to 320 psi\] of fuel pressure. The fuel flows through the fuel filter screen and fuel shutoff valve to the fueling and timing actuators and the fuel pressure sensor. The 1724 kPa \[250 psi\] regulator controls the fuel pressure.
>
> ### Component Location
>
> | Hydraulic Fuel System Circuit Components |  |  |  |  |  |  |  |
> |---|---|---|---|---|---|---|---|
> | 1 | Quick-disconnect pressure tap - suction side | 5 | Fuel inlet | 9 | Fuel shutoff valve solenoid | 13 | Front timing actuator |
> | 2 | 2206 kPa \[320 psi\] pressure regulator | 6 | Fuel filter/water separator | 10 | Quick-disconnect pressure tap - pressure side | 14 | Rear timing actuator |
> | 3 | Fuel return line fitting | 7 | Fuel/water separator drain valve/Water-in-fuel sensor | 11 | Fuel pressure sensor | 15 | Rear metering actuator |
> | 4 | 36-micron filter screen | 8 | 1724 kPa \[250 psi\] pressure regulator | 12 | Front metering actuator |  |  |
>
> ### Shoptalk
>
> The fuel pressure is monitored by the ECM. If the fuel pressure is outside of an acceptable range the fault code is activated.
>
> Refer to Troubleshooting Fault Code t05-449
