---
type: "Сервисный бюллетень"
doc: "4021927"
title_en: "On-Board Diagnostics (OBD) for Euro Certified Engines"
released: "2007-11-16"
modified: "2009-10-19"
engines:
  - "77804793"
  - "77804810"
families:
  - "15N"
  - "A8.5"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/4021927.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/4021927.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/15N"
  - "двигатель/A8.5"
  - "перевод/машинный"
---

# On-Board Diagnostics (OBD) for Euro Certified Engines

> [!abstract] Сервисный бюллетень · `4021927`
> **Двигатели:** [[77804793 — A8.5 CM2670 L153B CPL 6235|77804793]], [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N, A8.5
> **Даты:** выпущен 2007-11-16 · изменён 2009-10-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/4021927.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/4021927.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Диагностика бортовых систем (OBD) для сертифицированных двигателей Евро

### Назначение

В бюллетене службы содержится информация о бортовой диагностике (OBD) двигателей Cummins®, сертифицированных по уровням выбросов Евро 4, 4,5 и 5. Цель этого бюллетеня состоит в том, чтобы определить общие термины БД и объяснить правильные стратегии устранения неполадок и устранения кода неисправностей.

Что такое ОВД?

OBD является государственным стандартом, который требует от двигателей активного мониторинга и тестирования компонентов и систем, связанных с выбросами, для выявления неисправностей, которые отрицательно влияют на выбросы. Система БДД двигателя контролирует почти каждый компонент, который может повлиять на систему контроля выбросов. Если система БД обнаруживает неисправность, которая может привести к увеличению уровня выбросов выхлопных газов, система БД освещает лампу индикатора неисправности (MIL) на панели приборов транспортного средства, чтобы предупредить оператора о том, что двигатель нуждается в ремонте. Уровень требуемого мониторинга БД может варьироваться в зависимости от таких факторов, как общий рейтинг веса транспортного средства (GVWR), модельный год, уровень сертификации и применимые государственные правила.

Терминология BD

Для правильного устранения неполадок и диагностики систем двигателей, оснащенных системой Euro OBD, важно понимать следующие термины:

- Код ошибки (FC): Код, сообщенный и сохраненный двигателем ECM, который указывает на то, что определенная неисправность или ненормальное состояние были обнаружены. Различные режимы отказа вызывают сохранение различных кодов неисправностей, что обеспечивает направление для надлежащего устранения неполадок и ремонта. Коды ошибок можно прочитать, подключившись к ECM с помощью инструмента сканирования, такого как инструмент электронного обслуживания INSITETM.
- Неисправность индикатора лампы (MIL): Лампа, которая освещает и предупреждает оператора, когда код неисправности OBD становится «активным», что указывает на неисправность двигателя, которая может повлиять на выбросы.
- OBD монитор: Диагностический тест или серия измерительн, которые проводятся двигателем ECM и предназначены для определения рабочего состояния конкретного компонента или подсистемы, связанного с выбросами. Двигатели, оснащенные БД-устройствами, имеют несколько мониторов БД-систем, которые работают в определенных условиях эксплуатации. Эти мониторы тестируют свои соответствующие системы и хранят или сообщают о результатах соответственно.
- Постоянный монитор: Диагностика, которая работает непрерывно во время нормальной работы двигателя. Он записывает код неисправности и освещает MIL сразу после диагностических запусков и не проходит.
- Непрерывный монитор: Диагностика, которая выполняется только при определенных благоприятных условиях. Непрерывная диагностика может проводиться каждый раз, когда выполняются определенные условия эксплуатации или окружающей среды, или один раз за цикл привода.
- OBD 1 Trip Fault: Код неисправности, который настроен на «Актив» и освещает MIL после соответствующей диагностики кода неисправности, запускается и не проходит один раз во время цикла привода.
- OBD 2 Trip Fault: Код неисправности, который настроен на «Активный» и освещает MIL после соответствующей диагностики кода неисправности, запускается и не проходит в течение двух последовательных циклов привода.
- Цикл вождения: Конкретная серия этапов или набор условий, в которых транспортное средство должно эксплуатироваться, чтобы обеспечить возможность выполнения конкретной диагностики. Это может быть частью процесса, необходимого для очистки определенных кодов неисправностей БД. Условия цикла привода указаны в древе устранения неполадок для применимого кода неисправности.
- Цикл зажигания: Наиболее распространенный тип цикла привода, который начинается с запуска двигателя и заканчивается выключением двигателя.
- Цикл разогрева: Цикл привода, который включает в себя повышение температуры охлаждающей жидкости по меньшей мере на 22,3 ° C \[40 ° F \], когда температура охлаждающей жидкости проходит через 60° C \[140° F \]. Следующий цикл разминки начинается до тех пор, пока двигатель не будет выключен, не будет охлажден до температуры ниже 60°C[140°F] и не будет перезапущен.
- Холодный сок: Часть определенных циклов движения, в которых транспортное средство должно сидеть не менее 8 часов с выключенным двигателем. Это позволяет всем датчикам температуры выравниваться при температуре окружающей среды.
- Разряд: Действие, вызванное определенными кодами неисправностей, которые уменьшают доступную мощность двигателя. Это делается для защиты двигателя от повреждений и/или для инициирования служебного мероприятия. Некоторые из них происходят сразу, в то время как другие происходят через определенное количество времени после того, как ошибка стала «активной». После того, как ремонт будет сделан и неисправность станет «неактивной», двигатель больше не будет деградировать.
- Полное: OBD Monitor собрал достаточно информации для определения состояния системы.
- Неполное: OBD Monitor собрал достаточно информации для определения состояния своей системы. Статус завершения ошибки **не **должен учитываться при устранении неполадок и не является **состоянием кода ошибки. Он предоставляется в электронном сервисе INSITETM в качестве информации **только.
- В ожидании: Код ошибки OBD становится «В ожидании», когда диагностика ошибки поездки OBD 2 запущена и **не** прошла в одном цикле вождения. Код ошибки - "Активный", но ни одна тире-лампа не была освещена.
- Подтверждено: Код неисправности OBD становится «Подтвержденным», как только система OBD собрала достаточно информации, чтобы подтвердить, что существует неисправность, и код неисправности стал «Активным». Обратите внимание, что неисправность БД может оставаться «подтвержденной» даже после ремонта и срабатывания МИЛ. См. раздел Функциональность кода по умолчанию OBD для получения более подробной информации.
- Неразрешимый код ошибки: Историю кода ошибки можно **не** стереть из памяти ECM с помощью инструмента сканирования, такого как инструмент электронного обслуживания INSITETM. После того, как ремонт будет сделан и диагностика будет запущена, MIL будет работать, но неисправность останется «неактивной» и «подтвержденной». В зависимости от того, как настроен код неисправности, неисправность «Неактивный» удаляется из истории неисправностей после успешного завершения установленного количества циклов привода или после установленного количества времени. Эти настройки определяются регулирующим органом и программируются в двигатель ECM.

Не все коды неисправностей могут повлиять на выбросы. Поэтому двигатели, оснащенные OBD, могут иметь как коды неисправностей OBD, так и не-OBD. Как правило, не-OBD коды ошибок освещают либо лампу предупреждения об янтаре (AWL), либо красную стоп-лампу (RSL), которые являются традиционными лампами Cummins®. Неисправности БД всегда освещают MIL, а в некоторых случаях также освещаются AWL или RSL.

Устранение неисправностей OBD коды

Предпочтительная стратегия устранения неполадок кодов OBD аналогична традиционной Cummins Inc. Коды неисправностей: Устранение неполадок на основе Cummins Inc. Состояние неисправности, как показано на экране инструментов «Коды неисправностей» INSITETM. Экраны инструментов для электронных сервисов ”OBD Fault Codes” и ”OBD Monitors” INSITETM предназначены только для информации и должны использоваться только для устранения неполадок.

Во время процесса устранения неисправностей необходимо указать соответствующее дерево устранения неисправностей для каждого кода неисправности, чтобы завершить ремонт. Деревья для устранения неполадок можно найти в соответствующем руководстве по устранению неполадок и ремонту электронной системы управления. После ремонта дерево устранения неполадок предоставляет инструкции о том, как заставить диагностировать работу на цикле привода, чтобы проверить ремонт. Если ремонт был успешным, то Cummins Inc. Состояние кода неисправности (которое можно отслеживать на экране инструментов электронного сервиса INSITETM) станет «неактивным» после запуска и прохождения диагностики. Это должно быть сделано для каждого кода неисправности, присутствующего в ECM.

Заглушить MIL

Некоторые коды неисправностей требуют одного цикла привода для гашения MIL, а некоторые требуют трех циклов привода. Различия объясняются ниже:

One Drive Cycle MIL Off Fault Clearing (недоступная ссылка)

Все несъемные дефекты являются «отключением МИЛ при немедленных неисправностях», что означает, что МИЛ отключается сразу после диагностических прогонов и проходит один цикл привода. Поскольку «неактивный» дефект может

не

быть очищены с помощью электронного инструментария обслуживания INSITETM, ремонт производится на этом этапе для нестираемых неисправностей. Несъемные дефекты являются

только

«МиЛ от непосредственных ошибок».

Три цикла езды MIL Off Fault Clearing

Для остальных неисправностей БД коды неисправностей после диагностических прогонов и проходов остаются «неактивными», но MIL остается до тех пор, пока не будут завершены два дополнительных цикла привода, в которых диагностические пробеги и проходы. Когда один цикл привода завершен и код неисправности «Неактивен», ремонт был подтвержден, а код неисправности «Неактивный» может быть очищен с помощью инструментария электронного обслуживания INSITETM. Это гасит все тире лампы. Если код неактивной ошибки

не

Очистившись с помощью электронного инструментария INSITETM, MIL будет работать до тех пор, пока диагностика не пройдет два дополнительных цикла привода (всего три цикла привода).

Деревья устранения неполадок предоставляют важную информацию, такую как, является ли код неисправности неразрушимым, как установлен код неисправности, что необходимо сделать, чтобы запустить диагностику, и сколько циклов привода требуется, чтобы выключить MIL. Для большинства кодов неисправностей цикл привода может быть завершен путем запуска двигателя, позволяя ему простаивать в течение 1 минуты и отключать его. Однако некоторые коды неисправностей требуют, чтобы транспортное средство приводилось в движение или работало на динамометре шасси, чтобы диагностировать запуск и сделать код неисправности «Неактивным».

Функциональность кода ошибки OBD

Следующие иллюстрации показывают различные способы, которыми коды ошибок OBD настроены на «Активный» и включен MIL:

![[19901547.png]]

![[19901546.png]]

Следующие иллюстрации показывают различные способы очистки кодов ошибок OBD и выключения MIL:

![[19901545.png]]

![[19901548.png]]


> [!quote]- Original (English) · английский оригинал
> ## On-Board Diagnostics (OBD) for Euro Certified Engines
>
> ### Purpose
>
> This service bulletin contains information regarding on-board diagnostics (OBD) for Cummins® engines certified to Euro 4, 4.5, and 5 emissions levels. The purpose of this bulletin is to define common OBD terms and explain the proper troubleshooting and fault code clearing strategies.
>
> What is OBD?
>
> OBD is a government-mandated standard that requires engines to actively monitor and test emissions-related components and systems to detect malfunctions that adversely affect emissions. An engine's OBD system monitors nearly every component that can affect the emission control system. If the OBD system detects a malfunction that could cause an increase in exhaust emission levels, the OBD system illuminates the Malfunction Indicator Lamp (MIL) on the vehicle instrument panel to alert the operator that the engine is in need of repair. The level of OBD monitoring required can vary depending on factors such as Gross Vehicle Weight Rating (GVWR), model year, certification level, and applicable government regulations.
>
> OBD Terminology
>
> To properly troubleshoot and diagnose Euro OBD-equipped engine systems, it is important to understand the following terms:
>
> - Fault Code (FC): A code reported and stored by the engine ECM which indicates that a particular malfunction or abnormal condition has been detected. Different failure modes cause different fault codes to be stored, which provides direction for the appropriate troubleshooting and repair. Fault codes can be read by connecting to the ECM with a scan tool, such as the INSITE™ electronic service tool.
> - Malfunction Indicator Lamp (MIL): A dash lamp that illuminates and alerts the operator when an OBD fault code becomes ”Active”, indicating an engine malfunction that could impact emissions.
> - OBD Monitor: A diagnostic test or series of tests which are run by the engine ECM and are designed to determine the operational status of a specific emissions-related component or subsystem. OBD-equipped engines have multiple OBD monitors that run under certain operating conditions. These monitors test their respective systems and store or report the results accordingly.
> - Continuous Monitor: A diagnostic that runs continuously during normal engine operation. It records a fault code and illuminates the MIL immediately after the diagnostic runs and does **not** pass.
> - Non-Continuous Monitor: A diagnostic that runs **only** under certain enabling conditions. A non-continuous diagnostic may run every time certain operating or environmental conditions are met, or once per drive cycle.
> - OBD 1 Trip Fault: A fault code that is set to ”Active” and illuminates the MIL after the corresponding diagnostic for the fault code runs and does **not** pass once during a drive cycle.
> - OBD 2 Trip Fault: A fault code that is set to ”Active” and illuminates the MIL after the corresponding diagnostic for the fault code runs and does **not** pass during two consecutive drive cycles.
> - Drive Cycle: A specific series of steps or set of conditions that a vehicle **must** be operated under to enable a specific diagnostic to run. This can be part of the process required to clear certain OBD fault codes. Drive cycle conditions are stated in the troubleshooting tree for the applicable fault code.
> - Ignition Cycle: The most common type of drive cycle, which begins with engine start and ends with engine shutdown.
> - Warm-up Cycle: A drive cycle that includes an increase of at least 22.3°C \[40°F\] coolant temperature where the coolant temperature passes through 60°C \[140°F\]. The next warm-up cycle does **not** begin until the engine has been shut off, allowed to cool down to below 60°C \[140°F\], and is restarted.
> - Cold Soak: A portion of certain drive cycles in which a vehicle **must** sit for a minimum of 8 hours with the engine off. This allows all temperature sensors to equalize at ambient temperature.
> - Derate: An action caused by certain fault codes which decreases available engine power. This is done to protect the engine from damage and/or help initiate a service event. Some derates occur immediately, while others occur after a certain amount of time since a fault became ”Active”. Once the repair is made and the fault goes ”Inactive”, the engine will no longer be derated.
> - Complete: The OBD Monitor has collected enough information to determine the health of its respective system.
> - Not Complete: The OBD Monitor has **not** collected enough information to determine the health of its respective system. The fault completion status does **not** need to be considered during troubleshooting, and is **not** a fault code state. It is provided in the INSITE™ electronic service tool as information **only**.
> - Pending: An OBD fault code becomes ”Pending” once a diagnostic for an OBD 2 trip fault has run and **not** passed on one drive cycle. Fault code is ”Active”, but no dash lamps have been illuminated.
> - Confirmed: An OBD fault code becomes ”Confirmed” once the OBD system has gathered enough information to confirm that a malfunction exists and a fault code has become ”Active”. Note that an OBD fault can remain ”Confirmed” even after the repair has been made and the MIL goes off. See the OBD Fault Code Functionality section of this bulletin for further details.
> - Non-Erasable Fault Code: Fault code history can **not** be erased from the ECM memory with a scan tool such as the INSITE™ electronic service tool. Once the repair is made and the diagnostic has run, the MIL will go off, but the fault will remain ”Inactive” and ”Confirmed”. Depending on how the fault code is configured, the ”Inactive” fault is deleted from the fault history after the successful completion of a set number of drive cycles, or after a set amount of time. These settings are defined by the regulatory agency and are programmed into the engine ECM.
>
> Not all fault codes have the potential to impact emissions. Therefore, OBD-equipped engines can have both OBD and non-OBD fault codes. Typically, non-OBD fault codes illuminate either the Amber Warning Lamp (AWL) or Red Stop Lamp (RSL), which are the traditional Cummins® dash lamps. OBD faults always illuminate the MIL, and in some cases the AWL or RSL are illuminated as well.
>
> Troubleshooting OBD Fault Codes
>
> The preferred strategy for troubleshooting OBD fault codes is the same as for traditional Cummins Inc. fault codes: troubleshooting based on the Cummins Inc. fault status, as displayed in the ”Fault Codes” INSITE™ electronic service tool screen. The ”OBD Fault Codes” and ”OBD Monitors” INSITE™ electronic service tool screens are for information **only** and should **only** be used for advanced troubleshooting.
>
> During the troubleshooting process, the appropriate fault code troubleshooting tree for each fault code **must** be referred to in order to complete the repair. The troubleshooting trees can be found in the applicable Electronic Control System Troubleshooting and Repair Manual. Once a repair is made, the troubleshooting tree provides instructions on how to get the diagnostic to run on a drive cycle in order to validate the repair. If the repair was successful, the Cummins Inc. fault code status (which can be monitored in the ”Fault Codes” INSITE™ electronic service tool screen) will become ”Inactive” once the diagnostic runs and passes. This should be done for each fault code present in the ECM.
>
> Extinguishing the MIL
>
> Some fault codes require one drive cycle to extinguish the MIL, and some require three drive cycles. The differences are explained below:
>
> One Drive Cycle MIL Off Fault Clearing
>
> All non-erasable faults are ”MIL off immediate faults”, meaning the MIL will turn off immediately after the diagnostic runs and passes on one drive cycle. Since the ”Inactive” fault can
>
> not
>
> be cleared with the INSITE™ electronic service tool, the repair is done at this point for non-erasable faults. Non-erasable faults are the
>
> only
>
> ”MIL off immediate faults”.
>
> Three Drive Cycle MIL Off Fault Clearing
>
> For the remainder of the OBD faults, the fault codes go ”Inactive” after the diagnostic runs and passes once, but the MIL stays on until two additional drive cycles are completed in which the diagnostic runs and passes. When one drive cycle has been completed and the fault code is ”Inactive”, the repair has been validated, and the ”Inactive” fault code can be cleared with the INSITE™ electronic service tool. This extinguishes all dash lamps. If the ”Inactive” fault code is
>
> not
>
> cleared with the INSITE™ electronic service tool, the MIL will stay on until the diagnostic has run and passed on two additional drive cycles (three drive cycles total).
>
> The troubleshooting trees provide important information, such as whether a fault code is non-erasable, how the fault code is set, what must be done to get the diagnostic to run, and how many drive cycles are required to turn the MIL off. For most fault codes, a drive cycle can be completed by starting the engine, letting it idle for 1 minute, and shutting it down. However, some fault codes require that the vehicle be driven or operated on a chassis dynamometer in order to get the diagnostic to run and make the fault code go ”Inactive”.
>
> OBD Fault Code Functionality
>
> The following illustrations show the different ways that OBD fault codes are set to ”Active” and the MIL is turned on:
>
> The following illustrations show the different ways that OBD fault codes are cleared and how the MIL is turned off:
