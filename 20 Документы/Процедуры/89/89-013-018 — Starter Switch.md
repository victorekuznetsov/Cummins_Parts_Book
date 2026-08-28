---
aliases:
  - "Выключатель стартера"
type: "Процедура"
doc: "89-013-018"
title_en: "Starter Switch"
title_ru: "Выключатель стартера"
modified: "2003-09-04"
engines:
  - "85017333"
families:
  - "QSK23"
manuals:
  - "4021375"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-013-018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-013-018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
  - "перевод/машинный"
---

# Starter Switch
**Выключатель стартера**

> [!abstract] Процедура · `89-013-018`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-09-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-013-018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-013-018.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка напряжения

> [!danger] ОПАСНО
> Чтобы уменьшить вероятность получения травмы, не прикасайтесь к проводам или компонентам зажигания во время работы двигателя, если только не используете надлежащим образом изолированные инструменты.

Убедитесь, что стартовый выключатель находится в положении выключения.

Удалите провод, соединяющий стартерный переключатель с магнитным переключателем из терминала стартера.

Подключите положительный (+) вывод цифрового мультиметра, номер 3377161 или цифровой мультиметр, номер 3164488, к терминалу переключателя стартера, а отрицательный (-) приведет к местоположению шасси или заземления двигателя.

![[sb8tohb.png]]

При включении стартера в положение выключения **на терминале стартового переключателя не должно быть напряжения. Если мультиметр указывает на напряжение, стартерный выключатель неисправен и **должен быть заменен.

![[sb800kd.png]]

Поверните стартовый переключатель в положение START.

Мультиметр **должен** указывать на напряжение системы.

![[sb800ke.png]]

Если нет напряжения:

- Поверните стартовый переключатель в положение выключения.
- Подключение многометрового положительного (+) приводит к тому, что стартовый выключатель терминала имеет провод, соединяющий стартерный выключатель с стартерным соленоидом.
- Поверните стартовый переключатель в положение START.

![[sb800kf.png]]

Если мультиметр указывает на напряжение системы, то стартерный переключатель неисправен и должен быть заменен.

![[13400073.png]]

Если мультиметр указывает на отсутствие напряжения, переключатель **не** является причиной проблемы.

![[sb8tosg.png]]

Осмотрите проводку от стартера переключателя на стартер соленоид и от стартера соленоида на батарею.

Замените любые сломанные или поврежденные провода.

![[sb800ki.png]]


> [!quote]- Original (English) · английский оригинал
> ### Voltage Check
>
> **WARNING · Опасно**
> To reduce the possibility of personal injury, do not touch any ignition wires or components while the engine is operating, unless using suitably insulated tools.
>
> Make sure the starter switch is in the OFF position.
>
> Remove the wire connecting the starter switch to the magnetic switch from the starter switch terminal.
>
> Connect the positive (+) lead of the digital multimeter, Part Number 3377161, or digital multimeter, Part Number 3164488, to the starter switch terminal and the negative (-) lead to a chassis or engine ground location.
>
> With the starter switch in the OFF position, there **must** be no voltage at the starter switch terminal. If the multimeter indicates voltage, the starter switch is malfunctioning and **must** be replaced.
>
> Turn the starter switch to the START position.
>
> The multimeter **must** indicate system voltage.
>
> If there is no voltage:
>
> - Turn the starter switch to the OFF position.
> - Connect the multimeter positive (+) lead to the starter switch terminal having a wire connecting the starter switch to the starter solenoid.
> - Turn the starter switch to the START position.
>
> If the multimeter indicates system voltage, the starter switch is defective and **must** be replaced.
>
> If the multimeter indicates no voltage, the switch is **not** the cause of the problem.
>
> Inspect the wiring from the starter switch to the starter solenoid and from the starter solenoid to the battery.
>
> Replace any broken or damaged wires.
