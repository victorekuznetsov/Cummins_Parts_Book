---
aliases:
  - "Датчик положения педали или рычага подачи"
type: "Процедура"
doc: "99-019-085"
title_en: "Accelerator Pedal or Lever Position Sensor"
title_ru: "Датчик положения педали или рычага подачи"
modified: "2015-06-29"
engines:
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "K19"
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666070"
  - "3666214"
  - "3666266"
  - "4021442"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-085.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-085.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/K19"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/99"
  - "перевод/машинный"
---

# Accelerator Pedal or Lever Position Sensor
**Датчик положения педали или рычага подачи**

> [!abstract] Процедура · `99-019-085`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, K19, NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-085.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-085.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Педаль акселератора или датчик положения рычага будут варьироваться в зависимости от OEM. См. руководство производителя транспортного средства для конкретных процедур устранения неполадок и ремонта. Этот раздел содержит процедуры устранения неполадок и ремонта для одного типичного датчика положения педали акселератора или рычага.

Педаль акселератора или датчик положения рычага посылает сигнал в ECM, когда оператор нажимает на педаль акселератора или рычаг. Схема положения ускорителя состоит из датчика положения педали акселератора или рычага, ECM, педали акселератора / положения рычага +5 вольт, сигнала положения педали / положения рычага ускорителя и проводов возврата положения педали / положения рычага ускорителя.

![[19c01341.png]]

### Проверка сопротивления

Если имеется электронный инструмент, следите за датчиком положения ускорителя для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Отсоедините 3-контактный разъем от датчика положения ускорителя.

Подключите измерительный разъем.

![[tl8swkk.png]]

Подключите многометровый положительный (+) испытательный щуп к педали акселератора/рычажному положению +5 вольт подвода пробного соединительного провода. Подсоедините отрицательный (-) многометровый испытательный щуп к педали акселератора/рычажному месту обратного испытательного соединительного провода.

Измерьте сопротивление. Мультиметр **должен** показывать от 2000 до 3000 Ом, когда педаль акселератора освобождается (положение холостого хода) или депрессивное (положение полного топлива).

Если сопротивление **не** в пределах спецификации, датчик положения ускорителя не работает. Замените датчик положения ускорителя. См. руководство по устранению неполадок и ремонту OEM для процедур.

![[tl8swkl.png]]

Удалите многометровый щуп из педали акселератора/рычажного положения +5 вольт подвода измерительного соединительного провода и подключите его к проводу испытательного соединительного провода педали акселератора/рычажного положения.

Когда педаль акселератора находится в освобожденном (пустом) положении, измеряйте сопротивление. Мультиметр **должен** показывать от 1500 до 3000 Ом.

![[19900633.png]]

Усильте педаль акселератора (полнотопливное положение) и измерьте сопротивление. Мультиметр **должен** показывать от 250 до 1500 Ом. Это значение сопротивления **должно быть по меньшей мере на 1000 Ом ниже значения сопротивления 1500-3000 Ом, измеренного в вышеупомянутой проверке. Если значения сопротивления на двух предыдущих этапах не соответствуют спецификации, датчик положения ускорителя не работает. Заменить датчик положения ускорителя в соответствии с процедурами изготовителя транспортного средства. Если значения сопротивления находятся в пределах спецификаций, датчик положения ускорителя** должен быть проверен на короткое замыкание на землю.

![[19900634.png]]

### Проверка на замыкание на массу

Подключите многометровый положительный (+) щуп к педали акселератора/рычажному пробному соединительному проводу. Прикоснитесь к отрицательному (-) многометровому щупу к земле шасси и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19900635.png]]

Удалите многометровый положительный (+) щуп из провода обратного разъёма педали/рычага и соедините его с проводом испытательного разъёма педали/рычага/рычага. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19900636.png]]

Удалите многометровый положительный (+) щуп из провода для испытания сигнала педали/рычага положения ускорителя и соедините его с проводом для испытания подачи педали/рычага ускорителя +5 вольт. Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если значения сопротивления **не** в пределах спецификаций предыдущей проверки, датчик положения ускорителя не работает. Заменить датчик положения ускорителя в соответствии с процедурами изготовителя транспортного средства.

Если датчик положения ускорителя прошел все предыдущие проверки, подключите датчик к проводах ремня. Схема датчика положения ускорителя должна быть проверена.

![[19900637.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The accelerator pedal or lever position sensor will vary with OEM. Refer to the vehicle manufacturer's manual for the specific troubleshooting and repair procedures. This section contains troubleshooting and repair procedures for one typical accelerator pedal or lever position sensor.
>
> The accelerator pedal or lever position sensor sends a signal to the ECM when the operator pushes on the accelerator pedal or lever. The accelerator position circuit consists of the accelerator pedal or lever position sensor, the ECM, accelerator pedal/lever position +5 volt, accelerator pedal/lever position signal, and accelerator pedal/lever position return wires.
>
> ### Resistance Check
>
> If an electronic service tool is available, monitor the accelerator position sensor for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Disconnect the 3-pin connector from the accelerator position sensor.
>
> Connect the test connector.
>
> Connect the multimeter positive (+) test lead to the accelerator pedal/lever position +5 volt supply test connector wire. Connect the negative (-) multimeter test probe to the accelerator pedal/lever position return test connector wire.
>
> Measure the resistance. The multimeter **must** show between 2000 and 3000 ohms when the accelerator pedal is released (idle position) or depressed (full-fuel position).
>
> If the resistance is **not** within the specification, the accelerator position sensor has failed. Replace the accelerator position sensor. Refer to the OEM troubleshooting and repair manual for the procedures.
>
> Remove the multimeter probe from the accelerator pedal/lever position +5 volt supply test connector wire and connect it to the accelerator pedal/lever position signal test connector wire.
>
> When the accelerator pedal is in the released (idle) position, measure the resistance. The multimeter **must** show between 1500 and 3000 ohms.
>
> Depress the accelerator pedal assembly (full-fuel position) and measure the resistance. The multimeter **must** show between 250 and 1500 ohms. This resistance value **must** be at least 1000 ohms lower than the resistance value of 1500 to 3000 ohms measured in the above check. If the resistance values in the two previous steps are **not** within the specification, the accelerator position sensor has failed. Replace the accelerator position sensor according to the vehicle manufacturer's procedures. If the resistance values are within the specifications, the accelerator position sensor **must** still be checked for a short circuit to ground.
>
> ### Check for Short Circuit to Ground
>
> Connect the multimeter positive (+) probe to the accelerator pedal/lever position return test connector wire. Touch the negative (-) multimeter probe to the chassis ground and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the multimeter positive (+) probe from accelerator pedal/lever position return test connector wire and connect it to the accelerator pedal/lever position signal test connector wire. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the multimeter positive (+) probe from the accelerator pedal/lever position signal test connector wire and connect it to the accelerator pedal/lever position +5 volt supply test connector wire. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the resistance values are **not** within the specifications in the previous check, the accelerator position sensor has failed. Replace the accelerator position sensor according to the vehicle manufacturer's procedures.
>
> If the accelerator position sensor has passed all the previous checks, connect the sensor to the wiring harness. The accelerator position sensor circuit **must** still be checked.
