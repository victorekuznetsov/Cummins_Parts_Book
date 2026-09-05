---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "40-013-019"
title_en: "Starter Solenoid"
title_ru: "Втягивающее реле стартера"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 21
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Starter Solenoid
**Втягивающее реле стартера**

> [!abstract] Процедура · `40-013-019`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-019.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Перед устранением неисправностей пускового двигателя убедитесь, что клеммы батареи **не **рыхлые или разъединены.

![[ea8cosa.png]]

Если стартовый двигатель соленоида делает **не** издавать звук, проверьте наличие свободных проводных соединений.

![[es900ka.png]]

Используйте цифровой мультиметр, номер 3377161, или эквивалент, для установки шкалы напряжения.

Проверьте напряжение системы на стартовом терминале соленоидной батареи двигателя.

![[es900wk.png]]

Если мультиметр указывает на системное напряжение на стартовом терминале аккумуляторной батареи, проверьте напряжение на стартовом терминале соленоида двигателя «S», при этом пусковой выключатель заряжается.

Если мультиметр указывает на системное напряжение на терминале «S», но стартер не включается, стартовый соленоид двигателя неисправен, и стартер должен быть заменен.

![[13900056.png]]

Если мультиметр **не** указывает на системное напряжение на терминале "S", проверьте:

- предохранители
- Напряжение переключателя зажигания и магнитного переключателя.
- Системы безопасного отключения приложений.

![[es900wm.png]]

### Проверка напряжения

Установите цифровой мультиметр, номер 3377161, для измерения вольт постоянного тока.

Подключение многометрового положительного (+) приводит к стартеру соленоидного положительного кабельного терминала, а отрицательного (-) приводит к расположению шасси или заземления двигателя.

Мультиметр **должен** показывать напряжение с выключателем стартера в положении выключения, чтобы быть нормальным.

![[es900wc.png]]

Если мультиметр **не** указывает на напряжение, проверьте кабель, соединяющий стартер соленоида и батарею на наличие перерывов. Кроме того, проверьте наличие свободных или разъединенных соединений.

![[sb800kk.png]]

Если мультиметр указывает напряжение, но стартер будет **не** работать, проверьте провод, соединяющий стартер соленоид с стартерным выключателем для перерывов, а также проверьте наличие свободных или разъединенных соединений.

Кроме того, обязательно проверьте на:

- предохранители
- Системы отключения двигателей приложений.

![[sb800kl.png]]

Если провод, соединяющий стартер соленоид и стартерный выключатель, **не **свободен или поврежден, и стартер **не **работает:

- Удалите кабель, соединяющий стартер и стартер соленоида из соленоидного терминала.
- Соедините многометровый положительный (+) вывод к соленоидному положительному выводу, а отрицательный (-) вывод к шасси или расположению двигателя на земле.

![[sb800km.png]]

- Поверните стартовый переключатель в положение START.
- Если мультиметр указывает на напряжение, стартер соленоид неисправен и должен быть заменен.

![[sb800kn.png]]

- Если мультиметр **не** указывает на напряжение, проверьте провод, соединяющий стартер соленоид с магнитным переключателем, на наличие разрывов и на наличие рыхлых или корродированных соединений.

![[sb800ko.png]]

Если провод, соединяющий стартер соленоид с магнитным переключателем, **не является свободным или поврежденным, и стартер будет **не работать:

- Проверьте кабель, соединяющий стартер соленоид с стартерным двигателем для перерывов и для рыхлых или корродированных соединений.

![[sb200kb.png]]

- Проверьте кабель, соединяющий стартерный двигатель с батареей, на наличие разрывов и на наличие рыхлых или разъединенных соединений.

![[sb8cosa.png]]

- Если кабели не рыхлые или повреждены, стартерный двигатель неисправен и должен быть заменен. Видишь?[[40-013-020-tr — Starting Motor|Процедура 013-020]].

![[sb2cosa.png]]

Напряжение наклона цепи Solenoid Control на стартерах Delco®.

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

Отключите батарею.

![[13900050.png]]

Удалите все кабели и соединения из клеммы батареи коленчатого двигателя.

Закрепите все кабели и соединения вместе (1/2-дюймовый болт и гайка работают для зажима соединений). Оберните тяжелую ткань вокруг клеммы аккумулятора коленчатого двигателя, чтобы убедиться, что он не касается какого-либо металла.

![[13900051.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

Подключите батарею.

![[13900050.png]]

Подключите цифровой мультиметр, номер детали 3377161, между положительным зарядом батареи (+) и терминалом «S» (мультиметр должен показывать напряжение открытой цепи батареи, примерно от 12,5 до 12,6 ВДК).

![[13900052.png]]

Закройте выключатель запуска автомобиля, и первым чтением будет падение напряжения. Если вы подождите, показания напряжения быстро падают, так как соленоид нагревается и повышает сопротивление соленоида. Обязательно запишите первое чтение.

> [!note] Примечание
> Двигатель будет **не** коленчатым, если нет напряжения, подаваемого на двигатель.

Повторите шаг с помощью мультиметра, соединенного между отрицательной (-) батареей и отрицательной (-) двигателем. Добавьте напряжения с предыдущего шага и этого шага, чтобы получить падение напряжения цепи управления. Значения включены в таблицу ниже.

При включенных цепях удерживания и вытягивания максимально допустимое падение напряжения при 20°C[68°F] составляет:

| VDC | Снижается напряжение (максимальное) |
|---|---|
| 12 | 1.0 VDC |
| 24 | 2.0 VDC |
| 32 | 2.6 VDC |

| Соленоидная средняя амперационная черта |  |  |  |
|---|---|---|---|
| мотор | VDC | PI & HI Amps (англ.)русск. | HI Amps |
| 28 мкм | 12 | 69 | 13 |
|  | 24 | 120 | 13 |
| 37 мкм | 12 | 74 | 19 |
|  | 24 | 36 | 6 |
| 41/42MT | 12 | 97 | 18 |
|  | 24 | 57 | 13 |
| 50 мкм | 12 | 86 | 15 |
|  | 24 | 49 | 6 |
|  | 32 | 38 | 6 |
|  | 64 | 10 | 2 |
| Для 12-DC систем, нажмите 10 VDC на терминал «S». |  |  |  |
| Для систем 24-VDC, нажмите 20 VDC на терминал «S». |  |  |  |
| Для некоторых 32-VDC систем, примените 30 VDC к терминалу «S». |  |  |  |
| Для некоторых 32-VDC и всех 64-VDC систем, применить 30 VDC к терминалу "B+". |  |  |  |

![[13900053.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

Отключите батарею.

![[13900050.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

Замените все соединения на клемме батареи двигателя, а затем снова подключите батарею.

![[13900054.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Before troubleshooting the starting motor, make sure the battery terminals are **not** loose or corroded.
>
> If the starting motor solenoid does **not** make a sound, check for loose wiring connections.
>
> Use a digital multimeter, Part Number 3377161, or equivalent, to set the voltage scale.
>
> Check for system voltage at the starting motor solenoid battery terminal.
>
> If the multimeter indicates system voltage at the starting motor battery terminal, check the voltage at the starting motor solenoid "S" terminal, while the starting switch is energized.
>
> If the multimeter indicates system voltage at "S" terminal but the starter does **not** engage, the starting motor solenoid is malfunctioning and the starter **must** be replaced.
>
> If the multimeter does **not** indicate system voltage at the "S" terminal, check:
>
> - Fuses
> - Voltage to the ignition switch and magnetic switch.
> - Application safety shutoff systems.
>
> ### Voltage Check
>
> Set the digital multimeter, Part Number 3377161, to measure DC volts.
>
> Connect the multimeter positive (+) lead to the starter solenoid positive cable terminal and the negative (-) lead to a chassis or engine ground location.
>
> The multimeter **must** show voltage with the starter switch in the OFF position to be normal.
>
> If the multimeter does **not** indicate voltage, check the cable connecting the starter solenoid and battery for breaks. Also, check for loose or corroded connections.
>
> If the multimeter indicates voltage but the starter will **not** operate, check the wire connecting the starter solenoid to the starter switch for breaks, and also check for loose or corroded connections.
>
> In addition be sure to check for:
>
> - Fuses
> - Application engine shutoff systems.
>
> If the wire connecting the starter solenoid and starter switch is **not** loose or damaged and the starter will **not** operate:
>
> - Remove the cable connecting the starter and starter solenoid from the solenoid terminal.
> - Connect the multimeter positive (+) lead to the solenoid positive terminal and the negative (-) lead to the chassis or an engine ground location.
>
> - Turn the starter switch to the START position.
> - If the multimeter indicates voltage, the starter solenoid is malfunctioning and **must** be replaced.
>
> - If the multimeter does **not** indicate voltage, check the wire connecting the starter solenoid to the magnetic switch for breaks, and for loose or corroded connections.
>
> If the wire connecting the starter solenoid to the magnetic switch is **not** loose or damaged and the starter will **not** operate:
>
> - Check the cable connecting the starter solenoid to the starter motor for breaks, and for loose or corroded connections.
>
> - Check the cable connecting the starter motor to the battery for breaks, and for loose or corroded connections.
>
> - If the cables are **not** loose or damaged, the starter motor is defective and **must** be replaced. Refer to [[40-013-020-tr — Starting Motor|Procedure 013-020]].
>
> Solenoid Control Circuit Voltage Drop on Delco® Starters.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Disconnect the battery.
>
> Remove all cables and connections from the battery terminal of the cranking motor.
>
> Clamp all cables and connections together (a 1/2-inch bolt and nut works for clamping connections). Wrap a heavy cloth around the battery terminal of the cranking motor to be certain it does **not** touch any metal.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Connect the battery.
>
> Connect a digital multimeter, Part Number 3377161, between battery positive (+) and the “S” terminal (the multimeter should show battery open circuit voltage, about 12.5 to 12.6 VDC).
>
> Close the vehicle start switch and the very first reading is the voltage drop. If you wait, the voltage reading will drop rapidly as the solenoid heats up and raises the solenoid resistance. Be certain to record the very first reading.
>
> **Note · Примечание**
> The motor will **not** crank if there is no voltage supplied to the motor.
>
> Repeat the step with the multimeter connected between the battery negative (-) and motor negative (-). Add the voltages from the previous step and this step to get the control circuit voltage drop. Values are included in the table below.
>
> With the hold-in and pull-in circuits both activated the maximum allowable voltage drop at 20°C \[68°F\] is:
>
> | VDC | Voltage Drop (maximum) |
> |---|---|
> | 12 | 1.0 VDC |
> | 24 | 2.0 VDC |
> | 32 | 2.6 VDC |
>
> | Solenoid Average Amperage Draw |  |  |  |
> |---|---|---|---|
> | Motor | VDC | PI & HI Amps | HI Amps |
> | 28MT | 12 | 69 | 13 |
> |  | 24 | 120 | 13 |
> | 37MT | 12 | 74 | 19 |
> |  | 24 | 36 | 6 |
> | 41/42MT | 12 | 97 | 18 |
> |  | 24 | 57 | 13 |
> | 50MT | 12 | 86 | 15 |
> |  | 24 | 49 | 6 |
> |  | 32 | 38 | 6 |
> |  | 64 | 10 | 2 |
> | For 12 -DC systems, apply 10 VDC to the "S" terminal. |  |  |  |
> | For 24-VDC systems, apply 20 VDC to the "S" terminal. |  |  |  |
> | For some 32-VDC systems, apply 30 VDC to the "S" terminal. |  |  |  |
> | For some 32-VDC and all 64-VDC systems, apply 30 VDC to the "B+" terminal. |  |  |  |
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Disconnect the battery.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Replace all connections to the battery terminal of the motor and then reconnect the battery.
