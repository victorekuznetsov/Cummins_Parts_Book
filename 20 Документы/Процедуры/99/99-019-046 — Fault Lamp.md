---
aliases:
  - "Лампа неисправности"
type: "Процедура"
doc: "99-019-046"
title_en: "Fault Lamp"
title_ru: "Лампа неисправности"
modified: "2012-03-21"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666214"
  - "3666266"
  - "4021419"
  - "4021442"
  - "4021674"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-046.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-046.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/99"
  - "перевод/машинный"
---

# Fault Lamp
**Лампа неисправности**

> [!abstract] Процедура · `99-019-046`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19 · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2012-03-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-046.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-046.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Предупреждающие огни кода неисправности сообщают оператору, когда обнаружена неисправность детали или системы. Янтарная лампа может иметь на себе напечатанное слово ПРЕДУПРЕЖДЕНИЕ. Красная лампа может иметь слово «стоп» на ней.

Схемы ламп с кодом неисправности состоят из лампочки, выходного сигнала лампы и источника питания VDC из схемы переключателя зажигания.

![[19c01237.png]]

### Проверка напряжения

Измерьте напряжение между каждой лампой неисправности и землей.

Переведите замок зажигания в положение ON.

Прикоснитесь к положительному (+) многометровому щупу к сигнальному терминалу янтарной лампы.

Прикоснитесь к отрицательному (-) многометровому щупу к земле шасси. Измерьте напряжение.

Повторите эту проверку для другого терминала лампы с янтарным разломом. Мультиметр ** должен** показывать напряжение батареи.

Прикоснитесь к положительному (+) многометровому щупу к сигнальному терминалу красной стоп-сигналы.

Прикоснитесь к отрицательному (-) многометровому щупу на земле шасси.

Измерьте напряжение.

Повторите эту проверку для другого терминала красной лампы неисправности. Мультиметр ** должен** показывать напряжение батареи.

Если напряжение батареи ** не присутствует**, возникает проблема с линией переключателя зажигания или лампа вышла из строя. См. руководство по устранению неполадок и ремонту OEM для процедур ремонта.

Подключите все компоненты после завершения ремонта.

![[19c01339.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The fault code warning lamps let the operator know when a part or a system fault is detected. The amber lamp can have the word WARNING printed on it. The red lamp can have the word STOP printed on it
>
> The fault code lamp circuits consist of the light bulb, lamp signal output, and VDC supply from the keyswitch circuit.
>
> ### Voltage Check
>
> Measure the voltage between each fault lamp and ground.
>
> Turn the keyswitch to the ON position.
>
> Touch the positive (+) multimeter probe to the amber warning lamp signal terminal.
>
> Touch the negative (-) multimeter probe to the chassis ground. Measure the voltage.
>
> Repeat this check for the other terminal of the amber fault lamp. The multimeter **must** show the battery voltage.
>
> Touch the positive (+) multimeter probe to the red stop lamp signal terminal.
>
> Touch the negative (-) multimeter probe to chassis ground.
>
> Measure the voltage.
>
> Repeat this check for the other terminal of the red fault lamp. The multimeter **must** show battery voltage.
>
> If battery voltage is **not** present, there is a problem with the keyswitch line or the lamp has failed. Refer to the OEM troubleshooting and repair manual for repair procedures.
>
> Connect all components after the repair is complete.
