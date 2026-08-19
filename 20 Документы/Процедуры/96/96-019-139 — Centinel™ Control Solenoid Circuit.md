---
aliases:
  - "Цепь управляющего электромагнита Centinel™"
type: "Процедура"
doc: "96-019-139"
title_en: "Centinel™ Control Solenoid Circuit"
title_ru: "Цепь управляющего электромагнита Centinel™"
modified: "2004-02-25"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-139.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-019-139.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# Centinel™ Control Solenoid Circuit
**Цепь управляющего электромагнита Centinel™**

> [!abstract] Процедура · `96-019-139`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-139.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-019-139.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

тяжелый

Соленоидные цепи - это провода подачи и возврата в проводной упряжке к каждому из соленоидов. Возвратные провода идут от электропроводки упряжки в модуле управления CentinelTM к 2-контактному разъёму соленоидных проводов, которые соединяются с каждым соленоидом. Провода питания идут от реле питания к 2-контактному разъёму соленоидных проводов, которые соединяются с каждым соленоидом.

![[05600052.png]]

Высоколошадная сила

Соленоидные цепи - это провода подачи и возврата в проводной упряжке к каждому из соленоидов. Возвращающиеся провода идут от терминала батареи к 2-контактному разъёму соленоидных проводов, которые соединяются с каждым соленоидом. Провода питания идут от электропроводки упряжки в модуле управления CentinelTM к 2-контактному разъёму соленоидных проводов, которые соединяются с каждым соленоидом.

![[05600052.png]]

Отсоедините электропроводку от модуля управления CentinelTM и проверьте наличие поврежденных контактов.

![[05400055.png]]

### Проверка сопротивления

Значение сопротивления соленоидной цепи очень низкое. Соленоидное сопротивление также чувствительно к температуре. Для того чтобы считывать точное значение сопротивления, сопротивление мультиметра ** должно быть вычтено из общего сопротивления соленоидной цепи.

![[nobox.png]]

> [!note] Примечание
> Используйте цифровой мультиметр для этой процедуры. Используйте цифровой мультиметр Cummins, номер 3377161, или мультиметр с одинаковой точностью ±1/2 процента.

Поверните мультиметр в положение ON. Установите диапазон мультиметров до самой низкой шкалы ом. Измерьте сопротивление на двух испытательных зондах. Это значение многометрового сопротивления, которое будет вычтено из значения соленоидного сопротивления.

![[ee8cok80.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Heavy-Duty
>
> The solenoid circuits are the supply and return wires in the wiring harness to each of the solenoids. The return wires go from the wiring harness at the Centinel™ control module to the 2-pin connector of the solenoid wires that connect to each solenoid. The supply wires go from the power relay to the 2-pin connector of the solenoid wires that connect to each solenoid.
>
> High-Horsepower
>
> The solenoid circuits are the supply and return wires in the wiring harness to each of the solenoids. The return wires go from the terminal of the battery to the 2-pin connector of the solenoid wires that connect to each solenoid. The supply wires go from the wiring harness at the Centinel™ control module to the 2-pin connector of the solenoid wires that connect to each solenoid.
>
> Disconnect the wiring harness from the Centinel™ control module and check for damaged pins.
>
> ### Resistance Check
>
> The resistance value of the solenoid circuit is very low. The solenoid resistance is also temperature sensitive. To read an accurate resistance value, the resistance of the multimeter **must** be subtracted from the total resistance of the solenoid circuit.
>
> **Note · Примечание**
> Use a digital multimeter for this procedure. Use Cummins digital multimeter, Part Number 3377161, or a multimeter with the same accuracy of ±1/2 percent.
>
> Turn the multimeter to the ON position. Set the multimeter range to the lowest ohm scale. Measure the resistance across the two test leads. This is the multimeter resistance value that will be subtracted from the solenoid resistance value.
