---
aliases:
  - "Выключатель стартера"
type: "Процедура"
doc: "100-013-018"
title_en: "Starter Switch"
title_ru: "Выключатель стартера"
modified: "2003-09-03"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-013-018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/100-013-018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/100"
  - "перевод/машинный"
---

# Starter Switch
**Выключатель стартера**

> [!abstract] Процедура · `100-013-018`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-09-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-013-018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/100-013-018.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка

> [!danger] ОПАСНО
> Убедитесь, что стартовый выключатель двигателя находится в положении выключения, чтобы предотвратить электрический шок и травмы.

Удалите провод, соединяющий стартовый выключатель двигателя с магнитным выключателем (маркированный S или START) из стартового выключателя двигателя.

Подключите положительный (+) вывод цифрового мультиметра, Номер детали 3377161, к стартовому выключателю двигателя, а отрицательный (-) приведет к местоположению шасси или заземления двигателя.

![[es900we.png]]

> [!note] Примечание
> При пусковом выключателе двигателя в положении выключения ** не должно** быть напряжение на стартовом выключателе двигателя. Если мультиметр указывает на напряжение, пусковой выключатель двигателя неисправен и ** должен быть заменен.

![[sb800kd.png]]

Поверните стартовый двигатель в положение START. Мультиметр ** должен** указывать на напряжение системы.

![[sb800ks.png]]

Если нет напряжения:

- Включите стартовый двигатель в положение выключения.
- Подключите многометровый положительный щуп к стартовому терминалу переключателя двигателя, имеющему провод, соединяющий стартовый переключатель двигателя с стартовым терминалом соленоида В.

![[sb800kf.png]]

Поверните стартовый переключатель в положение START. Если мультиметр указывает на системное напряжение на входном терминале пускового переключателя двигателя, то пусковой переключатель двигателя является ** не** причиной жалобы.

Осмотрите проводку от стартового двигателя переключателя на стартовый двигатель соленоид B терминала и от стартового двигателя соленоида к батарее от поврежденных или сломанных проводов.

![[es900ki.png]]

Если мультиметр указывает на отсутствие напряжения, переключатель неисправен и ** должен быть заменен.

![[es900kh.png]]


> [!quote]- Original (English) · английский оригинал
> ### Test
>
> **WARNING · Опасно**
> Make sure the starting motor switch is in the OFF position to prevent electrical shock and personal injury.
>
> Remove the wire connecting the starting motor switch to the magnetic switch (marked S or START) from the starting motor switch terminal.
>
> Connect the positive (+) lead of digital multimeter, Part Number 3377161, to the starting motor switch terminal and the negative (-) lead to a chassis or engine ground location.
>
> **Note · Примечание**
> With the starting motor switch in the OFF position, there **must not** be voltage at the starting motor switch terminal. If the multimeter indicates voltage, the starting motor switch is malfunctioning and **must** be replaced.
>
> Turn the starting motor switch to the START position. The multimeter **must** indicate system voltage.
>
> If there is no voltage:
>
> - Turn the starting motor switch to the OFF position.
> - Connect the multimeter positive lead to the starting motor switch terminal having a wire connecting the starting motor switch to the starting motor solenoid B terminal.
>
> Turn the starter switch to the START position. If the multimeter indicates system voltage at the starting motor switch input terminal, the starting motor switch is **not** the cause of the complaint.
>
> Inspect the wiring from the starting motor switch to the starting motor solenoid B terminal and from the starting motor solenoid to the battery from damaged or broken wires.
>
> If the multimeter indicates no voltage, the switch is defective and **must** be replaced.
