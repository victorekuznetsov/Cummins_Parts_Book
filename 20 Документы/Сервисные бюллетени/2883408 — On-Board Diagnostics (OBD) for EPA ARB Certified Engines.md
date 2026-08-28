---
type: "Сервисный бюллетень"
doc: "2883408"
title_en: "On-Board Diagnostics (OBD) for EPA/ARB Certified Engines"
released: "2013-01-21"
modified: "2013-01-29"
engines:
  - "77804793"
  - "77804810"
families:
  - "15N"
  - "A8.5"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/2883408.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/2883408.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/15N"
  - "двигатель/A8.5"
  - "перевод/машинный"
---

# On-Board Diagnostics (OBD) for EPA/ARB Certified Engines

> [!abstract] Сервисный бюллетень · `2883408`
> **Двигатели:** [[77804793 — A8.5 CM2670 L153B CPL 6235|77804793]], [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N, A8.5
> **Даты:** выпущен 2013-01-21 · изменён 2013-01-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/2883408.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/2883408.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Диагностика бортовых систем (OBD) для сертифицированных двигателей EPA/ARB

Данный бюллетень содержит информацию о диагностике тяжелых грузовых автомобилей (HD-OBD) для двигателей Cummins®. Heavy Duty On-Board Diagnostics (HD-OBD) - это требование сертификации Агентства по охране окружающей среды / Совета по воздушным ресурсам (EPA / ARB) для двигателей, оснащенных в транспортных средствах с валовым весом транспортного средства (GVWR) \> 14 000 фунтов. Цель этого бюллетеня - определить общие термины OBD и объяснить правильные стратегии устранения неполадок и устранения неисправностей.Этот бюллетень предназначен для двигателей Cummins®, сертифицированных HD-OBD. Настоящий бюллетень не применяется к автомобилям/двигателям, сертифицированным по стандарту OBDII или E-OBD.

Что такое ОВД?

OBD является государственным стандартом, который требует от двигателей активного мониторинга и тестирования компонентов и систем, связанных с выбросами, для выявления неисправностей, которые отрицательно влияют на выбросы. Система БДД двигателя контролирует почти каждый компонент, который может повлиять на систему контроля выбросов. Если система БД обнаруживает неисправность, которая может привести к увеличению уровня выбросов выхлопных газов, система БД освещает индикатор неисправности (MIL) на приборной панели транспортного средства, чтобы предупредить оператора о том, что двигатель нуждается в ремонте. Уровень требуемого мониторинга БД может варьироваться в зависимости от таких факторов, как общий вес автомобиля (GVWR), модельный год, уровень сертификации и применимые государственные правила.

Терминология BD

Для правильного устранения неполадок и диагностики систем двигателей, оснащенных HD-OBD, важно понимать следующие термины:

- Код ошибки (FC): Код, сообщенный и сохраненный модулем управления двигателем (ECM), который указывает, что определенная неисправность или ненормальное состояние были обнаружены. Различные режимы отказа вызывают сохранение различных кодов неисправностей, что обеспечивает направление для надлежащего устранения неполадок и ремонта. Коды ошибок можно прочитать, подключившись к ECM с помощью инструмента сканирования, такого как инструмент электронного обслуживания INSITETM. Коды ошибок могут быть упомянуты в терминологии БД как диагностический код неисправности (DTC).
- Неисправность индикатора лампы (MIL): Лампа, которая освещает и предупреждает оператора, когда код неисправности OBD становится «активным», что указывает на неисправность двигателя, которая может повлиять на выбросы.
- Диагностика БД: Испытание или серия испытаний, которые проводятся двигателем ECM и предназначены для определения рабочего состояния конкретного компонента или подсистемы, связанного с выбросами. Двигатели, оснащенные БД, имеют несколько диагностических БД, которые работают в определенных условиях эксплуатации. Эти диагностические тесты проверяют соответствующие системы и хранят или сообщают о результатах соответственно. Иногда в терминологии БДО его называют «монитором».
- Непрерывная диагностика: Диагностика, которая работает непрерывно во время нормальной работы двигателя. Он записывает код неисправности и освещает MIL сразу после диагностических запусков и не проходит.
- Непрерывная диагностика: Диагностика, которая выполняется только при определенных благоприятных условиях. Непрерывная диагностика может проводиться каждый раз, когда выполняются определенные условия эксплуатации или окружающей среды, или один раз за поездку.
- Путешествие: Также известен как «цикл вождения». Конкретная серия этапов или набор условий, в которых транспортное средство должно эксплуатироваться, чтобы обеспечить возможность выполнения конкретной диагностики. Это может быть частью процесса, необходимого для очистки определенных кодов неисправностей БД. Условия поездки указаны в дереве устранения неполадок для применимого кода неисправности.
- Виноваты в 1-ти пробах: Код неисправности, который настроен на «Актив» и освещает MIL после соответствующей диагностики кода неисправности, запускается и не проходит один раз за поездку.
- Многостраничный дефект OBD: Код неисправности, который настроен на «Активный» и освещает MIL после соответствующей диагностики кода неисправности, запускается и не проходит во время нескольких последовательных поездок. Например, неисправность OBD 2-Trip будет освещать MIL после соответствующих диагностических прогонов и не проходит в течение двух последовательных поездок.
- Холодный сок: Часть определенных циклов движения, в которых транспортное средство **должно** сидеть в течение минимального количества времени (от 8 до 10 часов) с выключенным двигателем. Это позволяет всем датчикам температуры выравниваться при температуре окружающей среды.
- Разряд: Действие, вызванное определенными кодами неисправностей, которое уменьшает доступную мощность двигателя. Это делается для защиты двигателя от повреждений и/или для инициирования служебного мероприятия. Некоторые из них происходят сразу, в то время как другие происходят через определенное количество времени после того, как ошибка стала «активной». После того, как ремонт будет сделан и неисправность станет «неактивной», двигатель больше не будет деградировать.

лампы

Не все коды неисправностей могут повлиять на выбросы. Поэтому двигатели, оснащенные HD-OBD, могут иметь как коды неисправностей OBD, так и не-OBD. Как правило, не-OBD коды неисправностей освещают либо янтарную предупредительную лампу (AWL), либо красную стоп-сигнал (RSL), которые являются традиционными Cummins Inc. тире лампы. Неисправности БД всегда освещают MIL, а в некоторых случаях также освещаются AWL или RSL. См. руководство по обслуживанию производителя оригинального оборудования (OEM) для конкретных деталей о каждой приборной лампе.

Неисправность индикатора лампы

Неисправность индикаторной лампы янтарного (желтого) цвета и является изображением двигателя.

![[11c00253.png]]

Янтарная предупреждающая лампа

AWL имеет янтарный (желтый) цвет и может быть изображением двигателя с гаечным ключом или текстом: «Проверить» или «Проверить двигатель». AWL используется для указания на то, что код неисправности OBD активен или существует условие обслуживания.

![[19c01777.png]]

![[19c01778.png]]

Красная лампа стоп

RSL имеет красный цвет и может быть либо изображением двигателя с восклицательной точкой, контуром знака STOP с двигателем, либо текстом «Стоп» или «Стоп двигатель». RSL используется для указания кода неисправности защиты двигателя или состояния защиты двигателя.

![[11c00254.png]]

![[19c01780.png]]

Устранение неисправностей OBD коды

Предпочтительная стратегия устранения неисправностей кодов OBD такая же, как и для традиционных кодов неисправностей Cummins®: Устранение неполадок на основе состояния неисправности Cummins®, как показано на экране инструментов электронного сервиса INSITETM «Коды неисправностей». Экраны инструментов для электронных сервисов INSITETM «Коды ошибок OBD» и «Мониторы OBD» не используются на двигателях, сертифицированных по стандарту EPA 2010 или EPA 2013 OBD.

Во время процесса устранения неисправностей необходимо указать соответствующее дерево устранения неисправностей для каждого кода неисправности**, чтобы завершить ремонт. Дерево устранения неполадок можно найти в соответствующем руководстве по устранению неполадок кода ошибки. **Не все коды ошибок требуют замены деталей для завершения ремонта. Следуйте за деревом устранения неполадок тщательно и **только **заменяйте поврежденные части при получении инструкций. После ремонта дерево устранения неполадок дает инструкции о том, как получить диагностику для завершения цикла или поездки, чтобы проверить ремонт. Если ремонт был успешным, статус кода неисправности Cummins® (который можно отслеживать в экране электронного сервиса INSITETM «Коды ошибок») станет «Неактивным» после запуска и прохождения диагностики. Процесс устранения неполадок должен быть выполнен для каждого кода неисправности, присутствующего в ECM.

Заглушить MIL

Коды неисправностей OBD требуют трех циклов привода или поездок для тушения MIL. Коды неисправностей становятся «неактивными» после диагностических прогонов и проходят один раз, но MIL остается до тех пор, пока не будут завершены два дополнительных цикла или поездки, в которых проходит диагностика. Когда один цикл привода завершен и код неисправности «Неактивен», ремонт был подтвержден, а код неисправности «Неактивный» может быть очищен с помощью опции «Сбросить все ошибки» в электронном сервисе INSITETM. Это гасит соответствующие тире лампы. Если код неактивного отказа **не** очищен с помощью опции «Сбросить все ошибки» электронного сервиса INSITETM, MIL будет оставаться в рабочем состоянии до тех пор, пока диагностика не пройдет два дополнительных цикла привода (всего три цикла привода).

Деревья устранения неполадок предоставляют важную информацию, такую как, как установлен код ошибки, что **необходимо **сделать, чтобы запустить диагностику, и сколько циклов привода требуется, чтобы выключить MIL. Для многих кодов неисправностей цикл привода может быть завершен путем запуска двигателя, позволяя ему простаивать в течение 1 минуты и отключать его. Однако некоторые коды неисправностей могут потребовать, чтобы транспортное средство приводилось в движение, работало на динамометре шасси или было вынуждено выполнять стационарную регенерацию, чтобы диагностировать и сделать код неисправности «Неактивным». См. раздел «Условия для устранения кода неисправности» кода неисправности для определения соответствующих условий эксплуатации для проверки ремонта.

Функциональность кода ошибки OBD

![[19c01781.png]]

На иллюстрации показаны различные способы настройки кодов ошибок OBD для «Active» и включения MIL:

![[19c01782.png]]

На иллюстрации показаны различные способы настройки кодов ошибок OBD для «Active» и включения MIL:

![[19c01784.png]]

На иллюстрации показаны различные способы очистки кодов ошибок OBD и выключения MIL:

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## On-Board Diagnostics (OBD) for EPA/ARB Certified Engines
>
> This service bulletin contains information regarding Heavy Duty On-Board Diagnostics (HD-OBD) for Cummins® engines. Heavy Duty On-Board Diagnostics (HD-OBD) is an Environmental Protection Agency / Air Resources Board (EPA/ARB) certification requirement for engines equipped in vehicles with gross vehicle weight rating (GVWR) \> 14,000 lb. The purpose of this bulletin is to define common OBD terms and explain the proper troubleshooting and fault code clearing strategies.This service bulletin is specific to HD-OBD certified Cummins® engines. This bulletin does **not** apply to OBDII or E-OBD certified vehicles/engines.
>
> What is OBD?
>
> OBD is a government-mandated standard that requires engines to actively monitor and test emissions-related components and systems to detect malfunctions that adversely affect emissions. An engine's OBD system monitors nearly every component that can affect the emission control system. If the OBD system detects a malfunction that could cause an increase in exhaust emission levels, the OBD system illuminates the malfunction indicator lamp (MIL) on the vehicle instrument panel to alert the operator that the engine is in need of repair. The level of OBD monitoring required can vary, depending on factors such as gross vehicle weight rating (GVWR), model year, certification level, and applicable government regulations.
>
> OBD Terminology
>
> To properly troubleshoot and diagnose HD-OBD equipped engine systems, it is important to understand the following terms:
>
> - Fault Code (FC): A code reported and stored by the engine control module (ECM) which indicates that a particular malfunction or abnormal condition has been detected. Different failure modes cause different fault codes to be stored, which provides direction for the appropriate troubleshooting and repair. Fault codes can be read by connecting to the ECM with a scan tool, such as INSITE™ electronic service tool. Fault codes can be referred to within OBD terminology as a diagnostic trouble code (DTC).
> - Malfunction Indicator Lamp (MIL): A dash lamp that illuminates and alerts the operator when an OBD fault code becomes ”Active”, indicating an engine malfunction that could impact emissions.
> - OBD Diagnostic: A test or series of tests which are run by the engine ECM and are designed to determine the operational status of a specific emissions-related component or subsystem. OBD-equipped engines have multiple OBD diagnostics that run under certain operating conditions. These diagnostics test their respective systems and store or report the results accordingly. It is sometimes referred to within OBD terminology as a “monitor”.
> - Continuous Diagnostic: A diagnostic that runs continuously during normal engine operation. It records a fault code and illuminates the MIL immediately after the diagnostic runs and does **not** pass.
> - Non-Continuous Diagnostic: A diagnostic that runs **only** under certain enabling conditions. A non-continuous diagnostic may run every time certain operating or environmental conditions are met, or once per trip.
> - Trip: Also known as a “drive cycle”. A specific series of steps or set of conditions that a vehicle **must** be operated under to enable a specific diagnostic to run. This can be part of the process required to clear certain OBD fault codes. Trip conditions are stated in the troubleshooting tree for the applicable fault code.
> - OBD 1-Trip Fault: A fault code that is set to ”Active” and illuminates the MIL after the corresponding diagnostic for the fault code runs and does **not** pass once per trip.
> - OBD Multi-Trip Fault: A fault code that is set to ”Active” and illuminates the MIL after the corresponding diagnostic for the fault code runs and does **not** pass during multiple consecutive trips. For example, an OBD 2-Trip fault will illuminate the MIL after the corresponding diagnostic runs and does **not** pass during two consecutive trips.
> - Cold Soak: A portion of certain drive cycles in which a vehicle **must** sit for a minimum amount of time (8 to 10 hours) with the engine OFF. This allows all temperature sensors to equalize at ambient temperature.
> - Derate: An action, caused by certain fault codes, that decreases available engine power. This is done to protect the engine from damage and/or help initiate a service event. Some derates occur immediately, while others occur after a certain amount of time since a fault became ”Active”. Once the repair is made and the fault goes ”Inactive”, the engine will no longer be derated.
>
> Lamps
>
> Not all fault codes have the potential to impact emissions. Therefore, HD-OBD equipped engines can have both OBD and non-OBD fault codes. Typically, non-OBD fault codes illuminate either the amber warning lamp (AWL) or red stop lamp (RSL), which are the traditional Cummins Inc. dash lamps. OBD faults always illuminate the MIL, and in some cases the AWL or RSL are illuminated as well. Refer to the original equipment manufacturer (OEM) service manual for specific details about each dash lamp.
>
> Malfunction Indicator Lamp
>
> The malfunction indicator lamp is amber (yellow) in color and is the image of an engine.
>
> Amber Warning Lamp
>
> The AWL is amber (yellow) in color and can either be the image of an engine featuring a wrench or can be the text: “Check” or “Check Engine”. The AWL is used to indicate a non-OBD fault code is active or a maintenance condition exists.
>
> Red Stop Lamp
>
> The RSL is red in color and can either be the image of an engine featuring an exclamation point, the outline of a STOP sign featuring the engine, or the text “Stop” or “Stop Engine”. The RSL is used to indicate an engine protection fault code or engine protection condition exists.
>
> Troubleshooting OBD Fault Codes
>
> The preferred strategy for troubleshooting OBD fault codes is the same as for traditional Cummins® fault codes: troubleshooting based on the Cummins® fault status, as displayed in the ”Fault Codes” INSITE™ electronic service tool screen. The ”OBD Fault Codes” and ”OBD Monitors” INSITE™ electronic service tool screens are **not** used on EPA 2010 or EPA 2013 OBD certified engines.
>
> During the troubleshooting process, the appropriate fault code troubleshooting tree for each fault code **must** be referred to in order to complete the repair. The troubleshooting trees can be found in the applicable Fault Code Troubleshooting Manual. **Not all** fault codes require the replacement of parts to complete the repair. Follow the troubleshooting tree carefully and **only** replace damaged parts when instructed. Once a repair is made, the troubleshooting tree provides instructions on how to get the diagnostic to complete a drive cycle or trip in order to validate the repair. If the repair was successful, the Cummins® fault code status (which can be monitored in the INSITE™ electronic service tool “Fault Codes” screen) will become ”Inactive” once the diagnostic runs and passes. The troubleshooting process should be done for each fault code present in the ECM.
>
> Extinguishing the MIL
>
> OBD fault codes require three drive cycles or trips to extinguish the MIL. The fault codes go “Inactive” after the diagnostic runs and passes once, but the MIL stays on until two additional drive cycles or trips are completed in which the diagnostic runs and passes. When one drive cycle has been completed and the fault code is “Inactive”, the repair has been validated, and the “Inactive” fault code can be cleared with INSITE™ electronic service tool “Reset All Faults” option. This extinguishes the appropriate dash lamps. If the “Inactive” fault code is **not** cleared with INSITE™ electronic service tool “Reset All Faults” option, the MIL will stay on until the diagnostic has run and passed on two additional drive cycles (three drive cycles total).
>
> The troubleshooting trees provide important information, such as how the fault code is set, what **must** be done to get the diagnostic to run, and how many drive cycles are required to turn the MIL off. For many fault codes, a drive cycle can be completed by starting the engine, letting it idle for 1 minute, and shutting it down. However, some fault codes may require that the vehicle be driven, operated on a chassis dynamometer, or forced to perform a stationary regeneration in order to get the diagnostic to run and make the fault code go “Inactive”. Reference the “Conditions for Clearing the Fault Code“ section of the fault code troubleshooting in order to determine the appropriate operating conditions to verify the repair.
>
> OBD Fault Code Functionality
>
> The illustration shows the different ways that OBD fault codes are set to ”Active” and the MIL is turned on:
>
> The illustration shows the different ways that OBD fault codes are set to ”Active” and the MIL is turned on:
>
> The illustration shows the different ways that OBD fault codes are cleared and how the MIL is turned off:
>
> ### Document History
