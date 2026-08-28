---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "82-fc341"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
modified: "2010-09-02"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc341.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc341.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `82-fc341`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc341.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc341.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 341

### Цепь постоянного питания от АКБ

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 341 PID(P): S253 SPN: 630 FMI: 2/2 лампы: Желтая СТО: | Серьезная потеря данных от ЕКМ. | Возможно, никаких заметных эффектов производительности, **или**, двигатель умирает, **или** трудности в запуске двигателя. Информация о неисправности, информация о поездке и данные мониторинга технического обслуживания могут быть неточными. |

![[19c00043.png]]

Цепь постоянного питания от АКБ

### Описание цепи

ECM получает постоянное напряжение от батарей через непереключенные провода батареи, которые подключены непосредственно к положительному (+) посту батареи. В непереключенных проводах аккумуляторов есть два встроенных 15-амперных предохранителя, чтобы защитить жгут проводов двигателя от перегрева. ECM принимает вводимую аккумуляторную батарею через провод переключателя зажигания транспортного средства, когда переключатель зажигания транспортного средства включен. Провода возврата аккумулятора соединены непосредственно с отрицательной (-) позицией аккумулятора.

### Расположение компонента

ECM подключается к батарее с помощью OEM-проводов. Это прямое соединение обеспечивает постоянный источник питания для ECM. Расположение батареи будет варьироваться в зависимости от OEM. См. руководство изготовителя машины по диагностике и ремонту.

Устранение неполадок код t05-341


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 341
>
> ### Unswitched Battery Supply Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 341 PID(P): S253 SPN: 630 FMI: 2/2 Lamp: Yellow SRT: | Severe loss of data from the ECM. | Possibly no noticeable performance effects, **or** engine dying, **or** difficulty in starting the engine. Fault information, trip information, and maintenance monitor data can be inaccurate. |
>
> Unswitched Battery Supply Circuit
>
> ### Circuit Description
>
> The ECM receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the positive (+) battery post. There are two in-line 15-amp fuses in the unswitched battery wires to protect the engine harness from overheating. The ECM receives switched battery input through the vehicle keyswitch wire when the vehicle keyswitch is turned on. The battery return wires are connected directly to the negative (-) battery post.
>
> ### Component Location
>
> The ECM is connected to the battery by the OEM harness. This direct link provides a constant power supply for the ECM. The location of the battery will vary with the OEM. Refer to the OEM troubleshooting and repair manual.
>
> Refer to Troubleshooting Fault Code t05-341
