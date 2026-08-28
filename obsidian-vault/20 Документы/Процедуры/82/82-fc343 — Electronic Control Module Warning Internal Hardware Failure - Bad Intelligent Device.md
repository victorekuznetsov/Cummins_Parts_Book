---
aliases:
  - "Предупреждение о внутреннем аппаратном отказе ЭБУ"
type: "Процедура"
doc: "82-fc343"
title_en: "Electronic Control Module Warning Internal Hardware Failure - Bad Intelligent Device or Component"
title_ru: "Предупреждение о внутреннем аппаратном отказе ЭБУ"
modified: "2014-01-23"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc343.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc343.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Electronic Control Module Warning Internal Hardware Failure - Bad Intelligent Device or Component
**Предупреждение о внутреннем аппаратном отказе ЭБУ**

> [!abstract] Процедура · `82-fc343`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2014-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc343.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc343.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 343

### Предупреждение о внутреннем аппаратном отказе ЭБУ

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 343 P(P): S254 SPN: 629 FMI: 12/12 Лампа: Желтая СТО: | Внутренняя ошибка ECM. | Возможно, ни на производительность, ни на серьезный упадок. |

![[19c00010.png]]

Электронный блок управления

### Описание цепи

ECM контролирует как выход напряжения сигнала на форсунка, так и вход ECM от датчика положения двигателя.

### Расположение компонента

ECM расположен на стороне топливного насоса двигателя.

### Практические замечания

- Отключение двигателя или наземных соединений шасси может привести к регистрации кода 343 по умолчанию. Обратите особое внимание на отрицательное соединение начального сообщения.

- Влажность в разъемах ECM также может привести к тому, что ECM введет в систему код 343 ошибки.

- Симптомы могут включать прерывистый спотыкание или грубый бег.

Примечание: Всегда рекомендуется проверять сопротивление измерительного щупа, считывая сопротивление, отображаемое инструментом при касании положительного и отрицательного щупа вместе. Вычтите это из любых показаний, принятых за сопротивление. Это позволит более точно измерить сопротивление. Примечание: **Всегда** повторно применять диэлектрическую смазку при повторном подключении электрического соединения.

См. Код устранения неполадок t05-343


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 343
>
> ### Electronic Control Module Warning Internal Hardware Failure - Bad Intelligent Device or Component
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 343 PID(P): S254 SPN: 629 FMI: 12/12 Lamp: Yellow SRT: | Internal ECM error. | Possibly none on performance, or severe derate. |
>
> Electronic Control Module
>
> ### Circuit Description
>
> The ECM monitors both signal voltage output to the injectors and ECM input from the engine position sensor.
>
> ### Component Location
>
> The ECM is located on the fuel pump side of the engine.
>
> ### Shoptalk
>
> - Loose engine or chassis ground connections can cause Fault Code 343 to be logged. Pay special attention to the negative starter post connection.
>
> - Moisture in the ECM connectors can also cause the ECM to log Fault Code 343.
>
> - Symptoms can include intermittent stumble or rough running.
>
> Note: It is **always** a good idea to check the resistance of the meter leads by reading the resistance displayed by the tool when touching the positive and negative leads together. Subtract this reading from any readings taken for resistance. This will provide a more accurate resistance measurement. Note: **Always** reapply dielectric grease when reconnecting an electrical connection.
>
> Refer to Troubleshooting Fault Code t05-343
