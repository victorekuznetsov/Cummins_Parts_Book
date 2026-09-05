---
aliases:
  - "Идентификация компонентов"
type: "Процедура"
doc: "326-208-001"
title_en: "Component Identification"
title_ru: "Идентификация компонентов"
modified: "2019-10-21"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4358378"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-208-001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-208-001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/326"
  - "перевод/машинный"
---

# Component Identification
**Идентификация компонентов**

> [!abstract] Процедура · `326-208-001`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4358378 — Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick Marine Con|4358378]]
> **Секции:** Section E - Product and System Identification
> **Даты:** изменён 2019-10-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-208-001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-208-001.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система Cummins® Inboard Joystick теперь предлагается с оригинальным оборудованием производителя (OEM), поставляемым системами двигателей. Существуют две разные версии рычажных станций управления и бортовых джойстиков. Унаследованная версия 3 и более старая, а существующая версия 4 и больше. Наследственная версия джойстика - все версии 2 и старше, а существующая версия - 3 и больше. Версия 3 и более мощные джойстики, версия 4 и более мощные станции управления рычагами будут предварительно настроены с завода с помощью Handle ID No. 1. Существующие и устаревшие джойстики и станции управления рычагами обратно совместимы.

#### Электронная дроссельная заслонка и смещение (ETS)

1. Процессорный модуль управления дроссельной заслонки
2. Станция управления рычагом
3. Сети контроллеров (CAN) для расширения данных
4. CAN-данные, оканчивающие резистор
5. Управляющий дроссельным процессором модуль интерфейса проводов жгута.

![[17500007.png]]

#### Cummins® Inboard Joystick с OEM-поставщиком Thruster(s)

1. Модуль интерфейса Thruster (переключатель, аналог или CAN)
2. На борту джойстик
3. CAN Data Extension Wiring Grund
4. CAN Data Wiring Uspedge TEE
5. CAN-данные, оканчивающие резистор
6. Усилитель растяжки Thruster
7. Усилитель электропроводки Thruster Interface
8. Узкостный интерфейс передачи данных.

![[17500008.png]]

#### Конкретные компоненты трустера (1-10) и системные компоненты (11-20)

1. Прямой ток двигателя
2. Прямой ток моторных щеток
3. 4.1.2.1.1 Тормозной тепловой выключатель постоянного тока
4. Эстафета
5. Обложка ретранслятора
6. 2.1.2.2 Сцепление привода
7. горный фланж
8. Двигай ногой
9. Пропеллер
10. Жертвенный цинковый анод
11. Туннель Трустера
12. Модуль интерфейса Ruster
13. На борту джойстик
14. CAN Data Extension Wiring Grund
15. CAN Data Wiring Uspedge TEE
16. CAN-данные, оканчивающие резистор
17. Усилитель растяжки Thruster
18. Усилитель электропроводки Thruster Interface
19. Thruster интерфейс передачи данных жгут
20. Панель управления растяжкой, если она оборудована.

![[00a00170.png]]

#### Поддержка компонентов OEM (см. информацию об услугах производителя оборудования для идентификации)

- Банк батарей
- Замедленный взрыватель
- Переключатель отключения питания с помощью тягового устройства
- Узлы электропроводки Thruster Power
- Электронный дросселирующий сдвиг силовой электропроводки жгута
- OEM поставляла системы двигателей, если они были оборудованы
- Гидравлические системы двигателей, если они оборудованы.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Cummins® Inboard Joystick system is now offered with original equipment manufacturer (OEM) supplied thruster systems. There are two different versions of lever control stations and inboard joysticks. The legacy lever control station versions 3 and older and the existing version is 4 and greater. The legacy joystick version is all versions 2 and older and the existing version is 3 and greater. Version 3 and greater joysticks and version 4 and greater lever control stations will come pre-configured from the factory with Handle ID No. 1. Existing and legacy joysticks and lever control stations are backward compatible.
>
> #### Electronic Throttle and Shift (ETS)
>
> 1. Throttle control processor module
> 2. Lever control station
> 3. Controller area network (CAN) data extension harness
> 4. CAN data terminating resistor
> 5. Throttle control processor module interface harness.
>
> #### Cummins® Inboard Joystick With OEM Supplied Thruster(s)
>
> 1. Thruster interface module (switch, analog, or CAN)
> 2. Inboard joystick
> 3. CAN data extension wiring harness
> 4. CAN data wiring harness tee
> 5. CAN data terminating resistor
> 6. Thruster extension wiring harness
> 7. Thruster interface thruster wiring harness
> 8. Thruster interface data wiring harness.
>
> #### Thruster Specific Components (1-10) and System Components (11-20)
>
> 1. Direct current motor
> 2. Direct current motor brushes
> 3. Direct current motor thermal switch
> 4. Relay pack
> 5. Relay pack cover
> 6. Drive coupling
> 7. Mounting flange
> 8. Drive leg
> 9. Propeller
> 10. Sacrificial zinc anode
> 11. Thruster tunnel
> 12. Thruster interface module
> 13. Inboard joystick
> 14. CAN data extension harness
> 15. CAN data harness tee
> 16. CAN data terminating resistor
> 17. Thruster extension harness
> 18. Thruster interface thruster harness
> 19. Thruster interface data harness
> 20. Thruster control panel, if equipped.
>
> #### Supporting OEM Components (see equipment manufacturer service information for identification)
>
> - Battery bank
> - Slow blow fuse
> - Thruster power disconnect switch
> - Thruster power harness
> - Electronic throttle shift power harness
> - OEM supplied thruster systems, if equipped
> - Hydraulic thruster systems, if equipped.
