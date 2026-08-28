---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "87-019-050"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2022-08-16"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `87-019-050`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2022-08-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-050.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка

Этот тест проверяет внутренний соленоид Bosch® EHAB. Переключатель зажигания транспортного средства в положение выключения.

Отключите 9-контактный электрический разъем впрыска топлива Deutsch. Не отсоединяйте 2-контактный разъем EHAB.

![[19a00338.png]]

При внимательном прослушивании устройства Bosch® EHAB попросите кого-нибудь повернуть переключатель зажигания в положение Включения. Вы должны услышать щелкающий звук, когда внутренний соленоид заряжается энергией.

Если щелчок звука **не** слышен, проверьте сопротивление следующим образом.

![[19a00752.png]]

Переключатель зажигания транспортного средства в положение выключения. Отсоедините 2-контактный разъем устройства Bosch® EHAB от электропроводки двигателя. Установите мультиметр для измерения сопротивления. Подключите аллигаторы к многометровым зондам.

![[19a00339.png]]

Измерить сопротивление между контактами разъема Bosch® EHAB, стороны устройства EHAB. Сопротивление **должно** измеряться между 38,5 и 43,5 Ом.

Если устройство Bosch® EHAB не справляется с вышеуказанными испытаниями, оно должно обслуживаться авторизованным местом ремонта Bosch® или заменять устройство.

> [!note] Примечание
> На данный момент устройство Bosch® EHAB является сменным **только*** в качестве сборки.

![[19a00753.png]]

### Снятие

Очистите клапан отключения топлива EHAB и окружающую область.

![[19a00282.png]]

Отсоедините клапан отключения топлива EHAB от электропроводки двигателя.

![[19a00249.png]]

Удалите крепежные болты. Удалите соленоидный корпус, топливный щит, пружинную стиральную машину, клапанный диск, приводной диск и приводной корпус.

Уплотнительные кольца утилизируйте.

![[19a00283.png]]

### Установка

Соберите запорный клапан и новое кольцо.

Установите соленоид и болты.

> [!tip] Момент затяжки
> 8 Н·м [71 фунт-дюйм]

![[19a00283.png]]

Подключите клапан отключения топлива EHAB к электропроводке двигателя.

![[19a00249.png]]

### Проверка сопротивления

Отсоедините клапан отключения топлива EHAB от электропроводки двигателя.

Используйте мультиметр для проверки сопротивления катушки. Сопротивление катушки должно быть от 38,5 до 43,5 Ом для клапанов EHAB.

Если сопротивление катушки не соответствует спецификации, катушка должна быть заменена.[[87-019-050 — Fuel Shutoff Valve|См. процедуру 019-050]].

Подключите клапан к электропроводке двигателя, когда ремонт завершен.

![[19a00284.png]]

### Проверка напряжения

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения штифта и проводов, используйте проводку с помощью ветвящегося кабеля, номер детали 3163531, при проведении измерения.

Отсоедините электропроводку двигателя от EHAB (запорный клапан топлива). Установите проводной ремень ветвь кабеля между ремнем электропроводки двигателя и разъемом EHAB. Установите мультиметр для измерения напряжения. Переведите замок зажигания в положение ON.

![[19a00741.png]]

Прикосновение одного из мультиметров приводит к красному испытательному щупу проводного ветвящегося кабеля, а другого — к черному щупу кабеля. Измерьте напряжение.

Значение напряжения **должно быть** непереключенным напряжением батареи. Если напряжение не измеряет то же самое напряжение, что и напряжение непереключенной батареи, и все другие проверки проводов были выполнены и прошли спецификацию, ECM не сработал.

Заменить ECM.[[87-019-031 — Engine Control Module|См. процедуру 019-031]].

![[19a00741.png]]


> [!quote]- Original (English) · английский оригинал
> ### Test
>
> This test checks the Bosch® EHAB internal solenoid. Turn the vehicle keyswitch to the OFF position.
>
> Disconnect the 9-pin Deutsch fuel injection pump electrical connector. Do **not** disconnect the 2-pin EHAB connector.
>
> While listening closely to the Bosch® EHAB device, have someone turn the keyswitch to the ON position. You should hear a clicking sound as the internal solenoid energizes.
>
> If a clicking sound is **not** heard, check the resistance as follows.
>
> Turn the vehicle keyswitch to the OFF position. Disconnect the 2-pin Bosch® EHAB device connector from the engine harness. Set the multimeter to measure resistance. Connect the alligator clips of the test leads to the multimeter probes.
>
> Measure the resistance between the pins of the Bosch® EHAB connector, EHAB device side. The resistance **must** measure between 38.5 and 43.5 ohms.
>
> If the Bosch® EHAB device fails **either** of the above tests, it **must** be serviced by an authorized Bosch® repair location, or replace the device.
>
> **Note · Примечание**
> At the moment, the Bosch® EHAB device is replaceable **only** as an assembly.
>
> ### Remove
>
> Clean the EHAB fuel shutoff valve and surrounding area.
>
> Disconnect the EHAB fuel shutoff valve from the engine harness.
>
> Remove the mounting capscrews. Remove the solenoid housing, fuel shield, spring washer, valve disc, actuator disc, and actuator housing.
>
> Discard the o-rings.
>
> ### Install
>
> Assemble the shutoff valve install and new o-ring.
>
> Install the solenoid and the capscrews.
>
> **Момент затяжки · Torque Value**
> 8 n•m [71 in-lb]
>
> Connect the EHAB fuel shutoff valve to the engine harness.
>
> ### Resistance Check
>
> Disconnect the EHAB fuel shutoff valve from the engine harness.
>
> Use the multimeter to check the coil resistance. The coil resistance **must** be 38.5 to 43.5 ohms for EHAB valves.
>
> If the coil resistance does **not** meet specification, the coil **must** be replaced. [[87-019-050 — Fuel Shutoff Valve|Refer to Procedure 019-050]].
>
> Connect the valve to the engine harness when the repair is complete.
>
> ### Voltage Check
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use breakout cable, Part Number 3163531, when taking a measurement.
>
> Disconnect the engine harness from the EHAB (fuel shutoff valve). Install the breakout cable between the engine harness and the EHAB connector. Set the multimeter to measure voltage. Turn the keyswitch to the ON position.
>
> Touch one of the multimeter leads to the red test lead of the breakout cable and the other lead to the black lead of the cable. Measure the voltage.
>
> The voltage value **must** be unswitched battery voltage. If the voltage does **not** measure the same voltage as unswitched battery voltage and all other wiring checks have been performed and passed specification, the ECM has failed.
>
> Replace the ECM. [[87-019-031 — Engine Control Module|Refer to Procedure 019-031]].
