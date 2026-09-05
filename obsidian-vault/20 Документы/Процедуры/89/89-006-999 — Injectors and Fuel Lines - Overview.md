---
aliases:
  - "Форсунки и топливные магистрали — обзор"
type: "Процедура"
doc: "89-006-999"
title_en: "Injectors and Fuel Lines - Overview"
title_ru: "Форсунки и топливные магистрали — обзор"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-006-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-006-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
  - "перевод/машинный"
---

# Injectors and Fuel Lines - Overview
**Форсунки и топливные магистрали — обзор**

> [!abstract] Процедура · `89-006-999`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-006-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-006-999.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Топливные трубки

Подача топлива QSK23 (1), синхронизация подачи (2) и слив топлива (3) интегрированы в корпус впускного коллектора.

Линии подачи топлива и стока рассчитаны на обеспечение достаточного потока для впрыска и синхронизации функций. Прямые резьбы лицевой окольной фитинги используются для превосходной профилактики утечки.

Рекомендуемый размер впускной линии топливного насоса обеспечивает максимальное ограничение фильтра на уровне 102 мм рт.ст. \[4 в рт.ст. ] при высокой безотказной нагрузке.

Фитинг слива топлива обеспечивает максимальное ограничение линии слива 203 мм рт.ст. \[8 в рт.ст. \].

Температура топлива на входе топливного насоса **не должна **превышать 71°C \[160°F\]. Возможно, потребуется охладитель топлива в цепи слива топлива. Топливный охладитель должен быть предоставлен производителем оригинального оборудования (OEM).

![[06400179.png]]

Топливные рельсы в впускном коллекторе получают топливо от электронного привода клапана управления (ECVA) через подающую трубку (1) топливного рельса и подающую трубку (2) синхронизации топлива. Затем топливо проходит через топливные рельсы, через головку цилиндра и в форсунка. Неиспользованное топливо течет обратно через головку цилиндра, в топливный рельс и через установку слива топлива (3), чтобы вернуться в топливный бак.

Промышленные применения с двойными впускными коллекторами будут иметь стальную обратную линию, соединяющую два коллектора с установкой слива топлива.

![[06400180.png]]

Форсунка QuantumTM

Форсунка QSK23 QuantumTM начинает работу с дозирования. Нижний плунжер втягивается во время внутренней части круга основания профиля распределительного вала, таким образом, открывая порт подачи рельса. Топливо - это время давления (PT), измеренное в сопле. Измеренное количество является функцией давления на рельсах и скорости двигателя. Это давление питания будет таким же высоким, как 1379 кПа \[200 psi\] при максимальной заправке/скорости и таким же низким, как 13,8 кПа \[2 psi\] при простое время.

Топливо синхронизации также измеряется через отдельный порт учета в камеру между верхним и временным плунжерами в стволе. Это также происходит во время внутренней части круга основания профиля распределительного вала, начиная с того момента, когда верхний плунжер втягивается и обнаруживает порт подачи времени. Сроки дозирования заканчиваются, когда распределительный вал приводит в движение верхний плунжер вниз, покрывая порт подачи дозирования и удерживая топливо между верхним и временным плунжерами. Это захваченное топливо действует как твердое гидравлическое звено. Нижний плунжер также движется вниз, закрывая порт подачи рельсов и заканчивая закачиваемым счетчиком топлива.

Количество топлива, замеренное в камере синхронизации, определяет количество разделения верхних и синхронизирующих плунжеров. Это количество разделения, называемое перепутыванием, варьируется от приблизительного минимума 2 мм \[0,078 in\] при пиковом заправлении крутящим моментом до максимума 9 мм \[0,354 in\] при заправке на холостом ходу. Количество переезда изменяется, чтобы изменить начало впрыска для всех скоростей и условий заправки.

![[06400181.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Fuel Tubes
>
> The QSK23 fuel rail supply (1), timing rail supply (2), and fuel drain (3) are integrated into the intake manifold housing.
>
> Fuel supply and drain lines are sized to provide sufficient flow for injection and timing functions. Straight thread face o-ring fittings are used for superior leak prevention.
>
> The recommended fuel pump inlet line size provides a maximum clean filter restriction of 102 mm Hg \[4 in Hg\] at high idle-no load.
>
> The fuel drain fitting provides a maximum drain line restriction of 203 mm Hg \[8 in Hg\].
>
> The fuel temperature at the fuel pump inlet **must not** exceed 71°C \[160°F\]. A fuel cooler in the fuel drain circuit will possibly be required. The fuel cooler is to be provided by the original equipment manufacturer (OEM).
>
> The fuel rails in the intake manifold receive fuel from the Electronic Control Valve Actuator (ECVA) through a fuel rail supply tube (1) and fuel timing supply tube (2). The fuel then passes through the fuel rails, through the cylinder head, and into the injectors. Unused fuel flows back through the cylinder head, into the fuel rail, and out through the fuel drain fitting (3) to return to the fuel tank.
>
> Industrial applications with dual intake manifolds will have a steel return line connecting the two manifolds to the fuel drain fitting.
>
> Quantum™ Injector
>
> The QSK23 Quantum™ injector begins operation with metering. The lower plunger retracts during the inner base circle portion of the camshaft profile, thus uncovering the rail feed port. The fuel is Pressure Time (PT) metered into the nozzle. The amount metered is a function of rail pressure and engine speed. This supply pressure will be as high as 1379 kPa \[200 psi\] at maximum fueling/speed and as low as 13.8 kPa \[2 psi\] at idle.
>
> The timing fuel is also PT metered through a separate metering port into a chamber between the upper and timing plungers in the barrel. This also occurs during the inner base circle portion of the camshaft profile beginning when the upper plunger retracts and uncovers the timing feed port. Timing metering ends when the camshaft drives the upper plunger downward, covering the metering feed port and trapping the fuel between the upper and timing plungers. This trapped fuel acts as a solid hydraulic link. The lower plunger also moves downward, closing the rail feed port and ending injected fuel metering.
>
> The amount of fuel metered into the timing chamber determines the amount of separation of the upper and timing plungers. This separation amount, called overtravel, varies from an approximate minimum of 2 mm \[0.078 in\] at torque peak fueling to a maximum of 9 mm \[0.354 in\] at high idle fueling. The amount of overtravel is changed to vary the start of injection for all speed and fueling conditions.
