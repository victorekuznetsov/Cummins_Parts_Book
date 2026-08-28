---
aliases:
  - "Контроль напряжения — очень низкое напряжение"
type: "Процедура"
doc: "82-fc598"
title_en: "Voltage Monitor - Very Low Voltage"
title_ru: "Контроль напряжения — очень низкое напряжение"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc598.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc598.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Voltage Monitor - Very Low Voltage
**Контроль напряжения — очень низкое напряжение**

> [!abstract] Процедура · `82-fc598`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc598.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc598.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 598

### Контроль напряжения — очень низкое напряжение

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 598 PID(P): P167 SPN: 167 ФМИ: 1/1 лампа: Красная СТО: | Очень низкое напряжение батареи, обнаруженное функцией монитора напряжения батареи. | Красная лампа зажигается до тех пор, пока не будет исправлено очень низкое напряжение батареи. Электронный модуль управления (ECM) может увеличить скорость холостого хода и отключить переключатель декремента холостого хода, если включено ускорение холостого хода. Двигатель будет работать непрерывно, если ICONTM активен (автомобильный **только**). |

![[19c00043.png]]

Монитор напряжения цепи поставок

### Описание цепи

ECM получает непереключенный вход батареи через OEM-проводку. В непереключенном проводе батареи упряжки OEM-проводов есть два встроенных 15-амперных предохранителя, чтобы защитить упряжку проводов двигателя от перегрева. Провода возврата аккумулятора соединены непосредственно с отрицательной (-) позицией аккумулятора.

### Расположение компонента

ECM подключается к батарее с помощью OEM-проводов. Это прямое соединение обеспечивает постоянный источник питания для ECM. Расположение батареи будет варьироваться в зависимости от OEM. См. руководство OEM для определения местоположения батареи.

### Практические замечания

Убедитесь, что источник питания без переключения ECM поступает непосредственно от батареи и **не **стартера.

Возможные причины этого кода неисправности:

- Недозаряженные батареи, вызванные неисправным генератором или регулятором.

См. Устранение неполадок код t05-598


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 598
>
> ### Voltage Monitor - Very Low Voltage
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 598 PID(P): P167 SPN: 167 FMI: 1/1 Lamp: Red SRT: | Very low battery voltage detected by the battery voltage monitor feature. | Red lamp lit until very low battery voltage condition is corrected. The electronic control module (ECM) can increase idle speed and deactivate idle decrement switch if idle speedup is enabled. The engine will run continuously if ICON™ is active (automotive **only**). |
>
> Voltage Monitor Supply Circuit
>
> ### Circuit Description
>
> The ECM receives unswitched battery input through the OEM harness. There are two in-line 15-amp fuses in the unswitched battery wire of the OEM harness to protect the engine harness from overheating. The battery return wires are connected directly to the negative (-) battery post.
>
> ### Component Location
>
> The ECM is connected to the battery by the OEM harness. This direct link provides a constant power supply for the ECM. The location of the battery will vary with the OEM. Refer to the OEM manual for the battery location.
>
> ### Shoptalk
>
> Make sure the ECM unswitched battery supply is coming directly from the battery and **not** the starter.
>
> Possible causes of this fault code:
>
> - Undercharged batteries caused by a faulty alternator or regulator.
>
> Refer to Troubleshooting Fault Code t05-598
