---
aliases:
  - "Диагностика драйвера регулятора напряжения"
type: "Процедура"
doc: "01-fc1331"
title_en: "Voltage Regulator Driver Diagnostic"
title_ru: "Диагностика драйвера регулятора напряжения"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1331.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1331.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Voltage Regulator Driver Diagnostic
**Диагностика драйвера регулятора напряжения**

> [!abstract] Процедура · `01-fc1331`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1331.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1331.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1331

### Диагностика драйвера регулятора напряжения

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1331 P(P): СПН: ФМИ: Лампа: Отключение SRT: | Диагностика драйвера регулятора напряжения выявила состояние короткого замыкания. | Генератор будет отключен. |

![[19802802.png]]

Водительская схема регулятора напряжения

### Описание цепи

ECM проверяет драйвер регулятора напряжения, чтобы убедиться, что он работает правильно. ECM использует код неисправности, чтобы сообщить оператору, что ECM больше не управляет регулятором напряжения.

ECM контролирует напряжение (нет напряжения будет срабатывать код 1331 по умолчанию) и может быть вызвано короткими замыканиями, неисправным регулятором напряжения или драйвером регулятора напряжения в ECM.

### Расположение компонента

См. раздел E для определения местоположения регулятора напряжения.

### Практические замечания

Возможные режимы отказа - короткое замыкание, короткое к земле и потеря напряжения внутри ECM.

Модулированная схема с импульсной шириной регулятора напряжения либо закорочена высоко, либо низко. Регулятор напряжения импульсной ширины модулированного драйвера сам закорачивается или въезжает в закороченную цепь.

Водитель регулятора напряжения находится на базовой плате. Если водитель сам неисправен, то необходимо заменить базовую плату.

См. Код устранения неполадок t05-1331


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1331
>
> ### Voltage Regulator Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1331 PID(P): SPN: FMI: Lamp: Shutdown SRT: | The voltage regulator driver diagnostic has detected a short circuit condition. | Generator set will shut down. |
>
> Voltage Regulator Driver Circuit
>
> ### Circuit Description
>
> The ECM checks the voltage regulator driver to make certain it is operating correctly. The ECM uses fault code to inform the operator that the ECM is no longer driving the voltage regulator.
>
> The ECM monitors the voltage (no voltage will trip Fault Code 1331) and can be caused by short circuits, failed voltage regulator, or a voltage regulator driver in the ECM.
>
> ### Component Location
>
> Refer to Section E for location of the voltage regulator.
>
> ### Shoptalk
>
> The possible failure modes are short circuit, short to ground, and loss of voltage inside the ECM.
>
> The voltage regulator pulse width modulated circuit is either shorted high or low. The voltage regulator pulse width modulated driver is shorted itself or is driving into a shorted circuit.
>
> The voltage regulator driver is on the base board. If the driver itself is bad, the base board **must** be replaced.
>
> Refer to Troubleshooting Fault Code t05-1331
