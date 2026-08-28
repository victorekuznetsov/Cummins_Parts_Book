---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "20-013-019"
title_en: "Starter Solenoid"
title_ru: "Втягивающее реле стартера"
modified: "2006-06-30"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-013-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-013-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Starter Solenoid
**Втягивающее реле стартера**

> [!abstract] Процедура · `20-013-019`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2006-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-013-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-013-019.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка напряжения

Используйте мультиметр, номер 3164488 или 3164489, и установите его для измерения напряжения постоянного тока.

Подключение многометрового положительного (+) приводит к стартеру соленоидного положительного (+) кабельного терминала, а отрицательного (-) приводит к соединению аккумуляторного кабеля в пусковом двигателе. Мультиметр **должен** показывать напряжение системы.

![[sb800ki.png]]

Если мультиметр **не** указывает на системное напряжение, проверьте аккумулятор на запуск кабеля двигателя для неработающих, рыхлых или разъединенных соединений.

![[sb800kk.png]]

Если мультиметр указывает на системное напряжение, но пусковой двигатель будет **не** работать, проверьте провод, соединяющий стартер соленоид с стартерным выключателем для сломанных, рыхлых или корродированных соединений.

![[sb800kl.png]]

Если провод, соединяющий стартер соленоид и стартерный выключатель, **не** свободен или поврежден, и стартер **не** работает:

- Удалите кабель, соединяющий пусковой двигатель и стартер соленоида из соленоидного терминала.
- Соедините многометровый положительный (+) вывод к соленоидному положительному (+) выводу и отрицательный (-) вывод к шасси или заземлению двигателя.

![[sb800km.png]]

Поверните стартовый переключатель в положение START.

Если мультиметр указывает на напряжение системы, стартер соленоида неисправен и должен быть заменен.

![[sb800kn.png]]

Если мультиметр **не** указывает на напряжение системы, проверьте провод, соединяющий стартер соленоид с магнитным переключателем для сломанных, рыхлых или корродированных соединений.

![[sb800ko.png]]

Если провод, соединяющий стартер соленоид с магнитным переключателем, **не является свободным или поврежденным, и пусковой двигатель будет **не работать:

- Проверьте кабель, соединяющий стартер соленоид с пусковым двигателем для сломанных, рыхлых или коррозионных соединений.

![[sb800kp.png]]

Проверьте кабель, соединяющий стартер с батареей для сломанных, рыхлых или коррозийных соединений.

![[sb8cosa.png]]

Если кабели не рыхлые или повреждены, пусковой двигатель неисправен и должен быть заменен.

![[sb2cosa.png]]


> [!quote]- Original (English) · английский оригинал
> ### Voltage Check
>
> Use the multimeter, Part Number 3164488 or 3164489, and set it to measure DC voltage.
>
> Connect the multimeter positive (+) lead to the starter solenoid positive (+) cable terminal and the negative (-) lead to the battery cable connection at the starting motor. The multimeter **must** show system voltage.
>
> If the multimeter does **not** indicate system voltage, check the battery to starting motor cable for broken, loose, or corroded connections.
>
> If the multimeter indicates system voltage, but the starting motor will **not** operate, check the wire connecting the starter solenoid to the starter switch for broken, loose, or corroded connections.
>
> If the wire connecting the starter solenoid and starter switch is **not** loose or damaged and the starter will **not** operate:
>
> - Remove the cable connecting the starting motor and starter solenoid from the solenoid terminal.
> - Connect the multimeter positive (+) lead to the solenoid positive (+) terminal and the negative (-) lead to a chassis or engine ground.
>
> Turn the starter switch to the START position.
>
> If the multimeter indicates system voltage, the starter solenoid is malfunctioning and **must** be replaced.
>
> If the multimeter does **not** indicate system voltage, check the wire connecting the starter solenoid to the magnetic switch for broken, loose, or corroded connections.
>
> If the wire connecting the starter solenoid to the magnetic switch is **not** loose or damaged and the starting motor will **not** operate:
>
> - Check the cable connecting the starter solenoid to the starting motor for broken, loose, or corroded connections.
>
> Check the cable connecting the starter to the battery for broken, loose, or corroded connections.
>
> If the cables are **not** loose or damaged, the starting motor is defective and **must** be replaced.
