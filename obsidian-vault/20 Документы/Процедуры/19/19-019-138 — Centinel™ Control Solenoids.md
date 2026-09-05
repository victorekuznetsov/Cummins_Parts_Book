---
aliases:
  - "Управляющие электромагниты Centinel™"
type: "Процедура"
doc: "19-019-138"
title_en: "Centinel™ Control Solenoids"
title_ru: "Управляющие электромагниты Centinel™"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 18
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-138.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-138.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Centinel™ Control Solenoids
**Управляющие электромагниты Centinel™**

> [!abstract] Процедура · `19-019-138`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-138.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-138.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения разъема, не используйте щупы или провода, отличные от Части № 3822758. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Проверьте соленоидную цепь. Вставьте штифт свинца в контакт подачи А соленоидного разъёма. Вставьте другой свинцовый штифт в обратный контакт B соленоидного разъёма. Подключите аллигаторы к многометровым зондам.

![[19801513.png]]

Измерьте сопротивление. Вычтите значение сопротивления многометрового испытательного щупа из этого значения, чтобы определить истинное значение сопротивления соленоидной цепи. Сопротивление **должно быть от 14 до 120 Ом. Если значение сопротивления **не** правильно, то следует перейти к следующим разделам: Если сопротивление правильное, схема **должна все еще проверяться на короткое замыкание на землю и короткое замыкание от пин-кодов до пин-кодов.

![[19801513.png]]

**Сопротивление ниже спецификаций**

Осмотрите соленоидные провода для коротких замыканий между проводами. Если провода повреждены, замените провода. См. процедуру 019-202.

![[19801511.png]]

Если значение сопротивления соленоида правильное, проблема заключается в проводах жгута. Изолируйте проблему, проверив электропроводку. Осмотрите проводную упряжку для проводов, которые износились через изоляцию, порезы и любые другие повреждения, которые могут вызвать открытое или короткое замыкание. Если обнаружены какие-либо физические повреждения, отремонтируйте или замените поврежденную проводку. См. процедуру[[19-019-072 — OEM Interface Harness|019-072]]или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19400386.png]]

Проверьте проводку. Измерьте сопротивление между контактами А и В проводной стороны ремня разъёма, которая была удалена из соленоида. Сопротивление должно быть открытым контуром (более 1k ом). Если сопротивление меньше 1к Ом, замените электропроводку или ECM. См. процедуру[[19-019-043 — Engine Wiring Harness|019-043]]или[[19-019-031 — Engine Control Module|019-031]].

Подключите разъём жгута проводов, когда ремонт завершен.

![[ee2coke.png]]

**Значение сопротивления выше спецификации**

Осмотрите соленоидные провода на наличие сломанных проводов. Если провода повреждены, замените провода. См. процедуру 019-202. Не надо чинить провода.

![[19801511.png]]

Проверьте 2-контактный разъем соленоидных проводов для правильного подключения.

Если провод и разъем выглядят нормально, замените соленоид. См. раздел 2 Руководства по устранению неполадок и ремонту, Двигатели серии QSK19, Вестник 3666098, Руководство по устранению неполадок и ремонту, Двигатели серии QSK45 и QSK60, Вестник 3666261 или Руководство по устранению неполадок и ремонту, Двигатели серии QSK78, Вестник 3666727.

![[05100041.png]]

**Значение сопротивления в пределах спецификации**

Если значение сопротивления находится в пределах спецификации, схема **должна** все еще проверяться на короткое замыкание на землю и короткое замыкание от пин-кодов до пин-кодов.

![[19801512.png]]

### Проверка на замыкание на массу

Проверьте соленоидную цепь для короткого замыкания на землю шасси.

Переключатель зажигания в положение выключения

Используйте мультиметр для измерения сопротивления между выходным соленоидным штифтом на стороне проводов контроллера CentinelTM и заземлением блока двигателя.

Сопротивление должно быть более 1k Ом (открытая схема).

![[19801512.png]]

Если значение сопротивления меньше 1k Ом, есть короткое замыкание на землю в соленоиде, соленоидных проводах или проводной упряжке. Следуйте следующим образом, чтобы найти короткое замыкание на землю. Если значение сопротивления правильное, схема **должна **все еще проверяться на короткое замыкание от пин-кодов до пин-кодов.

![[19801513.png]]

Осмотрите соленоидные провода для короткого замыкания на землю. Если провода повреждены, замените провода. См. процедуру 019-202. Не надо чинить провода.

![[19801511.png]]

Проверьте соленоид на короткое замыкание на землю. Отключите соленоидные провода подачи и возврата от соленоида.

Прикоснитесь к одному из многометровых щупов на соленоидных штифтах. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Сопротивление должно быть более 1k Ом (открытая схема). Если сопротивление меньше 1к Ом, замените соленоид. См. раздел 2 Руководства по устранению неполадок и ремонту, Двигатели серии QSK19, Вестник 3666098, Руководство по устранению неполадок и ремонту, Двигатели серии QSK45 и QSK60, Вестник 3666261 или Руководство по устранению неполадок и ремонту, Двигатели серии QSK78, Вестник 3666727.

![[19801514.png]]

Если значение сопротивления правильное, проблема заключается в проводах ремня. Изолируйте проблему, проверив электропроводку.

![[19400386.png]]

Проверьте электропроводку ремня для короткого замыкания на землю. Отключите как соленоидные, так и проводные разъёмы. Прикоснитесь к многометровому щупу на контакте подачи разъёма проводов жгута. Прикоснитесь к другому многометровому щупу блока двигателя.

Измерьте сопротивление. Значение сопротивления должно быть более 1k Ом (открытая схема).

![[19801518.png]]

Удалите многометровый щуп от контакта с подачей и прикоснитесь к нему обратного контакта. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Сопротивление должно быть более 1k Ом (открытая схема).

Если в любой проверке измеряется менее 1 км ом, в электропроводке есть короткое замыкание на землю. Замените проводку упряжкой. См. процедуру[[19-019-043 — Engine Wiring Harness|019-043]].

Подключите разъём жгута проводов и соленоидный разъём, когда ремонт завершен.

![[19801519.png]]

### Проверка на замыкание между контактами

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!warning] ОСТОРОЖНО
> Аккумуляторы должны быть отключены перед выполнением этой проверки. Мультиметр будет поврежден, если батареи не отсоединятся.

Отсоедините аккумуляторные батареи.

![[ea8coha.png]]

Проверьте короткое замыкание между проводами для проблемы соленоида и всех других проводов в проводной упряжке.

Переведите замок зажигания в положение OFF.

Убедитесь, что разъём жгута проводов и соленоидный разъём отключены.

Вставьте свинец в контакт с поставкой. Вставьте другой свинец во все штифты разъема, кроме обратного контакта проблемы соленоида. Измерьте сопротивление. Сопротивление должно быть более 1k Ом (открытая схема).

![[19801515.png]]

Если между контактом с подачей и любым штифтом измеряется менее 1k Ом, в проводной упряжке между подачей или возвратным проводом есть короткое замыкание на любом штифте, который измеряется менее 1k Ом. Ремонт или замена проводов жгута. См. процедуру 019-202 или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19801516.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> To reduce the possibility of connector damage, do not use probes or leads other than Part Number 3822758. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> Inspect the solenoid circuit. Insert the pin of the lead into the supply pin A of the solenoid connector. Insert the other lead pin into the return pin B of the solenoid connector. Connect the alligator clips to the multimeter probes.
>
> Measure the resistance. Subtract the multimeter test lead resistance value from this value to determine the true solenoid circuit resistance value. The resistance **must** be 14 to 120 ohms. If the resistance value is **not** correct, proceed with the following sections. If the resistance is correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.
>
> **Resistance Value Below Specifications**
>
> Inspect the solenoid wires for short circuits between the wires. If the wires are damaged, replace the wires. Refer to Procedure 019-202.
>
> If the resistance value of the solenoid is correct, the problem is in the wiring harness. Isolate the problem by checking the wiring harness. Inspect the wiring harness for wires that have worn through insulation, cuts, and any other damage that may cause an open or short circuit. If any physical damage is found, repair or replace the damaged harness. Refer to Procedure [[19-019-072 — OEM Interface Harness|019-072]], or [[19-019-043 — Engine Wiring Harness|019-043]].
>
> Check the wiring harness. Measure the resistance between pin A and B of the harness side of the connector that was removed from the solenoid. The resistance **must** be an open circuit (more than 1k ohms). If the resistance is less than 1k ohms, replace the wiring harness or ECM. Refer to Procedure [[19-019-043 — Engine Wiring Harness|019-043]] or [[19-019-031 — Engine Control Module|019-031]].
>
> Connect the wiring harness connector when the repair is completed.
>
> **Resistance Value Above Specification**
>
> Inspect the solenoid wires for broken wires. If the wires are damaged, replace the wires. Refer to Procedure 019-202. Do **not** repair the wires.
>
> Check the 2-pin connector of the solenoid wires for proper connection.
>
> If the wire and connector looks OK, replace the solenoid. Refer to Section 2 of the Troubleshooting and Repair Manual, QSK19 Series Engines, Bulletin 3666098, the Troubleshooting and Repair Manual, QSK45 and QSK60 Series Engines, Bulletin 3666261, or the Troubleshooting and Repair Manual, QSK78 Series Engines, Bulletin 3666727.
>
> **Resistance Value Within Specification**
>
> If the resistance value is within specification, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.
>
> ### Check for Short Circuit to Ground
>
> Check the solenoid circuit for a short circuit to chassis ground.
>
> Turn the keyswitch to the OFF position
>
> Use the multimeter to measure the resistance between the solenoid output pin on the harness side of the Centinel™ Control Module and the engine block ground.
>
> The resistance **must** be more than 1k ohms (open circuit).
>
> If the resistance value is less than 1k ohms, there is a short circuit to ground in the solenoid, the solenoid wires, or the wiring harness. Proceed as follows to locate the short circuit to ground. If the resistance value is correct, the circuit **must** still be checked for a short circuit from pin to pin.
>
> Inspect the solenoid wires for a short circuit to ground. If the wires are damaged, replace the wires. Refer to Procedure 019-202. Do **not** repair the wires.
>
> Check the solenoid for a short circuit to ground. Disconnect the solenoid supply and return wires from the solenoid.
>
> Touch one multimeter probe to one of the solenoid pins. Touch the other multimeter probe to the engine block. Measure the resistance. The resistance **must** be more than 1k ohms (open circuit). If the resistance is less than 1k ohms, replace the solenoid. Refer to Section 2 of the Troubleshooting and Repair Manual, QSK19 Series Engines, Bulletin 3666098, Troubleshooting and Repair Manual, the QSK45 and QSK60 Series Engines, Bulletin 3666261, or the Troubleshooting and Repair Manual, QSK78 Series Engines, Bulletin 3666727.
>
> If the resistance value is correct, the problem is in the wiring harness. Isolate the problem by checking the wiring harness.
>
> Check the wiring harness for a short circuit to ground. Disconnect both the solenoid and wiring harness connectors. Touch the multimeter probe on the supply pin of the wiring harness connector. Touch the other multimeter probe to the engine block.
>
> Measure the resistance. The resistance value **must** be more than 1k ohms (open circuit).
>
> Remove the multimeter probe from the supply pin and touch it to the return pin. Touch the other multimeter probe to the engine block. Measure the resistance. The resistance **must** be more than 1k ohms (open circuit).
>
> If less than 1k ohms are measured in either check, there is a short circuit to ground in the wiring harness. Replace the wiring harness. Refer to Procedure [[19-019-043 — Engine Wiring Harness|019-043]].
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
> Turn the keyswitch to the OFF position.
>
> Make sure that the wiring harness connector and the solenoid connector are disconnected.
>
> Insert the lead into the supply pin. Insert the other lead into all pins of the connector except the return pin of the problem solenoid. Measure the resistance. The resistance **must** be more than 1k ohms (open circuit).
>
> If less than 1k ohms is measured between the supply pin and any pin, there is a short circuit in the wiring harness between the supply or return wire to any pin that measured less than 1k ohms. Repair or replace the wiring harness. Refer to Procedure 019-202 or [[19-019-043 — Engine Wiring Harness|019-043]].
