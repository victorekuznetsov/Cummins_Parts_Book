---
aliases:
  - "Выключатель генераторной установки"
type: "Процедура"
doc: "01-fc1328"
title_en: "Generator Set Circuit Breaker"
title_ru: "Выключатель генераторной установки"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1328.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1328.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Generator Set Circuit Breaker
**Выключатель генераторной установки**

> [!abstract] Процедура · `01-fc1328`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1328.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1328.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1328

### Выключатель генераторной установки

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1328 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Выключатель генераторной установки сработал. | Будет происходить сброс груза. Генератор продолжает работать. |

![[19802904.png]]

Генератор Set Circuit Breaker Circuit

### Описание цепи

Выключатель генераторной установки - это переключатель для подключения генераторной установки к шине. Выключатель открывается, когда происходят события, что заставляет генераторную установку больше не подключаться к шине. Выключатель закрывается, когда генераторная установка должна быть подключена к шине.

Этот код неисправности используется ECM для того, чтобы сообщить оператору, что из-за события генераторная установка должна быть отключена от шины.

### Расположение компонента

См. раздел E для определения местоположения клетки карты ECM.

См. документацию о клиенте/объекте/установке для определения местоположения выключателя генераторной установки.

### Практические замечания

Возможные режимы отказа - короткое замыкание, открытая цепь и выключатель генераторной установки.

Выключатель представляет собой устройство защиты от тока.

Параллельно выключатель генераторной установки действует как переключатель на генераторную установку автоподключения к системной шине и другим генераторным установкам.

См. Код устранения неполадок t05-1328


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1328
>
> ### Generator Set Circuit Breaker
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1328 PID(P): SPN: FMI: Lamp: Warning SRT: | The generator set circuit breaker has tripped. | Load dump will occur. Generator set continues to run. |
>
> Generator Set Circuit Breaker Circuit
>
> ### Circuit Description
>
> The generator set circuit breaker is the switch for the generator set's connection to the bus. The circuit breaker opens when events have occurred, which forces the generator set to no longer be connected to the bus. The circuit breaker closes when the generator set is to be connected to the bus.
>
> This fault code is used by the ECM to tell the operator that, due to an event, the generator set is to be disconnected from the bus.
>
> ### Component Location
>
> Refer to Section E for location of the ECM card cage.
>
> Refer to customer/facility/installation documentation for the location of the generator set circuit breaker.
>
> ### Shoptalk
>
> The possible failure modes are short circuit, open circuit, and failed generator set circuit breaker.
>
> The circuit breaker is an overcurrent protection device.
>
> In paralleling, the generator set circuit breaker acts as a switch to autoconnect generator set to system bus and other generator sets.
>
> Refer to Troubleshooting Fault Code t05-1328
