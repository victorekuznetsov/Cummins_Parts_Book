---
aliases:
  - "Батарея часов реального времени"
type: "Процедура"
doc: "82-019-311"
title_en: "Real-Time Clock Battery"
title_ru: "Батарея часов реального времени"
modified: "2002-06-03"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-311.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-311.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Real-Time Clock Battery
**Батарея часов реального времени**

> [!abstract] Процедура · `82-019-311`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-311.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-311.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Модуль резервного копирования часов в режиме реального времени подключен к основной ветке проводов двигателя вблизи 50-контактного разъема порта датчика ECM.

ECM использует функцию часов в реальном времени для маркировки времени и других данных с указанием времени и даты. Модуль резервного копирования аккумулятора используется для питания часовой схемы в режиме реального времени в ECM, когда питание аккумулятора транспортного средства удаляется из ECM. Если установлен резервный модуль батареи, часы ECM будут поддерживать правильное время и дату с отключенной от ECM мощностью при условии, что разъем электропроводки привода остается подключенным к ECM.

Если резервный модуль аккумулятора часов в реальном времени ** не** установлен на двигателе, необходимо будет установить время и дату с помощью INSITETM, когда функция часов в реальном времени включена в ECM, а мощность аккумулятора транспортного средства удалена из ECM.

![[19c00747.png]]

### Снятие

Найдите резервный модуль аккумулятора в режиме реального времени на главной проводах двигателя. Перережьте проводной галстук, закрепляющий корпус модуля на проводной ремне.

Очистите область вокруг аккумуляторного модуля проводов разъема жгута.

Отсоедините резервный модуль батареи от электропроводки двигателя.

![[19c00748.png]]

### Установка

Используйте быстросушливый электрический контактный очиститель, номер детали. 3824510, для очистки всей грязи и влаги от аккумуляторного резервного модуля и проводов ремня разъема.

**не** нанесите смазку или масло на разъём проводов или резервный модуль батареи.

Подключите резервный модуль батареи к электропроводке двигателя.

Закрепите резервный модуль батареи к основной проводах двигателя с помощью проводных связей.

![[19c00748.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The real-time clock battery backup module is connected to the engine harness main branch near the 50-pin ECM sensor port connector.
>
> The ECM uses the real-time clock feature to time-stamp faults and other data with the time and date. The battery backup module is used to power the real-time clock circuitry in the ECM when vehicle battery power is removed from the ECM. If a battery backup module is installed, the ECM clock will maintain the correct time and date with power removed from the ECM, provided the actuator harness connector remains plugged into the ECM.
>
> If a real-time clock battery backup module is **not** installed on the engine, it will be necessary to set the time and date using INSITE™ whenever the real-time clock feature is enabled in the ECM and vehicle battery power is removed from the ECM.
>
> ### Remove
>
> Locate the real-time clock battery backup module on the main engine harness. Cut the wire tie securing the module case to the harness.
>
> Clean the area around the battery backup module harness connector.
>
> Disconnect the battery backup module from the engine harness.
>
> ### Install
>
> Use quick-dry electrical contact cleaner, Part No. 3824510, to clean all dirt and moisture from the the battery backup module and harness connector.
>
> Do **not** apply grease or oil to either the harness connector or battery backup module.
>
> Connect the battery backup module to the engine harness.
>
> Secure the battery backup module to the main engine harness using wire ties.
