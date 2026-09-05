---
aliases:
  - "Топливная система — обзор"
type: "Процедура"
doc: "41-005-999"
title_en: "Fuel System - Overview"
title_ru: "Топливная система — обзор"
modified: "2006-08-31"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-005-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-005-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
  - "перевод/машинный"
---

# Fuel System - Overview
**Топливная система — обзор**

> [!abstract] Процедура · `41-005-999`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2006-08-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-005-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-005-999.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Функция топливной системы заключается в введении дозированного количества чистого атомизированного топлива в цилиндры двигателя в точное время ближе к концу такта сжатия. Компоненты топливной системы способствуют доставке топлива в цилиндры.

1. Топливный насос высокого давления
2. Топливные линии высокого давления
3. форсунка.

![[00900258.png]]

1. Топливный насос высокого давления
2. Линия подачи топлива
3. Топливный фильтр
4. Топливоподкачивающий насос
5. Топливный бак (не показан)
6. Линия возврата топлива.

![[fs900kt.png]]

Насос для передачи топлива механически приводится в движение плунжером, работающим против специальной доли на распределительном вале. Насос для передачи топлива содержит насосный поршень (A) и контрольные клапаны (B) (C) для управления потоком топлива и кровотока во время отключения двигателя.

1. Линия снабжения низкого давления
2. Насос предварительной прокачки
3. Впускная линия топлива
4. Голод.

![[fs901gl.png]]

Расположение клапана сброса давления в стороне подачи топливной цепи создает систему самокровотечения на топливном насосе типа А. Воздух, вводимый при замене любых компонентов на стороне подачи, автоматически вытекает из топливной системы.

Небольшое количество воздуха может быть вылито из насоса для впрыска топлива, работая ручным праймером на насосе для передачи топлива или запуская двигатель.

![[ip900kd.png]]

Двигатели 480C-E используют механический топливный насос Bosch P7100 с регулятором Bosch RE30. Механический, положительный смещенный насос для подъёма топлива обеспечивает топливо под давлением на впускной элемент топливного фильтра. Зажигательный запорный клапан с электрическим зажиганием устанавливается на выходе головки установки топливного фильтра. Фильтрируемое и герметичное топливо затем направляется обратно на вход топливного насоса.

Цель системы сброса давления, установленной на подъемном насосе, заключается в предотвращении чрезмерного давления в сборе топливного фильтра при отключении. Когда двигателю приказано выключиться, цепь переключателя зажигания прерывается и приводит к закрытию клапана отключения топлива. Когда двигатель останавливается, топливо все еще накачивается на топливный фильтр из насоса подъемника. Возможно, что давление может подняться достаточно высоко, чтобы вызвать отказ уплотнения топливного фильтра или корпуса.

Система использует рельсовый клапан в винте соединения банджо, расположенном на выходе подъемного насоса. шланг подключен к банджо, чтобы направить топливо обратно на вход насоса лифта. Рельефный клапан шарового и пружинного типа и устанавливается на открытие при 690 кПа \[100 psi\] +/- 70 кПа \[10 psi\] и регулируется **не**. Рельефный клапан должен быть открыт только после того, как двигатель был приказано остановиться.

Если предохранительный клапан застрял или полностью не сиденье, топливо будет непрерывно обходиться обратно на вход насоса подъемника. Это вызывает низкое давление на выходе насоса лифта и приводит к плохой производительности и трудному запуску.

Следуя соответствующим схемам устранения неполадок в руководстве по устранению неполадок и ремонту, выявит низкое давление насоса подъемной силы, связанное с неисправным клапаном рельефа.

![[fp901gs.png]]

> [!note] Примечание
> Насосы впрыска топлива типа MW без устройства слива топлива на стороне двигателя потребуют дополнительного вентиляции перед первоначальным запуском, заменой насоса для впрыска топлива или если у двигателя было разрешено исчерпать топливо. См. процедуру[[41-006-003 — Air in Fuel|006-003]]Для получения дополнительной информации.

![[fp900wg.png]]

Воздух от неисправленных утечек в цепи питания сделает двигатель:

- Трудно начать
- Беги грубо
- Огнестрельность
- Производить низкую мощность
- Избегать чрезмерного дыма
- Производить топливный стук.

![[oi901vj.png]]

Источник, часто упускаемый из виду для попадания воздуха в топливную систему, находится между входом префильтра и всасывающей трубкой в баке. Топливные баки, которые имеют выходную установку в верхней части, будут иметь всасывающую трубку, которая простирается до нижней части резервуара. Трещины или отверстия в штыре, которые соединяют трубку с фитингом, могут позволить воздуху проникать в топливную систему.

![[fs900se.png]]

Поскольку насос для передачи топлива обеспечивает положительное давление через топливный фильтр и линию подачи к насосу для впрыска топлива, свободные соединения или дефектные уплотнения будут отображаться как утечка топлива.

![[fs901kb.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The function of the fuel system is to inject a metered quantity of clean atomized fuel into the engine cylinders at a precise time near the end of the compression stroke. The components of the fuel system contribute to the delivery of fuel to the cylinders.
>
> 1. Fuel injection pump
> 2. High-pressure fuel lines
> 3. Injectors.
>
> 1. Fuel injection pump
> 2. Fuel supply line
> 3. Fuel filter
> 4. Fuel transfer pump
> 5. Fuel tank (**not** shown)
> 6. Fuel return line.
>
> The fuel transfer pump is mechanically driven by a plunger running against a special lobe on the camshaft. The fuel transfer pump contains a pumping piston (A) and check valves (B) (C) to control the flow of fuel and bleed back during engine shutdown.
>
> 1. Low-pressure supply line
> 2. Priming pump
> 3. Fuel inlet line
> 4. Plunger.
>
> The pressure relief valve arrangement in the supply side of the fuel circuit creates a self-bleeding system on the A-type fuel injection pump. Air introduced during replacement of any supply-side components will automatically bleed out of the fuel system.
>
> Small amounts of air can be bled from the fuel injection pump by operating the hand primer on the fuel transfer pump or by cranking the engine.
>
> Marine 480C-E engines use a Bosch® P7100 mechanical fuel pump with a Bosch® RE30 governor. A mechanical, positive displacement fuel lift pump provides pressurized fuel to the fuel filter head inlet. A keyswitch-activated electric fuel shutoff valve is mounted on the outlet of the fuel filter head. Filtered and pressurized fuel is then routed back to the fuel pump inlet.
>
> The purpose of the pressure relief system installed on the lift pump is to prevent over-pressurizeing of the fuel filter assembly upon shutdown. When the engine is commanded to shut down, the keyswitch circuit is interrupted and causes the fuel shutoff valve to close. As the engine comes to a stop, fuel is still pumped to the fuel filter from the lift pump. It is possible that the pressure can climb high enough to cause the fuel filter seal or body to fail.
>
> The system uses a relief valve in the banjo connection screw located at the outlet of the lift pump. A hose is connected to the banjo to direct the fuel back to the lift pump inlet. The relief valve is a ball and spring type and is set to open at 690 kPa \[100 psi\] +/- 70 kPa \[10 psi\] and is **not** adjustable. The relief valve should be open **only** after the engine has been commanded to stop.
>
> If the relief valve becomes stuck or does **not** seat completely, fuel will continuously be bypassed back to the lift pump inlet. This causes low lift pump output pressure and leads to poor performance and hard starting.
>
> Following the appropriate Troubleshooting Symptom charts in the Troubleshooting and Repair Manual will identify low lift pump pressure associated with a failed relief valve.
>
> **Note · Примечание**
> MW-type fuel injection pumps without the fuel drain arrangement on the engine side will require additional venting prior to initial start-up, fuel injection pump replacement, or if the engine has been allowed to run out of fuel. Refer to Procedure [[41-006-003 — Air in Fuel|006-003]] for more information.
>
> Air from uncorrected leaks in the supply circuit will make the engine:
>
> - Difficult to start
> - Run rough
> - Misfire
> - Produce low power
> - Emit excessive smoke
> - Produce fuel knock.
>
> A source, often overlooked for air to enter the fuel system, is between the inlet of the prefilter and the suction tube in the tank. Fuel tanks that have the outlet fitting at the top will have a suction tube that extends to the bottom of the tank. Cracks or pin holes in the weld that joins the tube to the fitting can allow air to enter the fuel system.
>
> Since the fuel transfer pump provides positive pressure through the fuel filter and supply line to the fuel injection pump, loose connections or defective seals will show as a fuel leak.
