---
aliases:
  - "Отказ контакта положения выключателя генератора — условие возникло"
type: "Процедура"
doc: "01-fc1454"
title_en: "Generator Circuit Breaker Position Contact Failed - Condition Exists"
title_ru: "Отказ контакта положения выключателя генератора — условие возникло"
modified: "2012-05-08"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1454.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1454.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Generator Circuit Breaker Position Contact Failed - Condition Exists
**Отказ контакта положения выключателя генератора — условие возникло**

> [!abstract] Процедура · `01-fc1454`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1454.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1454.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1454

### Отказ контакта положения выключателя генератора — условие возникло

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1454 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Контакт генератора выключателя не сработал. | Никаких действий со стороны ЕКМ не предпринимается. |

![[19802904.png]]

Схема генератора

### Описание цепи

Выключатель генераторной установки - это переключатель для подключения генераторной установки к шине. Выключатель открывается, когда происходят события, что заставляет генераторную установку больше не подключаться к шине. Выключатель закрывается, когда генераторная установка должна быть подключена к шине.

Этот код неисправности используется модулем управления двигателем (ECM) для того, чтобы сообщить оператору, что в результате события ECM может ** не** определить положение выключателя.

### Расположение компонента

См. раздел E для определения местоположения клетки карты ECM.

См. документацию о клиенте/объекте/установке для определения местоположения выключателя генераторной установки.

### Практические замечания

Возможные режимы отказа заключаются в том, что выключатель генераторной установки был **не** правильно подключен, существует открытое замыкание, короткое замыкание или короткое состояние контакта с контактом.

См. Код устранения неполадок t05-1454.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1454
>
> ### Generator Circuit Breaker Position Contact Failed - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1454 PID(P): SPN: FMI: Lamp: Warning SRT: | Generator circuit breaker position contact failed. | No action is taken by the ECM. |
>
> Generator Circuit
>
> ### Circuit Description
>
> The generator set circuit breaker is the switch for the generator set's connection to the bus. The circuit breaker opens when events have occurred, which forces the generator set to no longer be connected to the bus. The circuit breaker closes when the generator set is to be connected to the bus.
>
> This fault code is used by the engine control module (ECM) to tell the operator that, due to an event, the ECM can **not** determine the position of the circuit breaker.
>
> ### Component Location
>
> Refer to Section E for location of the ECM card cage.
>
> Refer to customer/facility/installation documentation for the location of the generator set circuit breaker.
>
> ### Shoptalk
>
> The possible failure modes are that the generator set circuit breaker was **not** wired properly, an open circuit, shorted circuit, or short pin-to-pin condition exists.
>
> Refer to Troubleshooting Fault Code t05-1454.
