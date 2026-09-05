---
type: "Процедура"
doc: "178-t05-123"
title_en: "FAULT CODE 123 - Intake Manifold 1 Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
modified: "2019-08-22"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326169"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-123.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-123.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/178"
  - "перевод/машинный"
---

# FAULT CODE 123 - Intake Manifold 1 Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `178-t05-123`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326169 — QSB6.7 CM2150 B109 Fault Code Troubleshooting Manual|4326169]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-08-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-123.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-123.pdf)

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
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте следующий испытательный щуп при проведении измерения; Номер детали 3164596 - штыревой испытательный щуп FramatomeTM и Номер детали 3822917 - измерительный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить коды неисправностей датчиков. | Сенсор подает коды неисправностей активные? |
|  | **STEP 1B.** Проверить неактивный код ошибки. | Код 123 неактивен? |
| ШАГ 2. | Проверьте датчик давления впускного коллектора и схему. |  |
|  | **STEP 2A.** Осмотрите датчик давления впускного коллектора и контакты разъема. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте напряжение питания датчика и схему возврата. | Между 4,75-VDC и 5,25-VDC? |
|  | **STEP 2C.** Проверьте реакцию цепи. | Код 122 активен, а Код 123 неактивен? |
|  | **STEP 2D.** Проверьте коды неисправностей и состояние датчика. | Код 123 активен? |
| ШАГ 3. | Проверьте ECM и электропроводку двигателя. |  |
|  | **STEP 3A.** Проверить контакты разъема ECM и проводов двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 3A-1.** Проверьте напряжение питания датчика и схему возврата. | Между 4,75-VDC и 5,25-VDC? |
|  | **STEP 3A-2.** Проверьте наличие активного кода неисправности. | Код 123 неактивен? |
|  | **STEP 3B** Проверить контакты разъема электропроводки и электропроводки двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 3B-1.** Проверьте реакцию ECM. | Код 122 активен, а Код 123 неактивен? |
|  | **STEP 3B-2.** Проверьте наличие активного кода неисправности. | Код 123 неактивен? |
| ШАГ 4. | Проверьте калибровку ECM и четкие коды неисправностей. |  |
|  | **STEP 4A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 4B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте коды неисправностей датчика.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте коды неисправностей датчика. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Сенсор подает коды неисправностей активные? *Да | Соответствующее дерево симптомов устранения неполадок |
| Сенсор подает коды неисправностей активные? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте неактивный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте неактивный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неактивных ошибок. | Код 123 неактивен? *Да | Используйте следующую процедуру для кода неактивной или неактивной ошибки.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |
| Код 123 неактивен? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте датчик давления впускного коллектора и схему.

#### ШАГ 2A. Осмотрите датчик давления впускного коллектора и контакты разъема.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления впускного коллектора от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъёма датчика давления впускного коллектора и проводов двигателя на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте напряжение питания датчика и обратную цепь.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления впускного коллектора от электропроводки двигателя. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение питания и обратную цепь. Измерить напряжение от давления впускного коллектора +5 VOLT контакта подачи к контакту возврата давления впускного коллектора на разъеме датчика проводов двигателя. Используйте схему проводов для идентификации штифта и следующую процедуру для общего многометрового использования.[[99-019-359 — Multimeter Usage\|См. процедуру 019-359 в разделе 19.]] | Между 4,75-VDC и 5,25-VDC? *Да | 2C |
| Между 4,75-VDC и 5,25-VDC? **НЕТ** | 3А |  |

#### ШАГ 2C. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления впускного коллектора от электропроводки двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте отклик цепи. Поместите провод перемычки между контактом подачи впускного коллектора +5 VOLT и контактом сигнала давления впускного коллектора на разъёме датчика давления впускного коллектора проводов двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 122 активен, а Код 123 неактивен? *Да | 2D |
| Код 122 активен, а Код 123 неактивен? **НЕТ** | 3B |  |

#### ШАГ 2D. Проверьте коды неисправностей и состояние датчика.

| **Условия:** Выключите замок зажигания. Подключите датчик давления впускного коллектора к электропроводке двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 123 активен? Поврежденный датчик был обнаружен. Замените датчик. См. процедуру 019-159 в Таблице ассоциированных процедур. | 4А |
| Код 123 активен? **Норвегия: **Нет. Удаление и установка разъема исправили неисправность. | 4А |  |

### ШАГ 3. Проверьте ECM и электропроводку двигателя.

#### ШАГ 3A. Проверьте контакты разъема ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините жгут электропроводки двигателя от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъёма электропроводки двигателя и разъема двигателя ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В разъеме двигателя ECM или разъеме ремней электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3А-1-1 |  |

#### ШАГ 3A-1. Проверьте напряжение питания датчика и обратную цепь.

| **Условия:** Выключите замок зажигания. Отсоедините жгут электропроводки двигателя от разъема ECM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение питания и обратную цепь. Измерить напряжение от давления впускного коллектора +5 VOLT контакта подачи к контакту возврата давления впускного коллектора на разъеме двигателя ECM. Используйте схему проводов для идентификации штифта и следующую процедуру для общего многометрового использования.[[99-019-359 — Multimeter Usage\|См. процедуру 019-359 в разделе 19.]] | Между 4,75-VDC и 5,25-VDC? *Да | 3А-2 |
| Между 4,75-VDC и 5,25-VDC? Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 4А |  |

#### ШАГ 3A-2. Проверьте активный код ошибки.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 123 неактивен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | 4А |
| Код 123 неактивен? **NORepair: **В ремне электропроводки двигателя обнаружена открытая или короткосхемная цепь подачи. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |  |

#### ШАГ 3B. Проверьте контакты разъема ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините жгут электропроводки двигателя от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъёма электропроводки двигателя и разъема двигателя ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В разъеме двигателя ECM или разъеме ремней электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3В-1-1 |  |

#### ШАГ 3B-1. Проверьте реакцию ECM.

| **Условия:** Выключите замок зажигания. Отсоедините жгут электропроводки двигателя от разъема ECM. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте реакцию ECM. Поместите провод перемычки между контактом подачи впускного коллектора +5 VOLT и контактом сигнала давления впускного коллектора на разъеме двигателя модуля управления двигателем. См. схему или схему проводов для идентификации контакта с разъемом. Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 122 активен, а Код 123 неактивен? *Да | 3В-2-2 |
| Код 122 активен, а Код 123 неактивен? Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 4А |  |

#### ШАГ 3B-2. Проверьте активный код ошибки.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 123 неактивен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | 4А |
| Код 123 неактивен? **NORepair: **Открытая схема или короткое замыкание контакт-контакт было обнаружено на проводе SIGNAL ремня электропроводки двигателя. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |  |

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
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB7 CM2880 B117 | 4358390 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG11 CM2880 G106 | 4332695 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG12 CM2880 G107 | 4332690 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG11 CM2880 G108 | 4332901 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG12 CM2880 G109 | 4332906 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSNT14 CM876 N102 | 4325993 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF2.8 CM2880 F104 | 4332741 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF2.8 CM2880 F108 | 4332746 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL8.9 CM2880 L112 | 4358493 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF3.8 CM2880 F112 | 4383825 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB5.9 CM2880 B127 | 4383645 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF3.8 CM2220 F116 | 4383664 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSL9.3 CM2880 L113 | 4383811 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSC8.3 CM2880 C102 | 4388785 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB5.9 CM2880 B139 | 4388870 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB3.9 CM2880 B138 | 5411050 |
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
| Жгут проводов двигателя | См. процедуру 019-043 | ISB3.9 CM2220 B107 | 4310792 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB4.5 CM2150 B108 | 4326163 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB6.7 CM2880 B117 | 4358390 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG11 CM2880 G106 | 4332695 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG12 CM2880 G107 | 4332690 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG11 CM2880 G108 | 4332901 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG12 CM2880 G109 | 4332906 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSNT14 CM876 N102 | 4325993 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSF2.8 CM2880 F104 | 4332741 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSF2.8 CM2880 F108 | 4332746 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISL8.9 CM2880 L112 | 4358493 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSF3.8 CM2880 F112 | 4383825 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISB5.9 CM2880 B127 | 4383645 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISF3.8 CM2220 F116 | 4383664 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSL9.3 CM2880 L113 | 4383811 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSC8.3 CM2880 C102 | 4388785 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB5.9 CM2880 B139 | 4388870 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB3.9 CM2880 B138 | 5411050 |
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
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISL9.5 CM2150 SN | 4310608 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISB3.9 CM2220 B107 | 4310792 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | QSB4.5 CM2150 B108 | 4326163 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | QSB7 CM2880 B117 | 4358390 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISG11 CM2880 G106 | 4332695 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISG12 CM2880 G107 | 4332690 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISG11 CM2880 G108 | 4332901 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISG12 CM2880 G109 | 4332906 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | QSNT14 CM876 N102 | 4325993 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | QSF2.8 CM2880 F104 | 4332741 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | QSF2.8 CM2880 F108 | 4332746 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISL8.9 CM2880 L112 | 4358493 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | QSF3.8 CM2880 F112 | 4383825 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISB5.9 CM2880 B127 | 4383645 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISF3.8 CM2220 F116 | 4383664 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | QSL9.3 CM2880 L113 | 4383811 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | QSC8.3 CM2880 C102 | 4388785 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | QSB5.9 CM2880 B139 | 4388870 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | QSB3.9 CM2880 B138 | 5411050 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISD6.7 CM2880 D101 | 5411372 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISF2.8 CM2220 F129 | 5411325 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISF4.5 CM2220 F123 | 5411320 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | QSG12 CM2880 G112 | 4388731 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | ISF3.8 CM2220 F134B | 5504165 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | Z14 M2670 Z103B | 5504577 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | D6.7 CM2670 D102B | 5504515 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | B6.2 CM2670 B156B | 5579510 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | X12 CM2670 X121B | 5504455 |
| Датчик давления и температуры впускного коллектора | См. процедуру 019-159 | L9 CM2670 L128B | 5504589 |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement; Part Number 3164596 - male Framatome™ test lead and Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for sensor supply fault codes. | Sensor supply fault codes active? |
> |  | **STEP 1B.** Check for an inactive fault code. | Fault Code 123 inactive? |
> | STEP 2. | Check the intake manifold pressure sensor and circuit. |  |
> |  | **STEP 2A.** Inspect the intake manifold pressure sensor and connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the sensor supply voltage and return circuit. | Between 4.75-VDC and 5.25-VDC? |
> |  | **STEP 2C.** Check the circuit response. | Fault Code 122 active and Fault Code 123 inactive? |
> |  | **STEP 2D.** Check the fault codes and verify sensor condition. | Fault Code 123 active? |
> | STEP 3. | Check the ECM and engine harness. |  |
> |  | **STEP 3A.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3A-1.** Check the sensor supply voltage and return circuit. | Between 4.75-VDC and 5.25-VDC? |
> |  | **STEP 3A-2.** Check for an active fault code. | Fault Code 123 inactive? |
> |  | **STEP 3B.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B-1.** Check the ECM response. | Fault Code 122 active and Fault Code 123 inactive? |
> |  | **STEP 3B-2.** Check for an active fault code. | Fault Code 123 inactive? |
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
> | Check for sensor supply fault codes. Use INSITE™ electronic service tool to read the fault codes. | Sensor supply fault codes active? **YES** | Appropriate troubleshooting symptom tree |
> | Sensor supply fault codes active? **NO** | 1B |  |
>
> #### STEP 1B. Check for an inactive fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for inactive fault code. Use INSITE™ electronic service tool to read the inactive fault codes. | Fault Code 123 inactive? **YES** | Use the following procedure for inactive or intemittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |
> | Fault Code 123 inactive? **NO** | 2A |  |
>
> ### STEP 2. Check the intake manifold pressure sensor and circuit.
>
> #### STEP 2A. Inspect the intake manifold pressure sensor and connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the intake manifold pressure sensor from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and intake manifold pressure sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the sensor supply voltage and return circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the intake manifold pressure sensor from the engine harness. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply voltage and return circuit. Measure the voltage from the intake manifold pressure +5 VOLT SUPPLY pin to the intake manifold pressure RETURN pin at the sensor connector of the engine harness. Use a wiring diagram for pin identification and the following procedure for general multimeter usage. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Between 4.75-VDC and 5.25-VDC? **YES** | 2C |
> | Between 4.75-VDC and 5.25-VDC? **NO** | 3A |  |
>
> #### STEP 2C. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the intake manifold pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the circuit response. Place a jumper wire between the intake manifold pressure +5 VOLT SUPPLY pin and the intake manifold pressure SIGNAL pin at the intake manifold pressure sensor connector of the engine harness. Refer to the circuit diagram or the wiring diagram for connector pin identification. Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 122 active and Fault Code 123 inactive? **YES** | 2D |
> | Fault Code 122 active and Fault Code 123 inactive? **NO** | 3B |  |
>
> #### STEP 2D. Check the fault codes and verify sensor condition.
>
> | **Conditions:** Turn keyswitch OFF. Connect the intake manifold pressure sensor to the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 123 active? **YESRepair:** A damaged sensor has been detected. Replace the sensor. Refer to Procedure 019-159 in the Associated Procedures Table. | 4A |
> | Fault Code 123 active? **NORepair:** None. The removal and installation of the connector corrected the fault. | 4A |  |
>
> ### STEP 3. Check the ECM and engine harness.
>
> #### STEP 3A. Inspect the ECM and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM engine connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM engine connector or engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
> | Dirty or damaged pins? **NO** | 3A-1 |  |
>
> #### STEP 3A-1. Check the sensor supply voltage and return circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply voltage and return circuit. Measure the voltage from the intake manifold pressure +5 VOLT SUPPLY pin to the intake manifold pressure RETURN pin at the ECM engine connector. Use a wiring diagram for pin identification and the following procedure for general multimeter usage. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Between 4.75-VDC and 5.25-VDC? **YES** | 3A-2 |
> | Between 4.75-VDC and 5.25-VDC? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 4A |  |
>
> #### STEP 3A-2. Check for an active fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 123 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
> | Fault Code 123 inactive? **NORepair:** An open or shorted supply circuit has been detected in the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |  |
>
> #### STEP 3B. Inspect the ECM and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM engine connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM engine connector or engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
> | Dirty or damaged pins? **NO** | 3B-1 |  |
>
> #### STEP 3B-1. Check the ECM response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ECM response. Place a jumper wire between the intake manifold pressure +5 VOLT SUPPLY pin and the intake manifold pressure SIGNAL pin at the engine control module engine connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Check the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 122 active and Fault Code 123 inactive? **YES** | 3B-2 |
> | Fault Code 122 active and Fault Code 123 inactive? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 4A |  |
>
> #### STEP 3B-2. Check for an active fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 123 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
> | Fault Code 123 inactive? **NORepair:** An open circuit or a pin-to-pin short circuit has been detected on the SIGNAL wire of the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |  |
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
> | Engine Control Module | Refer to Procedure 019-031 | QSB7 CM2880 B117 | 4358390 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G106 | 4332695 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G107 | 4332690 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G108 | 4332901 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G109 | 4332906 |
> | Engine Control Module | Refer to Procedure 019-031 | QSNT14 CM876 N102 | 4325993 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F104 | 4332741 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F108 | 4332746 |
> | Engine Control Module | Refer to Procedure 019-031 | ISL8.9 CM2880 L112 | 4358493 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF3.8 CM2880 F112 | 4383825 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB5.9 CM2880 B127 | 4383645 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F116 | 4383664 |
> | Engine Control Module | Refer to Procedure 019-031 | QSL9.3 CM2880 L113 | 4383811 |
> | Engine Control Module | Refer to Procedure 019-031 | QSC8.3 CM2880 C102 | 4388785 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB5.9 CM2880 B139 | 4388870 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB3.9 CM2880 B138 | 5411050 |
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
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISB3.9 CM2220 B107 | 4310792 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB4.5 CM2150 B108 | 4326163 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB6.7 CM2880 B117 | 4358390 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG11 CM2880 G106 | 4332695 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG12 CM2880 G107 | 4332690 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG11 CM2880 G108 | 4332901 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG12 CM2880 G109 | 4332906 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSNT14 CM876 N102 | 4325993 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSF2.8 CM2880 F104 | 4332741 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSF2.8 CM2880 F108 | 4332746 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISL8.9 CM2880 L112 | 4358493 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSF3.8 CM2880 F112 | 4383825 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISB5.9 CM2880 B127 | 4383645 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISF3.8 CM2220 F116 | 4383664 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSL9.3 CM2880 L113 | 4383811 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSC8.3 CM2880 C102 | 4388785 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB5.9 CM2880 B139 | 4388870 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB3.9 CM2880 B138 | 5411050 |
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
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISL9.5 CM2150 SN | 4310608 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISB3.9 CM2220 B107 | 4310792 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSB4.5 CM2150 B108 | 4326163 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSB7 CM2880 B117 | 4358390 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISG11 CM2880 G106 | 4332695 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISG12 CM2880 G107 | 4332690 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISG11 CM2880 G108 | 4332901 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISG12 CM2880 G109 | 4332906 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSNT14 CM876 N102 | 4325993 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSF2.8 CM2880 F104 | 4332741 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSF2.8 CM2880 F108 | 4332746 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISL8.9 CM2880 L112 | 4358493 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSF3.8 CM2880 F112 | 4383825 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISB5.9 CM2880 B127 | 4383645 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISF3.8 CM2220 F116 | 4383664 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSL9.3 CM2880 L113 | 4383811 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSC8.3 CM2880 C102 | 4388785 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSB5.9 CM2880 B139 | 4388870 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSB3.9 CM2880 B138 | 5411050 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISD6.7 CM2880 D101 | 5411372 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISF2.8 CM2220 F129 | 5411325 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISF4.5 CM2220 F123 | 5411320 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSG12 CM2880 G112 | 4388731 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISF3.8 CM2220 F134B | 5504165 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | Z14 CM2670 Z103B | 5504577 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | D6.7 CM2670 D102B | 5504515 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | B6.2 CM2670 B156B | 5579510 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | X12 CM2670 X121B | 5504455 |
> | Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | L9 CM2670 L128B | 5504589 |
