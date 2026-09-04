---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "56-013-017"
title_en: "Starter Magnetic Switch"
title_ru: "Втягивающее реле стартера"
modified: "2003-08-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33239746"
families:
  - "QSK60"
  - "QSK60 CM2150 MCRS"
manuals:
  - "4021530"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-013-017.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-013-017.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "двигатель/QSK60CM2150MCRS"
  - "группа/56"
  - "перевод/машинный"
---

# Starter Magnetic Switch
**Втягивающее реле стартера**

> [!abstract] Процедура · `56-013-017`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]]
> **Семейство:** QSK60, QSK60 CM2150 MCRS
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-08-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-013-017.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-013-017.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка при повторном использовании

Перед осмотром конкретных компонентов пусковой системы с помощью мультиметра:

- Осмотрите терминалы для свободных, сломанных или разъединенных соединений.
- Заменить или отремонтировать проводку и компоненты по мере необходимости.

![[sb8coca.png]]

> [!danger] ОПАСНО
> Убедитесь, что стартерный выключатель находится в положении выключения, чтобы уменьшить вероятность поражения электрическим током и травмы.

Удалите кабель, соединяющий магнитный переключатель с стартером соленоида из терминала магнитного переключателя.

Подключите провода цифрового мультиметра, Номер детали 3377161, к двум большим переключательным терминалам.

![[sb8toha.png]]

Установите мультиметр для измерения сопротивления.

При стартовом переключателе в положении OFF мультиметр **должен** указывать сопротивление на бесконечности.

- Если мультиметр указывает на нулевое или очень малое сопротивление, замените магнитный переключатель.
- Если мультиметр указывает на сопротивление на бесконечности, следуйте следующим инструкциям.

![[sb8toha.png]]

Поверните стартовый переключатель в положение START.

Мультиметр **должен **указывать нулевое или очень малое сопротивление. Клик будет услышан, когда стартовый переключатель будет повернут в положение START.

![[sb800ta.png]]

Если мультиметр указывает сопротивление на бесконечности с помощью стартового переключателя в положении START и щелчок **не** слышен:

- Поверните стартовый переключатель в положение выключения.
- Установите многометровую шкалу для указания напряжения постоянного тока.

![[sb800kx.png]]

Подключите положительный (+) вывод мультиметра к терминалу наземного провода магнитного переключателя, а другой - к терминалу небольшого магнитного переключателя.

Поверните стартовый переключатель в положение START.

Мультиметр будет указывать некоторое напряжение на магнитных переключателях. Если мультиметр указывает на полную динамическую изоляцию, магнитный переключатель неисправен и должен быть заменен.

![[sb800ky.png]]

Если мультиметр указывает на отсутствие напряжения, магнитный переключатель **не** является причиной жалобы. См. процедуру[[56-013-018 — Starter Switch|013-018]].

![[sb200ka.png]]

Поверните стартовый переключатель в положение выключения.

Удалите многометровые провода и подключите магнитный переключатель к стартерному соленоидному проводу.

![[sb8toma.png]]


> [!quote]- Original (English) · английский оригинал
> ### Inspect for Reuse
>
> Before inspecting specific starting system components with the multimeter:
>
> - Inspect terminals for loose, broken, or corroded connections.
> - Replace or repair wiring and components as necessary.
>
> **WARNING · Опасно**
> Be sure the starter switch is in the OFF position to reduce the possibility of electrical shock and personal injury.
>
> Remove the cable connecting the magnetic switch to the starter solenoid from the magnetic switch terminal.
>
> Connect the leads of digital multimeter, Part Number 3377161, to the two large switch terminals.
>
> Set the multimeter to measure resistance.
>
> With the starter switch in the OFF position, the multimeter **must** indicate resistance at infinity.
>
> - If the multimeter indicates zero or very little resistance, replace the magnetic switch.
> - If the multimeter indicates resistance at infinity, proceed with the following instructions.
>
> Turn the starter switch to the START position.
>
> The multimeter **must** indicate zero or very little resistance. A click will be heard when the starting switch is turned to the START position.
>
> If the multimeter indicates resistance at infinity with the starter switch in the START position and a click is **not** heard:
>
> - Turn the starter switch to the OFF position.
> - Set the multimeter scale to indicate DC voltage.
>
> Connect the positive (+) lead of the multimeter to the magnetic switch ground wire terminal and the other lead to the small magnetic switch terminal.
>
> Turn the starter switch to the START position.
>
> The multimeter will indicate some voltage across the magnetic switch terminals. If the multimeter indicates FULL SYSTEM VOLTAGE, the magnetic switch is malfunctioning and **must** be replaced.
>
> If the multimeter indicates no voltage, the magnetic switch is **not** the cause of the complaint. Refer to Procedure [[56-013-018 — Starter Switch|013-018]].
>
> Turn the starter switch to the OFF position.
>
> Remove the multimeter leads and connect the magnetic switch to the starter solenoid wire.
