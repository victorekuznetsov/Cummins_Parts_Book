---
aliases:
  - "Схемы компонентов"
type: "Процедура"
doc: "326-208-002"
title_en: "Component Diagrams"
title_ru: "Схемы компонентов"
modified: "2019-09-09"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4358378"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-208-002.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-208-002.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/326"
  - "перевод/машинный"
---

# Component Diagrams
**Схемы компонентов**

> [!abstract] Процедура · `326-208-002`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4358378 — Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick Marine Con|4358378]]
> **Секции:** Section E - Product and System Identification
> **Даты:** изменён 2019-09-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-208-002.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-208-002.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система Cummins® Inboard Joystick теперь предлагается с системами двигателей, поставляемыми производителем оборудования (OEM). Существуют две разные версии рычажных станций управления и бортовых джойстиков. Унаследованная версия рычажной станции управления - все версии 3 и старше, а существующая версия - 4 и больше. Наследственная версия джойстика - все версии 2 и старше, а существующая версия - 3 и больше. Версия 3 и более мощные джойстики, а также версия 4 и более мощные станции управления рычагами будут предварительно настроены с завода с идентификатором Handle ID номер 1. Существующие и устаревшие джойстики и станции управления рычагами обратно совместимы.

Cummins® Inboard Joystick System (наборная система джойстиков)

Cummins® Электронная дроссельная заслонка и переключение и Cummins® Наборные джойстики базовые компоненты местоположения.

1. Станция управления рычагом на главном штурвале
2. На борту Joystick на главном штурвале
3. Модуль процессора управления дроссельной заслонки рядом с двигателем
4. Модуль интерфейса ruster
5. Боу-Растер
6. Стерн Трюстер.

![[00900620.png]]

Cummins® Inboard Joystick с OEM-поставкой Thruster Systems

Cummins® Electronic Throttle and Shift и Cummins® Inboard Joystick базовые компоненты с проводными ремнями.

1. Станция управления рычагом на главном штурвале
2. На борту Joystick на главном штурвале
3. Модуль процессора управления дроссельной заслонки рядом с двигателем
4. Модуль Thruster Interface (Switch, Analog или CAN-based)
5. Производитель: Bow Thruster
6. OEM-поставщик Bow Thruster.

![[00900620.png]]

Cummins® Inboard Joystick System (наборная система джойстиков)

Cummins® Electronic Throttle and Shift (ETS) и Cummins® Inboard Joystick базовые компоненты с проводными ремнями.

1. Станция управления рычагом на главном штурвале
2. На борту Joystick на главном штурвале
3. Модуль процессора управления дроссельной заслонки рядом с двигателем
4. Модуль интерфейса ruster
5. Боу-Растер
6. Стерн Трустер
7. Портовый двигатель
8. Двигатель Starboard
9. Throttle Control Processor Module Interface интерфейс проводов
10. Controller Area Network (CAN) Расширение данных
11. Controller Area Network (CAN) - система передачи данных Tee
12. Thruster Interface Data Wiring Usgil с портом инструментов
13. Thruster Interface - Узлы для проводов Thruster
14. Узлы для проводов Thruster Extension.

![[00900621.png]]

Cummins® Inboard Joystick System с OEM-поставкой Thruster Systems

Cummins® Electronic Throttle and Shift (ETS) и Cummins® Inboard Joystick с OEM-поставленной системой Thruster с проводными ремнями.

1. Станция управления рычагом на главном штурвале
2. Панель управления Thruster на главном штурвале
3. Модуль процессора управления дроссельной заслонки рядом с двигателем
4. Модуль Thruster Interface (Switch, Analog или CAN-based)
5. Производитель: Bow Thruster
6. Поставщик: Stern Thruster
7. Портовый двигатель
8. Двигатель Starboard
9. Throttle Control Processor Module Interface интерфейс проводов
10. Controller Area Network (CAN) Расширение данных
11. Controller Area Network (CAN) - система передачи данных Tee
12. Thruster Interface Data Wiring с портом инструмента и модулем двойного реле
13. Thruster Interface - Узлы для проводов Thruster
14. Узлы для проводов Thruster Extension.

![[00900621.png]]

Cummins® Electronic Throttle and Shift (ETS) и Thruster Control Panel базовые компоненты с проводными ремнями,

1. Станция управления рычагом n главный руль
2. Панель управления Thruster на главном штурвале
3. Модуль процессора управления дроссельной заслонки рядом с двигателем
4. Thruster Extension Wiring Grund
5. Боу-Растер
6. Стерн Трустер
7. Портовый двигатель
8. Двигатель Starboard
9. Throttle Control Processor Module Interface интерфейс проводов
10. Управляющая зона Netwrok (CAN) Расширение данных жгут.

![[00900621.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Cummins® Inboard Joystick system is now offered with equipment manufacturer (OEM) supplied thruster systems. There are two different versions of lever control stations and inboard joysticks. The legacy lever control station version is all versions 3 and older and the existing version is 4 and greater. The legacy joystick version is all versions 2 and older and the existing version is 3 and greater. Version 3 and greater joysticks and version 4 and greater lever control stations will come pre-configured from factory with Handle ID Number 1. Existing and legacy joysticks and lever control stations are backwards compatible.
>
> Cummins® Inboard Joystick System
>
> Cummins® Electronic Throttle and Shift and Cummins® Inboard Joystick basic component locations.
>
> 1. Lever Control Station on main helm
> 2. Inboard Joystick on main helm
> 3. Throttle Control Processor Module near engine
> 4. Thruster Interface Module
> 5. Bow Thruster
> 6. Stern Thruster.
>
> Cummins® Inboard Joystick with OEM-Supplied Thruster Systems
>
> Cummins® Electronic Throttle and Shift and Cummins® Inboard Joystick basic component locations with harnesses.
>
> 1. Lever Control Station on main helm
> 2. Inboard Joystick on main helm
> 3. Throttle Control Processor Module near engine
> 4. Thruster Interface Module (Switch, Analog, or CAN-based)
> 5. OEM-Supplies Bow Thruster
> 6. OEM-Supplied Bow Thruster.
>
> Cummins® Inboard Joystick System
>
> Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick basic component locations with harnesses.
>
> 1. Lever Control Station on main helm
> 2. Inboard Joystick on main helm
> 3. Throttle Control Processor Module near engine
> 4. Thruster Interface Module
> 5. Bow Thruster
> 6. Stern Thruster
> 7. Port Engine
> 8. Starboard Engine
> 9. Throttle Control Processor Module Interface Harness
> 10. Controller Area Network (CAN) Data Extension Harness
> 11. Controller Area Network (CAN) Data Harness Tee
> 12. Thruster Interface Data Harness with tool port
> 13. Thruster Interface Thruster Harness
> 14. Thruster Extension Harness.
>
> Cummins® Inboard Joystick System with OEM-Supplied Thruster Systems
>
> Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick with OEM-Supplied Thruster System with harnesses.
>
> 1. Lever Control Station on main helm
> 2. Thruster Control Panel on main helm
> 3. Throttle Control Processor Module near engine
> 4. Thruster Interface Module (Switch, Analog, or CAN-based)
> 5. OEM-Supplied Bow Thruster
> 6. OEM-Supplied Stern Thruster
> 7. Port Engine
> 8. Starboard Engine
> 9. Throttle Control Processor Module Interface Harness
> 10. Controller Area Network (CAN) Data Extension Harness
> 11. Controller Area Network (CAN) Data Harness Tee
> 12. Thruster Interface Data Harness with tool port and dual relay module
> 13. Thruster Interface Thruster Harness
> 14. Thruster Extension Harness.
>
> Cummins® Electronic Throttle and Shift (ETS) and Thruster Control Panel basic component locations with harnesses,
>
> 1. Lever Control Station n main helm
> 2. Thruster Control Panel on main helm
> 3. Throttle Control Processor Module near engine
> 4. Thruster Extension Harness
> 5. Bow Thruster
> 6. Stern Thruster
> 7. Port Engine
> 8. Starboard Engine
> 9. Throttle Control Processor Module Interface Harness
> 10. Controller Area Netwrok (CAN) Data Extension Harness.
