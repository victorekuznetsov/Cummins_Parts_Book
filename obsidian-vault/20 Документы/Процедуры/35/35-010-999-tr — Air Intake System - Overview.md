---
aliases:
  - "Система впуска воздуха — обзор"
type: "Процедура"
doc: "35-010-999-tr"
title_en: "Air Intake System - Overview"
title_ru: "Система впуска воздуха — обзор"
modified: "2009-03-05"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-010-999-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-010-999-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Air Intake System - Overview
**Система впуска воздуха — обзор**

> [!abstract] Процедура · `35-010-999-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2009-03-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-010-999-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-010-999-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Переменный геометрический турбокомпрессор:

Турбокомпрессор с изменяемой геометрией используется на автомобиле с CM870, автомобиле с CM875 и автомобиле с двигателями CM876, чтобы максимизировать производительность двигателя, а также помочь снизить уровень выбросов.

Турбокомпрессоры с изменяемой геометрией имеют более быстрое время отклика и более быстрое замедление двигателя для более быстрого сдвига, чем турбокомпрессоры с фиксированной геометрией.

Из-за активного управления турбокомпрессором с изменяемой геометрией часто может изменяться давление впускного коллектора и звук турбокомпрессора. Существует **не** потеря мощности, связанная с изменением давления впускного коллектора; однако, восприятие мощности двигателя клиентом может быть затронуто. Как правило, когда давление впускного коллектора и звук турбокомпрессора изменяются во время работы в устойчивом состоянии, ECM регулирует поток EGR в двигатель, и мощность двигателя **не **влияет.

Когда дроссель высвобождается, возможно, для переключения передач, привод переменной геометрии закрывается. Это готовит турбокомпрессор к быстрому наращиванию давления впускного коллектора, чтобы обеспечить улучшенную реакцию турбокомпрессора, когда дросселя подавлено после смены передачи. Благодаря этой конструкции для улучшенного отклика турбокомпрессора, после выпуска дроссельной заслонки, скорость двигателя ISM с турбокомпрессором с изменяемой геометрией может снижаться быстрее, чем двигатель без турбокомпрессора с изменяемой геометрией. Быстрое замедление скорости двигателя может заставить водителей регулировать изменения стилей, пока они не привыкнут к различным скоростям замедления.

Из-за того, что механизм изменяемой геометрии содержится внутри корпуса турбины, обязательно, чтобы зажим V-диапазона не был нарушен во время обслуживания турбокомпрессора. Размывание зажима V-диапазона и вращение корпуса подшипника или корпуса турбины может привести к тому, что механизм переменной геометрии затормозится, а турбокомпрессор выйдет из строя. Сервисные турбокомпрессоры с правильной ориентацией корпуса турбины доступны, поэтому никаких регулировок не требуется.

Подобно всем тяжеловесным двигателям с электронным управлением Cummins®, двигатель ISM с турбокомпрессором с изменяемой геометрией включает в себя снижение мощности для защиты турбокомпрессора от повреждений при работе на больших высотах. Турбокомпрессор с изменяемой геометрией соответствует или превышает выходную мощность двигателей с турбокомпрессором с фиксированной геометрией на большинстве высот. Однако при высоте 2,438 км[8000 футов] небольшое снижение мощности может быть заметно при работе двигателя с турбокомпрессором переменной геометрии и сравнении его производительности с двигателем с турбокомпрессором фиксированной геометрии.

Автомобильный с CM875

Автомобильные двигатели CM875 и CM870 с турбокомпрессором переменной геометрии пневматически приводятся в действие воздухом из воздушных баков OEM. Высокое давление воздуха от клапана управления турбокомпрессором закрывает механизм переменной геометрии, который увеличивает давление выхлопных газов и облегчает поток EGR через двигатель. Механизм закрывающей переменной геометрии также увеличивает скорость турбокомпрессора и давление впускного коллектора при определенных условиях работы двигателя. Более низкое давление воздуха от клапана управления турбокомпрессором открывает механизм переменной геометрии, который снижает давление выхлопных газов, скорость турбокомпрессора и давление впускного коллектора при определенных условиях работы двигателя.

![[19202572.png]]

![[10200115.png]]

Рисунок 1

Рисунок 2

CM870 - Low Mount Turbocharger Control клапан - турбокомпрессор с низким уровнем заряда

В автомобильных двигателях CM870 используется как клапан управления турбокомпрессором, который расположен ниже охладителя моторного масла, так и фильтр для очистки воздуха и запорный клапанный узел. Фильтр воздухоочистителя и запорный клапанный узел установлены на переднем шестеренок корпуса, на стороне топливного насоса двигателя. См. рис.1 и рис.2.

![[19202655.png]]

Рис. 3

Автомобиль с CM875 - High Mount Turbocharger Control клапан

Автомобильные двигатели CM875 используют высоковольтный клапан управления турбокомпрессором. Высоконапорный клапан управления турбокомпрессором **не требует фильтра для очистки воздуха. Однако транспортное средство **должно быть оснащено воздушной сушилкой для удовлетворения требований к установке двигателя. Воздух, поступающий в транспортное средство, будет подаваться непосредственно в впускной порт управляющего клапана, идентифицированный как порт (1). Порт подачи воздуха на выходе турбокомпрессора переменной геометрии идентифицируется как порт (2).

![[10c00164.png]]

Рис. 4

Автомобильный с CM876

Автомобиль с турбокомпрессором переменной геометрии CM876 приводится в действие электронным способом. Электронный модуль управления (ECM) посылает команду непосредственно в привод изменяемой геометрии, установленный на турбокомпрессоре. См. рисунок 4.

Закрытие механизма изменяемой геометрии увеличивает давление выхлопных газов, облегчая поток EGR через двигатель. Скорость турбокомпрессора и давление впускного коллектора также будут увеличиваться при закрытии механизма изменяемой геометрии при определенных условиях работы двигателя. Закрытие турбокомпрессора с изменяемой геометрией также повысит температуру выхлопных газов при определенных нормальных условиях работы двигателя и во время регенерации после обработки. Это используется для повышения эффективности компонентов после обработки.

[[35-011-999-tr — Exhaust System - Overview|См. процедуру 011-999 в разделе F.]]для получения дополнительной информации о взаимодействии турбокомпрессора с изменяемой геометрией и системы последующей обработки.

Открытие механизма переменной геометрии снижает давление выхлопных газов, скорость турбокомпрессора и давление впускного коллектора при определенных условиях работы двигателя.

Система сгорания воздуха на двигателях серии M состоит из впускных воздушных трубопроводов, турбокомпрессора, воздушных трубопроводов заряда, воздушного охладителя заряда и трубопроводов выхлопных газов.

![[ew200gk.png]]

Турбокомпрессор использует энергию выхлопных газов для поворота колеса турбины. Колесо турбины приводит в движение компрессорный импеллер, который обеспечивает под давлением воздух для двигателя для сгорания. Дополнительный воздух, обеспечиваемый турбокомпрессором, позволяет впрыскивать больше топлива, чтобы увеличить выходную мощность двигателя.

![[tb800pb.png]]

Адекватный запас хорошего, фильтрованного масла очень важен для срока службы турбокомпрессора.

Колеса турбины и компрессора, а также вал поддерживаются двумя вращающимися подшипниками в корпусе подшипника. Проходы в подшипниковой обшивке непосредственно фильтруют, прессуют моторное масло к подшипникам вала и подшипникам тяги. Масло используется для смазки и охлаждения вращающихся компонентов, для обеспечения бесперебойной работы. Затем масло стекает из подшипникового кожуха в отстойник двигателя через линию слива масла. Ограниченная линия отвода масла может привести к тому, что корпус турбокомпрессора будет находиться под давлением, в результате чего масло протечет мимо колец уплотнения.

![[tb200pa.png]]

По мере того, как воздух на впуске сжимается турбокомпрессором, температура воздуха увеличивается. Этот нагретый воздух затем проходит через охладитель воздуха, который охлаждает воздух. Холодный воздух более плотный, что позволяет сжимать больше воздуха в цилиндр, что дает гораздо большую эффективность сгорания.

![[10c00001.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Variable Geometry Turbocharger:
>
> A variable geometry turbocharger is used on the automotive with CM870, automotive with CM875 and automotive with CM876 engines to maximize the performance of the engine and also to help decrease emissions levels.
>
> Variable geometry turbochargers have quicker response time, and quicker engine deceleration for quicker shifting than fixed geometry turbochargers.
>
> Because of the active control of the variable geometry turbocharger, the intake manifold pressure and turbocharger sound can often change. There is **not** a loss of power associated with the change in intake manifold pressure; however, customer perception of engine power can be affected. Typically, when the intake manifold pressure and turbocharger sound are changing during steady state operation, the ECM is adjusting the EGR flow into the engine and the engine's power is **not** affected.
>
> When the throttle is released, perhaps for a gear change, the variable geometry actuator closes. This prepares the turbocharger to be ready to build intake manifold pressure quickly to provide improved turbocharger response when the throttle is depressed after the gear change. Because of this design for improved turbocharger response, after releasing the throttle, the engine speed of the ISM engine with a variable geometry turbocharger can decrease more quickly than an engine without a variable geometry turbocharger. Fast deceleration of engine speed can cause the drivers to adjust shifting styles until becoming accustomed to the different deceleration speeds.
>
> Due to the variable geometry mechanism being contained inside the turbine housing, it is mandatory that the V-band clamp is **not** disturbed during turbocharger servicing. Loosening the V-band clamp and rotating the bearing housing or turbine housing can cause the variable geometry mechanism to jam and the turbocharger to fail. Service turbochargers with the proper turbine housing orientation are available so that no adjustments are necessary.
>
> Similar to all of Cummins® electronically controlled heavy duty engines, the ISM engine with variable geometry turbocharger incorporates a power derate to protect the turbocharger from damage while operating in high altitudes. The variable geometry turbocharger meets or exceeds the power output of the engines with a fixed geometry turbocharger at most altitudes. At and around 2.438 km \[8000 ft\] elevation, however, a slight power decrease can be noticeable when operating the engine with a variable geometry turbocharger and comparing its performance to an engine with a fixed geometry turbocharger.
>
> Automotive with CM875
>
> The automotive CM875 and CM870 engines with variable geometry turbocharger is pneumatically actuated with air from the OEM air tanks. High air pressure from the turbocharger control valve closes the variable geometry mechanism, which increases the exhaust gas pressure and facilitates EGR flow through the engine. A closing variable geometry mechanism also increases turbocharger speed and intake manifold pressure under certain engine operating conditions. Lower air pressure from the turbocharger control valve opens the variable geometry mechanism, which decreases exhaust gas pressure, turbocharger speed, and intake manifold pressure under certain engine operating conditions.
>
> Figure 1
>
> Figure 2
>
> With CM870 - Low Mount Turbocharger Control Valve
>
> Automotive CM870 engines use both the turbocharger control valve, which is located below the lubricating oil cooler, along with an air filter and shutoff valve assembly. The air filter and shutoff valve assembly is mounted on the front gear housing, on the fuel pump side of the engine. See Figure 1 and Figure 2.
>
> Figure 3
>
> Automotive with CM875 - High Mount Turbocharger Control Valve
>
> The automotive CM875 engines use the high mount turbocharger control valve. The high mount turbocharger control valve does **not** require an air filter. However, the vehicle **must** be equipped with an air dryer to meet engine installation requirements. The vehicle air supply will be plumbed directly to the control valve inlet port identified as port (1). The outlet air supply port to the variable geometry turbocharger is identified as port (2).
>
> Figure 4
>
> Automotive with CM876
>
> The automotive with CM876 variable geometry turbocharger is electronically actuated. The electronic control module (ECM) sends a command directly to the variable geometry actuator mounted on the turbocharger. See Figure 4.
>
> Closing the variable geometry mechanism increases the exhaust gas pressure, facilitating EGR flow through the engine. The turbocharger speed and intake manifold pressure will also increase when the variable geometry mechanism closes, under certain engine operating conditions. Closing the variable geometry turbocharger will also increase the exhaust gas temperature, under certain normal engine operating conditions, and during the aftertreatment regeneration event. This is used to improve the aftertreatment component efficiency.
>
> [[35-011-999-tr — Exhaust System - Overview|Refer to Procedure 011-999 in Section F]] for further information regarding the variable geometry turbocharger and aftertreatment system interactions.
>
> Opening the variable geometry mechanism decreases exhaust gas pressure, turbocharger speed, and intake manifold pressure under certain engine operating conditions.
>
> The combustion air system on M Series engines consists of intake air piping, turbocharger, charge air piping, charge air cooler, and exhaust gas piping.
>
> The turbocharger uses exhaust gas energy to turn the turbine wheel. The turbine wheel drives the compressor impeller, which provides pressurized air to the engine for combustion. The additional air provided by the turbocharger allows more fuel to be injected, to increase the power output of the engine.
>
> An adequate supply of good, filtered oil is very important to the operating life of the turbocharger.
>
> The turbine and compressor wheels, and the shaft are supported by two rotating bearings in the bearing housing. Passages in the bearing housing direct filtered, pressurized engine oil to the shaft bearings and thrust bearings. The oil is used to lubricate and cool the rotating components, to provide for smooth operation. The oil then drains from the bearing housing to the engine sump through the oil drain line. A restricted oil drain line can cause the turbocharger bearing housing to be pressurized, causing oil to leak past the seal rings.
>
> As the intake air is compressed by the turbocharger, the air temperature increases. This heated air is then passed through the charge-air cooler, which cools the air. Cool air is more dense, which allows more air to be compressed into the cylinder, yielding a much greater combustion efficiency.
