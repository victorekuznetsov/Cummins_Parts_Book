---
aliases:
  - "Устройство EHAB"
type: "Процедура"
doc: "57-005-083"
title_en: "EHAB Device"
title_ru: "Устройство EHAB"
modified: "2022-07-06"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021539"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/57/57-005-083.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/57-005-083.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/57"
  - "перевод/машинный"
---

# EHAB Device
**Устройство EHAB**

> [!abstract] Процедура · `57-005-083`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021539 — QST30 Service Manual|4021539]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2022-07-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/57/57-005-083.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/57-005-083.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Устройство Bosch® «EHAB» используется только на промышленной версии QST30. Он служит в качестве устройства управления топливом, контролируя поток топлива (включено/выключено) и направление потока. Устройство EHAB состоит из корпуса, электрического соленоида, привода и шпулевого клапанного узла.

![[05a00046.png]]

С включенным переключателем зажигания устройство Bosch® EHAB подпитывается энергией, и шпулевой клапан перемещается, чтобы обеспечить поток топлива из бака к насосу для подъёма топлива и из фильтров в галерею насоса для впрыска.

1. Запуск топлива из бака
2. Перелив топлива из галереи насосов для инъекций
3. Расход топлива для подъема насоса
4. Фильтрируемое топливо в
5. Впускной насос (фильтрованное топливо).

![[05a00058.png]]

Когда замок зажигания выключен, устройство Bosch® EHAB обесточено, и шпулевой клапан движется в противоположном направлении. Это предотвращает поток топлива в галерею насоса для впрыска и открывает путь, в результате чего насос лифта выкачивает топливо из галереи и обратно в бак.

1. Галерея переполненный порт
2. перелив топлива
3. Топливо из галереи для подъема насоса
4. Фильтрируемое топливо в
5. Отфильтрованное топливо вернулось на впуск бака
6. Перепускной клапан топливного насоса.

![[05a00059.png]]

### Проверка

> [!note] Примечание
> Этот тест проверяет внутренний соленоид Bosch® EHAB.

Выключите замок зажигания автомобиля.

Отключите 9-контактный электрический разъем впрыска топлива Deutsch. **Не отсоединять 2-контактный разъем устройства EHAB.

![[19a00338.png]]

Прислушайтесь к устройству EHAB и попросите кого-нибудь повернуть переключатель зажигания в положение Включения. Здесь вы должны щелкать звук, так как внутренний соленоид заряжает энергией. Если щелчок звука **не** слышен, проведите переключатель зажигания три или четыре раза. Если щелчок звука все еще не слышен, проверьте сопротивление, как описано ниже.

![[05a00098.png]]

Выключите замок зажигания.

Отсоедините 2-контактный разъем устройства EHAB от электропроводки двигателя.

![[19a00339.png]]

Измерьте сопротивление между двумя штифтами разъема устройства EHAB.

Внутреннее сопротивление EHAB должно быть от 38,5 до 43,5 Ом.

Если устройство Bosch® EHAB не проходит ни одного испытания, оно должно быть обслуживается авторизованным местом ремонта Bosch® или заменено. На данный момент устройство Bosch® EHAB** является только заменяемым в качестве сборки.

![[19a00753.png]]

### Снятие

> [!warning] ОСТОРОЖНО
> Не удаляйте соленоид/исполнитель из корпуса устройства Bosch® «EHAB». На данный момент устройство Bosch® «EHAB» можно заменить только в виде сборки.

![[05a00046.png]]

Удалите четыре болта и устройство Bosch® «EHAB» из корпуса насоса для впрыска топлива.

![[05a00062.png]]

### Очистка

> [!danger] ОПАСНО
> При работе со сжатым воздухом применяйте защиту глаз и лица. Разлетающиеся частицы и грязь могут привести к травме.

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

> [!warning] ОСТОРОЖНО
> Используйте чистящий растворитель, который не навредит алюминию.

Используйте щетку и растворитель для очистки устройства Bosch® «EHAB», фитингов, линий и окружающей среды.

Просушите сжатым воздухом.

![[05a00060.png]]

### Проверка при повторном использовании

Осмотрите устройство Bosch® «EHAB» на наличие вмятин, трещин и других повреждений корпуса.

Осмотрите устройство на предмет разделения, поломок, порезов или других повреждений электрического кабеля.

Проверка на наличие свободных или отсутствующих соленоидных/актуаторных болтов.

![[05a00061.png]]

### Установка

Положение двух о-кольцев на устройстве Bosch® «EHAB».

Установите устройство Bosch® EHAB и поместите его на корпус насоса для впрыска.

> [!note] Примечание
> Используйте Loctite 242 на четырех крепежных болтах перед установкой.

> [!tip] Момент затяжки
> 8 Н·м [71 фунт-дюйм]

![[05a00062.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The Bosch® “EHAB” device is used on **only** the industrial version of the QST30. It serves as a fuel control device by controlling the fuel flow (on/off) and the direction of flow. The EHAB device consists of a housing, electrical solenoid, actuator, and spool valve assembly.
>
> With the keyswitch on, the Bosch® EHAB device is energized and the spool valve moves to allow fuel flow from the tank to the fuel lift pump and from the filters into the injection pump gallery.
>
> 1. Fuel inlet from tank
> 2. Fuel overflow from injection pump gallery
> 3. Fuel outlet to lift pump
> 4. Filtered fuel in
> 5. Injection pump inlet (filtered fuel).
>
> When the keyswitch is turned off, the Bosch® EHAB device is de-energized and the spool valve moves in the opposite direction. This prevents the flow of fuel into the injection pump gallery and opens a path, causing the lift pump to pump fuel out of the gallery and back to the tank.
>
> 1. Gallery overflow port
> 2. Fuel overflow
> 3. Fuel from gallery to lift pump
> 4. Filtered fuel in
> 5. Filtered fuel returned to tank inlet
> 6. Fuel pump overflow valve.
>
> ### Test
>
> **Note · Примечание**
> This test checks the Bosch® EHAB internal solenoid.
>
> Turn the vehicle keyswitch OFF.
>
> Disconnect the 9-pin Deutsch fuel injection pump electrical connector. Do **not** disconnect the 2-pin EHAB device connector.
>
> Listen closely to the EHAB device and have someone turn the keyswitch to the ON position. You should here a clicking sound as the internal solenoid energizes. If a clicking sound is **not** heard, cycle the keyswitch three or four times. If a clicking sound is still **not** heard, check the resistance as described below.
>
> Turn the keyswitch OFF.
>
> Disconnect the 2-pin EHAB device connector from the engine harness.
>
> Measure the resistance between both pins of the EHAB device connector.
>
> The EHAB internal resistance **must** read between 38.5 to 43.5Ohms.
>
> If the Bosch® EHAB device fails either test, it **must** be serviced by an authorized Bosch® repair location or replaced. At the moment, the Bosch® EHAB device is **only** replaceable as an assembly.
>
> ### Remove
>
> **CAUTION · Осторожно**
> Do not remove the solenoid/actuator from the Bosch® “EHAB” device housing. At the moment, the Bosch® “EHAB” device is only replaceable as an assembly.
>
> Remove four capscrews and the Bosch® “EHAB” device from the fuel injection pump housing.
>
> ### Clean
>
> **WARNING · Опасно**
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> **CAUTION · Осторожно**
> Use a cleaning solvent that will not harm aluminum.
>
> Use a brush and solvent to clean the Bosch® “EHAB” device, fittings, lines, and surrounding area.
>
> Dry with compressed air.
>
> ### Inspect for Reuse
>
> Inspect the Bosch® “EHAB” device for dents, cracks, and other damage to the housing.
>
> Inspect the device for separation, frays, cuts, or other damage to the electrical cable.
>
> Inspect for loose or missing solenoid/actuator capscrews.
>
> ### Install
>
> Position two o-rings on the Bosch® “EHAB” device.
>
> Install the Bosch® EHAB device and position on the injection pump housing.
>
> **Note · Примечание**
> Use Loctite 242 on the four mounting capscrews before installation.
>
> **Момент затяжки · Torque Value**
> 8 n•m [71 in-lb]
