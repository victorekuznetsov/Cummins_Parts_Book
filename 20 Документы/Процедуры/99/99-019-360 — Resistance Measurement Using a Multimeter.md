---
aliases:
  - "Измерение сопротивления мультиметром"
type: "Процедура"
doc: "99-019-360"
title_en: "Resistance Measurement Using a Multimeter"
title_ru: "Измерение сопротивления мультиметром"
modified: "2012-03-26"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "41349633"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK19"
  - "QST30"
manuals:
  - "3666184"
  - "3666214"
  - "3666266"
  - "4021419"
  - "4021442"
  - "4021587"
  - "4021617"
  - "4021674"
figures: 14
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-360.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-360.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "группа/99"
  - "перевод/машинный"
---

# Resistance Measurement Using a Multimeter
**Измерение сопротивления мультиметром**

> [!abstract] Процедура · `99-019-360`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11, QSK19, QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]], [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19 · Section 19 — Electronic Engine Controls · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2012-03-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-360.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-360.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Используйте эту процедуру ** только**, если проводка ремня или разъема может быть отремонтирована.

После выполнения любой из приведенных ниже проверок, а также необходимости ремонта или замены электропроводки или разъёма, обратитесь к таблице содержимого в разделе 19 для соответствующей процедуры ремонта или замены.

Дерево устранения неисправностей кода ошибки будет ссылаться на эту процедуру, когда необходимо измерить сопротивление на проводах, разъеме или компоненте, к которому применяется код неисправности. Каждое дерево устранения неисправностей кода неисправности будет устранять неисправности конкретного компонента и связанной с ним схемы, такой как датчик давления, проводная упряжка и разъемы, которые соединяют датчик с электронным блоком управления.

При устранении неполадок для определения, существует ли короткий или открытый в конкретной цепи, все связанные разъемы, контакты, имена схем и соединения, которые применяются к этому компоненту, можно просматривать на соответствующей схеме проводов.

Используйте следующие процедуры, чтобы определить, как сделать необходимые проверки сопротивления на компонентах, разъемах и схемах, которые применяются к коду неисправности, который ссылался на эту процедуру.

![[nobox.png]]

### Проверка сопротивления

Выключите зажигание.

Отсоедините соответствующий разъем от компонента.

Настройте мультиметр для измерения сопротивления.

Используйте схему проводов, чтобы определить контакты, которые применяются к компоненту, который вы измеряете.

![[19400226.png]]

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения штифта и проводов, используйте соответствующий испытательный щуп для разъема. См. список инструментов обслуживания или соответствующий комплект для ремонта проводов.

Подключите соответствующий соединительный испытательный щуп к контактам разъёма и соедините зажимы аллигатора с многометровым щупом. Измерьте сопротивление.

Сравните это значение с применимым спецификацией кода неисправности или применимым электрическим или сенсорным спецификациями на схеме проводов. Если значение не правильное, компонент неисправен. См. применимую процедуру кода неисправности для инструкций.

![[19400227.png]]

### Проверка непрерывности

Непрерывность — электрическое соединение между двумя штифтами, которое меньше определенного значения. Для проводов жгута спецификация составляет менее 10 Ом.

![[19900495.png]]

Переключатель зажигания переключателя в положение выключения.

Отключите проводные разъёмы, которые должны быть протестированы.

Настройте мультиметр для измерения сопротивления.

![[19c00186.png]]

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения штифта и проводов, используйте соответствующий испытательный щуп для разъема. См. список инструментов обслуживания или соответствующий комплект для ремонта проводов.

Подключите соответствующий соединительный испытательный щуп к контактам разъёма и соедините зажимы аллигатора с многометровым щупом. Измерьте сопротивление.

![[19900496.png]]

Мультиметр **must** отображает менее 10 Ом для непрерывности провода. Если мультиметр отображает более 10 Ом, провод ** должен быть отремонтирован или заменен электропроводкой.

См. применимую процедуру кода неисправности для инструкций.

![[19400225.png]]

### Проверка на замыкание между контактами

Короткое замыкание от пин-к пин-проверки - это состояние, при котором электрическое соединение существует между двумя пинами, где оно не предназначено для существования.

Переключатель зажигания переключателя в положение выключения.

Отключите проводные разъёмы, которые должны быть протестированы.

Настройте мультиметр для измерения сопротивления.

![[19400213.png]]

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения штифта и проводов, используйте соответствующий испытательный щуп для разъема. См. список инструментов обслуживания или соответствующий комплект для ремонта проводов.

Подключите соответствующий пробный щуп разъёма к контактам разъёма и соедините зажимы аллигатора с многометровыми зондами. Измерьте сопротивление.

![[19800315.png]]

Мультиметр **must** читает больше 100k ом, что является открытой схемой. Если цепь ** не открыта, то проверяемые контакты электрически соединены. Смотрите схему проводов, чтобы убедиться, что провода предназначены для подключения.

Проверьте разъёмы проводов для влаги, которые могут вызвать ненадлежащее электрическое соединение.[[99-019-361 — Component Connector and Pin Inspection|См. процедуру 019-361]].

См. применимую процедуру кода неисправности для инструкций.

![[19a00016.png]]

### Проверка на замыкание на массу

Короткое замыкание на землю - это состояние, при котором соединение от цепи к земле существует, когда оно не предназначено.

Переключатель зажигания переключателя в положение выключения.

Отключите проводные разъёмы, которые должны быть протестированы.

![[19200195.png]]

При тестировании датчика требуется отключить только соединение датчика.

При испытании электропроводного ремня разъем электропроводки на электронном блоке управления и разъем на датчике или нескольких датчиках ** должны быть отключены.

Определите штифты, которые необходимо проверить.

Проверьте контакты разъема.[[99-019-361 — Component Connector and Pin Inspection|См. процедуру 019-361]].

![[19800313.png]]

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения штифта и проводов, используйте соответствующий испытательный щуп для разъема. См. список инструментов обслуживания или соответствующий комплект для ремонта проводов.

Подключите соответствующий пробный щуп разъёма к контакту разъёма и соедините зажим аллигатора с многометровым щупом.

Прикоснитесь к другому многометровому щупу с чистой, неокрашенной поверхностью на блоке двигателя или на земле шасси. Измерьте сопротивление.

![[19800314.png]]

Мультиметр **must** считывает более 100k ом, что указывает на открытую схему. Если цепь ** не** открыта, проверяемый провод имеет короткое замыкание на землю, блок двигателя или заземление шасси.

См. применимую процедуру кода неисправности для инструкций.

![[19800016.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Use this procedure **only** if the harness or connector can be repaired.
>
> After performing any of the checks below, and it is necessary to repair or replace a harness or connector, refer to the table of contents in section 19 for the appropriate repair or replacement procedure.
>
> Fault code troubleshooting trees will refer to this procedure when it is necessary to measure resistance on a harness, connector, or component that the fault code applies to. Each fault code troubleshooting tree will troubleshoot a particular component and the associated circuitry such as a pressure sensor, wiring harness and connectors that connect the sensor to the electronic control unit.
>
> When troubleshooting to determine if a short or open exists in a particular circuit, all of the associated connectors, pins, circuit names and connections that apply to this component can be viewed on the applicable wiring diagram.
>
> Use the following procedures to determine how to make the necessary resistance checks on components, connectors and circuits that apply to the fault code that referred you to this procedure.
>
> ### Resistance Check
>
> Turn the key switch off.
>
> Disconnect the appropriate connector from the component.
>
> Adjust the multimeter to measure resistance.
>
> Use the wiring diagram to determine the pins that apply to the component you are measuring.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the appropriate test lead for the connector. Refer to the Service Tools listing or the appropriate wiring repair kit.
>
> Connect the appropriate connector test leads to the connector pins and connect the alligator clips to the multimeter probe. Measure the resistance.
>
> Compare this value to the applicable fault code specification or applicable Electrical or Sensor Specification on the wiring diagram. If the value is not correct, the component is malfunctioning. Refer to the applicable fault code procedure for instructions.
>
> ### Continuity Check
>
> Continuity is an electrical connection between two pins that is less than a certain value. For harness wires, the specification is less than 10 ohms.
>
> Turn the key switch to the OFF position.
>
> Disconnect the harness connectors that are to be tested.
>
> Adjust the multimeter to measure resistance.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the appropriate test lead for the connector. Refer to the Service Tools listing or the appropriate wiring repair kit.
>
> Connect the appropriate connector test leads to the connector pins and connect the alligator clips to the multimeter probe. Measure the resistance.
>
> The multimeter **must** display less than 10 ohms for wire continuity. If the multimeter displays greater than 10 ohms, the wire **must** be repaired or the harness replaced.
>
> Refer to the applicable fault code procedure for instructions.
>
> ### Check for Short Circuit from Pin to Pin
>
> Short circuit from pin to pin check is a condition in which an electrical connection exists between two pins where it is **not** intended to exist.
>
> Turn the key switch to the OFF position.
>
> Disconnect the harness connectors that are to be tested.
>
> Adjust the multimeter to measure resistance.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the appropriate test lead for the connector. Refer to the Service Tools listing or the appropriate wiring repair kit.
>
> Connect the appropriate connector test leads to the connector pins and connect the alligator clips to the multimeter probes. Measure the resistance.
>
> The multimeter **must** read greater than 100k ohms, which is an open circuit. If the circuit is **not** open, the pins being checked are electrically connected. Refer to the wiring diagram to verify that the wires are intended to be connected.
>
> Inspect the harness connectors for moisture that can cause an inappropriate electrical connection. [[99-019-361 — Component Connector and Pin Inspection|Refer to Procedure procedure 019-361]].
>
> Refer to the applicable fault code procedure for instructions.
>
> ### Check for Short Circuit to Ground
>
> Short circuit to ground is a condition where a connection from a circuit to ground exists when it is not intended.
>
> Turn the key switch to the OFF position.
>
> Disconnect the harness connectors that are to be tested.
>
> When testing a sensor, **only** the sensor connection is required to be disconnected.
>
> When testing a harness, the harness connector at the electronic control unit and the connector at the sensor or multiple sensors **must** be disconnected.
>
> Identify the pins that need to be tested.
>
> Inspect the connector pins. [[99-019-361 — Component Connector and Pin Inspection|Refer to Procedure procedure 019-361]].
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the appropriate test lead for the connector. Refer to the Service Tools listing or the appropriate wiring repair kit.
>
> Connect the appropriate connector test lead to a connector pin and connect the alligator clip to the multimeter probe.
>
> Touch the other multimeter probe to a clean, unpainted surface on the engine block or chassis ground. Measure the resistance.
>
> The multimeter **must** read greater than 100k ohms, which indicates an open circuit. If the circuit is **not** open, the wire being checked has a short circuit to ground, the engine block or chassis ground.
>
> Refer to the applicable fault code procedure for instructions.
