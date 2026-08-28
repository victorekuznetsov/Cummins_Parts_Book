---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "100-013-017"
title_en: "Starter Magnetic Switch"
title_ru: "Втягивающее реле стартера"
modified: "2003-09-03"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-013-017.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-013-017.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/100"
  - "перевод/машинный"
---

# Starter Magnetic Switch
**Втягивающее реле стартера**

> [!abstract] Процедура · `100-013-017`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-09-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-013-017.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-013-017.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!danger] ОПАСНО
> Убедитесь, что стартовый выключатель двигателя находится в положении выключения, чтобы предотвратить электрический шок и травмы.

Удалите кабель, соединяющий магнитный переключатель с пусковым соленоидом двигателя, из терминала магнитного переключателя.

Подключите провода цифрового мультиметра, номер детали. 3377161, на два больших переключателя.

![[es900kg.png]]

Установите мультиметр для измерения сопротивления (омов).

При пусковом выключателе двигателя в положении OFF мультиметр *** должен** указывать на бесконечность.

Поверните стартовый двигатель в положение START.

Мультиметр **должен** указывать нулевое или очень малое сопротивление.

![[es900wa.png]]

### Проверка напряжения

Если мультиметр указывает сопротивление на бесконечности с пусковым моторным переключателем в положении СНВ:

- Включите стартовый двигатель в положение выключения.
- Установите многометровую шкалу для считывания напряжения постоянного тока.

![[es900wb.png]]

- Подключите один мультиметр к терминалу магнитного переключателя с пометкой S, а другой приведет к хорошей земле.
- Поверните стартовый двигатель в положение START.
- Если мультиметр указывает на отсутствие напряжения, магнитный переключатель **не** является причиной жалобы. См. Starter Motor Switch - Test в этом разделе.
- Если мультиметр указывает на напряжение, магнитный переключатель неисправен и должен быть заменен.

![[es900wc.png]]

- Включите стартовый двигатель в положение выключения.
- Удалите многометровые провода и подключите магнитный переключатель к стартовому моторному соленоидному проводу.

![[es900wd.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **WARNING · Опасно**
> Make sure the starting motor switch is in the OFF position to prevent electrical shock and personal injury.
>
> Remove the cable connecting the magnetic switch to the starting motor solenoid from the magnetic switch terminal.
>
> Connect the leads of digital multimeter, Part No. 3377161, to the two large switch terminals.
>
> Set the multimeter to measure resistance (ohms).
>
> With the starting motor switch in the OFF position, the multimeter **must** indicate infinity.
>
> Turn the starting motor switch to the START position.
>
> The multimeter **must** indicate zero or very little resistance.
>
> ### Voltage Check
>
> If the multimeter indicates resistance at infinity with the starting motor switch in the START position:
>
> - Turn the starting motor switch to the OFF position.
> - Set the multimeter scale to read DC voltage.
>
> - Connect one multimeter lead to the magnetic switch terminal marked S and the other lead to a good ground.
> - Turn the starting motor switch to the START position.
> - If the multimeter indicates no voltage, the magnetic switch is **not** the cause of the complaint. Refer to Starter Motor Switch - Test in this section.
> - If the multimeter indicates voltage, the magnetic switch is defective and **must** be replaced.
>
> - Turn the starting motor switch to the OFF position.
> - Remove the multimeter leads and connect the magnetic switch to the starting motor solenoid wire.
