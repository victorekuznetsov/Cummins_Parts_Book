---
aliases:
  - "Выключатель стартера"
type: "Процедура"
doc: "20-013-018"
title_en: "Starter Switch"
title_ru: "Выключатель стартера"
modified: "2006-06-30"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-013-018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-013-018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Starter Switch
**Выключатель стартера**

> [!abstract] Процедура · `20-013-018`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2006-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-013-018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-013-018.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка при повторном использовании

> [!danger] ОПАСНО
> Двигатель не должен работать, а переключатель зажигания или зажигания должен находиться в положении выключения при установке или снятии генератора зажигания. Чтобы уменьшить вероятность травм или повреждения оборудования, не прикасайтесь к штифтам на генераторе зажигания при работе двигателя. Всегда используйте хорошо изолированные инструменты.

Удалите провод, соединяющий стартерный переключатель с магнитным переключателем из терминала стартера.

Подключите положительный щуп цифрового мультиметра, Часть Номер 3164488 или 3164489, к терминалу переключателя стартера и отрицательный щуп к шасси или наземному местоположению двигателя.

![[sb8tohb.png]]

При включении стартера в положение выключения **должно быть** нет**напряжение на терминале стартера. Если мультиметр указывает на напряжение, стартерный выключатель неисправен и** должен быть заменен.

![[sb800kd.png]]

Поверните стартовый переключатель в положение START.

Мультиметр **должен** указывать на напряжение системы.

![[sb800ke.png]]

Если есть **no** напряжение:

- Поверните стартовый переключатель в положение выключения.
- Подключите многометровый положительный щуп к терминалу переключателя стартера, имеющему провод, соединяющий стартерный переключатель с стартерным соленоидом.

![[sb800kf.png]]

Если мультиметр указывает на напряжение системы, то стартерный переключатель неисправен и должен быть заменен.

![[sb800kt.png]]

Если мультиметр указывает на **no** напряжение, переключатель **не** является причиной жалобы.

![[sb8tosg.png]]

Осмотрите проводку от стартера переключателя на стартер соленоид и от стартера соленоида на батарею. Замените любые сломанные или иным образом поврежденные провода.

![[sb800ki.png]]


> [!quote]- Original (English) · английский оригинал
> ### Inspect for Reuse
>
> **WARNING · Опасно**
> The engine must not be running and the ignition or keyswitch must be in the OFF position when installing or removing the ignition generator. To reduce the possibility of personal injury or equipment damage, do not touch the pins on the ignition generator when the engine is operating. Always use suitably insulated tools.
>
> Remove the wire connecting the starter switch to the magnetic switch from the starter switch terminal.
>
> Connect the positive lead of the digital multimeter, Part Number 3164488 or 3164489, to the starter switch terminal and the negative lead to a chassis or engine ground location.
>
> With the starter switch in the OFF position, there **must** be **no** voltage at the starter switch terminal. If the multimeter indicates voltage, the starter switch is malfunctioning and **must** be replaced.
>
> Turn the starter switch to the START position.
>
> The multimeter **must** indicate system voltage.
>
> If there is **no** voltage:
>
> - Turn the starter switch to the OFF position.
> - Connect the multimeter positive lead to the starter switch terminal having a wire connecting the starter switch to the starter solenoid.
>
> If the multimeter indicates system voltage, the starter switch is defective and **must** be replaced.
>
> If the multimeter indicates **no** voltage, the switch is **not** the cause of the complaint.
>
> Inspect the wiring from the starter switch to the starter solenoid and from the starter solenoid to the battery. Replace any broken or otherwise damaged wires.
