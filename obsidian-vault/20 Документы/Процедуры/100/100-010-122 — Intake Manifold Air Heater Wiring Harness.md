---
aliases:
  - "Жгут проводов подогревателя впускного воздуха"
type: "Процедура"
doc: "100-010-122"
title_en: "Intake Manifold Air Heater Wiring Harness"
title_ru: "Жгут проводов подогревателя впускного воздуха"
modified: "2003-08-26"
engines:
  - "93047320"
  - "93058669"
  - "93087701"
families:
  - "6B5.9"
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
  - "3666087"
figures: 14
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-010-122.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-010-122.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "двигатель/C8.3"
  - "группа/100"
  - "перевод/машинный"
---

# Intake Manifold Air Heater Wiring Harness
**Жгут проводов подогревателя впускного воздуха**

> [!abstract] Процедура · `100-010-122`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** 6B5.9, C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]], [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2003-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-010-122.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-010-122.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Удалите и проверьте предохранитель в цепи питания на модуль управления нагревателем.

![[10900319.png]]

При включении переключателя зажигания в положении Включить проверьте напряжение от цепи переключателя зажигания до предохранителя.

| Напряжение |  |
|---|---|
| Система | VDC |
| 12-VDC | 10.5 - 17 |
| 24-VDC | 22-29 |

Если не указано или низкое напряжение, проводку и соединения от переключателя зажигания к держателю предохранителя  необходимо проверить.

Воздушный обогреватель будет **не** функционировать должным образом, если не будет получено указанное напряжение.

![[10900320.png]]

### Проверка напряжения

Подключите положительный щуп мультиметра к клеммам элементов нагревателя воздуха.

Направьте отрицательный щуп на хорошо известную землю.

![[10900306.png]]

> [!danger] ОПАСНО
> Сетки и шпильки нагревателя могут стать достаточно горячими, чтобы сжечь кожу.

> [!warning] ОСТОРОЖНО
> Не перерабатывать переключатель зажигания повторно в течение короткого периода времени. Это может привести к повреждению сетки или проводов.

Прикрепить мультиметр к проводам нагревателя.

Закрепите многометровый датчик тока вокруг обоих проводов к нагревателю воздуха.

Следующий тест будет длиться до 20 секунд. Время цикла предварительного нагрева см. в разделе «Общая информация».

| Напряжение системы | Диапазон напряжения | Диапазон ампеража |
|---|---|---|
| 12 | 10.5 - 17 | 80-110 (1 сетка) |
| 12 | 10.5 - 17 | 160-220 (2 сетки) |
| 24 | 22-29 | 80 - 110 |

Переведите замок зажигания в положение ON. Не трогай двигатель.

Записывайте показания напряжения и усилителя.

Переключатель зажигания должен быть выключен и снова включен, чтобы переработать.

Показания напряжения и ампеража должны быть в пределах спецификации.

![[10900322.png]]

Если напряжение не обнаружено, отсоедините датчик температуры впуска.

Отключение датчика температуры впуска имитирует температуру впускного коллектора менее 0°C \[32°F\]. Это перекрывает температурную цепь, если температура впускного коллектора слишком высока, чтобы позволить нагревателю включиться.

Выключите зажигание, затем снова включите.

Перепроверить показания напряжения и ампера.

См. раздел E для определения местоположения датчика.

![[10900298.png]]

Проверить цикл предварительного нагрева. Через 20 секунд напряжение и усилие должны упасть до нуля, когда цикл закончится.

Лампа «Watit to Start», если она оборудована, будет работать в течение 20 секунд. Через 20 секунд лампа начнет мигать, указывая на то, что цикл нагревателя выключен. Лампа будет продолжать мигать до тех пор, пока датчик температуры впуска отключен, что указывает на открытую цепь.

![[15200051.png]]

Если напряжение не обнаружено в сетке нагревателя с отключенным датчиком температуры потребления, проверьте напряжение на соленоид.

Подключите мультиметр и проверьте напряжение питания к соленоидной вторичной цепи (большой терминал).

Если напряжение отсутствует, отремонтируйте проводку до соленоида.

Если напряжение присутствует, проверьте соленоид.

См. процедуру[[100-010-126 — Intake Manifold Air Heater Solenoid Switch|010-126]], Intake Manifold Air Heater Solenoid Switch.

![[10900323.png]]

Проверьте напряжение на первичной стороне соленоида, от небольшого терминала до небольшого терминала.

Если нет напряжения, проверьте землю.

Если напряжение присутствует на обоих терминалах, замените соленоид.

![[10900324.png]]

Проверьте напряжение от соленоидной положительной первичной цепи до хорошо известной поверхности.

Если напряжение отсутствует, проверьте напряжение на модуле управления нагревателем.

Если напряжение присутствует, восстановить землю на соленоид.

![[10900325.png]]

Модуль управления соленоидом и нагревателем имеет одинаковую поверхность.

Проверьте провод или почистите разъемы.

![[10900298.png]]

Проверьте напряжение на модуле управления нагревателем.

Лампа WAIT TO START, если она оборудована, будет оставаться включенной, если нет напряжения на модуле управления нагревателем.

![[15200051.png]]

Если лампы WAIT TO START нет, проверьте напряжение на резисторе в проводе питания от предохранителя до модуля управления нагревателем.

Если нет напряжения, отремонтируйте проводку.

Смотрите схему проводов.

![[10900326.png]]

Если напряжение присутствует, проверьте резистор с помощью омметра.

Замените резистор, если это необходимо.

Сопротивление: 15.8k Ом на 12-VDC

![[10900327.png]]

Проверьте напряжение на обоих положительных датчиках при подключении к модулю управления нагревателем.

Если напряжение **не** присутствует, отремонтируйте электропроводку.

Если напряжение присутствует, замените модуль управления нагревателем.

![[10900325.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Remove and check the fuse in the power circuit to the heater control module.
>
> With the keyswitch in the ON position, verify the voltage from the keyswitch circuit to the fuse.
>
> | Voltage |  |
> |---|---|
> | System | VDC |
> | 12-VDC | 10.5 to 17 |
> | 24-VDC | 22 to 29 |
>
> If no or low voltage is indicated, the wiring and connections from the keyswitch to the fuse holder **must** be checked.
>
> The air heater will **not** function properly unless the specified voltage is obtained.
>
> ### Voltage Check
>
> Connect the positive lead of the multimeter to the air heater element terminals.
>
> Ground the negative lead to a good known ground.
>
> **WARNING · Опасно**
> Heater grids and studs can get hot enough to burn skin.
>
> **CAUTION · Осторожно**
> Do not recycle the keyswitch repeatedly in a short period of time. This may cause damage to the grids or the wiring.
>
> Attach a multimeter to the heater element wires.
>
> Clamp the multimeter current probe around both wires to the air heater.
>
> The following test will **only** last up to 20 seconds. Refer to the preheat cycle time in the General Information section.
>
> | System Voltage | Voltage Range | Amperage Range |
> |---|---|---|
> | 12 | 10.5 to 17 | 80 to 110 (1 grid) |
> | 12 | 10.5 to 17 | 160 to 220 (2 grids) |
> | 24 | 22 to 29 | 80 to 110 |
>
> Turn the keyswitch to the ON position. Do **not** crank the engine.
>
> Record both the voltage and amperage readings.
>
> The keyswitch **must** be turned OFF and ON again in order to recycle.
>
> Voltage and amperage readings **must** be within the specified limits.
>
> If no voltage is detected, disconnect the intake temperature sensor.
>
> Disconnecting the intake temperature sensor simulates intake manifold temperature of less than 0°C \[32°F\]. This overrides the temperature circuit if the intake manifold temperature is too hot to allow the heater to turn on.
>
> Turn the keyswitch OFF, then ON again.
>
> Recheck the voltage and ampere readings.
>
> Refer to Section E for the sensor location.
>
> Verify the preheat cycle. After 20 seconds the voltage and amperage should drop to zero when the cycle ends.
>
> The WAIT TO START lamp, if equipped, will stay on for 20 seconds. After 20 seconds, the lamp will begin to flash indicating the heater cycle has turned off. The lamp will continue to flash as long as the intake temperature sensor is disconnected indicating an open circuit.
>
> If no voltage is detected at the heater grid with the intake temperature sensor disconnected, check the voltage to the solenoid.
>
> Connect the multimeter and check the supply voltage to the solenoid secondary circuit (large terminal).
>
> If no voltage is present, repair the wiring to the solenoid.
>
> If voltage is present, check the solenoid.
>
> Refer to Procedure [[100-010-126 — Intake Manifold Air Heater Solenoid Switch|010-126]], Intake Manifold Air Heater Solenoid Switch.
>
> Check the voltage on the primary side of the solenoid, small terminal to small terminal.
>
> If no voltage is present, check the ground.
>
> If voltage is present at both terminals, replace the solenoid.
>
> Check the voltage from the solenoid positive primary circuit to a good known ground.
>
> If no voltage is present, check the voltage to the heater control module.
>
> If voltage is present, restore the ground to the solenoid.
>
> The solenoid and heater control module share the same ground.
>
> Check the wire or clean the connectors.
>
> Check the voltage to the heater control module.
>
> The WAIT TO START lamp, if equipped, will stay on if there is no voltage to the heater control module.
>
> If there is no WAIT TO START lamp, check the voltage at the resistor in the supply wire from the fuse to the heater control module.
>
> If no voltage is present, repair the wiring harness.
>
> Refer to the wiring diagram.
>
> If voltage is present, check the resistor with an ohmmeter.
>
> Replace the resistor if necessary.
>
> Resistance: 15.8k ohms at 12-VDC
>
> Check the voltage at both positive leads at the connection to the heater control module.
>
> If voltage is **not** present, repair the wiring harness.
>
> If voltage is present, replace the heater control module.
