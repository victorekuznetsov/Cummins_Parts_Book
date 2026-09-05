---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "35-013-017"
title_en: "Starter Magnetic Switch"
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
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-013-017.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-013-017.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Starter Magnetic Switch
**Втягивающее реле стартера**

> [!abstract] Процедура · `35-013-017`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2009-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-013-017.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-013-017.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Текущая проверка

> [!danger] ОПАСНО
> Убедитесь, что стартерный выключатель находится в положении выключения, чтобы предотвратить электрический шок.

Удалите кабель, соединяющий магнитный переключатель с стартером соленоида из терминала магнитного переключателя.

Подключите провода цифрового мультиметра, Номер детали 3377161, к двум терминалам с большим переключателем.

![[sb8toha.png]]

Установите мультиметр для измерения сопротивления (омов).

При выключении стартера мультиметр **должен** указывать сопротивление на бесконечности, открытой цепи.

Поверните стартовый переключатель в положение START.

Мультиметр **должен** указывать нулевое сопротивление, замкнутую цепь.

![[sb800ta.png]]

Если мультиметр указывает сопротивление на бесконечности с помощью стартового переключателя в положении START:

- Выключите стартер.
- Удалите проволоку, которая подключена к одному из небольших магнитных переключателей.

![[sb800kx.png]]

- Установите многометровую шкалу, чтобы указать вольты, 24 ВДК или более.
- Подключите положительный (+) провод мультиметра к наземному терминалу магнитного переключателя, а другой - к наземному проводу.
- Поверните стартовый переключатель в положение START.
- Мультиметр **должен** указывать напряжение электрической системы транспортного средства.

![[sb800ky.png]]

- Если мультиметр **не** указывает напряжение, обратитесь к Starter Switch - Проверьте в этом разделе.

![[sb200ka.png]]

- Поверните стартовый переключатель в положение выключения.
- Удалите мультиметровые провода.
- Подключите стартерный соленоидный кабель к терминалу магнитного переключателя и наземный провод к соответствующему терминалу на магнитном переключателе.

![[sb8toma.png]]


> [!quote]- Original (English) · английский оригинал
> ### Current Check
>
> **WARNING · Опасно**
> Be sure the starter switch is in the OFF position to prevent electrical shock.
>
> Remove the cable connecting the magnetic switch to the starter solenoid from the magnetic switch terminal.
>
> Connect the leads of the digital multimeter, Part Number 3377161, to the two large-switch terminals.
>
> Set the multimeter to measure resistance (ohms).
>
> With the starter switch off, the multimeter **must** indicate resistance at infinity, open circuit.
>
> Turn the starter switch to the START position.
>
> The multimeter **must** indicate zero resistance, closed circuit.
>
> If the multimeter indicates resistance at infinity with the starter switch in the START position:
>
> - Turn the starter switch off.
> - Remove the ground wire that is connected to one of the small magnetic switch terminals.
>
> - Set the multimeter scale to indicate volts, 24 VDC or more.
> - Connect the positive (+) lead of the multimeter to the magnetic switch ground terminal and the other lead to the ground wire.
> - Turn the starter switch to the START position.
> - The multimeter **must** indicate vehicle electrical system voltage.
>
> - If the multimeter does **not** indicate voltage, refer to Starter Switch - Check in this section.
>
> - Turn the starter switch to the OFF position.
> - Remove the multimeter leads.
> - Connect the starter solenoid cable to the magnetic switch terminal and the ground wire to its corresponding terminal on the magnetic switch.
