---
aliases:
  - "Выключатель положения педали сцепления"
type: "Процедура"
doc: "82-019-009"
title_en: "Clutch Pedal Position Switch"
title_ru: "Выключатель положения педали сцепления"
modified: "2003-10-09"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-009.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-009.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Clutch Pedal Position Switch
**Выключатель положения педали сцепления**

> [!abstract] Процедура · `82-019-009`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2003-10-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-009.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-009.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Схема переключателя сцепления используется для отключения функций PTO и круиз-контроля.

Схема представляет собой обычно закрытый переключатель управления, провод 2 (вход переключателя сцепления) и общую площадку. Когда выключатель сцепления установлен и настроен, точки контакта удерживаются закрытыми. Когда педаль сцепления находится в подавленном состоянии, переключатель сцепления находится в обычно закрытом положении. Это отключит PTO или круиз-контроль.

![[19c00202.png]]

### Проверка сопротивления

Если INSITETM доступен, проверьте переключатель сцепления для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Найдите выключатель сцепления. Месторасположение будет зависеть от процедур установки OEM.

Отделите проводной разъем.

Настройте мультиметр для измерения сопротивления.

Прикоснитесь к зондам мультиметра к двум терминалам в разъеме.

![[cl8swka.png]]

Задействуйте сцепление (выпущенная педаль сцепления). Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если выключатель **не** закрыт, когда сцепление полностью включено, отрегулируйте рычаг переключения сцепления.

![[cl8swkb.png]]

Ударь педалью сцепления. Выключатель сцепления **должен** открыться. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если выключатель **не** открыт, когда сцепление полностью включено, отрегулируйте рычаг переключения сцепления.

![[cl8swke.png]]

### Проверка на замыкание на массу

Удалите один многометровый щуп из разъема и прикоснитесь к щупу к земле шасси. Мультиметр **должен** показывать открытую схему (100к Ом или более), когда педаль сцепления находится в депрессии. Если цепь закрыта, замените выключатель сцепления. См. руководство изготовителя машины по диагностике и ремонту.

Если выключатель сцепления прошел все предыдущие проверки, подключите выключатель к проводах ремня. Схема переключателя сцепления должна быть проверена.

![[cl8swkf.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Переключатель зажигания транспортного средства в положение Включения.

Настройте мультиметр для измерения VDC.

Вставьте один из многометровых щупов в разъём переключателя сцепления.

Прикоснитесь к другому многометровому щупу, чтобы блокировать землю двигателя и измерить напряжение. Напряжение должно быть 1.5 VDC или меньше с выключенной и подавленной педалью сцепления.

![[19c00879.png]]

Если значение напряжения больше 1,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в проводах OEM-проводов, который несет напряжение.

Удалите внешний источник напряжения.

Если выключатель сцепления прошел все предыдущие проверки, подключите выключатель к проводах ремня. Схема переключателя сцепления должна быть проверена.

![[19c00724.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The clutch switch circuit is used to disable the PTO and cruise control features.
>
> The circuit is a normally closed control switch, wire 2 (clutch switch input), and a common ground. When the clutch switch is installed and adjusted, the contact points are held closed. When the clutch pedal is depressed, the clutch switch is in its normally closed position. This will disable the PTO or cruise control operation.
>
> ### Resistance Check
>
> If INSITE™ is available, monitor the clutch switch for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Find the clutch switch. The location will depend on the OEM installation procedures.
>
> Separate the wire connector.
>
> Adjust the multimeter to measure resistance.
>
> Touch the probes of the multimeter to the two terminals in the connector.
>
> Engage the clutch (clutch pedal released). The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the switch is **not** closed when the clutch is fully engaged, adjust the clutch switch trip lever.
>
> Depress the clutch pedal. The clutch switch **must** open. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the switch is **not** open when the clutch is fully engaged, adjust the clutch switch trip lever.
>
> ### Check for Short Circuit to Ground
>
> Remove one multimeter probe from the connector and touch the probe to the chassis ground. The multimeter **must** show an open circuit (100k ohms or more) when the clutch pedal is depressed. If the circuit is closed, replace the clutch switch. Refer to the OEM troubleshooting and repair manual.
>
> If the clutch switch passed all previous checks, connect the switch to the wiring harness. The clutch switch circuit **must** be checked.
>
> ### Check for Short Circuit to External Voltage Source
>
> Turn the vehicle keyswitch to the ON position.
>
> Adjust the multimeter to measure VDC.
>
> Insert one of the multimeter probes into the clutch switch connector.
>
> Touch the other multimeter probe to the engine block ground and measure the voltage. The voltage **must** be 1.5 VDC or less with the clutch pedal released and depressed.
>
> If the voltage value is more than 1.5 VDC, there is a short circuit to an external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the OEM harness wiring that carries the voltage.
>
> Remove the external voltage source.
>
> If the clutch switch passed all previous checks, connect the switch to the wiring harness. The clutch switch circuit **must** be checked.
