---
type: "Процедура"
doc: "178-t05-272"
title_en: "FAULT CODE 272 - Engine Fuel Pump Pressurizing Assembly 1 Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2019-08-22"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326169"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-272.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-272.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/178"
  - "перевод/машинный"
---

# FAULT CODE 272 - Engine Fuel Pump Pressurizing Assembly 1 Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `178-t05-272`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326169 — QSB6.7 CM2150 B109 Fault Code Troubleshooting Manual|4326169]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-08-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-272.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-272.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822758 - пробный щуп типа пробки DeutschTM/AMPTM/Metri-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить наличие активного кода неисправности. | Код 272 ошибки активен или неактивен, если за последние 25 часов работы двигателя было зарегистрировано более одного счета? |
| ШАГ 2. | Проверьте привод топливного насоса и схему. |  |
|  | **STEP 2A.** Проверить привод топливного насоса и контакты разъема. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте реакцию цепи. | Код 271 активен, а Код 272 неактивен? |
|  | **STEP 2C** Проверить коды неисправностей и состояние привода топливного насоса. | Код 272 активен? |
| ШАГ 3. | Проверьте модуль управления двигателем (ECM) и электропроводку двигателя. |  |
|  | **STEP 3A.** Проверить контакты разъема ECM и проводов двигателя. | Грязные или поврежденные контакты? |
|  | **СТЭП 3В.** Проверить реакцию ECM. | Код 271 активен, а Код 272 неактивен? |
|  | **STEP 3C.** Проверьте наличие открытой цепи в ремне электропроводки двигателя. | Менее 10 Ом? |
|  | **STEP 3D.** Проверьте короткое замыкание в контактной проводах двигателя. | Больше 100 тысяч ом? |
|  | **STEP 3E.** Проверить неактивный код ошибки. | Код 272 неактивен? |
| ШАГ 4. | Проверьте калибровку ECM и четкие коды неисправностей. |  |
|  | **STEP 4A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 4B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 272 ошибки активен или неактивен, если за последние 25 часов работы двигателя было зарегистрировано более одного счета? *Да | 2А |
| Код 272 ошибки активен или неактивен, если за последние 25 часов работы двигателя было зарегистрировано более одного счета? **НЕТ** | Используйте следующую процедуру для неактивного или прерывистого кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |  |

### ШАГ 2. Проверьте привод топливного насоса и схему.

#### ШАГ 2A. Проверьте контакты с жгутом и разъемом привода двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините привод топливного насоса от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты ремня электропроводки двигателя и разъема привода для следующего: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В разъеме привода или разъеме ремней электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Подожди 30 секунд. Отсоедините привод топливного насоса от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте отклик цепи. Поместите провод перемычки между контактом сигнала привода топливного насоса и обратным контактом привода топливного насоса на разъеме привода топливного насоса проводов двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. Используйте схему или схему проводов для идентификации контакта с разъемом. Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 271 активен, а Код 272 неактивен? *Да | 2C |
| Код 271 активен, а Код 272 неактивен? **НЕТ** | 3А |  |

#### ШАГ 2C. Проверьте коды неисправностей и состояние привода топливного насоса.

| **Условия:** Выключите замок зажигания. Подключите привод топливного насоса к ремню электропроводки двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 272 активен? **Ремонт:** Поврежденный привод топливного насоса обнаружен. Заменить привод топливного насоса. См. процедуру 019-117 в Таблице ассоциированных процедур. | 4А |
| Код 272 активен? **Норвегия: **Нет. Удаление и установка разъема исправили неисправность. | 4А |  |

### ШАГ 3. Проверьте ECM и электропроводку двигателя.

#### ШАГ 3A. Проверьте контакты разъема ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините жгут электропроводки двигателя от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты электропроводки двигателя и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? Поврежденное соединение было обнаружено в разъеме ECM или разъеме электропроводки оригинального производителя оборудования (OEM). Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъёмы или штифты.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]] | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте реакцию ECM.

| **Условия:** Выключите замок зажигания. Отсоедините жгут электропроводки двигателя от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте отклик цепи. Поместите провод перемычки между контактом сигнала привода топливного насоса и приводом топливного насоса ВПЕРЕДУЙТЕ на разъеме двигателя ECM. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. Используйте схему или схему проводов для идентификации контакта с разъемом. Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 271 активен, а Код 272 неактивен? *Да | 3C |
| Код 271 активен, а Код 272 неактивен? Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 4А |  |

#### ШАГ 3C. Проверьте наличие открытой цепи в ремне электропроводки двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините жгут электропроводки двигателя от разъема ECM. Отсоедините привод топливного насоса от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление между контактом сигнала привода топливного насоса на разъеме ECM электропроводки ремня и контактом сигнала привода топливного насоса на разъеме привода топливного насоса электропроводки двигателя. Измерить сопротивление между обратным контактом привода топливного насоса на разъеме ECM электропроводки ремня и обратным контактом привода топливного насоса на разъеме привода топливного насоса электропроводки двигателя. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 3D |
| Менее 10 Ом? **NORepair:** Ремонтировать или заменить электропроводку двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |  |

#### ШАГ 3D. Проверьте короткое замыкание контакт-контакт в ремне электропроводки двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините жгут электропроводки двигателя от разъема ECM. Отсоедините привод топливного насоса от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание контакт-контакт на одном разъеме. Измерьте сопротивление между контактом сигнала привода топливного насоса в разъёме электропроводки двигателя ECM и всеми другими штифтами в разъёме. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3E |
| Больше 100 тысяч ом? **NORepair:** Ремонтировать или заменить электропроводку двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |  |

#### ШАГ 3E. Проверьте неактивный код ошибки.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 272 неактивен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | 4А |
| Код 272 неактивен? Следует повторять процедуры устранения неполадок с самого начала. Режим отказа должен был быть обнаружен. | 1А |  |

### ШАГ 4. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 4A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 4B |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]] | 4B |  |

#### ШАГ 4B. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да | Ремонт завершён. |
| Код неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

## Связанные процедуры

| Связанные процедуры |  |  |  |
|---|---|---|---|
| Название процедуры | Процедурный номер | Модельный сервис | Номер бюллетеня |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL9.5 CM2150 SN | 4310608 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB4.5 CM2150 B108 | 4326163 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB7 CM2880 B117 | 4358390 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG11 CM2880 G106 | 4332695 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG12 CM2880 G107 | 4332690 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG11 CM2880 G108 | 4332901 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG12 CM2880 G109 | 4332906 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF2.8 CM2880 F104 | 4332741 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF2.8 CM2880 F108 | 4332746 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL8.9 CM2880 L112 | 4358493 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF3.8 CM2880 F112 | 4383825 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSL9.3 CM2880 L113 | 4383811 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISD6.7 CM2880 D101 | 5411372 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF2.8 CM2220 F129 | 5411325 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF4.5 CM2220 F123 | 5411320 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSG12 CM2880 G112 | 4388731 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF3.8 CM2220 F134B | 5504165 |
| Электронный блок управления двигателем | См. процедуру 019-031 | Z14 M2670 Z103B | 5504577 |
| Электронный блок управления двигателем | См. процедуру 019-031 | D6.7 CM2670 D102B | 5504515 |
| Электронный блок управления двигателем | См. процедуру 019-031 | B6.2 CM2670 B156B | 5579510 |
| Электронный блок управления двигателем | См. процедуру 019-031 | X12 CM2670 X121B | 5504455 |
| Электронный блок управления двигателем | См. процедуру 019-031 | L9 CM2670 L128B | 5504589 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISL9.5 CM2150 SN | 4310608 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB4.5 CM2150 B108 | 4326163 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB7 CM2880 B117 | 4358390 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG11 CM2880 G106 | 4332695 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG12 CM2880 G107 | 4332690 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG11 CM2880 G108 | 4332901 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG12 CM2880 G109 | 4332906 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSF2.8 CM2880 F104 | 4332741 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSF2.8 CM2880 F108 | 4332746 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISL8.9 CM2880 L112 | 4358493 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSF3.8 CM2880 F112 | 4383825 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSL9.3 CM2880 L113 | 4383811 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISD6.7 CM2880 D101 | 5411372 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISF2.8 CM2220 F129 | 5411325 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISF4.5 CM2220 F123 | 5411320 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSG12 CM2880 G112 | 4388731 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISF3.8 CM2220 F134B | 5504165 |
| Жгут проводов двигателя | См. процедуру 019-043 | Z14 M2670 Z103B | 5504577 |
| Жгут проводов двигателя | См. процедуру 019-043 | D6.7 CM2670 D102B | 5504515 |
| Жгут проводов двигателя | См. процедуру 019-043 | B6.2 CM2670 B156B | 5579510 |
| Жгут проводов двигателя | См. процедуру 019-043 | X12 CM2670 X121B | 5504455 |
| Жгут проводов двигателя | См. процедуру 019-043 | L9 CM2670 L128B | 5504589 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | ISL9.5 CM2150 SN | 4310608 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | QSB4.5 CM2150 B108 | 4326163 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | QSB7 CM2880 B117 | 4358390 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | ISG11 CM2880 G106 | 4332695 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | ISG12 CM2880 G107 | 4332690 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | ISG11 CM2880 G108 | 4332901 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | ISG12 CM2880 G109 | 4332906 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | QSF2.8 CM2880 F104 | 4332741 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | QSF2.8 CM2880 F108 | 4332746 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | ISL8.9 CM2880 L112 | 4358493 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | QSF3.8 CM2880 F112 | 4383825 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | QSL9.3 CM2880 L113 | 4383811 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | ISD6.7 CM2880 D101 | 5411372 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | ISF2.8 CM2220 F129 | 5411325 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | ISF4.5 CM2220 F123 | 5411320 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | QSG12 CM2880 G112 | 4388731 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | ISF3.8 CM2220 F134B | 5504165 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | Z14 M2670 Z103B | 5504577 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | D6.7 CM2670 D102B | 5504515 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | B6.2 CM2670 B156B | 5579510 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | X12 CM2670 X121B | 5504455 |
| Исполнительный механизм топливного насоса | См. процедуру 019-117 | L9 CM2670 L128B | 5504589 |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for an active fault code. | Fault Code 272 active or inactive with more than one count logged in the last 25 engine hours? |
> | STEP 2. | Check the fuel pump actuator and circuit. |  |
> |  | **STEP 2A.** Inspect the fuel pump actuator and connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the circuit response. | Fault Code 271 active and Fault Code 272 inactive? |
> |  | **STEP 2C.** Check the fault codes and verify fuel pump actuator condition. | Fault Code 272 active? |
> | STEP 3. | Check the engine control module (ECM) and engine harness. |  |
> |  | **STEP 3A.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the ECM response. | Fault Code 271 active and Fault Code 272 inactive? |
> |  | **STEP 3C.** Check for an open circuit in the engine harness. | Less than 10 ohms? |
> |  | **STEP 3D.** Check for a pin-to-pin short circuit in the engine harness. | Greater than 100k ohms? |
> |  | **STEP 3E.** Check for an inactive fault code. | Fault Code 272 inactive? |
> | STEP 4. | Check ECM calibration and clear fault codes. |  |
> |  | **STEP 4A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 4B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for an active fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 272 active or inactive with more than one count logged in the last 25 engine hours? **YES** | 2A |
> | Fault Code 272 active or inactive with more than one count logged in the last 25 engine hours? **NO** | Use the following procedure for an inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |
>
> ### STEP 2. Check the fuel pump actuator and circuit.
>
> #### STEP 2A. Inspect the engine harness and actuator connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the fuel pump actuator from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and actuator connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the actuator connector or engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Wait 30 seconds. Disconnect the fuel pump actuator from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the circuit response. Place a jumper wire between the fuel pump actuator SIGNAL pin and the fuel pump actuator RETURN pin at the fuel pump actuator connector of the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. Use the circuit diagram or the wiring diagram for connector pin identification. Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 271 active and Fault Code 272 inactive? **YES** | 2C |
> | Fault Code 271 active and Fault Code 272 inactive? **NO** | 3A |  |
>
> #### STEP 2C. Check the fault codes and verify fuel pump actuator condition.
>
> | **Conditions:** Turn keyswitch OFF. Connect the fuel pump actuator to the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 272 active? **YESRepair:** A damaged fuel pump actuator has been detected. Replace the fuel pump actuator. Refer to Procedure 019-117 in the Associated Procedures Table. | 4A |
> | Fault Code 272 active? **NORepair:** None. The removal and installation of the connector corrected the fault. | 4A |  |
>
> ### STEP 3. Check the ECM and engine harness.
>
> #### STEP 3A. Inspect the ECM and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or original equipment manufacturer (OEM) harness connector. Clean the connector and pins. Repair the damaged harness, connectors, or pins, if possible. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the ECM response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the circuit response. Place a jumper wire between the fuel pump actuator SIGNAL pin and the fuel pump actuator RETURN at the ECM engine connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. Use the circuit diagram or the wiring diagram for connector pin identification. Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 271 active and Fault Code 272 inactive? **YES** | 3C |
> | Fault Code 271 active and Fault Code 272 inactive? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 4A |  |
>
> #### STEP 3C. Check for an open circuit in the engine harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. Disconnect the fuel pump actuator from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the fuel pump actuator SIGNAL pin at the ECM connector of the engine harness and the fuel pump actuator SIGNAL pin at the fuel pump actuator connector of the engine harness. Measure the resistance between the fuel pump actuator RETURN pin at the ECM connector of the engine harness and the fuel pump actuator RETURN pin at the fuel pump actuator connector of the engine harness. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3D |
> | Less than 10 ohms? **NORepair:** Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |  |
>
> #### STEP 3D. Check for a pin-to-pin short circuit in the engine harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. Disconnect the fuel pump actuator from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short circuit on one connector. Measure the resistance between the fuel pump actuator SIGNAL pin in the engine harness ECM connector and all other pins in the connector. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3E |
> | Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |  |
>
> #### STEP 3E. Check for an inactive fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 272 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
> | Fault Code 272 inactive? **NORepair:** Troubleshooting procedures need to be repeated from the beginning. A failure mode should have been detected. | 1A |  |
>
> ### STEP 4. Check ECM calibration and clear fault codes.
>
> #### STEP 4A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 4B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 4B |  |
>
> #### STEP 4B. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
> | Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> ## Associated Procedures
>
> | Associated Procedures |  |  |  |
> |---|---|---|---|
> | Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
> | Engine Control Module | Refer to Procedure 019-031 | ISL9.5 CM2150 SN | 4310608 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB4.5 CM2150 B108 | 4326163 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
> | Engine Control Module | Refer to Procedure 019-031 | QSB7 CM2880 B117 | 4358390 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G106 | 4332695 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G107 | 4332690 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G108 | 4332901 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G109 | 4332906 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F104 | 4332741 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F108 | 4332746 |
> | Engine Control Module | Refer to Procedure 019-031 | ISL8.9 CM2880 L112 | 4358493 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF3.8 CM2880 F112 | 4383825 |
> | Engine Control Module | Refer to Procedure 019-031 | QSL9.3 CM2880 L113 | 4383811 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Engine Control Module | Refer to Procedure 019-031 | ISD6.7 CM2880 D101 | 5411372 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF2.8 CM2220 F129 | 5411325 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF4.5 CM2220 F123 | 5411320 |
> | Engine Control Module | Refer to Procedure 019-031 | QSG12 CM2880 G112 | 4388731 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F134B | 5504165 |
> | Engine Control Module | Refer to Procedure 019-031 | Z14 CM2670 Z103B | 5504577 |
> | Engine Control Module | Refer to Procedure 019-031 | D6.7 CM2670 D102B | 5504515 |
> | Engine Control Module | Refer to Procedure 019-031 | B6.2 CM2670 B156B | 5579510 |
> | Engine Control Module | Refer to Procedure 019-031 | X12 CM2670 X121B | 5504455 |
> | Engine Control Module | Refer to Procedure 019-031 | L9 CM2670 L128B | 5504589 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISL9.5 CM2150 SN | 4310608 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB4.5 CM2150 B108 | 4326163 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB7 CM2880 B117 | 4358390 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG11 CM2880 G106 | 4332695 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG12 CM2880 G107 | 4332690 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG11 CM2880 G108 | 4332901 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG12 CM2880 G109 | 4332906 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSF2.8 CM2880 F104 | 4332741 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSF2.8 CM2880 F108 | 4332746 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISL8.9 CM2880 L112 | 4358493 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSF3.8 CM2880 F112 | 4383825 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSL9.3 CM2880 L113 | 4383811 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISD6.7 CM2880 D101 | 5411372 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISF2.8 CM2220 F129 | 5411325 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISF4.5 CM2220 F123 | 5411320 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSG12 CM2880 G112 | 4388731 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISF3.8 CM2220 F134B | 5504165 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | Z14 CM2670 Z103B | 5504577 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | D6.7 CM2670 D102B | 5504515 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | B6.2 CM2670 B156B | 5579510 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | X12 CM2670 X121B | 5504455 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | L9 CM2670 L128B | 5504589 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | ISL9.5 CM2150 SN | 4310608 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | QSB4.5 CM2150 B108 | 4326163 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | QSB7 CM2880 B117 | 4358390 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | ISG11 CM2880 G106 | 4332695 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | ISG12 CM2880 G107 | 4332690 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | ISG11 CM2880 G108 | 4332901 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | ISG12 CM2880 G109 | 4332906 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | QSF2.8 CM2880 F104 | 4332741 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | QSF2.8 CM2880 F108 | 4332746 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | ISL8.9 CM2880 L112 | 4358493 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | QSF3.8 CM2880 F112 | 4383825 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | QSL9.3 CM2880 L113 | 4383811 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | ISD6.7 CM2880 D101 | 5411372 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | ISF2.8 CM2220 F129 | 5411325 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | ISF4.5 CM2220 F123 | 5411320 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | QSG12 CM2880 G112 | 4388731 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | ISF3.8 CM2220 F134B | 5504165 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | Z14 CM2670 Z103B | 5504577 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | D6.7 CM2670 D102B | 5504515 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | B6.2 CM2670 B156B | 5579510 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | X12 CM2670 X121B | 5504455 |
> | Fuel Pump Actuator | Refer to Procedure 019-117 | L9 CM2670 L128B | 5504589 |
