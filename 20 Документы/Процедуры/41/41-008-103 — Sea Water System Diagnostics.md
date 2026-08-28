---
aliases:
  - "Диагностика системы забортной воды"
type: "Процедура"
doc: "41-008-103"
title_en: "Sea Water System Diagnostics"
title_ru: "Диагностика системы забортной воды"
modified: "2004-12-08"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 27
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-008-103.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-008-103.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
  - "перевод/машинный"
---

# Sea Water System Diagnostics
**Диагностика системы забортной воды**

> [!abstract] Процедура · `41-008-103`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 8 - Cooling System - Group 08
> **Даты:** изменён 2004-12-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-008-103.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-008-103.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Типичная система охлаждения морской воды

1. Штамповка типа Grate, расположенная на дне корпуса лодки
2. Дно судна/корпус
3. Впускной клапан морской воды
4. Шланг
5. Фильтр забортной воды

![[08900279.png]]

1. Насос забортной воды
2. Топливный кулер
3. Охладитель наддувочного воздуха
4. Охладитель трансмиссионного масла
5. Теплообменник
6. Морской выход воды.

![[08900280.png]]

### Первичная проверка

Найдите и убедитесь, что впускной клапан морской воды находится в полностью открытом положении. Если он закрыт или частично закрыт, откройте клапан и перепроверьте температуру двигателя.

![[17600022.png]]

Осмотрите сетчатку морской воды на предмет посторонних предметов, которые могут ограничить поток воды.

Некоторые сетчатки имеют четкие крышки для легкого осмотра. Если сетчатку необходимо открыть для проверки, обратитесь к процедуре[[99-008-067 — Sea Water Strainer|008-067]].

![[08600057.png]]

Если двигатель работал с системой морской воды с высокой степенью ограничения из-за закрытого впускного клапана морской воды или забитого штриховщика морской воды, желательно, чтобы гребной винт морской воды должен быть проверен на предмет повреждения.

Если возраст водопроводного колеса неизвестен, рекомендуется осмотр водопроводного колеса. См. процедуру[[41-008-057 — Sea Water Pump|008-057]].

![[08900217.png]]

Если двигатель продолжает перегреваться, выполните следующие процедуры. Если двигатель перегревается на стенде подсудимых, проведите морское испытание и проверьте на предмет перегрева.

![[17600022.png]]

### Проверка

Прикрепить вакуумный калибр к входной стороне морского водяного насоса.

![[08900281.png]]

Запускай двигатель.

![[15600049.png]]

Зафиксируйте ограничение входа морской воды от низкого холостого хода до номинальной скорости с шагом 500 об/мин. Это испытание может проводиться в то время, когда судно находится в доке и не находится в снаряжении или в процессе.

См. процедуру[[41-018-018-tr — Cooling System|018-018]]Спецификации морских двигателей.

![[eg200kb.png]]

Если ограничение на вход морской воды выше спецификации, источник ограничения должен быть найден. Устранение неполадок и ремонт чрезмерного ограничения морской воды является обязанностью производителя или владельца судна. См. руководство по обслуживанию OEM судна. Если ограничение входа в соответствии с спецификацией и жалоба может быть проверена на стыке, тест должен быть повторен в процессе.

![[08900279.png]]

Если показания ограничения входа морской воды колеблются во время испытания, проверьте водоснабжение моря на наличие утечек или проникновения воздуха. Устранение неполадок и ремонт аэрации морской воды **не** покрывается гарантией Cummins.

![[08200185.png]]

Возможно, что аэрация (колебание измерительной шкалы) будет происходить только в то время, когда судно находится в процессе эксплуатации из-за введения воздуха. См. руководство по обслуживанию OEM судна.

![[08200184.png]]

### Испытание на давление

Прикрепить датчик измерения давления к выходной стороне насоса морской воды для проверки давления выхода насоса.

![[08900282.png]]

Запустите двигатель и запишите давление на выходе морской воды от низкого холостого хода до номинальной скорости с шагом 500 об/мин. Это испытание может проводиться в то время, когда судно находится на стыке и **не** в снаряжении или в процессе.

См. процедуру[[41-018-018-tr — Cooling System|018-018]]Спецификации морских двигателей.

Если давление на выходе морского водяного насоса соответствует спецификациям, обратитесь к температурному дифференциальному тесту в этой процедуре.

![[08900283.png]]

Если давление морской воды не присутствует, проверьте насос на наличие повреждений. См. процедуру[[41-008-057 — Sea Water Pump|008-057]].

![[08900284.png]]

Если давление на выходе морского водяного насоса превышает максимальное значение, то для каждого компонента системы морской воды используется избыточное падение давления, описанное на этапе испытания на дифференциальное давление.

См. процедуру[[41-018-018-tr — Cooling System|018-018]]Спецификации морских двигателей.

![[08900285.png]]

### Дифференциальный тест давления

Проверьте давление морской воды на входной стороне послеохладителя при номинальной оборотной массе. Запишите прочтение. Если падение давления между выходом морского водяного насоса и входом охладителя превышает максимальную спецификацию, проверьте или замените водопроводную систему топливного охладителя по мере необходимости.

См. процедуру[[41-018-018-tr — Cooling System|018-018]]Спецификации морских двигателей.

![[08900286.png]]

Если падение давления находится в пределах спецификации, проверьте давление морской воды на стороне сброса послеохладителя. Запишите прочтение.

Если падение давления между входной стороной послеохладителя превышает максимум, проверьте блокировку в послеохладитель. Чистить или заменить, если это необходимо.

См. процедуру[[41-018-018-tr — Cooling System|018-018]]Спецификации морских двигателей.

![[08900287.png]]

Если падение давления между входной стороной послеохладителя и выходной стороной послеохладителя находится в заданных пределах, прикрепите датчик измерения давления к дренажной пробке охладителя масел, расположенной на выходной стороне, и проверьте падение давления через охладитель масла передач.

![[08900288.png]]

Если падение давления между впускной стороной (1) и выпускной стороной (2) охладителя передач превышает максимальную спецификацию, проверьте блокировку в охладитель передач. Чистить или заменить, если это необходимо.

См. процедуру[[41-018-018-tr — Cooling System|018-018]]Спецификации морских двигателей.

![[08900289.png]]

Если падение давления в масляном охладитель передачи находится в заданных пределах, проверьте падение давления на теплообменнике двигателя.

Изготовить инструмент для испытания морской воды с помощью трубы 44 мм \[1 3/4 в\] с фитингом в центре для подключения измерителя давления.

![[08900290.png]]

Установите изготовленный испытательный инструмент между выпускной стороной теплообменника и выхлопным локтем. Проверьте падение давления через теплообменник.

Если падение давления превышает максимальную спецификацию, проверьте блокировку в теплообменнике. Чистить или заменить, если это необходимо.

См. процедуру[[41-018-018-tr — Cooling System|018-018]]Спецификации морских двигателей.

![[08900291.png]]

Если падение давления по теплообменнику находится в заданных пределах, определите падение давления по локту выхлопа (диффузора). Это делается путем вычитания давления на выходе теплообменника из давления на выходе морского водяного насоса. Если это давление превышает максимальную спецификацию, проверьте наличие закупорки в локте выхлопных газов (диффузор) и выхлопной системе судна. Чистить или заменить, если это необходимо.

См. процедуру[[41-018-018-tr — Cooling System|018-018]]Спецификации морских двигателей.

![[08900292.png]]

### Дифференциальный температурный тест

Изготовить инструмент для испытания морской воды с помощью трубы \[1 3/4 в\] с фитингом в центре для подключения датчика температуры.

![[08900290.png]]

Установите испытательный инструмент для морской воды с температурным щупом между выпускной стороной теплообменника и выхлопным локтем (1). Управляйте двигателем при номинальной оборотах в минуту и нагрузке и записывайте температуру.

![[08900293.png]]

Установите датчик температуры в выпускную сторону послеохладителя (1). Управляйте двигателем при номинальной оборотах и нагрузке и записывайте температуру. Если разница температур между выходом послеохладителя и выходом теплообменника двигателя превышает 20 ° C \[40 ° F \], проверьте насос морской воды на наличие проблем с потоком воды. См. процедуру[[41-008-057 — Sea Water Pump|008-057]].

![[08900297.png]]

Если разница температур морской воды составляет менее 3 ° C \[5 ° F \], проверьте теплообменник на предмет возможного покрытия теплообменника. Чрезмерное нанесение покрытия на внутреннюю или внешнюю часть охлаждающих трубок повлияет на эффективность теплообменника.

![[08900302.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Typical sea water cooling system
>
> 1. Grate-type strainer located on the bottom of the boat hull
> 2. Vessel bottom/hull
> 3. Sea water inlet valve
> 4. Hose
> 5. Sea water strainer
>
> 1. Sea water pump
> 2. Fuel cooler
> 3. Aftercooler
> 4. Transmission oil cooler
> 5. Heat exchanger
> 6. Sea water outlet.
>
> ### Initial Check
>
> Locate and verify that the sea water inlet valve is in the full open position. If it is closed or partially closed, open the valve and recheck the engine temperature.
>
> Inspect the sea water strainer for foreign objects that could restrict the water flow.
>
> Some strainers have clear covers for easy inspection. If the strainer has to be opened for inspection, refer to Procedure [[99-008-067 — Sea Water Strainer|008-067]].
>
> If the engine was run with the sea water system highly restricted due to a closed off sea water inlet valve or a clogged sea water strianer, it is advisable that the sea water impeller **must** be inspected for damage.
>
> If the age of the sea water impeller is unknown, inspection of the sea water impeller is advisable. Refer to Procedure [[41-008-057 — Sea Water Pump|008-057]].
>
> If the engine continues to overheat, perform the following procedures. If the engine does **not** overheat at the dock, perform a sea trial and check for overheating under way.
>
> ### Test
>
> Attach a vacuum gauge to the inlet side of the sea water pump.
>
> Start the engine.
>
> Record the sea water inlet restriction from low idle to rated speed at 500 rpm increments. This test can be conducted while the vessel is at the dock and **not** in gear or underway.
>
> Refer to Procedure [[41-018-018-tr — Cooling System|018-018]] for Marine engine specifications.
>
> If the sea water inlet restriction is above specification, the source of the restriction **must** be found. Troubleshooting and repair of excessive sea water restriction is a boat manufacturer or boat owner responsibility. Refer to the vessel's OEM service manual. If the inlet restriction is within the specification and the complaint can **not** be verified at the dock, the test **must** be repeated underway.
>
> If the sea water inlet restriction readings fluctuate during the test, inspect the sea water supply for leaks or air intrusion. Troubleshooting and repair for sea water aeration is **not** covered under Cummins warranty.
>
> It is possible that aeration (gauge fluctuation) will **only** occur while the vessel is underway due to the introduction of air. Refer to the vessel's OEM service manual.
>
> ### Pressure Test
>
> Attach a pressure gauge to the outlet side of the sea water pump to check pump outlet pressure.
>
> Start the engine and record the sea water outlet pressure from low idle to rated speed at 500 rpm increments. This test can be conducted while the vessel is at dock and **not** in gear or underway.
>
> Refer to Procedure [[41-018-018-tr — Cooling System|018-018]] for Marine engine specifications.
>
> If the sea water pump outlet pressure is within specifications, refer to the Temperature Differential Test in this procedure.
>
> If sea water pressure is **not** present, check the pump for damage. Refer to Procedure [[41-008-057 — Sea Water Pump|008-057]].
>
> If the sea water pump outlet pressure is above the maximum specification test the individual sea water system components for excessive pressure drop as described in the Pressure Differential Test step.
>
> Refer to Procedure [[41-018-018-tr — Cooling System|018-018]] for Marine engine specifications.
>
> ### Pressure Differential Test
>
> Check the sea water pressure at the inlet side of the aftercooler at the rated rpm. Record the reading. If the pressure drop between the sea water pump outlet and the aftercooler inlet exceeds the maximum specification, check or replace fuel cooler plumbing as necessary.
>
> Refer to Procedure [[41-018-018-tr — Cooling System|018-018]] for Marine engine specifications.
>
> If the pressure drop is within specification, check the sea water pressure at the discharge side of the aftercooler outlet. Record the reading.
>
> If the pressure drop between the inlet side of the aftercooler exceeds the maximum, check for blockage in the aftercooler. Clean or replace if necessary.
>
> Refer to Procedure [[41-018-018-tr — Cooling System|018-018]] for Marine engine specifications.
>
> If the pressure drop between the inlet side of the aftercooler and the outlet side of the aftercooler is within specification, attach the pressure gauge to the gear oil cooler drain plug located on the outlet side and check for pressure drop across the gear oil cooler.
>
> If the pressure drop between the inlet side (1) and the outlet side (2) of the gear cooler is greater than the maximum specification, check for blockage in the gear cooler. Clean or replace if necessary.
>
> Refer to Procedure [[41-018-018-tr — Cooling System|018-018]] for Marine engine specifications.
>
> If the pressure drop in the gear oil cooler is within specification, test the pressure drop across the engine heat exchanger.
>
> Fabricate a sea water test tool by using a 44 mm \[1 3/4 in\] pipe with a fitting in the center to connect a pressure gauge.
>
> Install the fabricated test tool between the outlet side of the heat exchanger and the exhaust elbow. Check the pressure drop across the heat exchanger.
>
> If the pressure drop is greater than the maximum specification, check for blockage in the heat exchanger. Clean or replace if necessary.
>
> Refer to Procedure [[41-018-018-tr — Cooling System|018-018]] for Marine engine specifications.
>
> If the pressure drop across the heat exchanger is within specification, determine the pressure drop across the exhaust elbow (diffuser). This is done by subtracting the heat exchanger outlet pressure from the sea water pump outlet pressure. If this pressure exceeds the maximum specification, check for blockage in the exhaust elbow (diffuser) and exhaust system of the vessel. Clean or replace if necessary.
>
> Refer to Procedure [[41-018-018-tr — Cooling System|018-018]] for Marine engine specifications.
>
> ### Temperature Differential Test
>
> Fabricate a sea water test tool by using a \[1 3/4 in\] pipe with a fitting in the center to connect a temperature probe.
>
> Install the sea water test tool with a temperature probe between the outlet side of the heat exchanger and the exhaust elbow (1). Operate the engine at rated rpm and load and record the temperature.
>
> Install the temperature probe in the outlet side of the aftercooler (1). Operate the engine at the rated rpm and load and record the temperature. If the temperature difference between the aftercooler outlet and the engine heat exchanger outlet is greater than 20° C \[40° F\], check the sea water pump for water flow problems. Refer to Procedure [[41-008-057 — Sea Water Pump|008-057]].
>
> If the sea water temperature difference is less than 3°C \[5°F\], check the heat exchanger for possible plating to the heat exchanger core. Excessive plating or coating to the inside or outside of the cooling tubes will affect the efficiency of the heat exchanger.
