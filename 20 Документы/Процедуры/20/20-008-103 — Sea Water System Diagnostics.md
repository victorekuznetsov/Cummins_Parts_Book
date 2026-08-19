---
aliases:
  - "Диагностика системы забортной воды"
type: "Процедура"
doc: "20-008-103"
title_en: "Sea Water System Diagnostics"
title_ru: "Диагностика системы забортной воды"
modified: "2006-06-30"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 11
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-008-103.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-008-103.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Sea Water System Diagnostics
**Диагностика системы забортной воды**

> [!abstract] Процедура · `20-008-103`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 8 - Cooling System - Group 08
> **Даты:** изменён 2006-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-008-103.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-008-103.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Типичная система охлаждения морской воды:

1. Штамповка типа Grate, расположенная на дне корпуса лодки
2. Дно судна/корпус
3. Впускной клапан морской воды
4. Шланг
5. Фильтр забортной воды
6. Насос забортной воды
7. трубка
8. Теплообменник
9. Морской выход воды.

![[08400258.png]]

### Осмотр

Найдите и убедитесь, что впускной клапан морской воды находится в полностью открытом положении. Если клапан закрыт или частично закрыт, откройте клапан и проверьте температуру двигателя.

![[08400295.png]]

### Проверка

Прикрепить вакуумный калибр к входной стороне морского водяного насоса.

![[08400259.png]]

Запускай двигатель.

![[15600049.png]]

Проверьте ограничение морской воды от холостого хода до номинальной скорости с шагом 200 об/мин, пока судно находится в доке. Ограничения на морскую воду ** должны быть менее 17 кПа \[5 in-Hg\] при любых условиях эксплуатации.

![[eg200kb.png]]

Если ограничение на вход морской воды выше спецификации, источник ограничения (1,2,3 или 4) ** должен быть найден. Устранение неполадок и ремонт чрезмерного ограничения морской воды является обязанностью производителя или владельца лодки и не покрывается гарантией Cummins®.

![[08400262.png]]

Если показания ограничения морской воды колеблются, проверьте водоснабжение моря на наличие утечек. Эти компоненты ** не** построены или поставляются компанией Cummins Inc. Устранение неполадок и ремонт аэрации морской воды ** не*** покрывается гарантией Cummins®.

![[08400260.png]]

Возможно, что аэрация (колебание измерительной шкалы) будет происходить только в то время, когда судно находится в процессе эксплуатации из-за введения воздуха.

![[08400261.png]]

### Испытание на давление

Прикрепить датчик измерения давления к выходной стороне насоса морской воды для проверки давления выхода насоса. Проверьте спецификации водяного насоса для правильного давления. Рекордное давление для следующего шага.

![[08400263.png]]

Прикрепить датчик измерения давления к стороне разряда теплообменника и проверить падение давления. Обязательно проверьте оба давления в одинаковых условиях работы, например, как на холостом ходу, так и на номинальной скорости.

![[08400264.png]]

Если падение давления между входной стороной теплообменника и выходной стороной теплообменника больше, чем спецификация, проверьте блокировку в теплообменнике.

![[08400265.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Typical sea water cooling system:
>
> 1. Grate-type strainer located on the bottom of the boat hull
> 2. Vessel bottom/hull
> 3. Sea water inlet valve
> 4. Hose
> 5. Sea water strainer
> 6. Sea water pump
> 7. Tube
> 8. Heat exchanger
> 9. Sea water outlet.
>
> ### Inspect
>
> Locate and verify that the sea water inlet valve is in the full-open position. If closed or partially closed, open the valve and check the engine temperature.
>
> ### Test
>
> Attach a vacuum gauge to the inlet side of the sea water pump.
>
> Start the engine.
>
> Check sea water restriction from idle to rated speed at 200-rpm increments while the vessel is in the dock. Sea water restrictions **must** be less than 17 kPa \[5 in-Hg\] under all operating conditions.
>
> If the sea water inlet restriction is above specification, the source of the restriction (1,2,3 or 4) **must** be found. Troubleshooting and repair of excessive sea water restriction is a boat manufacturer or boat owner responsibility and **not** covered by Cummins® warranty.
>
> If the sea water restriction readings fluctuate, inspect the sea water supply for leaks. These components are **not** built or supplied by Cummins Inc. Troubleshooting and repair of sea water aeration is **not** covered under Cummins® warranty.
>
> It is possible that aeration (gauge fluctuation) will **only** occur while the vessel is underway due to the introduction of air.
>
> ### Pressure Test
>
> Attach a pressure gauge to the outlet side of the sea water pump to check pump outlet pressure. Check water pump specifications for proper pressure. Record pressure reading for next step.
>
> Attach the pressure gauge to the discharge side of the heat exchanger and check for pressure drop. Be certain to check both pressures under the same operating conditions- for instance, both at idle or rated speed.
>
> If the pressure drop between the inlet side of the heat exchanger and the outlet side of the heat exchanger is greater than specification, check for blockage in the heat exchanger.
