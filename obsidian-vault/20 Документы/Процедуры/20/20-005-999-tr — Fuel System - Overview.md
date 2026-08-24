---
aliases:
  - "Топливная система — обзор"
type: "Процедура"
doc: "20-005-999-tr"
title_en: "Fuel System - Overview"
title_ru: "Топливная система — обзор"
modified: "2006-06-30"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-005-999-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-005-999-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Fuel System - Overview
**Топливная система — обзор**

> [!abstract] Процедура · `20-005-999-tr`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2006-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-005-999-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-005-999-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

с форсункой механического управления

> [!danger] ОПАСНО
> В зависимости от условий топливо огнеопасно. Держите все сигареты, пламя, пилотные огни, дуговое оборудование и выключатели из рабочей зоны и областей, разделяющих вентиляцию, чтобы избежать серьезных травм или смерти при работе на топливной системе.

> [!warning] ОСТОРОЖНО
> Загрязнения с топливным насосом могут аннулировать гарантию двигателя, снизить производительность двигателя и быть нарушением закона.

Топливная система QSK используется на двигателе QSK19. Дополнительная информация о топливной системе QSK доступна в Руководстве по устранению неполадок и ремонту, Электронной системе управления топливом, QSK19, QSK23, QSK45, QSK60 и двигателях QSK78, Бюллетень 3666113.

> [!note] Примечание
> Гарантийный ремонт не должен производиться на топливный насос, если работа не выполняется в магазине, отвечающем всем требованиям, установленным Cummins Inc. Для точной калибровки, тестирования и ремонта топливных систем на двигателях Cummins®.

![[06400099.png]]

Производительность двигателя определяется списком контрольных частей (CPL) и кодом топливного насоса. Калибровка топливного насоса ** должна быть в пределах опубликованных спецификаций. Калибровка топливных насосов сертифицирована несколькими агентствами по выбросам.

Топливная система QSK с механически приводимой в действие форсунки использует топливный насос типа PT для подачи линейного давления переключения передач от 414 кПа \[60 psi\] при 600 об/мин до 1931 кПа \[280 psi\] при 2100 об/мин на электронный клапан управления топливом.

![[05400009.png]]

Дробовый вал топливного насоса QSK заперт в полностью закрытом положении.

На топливном насосе QSK имеется **no** механическое дроссельное заслонка.

![[05400010.png]]

Топливный насос QSK содержит **не** клапан управления воздушным топливом (AFC). Насос **только ** имеет крышку для управления воздушным топливом (AFC).

![[05400011.png]]

Электронный клапан управления топливом расположен на стороне топливного насоса двигателя.

Электронный клапан управления топливом включает в себя:

- Датчики давления временных и рельсовых
- Сроки и приводы рельсов
- Клапан отсечки топлива
- Датчик атмосферного давления
- Впускное и выходное соединения топлива.

Электронный клапан управления топливом содержит следующие компоненты:

1. Исполнительный механизм опережения впрыска
2. Клапан отсечки топлива
3. Железнодорожный привод
4. Датчик атмосферного давления
5. Датчик давления в топливной рампе
6. Датчик давления опережения впрыска
7. Разъем линии подачи топлива
8. Разъем линии подачи топлива
9. Разъем линии подачи топлива.

![[05400012.png]]

Насос для очистки моторного масла (A) ** должен быть удален до удаления топливного насоса (B), чтобы обеспечить доступ к болтам для монтажа топливного насоса.

Топливный насос (B) ** должен быть установлен до установки насоса для очистки моторного масла (A).

![[17400021.png]]

с форсункой электронного управления

Топливная система двигателя QSK19 оснащена модульной топливной системой общего рельса. Система обеспечивает полный электронный контроль двигателя с впрыском топлива высокого давления.

![[05400240.png]]

Топливный насос состоит из двух насосов:

- Первичный насос (1) представляет собой двухпоршневой насос, обеспечивающий постоянную подачу топлива в форсунка. Насос смазывается системой моторного масла. Впускной клапан для измерения контролирует подачу топлива к насосу в зависимости от количества энергии, которое требуется. Для избыточного топлива механический клапан (6) снимает избыточное топливо с насоса и возвращает его в топливный бак. Датчик (7) давления подает сигнал на ECM для контроля давления от насоса.
- Второй насос (2), расположенный на задней панели, представляет собой насос в героторном стиле, который берет топливо из фильтра первой ступени и отправляет его через охлаждающую пластину ECM и фильтр второй ступени. На крышке (4) также находится регулятор давления для героторного насоса. Кольцо (3) обеспечивает уплотнение для предотвращения утечек.

Топливный насос подает приблизительно 1600 бар \[23 000 psi\] в форсунка, что устраняет необходимость механического впрыска. Рука клапанного качалка, трубка, кран и кулачная доля были устранены. Инъекция контролируется электронным способом через ECM. В сборе топливного фильтра для монтажа головки содержится двухступенчатая система фильтрации. Первая ступень содержит 7-микронный топливный фильтр. Первый фильтр также имеет водоотводной клапан и воду в датчике фильтра. Датчик подключен к ECM и будет предупреждать оператора с помощью контрольной лампы двигателя, если присутствует вода. Вторая ступень содержит 3-микронный топливный фильтр. Электрический насос работает только во время проворачивания, чтобы помочь в запуске.

Датчик температуры топлива и датчик давления расположены в головке крепления топливного фильтра, поэтому ECM может контролировать состояние топлива.

![[05400240.png]]

### Рекомендации по установке

Издания по установке доступны для предоставления рекомендаций по установке топливной системы, одобренных Cummins Inc. См. процедуру[[20-205-001-tr — Additional Service Literature|205-001]]для публикации заказа информации.

Свяжитесь с ближайшим авторизованным местом ремонта Cummins для спецификаций и требований к топливной системе двигателя, представленных в спецификации и приложении.

![[oi800kv.png]]

> [!danger] ОПАСНО
> В зависимости от условий топливо огнеопасно. При выполнении любых или всех из следующих процедур для удаления линий подачи топлива и связанных с ними компонентов, держите все сигареты, пламя, пилотные огни, дуговое оборудование и выключатели из рабочей зоны и областей, разделяющих вентиляцию, чтобы уменьшить вероятность серьезных травм или смерти при работе на топливной системе.

> [!danger] ОПАСНО
> Если клапан отключения топливной линии не установлен, верхний резервуар может стекать при изменении топливного фильтра, что приводит к чрезвычайной пожароопасности.

Cummins Inc. рекомендует клапан шарового типа и **не** клапан затворного типа для установки накладного резервуара.

Установите запорный клапан между фильтром и топливным баком.

![[ft8vaca.png]]

Установите контрольный клапан в линии слива топлива, когда максимальный уровень топлива в топливном баке равен или выше расхода топлива, который находится в головке цилиндра. Установите клапан со стрелкой потока топлива в сторону топливного бака.

![[06400063.png]]

Топливный насос QSK для форсунки с механическим приводом содержит интегральный контрольный клапан в выпускной розетке топливного насоса. Дополнительный контрольный клапан ** не требуется, когда максимальный уровень топлива выше слива топливного форсунка или когда топливные фильтры ниже, чем топливный бак.

> [!missing]- Иллюстрация `05400026.png` не извлечена — смотрите PDF-оригинал документа

Дизельные двигатели Cummins были разработаны, чтобы использовать высокое содержание энергии и, как правило, более низкую стоимость дизельного топлива № 2. Дизельный двигатель Cummins также будет удовлетворительно работать на топливе № 1 или других видах топлива в соответствии со следующими спецификациями. Для более подробных рекомендаций по топливу обратитесь к топливу для двигателей Cummins, Бюллетень[[3379001 — Fuels for Cummins® Engines|3379001]].


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> with Mechanically Actuated Injector
>
> **WARNING · Опасно**
> Depending on the circumstance, fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to avoid severe personal injury or death when working on the fuel system.
>
> **CAUTION · Осторожно**
> Tampering with the fuel pump can void the engine warranty, lower engine performance, and be a violation of law.
>
> The QSK fuel system is used on the QSK19 engine. Additional information about the QSK fuel system is available in the Troubleshooting and Repair Manual, Electronic Control Fuel System, QSK19, QSK23, QSK45, QSK60, and QSK78 Engines, Bulletin 3666113.
>
> **Note · Примечание**
> Warranty repairs are **not** to be made to the fuel pump unless the work is performed in a shop meeting all requirements established by Cummins Inc. to accurately calibrate, test and repair the fuel systems on Cummins® engines.
>
> The performance of the engine is defined by the control parts list (CPL) and the fuel pump code. The fuel pump calibration **must** be within published specifications. Fuel pump calibration is certified by several emissions agencies.
>
> The QSK fuel system with mechanically actuated injectors uses a PT type fuel pump to supply a linear gear pump pressure from 414 kPa \[60 psi\] at 600 rpm to 1931 kPa \[280 psi\] at 2100 rpm to the electronic fuel control valve assembly.
>
> The QSK fuel pump throttle shaft is locked in the full closed position.
>
> There is **no** mechanical throttle on the QSK fuel pump.
>
> The QSK fuel pump does **not** contain an air fuel control valve (AFC) valve. The pump **only** has an air fuel control (AFC) cover plate.
>
> The electronic fuel control valve assembly is located on the fuel pump side of the engine.
>
> The electronic fuel control valve assembly includes:
>
> - Timing and rail pressure sensors
> - Timing and rail actuators
> - Fuel shutoff valve
> - Ambient air pressure sensor
> - Fuel inlet and outlet connections.
>
> The electronic fuel control valve contains the following components:
>
> 1. Timing actuator
> 2. Fuel shutoff valve
> 3. Rail actuator
> 4. Ambient air pressure sensor
> 5. Rail pressure sensor
> 6. Timing pressure sensor
> 7. Fuel rail supply line connector
> 8. Fuel timing supply line connector
> 9. Fuel control supply line connector.
>
> The lubricating oil scavenge pump (A) **must** be removed prior to removing the fuel pump (B) to allow access to the fuel pump mounting capscrews.
>
> The fuel pump (B) **must** be installed prior to installing the lubricating oil scavenge pump (A).
>
> with Electronically Actuated Injector
>
> The fuel system for the QSK19 engine is equipped with a modular common rail fuel system. The system provides full electronic control of the engine with high-pressure fuel injection.
>
> The fuel pump consists of two pumps:
>
> - The primary pump (1) is a two piston pump that provides a constant fuel supply to the injectors. The pump is lubricated by the engine oil system. An inlet metering valve controls the fuel supply to the pump depending on the amount of power that is being required. For excess fuel, a mechanical dump valve (6) relieves excess fuel from the pump and returns it to the fuel tank. A pressure sensor (7) provides a signal to the ECM to monitor the pressure from the pump.
> - A second pump (2) located on the back is a gerotor style pump that takes fuel from the stage one filter and sends it through the ECM cooling plate and stage two filter. The cover plate (4) also contains the pressure regulator for the gerotor pump. An o-ring (3) provides a seal to prevent leaks.
>
> The fuel pump delivers approximately 1600 bar \[23,000 psi\] to the injectors, which eliminates the need for mechanical injection. The rocker arm, push tube, cam follower, and cam lobe have been eliminated. Injection is controlled electronically through the ECM. The fuel filter head assembly contains a two-stage filtration system. The first stage contains a 7 micron fuel filter. The first stage filter also has a water drain valve and water in filter sensor. The sensor is connected to the ECM and will alert the operator with a check engine lamp if water is present. The second stage contains a 3 micron fuel filter. The electric lift pump operates **only** during cranking to aid in starting.
>
> A fuel temperature sensor and pressure sensor are located in the fuel filter head so the ECM can monitor the condition of the fuel.
>
> ### Installation Recommendations
>
> Installation publications are available to provide fuel system installation recommendations approved by Cummins Inc. Refer to Procedure [[20-205-001-tr — Additional Service Literature|205-001]] for publication ordering information.
>
> Contact the nearest Cummins Authorized Repair Location for engine fuel system specifications and requirements provided on the Engine Data Sheet for your specific engine and application.
>
> **WARNING · Опасно**
> Depending on the circumstance, fuel is flammable. When performing any or all of the following procedures to remove fuel supply lines and related components, keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.
>
> **WARNING · Опасно**
> If a fuel line shutoff valve is not installed, the overhead tank can drain when the fuel filter is changed, causing an extreme fire hazard.
>
> Cummins Inc., recommends a ball-type valve and **not** a gate-type valve for the overhead tank installation.
>
> Install a fuel shutoff valve between the filter and the fuel tank.
>
> Install a check valve in the fuel drain line when the maximum fuel level in the fuel tank is even or above the fuel drain that is in the cylinder head. Install the valve with the fuel flow arrow toward the fuel tank.
>
> The QSK fuel pump for mechanically actuated injectors contains an integral check valve in the fuel pump outlet. An additional check valve is **not** required when the maximum fuel level is above the injector drain, or when the fuel filters are lower than the fuel tank.
>
> Cummins diesel engines have been developed to take advantage of the high energy content and generally lower cost of number 2 diesel fuels. A Cummins diesel engine will also operate satisfactorily on number 1 fuels or other fuels within the following specifications. For more detailed fuel recommendations, refer to Fuel for Cummins Engines, Bulletin [[3379001 — Fuels for Cummins® Engines|3379001]].
