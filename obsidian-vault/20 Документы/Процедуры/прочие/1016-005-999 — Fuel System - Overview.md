---
aliases:
  - "Топливная система — обзор"
type: "Процедура"
doc: "1016-005-999"
title_en: "Fuel System - Overview"
title_ru: "Топливная система — обзор"
modified: "2022-12-14"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-005-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-005-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
  - "перевод/машинный"
---

# Fuel System - Overview
**Топливная система — обзор**

> [!abstract] Процедура · `1016-005-999`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2022-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-005-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-005-999.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!danger] ОПАСНО
> Природный газ взрывоопасен и воспламеняется. Всегда следите за поддержанием адекватной вентиляции в рабочем помещении. Храните все сигареты, пламя, пилотные огни, дуговое оборудование и выключатели из рабочей зоны и областей с общей вентиляцией, чтобы уменьшить вероятность серьезных травм или смерти при работе на системе природного газа.

#### Система сжиженного природного газа (СПГ)

- Система СПГ состоит из компонентов, включая резервуар СПГ (предоставленный производителем оригинального оборудования (OEM)), регулятор давления топлива (интегрированный с клапанами отключения топлива), фильтры низкого давления, клапан учета топлива и т. Д.[[1016-200-001 — Flow Diagram, Fuel System|См. процедуру 200-001 в разделе F.]]
- Из резервуара СПГ поток газа направляется через регуляторы высокого давления, которые обычно снижают давление от резервуаров для хранения до менее чем 10 бар [145 psi].

#### Система сжатого природного газа (CNG)

- Система CNG состоит из компонентов, включая резервуар CNG (предоставленный OEM), два регулятора давления топлива (интегрированный с клапанами отключения топлива), фильтры низкого давления, клапан учета топлива и так далее.[[1016-200-001 — Flow Diagram, Fuel System|См. процедуру 200-001 в разделе F.]]
- Из резервуара с СПГ поток газа направляется через регуляторы высокого давления (1), которые обычно уменьшают давление из резервуаров для хранения до менее чем 10 бар \[145 psi \]. Поток газа для двух регуляторов соединен параллельно.
- Быстрое расширение газа через регуляторы поглощает тепло и может вызвать обледенение. Чтобы предотвратить обледенение, регуляторы высокого давления могут нагреваться с помощью охлаждающей жидкости двигателя. Порты (2) охлаждающей жидкости в двух регуляторах соединены последовательно.

![[05s00078.png]]

- Клапан отключения топлива (интегрированный с регуляторами давления топлива) закрыт в немощном положении.
- В случае утечки топлива или неисправности компонентов во время работы транспортного средства клапан обесточен для изоляции утечки или неисправности.

![[05s00026.png]]

- Фильтр низкого давления представляет собой коалесцирующий фильтр, который будет захватывать масляные загрязнения и влагу, обычно встречающуюся в топливе.

![[05n00045.png]]

- Клапан учета топлива представляет собой коллектор, содержащий восемь топливных форсунок и датчик давления и температуры впускного топлива. Каждый форсунка управляется отдельно сигналами модуляции ширины импульса.

![[05s00027.png]]

#### Топливная система потока газа

- СПГ, поставляемый из танка OEM LNG, пропускается через регулятор давления топлива (интегрированный с клапанами отключения топлива) и топливный фильтр, а затем в клапан учета топлива.
- КПГ, поставляемый из резервуара OEM CNG, пропускается через регуляторы давления топлива (интегрированные с клапанами отключения топлива) и топливный фильтр, а затем в клапан учета топлива.
- Из корпуса клапана учета топлива газ проходит в корпус топливного смесителя воздуха, где он вводится в поток воздуха заряда.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **WARNING · Опасно**
> Natural gas is explosive and flammable. Always be sure to maintain adequate ventilation in the work area. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas with shared ventilation to reduce the possibility of severe personal injury or death when working on a natural gas system.
>
> #### Vehicle Liquefied Natural Gas (LNG) System
>
> - LNG system consists of components including LNG tank (provided by Original Equipment Manufacturer (OEM)), fuel pressure regulator (integrated with fuel shutoff valves), low-pressure filters, fuel metering valve, and so forth. [[1016-200-001 — Flow Diagram, Fuel System|Refer to Procedure 200-001 in Section F.]]
> - From LNG tank, the gas flow is directed through the high-pressure regulators, which will typically reduce the pressure from the storage tanks to less than 10 bar \[ 145 psi \].
>
> #### Vehicle Compressed Natural Gas (CNG) System
>
> - CNG system consists of components including CNG tank (provided by OEM), two fuel pressure regulators (integrated with fuel shutoff valves), low-pressure filters, fuel metering valve, and so forth. [[1016-200-001 — Flow Diagram, Fuel System|Refer to Procedure 200-001 in Section F.]]
> - From CNG tank, the gas flow is directed through the high-pressure regulators (1), which will typically reduce the pressure from the storage tanks to less than 10 bar \[ 145 psi \]. The gas flow for the two regulators is connected in parallel.
> - The rapid expansion of the gas through the regulators absorbs heat and can cause icing. To prevent icing, the high-pressure regulators can be heated with engine coolant. The coolant ports (2) in the two regulators are connected in series.
>
> - The fuel shutoff valve (integrated with fuel pressure regulators) is closed in the un-powered position.
> - In the event of a fuel leakage or component malfunction during vehicle operation, the valve is de-energized to isolate the leak or malfunction.
>
> - Low-pressure filter is a coalescent-type filter that will capture oil contaminations and moisture typically found in the fuel.
>
> - Fuel metering valve is a manifold containing eight injectors and an inlet fuel pressure and temperature sensor. Every injector is controlled separately by pulse width modulation signals.
>
> #### Fuel System Gas Flow
>
> - The LNG, supplied from OEM LNG tank, is plumbed through the fuel pressure regulator (integrated with fuel shutoff valves) and fuel filter, then into the fuel metering valve.
> - The CNG, supplied from OEM CNG tank, is plumbed through the fuel pressure regulators (integrated with fuel shutoff valves) and fuel filter, then into the fuel metering valve.
> - From the fuel metering valve housing, the gas passes into the air fuel mixer housing, where it is introduced into the charge air flow.
