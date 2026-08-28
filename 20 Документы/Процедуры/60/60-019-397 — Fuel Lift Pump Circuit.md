---
aliases:
  - "Цепь топливоподкачивающего насоса"
type: "Процедура"
doc: "60-019-397"
title_en: "Fuel Lift Pump Circuit"
title_ru: "Цепь топливоподкачивающего насоса"
modified: "2021-02-12"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-397.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-397.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Fuel Lift Pump Circuit
**Цепь топливоподкачивающего насоса**

> [!abstract] Процедура · `60-019-397`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Controls · Section 19 - Electronic Controls - Group 19 · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2021-02-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-397.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-397.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Мультиметр, номер детали 3164488

#### Дополнительные сервисные позиции

- Кабель, электропроводка, электропроводка, номер детали 3163531

### Общие сведения

Насос для подъёма топлива управляется модулем управления двигателем (ECM). ECM поставляет энергию к насосу топливного подъемника без использования реле или предохранителя.

![[25t00001.png]]

### Первичная проверка

Осмотрите упряжку для проводов двигателя, разъём мощности насоса подъемного устройства, разъём мощности ретранслятора насоса подъемного устройства и штифты ретранслятора насоса подъемного устройства для следующего:

- разъемный разъем
- разъеденные булавки
- согнутые или сломанные булавки
- отодвигать назад или расширять штифты
- влажность внутри или на разъёме
- Отсутствие или повреждение соединительных уплотнений
- грязь или мусор в или на контактах разъема
- разорванная оболочка разъёма
- повреждение изоляции провода
- Поврежденная блокировка разъема.

Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection|См. процедуру 019-361 в разделе 19.]]

Используйте следующую процедуру для правильной замены или ремонта разъемов, штифтов или проводов.[[60-019-043 — Engine Wiring Harness|См. процедуру 019-043 в разделе 19.]]

![[19400002.png]]

### Проверка сопротивления

Проверьте наличие открытой цепи в обратной цепи топливного насоса. Отсоедините 2-контактный разъем питания топливного насоса на насосе топливного лифта.

Отключите проводку двигателя с помощью разъема ECM.

Измерьте сопротивление цепи насоса топливного подъема между подачей и возвратом на 2-контактном разъеме насоса топливного подъема.

Измерьте сопротивление подачи насоса топливного лифта и обратных цепей между этими двумя разъемами.

Сопротивление должно быть 10 Ом или меньше. Если сопротивление больше 10 Ом, отремонтируйте или замените электропроводку двигателя.

![[00r00985.png]]

### Проверка напряжения

Включите переключатель зажигания, схема должна быть загружена для измерения напряжения.

1. Отсоедините разъем питания топливного насоса от разъема жгутов проводов двигателя (1).
2. Подключите кабель, электропроводку, ветку электропроводки, номер детали 3163531 к насосу топливного подъемника и электропроводку двигателя, подключите электрический разъем.
3. Подключить многометровый испытательный щуп (2) к открытому разъему на кабеле, электропроводке упряжки ветки проводов упряжки
4. Включите переключатель зажигания двигателя и измерьте падение напряжения.
5. Напряжение, указанное на мультиметре (2), должно находиться в пределах одного вольта напряжения батареи.

**Измерять напряжение только в течение первых 30 секунд включения переключателя зажигания. Если измерения** не**выполняются в течение отведенного времени, переключатель зажигания **должен быть цикличен.

| Сброс напряжения | В пределах + 1 VDC напряжения батареи |
|---|---|

- Если напряжение батареи **не** в пределах заданных значений напряжения, то был обнаружен неисправный насос топливного подъемника.
- Если напряжение батареи не указано, проверьте мультиметр на неисправность и повторите тест, если вторая проверка не дает показания напряжения, то была обнаружена неисправная проводка.
- Проверьте ECM для правильной калибровки. Если калибровка верна и актуальна, и напряжение батареи все еще не установлено, обратитесь в авторизованное место ремонта Cummins®.

![[00r00984.png]]


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Multimeter, Part Number 3164488
>
> #### Additional Service Items
>
> - Cable, Electrical Breakout Harness, Part Number 3163531
>
> ### General Information
>
> The fuel lift pump is controlled by the engine control module (ECM). The ECM supplies power to the fuel lift pump without the use of a relay or fuse.
>
> ### Initial Check
>
> Inspect the engine harness, lift pump power connector, lift pump relay power connector, and the lift pump relay pins for the following:
>
> - loose connector
> - corroded pins
> - bent or broken pins
> - pushed back or expanded pins
> - moisture in or on the connector
> - missing or damaged connector seals
> - dirt or debris in or on the connector pins
> - connector shell broken
> - wire insulation damage
> - damaged connector locking tab.
>
> Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection|Refer to Procedure 019-361 in Section 19]]
>
> Use the following procedure for the properly replace or repair the connectors, pins, or harness. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
>
> ### Resistance Check
>
> Check for an open circuit in the fuel lift pump return circuit. Disconnect the 2 pin fuel lift pump power connector at the fuel lift pump.
>
> Disconnect the engine wiring harness ECM connector.
>
> Measure the resistance of the fuel lift pump circuit between the supply and return at the 2 pin fuel lift pump connector.
>
> Measure the resistance of the fuel lift pump supply and return circuits between these two connectors.
>
> The resistance **must** be 10 ohms or less. If the resistance is greater than 10 ohms, repair or replace the engine harness.
>
> ### Voltage Check
>
> Turn the keyswitch ON, the circuit **must** be loaded to measure the voltage.
>
> 1. Disconnect the fuel lift pump power connector from engine harness connector (1).
> 2. Connect cable, electrical breakout harness, Part Number 3163531 to the fuel lift pump and engine harness electrical connector.
> 3. Connect multimeter test leads (2) to the open connector on the cable, electrical breakout harness
> 4. .Turn engine keyswitch ON and measure voltage drop.
> 5. The voltage indicated on the multimeter (2) should be within one volt of battery voltage.
>
> **Only** measure voltage during the first 30 seconds of the keyswitch being ON. If measurements are **not** done within allotted time, the keyswitch **must** be cycled.
>
> | Voltage Drop | Within + 1 VDC of battery voltage |
> |---|---|
>
> - If battery voltage is **not** within specified voltage values, then a malfunctioning fuel lift pump has been detected.
> - If battery voltage is **not** indicated, check multimeter for a malfunction and retest, if a second check yields no voltage reading, then a malfunctioning wiring harness has been detected.
> - Check the ECM for the proper calibration. If calibration is correct and up to date, and there is still **not** battery voltage, contact a Cummins® Authorized Repair Location.
