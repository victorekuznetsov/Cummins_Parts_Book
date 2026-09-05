---
aliases:
  - "Топливная система — обзор"
type: "Процедура"
doc: "89-005-999"
title_en: "Fuel System - Overview"
title_ru: "Топливная система — обзор"
modified: "2003-07-08"
engines:
  - "85017333"
families:
  - "QSK23"
manuals:
  - "4021375"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-005-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-005-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
  - "перевод/машинный"
---

# Fuel System - Overview
**Топливная система — обзор**

> [!abstract] Процедура · `89-005-999`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-005-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-005-999.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Топливная система

Двигатель QSK23 оснащен топливной системой QuantumTM. Топливная система QuantumTM обеспечивает полный электронный контроль двигателя с впрыском топлива высокого давления.

Работа

Топливный насос QSK23 подает регулируемое давление в клапан управления для рельса и синхронизации в зависимости от скорости. Топливо подается как в рельсы, так и в исполнительные механизмы. Приводы действуют как дроссель для контроля количества топлива, измеренного до топливного форсунка, и линий подачи синхронизации. Датчики давления синхронизации и рельсов после приводов измеряют фактические давления, подаваемые. ECM сравнивает фактические давления, подаваемые на поставляемые устройства, с желаемыми давлениями. Желаемое давление подачи основано на положении дроссельной заслонки и входах скорости. Затем ECM передает в исполнительный механизм для изменения положения плунжера катушки, которое изменяет область отверстия потока до получения желаемого давления.

Топливный фильтр

Для QSK23 требуется два 10-микронных топливных фильтра с водоотделителями Fleetguard® Part Number FS1006, чтобы обеспечить защиту топливного форсунка и клапана управления.

![[05400181.png]]

Топливный насос

QSK23 имеет топливный насос с электронным управлением, который регулирует выходное давление до конкретных значений на основе заданной скорости двигателя. Насос имеет схему регулятора обхода топлива, управляемую приводом. Привод получает свою команду от ECM на основе датчика давления насоса и датчика скорости двигателя.

Топливный насос QSK23 очень похож на насос, используемый на двигателях серий QSK45, QSK60 и QSK78.

![[05400183.png]]

Электронная контрольная клапанная сборка (ECVA)

Электронный клапанный узел управления расположен на стороне топливного насоса двигателя. В сборке установлены следующие исполнительные механизмы и датчики:

1. Датчик давления в рамках рельсов
2. Датчик давления в топливной рельсовой магистрали
3. Датчик барометрического давления
4. Привод рельсового топлива
5. Датчик температуры топлива
6. 4.2.1.1 Сроки привода рельсового
7. Впускная способность подачи топлива
8. Срок выхода железнодорожного транспорта
9. Распорка топливного рельса
10. Клапан отсечки топлива.

![[05400182.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Fuel System
>
> The QSK23 engine is equipped with the Quantum™ fuel system. The Quantum™ fuel system provides full electronic control of the engine with high-pressure fuel injection.
>
> Operation
>
> The QSK23 fuel pump supplies regulated pressure to the control valve assembly for the rail and timing as a function of speed. The fuel is supplied to both the rail and timing actuators. The actuators act as throttles to control the amount of fuel metered to the injector and timing supply lines. Timing and rail pressure sensors, after the actuators, measure the actual supplied pressures. The ECM compares the actual supplied pressures to the desired supply pressures. Desired supply pressure is based on throttle position and speed inputs. The ECM then communicates to the actuator to change spool plunger position which changes the flow orifice area until the desired pressures are obtained.
>
> Fuel Filter
>
> The QSK23 requires two 10-micron fuel filters with water separators, Fleetguard® Part Number FS1006, to provide injector and control valve protection.
>
> Fuel Pump
>
> The QSK23 has an electronically-controlled fuel pump that regulates output pressure to specific values based on a given engine speed. The pump has a fuel bypass regulator circuit controlled by an actuator. The actuator receives its command from the ECM based on the pump pressure sensor and the engine speed sensor.
>
> The QSK23 fuel pump is very similar to the pump used on QSK45, QSK60, and QSK78 series engines.
>
> Electronic Control Valve Assembly (ECVA)
>
> The electronic control valve assembly is located on the fuel pump side of the engine. The assembly contains the following actuators and sensors:
>
> 1. Timing rail pressure sensor
> 2. Fuel rail pressure sensor
> 3. Barometric pressure sensor
> 4. Fuel rail actuator
> 5. Fuel temperature sensor
> 6. Timing rail actuator
> 7. Fuel supply inlet
> 8. Timing rail outlet
> 9. Fuel rail outlet
> 10. Fuel shutoff valve.
