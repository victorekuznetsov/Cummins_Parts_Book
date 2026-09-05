---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "89-013-017"
title_en: "Starter Magnetic Switch"
title_ru: "Втягивающее реле стартера"
modified: "2003-09-04"
engines:
  - "85017333"
families:
  - "QSK23"
manuals:
  - "4021375"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-013-017.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-013-017.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
  - "перевод/машинный"
---

# Starter Magnetic Switch
**Втягивающее реле стартера**

> [!abstract] Процедура · `89-013-017`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-09-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-013-017.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-013-017.pdf)

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

Удалите кабель, соединяющий магнитный переключатель с стартером соленоида из терминала магнитного переключателя.

Подключите провода цифрового мультиметра, Part Number 3377161, или Digital Multimeter, Part Number 3164488, к двум большим переключающим терминалам.

![[sb8toha.png]]

Установите мультиметр для измерения сопротивления (омов).

При выключении стартера мультиметр **должен** указывать сопротивление на бесконечности, открытой цепи.

Поверните стартовый переключатель в положение START.

Мультиметр **должен** указывать на почти нулевое сопротивление, замкнутую цепь.

![[sb800ta.png]]

Если мультиметр указывает сопротивление на бесконечности с помощью стартового переключателя в положении START:

- Выключите стартер.
- Удалите проволоку, которая подключена к одному из небольших магнитных переключателей.

![[sb800kx.png]]

- Установите многометровую шкалу, чтобы указать вольты, 24-VDC или более.
- Подключите положительный (+) провод мультиметра к наземному терминалу магнитного переключателя, а другой - к наземному проводу.
- Поверните стартовый переключатель в положение START.
- Если мультиметр указывает на напряжение электрической системы транспортного средства, магнитный переключатель неисправен и должен быть заменен.

![[13400074.png]]

- Если мультиметр **не** указывает на напряжение, подсоедините положительный (+) вывод мультиметра к малому положительному (+) выводу на магнитном переключателе, а отрицательный мультиметр ведет к проволоке.
- Поверните стартовый переключатель в положение START.
- Если мультиметр указывает на напряжение электрической системы транспортного средства, магнитный переключатель неисправен и должен быть заменен.
- Если мультиметр **не** указывает напряжение, обратитесь к процедуре[[89-013-018 — Starter Switch|013-018]].

![[13400075.png]]

- Поверните стартовый переключатель в положение выключения.
- Удалите мультиметровые провода.
- Подключите стартерный соленоидный кабель к терминалу магнитного переключателя, а наземный провод к соответствующему терминалу на магнитном переключателе.

![[sb8toma.png]]


> [!quote]- Original (English) · английский оригинал
> ### Voltage Check
>
> **WARNING · Опасно**
> To reduce the possibility of personal injury, do not touch any ignition wires or components while the engine is operating, unless using suitably insulated tools.
>
> Make sure the starter switch is in the OFF position.
>
> Remove the cable connecting the magnetic switch to the starter solenoid from the magnetic switch terminal.
>
> Connect the leads of the digital multimeter, Part Number 3377161, or digital multimeter, Part Number 3164488, to the two large switch terminals.
>
> Set the multimeter to measure resistance (ohms).
>
> With the starter switch off, the multimeter **must** indicate resistance at infinity, open circuit.
>
> Turn the starter switch to the START position.
>
> The multimeter **must** indicate near zero resistance, closed circuit.
>
> If the multimeter indicates resistance at infinity with the starter switch in the START position:
>
> - Turn the starter switch off.
> - Remove the ground wire that is connected to one of the small magnetic switch terminals.
>
> - Set the multimeter scale to indicate volts, 24-VDC or more.
> - Connect the positive (+) lead of the multimeter to the magnetic switch ground terminal and the other lead to the ground wire.
> - Turn the starter switch to the START position.
> - If the multimeter indicates vehicle electrical system voltage, the magnetic switch is defective and **must** be replaced.
>
> - If the multimeter does **not** indicate voltage connect the positive (+) lead of the multimeter to the small positive (+) terminal on the magnetic switch and the negative multimeter lead to the ground wire.
> - Turn the starter switch to the START position.
> - If the multimeter indicates vehicle electrical system voltage, the magnetic switch is defective and **must** be replaced.
> - If the multimeter does **not** indicate voltage, refer to Procedure [[89-013-018 — Starter Switch|013-018]].
>
> - Turn the starter switch to the OFF position.
> - Remove the multimeter leads.
> - Connect the starter solenoid cable to the magnetic switch terminal, and the ground wire to its corresponding terminal on the magnetic switch.
