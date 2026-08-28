---
aliases:
  - "Генератор системы зарядки"
type: "Процедура"
doc: "20-013-001-tr"
title_en: "Charging System Alternator"
title_ru: "Генератор системы зарядки"
modified: "2015-08-20"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 17
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-013-001-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-013-001-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Charging System Alternator
**Генератор системы зарядки**

> [!abstract] Процедура · `20-013-001-tr`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2015-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-013-001-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-013-001-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Отсоедините проводку и наземный ремешок от генератора. См. сервисную документацию изготовителя оборудования.

![[ea8coma.png]]

Устранить регулировочное звено и крепления генератора.

> [!note] Примечание
> Нижний локон имеет **левую** резьбу.

Освободите оба ореха. Поверните регулирующий винт, чтобы снять натяжение ремня.

Снимите ремень генератора.

![[eh4blmb.png]]

Удалите болты (1) и (2) и корректирующее звено.

Удалите болты (3) и гайки.

Удалите генератор.

![[eh4bdha.png]]

### Проверка при повторном использовании

Удалите гайку и шкив из генератора.

Очистите и проверьте шкив для повторного использования.

![[ea8puha.png]]

### Проверка

Следующие инструкции предназначены для использования с анализатором системы индуктивной зарядки и ранжирования 3377193, или эквивалентом.

> [!note] Примечание
> Перед выполнением следующего испытания убедитесь, что ремень генератора затянут до правильных спецификаций.[[20-013-005-tr — Charging System Alternator Drive Belt|См. процедуру 013-005 в разделе 13.]].

![[eh4toga.png]]

Установите ручку селектора напряжения на соответствующую шкалу. Для 24-вольтовой системы выберите шкалу 40 вольт.

Установите ручку селектора усилителя на 100 ампер.

![[ea8tola.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

Удалите кабели на любую другую батарею в цепи.

Подключение правильного анализатора приводит к **положительным** и **отрицательным** клеммам на батарее.

![[ea800kf.png]]

Подключите зажимный усилитель к выходному кабелю генератора как можно дальше от генератора.

![[ea8tohc.png]]

Управляйте двигателем на высоком холостом ходу и поворачивайте ручку управления нагрузкой анализатора **по часовой стрелке** до тех пор, пока не будет получен максимальный считывание усилителей.

> [!note] Примечание
> Сделайте **не**, чтобы нагрузка упала ниже 26 вольт для системы 24 вольт.

Максимальное значение усилителя - выход генератора переменного тока, и **должно** соответствовать спецификациям производителя генератора переменного тока.

![[ea800kg.png]]

> [!note] Примечание
> Максимальный номинальный выход генератора обычно маркируется или маркируется на генераторе.

> [!note] Примечание
> Также проверьте прибор амметра калибра. Если он читается **не** примерно так же, как и испытательное оборудование, его следует заменить.

> [!note] Примечание
> Если выход генератора переменного тока **не** в пределах 10 процентов от номинального выхода, отремонтируйте или замените генератор. См. сервисную документацию изготовителя оборудования.

![[ea800kh.png]]

Поверните ручку управления нагрузкой анализатора **против часовой стрелки** в положение «OFF» и выключите двигатель.

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

Удалите испытательное оборудование. Подключите все кабели аккумулятора, которые были удалены.

![[ea800ki.png]]

### Установка

Смазать вал моторным маслом. Установите шкив и гайку на вал генератора.

Затяните гайку.

> [!tip] Момент затяжки
> 100 Н·м [75 фунт-фут]

![[ea8puhb.png]]

Ремень * должен быть отрегулирован до того, как затворы будут затянуты.

> [!note] Примечание
> Конец регулировочного звена с наибольшей площадью на затворе должен быть ближе всего к генератору.

Установите генератор переменного тока и корректирующую линию, как показано.

![[eh4bdha.png]]

> [!warning] ОСТОРОЖНО
> Не пытайтесь пощипать пояс на шкиве, чтобы избежать повреждения шкива и пояса.

Установите ремень. Поверните регулировочный винт **против часовой стрелки**, чтобы сократить соединение, если это необходимо.

![[eh4blmb.png]]

Поверните регулирующий винт **по часовой стрелке**, чтобы затянуть ремень.

Затяните пояс.

| Измерения |  |  |
|---|---|---|
|  | n | хулиган |
| Напряженность в поясе | 670 | 150 |

Используйте измеритель напряжения ремня (Burroughs), номер детали ST-1138, чтобы проверить натяжение ремня.

![[eh4toga.png]]

> [!note] Примечание
> Нижний локон имеет **левую** резьбу.

Затяните гайки на регулировочном винте.

Затягивать регулировочные звенья и крепления генераторов переменного тока.

Момент затяжки:

Джейм Натс

Момент затяжки:

6.2.1.3 Установочные болты

![[eh4lkuc.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подключите проводку к генератору. См. сервисную документацию изготовителя оборудования.
- Подсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.

![[19400050.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries. See equipment manufacturer service information.
> - Disconnect the wiring and ground strap from the alternator. See equipment manufacturer service information.
>
> Loosen the adjusting link and the alternator mounting capscrews.
>
> **Note · Примечание**
> The lower jam nut has **left-hand** threads.
>
> Loosen both of the jam nuts. Turn the adjusting screw to relieve the belt tension.
>
> Remove the alternator belt.
>
> Remove capscrews (1) and (2) and the adjusting link.
>
> Remove capscrew (3) and nut.
>
> Remove the alternator.
>
> ### Inspect for Reuse
>
> Remove the nut and the pulley from the alternator.
>
> Clean and check the pulley for reuse.
>
> ### Test
>
> The following instructions are for use with the Part Number 3377193 Inductive Charging and Cranking System Analyzer, or equivalent.
>
> **Note · Примечание**
> Before performing the following test, be sure the alternator belt is tightened to the correct specifications. [[20-013-005-tr — Charging System Alternator Drive Belt|Refer to Procedure 013-005 in Section 13.]].
>
> Set the voltage selector knob to the appropriate scale. For a 24 volt system, choose the 40 volt scale.
>
> Set the amp selector knob to 100 amps.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Remove the cables to any other battery in the circuit.
>
> Connect the correct analyzer leads to the **positive** and **negative** terminals on the battery.
>
> Connect the clamp-on amp pick-up to the alternator output cable as far away from the alternator as possible.
>
> Operate the engine at high idle and turn the analyzer load control knob **clockwise** until a maximum amps reading is obtained.
>
> **Note · Примечание**
> Do **not** let the load volts drop below 26 volts for a 24 volt system.
>
> The maximum amp reading is the alternator output, and **must** meet the alternator manufacturer's specifications.
>
> **Note · Примечание**
> The alternator maximum rated output is normally stamped or labeled on the alternator.
>
> **Note · Примечание**
> Also check the equipment ammeter gauge. If it does **not** read approximately the same as the test equipment, it should be replaced.
>
> **Note · Примечание**
> If the alternator output is **not** within 10 percent of rated output, repair or replace the alternator. See equipment manufacturer service information.
>
> Turn the analyzer load control knob **counterclockwise** to the “OFF” position and shut off the engine.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Remove the test equipment. Connect all battery cables that were removed.
>
> ### Install
>
> Lubricate the shaft with engine oil. Install the pulley and nut on the alternator shaft.
>
> Tighten the nut.
>
> **Момент затяжки · Torque Value**
> 100 n•m [75 ft-lb]
>
> The belt **must** be adjusted before the capscrews are tightened.
>
> **Note · Примечание**
> The end of the adjusting link with the largest area at the capscrew hole **must** be nearest to the alternator.
>
> Install the alternator and the adjusting link as shown.
>
> **CAUTION · Осторожно**
> Do not attempt to pry the belt on the pulley to avoid damage to pulley and belt.
>
> Install the belt. Turn the adjusting screw **counterclockwise** to shorten the link, if necessary.
>
> Turn the adjusting screw **clockwise** to tighten the belt.
>
> Tighten the belt.
>
> | Measurements |  |  |
> |---|---|---|
> |  | n | lbf |
> | Belt Tension | 670 | 150 |
>
> Use the (Burroughs) belt tension gauge, Part Number ST-1138, to check the belt tension.
>
> **Note · Примечание**
> The lower jam nut has **left-hand** threads.
>
> Tighten the jam nuts on the adjusting screw.
>
> Tighten the adjusting link and alternator mounting capscrews.
>
> Torque Value:
>
> Jam Nuts
>
> Torque Value:
>
> Alternator Mounting Capscrews
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect the wiring to the alternator. See equipment manufacturer service information.
> - Connect the batteries. See equipment manufacturer service information.
