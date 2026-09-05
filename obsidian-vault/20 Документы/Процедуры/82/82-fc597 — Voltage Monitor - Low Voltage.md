---
aliases:
  - "Контроль напряжения — низкое напряжение"
type: "Процедура"
doc: "82-fc597"
title_en: "Voltage Monitor - Low Voltage"
title_ru: "Контроль напряжения — низкое напряжение"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc597.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc597.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Voltage Monitor - Low Voltage
**Контроль напряжения — низкое напряжение**

> [!abstract] Процедура · `82-fc597`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc597.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc597.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 597

### Контроль напряжения — низкое напряжение

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 597 PID(P): P167 SPN: 67 ФМИ: 1/18 лампы: Желтая СТО: | ICONTM перезапустил двигатель три раза за 7 часов из-за низкого напряжения батареи. | Двигатель будет работать непрерывно. Система ICONTM будет отключена **не**. Аксессуары будут **не** |

![[19803221.png]]

Монитор напряжения цепи поставок

### Описание цепи

Электронный модуль управления (ECM) принимает непереключенный вход батареи через OEM-проводку. В непереключенном проводе батареи упряжки OEM-проводов есть два встроенных 15-амперных предохранителя, чтобы защитить упряжку проводов двигателя от перегрева. Провода возврата аккумулятора соединены непосредственно с отрицательной (-) позицией аккумулятора.

### Расположение компонента

ECM подключается к батарее с помощью OEM-проводов. Это прямое соединение обеспечивает постоянный источник питания для ECM. Расположение батареи будет варьироваться в зависимости от OEM. Смотрите руководство по устранению неполадок и ремонту OEM для местоположения батареи.

### Практические замечания

Убедитесь, что источник питания отключённой батареи ECM поступает непосредственно от батареи, а не от стартера.

Возможны следующие причины этой ошибки:

- Подзаряженные батареи, вызванные неисправным генератором или регулятором

- Высокоточные устройства на транспортном средстве, такие как холодильники, усилители радиосвязи граждан, многочисленные внешние огни или другие аксессуары.

См. Код устранения неполадок t05-597


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 597
>
> ### Voltage Monitor - Low Voltage
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 597 PID(P): P167 SPN: 67 FMI: 1/18 Lamp: Yellow SRT: | ICON™ has restarted the engine three times in 7 hours due to low battery voltage. | The engine will run continuously. The ICON™ system will **not** be disabled. Accessories will **not** be on. |
>
> Voltage Monitor Supply Circuit
>
> ### Circuit Description
>
> The electronic control module (ECM) receives unswitched battery input through the OEM harness. There are two in-line 15-amp fuses in the unswitched battery wire of the OEM harness to protect the engine harness from overheating. The battery return wires are connected directly to the negative (-) battery post.
>
> ### Component Location
>
> The ECM is connected to the battery by the OEM harness. This direct link provides a constant power supply for the ECM. The location of the battery will vary with the OEM. Refer to the OEM troubleshooting and repair manual for the battery location.
>
> ### Shoptalk
>
> Make certain that the ECM unswitched battery supply is coming directly from the battery and **not** the starter.
>
> The following are possible causes of this fault:
>
> - Undercharged batteries caused by a faulty alternator or regulator
>
> - High-current devices on the vehicle such as refrigerators, citizens band radio amplifiers, numerous exterior lights, or other accessories.
>
> Refer to Troubleshooting Fault Code t05-597
