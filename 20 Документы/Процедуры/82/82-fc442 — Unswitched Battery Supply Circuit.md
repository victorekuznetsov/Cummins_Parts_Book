---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "82-fc442"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc442.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc442.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `82-fc442`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc442.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc442.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 442

### Цепь постоянного питания от АКБ

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 442 P(P): P168 SPN: 168 ФМИ: 0/16 лампа: Желтая СТО: | Напряжение батареи выше нормального рабочего уровня. | Ни одного на выступление. |

![[19c00043.png]]

Цепь постоянного питания от АКБ

### Описание цепи

Электронный модуль управления (ECM) принимает непереключенный вход батареи через OEM-проводку. В непереключенном проводе батареи есть два встроенных 15-амперных предохранителя, чтобы защитить проводку OEM от перегрева. Провода возврата аккумулятора соединены непосредственно с отрицательной (-) позицией аккумулятора.

### Расположение компонента

ECM подключается к батарее с помощью OEM-проводов. Это прямое соединение обеспечивает постоянный источник питания для ECM. Смотрите руководство по устранению неполадок и ремонту OEM для определения местоположения батареи.

### Практические замечания

Отключите все устройства послепродажного обслуживания от цепи питания батареи. Убедитесь, что используются предохранители надлежащего размера (запалы 15-ампер).

Устранение неполадок код t05-442


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 442
>
> ### Unswitched Battery Supply Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 442 PID(P): P168 SPN: 168 FMI: 0/16 Lamp: Yellow SRT: | Battery voltage above normal operating level. | None on performance. |
>
> Unswitched Battery Supply Circuit
>
> ### Circuit Description
>
> The electronic control module (ECM) receives unswitched battery input through the OEM harness. There are two in-line 15-amp fuses in the unswitched battery wire to protect the OEM harness from overheating. The battery return wires are connected directly to the negative (-) battery post.
>
> ### Component Location
>
> The ECM is connected to the battery by the OEM harness. This direct link provides a constant power supply for the ECM. Refer to the OEM troubleshooting and repair manual for battery location.
>
> ### Shoptalk
>
> Disconnect all aftermarket devices from the battery supply circuit. Make sure the proper-size fuses are being used (15-amp fuses).
>
> Refer to Troubleshooting Fault Code t05-442
