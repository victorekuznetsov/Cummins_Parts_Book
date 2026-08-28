---
aliases:
  - "Жгут проводов двигателя"
type: "Процедура"
doc: "98-019-043"
title_en: "Engine Wiring Harness"
title_ru: "Жгут проводов двигателя"
modified: "2004-05-14"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 21
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-043.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-043.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Wiring Harness
**Жгут проводов двигателя**

> [!abstract] Процедура · `98-019-043`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-05-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-043.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-043.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

Отсоедините электропровода управления электронным топливом от электронного клапана управления топливом (1).

Отсоедините подающий провод +12-VDC от затвора топлива соленоида (2).

![[19802105.png]]

Удалите зажимы для монтажа проводов.

![[19801922.png]]

Отсоедините наземный провод, разъем С5 и разъем С6 от блока двигателя.

![[19801920.png]]

Отключите разъем датчика давления в рельсах.

![[19801919.png]]

Отключите соленоид управления временем шага, если двигатель оснащен электрическим управлением временем шага.

![[19801917.png]]

Удалите три крепежных болта, обеспечивающих электронный модуль управления (ECM), в электронный модуль управления топливом.

Удалить ECM.

![[19801900.png]]

> [!warning] ОСТОРОЖНО
> Свободный или отсутствующий пост разъема ECM может привести к тому, что двигатель будет работать беспорядочно, резко расти или неожиданно гибнуть, а также к регистрации любого количества различных кодов неисправностей. Используйте 1/4-дюймовый разъем с открытым концом, чтобы удерживать джек-пост, ослабляя основные болты разъема ECM.

Удалите два соединительных болта ECM-проводов из блока ECM.

Удалите главный разъём электропроводки двигателя из ECM.

![[19801121.png]]

Отключите датчики скорости двигателя от основной электропроводки двигателя.

![[19801626.png]]

Удалите основную проводку двигателя из двигателя.

![[19801913.png]]

### Установка

Поместите основную проводку двигателя вдоль боковой части блока двигателя.

Поместите датчик скорости двигателя часть основного двигателя проводов жгута в правильном месте.

![[19801913.png]]

Установите разъём жгута проводов в сосуд ECM. Тщательно выровняйте соединительные направляющие слоты с гнездами направляющих в ECM и вставьте разъем.

![[19801855.png]]

Подключите провод электропитания +12-VDC к соленоиду отключения топлива.

![[19802006.png]]

Маршрут и зажим датчика скорости двигателя часть основного двигателя проводов жгута к местоположению датчика в корпусе маховика.

![[19801825.png]]

Подключите разъемы датчика скорости двигателя.

![[19801816.png]]

Подключите разъем датчика давления рельса.

![[19801919.png]]

Подключите разъемы C5 и C6.

![[19801812.png]]

Подключите заземляющий провод блока двигателя.

![[19801920.png]]

Подключите провод управления временем шага, если используется.

![[19801806.png]]

Подключение электронного управления топливом приводит к электронному клапану управления топливом. Включить электропроводной кабель управления топливом в щелевой канал электронного модуля управления топливом CENTRYTM.

![[19801839.png]]

Установите основные проводов двигателя, упряжьте крепления зажимов в сторону блока двигателя.

Затянуть крепежные зажимные болты.

> [!tip] Момент затяжки
> 25 Н·м [18 фунт-фут]

![[19801922.png]]

### Завершающие операции

Установить ECM. См. процедуру[[98-019-031 — Engine Control Module|019-031]].

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> Disconnect the electronic fuel control electrical wires from the electronic fuel control valve (1).
>
> Disconnect the +12-VDC supply wire from the fuel shutoff solenoid (2).
>
> Remove the harness mounting clamps.
>
> Disconnect the ground wire, C5 connector, and C6 connector from the engine block.
>
> Disconnect the rail pressure sensor connector.
>
> Disconnect the step timing control solenoid if the engine is equipped with electrical step timing control.
>
> Remove the three mounting capscrews securing the electronic control module (ECM) to the electronic fuel control module.
>
> Remove the ECM.
>
> **CAUTION · Осторожно**
> A loose or missing ECM jack post can cause the engine to run erratically, surge, or die unexpectedly, as well as to log any number of different fault codes. Use a 1/4-inch open-end wrench to hold the jack post while loosening the main engine harness ECM connector capscrews.
>
> Remove the two ECM harness connector capscrews from the ECM unit.
>
> Remove the main engine harness connector from the ECM.
>
> Disconnect the engine speed sensors from the main engine harness.
>
> Remove the main engine harness from the engine.
>
> ### Install
>
> Place the main engine harness along the side of the engine block.
>
> Place the engine speed sensor portion of the main engine harness in the correct location.
>
> Install the harness connector into the ECM receptacle. Carefully align the connector guide slots with the receptacle guide slots in the ECM and insert the connector.
>
> Connect the +12-VDC power supply wire to the fuel shutoff solenoid.
>
> Route and clamp the engine speed sensor portion of the main engine harness to the sensor location in the flywheel housing.
>
> Connect the engine speed sensor connectors.
>
> Connect the rail pressure sensor connector.
>
> Connect the C5 and C6 connectors.
>
> Connect the engine block ground wire.
>
> Connect the step timing control wire, if used.
>
> Connect the electronic fuel control leads to the electronic fuel control valve. Insert the electronic fuel control electrical wiring cable into the slotted channel of the CENTRY™ electronic fuel control module.
>
> Install the main engine harness mounting clamps to the side of the engine block.
>
> Tighten the mounting clamp capscrews.
>
> **Момент затяжки · Torque Value**
> 25 n•m [18 ft-lb]
>
> ### Finishing Steps
>
> Install ECM. Refer to procedure [[98-019-031 — Engine Control Module|019-031]].
