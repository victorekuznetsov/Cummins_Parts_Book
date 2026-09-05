---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "35-013-019-tr"
title_en: "Starter Solenoid"
title_ru: "Втягивающее реле стартера"
modified: "2009-01-23"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-013-019-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-013-019-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Starter Solenoid
**Втягивающее реле стартера**

> [!abstract] Процедура · `35-013-019-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2009-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-013-019-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-013-019-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка напряжения

Используйте цифровой мультиметр, номер 3377161, с коммутатором, установленным в положение VDC.

Подключение многометрового положительного (+) приводит к стартеру соленоидного положительного (+) кабельного терминала, а отрицательного (-) приводит к расположению шасси или заземления двигателя.

Мультиметр **должен** показывать напряжение с выключателем стартера, чтобы быть нормальным.

![[sb800ki.png]]

Если мультиметр **не** указывает на напряжение, проверьте кабель, соединяющий стартер соленоида и батарею на наличие перерывов. Кроме того, проверьте наличие свободных или разъединенных соединений.

![[sb800kk.png]]

Если мультиметр указывает напряжение, но стартер будет **не** работать, проверьте провод, соединяющий стартер соленоид с стартерным выключателем для перерывов, а также проверьте наличие свободных или разъединенных соединений.

![[sb800kl.png]]

Если провод, соединяющий стартер соленоид и стартерный выключатель, **не **свободен или поврежден, и стартер будет **не **работать:

- Удалите кабель, соединяющий стартер и стартер соленоида из соленоидного терминала.
- Соедините многометровый положительный (+) вывод к соленоидному положительному (+) выводу, а отрицательный (-) вывод к шасси или расположению двигателя на земле.

![[sb800km.png]]

Поверните стартовый переключатель в положение START.

Если мультиметр указывает на напряжение, стартер соленоид неисправен и должен быть заменен.

![[sb800kn.png]]

Если мультиметр **не** указывает на напряжение, проверьте провод, соединяющий стартер соленоид с магнитным переключателем, на наличие разрывов и на наличие рыхлых или корродированных соединений.

![[sb800ko.png]]

Если провод, соединяющий стартер соленоид с магнитным переключателем, **не является свободным или поврежденным, и стартер будет **не работать:

- Проверьте кабель, соединяющий стартер соленоид с пусковым двигателем для перерывов и для рыхлых или коррозионных соединений.

![[sb200kb.png]]

Проверьте кабель, соединяющий пусковой двигатель с батареей, на наличие разрывов и на наличие рыхлых или разъединенных соединений.

![[sb8cosa.png]]

Если кабели не рыхлые или повреждены, пусковой двигатель неисправен и должен быть заменен.

![[sb200ma.png]]


> [!quote]- Original (English) · английский оригинал
> ### Voltage Check
>
> Use digital multimeter, Part Number 3377161, with the switch set to the VDC position
>
> Connect the multimeter positive (+) lead to the starter solenoid positive (+) cable terminal and the negative (-) lead to a chassis or engine ground location.
>
> The multimeter **must** show a voltage with the starter switch off to be normal.
>
> If the multimeter does **not** indicate a voltage, check the cable connecting the starter solenoid and battery for breaks. Also, check for loose or corroded connections.
>
> If the multimeter indicates a voltage but the starter will **not** operate, check the wire connecting the starter solenoid to the starter switch for breaks, and also check for loose or corroded connections.
>
> If the wire connecting the starter solenoid and starter switch is **not** loose or damaged, and the starter will **not** operate:
>
> - Remove the cable connecting the starter and starter solenoid from the solenoid terminal.
> - Connect the multimeter positive (+) lead to the solenoid positive (+) terminal and the negative (-) lead to the chassis or an engine ground location
>
> Turn the starter switch to the START position.
>
> If the multimeter indicates a voltage, the starter solenoid is malfunctioning and **must** be replaced.
>
> If the multimeter does **not** indicate a voltage, check the wire connecting the starter solenoid to the magnetic switch for breaks and for loose or corroded connections.
>
> If the wire connecting the starter solenoid to the magnetic switch is **not** loose or damaged, and the starter will **not** operate:
>
> - Check the cable connecting the starter solenoid to the starting motor for breaks and for loose or corroded connections.
>
> Check the cable connecting the starting motor to the battery for breaks and for loose or corroded connections.
>
> If the cables are **not** loose or damaged, the starting motor is defective and **must** be replaced.
