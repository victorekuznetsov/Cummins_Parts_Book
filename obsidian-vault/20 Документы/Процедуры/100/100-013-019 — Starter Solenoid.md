---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "100-013-019"
title_en: "Starter Solenoid"
title_ru: "Втягивающее реле стартера"
modified: "2003-09-03"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 14
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-013-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-013-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/100"
  - "перевод/машинный"
---

# Starter Solenoid
**Втягивающее реле стартера**

> [!abstract] Процедура · `100-013-019`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-09-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-013-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-013-019.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Перед устранением неисправностей пускового двигателя убедитесь, что клеммы батареи **не **рыхлые или разъединены.

![[ea8cosa.png]]

Если стартовый двигатель соленоид делает **не** издавать звуковой звук, проверьте наличие свободных проводных соединений.

![[es900ka.png]]

Используйте цифровой мультиметр, Cummins Part Number 3164488, или эквивалент, для установки шкалы напряжения.

Проверьте напряжение системы на стартовом терминале соленоидной батареи двигателя.

![[es900wk.png]]

Если мультиметр указывает на системное напряжение в пусковом терминале аккумуляторной батареи, проверьте напряжение в пусковом моторном соленоидном терминале S, когда пусковой выключатель запитан.

Если мультиметр указывает на системное напряжение на терминале S, но стартер не включается, стартовый соленоид двигателя неисправен, и стартер должен быть заменен. См. процедуру[[100-013-020 — Starting Motor|013-020]].

![[es900wl.png]]

Если мультиметр **не** указывает на напряжение системы на терминале S, проверьте:

- предохранители
- Напряжение переключателя зажигания и магнитного переключателя. См. раздел «Начало работы моторного переключателя и магнитного переключателя — проверка» в этом разделе. См. процедуры[[100-013-017 — Starter Magnetic Switch|013-017]]и[[100-013-018 — Starter Switch|013-018]]
- Системы отключения безопасности

![[es900wm.png]]

### Проверка напряжения

Установите цифровой мультиметр, номер детали 3164488, для измерения напряжения постоянного тока.

Подключение многометрового положительного (+) приводит к стартеру соленоидного положительного кабельного терминала, а отрицательного (-) приводит к расположению шасси или заземления двигателя.

Мультиметр **должен** показывать напряжение с пусковым переключателем «OFF», чтобы быть нормальным.

![[sb800ki.png]]

Если мультиметр **не** указывает на напряжение, проверьте кабель, соединяющий стартер соленоида и батарею на наличие перерывов.

Также проверьте наличие свободных или разъединенных соединений.

![[sb800kk.png]]

Если мультиметр указывает на напряжение, но стартер будет **не** работать, проверьте провод, соединяющий стартер соленоид с стартерным выключателем на наличие разрывов.

Также проверьте наличие свободных или разъединенных соединений.

Обязательно проверьте на:

- предохранители
- Системы отключения двигателей приложений.

![[sb800kl.png]]

Если провод, соединяющий стартерный соленоид и стартерный выключатель, **не **свободен или поврежден, и стартер будет **не **работать, удалите кабель, соединяющий стартер и стартерный соленоид из соленоидного терминала.

Соедините многометровый положительный (+) вывод к соленоидному положительному (+) выводу, а отрицательный (-) вывод к шасси или расположению двигателя на земле.

![[sb800km.png]]

Поверните стартовый переключатель в положение «СТАРТ».

Если мультиметр указывает на напряжение, стартер соленоид неисправен и должен быть заменен.

![[sb800kn.png]]

Если мультиметр **не** указывает на напряжение, проверьте провод, соединяющий стартер соленоид с магнитным переключателем, на наличие разрывов и на наличие рыхлых или корродированных соединений.

![[sb800ko.png]]

Если провод, соединяющий стартер соленоид с магнитным переключателем, **не является рыхлым или поврежденным, и стартер будет **не работать, проверьте кабель, соединяющий стартер соленоид с пусковым двигателем, на наличие разрывов и на наличие рыхлых или корродированных соединений.

![[es900ka.png]]

Проверьте кабель, соединяющий пусковой двигатель с батареей, на наличие разрывов и на наличие рыхлых или разъединенных соединений.

![[sb8cosa.png]]

Если кабели не рыхлые или повреждены, пусковой двигатель неисправен и должен быть заменен. См. процедуру[[100-013-020 — Starting Motor|013-020]].

![[13900038.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Before troubleshooting the starting motor, make sure the battery terminals are **not** loose or corroded.
>
> If the starting motor solenoid does **not** make an audible sound, check for loose wiring connections.
>
> Use a digital multimeter, Cummins Part Number 3164488, or equivalent, to set the voltage scale.
>
> Check for system voltage at the starting motor solenoid battery terminal.
>
> If the multimeter indicates system voltage at the starting motor battery terminal, check the voltage at the starting motor solenoid S terminal, when the starting switch is energized.
>
> If the multimeter indicates system voltage at the S terminal, but the starter does **not** engage, the starting motor solenoid is malfunctioning and the starter **must** be replaced. Refer to Procedure [[100-013-020 — Starting Motor|013-020]].
>
> If the multimeter does **not** indicate system voltage at the S terminal, check:
>
> - Fuses
> - Voltage to the ignition switch and magnetic switch. Refer to "Starting Motor Switch and Magnetic Switch - Checking" in this section. Refer to Procedures [[100-013-017 — Starter Magnetic Switch|013-017]] and [[100-013-018 — Starter Switch|013-018]]
> - Application safety shutoff systems
>
> ### Voltage Check
>
> Set the digital multimeter, Part Number 3164488, to measure DC voltage.
>
> Connect the multimeter positive (+) lead to the starter solenoid positive cable terminal and the negative (-) lead to a chassis or engine ground location.
>
> The multimeter **must** show a voltage with the starter switch “OFF” to be normal.
>
> If the multimeter does **not** indicate a voltage, check the cable connecting the starter solenoid and battery for breaks.
>
> Also check for loose or corroded connections.
>
> If the multimeter indicates a voltage, but the starter will **not** operate, check the wire connecting the starter solenoid to the starter switch for breaks.
>
> Also check for loose or corroded connections.
>
> Be sure to check for:
>
> - Fuses
> - Application engine shutoff systems.
>
> If the wire connecting the starter solenoid and starter switch is **not** loose or damaged, and the starter will **not** operate, remove the cable connecting the starter and starter solenoid from the solenoid terminal.
>
> Connect the multimeter positive (+) lead to the solenoid positive (+) terminal and the negative (-) lead to the chassis or an engine ground location.
>
> Turn the starter switch to the “START” position.
>
> If the multimeter indicates a voltage, the starter solenoid is malfunctioning and **must** be replaced.
>
> If the multimeter does **not** indicate a voltage, check the wire connecting the starter solenoid to the magnetic switch for breaks, and for loose or corroded connections.
>
> If the wire connecting the starter solenoid to the magnetic switch is **not** loose or damaged and the starter will **not** operate, check the cable connecting the starter solenoid to the starting motor for breaks, and for loose or corroded connections.
>
> Check the cable connecting the starting motor to the battery for breaks, and for loose or corroded connections.
>
> If the cables are **not** loose or damaged, the starting motor is defective and **must** be replaced. Refer to Procedure [[100-013-020 — Starting Motor|013-020]].
