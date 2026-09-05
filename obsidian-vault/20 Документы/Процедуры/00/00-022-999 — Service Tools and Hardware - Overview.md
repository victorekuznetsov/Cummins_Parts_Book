---
aliases:
  - "Сервисный инструмент и оснастка — обзор"
type: "Процедура"
doc: "00-022-999"
title_en: "Service Tools and Hardware - Overview"
title_ru: "Сервисный инструмент и оснастка — обзор"
modified: "2023-09-06"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33239899"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41349633"
  - "41353297"
  - "41370103"
  - "85017333"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "K19"
  - "K38/K50 · QSK38, QSK50"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK19"
  - "QSK23"
  - "QSK60"
  - "QST30"
manuals:
  - "3666070"
  - "3666113"
  - "3666214"
  - "3666266"
  - "4021442"
  - "4022094"
  - "4022102"
  - "5411181"
figures: 18
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-022-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-022-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/K19"
  - "двигатель/K38/K50"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "группа/00"
  - "перевод/машинный"
---

# Service Tools and Hardware - Overview
**Сервисный инструмент и оснастка — обзор**

> [!abstract] Процедура · `00-022-999`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, K19, K38/K50 · QSK38, QSK50, NT/NTA855 · ISM/QSM11, QSK19, QSK23, QSK60, QST30
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]], [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]], [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]], [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2023-09-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-022-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-022-999.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Cummins Inc. Производит множество двигателей, которые управляются электронным способом. Эти двигатели имеют специальные диагностические требования к модулю управления двигателем (ECM) в системе. Для взаимодействия с ECM были разработаны инструменты электронного обслуживания.

Рекомендуемая электронная сервисная оснастка Cummins® или эквивалентные интерфейсы с электронными двигателями через шину данных CAN. Шина данных CAN обеспечивает средство передачи и сортировки электрических сигналов и состоит из специальной электронной схемы и электропроводки. Точки подключения от электронных инструментов обслуживания также являются частью шины данных CAN. Оригинальная шина данных CAN производителя оборудования (OEM), если таковая имеется, предоставляется OEM и состоит из схемы, расположенной в ремне проводов OEM. Шина данных CAN двигателя состоит из схемы, расположенной в ремне электропроводки двигателя. Как ссылки на данные о двигателе, так и OEM-производителях определяются стандартами, написанными Обществом автомобильных инженеров (SAE). Cummins Inc. Использует два таких стандарта для электронных средств обслуживания. Один из них представляет собой комбинацию SAE J1587 и SAE J1708, а другой - SAE J1939. Шина данных J1939 CAN более подробно описана в Процедуре 019-165 в соответствующем руководстве по обслуживанию двигателя. Шина данных J1587/J1708 CAN более подробно описана в Процедуре 019-166 в соответствующем руководстве по обслуживанию и далее в настоящем документе называется J1708. Ссылки на данные двигателя (как J1939, так и J1708) более подробно рассматриваются в Процедуре 019-428 в соответствующем руководстве по обслуживанию двигателя.

### Электронный сервис инструмент Описание

Рекомендуемый инструмент для электронных услуг Cummins® или эквивалентный ему инструмент представляет собой программное приложение на базе Windows®, которое работает с ECM Cummins® для диагностики и устранения проблем с двигателем, хранения и анализа исторической информации о двигателе и изменения рабочих значений двигателя. Электронный сервисный инструмент Professional также позволяет передавать калибровки в ECM.

Инструмент электронного сервиса используется на персональном компьютере (ПК), который прикреплен к ECM через набор адаптера шины данных INLINETM CAN.

1. Адаптеры INLINETM, INLINETM I, INLINETM 2, INLINETM 4 и INLINETM 5 устарели. Их можно использовать с электронным сервисным оборудованием, но техническая поддержка этих адаптеров недоступна.

После регистрации копии инструментария электронного обслуживания и подключения к источнику данных ECM инструмент электронного сервиса позволяет вам извлекать существующие или записанные данные о двигателе, изменять настройки ECM, хранить данные для просмотра в более позднее время, анализировать данные для мониторинга и оценки работы двигателя и просматривать коды ошибок активного или неактивного двигателя.

Инструмент электронного сервиса устанавливается в папке INTELECTTM на жёстком диске персонального компьютера. Руководства пользователя доступны в папке INTELECTTM и Руководства для конкретных электронных двигателей Cummins®. Дополнительная информация для обслуживания и поддержки от дистрибьютора Cummins® для вопросов по электронному инструменту обслуживания включена в передней части руководств пользователя.

Различные версии инструментария для электронных услуг могут быть доступны для использования в одно время, хотя некоторые версии инструментария для электронных услуг могут быть несовместимы с некоторыми ECM. Информация о совместимости ECM и электронных услуг доступна на веб-сайте Продукта. Улучшения электронного инструментария иногда выпускаются в виде пакетов функций. Последняя информация о пакете функций для конкретных версий инструментов для электронных услуг также доступна на веб-сайте продукта для электронных услуг. Поддерживайте электронный сервис с последними версиями и пакетами функций, которые становятся доступными.

Инструменты электронного сервиса могут использовать либо порт связи (порт COM), универсальную последовательную шину (USB), WIFI, либо соединение Bluetooth на ПК при общении с ECM. Порт COM должен быть правильно настроен для правильной работы инструментария электронного сервиса. Другие программы на ПК могут взять под контроль порт COM и предотвратить доступ к порту COM. Информация о устранении неполадок для проблем связи с электронным сервисом доступна в базовом руководстве пользователя, а также в ECM № Communication Troubleshooting Tree на QuickServeTM Online или Intercept.

### Первичная проверка

#### Инструмент электронного обслуживания

- В главном окне инструментов для электронных услуг убедитесь, что шина данных CAN, выбранная в выпадающем выпадающем окне подключения к источнику данных ECM, соответствует используемому оборудованию шины данных CAN.
- Проверьте правильность установленной версии. Версия может быть определена из главного окна, выбрав Help, About.
- Проверить, отключен ли инфракрасный порт, чтобы последовательный порт использовался только для связи ECM.
- Если у вас есть менеджер горячей синхронизации Palm Pilot на ПК, который **только **имеет один последовательный порт, вы должны отключить диспетчер горячей синхронизации перед подключением к ECM.

#### Адаптеры шины данных CAN

- Проверьте версию прошивки адаптера шины данных INLINETM CAN - это последняя доступная версия прошивки.
- Убедитесь, что используемый адаптер шины данных CAN совместим с проводкой шины данных CAN, доступной на двигателе или транспортном средстве.

- Адаптер шины данных CAN представляет собой устройство, которое преобразует сообщения шины данных J1708 или J1939 CAN из ECM в сообщение, которое может обрабатывать ПК. Поскольку инструмент электронного обслуживания является инструментом на базе ПК, для устранения неполадок требуется адаптер шины данных CAN.
- Сервисные продукты Cummins® предлагают следующие комплекты адаптера шины данных CAN:

- На следующей иллюстрации показаны адаптеры шины данных INLINETM CAN.

Мощность адаптеров шины данных INLINETM CAN зависит от используемой настройки связи. Мощность 12 VDC обеспечивается системой питания транспортного средства для транспортных средств и установок связи двигателя. 12 VDC питание обеспечивается вспомогательным источником питания для установки связи испытательного стенда.

Адаптер шины данных INLINETM CAN будет поддерживать протокол J1708 или J1939. При подключении к инструменту электронного обслуживания с помощью адаптера шины данных INLINETM CAN инструмент электронного сервиса сначала попытается установить связь с ECM на J1939. Если на J1939 не будет установлено сообщение, то инструмент электронного сервиса попытается установить связь на J1708.

![[22800616.png]]

CAN шина данных Adapter Identification Diagram - INLINETM 4.

1. Светильник
2. J1939 - коммуникационный свет
3. Светодиапазон J1708
4. RS-232 для PC Light

INLINETM 4 представляет собой совместимый с RP1210A адаптер шины данных CAN, который будет поддерживать протокол J1708 и J1939. RP1210A является отраслевым стандартом, который определяет формат сообщения шины данных CAN для инструментов обслуживания. INLINETM 4 должен быть правильно настроен в инструменте электронного обслуживания для определения порта COM, используемого на ПК, и типа доступного протокола шины данных CAN, J1708, J1939 или автодетектирования.

![[22800617.png]]

CAN шина данных Adapter Identification Diagram - INLINETM 5.

1. Светильник
2. J1939 - коммуникационный свет
3. Светодиапазон J1708
4. RS-232 для PC Light
5. USB на PC свет.

INLINETM 5 - это адаптер шины данных CAN, совместимый с RP1210A, который будет поддерживать протокол J1708 и J1939. Адаптер может использоваться с портом COM или портом USB. INLINETM 5 должен быть правильно настроен в инструменте электронного обслуживания для определения COM или USB-порта, используемого на ПК, и типа протокола шины данных CAN, доступного, J1708 или J193, или автодетектирования.

![[22r00008.png]]

Схема идентификации адаптера шины данных - INLINETM 6

1. Светильник
2. CAN 1 Communication Light (J1939)
3. CAN 2 Communication Light (J1939) (недоступная ссылка)
4. J1708 Коммуникация
5. RS-232 для PC Light
6. USB на PC свет.

INLINETM 6 представляет собой совместимый с RP1210A адаптер шины данных CAN, который будет поддерживать протоколы J1708 и J1939. Адаптер может использоваться с портом COM или портом USB. INLINETM 6 должен быть правильно настроен в инструменте электронного обслуживания для определения COM или USB-порта, используемого на ПК, и типа доступного протокола шины данных CAN, J1708, J1939 или автодетектирования.

![[19r99367.png]]

Схема идентификации адаптера шины данных - INLINETM 7

1. Светильник
2. Светодиодная связь
3. Световой индикатор/световой индикатор типа связи
4. Свет от вины.

INLINETM 7 представляет собой адаптер шины данных RP1210A, RP1210B и RP1210C, который будет поддерживать J1587/J1708, а также J1939 (250K, 500K или 1MB Baud Rate). Адаптер может **только **быть подключен к ПК через USB, WIFI или Bluetooth соединение. Инструмент должен быть правильно настроен в инструменте электронного обслуживания для определения типа соединения на ПК и типа доступного протокола шины данных CAN, J1587/J1708 или J1939.

Адаптеры шины данных INLINETM CAN требуют программного обеспечения прошивки для правильной работы. Версии прошивки периодически обновляются и **должны быть загружены в адаптеры шины данных CAN при выпуске обновлений. Последняя версия прошивки всегда доступна на последнем DVD-ROM INCALTM, а также на веб-сайте http://cumminsengines.com/inline. Версия прошивки для адаптера шины данных CAN может быть найдена в рекомендуемой электронной службе Cummins или эквивалентной. При использовании инструментария электронного сервиса версия прошивки отображается в правом нижнем углу главного окна при подключении к ECM. Инструменты электронного сервиса **должны быть подключены к ECM для отображения версии прошивки.

### Настройка

Общие сведения

Связь с ECM может быть установлена в трех основных местах:

- Настройка стенда для тестирования
- Настройка связи транспортного средства
- Настройка связи двигателя.

Настройки связи более подробно описаны в остальной части этой процедуры. В каждом месте используются различные кабели адаптера шины данных CAN. Все три местоположения требуют либо последовательного кабеля, USB-кабеля, WIFI или соединения Bluetooth для интерфейса с адаптера шины данных CAN на ПК. Ссылка на таблицу ниже.

ECM на новых двигателях может поддерживать связь шины данных CAN на шине данных OEM CAN через разъем OEM в ECM. ECM также может поддерживать связь шины данных CAN на шине данных CAN двигателя через разъем двигателя в ECM. Диаграмма проводов для конкретного двигателя и ECM должна быть проверена, чтобы определить, поддерживает ли ECM как шину данных OEM CAN, так и шину данных CAN двигателя.

Для двигателей Midrange и Heavy Duty рекомендуемой установкой связи, если она доступна, является Cummins Inc. Настройка связи испытательного стенда, которая устанавливает связь непосредственно с ECM. Настройка связи на испытательном стенде может поддерживать как протоколы шины данных J1708, так и J1939 CAN при использовании с ECM, которые поддерживают оба протокола.

Для двигателей высокой мощности с несколькими ECM, рекомендуемая настройка связи - это настройка связи двигателя через 9-контактный разъем, предусмотренный в ремне электропроводки двигателя.

J1939 Сообщение шины данных CAN, если таковое имеется, предпочтительно для передачи калибровок из-за меньших помех от других устройств шины данных CAN, таких как системы управления тягой и электронные тире. Для связи J1708 может потребоваться дополнительное время для отключения OEM ECM, которые также обмениваются данными на шине J1708 CAN, чтобы избежать помех от этих устройств. Кроме того, скорость передачи информации J1939 быстрее, чем J1708, и загрузка калибровки займет меньше времени для завершения с использованием связи J1939 по сравнению с связью J1708.

Функциональность установки связи может быть проверена путем тестирования установки связи на втором ECM или транспортном средстве, если таковая имеется, или путем завершения проверок сопротивления, определенных для каждого типа установки.

В следующей таблице кратко излагаются схемы связи ECM.

| Настройка связи | Место соединения шины данных | Двигатель ECM CAN Data Bus Источник | Поддерживаемые протоколы шины данных CAN |
|---|---|---|---|
| испытательный стенд | разъём ECM | ОЭМ | J1708, J1939 |
| 6-контактный автомобиль | Разъем для штифтов Dash 6 | ОЭМ | 1708 год |
| 9-пинковый автомобиль | Разъем 9 pin | ОЭМ | J1708, J1939 1 |
| Двигатель | ← 3-х штифтовый разъем | Двигатель | 1939 год |
| Двигатель | 6-контактный разъем 6 pin | Двигатель | 1708 2 |
| Двигатель | 9-контактный разъем для подключения двигателя | Двигатель | 1939 3-й год |

#### Примечания:

1. 9-контактный разъем должен быть полностью подключен к протоколу J1939.
2.
3.

Измерительный стенд Communication Setup

Настройка связи испытательного стенда устанавливает связь непосредственно с ECM через порт разъема на ECM. Пример установки связи испытательного стенда показан ниже.

Калибровочная проводка испытательного стенда (1) является общей для большинства установок испытательного стенда и может использоваться с соответствующим калибровочным кабелем испытательного стенда (5) для связи с различными ECM. Список доступных кабелей (5) для калибровки стендов для различных ECM включен в Инструкцию по эксплуатации инструментария, Бюллетень 3377791, которая доступна на QuickServeTM Online. Правильная функция испытательного стенда калибровочной проводов упряжки (1) и испытательного стенда калибровочного кабеля (5) может быть проверена с помощью схем проводов, предоставленных для завершения проверок сопротивления.

![[22800563.png]]

Измерительный стенд Communication Setup

1. испытательный стенд калибровочный жгут, номер детали 3163151
2. Электропитание 1
3. Инструмент электронного обслуживания
4. Адаптер шины данных CAN
5. ECM 1 испытательный стенд калибровочный кабель
6. USB-кабель, номер детали 4918591 или последовательный кабель, номер детали 4918418 (справочная таблица выше для типа кабеля)
7. Кабель адаптера шины данных CAN, номер детали 3165159 (INLINETM 4, 5 и 6)
8. CM570 ECM (пример).

1. См. Service tooling Instruction, ECM test stand calibration Base Wiring harness, Bulletin 3377791, for part number.

Настройка связи транспортного средства

Дополнительная настройка связи - это соединение 9 или 6 контактов DeutschTM, которое обычно находится в кабине транспортного средства. Настройка связи транспортного средства использует OEM-проводку и подключается к ECM в порту разъема OEM. 9-контактный разъем в кабине, если он полностью подключен, может поддерживать протокол J1939 и J1708. Некоторые OEM-производители размещают 9-контактный разъем в кабине, но не обеспечивают проводку для поддержки протокола J1939. 6-контактный разъем **только **поддерживает протокол J1708.

![[22800562.png]]

Настройка связи с транспортным средством

1. Адаптер шины данных CAN
2. USB-кабель, номер детали 4918591 или последовательный кабель, номер детали 4918418 (справочная таблица выше для типа кабеля)
3. кабель адаптера шины данных 1
4. Инструмент электронного обслуживания
5. Коннектор адаптера данных CAN 1.

1. См. Service tooling Instruction, ECM test stand calibration Base Wiring harness, Bulletin 3377791, for part number.

Сети шины данных INLINETM 6 CAN, оборудованные для поддержки 500K baud CAN скорости шины данных, требуют инструмента адаптера, Номер детали 5299126, для подключения к 9-контактному разъему.

Только INLINETM 6 и INLINETM 7 способны поддерживать скорость шины данных CAN 500K baud. INLINETM 4 и INLINETM 5 поддерживают скорость шины данных 500K baud CAN.

Настройка системы связи

Настройка связи двигателя использует шину данных CAN двигателя, предоставленную на ремне проводов двигателя. В зависимости от двигателя, настройка связи двигателя, доступная на ремне проводов двигателя, может быть 3-контактным разъемом DeutschTM, 6-контактным разъемом DeutschTM или 9-контактным разъемом DeutschTM.

Разъем 3 pin DeutschTM на ремне электропроводки двигателя доступен на новых двигателях и обеспечивает точку подключения к шине данных J1939 CAN. Для подключения к ECM по протоколу J1939 может потребоваться мини-кабель, который включает в себя резистор 60 Ом и кабель для изменения пола. Для адаптера шины данных CAN требуется вспомогательный источник питания.

![[22800620.png]]

3 Pin DeutschTM Connector

1. Шина данных CAN 1
2. Кабель питания 1
3. Инструмент электронного обслуживания
4. Адаптер шины данных CAN
5. Кабель для смены пола, номер детали 3163597
6. Мини-кабель, номер детали 3163096
7. USB-кабель, номер детали 4918591 или последовательный кабель, номер детали 4918418 (справочная таблица выше для типа кабеля)
8. 3-контактный разъем, номер детали 3165141.

1. См. Service tooling Instruction, ECM test stand calibration Base Wiring harness, Bulletin 3377791, for part number.

6-контактный разъем DeutschTM доступен на ремне электропроводки двигателя для некоторых старых двигателей и обеспечивает точку подключения к шине данных J1939 CAN. 6-контактный разъем включает в себя источник питания для адаптера шины данных CAN.

### Проверка сопротивления

Для интерфейса с адаптером шины данных CAN на ПК требуется последовательный кабель, или USB-кабель может использоваться с адаптером шины данных INLINETM 5/6/7 CAN.

> [!warning] ОСТОРОЖНО
> Используйте испытательный щуп, номер детали 3822758, и испытательный щуп, номер детали 3822917, чтобы избежать возможности повреждения последовательных штифтов кабеля.

![[22800565.png]]

Серийный кабель, номер детали 4918418

1. Открыть
2. Передача данных
3. Получать данные
4. Готовый терминал обработки данных (+5 VDC)
5. Сигнальная площадка
6. Открыть
7. Запрос на отправку (+5 VDC)
8. Ясно посылать
9. Открывай.

- Вставьте измерительный щуп в контакт 1 гнездового конца последовательного кабеля, и подключите свинец к многометровому щупу. Прикрепите другой испытательный щуп для контакта с 1 штыревым концом последовательного кабеля и соедините свинец с многометровым щупом.
- Измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Повторите измерение сопротивления для контактов 2-9. Мультиметр **должен** показывать замкнутую цепь (10 Ом или меньше) для каждого штифта. Если цепь **не** закрыта, замените последовательный кабель.

> [!warning] ОСТОРОЖНО
> Чтобы избежать возможности повреждения контактов разъема, используйте пробный щуп, номер детали 3823993, на разъеме 8 штифтов. Используйте пробный щуп, номер детали 3823994, на круглом 9-контактном разъеме. Используйте измерительный щуп, номер детали 3824812, на 3-контактном разъеме.

![[22800618.png]]

испытательный стенд калибровочный жгут, номер детали 3163151

1. J1939 CAN Data Bus (+) (недоступная ссылка)
2. J1939 Щит шины данных
3. Аккумулятор (+)
4. Батарея (-)
5. переключатель зажигания
6. J1939 CAN Data Bus (-) (недоступная ссылка)
7. J1708 CAN Data Bus (+)
8. J1708 CAN Data Bus (-) (недоступная ссылка)

- Измерьте сопротивление каждого штифта в 8 штифтовом разъеме к соответствующему местоположению в 9 штифтах и/или 3 штифтовых разъемах. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не** закрыта, замените испытательный стенд калибровочной проводкой.

> [!warning] ОСТОРОЖНО
> Чтобы избежать возможности повреждения контактов разъема, используйте пробный щуп, номер детали 382994, на разъеме 8 штифтов. Определить соответствующий испытательный щуп, необходимый для разъема ECM на испытательном стенде калибровочного кабеля.

![[22800619.png]]

испытательный стенд калибровка кабель

1. J1939 CAN Data Bus (+) (недоступная ссылка)
2. J1939 Щит шины данных
3. Аккумулятор (+)
4. Батарея (-)
5. переключатель зажигания
6. J1939 CAN Data Bus (-) (недоступная ссылка)
7. J1708 CAN Data Bus (+)
8. J1708 CAN Data Bus (-) (недоступная ссылка).
9. ECM Connector (см. схему проводов для идентификации контакта с разъемом ECM).

- Измерьте сопротивление каждого штифта в 8 штифтовом разъеме к соответствующему месту в разъеме ECM. См. схему проводов для ECM для идентификации контакта с разъемом. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не** закрыта, замените калибровочный кабель испытательного стенда.

> [!warning] ОСТОРОЖНО
> Чтобы избежать возможности повреждения контактов разъема, используйте штыревой испытательный щуп, номер детали 3823993, на разъеме 9 pin DeutschTM. Используйте штыревой тест-щуп, номер детали 3822758, на 25-контактном разъеме.

![[22800621.png]]

![[19400739.png]]

9 Pin CAN Data Bus Кабель, номер детали 3165159

9 Pin In-Cab CAN Data Bus Connector

- А. земля
- Б. Аккумулятор (+)
- С. J1939 CAN Data Bus (+) (недоступная ссылка)
- Ди. J1939 CAN Data Bus (-) (недоступная ссылка)
- Е. J1939 Щит шины данных
- Ф. J1708 CAN Data Bus (+)
- Г. J1708 CAN Data Bus (-) (недоступная ссылка)
- Х. Открыть
- Джей. Открыть

- Измерить сопротивление от контактов A, B, C, D, E, F и G в 9-контактном разъёме к соответствующему местоположению в 25-контактном разъёме, как показано. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не **закрыта, замените кабель шины данных CAN.

> [!warning] ОСТОРОЖНО
> Чтобы избежать возможности повреждения контактов разъема, используйте штыревой испытательный щуп, номер детали 3824811, на разъеме 6 pin DeutschTM. Используйте штыревой тест-щуп, номер детали 3822758, на 25-контактном разъеме.

![[05800054.png]]

![[19400740.png]]

6 Pin CAN Data Bus Кабель, номер детали 3165160

6 Pin In-Cab CAN Data Bus Connector

1. J1708 CAN Data Bus (+)
2. J1708 CAN Data Bus (-) (недоступная ссылка)
3. Аккумулятор (+)
4. Открыть
5. земля
6. Открывай.

- Измерьте сопротивление контактов A, B, C и E в 6-контактном разъёме с соответствующим местоположением в 25-контактном разъёме, как показано. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не **закрыта, замените кабель шины данных CAN.

> [!warning] ОСТОРОЖНО
> Чтобы избежать возможности повреждения контактов разъема, используйте штыревой испытательный щуп, номер детали 3822758, на разъеме 25 штифтов. Используйте гнездовой тест-щуп, номер детали 3823994, на 3-контактном разъеме. Используйте штыревой испытательный щуп, номер детали 3822995, на 2-контактном разъеме питания.

![[22800568.png]]

3 Pin CAN Data Bus Кабель, номер детали 3165141

- Измерьте сопротивление контактов A, B и C в 3-контактном разъёме к соответствующему местоположению в 25-контактном разъёме, как показано. Измерить сопротивление от контактов D и E в 2-контактном разъеме питания к соответствующему месту в 5-контактном разъеме, как показано. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не **закрыта, замените кабель шины данных CAN.

> [!warning] ОСТОРОЖНО
> Чтобы избежать возможности повреждения контактов разъема, используйте два штыревых испытательных щупа, номер детали 3823993, на каждом разъеме с 3 штифтами.

![[19803849.png]]

Мини-кабель, номер детали 3163096

- Измерьте сопротивление от контакта А в одном конце магистрального кабеля до контакта А в противоположном конце магистрального кабеля. Повторить для контактов В и С. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не **закрыта, замените магистральный кабель. Измерить сопротивление между контактами А и В на обоих концах кабеля для измерения конечного сопротивления. Значение конечного сопротивления **должно **измеряться от 50 до 70 Ом.

> [!warning] ОСТОРОЖНО
> Чтобы избежать возможности повреждения контактов разъема, используйте два гнездовых испытательных щупа, номер детали 3823994, на каждом разъеме с 3 штифтами.

![[19901672.png]]

Кабель для смены пола, номер детали 3163597

- Измерьте сопротивление от контакта А на одном конце кабеля для изменения пола, чтобы связаться с А на противоположном конце кабеля для изменения пола. Повторить для контактов В и С. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не **закрыта, замените кабель для смены пола.

> [!warning] ОСТОРОЖНО
> Чтобы избежать возможности повреждения контактов разъема, используйте два штыревых испытательных щупа, номер детали 3164113, на 26-контактном разъеме с INLINETM 7. Используйте штыревой тест-щуп, номер детали 3824811, на 6-контактном разъеме DeutschTM. Используйте штыревой тест-щуп, номер детали 3823993, на 9-контактном разъеме DeutschTM.

![[19r99368.png]]

INLINETM 7 CAN шина данных

#### 6 Pin DeutschTM Connector устранение неполадок

- Измерьте сопротивление контактов A, B, C и E в 6-контактном разъёме с соответствующим местоположением в 26-контактном разъёме, как показано. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не **закрыта, замените кабель шины данных CAN.

#### 9 Pin DeutschTM Connector Устранение неполадок

- Измерить сопротивление контактов A, B, C, D, E, F и G в 9-контактном разъёме к соответствующему местоположению в 26-контактном разъёме, как показано. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не **закрыта, замените кабель шины данных CAN.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Cummins Inc. produces many engines that are electronically controlled. These engines have special diagnostic requirements for the engine control module (ECM) in the system. To interface with the ECMs, electronic service tools have been developed.
>
> The recommended Cummins® electronic service tool or equivalent interfaces with the electronic engines via a data link. A data link provides a means of transmitting and sorting electric signals, and consists of special electronic circuitry and electrical harnesses. Connection points from electronic service tools are also part of the data link. An original equipment manufacturer (OEM) data link, if available, is provided by the OEM and consists of circuitry located in the OEM harness. An engine data link consists of circuitry located in the engine harness. Both engine and OEM data links alike are defined by standards written by the Society of Automotive Engineers (SAE). Cummins Inc. uses two such standards for electronic service tools. One is a combination of SAE J1587 and SAE J1708 and the other is SAE J1939. The J1939 data link is described in more detail in Procedure 019-165 in the appropriate engine service manual. The J1587/J1708 data link is described in more detail in Procedure 019-166 in the appropriate service manual, and is hereafter referred to as J1708 in this document. Engine data links (both J1939 and J1708) are discussed in more detail in Procedure 019-428 in the appropriate engine service manual.
>
> ### Electronic Service Tool Description
>
> The recommended Cummins® electronic service tool, or equivalent, is a Windows® based software application that works with Cummins® ECMs to diagnose and troubleshoot engine problems, store and analyze historical information about an engine, and to modify an engine's operating values. The electronic service tool Professional also enables you to transfer calibrations to an ECM.
>
> The electronic service tool is used on a personal computer (PC) that is attached to an ECM through an INLINE™ data link adapter kit.
>
> 1. The INLINE™, INLINE™ I, INLINE™ 2, INLINE™ 4, and INLINE™ 5 adapters have become obsolete. They can be used with the electronic service tool, but technical support for these adapters is not available.
>
> After registering a copy of the electronic service tool and connecting to an ECM data source, the electronic service tool enables you to retrieve present or recorded data about an engine, alter ECM settings, store data for viewing at a later time, analyze data to monitor and assess the operation of an engine, and view active or inactive engine fault codes.
>
> The electronic service tool is installed in the INTELECT™ folder on the hard drive of a personal computer. User manuals are available in the INTELECT™ and Manuals folder for specific Cummins® electronic engines. Additional information for service and support from a Cummins® distributor for the electronic service tool questions is included in the front of the user manuals.
>
> Different versions of the electronic service tool may be available for use at one time, although some electronic service tool versions may **not** be compatible with some ECMs. ECM and electronic service tool compatibility information is available at the Product website. Electronic service tool improvements are sometimes released as Feature Packs. The latest Feature Pack information for specific electronic service tool versions is also available at the electronic service tool product website. Maintain the electronic service tool with the latest versions and Feature Packs that become available.
>
> The electronic service tool can utilize either a communication port (COM port), universal serial bus (USB), WIFI, or Bluetooth connection on the PC when communicating with an ECM. A COM port **must** be configured properly for the electronic service tool to function correctly. Other software programs on the PC can take control of a COM port and prevent the electronic service tool from accessing the COM port. Troubleshooting information for the electronic service tool communication issues is available in the base user manual and also in the ECM No Communication Troubleshooting Tree on QuickServe™ Online or Intercept.
>
> ### Initial Check
>
> #### Electronic service tool
>
> - In the main electronic service tool window, verify that the data link selected in the ECM Data Source Connection drop-down matches the data link hardware being used
> - Verify the correct version is installed. The version can be determined from the main window by selecting Help, About.
> - Verify the infrared port is disabled so the serial port is **only** being used for ECM communications.
> - If you have the Palm Pilot Hot Sync Manager on a PC that **only** has one serial port, you **must** disable the Hot Sync Manager before connecting to an ECM.
>
> #### Data Link Adapters
>
> - Check the firmware version of the INLINE™ data link adapter is the latest firmware version available.
> - Verify that the data link adapter being used is compatible with the data link wiring available on the engine or vehicle.
>
> - A data link adapter is a device that converts the J1708, or J1939 data link messages from the ECM into a message that a PC can process. Because the electronic service tool is a PC based tool, a data link adapter is required to troubleshoot engines.
> - Cummins® Service Products offer the following data link adapter kits:
>
> - The following illustration shows INLINE™ data link adapters.
>
> Power for the INLINE™ data link adapters depends upon the communication setup in use. The 12 VDC power is supplied by the vehicle power system for the vehicle and engine communication setups. The 12 VDC power is supplied by an auxiliary power supply for the bench communication setup.
>
> The INLINE™ data link adapter will support either J1708 or J1939 protocol. When connecting with the electronic service tool using an INLINE™ data link adapter, the electronic service tool will attempt to establish communication with an ECM on J1939 first. If no communication is established on J1939, the electronic service tool will then attempt to establish communication on J1708.
>
> Data Link Adapter Identification Diagram - INLINE™ 4.
>
> 1. Power light
> 2. J1939 communication light
> 3. J1708 communication light
> 4. RS-232 to PC light.
>
> The INLINE™ 4 is an RP1210A compliant data link adapter that will support both J1708, and J1939 protocol. RP1210A is an industry wide standard that defines data link message format for service tools. The INLINE™ 4 **must** be configured correctly within the electronic service tool to define the COM port being used on the PC and the type of data link protocol that is available, J1708, J1939, or autodetect.
>
> Data Link Adapter Identification Diagram - INLINE™ 5.
>
> 1. Power light
> 2. J1939 communication light
> 3. J1708 communication light
> 4. RS-232 to PC light
> 5. USB to PC light.
>
> The INLINE™ 5 is an RP1210A compliant data link adapter that will support both J1708, and J1939 protocol. The adapter can be used with either a COM port or USB port. The INLINE™ 5 **must** be configured correctly within the electronic service tool to define the COM or USB port being used on the PC and the type of data link protocol that is available, J1708, or J193, or autodetect.
>
> Data Link Adapter Identification Diagram - INLINE™ 6
>
> 1. Power light
> 2. CAN 1 communication light (J1939)
> 3. CAN 2 communication light (J1939)
> 4. J1708 communication
> 5. RS-232 to PC light
> 6. USB to PC light.
>
> The INLINE™ 6 is an RP1210A compliant data link adapter that will support both J1708 and J1939 protocols. The adapter can be used with either a COM port or USB port. The INLINE™ 6 **must** be configured correctly within the electronic service tool to define the COM or USB port being used on the PC and the type of data link protocol that is available, J1708, J1939, or autodetect.
>
> Data Link Adapter Identification Diagram - INLINE™ 7
>
> 1. Power light
> 2. Communication light
> 3. Communication-type light/indicator
> 4. Fault light.
>
> The INLINE™ 7 is an RP1210A, RP1210B, and RP1210C compliant data link adapter that will support J1587/J1708 as well as J1939 (250K, 500K, or 1MB Baud Rate). The adapter can **only** be connected to the PC via USB, WIFI, or Bluetooth connection. The tool **must** be configured correctly within the electronic service tool to define the connection type on the PC and the type of data link protocol that is available, either J1587/J1708 or J1939.
>
> The INLINE™ data link adapters require firmware software in order to operate correctly. Firmware versions are updated periodically and **must** be uploaded into data link adapters when updates are released. The latest firmware version is always available on the most recent INCAL™ DVD-ROM as well as from the website http://cumminsengines.com/inline. The firmware version for a data link adapter can be found within the recommended Cummins electronic service tool or equivalent. When using the electronic service tool, the firmware version is displayed at the lower right corner of the main window when connected to an ECM. The electronic service tool **must** be connected to an ECM in order for the firmware version to be displayed.
>
> ### Setup
>
> General Information
>
> Communication with the ECM can be established at three basic locations:
>
> - Bench communication setup
> - Vehicle communication setup
> - Engine communication setup.
>
> The communication setups are described in more detail in the remainder of this procedure. Each location utilizes different data link adapter cables. All three locations require either a serial cable, USB cable, WIFI, or Bluetooth connection to interface from the data link adapter to the PC. Reference the table below.
>
> The ECM on newer engines can support data link communication on the OEM data link through the OEM connector at the ECM. The ECM can also support data link communication on the engine data link through the engine connector at the ECM. The wiring diagram for a specific engine and ECM **must** be consulted to determine if an ECM supports both OEM data link and engine data link communication.
>
> For Midrange and Heavy Duty engines, the recommended communication setup, if available, is the Cummins Inc. bench communication setup which establishes communication directly to the ECM. The bench communication setup can support both J1708 and J1939 data link protocols, when used with ECMs that support both protocols.
>
> For High Horsepower engines with multiple ECMs, the recommended communication setup is the engine communication setup through the 9 pin connector provided in the engine harness.
>
> J1939 data link communication, if available, is preferred for transferring calibrations because of less interference from other data link devices such as traction control systems and electronic dashes. J1708 communication can require extra time to disable the OEM ECMs that are also communicating on the J1708 data link in order to avoid interference from those devices. Also, the J1939 information transfer rate is faster than J1708 and a calibration download will take less time to complete using J1939 communication compared to J1708 communication.
>
> The functionality of a communication setup can be verified by testing the communication setup on a second ECM or vehicle, if available, or by completing the resistance checks defined for each setup type.
>
> The following table summarizes the ECM communication setups.
>
> | Communication Setup | Data Link Connection Location | Engine ECM data link Source | Data Link Protocols Supported |
> |---|---|---|---|
> | Bench | ECM connector | OEM | J1708, J1939 |
> | Vehicle 6 pin | Dash 6 pin connector | OEM | J1708 |
> | Vehicle 9 pin | Dash 9 pin connector | OEM | J1708, J1939 1 |
> | Engine | Engine harness 3 pin connector | Engine | J1939 |
> | Engine | Engine harness 6 pin connector | Engine | J1708 2 |
> | Engine | Engine harness 9 pin connector | Engine | J1939 3 |
>
> #### Notes:
>
> 1. The 9 pin connector **must** be fully wired to support J1939 protocol.
> 2. Available **only** on selected older engines.
> 3. Available **only** on selected High Horsepower engines.
>
> Bench Communication Setup
>
> The bench communication setup establishes communication directly with the ECM through the connector port on the ECM. An example of a bench communication setup is shown below.
>
> The bench calibration harness (1) is common for most bench setups and can be used with the appropriate bench calibration cable (5) to communicate with various ECMs. A list of available bench calibration cables (5) for various ECMs is included in Service Tool Instruction, Bulletin 3377791, which is accessible on QuickServe™ Online. Proper function of the bench calibration harness (1) and bench calibration cable (5) can be verified by using the wiring diagrams provided to complete resistance checks.
>
> Bench Communication Setup
>
> 1. Bench calibration harness, Part Number 3163151
> 2. Power supply 1
> 3. Electronic service tool
> 4. Data link adapter
> 5. ECM 1 bench calibration cable
> 6. USB cable, Part Number 4918591, or serial cable, Part Number 4918418 (reference table above for cable type)
> 7. Data link adapter cable, Part Number 3165159 (INLINE™ 4, 5, and 6
> 8. CM570 ECM (example).
>
> 1. See Service Tool Instruction, ECM Bench Calibration Base Harness, Bulletin 3377791, for part number.
>
> Vehicle Communication Setup
>
> An additional communication setup is a 9 pin or 6 pin Deutsch™ connection that is commonly located in the cab of a vehicle. The vehicle communication setup utilizes the OEM harness and connects to the ECM at the OEM connector port. A 9 pin connector in the cab, if fully wired, is capable of supporting both J1939 and J1708 protocol. Some OEMs place a 9 pin connector in the cab but do **not** provide wiring to support J1939 protocol. A 6 pin connector will **only** support J1708 protocol.
>
> On Vehicle Communication Setup
>
> 1. Data link adapter
> 2. USB cable, Part Number 4918591, or serial cable, Part Number 4918418 (reference table above for cable type)
> 3. Data link adapter cable 1
> 4. Electronic service tool
> 5. Vehicle data link adapter connector 1.
>
> 1. See Service Tool Instruction, ECM Bench Calibration Base Harness, Bulletin 3377791, for part number.
>
> INLINE™ 6 data link networks equipped to support 500K baud data link speeds require an adapter tool, Part Number 5299126, to connect to the 9 pin connector.
>
> Only the INLINE™ 6 and INLINE™ 7 are capable of supporting data link speeds of 500K baud. The INLINE™ 4 and INLINE™ 5 do **not** support 500K baud data link speeds.
>
> Engine Communication Setup
>
> The engine communication setup utilizes the engine data link provided on the engine wiring harness. Depending upon the engine, the engine communication setup available on the engine harness can be a 3 pin Deutsch™ connector, a 6 pin Deutsch™ connector, or a 9 pin Deutsch™ connector.
>
> A 3 pin Deutsch™ connector on the engine harness is available on newer engines and provides a connection point to the J1939 data link. A mini-backbone cable, which includes a 60 ohm resistor and a gender changer cable, may be required in order to connect to the ECM on the J1939 protocol. An auxiliary power supply is required for the data link adapter.
>
> 3 Pin Deutsch™ Connector
>
> 1. Data link cable 1
> 2. Power supply cable 1
> 3. Electronic service tool
> 4. Data link adapter
> 5. Gender changer cable, Part Number 3163597
> 6. Mini-backbone cable, Part Number 3163096
> 7. USB cable, Part Number 4918591, or serial cable, Part Number 4918418 (reference table above for cable type)
> 8. Engine harness 3 pin connector, Part Number 3165141.
>
> 1. See Service Tool Instruction, ECM Bench Calibration Base Harness, Bulletin 3377791, for part number.
>
> A 6 pin Deutsch™ connector is available on the engine harness for some older engines and provides a connection point to the engine J1939 data link. The 6 pin connector includes a power supply for the data link adapter.
>
> ### Resistance Check
>
> A serial cable is required to interface from the data link adapter to the PC, or a USB cable can be used with an INLINE™ 5/6/7 data link adapter.
>
> **CAUTION · Осторожно**
> Use test lead, Part Number 3822758, and test lead, Part Number 3822917, to avoid the possibility of damage to the serial cable pins.
>
> Serial Cable, Part Number 4918418
>
> 1. Open
> 2. Transmit data
> 3. Receive data
> 4. Data terminal ready (+5 VDC)
> 5. Signal ground
> 6. Open
> 7. Request to send (+5 VDC)
> 8. Clear to send
> 9. Open.
>
> - Insert a test lead into pin 1 of the female end of the serial cable, and connect lead to the multimeter probe. Attach the other test lead to pin 1 of the male end of the serial cable, and connect lead to the multimeter probe.
> - Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). Repeat the resistance measurement for pins 2 through 9. The multimeter **must** show a closed circuit (10 ohms or less) for each pin. If the circuit is **not** closed, replace the serial cable.
>
> **CAUTION · Осторожно**
> To avoid the possibility of damage to connector pins, use test lead, Part Number 3823993, on the 8 pin connector. Use test lead, Part Number 3823994, on the round 9 pin connector. Use test lead, Part Number 3824812, on the 3 pin connector.
>
> Bench Calibration Harness, Part Number 3163151
>
> 1. J1939 data link (+)
> 2. J1939 data link shield
> 3. Battery (+)
> 4. Battery (-)
> 5. Keyswitch
> 6. J1939 data link (-)
> 7. J1708 data link (+)
> 8. J1708 data link (-)
>
> - Measure the resistance from each pin in the 8 pin connector to the corresponding location in the 9 pin and/or 3 pin connector. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the bench calibration harness.
>
> **CAUTION · Осторожно**
> To avoid the possibility of damage to connector pins, use test lead, Part Number 382994, on the 8 pin connector. Determine the appropriate test lead needed for the ECM connector on the bench calibration cable.
>
> Bench Calibration Cable
>
> 1. J1939 data link (+)
> 2. J1939 data link shield
> 3. Battery (+)
> 4. Battery (-)
> 5. Keyswitch
> 6. J1939 data link (-)
> 7. J1708 data link (+)
> 8. J1708 data link (-).
> 9. ECM Connector (See wiring diagram for ECM connector pin identification).
>
> - Measure the resistance from each pin in the 8 pin connector to the corresponding location in the ECM connector. See wiring diagram for the ECM for connector pin identification. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the bench calibration cable.
>
> **CAUTION · Осторожно**
> To avoid the possibility of damage to connector pins, use male test lead, Part Number 3823993, on the 9 pin Deutsch™ connector. Use male test lead, Part Number 3822758, on the 25 pin connector.
>
> 9 Pin Data Link Cable, Part Number 3165159
>
> 9 Pin In-Cab Data Link Connector
>
> - A. Ground
> - B. Battery (+)
> - C. J1939 data link (+)
> - D. J1939 data link (-)
> - E. J1939 data link shield
> - F. J1708 data link (+)
> - G. J1708 data link (-)
> - H. Open
> - J. Open
>
> - Measure the resistance from pins A, B, C, D, E, F, and G in the 9 pin connector to the corresponding location in the 25 pin connector, as shown. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the data link cable.
>
> **CAUTION · Осторожно**
> To avoid the possibility of damage to connector pins, use male test lead, Part Number 3824811, on the 6 pin Deutsch™ connector. Use male test lead, Part Number 3822758, on the 25 pin connector.
>
> 6 Pin Data Link Cable, Part Number 3165160
>
> 6 Pin In-Cab Data Link Connector
>
> 1. J1708 data link (+)
> 2. J1708 data link (-)
> 3. Battery (+)
> 4. Open
> 5. Ground
> 6. Open.
>
> - Measure the resistance from pins A, B, C, and E in the 6 pin connector to the corresponding location in the 25 pin connector, as shown. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the data link cable.
>
> **CAUTION · Осторожно**
> To avoid the possibility of damage to the connector pins, use male test lead, Part Number 3822758, on the 25 pin connector. Use female test lead, Part Number 3823994, on the 3 pin connector. Use male test lead, Part Number 3822995, on the 2 pin power connector.
>
> 3 Pin Data Link Cable, Part Number 3165141
>
> - Measure the resistance from pins A, B, and C in the 3 pin connector to the corresponding location in the 25 pin connector, as shown. Measure the resistance from pins D and E in the 2 pin power supply connector to the corresponding location in the 5 pin connector, as shown. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the data link cable.
>
> **CAUTION · Осторожно**
> To avoid the possibility of damage to connector pins, use two male test leads, Part Number 3823993, on each 3 pin connector.
>
> Mini Backbone Cable, Part Number 3163096
>
> - Measure the resistance from pin A in one end of the backbone cable to pin A in the opposite end of the backbone cable. Repeat for pins B and C. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the backbone cable. Measure the resistance across pins A and B at either end of the cable to measure the terminating resistance. The terminating resistance value **must** measure between 50 to 70 ohms.
>
> **CAUTION · Осторожно**
> To avoid the possibility of damage to connector pins, use two female test leads, Part Number 3823994, on each 3 pin connector.
>
> Gender Changer Cable, Part Number 3163597
>
> - Measure the resistance from pin A in one end of the gender changer cable to pin A in the opposite end of the gender changer cable. Repeat for pins B and C. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the gender changer cable.
>
> **CAUTION · Осторожно**
> To avoid the possibility of damage to connector pins, use two male test leads, Part Number 3164113, on the 26 pin connector to the INLINE™ 7. Use male test lead, Part Number 3824811, on the 6 pin Deutsch™ connector. Use male test lead, Part Number 3823993, on the 9 pin Deutsch™ connector.
>
> INLINE™ 7 Data Link Cable
>
> #### 6 Pin Deutsch™ Connector Troubleshooting
>
> - Measure the resistance from pins A, B, C, and E in the 6 pin connector to the corresponding location in the 26 pin connector, as shown. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the data link cable.
>
> #### 9 Pin Deutsch™ Connector Troubleshooting
>
> - Measure the resistance from pins A, B, C, D, E, F, and G in the 9 pin connector to the corresponding location in the 26 pin connector, as shown. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the data link cable.
