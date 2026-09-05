---
aliases:
  - "Управляющие электромагниты Centinel™"
type: "Процедура"
doc: "96-019-138"
title_en: "Centinel™ Control Solenoids"
title_ru: "Управляющие электромагниты Centinel™"
modified: "2004-04-22"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 18
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-138.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-019-138.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# Centinel™ Control Solenoids
**Управляющие электромагниты Centinel™**

> [!abstract] Процедура · `96-019-138`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-04-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-138.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-019-138.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, отличные от Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Проверьте соленоидную цепь. Поместите штифт свинца в контакт подачи А соленоидного разъёма. Поместите другой свинцовый штифт в обратный контакт B соленоидного разъема. Подключите аллигаторы к многометровым зондам.

![[19801510.png]]

Измерьте сопротивление. Вычтите значение сопротивления многометрового испытательного щупа из этого значения, чтобы определить истинное значение сопротивления соленоидной цепи. Сопротивление должно быть:

12-VDC соленоид: 18-24 Ом при 25°C[77°F]

24-VDC соленоид: 78-94 Ом при 25°C[77°F].

Если значение сопротивления **не** правильно, то следует перейти к следующим разделам: Если сопротивление правильное, схема **должна **все еще проверяться на короткое замыкание на землю и короткое замыкание от пин-кодов до пин-кодов.

![[nobox.png]]

Если значение сопротивления ниже спецификаций, проверьте соленоидные провода на короткие замыкания между проводами. Если провода повреждены, замените провода. См. процедуру[[99-019-201 — Weather Pack Connector Series|019-201]].

![[19801511.png]]

Если значение сопротивления соленоида правильное, проблема заключается в проводах жгута. Изолируйте проблему, проверив электропроводку.

![[19400386.png]]

Проверьте проводку. Измерьте сопротивление между контактами А и В проводной стороны ремня разъема, которая была удалена из соленоида. Сопротивление должно быть открытым контуром (более 1 м ом). Если сопротивление меньше 1 м Ом, замените проводку ремня управления или модуля управления CentinelTM. См. процедуру[[96-019-130-tr — Centinel™ Control Module|019-130]]или[[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

Подключите разъём жгута проводов, когда ремонт завершен.

![[ee2coke.png]]

Если значение сопротивления выше спецификации, проверьте соленоидные провода на наличие сломанных проводов. Если провода повреждены, замените провода. См. процедуру[[99-019-201 — Weather Pack Connector Series|019-201]]. Не надо чинить провода.

![[19801511.png]]

Проверьте 2-контактный разъем соленоидных проводов для правильного подключения.

Если провод и разъем выглядят нормально, замените соленоид. См. процедуру[[96-007-076 — Burn Solenoid|007-076]].

![[05100041.png]]

Если значение сопротивления находится в пределах спецификации, схема **должна** все еще проверяться на короткое замыкание на землю и короткое замыкание от пин-кодов до пин-кодов.

![[19801512.png]]

### Проверка на замыкание на массу

Проверьте соленоидную цепь для короткого замыкания на землю шасси.

Ключ должен быть в положении OFF

Используйте мультиметр для измерения сопротивления между выходным соленоидным штифтом на стороне проводов блока управления модуля CentinelTM и заземлением блока двигателя.

Сопротивление должно быть более 1M Ом (открытая схема).

![[19801512.png]]

Если значение сопротивления меньше 1M Ом, есть короткое замыкание на землю в соленоиде, соленоидных проводах или проводной упряжке. Следуйте следующим образом, чтобы найти короткое замыкание на землю. Если значение сопротивления правильное, схема **должна **все еще проверяться на короткое замыкание от пин-кодов до пин-кодов.

![[19801513.png]]

Осмотрите соленоидные провода для короткого замыкания на землю. Если провода повреждены, замените провода. См. процедуру[[99-019-201 — Weather Pack Connector Series|019-201]]. Не надо чинить провода.

![[19801511.png]]

Проверьте соленоид на короткое замыкание на землю. Отключите соленоидные провода подачи и возврата от соленоида.

Прикоснитесь к одному из многометровых щупов на соленоидных штифтах. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Сопротивление должно быть более 1M Ом (открытая схема). Если сопротивление меньше 1 м Ом, замените соленоид. См. процедуру[[96-007-076 — Burn Solenoid|007-076]].

![[19801514.png]]

Если значение сопротивления правильное, проблема заключается в проводах ремня. Изолируйте проблему, проверив электропроводку.

![[19400386.png]]

Проверьте электропроводку ремня для короткого замыкания на землю. Отключите как соленоидные, так и проводные разъёмы. Прикоснитесь к многометровому щупу на контакте подачи разъёма проводов жгута. Прикоснитесь к другому многометровому щупу блока двигателя.

Измерьте сопротивление. Значение сопротивления должно быть более 1M Ом (открытая схема).

![[19801518.png]]

Удалите многометровый щуп от контакта с подачей и прикоснитесь к нему обратного контакта. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Сопротивление должно быть более 1M Ом (открытая схема).

Если в любой проверке измеряется менее 1 м Ом, в электропроводке есть короткое замыкание на землю. Замените проводку упряжкой. См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

Подключите разъём жгута проводов и соленоидный разъём, когда ремонт завершен.

![[19801519.png]]

### Проверка на замыкание между контактами

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!warning] ОСТОРОЖНО
> Аккумуляторы должны быть отключены перед выполнением этой проверки. Мультиметр будет поврежден, если батареи не отсоединятся.

Отсоедините аккумуляторные батареи.

Проверьте короткое замыкание между проводами для проблемы соленоида и всех других проводов в проводной упряжке.

![[ea8coha.png]]

Переключатель зажигания транспортного средства в положение выключения.

Убедитесь, что разъём жгута проводов и соленоидный разъём отключены.

Вставьте свинец в контакт с поставкой. Вставьте другой свинец во все штифты разъема, кроме обратного контакта проблемного соленоида. Измерьте сопротивление. Сопротивление должно быть более 1M Ом (открытая схема).

![[19801515.png]]

Если между контактом с подачей и любым штифтом измеряется менее 1 м Ом, то в проводной упряжке между подачей или возвратным проводом имеется короткое замыкание на любой штифт, измеряемый менее 1 м Ом. Ремонт или замена проводов жгута. См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

![[19801516.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> Inspect the solenoid circuit. Place the pin of the lead into the supply pin A of the solenoid connector. Place the other lead pin into the return pin B of the solenoid connector. Connect the alligator clips to the multimeter probes.
>
> Measure the resistance. Subtract the multimeter test lead resistance value from this value to determine the true solenoid circuit resistance value. The resistance **must** be:
>
> 12-VDC solenoid: 18 to 24 ohms at 25°C \[77°F\]
>
> 24-VDC solenoid: 78 to 94 ohms at 25°C \[77°F\].
>
> If the resistance value is **not** correct, proceed with the following sections. If the resistance is correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.
>
> If the resistance value is below specifications, inspect the solenoid wires for short circuits between the wires. If the wires are damaged, replace the wires. Refer to Procedure [[99-019-201 — Weather Pack Connector Series|019-201]].
>
> If the resistance value of the solenoid is correct, the problem is in the wiring harness. Isolate the problem by checking the wiring harness.
>
> Check the wiring harness. Measure the resistance between pins A and B of the harness side of the connector that was removed from the solenoid. The resistance **must** be an open circuit (more than 1M ohms). If the resistance is less than 1M ohms, replace the wiring harness or Centinel™ control module. Refer to Procedure [[96-019-130-tr — Centinel™ Control Module|019-130]] or [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].
>
> Connect the wiring harness connector when the repair is completed.
>
> If the resistance value is above specification, inspect the solenoid wires for broken wires. If the wires are damaged, replace the wires. Refer to Procedure [[99-019-201 — Weather Pack Connector Series|019-201]]. Do **not** repair the wires.
>
> Check the 2-pin connector of the solenoid wires for proper connection.
>
> If the wire and connector look OK, replace the solenoid. Refer to Procedure [[96-007-076 — Burn Solenoid|007-076]].
>
> If the resistance value is within specification, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.
>
> ### Check for Short Circuit to Ground
>
> Check the solenoid circuit for a short circuit to chassis ground.
>
> The key should be in the OFF position
>
> Use the multimeter to measure the resistance between the solenoid output pin on the harness side of the Centinel™ control module and the engine block ground.
>
> The resistance **must** be more than 1M ohms (open circuit).
>
> If the resistance value is less than 1M ohms, there is a short circuit to ground in the solenoid, the solenoid wires, or the wiring harness. Proceed as follows to locate the short circuit to ground. If the resistance value is correct, the circuit **must** still be checked for a short circuit from pin to pin.
>
> Inspect the solenoid wires for a short circuit to ground. If the wires are damaged, replace the wires. Refer to Procedure [[99-019-201 — Weather Pack Connector Series|019-201]]. Do **not** repair the wires.
>
> Check the solenoid for a short circuit to ground. Disconnect the solenoid supply and return wires from the solenoid.
>
> Touch one multimeter probe to one of the solenoid pins. Touch the other multimeter probe to the engine block. Measure the resistance. The resistance **must** be more than 1M ohms (open circuit). If the resistance is less than 1M ohms, replace the solenoid. Refer to Procedure [[96-007-076 — Burn Solenoid|007-076]].
>
> If the resistance value is correct, the problem is in the wiring harness. Isolate the problem by checking the wiring harness.
>
> Check the wiring harness for a short circuit to ground. Disconnect both the solenoid and wiring harness connectors. Touch the multimeter probe on the supply pin of the wiring harness connector. Touch the other multimeter probe to the engine block.
>
> Measure the resistance. The resistance value **must** be more than 1M ohms (open circuit).
>
> Remove the multimeter probe from the supply pin and touch it to the return pin. Touch the other multimeter probe to the engine block. Measure the resistance. The resistance **must** be more than 1M ohms (open circuit).
>
> If less than 1M ohms are measured in either check, there is a short circuit to ground in the wiring harness. Replace the wiring harness. Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].
>
> Connect the wiring harness connector and the solenoid connector when the repair is completed.
>
> ### Check for Short Circuit from Pin to Pin
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **CAUTION · Осторожно**
> The batteries must be disconnected before performing this check. The multimeter will be damaged if the batteries are not disconnected.
>
> Disconnect the batteries.
>
> Check for a short circuit between the wires for the problem solenoid and all other wires in the wiring harness.
>
> Turn the vehicle keyswitch to the OFF position.
>
> Make sure that the wiring harness connector and the solenoid connector are disconnected.
>
> Insert the lead into the supply pin. Insert the other lead into all of the pins of the connector except the return pin of the problem solenoid. Measure the resistance. The resistance **must** be more than 1M ohms (open circuit).
>
> If less than 1M ohms are measured between the supply pin and any pin, there is a short circuit in the wiring harness between the supply or return wire to any pin that measured less than 1M ohms. Repair or replace the wiring harness. Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].
