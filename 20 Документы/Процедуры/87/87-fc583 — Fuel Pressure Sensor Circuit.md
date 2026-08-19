---
aliases:
  - "Цепь датчика давления топлива"
type: "Процедура"
doc: "87-fc583"
title_en: "Fuel Pressure Sensor Circuit"
title_ru: "Цепь датчика давления топлива"
modified: "2011-06-27"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc583.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc583.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Fuel Pressure Sensor Circuit
**Цепь датчика давления топлива**

> [!abstract] Процедура · `87-fc583`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-06-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc583.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc583.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 583

### Цепь датчика давления топлива

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 583 PID(P): P015 SPN: ФМИ: 1/18 лампы: Желтая СТО: | Цепь датчика давления топлива. Давление фильтра постов низкое - данные действительны, но ниже операционного диапазона. | Возможно, жесткий старт, отсутствие старта или низкая мощность. |

![[19f00010.png]]

Цепь датчика давления топлива

### Описание цепи

Датчик давления топлива подает сигнал электронному модулю управления (ECM) для контроля давления подачи топлива непосредственно после фильтра топлива и перед его подачей на насос впрыска топлива. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления.

### Расположение компонента

Датчик давления топлива расположен на выходе топливного фильтра, монтажной головки и перед насосом впрыска топлива на промышленных двигателях QST30 с электрическими насосами подъема топлива. Используйте следующую процедуру в Руководстве по эксплуатации, QST30, Бюллетень [[4021539 — QST30 Service Manual\|4021539]] для определения местоположения датчика давления топлива.[[57-100-002 — Engine Diagrams|См. процедуру 100-002 в разделе E.]]

### Практические замечания

Код поломки 583** применяется только к промышленным двигателям QST30 с электрическими топливными подъемными насосами и цельной проводкой. Код неисправности становится активным, если давление топлива на датчиках падает ниже 103 кПа[15 psi] в течение 35 секунд.

Низкое давление фильтрованного топлива может быть вызвано одной из следующих возможных причин:

- Высокое ограничение топливного фильтра (засохший топливный фильтр)

- Высокое ограничение префильтра топлива (подключенный префильтр)

- Высокое ограничение подачи топлива

- Поврежденный или неисправный насос(ы) для подъема топлива

- Воздух в топливе.

См. Код устранения неполадок t05-583


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 583
>
> ### Fuel Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 583 PID(P): P015 SPN: FMI: 1/18 Lamp: Yellow SRT: | Fuel Pressure Sensor Circuit. Post filter pressure low - Data valid but below operational range. | Possible hard start, no start, or low power. |
>
> Fuel Pressure Sensor Circuit
>
> ### Circuit Description
>
> The fuel pressure sensor provides a signal to the electronic control module (ECM) to monitor fuel delivery pressure directly after the fuel filter, and before it is supplied to the fuel injection pump. The ECM monitors the voltage on the SIGNAL pin and converts this to a pressure value.
>
> ### Component Location
>
> The fuel pressure sensor is located on the outlet of the fuel filter head and before the fuel injection pump on QST30 industrial engines with electric fuel lift pumps. Use the following procedure in Service Manual, QST30, Bulletin [[4021539 — QST30 Service Manual\|4021539]] for fuel pressure sensor location. [[57-100-002 — Engine Diagrams|Refer to Procedure 100-002 in Section E.]]
>
> ### Shoptalk
>
> Fault Code 583 **only** applies to QST30 industrial engines with electric fuel lift pumps and a one-piece wiring harness. The fault code becomes active if fuel pressure at the sensors drops below 103 kPa \[15 psi\] for 35 seconds.
>
> Low filtered fuel pressure can be caused by one of the following possible causes:
>
> - High fuel filter restriction (plugged fuel filter)
>
> - High fuel pre-filter restriction (plugged pre-filter)
>
> - High fuel supply hose restriction
>
> - Damaged or malfunctioning fuel lift pump(s)
>
> - Air in fuel.
>
> Refer to Troubleshooting Fault Code t05-583
