---
aliases:
  - "Выключатель генератора не отключился — условие возникло"
type: "Процедура"
doc: "01-fc1453"
title_en: "Generator Circuit Breaker - Failed to Open - Condition Exists"
title_ru: "Выключатель генератора не отключился — условие возникло"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1453.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1453.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Generator Circuit Breaker - Failed to Open - Condition Exists
**Выключатель генератора не отключился — условие возникло**

> [!abstract] Процедура · `01-fc1453`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1453.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1453.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1453

### Выключатель генератора не отключился — условие возникло

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1453 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Выключатель генераторной цепи не открылся. | Генераторная установка будет отключена. |

![[19802904.png]]

Генератор Set Circuit Breaker Circuit

### Описание цепи

Выключатель генераторной установки - это переключатель для соединений генераторной установки с шиной. Выключатель открывается, когда происходят события, что заставляет генераторную установку больше не подключаться к шине. Выключатель закрывается, когда генераторная установка должна быть подключена к шине.

Этот код неисправности используется модулем управления двигателем (ECM) для того, чтобы сообщить оператору, что из-за события генераторная установка может **не** отсоединиться от шины.

### Расположение компонента

См. раздел E для определения местоположения клетки карты ECM.

См. документацию о клиенте/объекте/установке для определения местоположения выключателя генераторной установки.

### Практические замечания

Возможные режимы отказа заключаются в том, что выключатель генераторной установки был **не** правильно подключен, существует открытое замыкание, короткое замыкание или короткое состояние контакта с контактом.

См. Код устранения неполадок t05-1453.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1453
>
> ### Generator Circuit Breaker - Failed to Open - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1453 PID(P): SPN: FMI: Lamp: Shutdown SRT: | The generator circuit breaker failed to open. | The generator set will shut down. |
>
> Generator Set Circuit Breaker Circuit
>
> ### Circuit Description
>
> The generator set circuit breaker is the switch for the generator set's connections to the bus. The circuit breaker opens when events have occurred, which forces the generator set to no longer be connected to the bus. The circuit breaker closes when the generator set is to be connected to the bus.
>
> This fault code is used by the engine control module (ECM) to tell the operator that, due to an event, the generator set can **not** disconnect from the bus.
>
> ### Component Location
>
> Refer to Section E for the location of the ECM card cage.
>
> Refer to customer/facility/installation documentation for the location of the generator set circuit breaker.
>
> ### Shoptalk
>
> The possible failure modes are that the generator set circuit breaker was **not** wired properly, an open circuit, shorted circuit, or short pin-to-pin condition exists.
>
> Refer to Troubleshooting Fault Code t05-1453.
