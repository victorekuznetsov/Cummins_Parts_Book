---
aliases:
  - "Система выпуска — обзор"
type: "Процедура"
doc: "35-011-999-tr"
title_en: "Exhaust System - Overview"
title_ru: "Система выпуска — обзор"
modified: "2015-04-01"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-011-999-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-011-999-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Exhaust System - Overview
**Система выпуска — обзор**

> [!abstract] Процедура · `35-011-999-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2015-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-011-999-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-011-999-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Выхлопной газ рециркулируется через двигатель, чтобы уменьшить количество окислов азота (NO x), выделяемых из двигателя. Выхлопные газы охлаждаются, когда они проходят через охладитель рециркуляции выхлопных газов (EGR), а затем смешиваются с сжатым свежим воздухом из турбокомпрессора перед входом в впускной коллектор. EGR был введен для уменьшения количества кислорода в цилиндре, доступного для сгорания, при сохранении того же количества потока через двигатель. Выхлопные газы, присутствующие в начале горения, очень стабильны и имеют очень медленную скорость реакции. Они поглощают тепло во время сгорания, что приводит к снижению пиковых температур пламени в цилиндре и, следовательно, к снижению выбросов NO x.

Миксер EGR был разработан для полного смешивания газа EGR с турбированным воздухом из охладителя воздуха. Полное смешивание необходимо для обеспечения бесперебойной работы и снижения выбросов.

Клапан EGR управляется электронным модулем управления (ECM). ISM с двигателями CM870 управляет клапаном EGR модулированным сигналом шириной импульса, посылаемым ECM, и работает от 0 до 100 процентов. Когда клапан EGR открыт, выхлопные газы текут с горячей стороны двигателя, через охладитель EGR и в смеситель EGR.

ISM с двигателями CM876 управляет клапаном EGR через сигнал шины данных J1939 CAN, отправленный ECM, и работает от 0 до 100 процентов. Когда клапан EGR открыт, выхлопные газы текут из охладителя EGR через соединительную трубку EGR и в смеситель EGR.

ISM с соединительной трубкой CM876 EGR обеспечивает поток охлажденных выхлопных газов от выпускного отверстия клапана EGR в задней части двигателя до смесителя EGR перед впускным коллектором. Этот двигатель использует двухкомпонентную конструкцию соединительной трубки EGR, которая также включает в себя трубку EGR venturi.

Подключительная трубка ISM CM870 и ISM CM875 EGR обеспечивает поток охлажденных выхлопных газов от выпускного отверстия охладителя EGR в задней части двигателя до смесителя EGR перед впускным коллектором. Этот двигатель использует двухкомпонентную соединительную трубку EGR, которая также включает в себя трубку EGR venturi.

Трубка EGR venturi содержит проточный отверстие, которое используется для измерения количества потока выхлопных газов с использованием датчика дифференциального давления EGR и трубок высокого и эталонного датчиков дифференциального давления.

Выхлопной коллектор для ISM с двигателем CM876 был переработан, чтобы включить металлическое уплотнение в скольжениях в усилиях по уменьшению утечки. Выхлопной коллектор также имеет порт рядом с портом номер один для датчика давления выхлопных газов.

Турбокомпрессор с изменяемой геометрией необходим для нескольких важных условий работы двигателя. Он используется для облегчения потока EGR через двигатель.[[35-010-999-tr — Air Intake System - Overview|См. процедуру 010-999 в разделе F.]]для получения дополнительной информации о турбокомпрессорах с изменяемой геометрией и взаимодействиях потока EGR.

Турбокомпрессор с изменяемой геометрией также используется для торможения двигателя. Механизм изменяемой геометрии закрывается для увеличения давления выхлопного коллектора. Повышенное давление выхлопных газов работает против поршней на тормозящей скорости двигателя выхлопного хода.

Система последующей обработки используется для сокращения выбросов твердых частиц и состоит из шести основных компонентов:

1. После лечения впуск
2. После обработки дизельного фильтра твердых частиц датчик дифференциального давления
3. После обработки дизельным катализатором окисления
4. После обработки дизельным фильтром твердых частиц
5. После лечения выход
6. После обработки датчики температуры выхлопных газов.

> [!note] Примечание
> В некоторых применениях катализатор окисления дизельного топлива после обработки может содержаться в впускной секции системы последующей обработки.

![[11c00256.png]]

Пассивная регенерация происходит, когда температура выхлопных газов достаточно высока, чтобы окислить сажу, собранную в фильтре для твердых частиц дизельного топлива после обработки, быстрее, чем собранная сажа.

Пассивная регенерация обычно происходит, когда температура фильтра для твердых частиц дизельного топлива после обработки выше 316 ° C \[600° F \]. Это происходит во время движения по шоссе или вождения с тяжелыми нагрузками.

Поскольку пассивная регенерация происходит естественным образом, она считается нормальной работой двигателя. В поток выхлопных газов при пассивной регенерации топливо не добавляется.

![[11c00256.png]]

Активная регенерация происходит, когда температура выхлопных газов **не** достаточно высока, чтобы окислить сажу, собранную в фильтре для твердых частиц дизельного топлива после обработки, быстрее, чем она собирается.

Активная регенерация требует помощи от двигателя для повышения температуры выхлопа. Это обычно делается путем впрыска небольшого количества дизельного топлива в поток выхлопных газов (так называемый впрыск после обработки), который затем окисляется катализатором окисления дизельного топлива после обработки. Окисление этого дополнительного топлива создает тепло, необходимое для регенерации фильтра для твердых частиц дизельного топлива после обработки.

Для активной регенерации ECM** должен** обнаружить, что ограничение фильтра для твердых частиц дизельного топлива после обработки достигло определенного предела. Как только этот предел будет достигнут, двигатель изменит свою работу, чтобы создать достаточно высокие температуры выхлопных газов, чтобы активно регенерировать фильтр для твердых частиц дизельного топлива после обработки.

Активное событие регенерации обычно состоит из двух частей: фаза разогрева и регенерация.

Цель фазы разогрева заключается в повышении температуры выхлопных газов до такой степени, что может произойти инъекция после обработки.

![[11d00170.png]]

Послеоперационная инъекция требует, чтобы температура в системе послеоперационной обработки достигала приблизительно 288 ° C [550° F ]. При этой температуре и выше небольшое количество топлива, впрыскиваемого в выхлоп, будет должным образом окисляться через катализатор окисления дизельного топлива после обработки, создавая дополнительное тепло, необходимое для активного восстановления фильтра твердых частиц дизельного топлива после обработки.

После завершения фазы разогрева и начала последующей обработки, начинается фаза активной регенерации.

Во время активной регенерации двигатель ECM контролирует температуру выхлопных газов до и после последующей обработки дизельным фильтром твердых частиц и поддерживает температуру в диапазоне примерно от 427 до 649 ° C \[800 до 1200° F \]. Количество топлива, используемого для последующей обработки, будет варьироваться, поскольку температура контролируется в этих пределах.

Температура, достигаемая во время активной регенерации, обычно выше, чем температура, достигаемая во время пассивной регенерации. Преобразование сажи в углекислый газ происходит гораздо быстрее, поскольку температура увеличивается.

Типичное активное событие регенерации займет от 20 до 40 минут, пока автомобиль работает. Оператор транспортного средства может замечать дополнительный шум турбокомпрессора в течение этого времени, а также освещенную лампу с высокой температурой выхлопа, если она оборудована.

Частота, с которой двигатель потребует активной регенерации, сильно варьируется от приложения к приложению. В целом, для транспортных средств с низкой скоростью движения, таких как городские транспортные средства, или с низким уровнем нагрузки, потребуется более активное восстановление, чем для транспортных средств с высокой нагрузкой или транспортных средств с высоким уровнем скорости.

ECM двигателя также содержит функцию, основанную на времени для активной регенерации, которая используется для проверки правильной работы после обработки, когда рабочий цикл транспортного средства обычно достаточно высок, чтобы активные события регенерации не были необходимы.

В некоторых условиях эксплуатации, таких как низкая скорость, низкая нагрузка или циклы остановки и движения, двигатель может **не** иметь достаточно возможностей для регенерации фильтра дизельных твердых частиц после обработки во время нормальной работы транспортного средства. Когда это происходит, двигатель освещает лампу фильтра для дизельных частиц после обработки, чтобы сообщить оператору транспортного средства, что требуется помощь, как правило, в виде стационарной (припаркованной) регенерации.

Стационарная (припаркованная) регенерация – это форма активной регенерации, которая инициируется оператором транспортного средства, когда транспортное средство не движется.

Следующая процедура предоставляет дополнительную информацию о стационарной (паркованной) регенерации.[[101-014-013 — Aftertreatment Testing|См. процедуру 014-013 в разделе 14.]]

![[11d00294.png]]

Изготовитель транспортного средства имеет такую возможность установки двух переключателей, которые контролируют функции последующей обработки: Стартовый выключатель и разрешительный выключатель.

Стартовый переключатель (известный как Diesel Particulate Filter Regeneration Start Switch в электронном сервисном оборудовании INSITETM) используется для запуска стационарной (припаркованной) регенерации. Производитель транспортного средства может также ссылаться на этот переключатель как на стационарный переключатель регенерации, переключатель запуска или переключатель припаркованной регенерации.

Переключатель разрешения (известный как Diesel Particulate Filter Permit Switch в электронном сервисном оборудовании INSITETM) используется для того, чтобы оператор транспортного средства мог отключить активную регенерацию, если это необходимо. Производитель транспортного средства может также ссылаться на этот переключатель как на тормозной переключатель, стоп-переключатель или выключатель.

Следующая процедура описывает операцию переключателя и шаги устранения неполадок.[[35-011-056 — Exhaust System Diagnostics|См. процедуру 011-056 в разделе 11.]]

Автомобильный с CM570

Отработанный турбокомпрессор представляет собой модель Holset® HX55. Он состоит из турбокомпрессора, привода обходного клапана турбины и обходного клапана турбины в корпусе турбины. Отработанный турбокомпрессор обеспечивает улучшенную реакцию при низких оборотах двигателя без ущерба для долговечности турбокомпрессора на высоких скоростях. Это достигается за счет того, что выхлопные газы обходят колесо турбины при определенных режимах работы двигателя. Во время работы с низким оборотом турбокомпрессор работает как турбокомпрессор с закрытой системой, где энергия газов передается на колесо компрессора и используется для сжатия впускного воздуха. Однако во время работы с высокой оборотной силой турбокомпрессор становится турбокомпрессором с открытой системой и позволяет выхлопным газам обходить турбину. Поскольку выхлопные газы закрываются вокруг колеса турбины, меньше энергии поглощается через турбину и передается компрессору, уменьшая давление впускного коллектора и скорости турбины.

![[10c00011.png]]

Контроллер обходного клапана турбины установлен на задней части впускного коллектора на стороне турбокомпрессора двигателя и управляется ECM. Контроллер обходного клапана турбины регулирует процент давления впускного коллектора, посылаемого в привод обходного клапана турбины. Два соленоида, похожие на клапаны отключения топливного насоса продукта CELECTTM, используются в сочетании с четырьмя отверстиями для регулирования этого процента.

![[10200062.png]]

Турбинный шунтирующий привод клапана установлен на турбокомпрессоре и состоит из канистра давления, диафрагмы и стержня. По мере изменения давления в канистре, как это диктуется регулятором обходного клапана турбины, стержень привода соответствующим образом регулирует обходной клапан турбины.

![[10900029.png]]

Вентиль обходного клапана турбины установлен внутри турбокомпрессора в корпусе турбины. По мере открытия клапана выхлопным газам разрешается обходить колесо турбины, снижая скорость турбины для регулирования давления впускного коллектора.

![[10900029.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Exhaust gas is recirculated through the engine to reduce the amount of Oxides of Nitrogen (NO x) emitted from the engine. The exhaust gas is cooled as it flows through the exhaust gas recirculation (EGR) cooler, and then is mixed with the compressed fresh air from the turbocharger before entering the intake manifold. EGR was introduced to reduce the amount of in-cylinder oxygen available for combustion while maintaining the same amount of flow through the engine. Exhaust gases present during the start of combustion are very stable and have a very slow reaction rate. They absorb heat during combustion, resulting in lower in-cylinder peak flame temperatures and therefore lower NO x emissions.
>
> The EGR mixer was designed to completely mix the EGR gas with the turbocharged air from the charge air cooler. Complete mixing is necessary to provide smooth operation and decreased emissions.
>
> The EGR valve is controlled by the electronic control module (ECM). ISM with CM870 engines control the EGR valve by a pulse width modulated signal sent by the ECM and operates between 0 percent and 100 percent open. When the EGR valve is open, exhaust gas flows from the hot side of the engine, through the EGR cooler, and into the EGR mixer.
>
> ISM with CM876 engines control the EGR valve through a J1939 datalink signal sent by the ECM and operates between 0 percent and 100 percent open. When the EGR valve is open, exhaust gas flows from the EGR cooler through the EGR connection tube, and into the EGR mixer.
>
> The ISM with CM876 EGR connection tube allows the flow of cooled exhaust gas from the EGR valve outlet at the rear of the engine to the EGR mixer before the intake manifold. This engine utilizes a two-piece EGR connection tube design which also includes the EGR venturi tube.
>
> The ISM CM870 and ISM CM875 EGR connection tube allows the flow of cooled exhaust gas from the EGR cooler outlet at the rear of the engine to the EGR mixer before the intake manifold. This engine utilizes a two-piece EGR connection tube which also includes the EGR venturi tube.
>
> The EGR venturi tube contains a flow orifice that is used to measure the amount of exhaust gas flow using an EGR differential pressure sensor and a high and reference differential pressure sensing tubes.
>
> The exhaust manifold for the ISM with CM876 engine was redesigned to include a metal seal within the slip joints in efforts to reduce leakage. The exhaust manifold also has a port near the number one exhaust port for the exhaust pressure sensor.
>
> The variable geometry turbocharger is required for several important engine operating conditions. It is used to facilitate EGR flow through the engine. [[35-010-999-tr — Air Intake System - Overview|Refer to Procedure 010-999 in Section F]] for further information regarding variable geometry turbocharger and EGR flow interactions.
>
> The variable geometry turbocharger is also used for engine braking. The variable geometry mechanism closes in order to increase exhaust manifold pressure. The increased exhaust pressure works against the pistons on the exhaust stroke retarding engine speed.
>
> The aftertreatment system is used to reduce particulate emissions and is composed of six main components:
>
> 1. Aftertreatment inlet
> 2. Aftertreatment diesel particulate filter differential pressure sensor
> 3. Aftertreatment diesel oxidation catalyst
> 4. Aftertreatment diesel particulate filter
> 5. Aftertreatment outlet
> 6. Aftertreatment exhaust gas temperature sensors.
>
> **Note · Примечание**
> In some applications, the aftertreatment diesel oxidation catalyst can be contained within the inlet section of the aftertreatment system.
>
> Passive regeneration occurs when the exhaust temperatures are naturally high enough to oxidize the soot collected in the aftertreatment diesel particulate filter faster than the soot is collected.
>
> Passive regeneration typically occurs when the temperature of the aftertreatment diesel particulate filter is above 316°C \[600°F\]. This occurs during highway driving or driving with heavy loads.
>
> Since passive regeneration occurs naturally, it is considered to be normal engine operation. No fuel is added to the exhaust stream during passive regeneration.
>
> Active regeneration occurs when the exhaust temperatures are **not** naturally high enough to oxidize the soot collected in the aftertreatment diesel particulate filter faster than it is collected.
>
> Active regeneration requires assistance from the engine in order to increase the exhaust temperature. This is typically done by injecting a small amount of diesel fuel into the exhaust stream (called aftertreatment injection) which is then oxidized by the aftertreatment diesel oxidation catalyst. The oxidation of this additional fuel creates the heat needed to regenerate the aftertreatment diesel particulate filter.
>
> For active regeneration to occur, the ECM **must** detect that the aftertreatment diesel particulate filter restriction has reached a specified limit. Once this limit is reached, the engine will alter its operation in order to create exhaust temperatures high enough to actively regenerate the aftertreatment diesel particulate filter.
>
> An active regeneration event typically consists of two parts: a warming up phase and a regenerating phase.
>
> The purpose of the warm up phase is to increase the exhaust temperatures to the point that aftertreatment injection can occur.
>
> Aftertreatment injection requires that temperatures in the aftertreatment system reach approximately 288°C \[550°F\]. At this temperature and above, the small quantities of fuel injected into the exhaust will properly oxidize across the aftertreatment diesel oxidation catalyst creating the additional heat required to actively regenerate the aftertreatment diesel particulate filter.
>
> Once the warm up phase is complete and the aftertreatment injection has begun, the active regeneration phase begins.
>
> During active regeneration, the engine ECM monitors the exhaust temperatures before and after the aftertreatment diesel particulate filter and maintains the temperatures in a range of approximately 427 to 649°C \[800 to 1200°F\]. The quantity of fuel used for aftertreatment injection will vary as the temperature is controlled within these limits.
>
> The temperatures achieved during active regeneration are typically higher than those achieved during passive regeneration. The conversion of soot to carbon dioxide occurs much faster as temperatures increase.
>
> A typical active regeneration event will take approximately 20 to 40 minutes to complete while the vehicle is operating. The vehicle operator may notice additional turbocharger noise during this time, along with an illuminated high exhaust temperature lamp, if equipped.
>
> The frequency at which an engine will require an active regeneration varies greatly from application to application. In general, vehicles with a low vehicle speed, such as urban vehicles, or a low-load duty cycle, will require more active regeneration events than a heavily loaded vehicle or a vehicle with a high speed duty cycle.
>
> The engine ECM also contains a time-based feature for active regenerations which is used to verify correct aftertreatment operation when the vehicle duty cycle is typically high enough that active regeneration events are **not** necessary.
>
> Under some operating conditions, such as low speed, low load, or stop and go duty cycles, the engine may **not** have enough opportunity to regenerate the aftertreatment diesel particulate filter during normal vehicle operation. When this occurs, the engine illuminates the aftertreatment diesel particulate filter lamp to inform the vehicle operator that assistance is required, typically in the form of a stationary (parked) regeneration.
>
> Stationary (parked) regeneration is a form of active regeneration that is initiated by the vehicle operator when the vehicle is **not** moving.
>
> The following procedure provides more information on Stationary (Parked) regeneration. [[101-014-013 — Aftertreatment Testing|Refer to Procedure 014-013 in Section 14.]]
>
> The vehicle manufacturer has the that option of installing two switches that control aftertreatment functions: the start switch and the permit switch.
>
> The start switch (known as the Diesel Particulate Filter Regeneration Start Switch in INSITE™ electronic service tool) is used to start a stationary (parked) regeneration. The vehicle manufacturer may also reference this switch as a stationary regeneration switch, start switch, or parked regeneration switch.
>
> The permit switch (known as the Diesel Particulate Filter Permit Switch in INSITE™ electronic service tool) is used to allow the vehicle operator to disable active regeneration, if necessary. The vehicle manufacturer may also reference this switch as an inhibit switch, stop switch, or disable switch.
>
> The following procedure describes the switch operation and troubleshooting steps. [[35-011-056 — Exhaust System Diagnostics|Refer to Procedure 011-056 in Section 11.]]
>
> Automotive with CM570
>
> The wastegated turbocharger is a Holset® model HX55. It is comprised of a turbocharger, wastegate actuator, and wastegate valve in the turbine housing. A wastegated turbocharger provides improved response at low engine speeds without sacrificing turbocharger durability at high speeds. This is accomplished by allowing exhaust gases to bypass the turbine wheel during certain modes of engine operation. During low rpm operation, the turbocharger operates as a closed-system turbocharger, where the gases' energy is transferred to the compressor wheel and used to compress intake air. During high rpm operation, however, the turbocharger becomes an open-system turbocharger and allows exhaust gas to bypass the turbine. Since exhaust gas is gated around the turbine wheel, less energy is absorbed through the turbine and transferred to the compressor, reducing intake manifold pressures and turbine speeds.
>
> The wastegate controller is mounted on the rear of the intake manifold on the turbocharger side of the engine and is controlled by the ECM. The wastegate controller regulates the percentage of the intake manifold pressure sent to the wastegate actuator. Two solenoids, similar to the fuel pump shutoff valves of the CELECT™ product, are used in conjunction with four orifices to regulate this percentage.
>
> The wastegate actuator is mounted on the turbocharger and consists of a pressure canister, diaphragm, and rod. As pressure changes in the canister, as dictated by the wastegate controller, the actuator rod adjusts the wastegate valve accordingly.
>
> The wastegate valve is mounted inside the turbocharger in the turbine housing. As the valve opens, exhaust gas is allowed to bypass the turbine wheel, lowering turbine speed to adjust intake manifold pressure.
