---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "40-013-017-tr"
title_en: "Starter Magnetic Switch"
title_ru: "Втягивающее реле стартера"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 10
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-017-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-017-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Starter Magnetic Switch
**Втягивающее реле стартера**

> [!abstract] Процедура · `40-013-017-tr`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-017-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-017-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

> [!danger] ОПАСНО
> Убедитесь, что стартовый выключатель двигателя находится в положении выключения, чтобы предотвратить электрический шок и травмы.

Удалите кабель, соединяющий магнитный переключатель с пусковым соленоидом двигателя, из терминала магнитного переключателя.

Подключите провода цифрового мультиметра, номер 3377161, или эквивалент, к двум большим переключающим терминалам.

![[ea900wb.png]]

Установите мультиметр для измерения сопротивления (OHMS).

При пусковом выключателе двигателя в положении OFF мультиметр **должен** указывать сопротивление на бесконечности.

Поверните стартовый двигатель в положение START.

Мультиметр **должен **указывать нулевое или очень малое сопротивление.

![[es900wa.png]]

Если мультиметр указывает сопротивление на бесконечности с пусковым моторным переключателем в положении СНВ:

- Включите стартовый двигатель в положение выключения.
- Установите многометровую шкалу для считывания напряжения постоянного тока.

![[es900wb.png]]

- Подключите один многометровый вывод к магнитному переключателю с пометкой «S», а другой ведет к земле.
- Поверните стартовый двигатель в положение START.
- Если мультиметр указывает на отсутствие напряжения, магнитный переключатель **не** является причиной жалобы.
- Если мультиметр указывает на напряжение, магнитный переключатель неисправен и должен быть заменен.

![[es900wc.png]]

- Включите стартовый двигатель в положение выключения.
- Удалите многометровые провода и подключите магнитный переключатель к стартовому моторному соленоидному проводу.

![[es900wd.png]]

### Проверка сопротивления

> [!danger] ОПАСНО
> Убедитесь, что стартерный выключатель двигателя находится в положении OFF, чтобы уменьшить вероятность получения травмы от электрического шока.

Удалите кабель, соединяющий магнитный переключатель с стартером соленоида двигателя от терминала магнитного переключателя.

Подключите провода цифрового мультиметра, номер 3377161, или эквивалент, к двум большим переключающим терминалам.

Установите цифровой мультиметр, номер 3377161, для измерения сопротивления (омов).

![[ea900wb.png]]

Подключение ведет к двум большим переключателям.

При включении стартера в положение выключения мультиметр **должен** указывать сопротивление более 100k Ом.

Поверните стартовый двигатель в положение START.

Мультиметр **должен **указывать менее 10 Ом. Если **не** в пределах спецификаций, замените стартерный магнитный переключатель в соответствии с инструкциями производителя.

![[es900wa.png]]

### Проверка напряжения

Если мультиметр указывает сопротивление более 100k Ом при включении стартера в положение START:

- Включите стартовый двигатель в положение выключения.
- Установите многометровую шкалу для считывания напряжения постоянного тока.

![[es900wb.png]]

- Подключите один многометровый вывод к магнитному переключателю с пометкой «S», а другой ведет к земле.
- Поверните стартовый двигатель в положение START.
- Если мультиметр указывает на отсутствие напряжения, магнитный переключатель **не** является причиной жалобы. Видишь?[[40-013-018 — Starter Switch|Процедура 013-018]]. Если стартерный магнитный переключатель **не** в пределах спецификации, замените переключатель согласно инструкциям изготовителя.

![[es900wc.png]]

- Включите стартовый двигатель в положение выключения.
- Удалите многометровые провода и подключите магнитный переключатель к стартерному моторному соленоидному проводу.

![[es900wd.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> **WARNING · Опасно**
> Be sure the starting motor switch is in the OFF position to prevent electrical shock and personal injury.
>
> Remove the cable connecting the magnetic switch to the starting motor solenoid from the magnetic switch terminal.
>
> Connect the leads of digital multimeter, Part Number 3377161, or equivalent, to the two large switch terminals.
>
> Set the multimeter to measure resistance (OHMS).
>
> With the starting motor switch in the OFF position, the multimeter **must** indicate resistance at infinity.
>
> Turn the starting motor switch to the START position.
>
> The multimeter **must** indicate zero or very little resistance.
>
> If the multimeter indicates resistance at infinity with the starting motor switch in the START position:
>
> - Turn the starting motor switch to the OFF position.
> - Set the multimeter scale to read DC voltage.
>
> - Connect one multimeter lead to the magnetic switch terminal marked "S" and the other lead to the ground.
> - Turn the starting motor switch to the START position.
> - If the multimeter indicates no voltage, the magnetic switch is **not** the cause of the complaint.
> - If the multimeter indicates voltage, the magnetic switch is defective and **must** be replaced.
>
> - Turn the starting motor switch to the OFF position.
> - Remove the multimeter leads, and connect the magnetic switch to the starting motor solenoid wire.
>
> ### Resistance Check
>
> **WARNING · Опасно**
> Be sure the starter motor switch is in the OFF position to reduce the possibility of personal injury from electrical shock.
>
> Remove the cable connecting the magnetic switch to the starter motor solenoid from the magnetic switch terminal.
>
> Connect the leads of the digital multimeter, Part Number 3377161, or equivalent, to the two large switch terminals.
>
> Set the digital multimeter, Part Number 3377161, to measure resistance (ohms).
>
> Connect the leads to the two large switch terminals.
>
> With the starter motor switch in the OFF position, the multimeter **must** indicate resistance greater than 100k ohms.
>
> Turn the starter motor switch to the START position.
>
> The multimeter **must** indicate less than 10 ohms. If **not** within specifications, replace the starter magnetic switch according to the manufacturer's instructions.
>
> ### Voltage Check
>
> If the multimeter indicates resistance greater than 100k ohms with the starter motor switch in the START position:
>
> - Turn the starter motor switch to the OFF position.
> - Set the multimeter scale to read DC voltage.
>
> - Connect one multimeter lead to the magnetic switch terminal marked "S" and the other lead to the ground.
> - Turn the starter motor switch to the START position.
> - If the multimeter indicates no voltage, the magnetic switch is **not** the cause of the complaint. Refer to [[40-013-018 — Starter Switch|Procedure 013-018]]. If the starter magnetic switch is **not** within specification, replace the switch according to the manufacturer's instructions.
>
> - Turn the starter motor switch to the OFF position.
> - Remove the multimeter leads, and connect the magnetic switch to the starter motor solenoid wire.
