---
type: "Процедура"
doc: "178-t05-135"
title_en: "FAULT CODE 135 - Engine Oil Rifle Pressure 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2019-08-22"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326169"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-135.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-135.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/178"
  - "перевод/машинный"
---

# FAULT CODE 135 - Engine Oil Rifle Pressure 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `178-t05-135`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326169 — QSB6.7 CM2150 B109 Fault Code Troubleshooting Manual|4326169]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-08-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-135.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-135.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
> Чтобы не повредить новый блок управления двигателем (ЭБУ), перед его заменой разберитесь со всеми остальными активными кодами неисправностей.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3164596 — штыревой пробный щуп FramatomeTM и номер детали 3822917 — пробный щуп типа сокет DeutschTM/AMPTM/Metri-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить коды неисправностей датчиков. | Сенсор подает коды неисправностей активные? |
|  | **STEP 1B.** Проверить неактивный код ошибки. | Код 135 неактивен? |
| ШАГ 2. | Проверьте датчик давления масла и схему. |  |
|  | **STEP 2A** Проверить датчик давления масла и контакты разъема. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте реакцию цепи. | Код 141 активен, а Код 135 неактивен? |
|  | **STEP 2C** Проверьте напряжение питания датчика и схему возврата. | 4.7 VDC и 5.25 VDC. |
|  | **STEP 2D.** Проверьте коды неисправностей и состояние датчика. | Код 135 ошибки активен? |
| ШАГ 3. | Проверьте ECM и электропроводку двигателя. |  |
|  | **STEP 3A.** Проверить контакты разъема ECM и проводов двигателя. | Грязные или поврежденные контакты? |
|  | **СТЭП 3А-1** Проверить реакцию на ЭКО. | Код 141 активен, а Код 135 неактивен? |
|  | **STEP 3A-2.** Проверьте наличие активного кода неисправности. | Код 135 неактивен? |
|  | **STEP 3B** Проверить контакты разъема электропроводки и электропроводки двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 3B-1.** Проверьте напряжение питания датчика и схему возврата | 4,75 VDC и 5,25 VDC? |
|  | **STEP 3B-2.** Проверьте наличие активного кода неисправности. | Код 135 неактивен? |
| ШАГ 4. | Проверьте калибровку ECM и четкие коды неисправностей. |  |
|  | **STEP 4A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 4B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте коды неисправностей датчика.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте коды неисправностей датчика. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Сенсор подает коды неисправностей активные? *Да | Соответствующий код неисправности дерево |
| Сенсор подает коды неисправностей активные? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте неактивный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте неактивный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 135 неактивен? *Да | Используйте следующую процедуру для неактивного или прерывистого кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |
| Код 135 неактивен? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте датчик давления масла и схему.

#### ШАГ 2A. Проверьте датчик давления масла и контакты разъема.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления масла от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы разъёма электропроводки двигателя и датчика давления масла на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема повреждено Утепление провода Поврежден разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления масла от электропроводки двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 141 активен, а Код 135 неактивен? *Да | 2C |
| Код 141 активен, а Код 135 неактивен? **НЕТ** | 3А |  |

#### ШАГ 2C. Проверьте напряжение питания датчика и обратную цепь.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления масла от электропроводки двигателя. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение питания и обратную цепь. Измерьте напряжение от контакта подачи масла +5 VOLT до обратного контакта давления масла на разъеме датчика проводов двигателя. Используйте схему проводов для идентификации штифта и следующую процедуру для общего многометрового использования.[[99-019-359 — Multimeter Usage\|См. процедуру 019-359 в разделе 19.]] | 4,75 VDC и 5,25 VDC? *Да | 2D |
| 4,75 VDC и 5,25 VDC? **НЕТ** | 3B |  |

#### ШАГ 2D. Проверьте коды неисправностей и состояние датчика.

| **Условия:** Выключите замок зажигания. Подключите датчик давления масла к электропроводке двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 135 ошибки активен? Поврежденный датчик был обнаружен. Замените датчик давления масла. См. процедуру 019-066 в Таблице ассоциированных процедур. | 4А |
| Код 135 ошибки активен? **Норвегия: **Нет. Удаление и установка разъема исправили неисправность. | 4А |  |

### ШАГ 3. Проверьте ECM и электропроводку двигателя.

#### ШАГ 3A. Проверьте контакты разъема ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъёма электропроводки двигателя и разъема двигателя ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема повреждено Утепление провода Поврежден разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В разъеме двигателя ECM или разъеме ремней электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3А-1-1 |  |

#### ШАГ 3A-1. Проверьте реакцию ECM.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 141 активен, а Код 135 неактивен? *Да | 3А-2 |
| Код 141 активен, а Код 135 неактивен? Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 4А |  |

#### ШАГ 3A-2. Проверьте активный код ошибки.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 135 неактивен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | 4А |
| Код 135 неактивен? **NORepair: **На проводе SIGNAL ремня электропроводки двигателя обнаружено короткое замыкание от контакта к контакту. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |  |

#### ШАГ 3B. Проверьте контакты разъема ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъёма электропроводки двигателя и разъема двигателя ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема повреждено Утепление провода Поврежден разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В разъеме двигателя ECM или разъеме ремней электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3В-1-1 |  |

#### ШАГ 3B-1. Проверьте напряжение питания датчика и обратную цепь.

| **Условия:** Выключите замок зажигания. Отсоедините жгут электропроводки двигателя от разъема двигателя ECM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение питания и обратную цепь. Измерьте напряжение от контакта подачи масла +5 VOLT до обратного контакта давления масла на разъеме двигателя ECM. См. схему или схему проводов для идентификации контакта с разъемом. | 4,75 VDC и 5,25 VDC? *Да | 3В-2-2 |
| 4,75 VDC и 5,25 VDC? Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 4А |  |

#### ШАГ 3B-2. Проверьте активный код ошибки.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 135 неактивен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | 4А |
| Код 135 неактивен? **NORepair:** В ремне электропроводки двигателя обнаружена схема открытого возврата. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |  |

### ШАГ 4. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 4A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 4B |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]] | 1А |  |

#### ШАГ 4B. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да | Ремонт завершён |
| Код неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

## Связанные процедуры

| Связанные процедуры |  |  |  |
|---|---|---|---|
| Название процедуры | Процедурный номер | Модельный сервис | Номер бюллетеня |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL9.5 CM2150 SN | 4310608 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB3.9 CM2220 B107 | 4310792 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB4.5 CM2150 B108 | 4326163 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG11 CM2880 G106 | 4332695 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG12 CM2880 G107 | 4332690 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG11 CM2880 G108 | 4332901 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG12 CM2880 G109 | 4332906 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSNT14 CM876 N102 | 4325993 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL8.9 CM2880 L112 | 4358493 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB5.9 CM2880 B127 | 4383645 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSL9.3 CM2880 L113 | 4383811 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSC8.3 CM2880 C102 | 4388785 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB5.9 CM2880 B139 | 4388870 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB3.9 CM2880 B138 | 5411050 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISD6.7 CM2880 D101 | 5411372 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSG12 CM2880 G112 | 4388731 |
| Электронный блок управления двигателем | См. процедуру 019-031 | Z14 M2670 Z103B | 5504577 |
| Электронный блок управления двигателем | См. процедуру 019-031 | D6.7 CM2670 D102B | 5504515 |
| Электронный блок управления двигателем | См. процедуру 019-031 | B6.2 CM2670 B156B | 5579510 |
| Электронный блок управления двигателем | См. процедуру 019-031 | X12 CM2670 X121B | 5504455 |
| Электронный блок управления двигателем | См. процедуру 019-031 | L9 CM2670 L128B | 5504589 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISL9.5 CM2150 SN | 4310608 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISB3.9 CM2220 B107 | 4310792 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB4.5 CM2150 B108 | 4326163 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG11 CM2880 G106 | 4332695 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG12 CM2880 G107 | 4332690 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG11 CM2880 G108 | 4332901 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG12 CM2880 G109 | 4332906 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSNT14 CM876 N102 | 4325993 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISL8.9 CM2880 L112 | 4358493 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISB5.9 CM2880 B127 | 4383645 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSL9.3 CM2880 L113 | 4383811 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSC8.3 CM2880 C102 | 4388785 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB5.9 CM2880 B139 | 4388870 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB3.9 CM2880 B138 | 5411050 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISD6.7 CM2880 D101 | 5411372 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSG12 CM2880 G112 | 4388731 |
| Жгут проводов двигателя | См. процедуру 019-043 | Z14 M2670 Z103B | 5504577 |
| Жгут проводов двигателя | См. процедуру 019-043 | D6.7 CM2670 D102B | 5504515 |
| Жгут проводов двигателя | См. процедуру 019-043 | B6.2 CM2670 B156B | 5579510 |
| Жгут проводов двигателя | См. процедуру 019-043 | X12 CM2670 X121B | 5504455 |
| Жгут проводов двигателя | См. процедуру 019-043 | L9 CM2670 L128B | 5504589 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | ISL9.5 CM2150 SN | 4310608 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | ISB3.9 CM2220 B107 | 4310792 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | QSB4.5 CM2150 B108 | 4326163 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | ISG11 CM2880 G106 | 4332695 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | ISG12 CM2880 G107 | 4332690 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | ISG11 CM2880 G108 | 4332901 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | ISG12 CM2880 G109 | 4332906 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | QSNT14 CM876 N102 | 4325993 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | ISL8.9 CM2880 L112 | 4358493 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | QSL9.3 CM2880 L113 | 4383811 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | QSC8.3 CM2880 C102 | 4388785 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | QSB3.9 CM2880 B138 | 5411050 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | QSB5.9 CM2880 B139 | 4388870 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | ISD6.7 CM2880 D101 | 5411372 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | QSG12 CM2880 G112 | 4388731 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | Z14 M2670 Z103B | 5504577 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | D6.7 CM2670 D102B | 5504515 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | B6.2 CM2670 B156B | 5579510 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | X12 CM2670 X121B | 5504455 |
| Датчик давления моторного масла / коммутатор | См. процедуру 019-066 | L9 CM2670 L128B | 5504589 |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3164596 - male Framatome™ test lead and Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for sensor supply fault codes. | Sensor supply fault codes active? |
> |  | **STEP 1B.** Check for an inactive fault code. | Fault Code 135 inactive? |
> | STEP 2. | Check the oil pressure sensor and circuit. |  |
> |  | **STEP 2A.** Inspect the oil pressure sensor and connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the circuit response. | Fault Code 141 active and Fault Code 135 inactive? |
> |  | **STEP 2C.** Check the sensor supply voltage and return circuit. | Between 4.7 VDC and 5.25 VDC? |
> |  | **STEP 2D.** Check the fault codes and verify sensor condition. | Fault Code 135 active? |
> | STEP 3. | Check the ECM and engine harness. |  |
> |  | **STEP 3A.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3A-1.** Check the ECM response. | Fault Code 141 active and Fault Code 135 inactive? |
> |  | **STEP 3A-2.** Check for an active fault code. | Fault Code 135 inactive? |
> |  | **STEP 3B.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B-1.** Check the sensor supply voltage and return circuit | Between 4.75 VDC and 5.25 VDC? |
> |  | **STEP 3B-2.** Check for an active fault code. | Fault Code 135 inactive? |
> | STEP 4. | Check ECM calibration and clear fault codes. |  |
> |  | **STEP 4A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 4B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for sensor supply fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for sensor supply fault codes. Use INSITE™ electronic service tool to read the fault codes. | Sensor supply fault codes active? **YES** | Appropriate fault code troubleshooting tree |
> | Sensor supply fault codes active? **NO** | 1B |  |
>
> #### STEP 1B. Check for an inactive fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an inactive fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 135 inactive? **YES** | Use the following procedure for inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |
> | Fault Code 135 inactive? **NO** | 2A |  |
>
> ### STEP 2. Check the oil pressure sensor and circuit.
>
> #### STEP 2A. Inspect the oil pressure sensor and connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the oil pressure sensor from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and oil pressure sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Dirt or debris in or on the connector pins Missing or damaged connector seals Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the oil pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 141 active and Fault Code 135 inactive? **YES** | 2C |
> | Fault Code 141 active and Fault Code 135 inactive? **NO** | 3A |  |
>
> #### STEP 2C. Check the sensor supply voltage and return circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the oil pressure sensor from the engine harness. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply voltage and return circuit. Measure the voltage from the oil pressure +5 VOLT SUPPLY pin to the oil pressure RETURN pin at the sensor connector of the engine harness. Use a wiring diagram for pin identification and the following procedure for general multimeter usage. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Between 4.75 VDC and 5.25 VDC? **YES** | 2D |
> | Between 4.75 VDC and 5.25 VDC? **NO** | 3B |  |
>
> #### STEP 2D. Check the fault codes and verify sensor condition.
>
> | **Conditions:** Turn keyswitch OFF. Connect the oil pressure sensor to the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 135 active? **YESRepair:** A damaged sensor has been detected. Replace the oil pressure sensor. Refer to Procedure 019-066 in the Associated Procedures Table. | 4A |
> | Fault Code 135 active? **NORepair:** None. The removal and installation of the connector corrected the fault. | 4A |  |
>
> ### STEP 3. Check the ECM and engine harness.
>
> #### STEP 3A. Inspect the ECM and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM engine connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Dirt or debris in or on the connector pins Missing or damaged connector seals Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM engine connector or engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
> | Dirty or damaged pins? **NO** | 3A-1 |  |
>
> #### STEP 3A-1. Check the ECM response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 141 active and Fault Code 135 inactive? **YES** | 3A-2 |
> | Fault Code 141 active and Fault Code 135 inactive? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 4A |  |
>
> #### STEP 3A-2. Check for an active fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 135 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
> | Fault Code 135 inactive? **NORepair:** A pin-to-pin short circuit has been detected on the SIGNAL wire of the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |  |
>
> #### STEP 3B. Inspect the ECM and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM engine connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Dirt or debris in or on the connector pins Missing or damaged connector seals Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM engine connector or engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
> | Dirty or damaged pins? **NO** | 3B-1 |  |
>
> #### STEP 3B-1. Check the sensor supply voltage and return circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM engine connector. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply voltage and return circuit. Measure the voltage from the oil pressure +5 VOLT SUPPLY pin to the oil pressure RETURN pin at the ECM engine connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Between 4.75 VDC and 5.25 VDC? **YES** | 3B-2 |
> | Between 4.75 VDC and 5.25 VDC? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 4A |  |
>
> #### STEP 3B-2. Check for an active fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 135 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
> | Fault Code 135 inactive? **NORepair:** An open return circuit has been detected in the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |  |
>
> ### STEP 4. Check ECM calibration and clear fault codes.
>
> #### STEP 4A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 4B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 1A |  |
>
> #### STEP 4B. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete |
> | Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> ## Associated Procedures
>
> | Associated Procedures |  |  |  |
> |---|---|---|---|
> | Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
> | Engine Control Module | Refer to Procedure 019-031 | ISL9.5 CM2150 SN | 4310608 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB3.9 CM2220 B107 | 4310792 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB4.5 CM2150 B108 | 4326163 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
> | Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G106 | 4332695 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G107 | 4332690 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G108 | 4332901 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G109 | 4332906 |
> | Engine Control Module | Refer to Procedure 019-031 | QSNT14 CM876 N102 | 4325993 |
> | Engine Control Module | Refer to Procedure 019-031 | ISL8.9 CM2880 L112 | 4358493 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB5.9 CM2880 B127 | 4383645 |
> | Engine Control Module | Refer to Procedure 019-031 | QSL9.3 CM2880 L113 | 4383811 |
> | Engine Control Module | Refer to Procedure 019-031 | QSC8.3 CM2880 C102 | 4388785 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB5.9 CM2880 B139 | 4388870 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB3.9 CM2880 B138 | 5411050 |
> | Engine Control Module | Refer to Procedure 019-031 | ISD6.7 CM2880 D101 | 5411372 |
> | Engine Control Module | Refer to Procedure 019-031 | QSG12 CM2880 G112 | 4388731 |
> | Engine Control Module | Refer to Procedure 019-031 | Z14 CM2670 Z103B | 5504577 |
> | Engine Control Module | Refer to Procedure 019-031 | D6.7 CM2670 D102B | 5504515 |
> | Engine Control Module | Refer to Procedure 019-031 | B6.2 CM2670 B156B | 5579510 |
> | Engine Control Module | Refer to Procedure 019-031 | X12 CM2670 X121B | 5504455 |
> | Engine Control Module | Refer to Procedure 019-031 | L9 CM2670 L128B | 5504589 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISL9.5 CM2150 SN | 4310608 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISB3.9 CM2220 B107 | 4310792 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB4.5 CM2150 B108 | 4326163 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG11 CM2880 G106 | 4332695 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG12 CM2880 G107 | 4332690 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG11 CM2880 G108 | 4332901 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG12 CM2880 G109 | 4332906 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSNT14 CM876 N102 | 4325993 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISL8.9 CM2880 L112 | 4358493 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISB5.9 CM2880 B127 | 4383645 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSL9.3 CM2880 L113 | 4383811 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSC8.3 CM2880 C102 | 4388785 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB5.9 CM2880 B139 | 4388870 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB3.9 CM2880 B138 | 5411050 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISD6.7 CM2880 D101 | 5411372 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSG12 CM2880 G112 | 4388731 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | Z14 CM2670 Z103B | 5504577 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | D6.7 CM2670 D102B | 5504515 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | B6.2 CM2670 B156B | 5579510 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | X12 CM2670 X121B | 5504455 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | L9 CM2670 L128B | 5504589 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | ISL9.5 CM2150 SN | 4310608 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | ISB3.9 CM2220 B107 | 4310792 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | QSB4.5 CM2150 B108 | 4326163 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | ISG11 CM2880 G106 | 4332695 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | ISG12 CM2880 G107 | 4332690 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | ISG11 CM2880 G108 | 4332901 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | ISG12 CM2880 G109 | 4332906 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | QSNT14 CM876 N102 | 4325993 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | ISL8.9 CM2880 L112 | 4358493 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | QSL9.3 CM2880 L113 | 4383811 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | QSC8.3 CM2880 C102 | 4388785 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | QSB3.9 CM2880 B138 | 5411050 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | QSB5.9 CM2880 B139 | 4388870 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | ISD6.7 CM2880 D101 | 5411372 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | QSG12 CM2880 G112 | 4388731 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | Z14 CM2670 Z103B | 5504577 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | D6.7 CM2670 D102B | 5504515 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | B6.2 CM2670 B156B | 5579510 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | X12 CM2670 X121B | 5504455 |
> | Engine Oil Pressure Sensor/Switch | Refer to Procedure 019-066 | L9 CM2670 L128B | 5504589 |
