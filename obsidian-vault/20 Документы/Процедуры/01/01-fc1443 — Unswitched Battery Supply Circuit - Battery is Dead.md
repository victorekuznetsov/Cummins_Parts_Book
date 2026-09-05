---
aliases:
  - "Цепь постоянного питания от АКБ — АКБ разряжена"
type: "Процедура"
doc: "01-fc1443"
title_en: "Unswitched Battery Supply Circuit - Battery is Dead"
title_ru: "Цепь постоянного питания от АКБ — АКБ разряжена"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1443.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1443.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Unswitched Battery Supply Circuit - Battery is Dead
**Цепь постоянного питания от АКБ — АКБ разряжена**

> [!abstract] Процедура · `01-fc1443`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1443.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1443.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1443

### Цепь постоянного питания от АКБ — АКБ разряжена

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1443 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Батарея мертва. | Двигатель не запускается. |

![[19803586.png]]

Цепь постоянного питания от АКБ

### Описание цепи

Модуль управления двигателем (ECM) получает непереключенный вход батареи через жгут проводов двигателя. Существует встроенный 20-амперный предохранитель в непереключенном положительном (+) проводе батареи жгута проводов двигателя, чтобы защитить жгут проводов двигателя от перегрева. Провода возврата аккумулятора соединены непосредственно с отрицательной (-) позицией аккумулятора.

### Расположение компонента

ECM подключается к батарее с помощью OEM-проводов. Это прямое соединение обеспечивает постоянный источник питания для ECM. См. руководство по обслуживанию OEM для местоположения батареи.

### Практические замечания

Эта неисправность обычно вызвана рыхлыми или разъединенными соединениями батареи.

См. Код устранения неполадок t05-1443.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1443
>
> ### Unswitched Battery Supply Circuit - Battery is Dead
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1443 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Battery is dead. | Engine will **not** start. |
>
> Unswitched Battery Supply Circuit
>
> ### Circuit Description
>
> The engine control module (ECM) receives unswitched battery input through the engine harness. There is an inline 20-amp fuse in the unswitched positive (+) battery wire of the engine harness to protect the engine harness from overheating. The battery return wires are connected directly to the negative (-) battery post.
>
> ### Component Location
>
> The ECM is connected to the battery by the OEM harness. This direct link provides a constant power supply for the ECM. Refer to the OEM service manual for the battery location.
>
> ### Shoptalk
>
> This fault is usually caused by loose or corroded battery connections.
>
> Refer to Troubleshooting Fault Code t05-1443.
