---
aliases:
  - "Высокое напряжение АКБ 1 — предупреждение"
type: "Процедура"
doc: "01-fc442"
title_en: "Battery 1 Voltage High - Warning"
title_ru: "Высокое напряжение АКБ 1 — предупреждение"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc442.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc442.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Battery 1 Voltage High - Warning
**Высокое напряжение АКБ 1 — предупреждение**

> [!abstract] Процедура · `01-fc442`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc442.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc442.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 442

### Высокое напряжение АКБ 1 — предупреждение

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 442 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Высокое напряжение АКБ 1 — предупреждение. | Повреждение ECM произойдет. |

![[19803586.png]]

Цепь постоянного питания от АКБ

### Описание цепи

Электронный модуль управления (ECM) получает непереключенный вход батареи через электропроводку двигателя. Существует встроенный 20-амперный предохранитель в непереключенном положительном (+) проводе батареи ремня электропроводки двигателя, чтобы защитить ремень электропроводки двигателя от перегрева. Провода возврата аккумулятора соединены непосредственно с отрицательной (-) позицией аккумулятора.

### Расположение компонента

ECM подключается к батарее с помощью OEM-проводов. Это прямое соединение обеспечивает постоянный источник питания для ECM. См. руководство OEM для определения местоположения батареи.

### Практические замечания

Неправильная проводка цепи батареи является наиболее вероятной причиной этой неисправности.

Устранение неполадок код t05-442


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 442
>
> ### Battery 1 Voltage High - Warning
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 442 PID(P): SPN: FMI: Lamp: Warning SRT: | Battery 1 voltage high - warning. | ECM damage will occur. |
>
> Unswitched Battery Supply Circuit
>
> ### Circuit Description
>
> The electronic control module (ECM) receives unswitched battery input through the engine harness. There is an in-line 20 amp fuse in the unswitched positive (+) battery wire of the engine harness to protect the engine harness from overheating. The battery return wires are connected directly to the negative (-) battery post.
>
> ### Component Location
>
> The ECM is connected to the battery by the OEM harness. This direct link provides a constant power supply for the ECM. Refer to the OEM manual for the battery location.
>
> ### Shoptalk
>
> Improper wiring of the battery circuit is the most likely cause of this fault.
>
> Refer to Troubleshooting Fault Code t05-442
