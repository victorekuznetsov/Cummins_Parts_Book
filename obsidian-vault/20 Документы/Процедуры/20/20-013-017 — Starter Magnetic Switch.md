---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "20-013-017"
title_en: "Starter Magnetic Switch"
title_ru: "Втягивающее реле стартера"
modified: "2006-06-30"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-013-017.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-013-017.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Starter Magnetic Switch
**Втягивающее реле стартера**

> [!abstract] Процедура · `20-013-017`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2006-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-013-017.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-013-017.pdf)

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
> Двигатель не должен работать, а переключатель зажигания или зажигания должен находиться в положении выключения при установке или снятии генератора зажигания. Чтобы уменьшить вероятность травм или повреждения оборудования, не прикасайтесь к штифтам на генераторе зажигания при работе двигателя. Всегда используйте хорошо изолированные инструменты.

Удалите кабель, соединяющий магнитный переключатель с стартером соленоида из терминала магнитного переключателя.

Подключите провода цифрового мультиметра, номер 3164488 или 3164489, к двум большим переключающим терминалам.

![[sb8toha.png]]

Установите мультиметр для измерения сопротивления (OHMS).

При стартовом переключателе в положении OFF мультиметр ** должен** указывать сопротивление на бесконечности.

- Если мультиметр указывает на нулевое сопротивление («0») или очень малое сопротивление, замените магнитный переключатель.
- Если мультиметр указывает на сопротивление на бесконечности, следуйте следующим инструкциям.

![[sb8toha.png]]

Поверните стартовый переключатель в положение START.

Мультиметр ** должен ** указывать нулевое сопротивление (0) или очень малое сопротивление. Слышный щелчок будет слышен, когда стартовый переключатель будет повернут в положение START.

![[sb800ta.png]]

Если мультиметр указывает сопротивление на бесконечности с помощью стартового переключателя в положении START и слышимого щелчка **не** слышно:

- Поверните стартовый переключатель в положение выключения.
- Установите многометровую шкалу для указания напряжения постоянного тока.

![[sb800kx.png]]

Подключите положительный щуп одного мультиметра к терминалу наземного провода магнитного переключателя, а другой приведет к терминалу небольшого магнитного переключателя.

Поверните стартовый переключатель в положение START.

Мультиметр будет указывать некоторое напряжение на магнитных переключателях. Если мультиметр указывает на полную динамическую изоляцию, магнитный переключатель неисправен и должен быть заменен.

![[sb800ky.png]]

Если мультиметр указывает на **no** напряжение, магнитный переключатель ** не** является причиной жалобы. См. процедуру[[20-013-018 — Starter Switch|013-018]].

![[sb200ka.png]]

Поверните стартовый переключатель в положение выключения.

Удалите многометровые провода и подключите магнитный переключатель к стартерному соленоидному проводу.

> [!missing]- Иллюстрация `sb8toma.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### Inspect for Reuse
>
> Before inspecting specific starting system components with the multimeter:
>
> - Inspect terminals for loose, broken, or corroded connections.
> - Replace or repair wiring and components as necessary.
>
> **WARNING · Опасно**
> The engine must not be running and the ignition or keyswitch must be in the OFF position when installing or removing the ignition generator. To reduce the possibility of personal injury or equipment damage, do not touch the pins on the ignition generator when the engine is operating. Always use suitably insulated tools.
>
> Remove the cable connecting the magnetic switch to the starter solenoid from the magnetic switch terminal.
>
> Connect the leads of the Digital Multimeter, Part Number 3164488 or 3164489, to the two large switch terminals.
>
> Set the multimeter to measure resistance (OHMS).
>
> With the starter switch in the OFF position, the multimeter **must** indicate resistance at infinity.
>
> - If the multimeter indicates ZERO ("0") or very little resistance, replace the magnetic switch.
> - If the multimeter indicates resistance at infinity, proceed with the following instructions.
>
> Turn the starter switch to the START position.
>
> The multimeter **must** indicate ZERO ("0") or very little resistance. An audible click will be heard when the starting switch is turned to the START position.
>
> If the multimeter indicates resistance at infinity with the starter switch in the START position and an audible click is **not** heard:
>
> - Turn the starter switch to the OFF position.
> - Set the multimeter scale to indicate DC voltage.
>
> Connect the positive lead of the one multimeter to the magnetic switch ground wire terminal and the other lead to the small magnetic switch terminal.
>
> Turn the starter switch to the START position.
>
> The multimeter will indicate some voltage across the magnetic switch terminals. If the multimeter indicates FULL SYSTEM VOLTAGE, the magnetic switch is malfunctioning and **must** be replaced.
>
> If the multimeter indicates **no** voltage, the magnetic switch is **not** the cause of the complaint. Refer to Procedure [[20-013-018 — Starter Switch|013-018]].
>
> Turn the starter switch to the OFF position.
>
> Remove the multimeter leads and connect the magnetic switch to starter solenoid wire.
