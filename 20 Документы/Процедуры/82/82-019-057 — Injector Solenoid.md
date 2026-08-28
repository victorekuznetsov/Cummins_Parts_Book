---
aliases:
  - "Электромагнит форсунки"
type: "Процедура"
doc: "82-019-057"
title_en: "Injector Solenoid"
title_ru: "Электромагнит форсунки"
modified: "2002-06-03"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-057.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-057.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Injector Solenoid
**Электромагнит форсунки**

> [!abstract] Процедура · `82-019-057`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-057.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-057.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Соленоидные схемы форсунки представляют собой провода подачи и возврата в электропроводке привода. Провода идут от разъема ECM к 15-контактному разъему в корпусе рычага качения клапана. 15-контактный разъем соединяет внешнюю и внутреннюю проводку привода. Внутренняя проводка жгута идет на каждый топливный форсун. Три провода работают на цепях привода тормоза двигателя.

![[19200332.png]]

Штифты цепей следующие:

| Контакты с поставщиками | обратный контакт |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Кайл. № | ECM Конн. | 15-пин Конн. | Индж. Пин | ECM Конн. | 15-пин Конн. | Индж. Пин |
| 1 | 10 | 01 | А. | 09 | 02 | B |
| 2 | 08 | 03 | А. | 07 | 04 | B |
| 3 | 06 | 05 | А. | 16 | 06 | B |
| 4 | 26 | 07 | А. | 36 | 08 | B |
| 5 | 04 | 09 | А. | 03 | 10 | B |
| 6 | 02 | 11 | А. | 01 | 12 | B |

![[19200333.png]]

Удалите разъём электропроводки привода из ECM и проверьте наличие поврежденных контактов.

![[19c00178.png]]

### Проверка сопротивления

Значение сопротивления соленоидной цепи форсунки очень низкое. Соленоидное сопротивление также чувствительно к температуре. Для того чтобы считывать точное значение сопротивления, сопротивление мультиметра должно быть вычтено из общего сопротивления соленоидной цепи форсунки.

![[19800481.png]]

> [!warning] ОСТОРОЖНО
> Используйте мультиметр для этой процедуры. Используйте мультиметр Камминса, номер детали. 3377161, или метр с одинаковой точностью ±1/2 процента.

Включите мультиметр. Установите диапазон метра до самой низкой шкалы ом. Измерьте сопротивление на двух испытательных зондах. Это значение многометрового сопротивления, которое будет вычтено из значения соленоидного сопротивления форсунки.

![[ee8cok80.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The injector solenoid circuits are the supply and return wires in the actuator harness. The wires go from the ECM connector to a 15-pin connector in the rocker lever housing. The 15-pin connector connects the external and internal actuator harness. The internal harness goes to each injector. Three of the wires operate the engine brake actuator circuits.
>
> The pins of the circuits are as follows:
>
> | Supply Pin | Return Pin |  |  |  |  |  |
> |---|---|---|---|---|---|---|
> | Cyl. No. | ECM Conn. | 15-Pin Conn. | Inj. Pin | ECM Conn. | 15-Pin Conn. | Inj. Pin |
> | 1 | 10 | 01 | A | 09 | 02 | B |
> | 2 | 08 | 03 | A | 07 | 04 | B |
> | 3 | 06 | 05 | A | 16 | 06 | B |
> | 4 | 26 | 07 | A | 36 | 08 | B |
> | 5 | 04 | 09 | A | 03 | 10 | B |
> | 6 | 02 | 11 | A | 01 | 12 | B |
>
> Remove the actuator harness connector from the ECM and check for damaged pins.
>
> ### Resistance Check
>
> The resistance value of the injector solenoid circuit is very low. The solenoid resistance is also temperature sensitive. To read an accurate resistance value, the resistance of the multimeter **must** be subtracted from the total resistance of the injector solenoid circuit.
>
> **CAUTION · Осторожно**
> Use a multimeter for this procedure. Use Cummins multimeter, Part No. 3377161, or a meter with the same accuracy of ±1/2 percent.
>
> Turn the multimeter on. Set the meter range to the lowest ohm scale. Measure the resistance across the two test probes. This is the multimeter resistance value which will be subtracted from the injector solenoid resistance value.
