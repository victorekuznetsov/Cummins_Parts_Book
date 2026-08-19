---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "60-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `60-101-007`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section F — Familiarization
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-101-007.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система управления приводом генератора представляет собой электронную систему управления, которая состоит из трех ECM.

- ECM 1 и ECM 3 являются моделями CM552. CM552 контролирует и контролирует заправку.
- ECM 2 — это модель CM850. Он контролирует и контролирует все другие функции двигателя.

ECM имеют некоторые функции мониторинга, которые рассматриваются в разделе TF.

![[19a00825.png]]

### Диагностические коды ошибок

Электронная система управления QST30 может регистрировать определенные условия неисправности. Эти условия могут быть отображены путем подключения электронного инструментария обслуживания.

Существует два порта шины данных CAN для связи с ECM.

Порты шины данных CAN расположены на левой стороне двигателя. Передний порт шины данных CAN предназначен для связи с ECM CM552.

Задний порт предназначен для связи с CM850 ECM и должен быть подключен первым.

![[19a00837.png]]

Существует два типа кодов неисправностей:

- Коды неисправностей в электронной топливной системе двигателя
- Коды неисправностей системы защиты двигателя

Все коды ошибок, записанные будут либо активными (код ошибки активен на двигателе), либо неактивными (код ошибки был активен в одно время, но ** не ** в этот момент).

Активные и неактивные коды неисправностей можно просматривать с помощью инструментария электронного обслуживания INSITETM.

![[19800902.png]]

Система защиты двигателя записывает отдельные коды неисправностей, когда обнаруживается состояние вне зоны действия любого из датчиков в системе защиты двигателя.

Ниже приведены коды неисправностей системы защиты двигателя вне зоны действия:

- Температура охлаждающей жидкости
- Уровень охлаждения (необязательно)
- Давление масла.

![[19e00093.png]]

### Код ошибки Snapshot Data

Диагностический код неисправности записывается в ECM.

Данные ввода и вывода ECM регистрируются со всех датчиков и коммутаторов.

Данные снимка позволяют просматривать отношения между входами и выходами ECM во время устранения неполадок.

![[19e00093.png]]

### Система защиты двигателя

Система защиты двигателя контролирует критические температуры двигателя, уровень жидкости, положение переключателей и давление. Диагностические коды неисправностей регистрируются, когда происходит превышение или превышение нормального диапазона работы.

Если существует вне диапазона, может быть инициировано действие разрушителя двигателя. Если вне диапазона состояния существует, активный код неисправности будет генерироваться в ECM.

Система защиты двигателя мониторы:

- Температура охлаждающей жидкости
- Уровень охлаждения (необязательно)
- температура коллектора
- Давление масла.

Система защиты двигателя мониторы для:

- Высокая температура охлаждающей жидкости
- Низкий уровень охлаждающей жидкости (необязательно)
- Высокая температура коллектора впуска
- От низкого до очень низкого давления масла.

Система защиты двигателя может иметь две выбираемые функции:

- Защита двигателя позволяет - мощность двигателя и скорость постепенно снижаются в зависимости от уровня тяжести состояния.
- Защита двигателя выключается - двигатель будет выключен, но может быть перезапущен, выключив зажигание, а затем снова включен.

![[19a00825.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The generator-drive control system is an electronic control system that is comprised of three ECMs.
>
> - ECM 1 and ECM 3 are CM552 models. The CM552 monitors and controls fueling.
> - ECM 2 is a CM850 model. It monitors and controls all other engine functions.
>
> The ECMs share some monitoring functions that are addressed in Section TF.
>
> ### Diagnostic Fault Codes
>
> The QST30 electronic control system can record certain fault conditions. These conditions can be displayed by connecting an electronic service tool.
>
> There are two data link ports for communication with the ECMs.
>
> The data link ports are located on the left hand side of the engine. The forward data link port is for communication with the CM552 ECMs.
>
> The rear port is for communication with the CM850 ECM and **must** be connected first.
>
> There are two types of fault codes:
>
> - Engine electronic fuel system fault codes
> - Engine protection system fault codes
>
> All fault codes recorded will either be active (fault code is active on engine) or inactive (fault code was active at one time, but **not** at this moment).
>
> Active and inactive fault codes can be viewed with INSITE™ electronic service tool.
>
> The engine protection system records separate fault codes when an out-of-range condition is found for any of the sensors in the engine protection system.
>
> The following are engine protection system out-of-range fault codes:
>
> - Coolant temperature
> - Coolant level (optional)
> - Oil pressure.
>
> ### Fault Code Snapshot Data
>
> A diagnostic fault code is recorded in the ECM.
>
> The ECM input and output data is recorded from all sensors and switches.
>
> Snapshot data allow the relationships between ECM inputs and outputs to be viewed during troubleshooting.
>
> ### Engine Protection System
>
> The engine protection system monitors critical engine temperatures, fluid levels, switch positions and pressures. Diagnostic fault codes will log when an over or under normal operating range occurs.
>
> If an out-of-range condition exists, an engine derate action can be initiated. If an out-of-range condition exists, an active fault code will be generated in the ECM.
>
> Engine protection system monitors:
>
> - Coolant temperature
> - Coolant level (optional)
> - Intake manifold temperature
> - Oil pressure.
>
> Engine protection system monitors for:
>
> - High coolant temperature
> - Low coolant level (optional)
> - High intake manifold temperature
> - Low to very low oil pressure.
>
> The engine protection system can have two selectable features:
>
> - Engine protection enable - Engine power and speed are gradually reduced, depending on level of severity of condition.
> - Engine protection shutdown - The engine will shut down, but can be restarted by turning the keyswitch off and then back on.
