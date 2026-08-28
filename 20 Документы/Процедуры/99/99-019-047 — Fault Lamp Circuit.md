---
aliases:
  - "Цепь лампы неисправности"
type: "Процедура"
doc: "99-019-047"
title_en: "Fault Lamp Circuit"
title_ru: "Цепь лампы неисправности"
modified: "2015-06-29"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "35354607"
  - "35373113"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
  - "71156161"
  - "80141463"
  - "80248213"
  - "85017333"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "K19"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK23"
  - "QSK60"
  - "QSM11"
  - "QST30"
  - "QSX15"
manuals:
  - "3666070"
  - "3666113"
  - "3666184"
  - "3666214"
  - "3666266"
  - "3666415"
  - "4021419"
  - "4021442"
  - "4021674"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-047.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-047.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/K19"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QSM11"
  - "двигатель/QST30"
  - "двигатель/QSX15"
  - "группа/99"
  - "перевод/машинный"
---

# Fault Lamp Circuit
**Цепь лампы неисправности**

> [!abstract] Процедура · `99-019-047`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, K19, NT/NTA855 · ISM/QSM11, QSK23, QSK60, QSM11, QST30, QSX15
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]], [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[3666415 — ICON Idle Control System Master Repair Manual|3666415]], [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19 · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-047.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-047.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка напряжения

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.

Переведите замок зажигания в положение ON. Настройте мультиметр для измерения VDC. Вставьте многометровый свинец в янтарный сигнал предупредительной лампы и прикрепите его к многометровому щупу. Прикоснитесь к другому многометровому щупу блока двигателя. Прочитайте дисплей на мультиметре.

Мультиметр **должен** показывать напряжение батареи. Если напряжение батареи не присутствует, возникает проблема с проводом OEM-проводов при условии, что янтарная предупредительная лампа ранее была проверена.

См. руководство по устранению неполадок и ремонту OEM для процедур ремонта.

![[19c01158.png]]

Удалите свинец из янтарного сигнального контакта и вставьте его в сигнальный контакт индикатора неисправности (MIL). Прикоснитесь к другому многометровому щупу блока двигателя.

Мультиметр **должен** показывать напряжение батареи. Если напряжение батареи **не** присутствует, возникает проблема с неисправностью индикаторной лампы (MIL) провода OEM-проводов при условии, что индикаторная лампа (MIL) неисправности была ранее проверена.

См. руководство по устранению неполадок и ремонту OEM для процедур ремонта.

![[19c01158.png]]

Удалите свинец из сигнального контакта индикатора неисправности (MIL) и вставьте его в красный контакт сигнала стоп-сигнала. Прикоснитесь к другому многометровому щупу блока двигателя.

Мультиметр **должен** показывать напряжение батареи. Если напряжение батареи не присутствует, возникает проблема с проводом OEM-проводов красной стоп-сигналом при условии, что красная стоп-сигнал ранее был проверен. См. руководство по устранению неполадок и ремонту OEM для процедур ремонта.

После ремонта подсоедините все компоненты.

![[19c01158.png]]


> [!quote]- Original (English) · английский оригинал
> ### Voltage Check
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.
>
> Turn the keyswitch to the ON position. Adjust the multimeter to measure VDC. Insert the multimeter lead into the amber warning lamp signal pin and attach it to the multimeter probe. Touch the other multimeter probe to the engine block. Read the display on the multimeter.
>
> The multimeter **must** show battery voltage. If battery voltage is **not** present, there is a problem with an OEM harness wire, provided the amber warning lamp has previously been checked.
>
> Refer to the OEM troubleshooting and repair manual for repair procedures.
>
> Remove the lead from the amber warning lamp signal pin and insert it into the malfunction indicator lamp (MIL) signal pin. Touch the other multimeter probe to the engine block.
>
> The multimeter **must** show battery voltage. If battery voltage is **not** present, there is a problem with the malfunction indicator lamp (MIL) OEM harness wire, provided the malfunction indicator lamp (MIL) has been previously checked.
>
> Refer to the OEM troubleshooting and repair manual for repair procedures.
>
> Remove the lead from the malfunction indicator lamp (MIL) signal pin and insert it into the red stop lamp signal pin. Touch the other multimeter probe to the engine block.
>
> The multimeter **must** show battery voltage. If battery voltage is **not** present, there is a problem with the red stop lamp OEM harness wire, provided the red stop lamp has been previously checked. Refer to the OEM troubleshooting and repair manual for repair procedures.
>
> Connect all components after completing the repair.
