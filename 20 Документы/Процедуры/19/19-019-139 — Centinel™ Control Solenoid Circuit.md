---
aliases:
  - "Цепь управляющего электромагнита Centinel™"
type: "Процедура"
doc: "19-019-139"
title_en: "Centinel™ Control Solenoid Circuit"
title_ru: "Цепь управляющего электромагнита Centinel™"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-139.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-139.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Centinel™ Control Solenoid Circuit
**Цепь управляющего электромагнита Centinel™**

> [!abstract] Процедура · `19-019-139`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-139.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-139.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

**Высокая лошадиная сила**

Соленоидные цепи - это провода подачи и возврата в проводной упряжке к каждому из соленоидов. Возвращающиеся провода идут от терминала батареи к 2-контактному разъёму соленоидных проводов, которые соединяются с каждым соленоидом. Провода подачи идут от проводной упряжки в ECM к 2-контактному разъёму соленоидных проводов, которые соединяются с каждым соленоидом.

![[19400640.png]]

Отсоедините электропроводку от ECM и проверьте наличие поврежденных контактов. См. процедуру 019-999, контакты разъема - Проверка.

![[19400641.png]]

### Проверка сопротивления

Значение сопротивления соленоидной цепи очень низкое. Соленоидное сопротивление также чувствительно к температуре. Для того чтобы считывать точное значение сопротивления, сопротивление мультиметра должно быть вычтено из общего сопротивления соленоидной цепи.

![[nobox.png]]

> [!warning] ОСТОРОЖНО
> Используйте цифровой мультиметр для этой процедуры. Используйте цифровой мультиметр Cummins, номер 3377161 или мультиметр с одинаковой точностью ± 1⁄2 процента.

Поверните мультиметр в положение ON. Установите диапазон мультиметров до самой низкой шкалы ом. Измерьте сопротивление на двух испытательных зондах. Это значение многометрового сопротивления, которое будет вычтено из значения соленоидного сопротивления.

![[ee8cok80.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **High Horse Power**
>
> The solenoid circuits are the supply and return wires in the wiring harness to each of the solenoids. The return wires go from the terminal of the battery to the 2-pin connector of the solenoid wires which connect to each solenoid. The supply wires go from the wiring harness at the ECM to the 2-pin connector of the solenoid wires which connect to each solenoid.
>
> Disconnect the wiring harness from the ECM and check for damaged pins. Refer to Procedure 019-999, Connector Pins - Checking.
>
> ### Resistance Check
>
> The resistance value of the solenoid circuit is very low. The solenoid resistance is also temperature sensitive. To read an accurate resistance value, the resistance of the multimeter **must** be subtracted from the total resistance of the solenoid circuit.
>
> **CAUTION · Осторожно**
> Use a digital multimeter for this procedure. Use Cummins digital multimeter, Part Number 3377161, or a multimeter with the same accuracy of ±½ percent.
>
> Turn the multimeter to the ON position. Set the multimeter range to the lowest ohm scale. Measure the resistance across the two test leads. This is the multimeter resistance value which will be subtracted from the solenoid resistance value.
