---
aliases:
  - "Цепь реле зажигания"
type: "Процедура"
doc: "82-019-308"
title_en: "Ignition Relay Circuit"
title_ru: "Цепь реле зажигания"
modified: "2005-01-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-308.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-308.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Ignition Relay Circuit
**Цепь реле зажигания**

> [!abstract] Процедура · `82-019-308`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-308.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-308.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

Переведите замок зажигания в положение OFF.

Отсоедините разъём OEM-проводов от ECM.

Отсоедините разъем релейной проводов шины холостого хода/зажигания от проводной ремни OEM.

Установите мультиметр для измерения сопротивления.

![[19c00736.png]]

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте пробный щуп, номер детали 3822758, при проведении измерений.

Прикосновение к одному из мультиметров приводит к контакту 35 с OEM-разъемом проводов.

Прикосновение к другому мультиметру приводит к контакту разъема релейной проводов зажигания шины.

Считайте показания мультиметра.

![[19c00726.png]]

Мультиметр ** должен ** отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь ** не** закрыта, отремонтируйте или замените электропроводку OEM. См. процедуру 019-071.

После ремонта подсоедините все компоненты.

![[19801619.png]]

### Проверка на замыкание на массу

Переведите замок зажигания в положение OFF.

Отсоедините разъём OEM-проводов от ECM.

Отсоедините разъем релейной проводов шины холостого хода/зажигания от проводной ремни OEM.

Установите мультиметр для измерения сопротивления.

![[19c00736.png]]

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте пробный щуп, номер детали 3822758, при проведении измерений.

Прикосновение к одному из мультиметров приводит к контакту 35 с OEM-разъемом проводов.

Прикосновение к другому мультиметру приводит к заземлению блока двигателя.

Считайте показания мультиметра.

![[19c00741.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема ** не** открыта, отремонтируйте или замените проводку OEM. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверка на замыкание между контактами

Переведите замок зажигания в положение OFF.

Отсоедините разъём OEM-проводов от ECM.

Отсоедините разъем релейной проводов шины холостого хода/зажигания от проводной ремни OEM.

Установите мультиметр для измерения сопротивления.

![[19c00736.png]]

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте пробный щуп, номер детали 3822758, при проведении измерений.

Прикосновение к одному из мультиметров приводит к контакту 35 с OEM-разъемом проводов.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме.

Считайте показания мультиметра.

![[19c00754.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема ** не открыта, между контактом 35 и любым другим штифтом, который зарегистрировал замкнутую цепь, есть короткое замыкание. Ремонт или замена OEM проводов жгута. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Отсоедините разъём OEM-проводов от ECM.

Отсоедините разъем релейной проводов шины холостого хода/зажигания от проводной ремни OEM.

Установите мультиметр для измерения VDC.

Переведите замок зажигания в положение ON.

![[19c00736.png]]

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте пробный щуп, номер детали 3822758, при проведении измерений.

Прикосновение к одному из мультиметров приводит к контакту 35 с OEM-разъемом проводов.

Прикосновение к другому мультиметру приводит к заземлению блока двигателя.

Считайте показания мультиметра.

![[19c00741.png]]

Мультиметр **must** отображает показания менее 1,5 VDC.

Если напряжение ** не ** менее 1,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в OEM или проводах двигателя, который несет напряжение.

Удалите внешний источник напряжения.

После ремонта подсоедините все компоненты.

![[19c00724.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the OEM harness connector from the ECM.
>
> Disconnect the idle shutdown/ignition bus relay harness connector from the OEM harness.
>
> Set the multimeter to measure resistance.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.
>
> Touch one of the multimeter leads to pin 35 of the OEM harness connector.
>
> Touch the other multimeter lead to the ignition bus relay harness connector pin.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure 019-071.
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to Ground
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the OEM harness connector from the ECM.
>
> Disconnect the idle shutdown/ignition bus relay harness connector from the OEM harness.
>
> Set the multimeter to measure resistance.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.
>
> Touch one of the multimeter leads to pin 35 of the OEM harness connector.
>
> Touch the other multimeter lead to the engine block ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, repair or replace the OEM harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit from Pin to Pin
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the OEM harness connector from the ECM.
>
> Disconnect the idle shutdown/ignition bus relay harness connector from the OEM harness.
>
> Set the multimeter to measure resistance.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.
>
> Touch one of the multimeter leads to pin 35 of the OEM harness connector.
>
> Touch the other multimeter lead to all other pins in the connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit between pin 35 and any other pin that registered a closed circuit. Repair or replace the OEM harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to External Voltage Source
>
> Disconnect the OEM harness connector from the ECM.
>
> Disconnect the idle shutdown/ignition bus relay harness connector from the OEM harness.
>
> Set the multimeter to measure VDC.
>
> Turn the keyswitch to the ON position.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.
>
> Touch one of the multimeter leads to pin 35 of the OEM harness connector.
>
> Touch the other multimeter lead to the engine block ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 1.5 VDC.
>
> If the voltage is **not** less than 1.5 VDC, there is a short circuit to an external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the OEM or engine harness wiring that carries voltage.
>
> Remove the external voltage source.
>
> Connect all components after completing the repair.
