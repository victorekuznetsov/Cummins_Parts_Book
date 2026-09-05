---
aliases:
  - "Выключатель стартера"
type: "Процедура"
doc: "40-013-018"
title_en: "Starter Switch"
title_ru: "Выключатель стартера"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Starter Switch
**Выключатель стартера**

> [!abstract] Процедура · `40-013-018`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-018.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

> [!danger] ОПАСНО
> Убедитесь, что пусковой выключатель двигателя находится в положении выключения, чтобы уменьшить вероятность получения травмы от электрического шока.

Удалите провод, соединяющий стартовый выключатель двигателя с магнитным выключателем (маркированный «S» или START) из стартового выключателя двигателя.

Подключите положительный щуп цифрового мультиметра, номер детали 3377161, или эквивалент, к стартовому терминалу переключателя двигателя и отрицательный щуп к шасси или наземному местоположению двигателя.

![[es900we.png]]

> [!note] Примечание
> При пусковом выключателе двигателя в положении выключения **не должно** быть напряжение на стартовом выключателе двигателя. Если счетчик указывает напряжение, пусковой выключатель двигателя неисправен и должен быть заменен.

![[sb800kd.png]]

Поверните стартовый двигатель в положение START.

Мультиметр **должен** указывать на напряжение системы.

![[sb800ks.png]]

Если нет напряжения:

- Включите стартовый двигатель в положение выключения.
- Подключите многометровый положительный щуп к пусковому выключателю двигателя, имеющему провод, соединяющий пусковой выключатель двигателя с пусковым соленоидным терминалом «В».

![[sb800kf.png]]

Поверните стартовый переключатель в положение START.

Если счетчик указывает на системное напряжение на входном терминале пускового переключателя двигателя, то пусковой переключатель двигателя является **не** причиной жалобы.

Проверьте проводку от стартового переключателя до стартового моторного соленоидного терминала «В», а от стартового моторного соленоида до аккумулятора для сломанных или поврежденных проводов.

![[es900wi.png]]

Если счетчик не указывает на напряжение, переключатель неисправен и должен быть заменен.

Проверьте проводку от стартового переключателя до стартового моторного соленоидного терминала «В» и от стартового моторного соленоида до аккумулятора для сломанных или поврежденных проводов.

![[es900wj.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> **WARNING · Опасно**
> Be sure the starting motor switch is in the OFF position to reduce the possibility of personal injury from electrical shock.
>
> Remove the wire connecting the starting motor switch to the magnetic switch (marked "S" or START) from the starting motor switch terminal.
>
> Connect the positive lead of digital multimeter, Part Number 3377161, or equivalent, to the starting motor switch terminal and the negative lead to a chassis or engine ground location.
>
> **Note · Примечание**
> With the starting motor switch in the OFF position, there **must not** be voltage at the starting motor switch terminal. If the meter indicates voltage, the starting motor switch is malfunctioning and **must** be replaced.
>
> Turn the starting motor switch to the START position.
>
> The multimeter **must** indicate system voltage.
>
> If there is no voltage:
>
> - Turn the starting motor switch to the OFF position.
> - Connect the multimeter positive lead to the starting motor switch terminal having a wire connecting the starting motor switch to the starting motor solenoid “B” terminal.
>
> Turn the starter switch to the START position.
>
> If the meter indicates system voltage at the starting motor switch input terminal, the starting motor switch is **not** the cause of the complaint.
>
> Check the wiring from the starting switch to the starting motor solenoid “B” terminal, and from the starting motor solenoid to the battery for broken or damaged wires.
>
> If the meter indicates no voltage, the switch is defective and **must** be replaced.
>
> Check the wiring from the starting switch to the starting motor solenoid "B" terminal and from the starting motor solenoid to the battery for broken or damaged wires.
