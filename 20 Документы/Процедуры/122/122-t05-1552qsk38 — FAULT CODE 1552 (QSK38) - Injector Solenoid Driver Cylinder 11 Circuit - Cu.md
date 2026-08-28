---
aliases:
  - "Код 1552 (QSK38) — цепь электромагнита форсунки цилиндра 11 — ток ниже нормы или обрыв"
type: "Процедура"
doc: "122-t05-1552qsk38"
title_en: "FAULT CODE 1552 (QSK38) - Injector Solenoid Driver Cylinder 11 Circuit - Current Below Normal or Open Circuit"
title_ru: "Код 1552 (QSK38) — цепь электромагнита форсунки цилиндра 11 — ток ниже нормы или обрыв"
modified: "2019-05-31"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1552qsk38.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1552qsk38.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 1552 (QSK38) - Injector Solenoid Driver Cylinder 11 Circuit - Current Below Normal or Open Circuit
**Код 1552 (QSK38) — цепь электромагнита форсунки цилиндра 11 — ток ниже нормы или обрыв**

> [!abstract] Процедура · `122-t05-1552qsk38`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-05-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1552qsk38.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1552qsk38.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!danger] ОПАСНО
> На электромагниты форсунок при работающем двигателе подаётся высокое напряжение. Чтобы уменьшить вероятность получения травмы от поражения электрическим током, не носите ювелирные изделия или сырую одежду, а также не прикасайтесь к соленоидам форсунки или соленоидным проводам при работе двигателя.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить новый блок управления двигателем (ЭБУ), перед его заменой разберитесь со всеми остальными активными кодами неисправностей.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3824811 — пробный щуп типа штепсельной заглушки DeutschTM, номер детали 3824812 — пробный щуп типа розетки DeutschTM, номер детали 3822758 — пробный щуп типа штепсельной заглушки DeutschTM/AMPTM/Metri-PackTM, а номер детали 3822917 — пробный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте наличие активных кодов неисправностей. |  |
|  | **ШАГ 1А.** Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM. | Код ошибки 1552, 1548 или 1622 активен? |
|  | **ШАГ 1В.** Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM. |  Код 1552 неисправности активен. |
|  | **STEP 1C.** Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM. | Активны коды разломов топливных форсунок? |
| ШАГ 2. | Проверьте форсунка и форсунка соленоидный цилиндр 11 для открытой цепи. |  |
|  | **STEP 2A.** Проверить соединения жгута с проводкой двигателя. | Подключатели правильно подключены? |
|  | **STEP 2A-1.** Проверить контактные линзы электропроводки двигателя и разъема ECM. | Грязные или поврежденные контакты? |
|  | **ШАГ 2В.** Проверить наличие открытой цепи. | Сопротивление между 0,5 и 5 Ом? |
|  | **STEP 2C** Проверить контакты разъема топливного форсунка. | Грязные или поврежденные контакты? |
|  | **STEP 2D.** Проверьте наличие открытой цепи. | Сопротивление между 0,5 и 5 Ом? |
|  | **ШАГ 2Е.** Прочитайте коды ошибок. |  Код 1552 неисправности активен. |
| ШАГ 3. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 3A.** Осмотрите контактные линзы для подключения к электропроводке двигателя и форсунка соленоидный драйвер. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте форсунка соленоидных драйверов для короткого замыкания на землю. | Больше 100 тысяч ом? |
|  | **STEP 3C** Проверить жгут электропроводки двигателя. | Грязные или поврежденные контакты, или поврежденная изоляция провода? |
|  | **STEP 3C-1.** Проверьте упряжку электропроводки двигателя для короткого замыкания на землю. | Больше 100 тысяч ом? |
|  | **STEP 3C-2.** Проверьте упряжку электропроводки двигателя для короткого замыкания от контакта к контакту. | Больше 100 тысяч ом? |
| ШАГ 4. | Отключите и очистите коды ошибок. |  |
|  | **STEP 4A.** Отключить код ошибки. | Одинаковые коды разломов топливных форсунок? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте наличие активных кодов неисправностей.

#### ШАГ 1A. Считайте коды неисправностей программой INSITE™.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Управляйте двигателем и соблюдайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неисправностей. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 1552, 1548 или 1622 активен? *Да | 1В |
| Код ошибки 1552, 1548 или 1622 активен? **НЕТ** | Используйте следующую процедуру для неактивного или прерывистого кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |  |

#### ШАГ 1B. Считайте коды неисправностей программой INSITE™.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | **Код 1552 неисправности активен. *Да** | 2А |
| **Код 1552 неисправности активен. **НЕТ | 1С |  |

#### ШАГ 1C. Считайте коды неисправностей программой INSITE™.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Активны коды разломов топливных форсунок? *Да | 3А |
| Активны коды разломов топливных форсунок? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте форсунка и форсунка соленоидный цилиндр 11 для открытой цепи.

#### ШАГ 2A. Проверьте соединения жгутов для проводов двигателя.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что следующие соединения жгутов проводов для проводов двигателя правильно сделаны: Упряжка для проводов двигателя, подключенная к электропроводке двигателя ECM, подключенная к топливному форсунке соленоидного цилиндра 11 водителя. | Подключатели правильно подключены? *Да | 2А-1-1 |
| Подключатели правильно подключены? **NORepair:** Установите правильно разъёмы жгутов проводов двигателя. | 4А |  |

#### ШАГ 2A-1. Проверьте контакты разъёма электропроводки двигателя и разъема ECM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты электропроводки двигателя и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые разъемы Разъем разъема или разъема Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** Очистить разъем и штифты. Заменить поврежденный участок проводов жгутом. См. схему или схему проводов для всех соединений проводов. Ремонт ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте непрерывность в цепи 11 цилиндра двигателя соленоида форсунки. Измерить сопротивление между топливным форсункой соленоидного драйвера 11 сигнального контакта и топливным форсункой соленоидного драйвера 11 обратного контакта на цМ 60 штифтового разъёма проводов двигателя ремня. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление между 0,5 и 5 Ом? *Да | 2Е |
| Сопротивление между 0,5 и 5 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте контакты топливных форсунок.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. Отсоедините разъём жгута проводов двигателя от разъема форсунки соленоидного цилиндра водителя 11. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите проводку двигателя и форсунка соленоидного драйвера 11 разъемных контактов на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем или изоляция Поврежденные штифты блокировки разъема или изоляции Разъем разъема разъ Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** Очистить разъем и штифты. Заменить поврежденный участок проводов ремня или поврежденный форсунка. См. схему или схему проводов для всех соединений проводов. Ремонт ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. Заменить поврежденный форсунка. Используйте следующие процедуры из K38, K50, QSK38 и QSK60 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-026 в разделе 6. Используйте следующую процедуру из руководства по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-026 в разделе 6. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. Отсоедините разъём жгута проводов двигателя от разъема форсунки соленоидного цилиндра водителя 11. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте непрерывность в топливном форсунке соленоидного цилиндра 11 водителя. Измерить сопротивление между топливным форсункой соленоидного цилиндра 11 водителя сигнального контакта и топливным форсункой соленоидного цилиндра 11 водителя обратного контакта на топливном форсунке соленоидного цилиндра 11 водителя разъёма. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление между 0,5 и 5 Ом? **Ремонт:** Устранение неполадок во всех проводных упряжках, соединенных последовательно, чтобы определить, какая из них содержит открытую цепь. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом.[[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043 в разделе 19.]] | 4А |
| Сопротивление между 0,5 и 5 Ом? **NORepair:** Заменить форсунка. Используйте следующие процедуры из руководства по обслуживанию K38, K50, QSK38 и QSK50, вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]].[[28-006-026-tr — Injector\|См. процедуру 006-026 в разделе 6.]]Используйте следующую процедуру из руководства по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]].[[28-006-026-tr — Injector\|См. процедуру 006-026 в разделе 6.]] | 4А |  |

#### ШАГ 2E. Считайте коды неисправностей.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Управляйте двигателем и соблюдайте коды неисправностей. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | **Код 1552 неисправности активен. **Заменить ЭКМ. См. процедуру 019-031 в разделе 19. | 4А |
| **Код 1552 неисправности активен. **НЕТ | 4А |  |

### ШАГ 3. Проверьте жгут проводов двигателя.

#### ШАГ 3A. Осмотрите контактные линзы для подключения жгута и форсунки соленоидного водителя.

| **Условия:** Выключите замок зажигания. Отсоедините разъёмы жгута проводов двигателя от разъемов топливного форсунка для цилиндров 11, 7 и 9. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы 11, 7 и 9 разъемов для проводов двигателя и форсунки соленоидного цилиндра водителя для следующих целей: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем или изоляция Поврежденные штифты блокировки разъема или изоляции Разъем разъема разъ Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** Очистить разъем и штифты. Заменить поврежденный участок проводов ремня или поврежденный форсунка (форсунки). См. схему или схему проводов для всех соединений проводов. Ремонт ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. Заменить поврежденный форсунка. Используйте следующие процедуры из руководства по обслуживанию K38, K50, QSK38 и QSK50, вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-026 в разделе 6. Используйте следующую процедуру из руководства по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-026 в разделе 6. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте форсунка соленоидных драйверов для коротких замыканий на землю.

| **Условия:** Выключите замок зажигания. Отсоедините разъёмы жгута проводов двигателя от топливных форсунок соленоидного цилиндра водителя 11, 7 и 9 разъемов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на землю. Измерьте сопротивление между топливным форсункой соленоидного цилиндра водителя 11 сигнального контакта и заземлением блока двигателя. Измерьте сопротивление между топливным форсункой соленоидного цилиндра водителя 7 сигнального контакта и блоком двигателя заземления. Измерьте сопротивление между соленоидным цилиндром 9 двигателя и заземлением блока двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3C |
| Больше 100 тысяч ом? **NORepair:** Заменить форсунка (форсунки). Используйте следующие процедуры из руководства по обслуживанию K38, K50, QSK38 и QSK50, вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-026 в разделе 6. Используйте следующую процедуру из руководства по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-026 в разделе 6. | 4А |  |

#### ШАГ 3C. Проверьте жгут электропроводки двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы форсунки от разъемов жгута проводов двигателя. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите жгут электропроводки двигателя и разъемы ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем или изоляция Поврежденные штифты блокировки разъема или изоляции Разъем разъема разъ Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты или поврежденная изоляция провода? **Ремонт:** Заменить поврежденный участок проводов ремня или поврежденный форсунка(ы). См. схему или схему проводов для всех соединений проводов. Ремонт ремня электропроводки двигателя.[[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043 в разделе 19.]]Заменить поврежденный форсунка. Используйте следующие процедуры из руководства по обслуживанию K38, K50, QSK38 и QSK50, вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]].[[28-006-026-tr — Injector\|См. процедуру 006-026 в разделе 6.]]Используйте следующую процедуру из руководства по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]].[[28-006-026-tr — Injector\|См. процедуру 006-026 в разделе 6.]] | 4А |
| Грязные или поврежденные контакты или поврежденная изоляция провода? **НЕТ** | 3С-1-1 |  |

#### ШАГ 3C-1. Проверьте упряжку проводов двигателя для короткого замыкания на землю.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. Отсоедините форсунка соленоидный цилиндр водителя 11, 7 и 9 разъемов от разъемов жгута электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на землю. Измерить сопротивление от форсунки соленоидного цилиндра водителя 11 сигнального контакта на ЭКМ 60 штифтового разъёма проводов двигателя ремня до заземления блока двигателя. Повторите проверку на цилиндре 7 SIGNAL для водителя соленоида форсунки и на цилиндре 9 для водителя соленоида для форсунки. Измерить сопротивление от форсунки соленоидного цилиндра 11 водителя обратному контакту на цокольном разъеме ECM 60 проводов двигателя упряжке к заземлению блока двигателя. Повторите проверку для форсунки соленоидного цилиндра 7 ВПЕРЕД и форсунки соленоидного цилиндра 9 ВПЕРЕД. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3С-2 |
| Больше 100 тысяч ом? **NORepair:** Устранение неполадок во всех проводных упряжках, соединенных последовательно, для определения того, в какой из них содержится короткое замыкание. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом.[[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043 в разделе 19.]] | 4А |  |

#### ШАГ 3C-2. Проверьте упряжку проводов двигателя для контактных коротких замыканий.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. Отсоедините форсунка соленоидный цилиндр водителя 11, 7 и 9 разъемов от разъемов жгута электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание от пин-кодов до пин-кодов. Измерить сопротивление от форсунки соленоидного цилиндра 11 привода сигнального контакта на цоколе ECM 60 проводов жгута двигателя ко всем другим штифтам в разъеме. Повторите проверку на цилиндре 7 SIGNAL для водителя соленоида форсунки и на цилиндре 9 для водителя соленоида для форсунки. Измерить сопротивление от форсунки соленоидного цилиндра 11 возвратного контакта на цоколе ECM 60 проводов жгута двигателя ко всем другим цоколям в разъеме. Повторите проверку для форсунки соленоидного цилиндра 7 ВПЕРЕД и форсунки соленоидного цилиндра 9 ВПЕРЕД. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 4А |
| Больше 100 тысяч ом? **NORepair:** Устранение неполадок во всех проводных упряжках, соединенных последовательно, для определения того, какая из них содержит короткое контактное соединение. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом.[[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043 в разделе 19.]] | 4А |  |

### ШАГ 4. Отключите и очистите коды ошибок.

#### ШАГ 4A. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Запуск двигателя и холостого двигателя на 1 минуту. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кодов неисправностей. | Одинаковые коды разломов топливных форсунок? Если все шаги выполнены, то следуйте процессу технической эскалации. | Эскалация или призыв к помощи. |
| Одинаковые коды разломов топливных форсунок? **НЕТ** | 4B |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён. |
| Все коды неисправностей очищены? **NORepair:** Устранение неполадок с оставшимися кодами неисправностей. | Перейдите к соответствующим шагам устранения неполадок. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **WARNING · Опасно**
> The injector solenoids receive high voltage when the engine is operating. To reduce the possibility of personal injury from electrical shock, do not wear jewelry or damp clothing, and do not touch the injector solenoids or the solenoid wires when the engine is operating.
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3824811 - male Deutsch™ test lead, Part Number 3824812 - female Deutsch™ test lead, Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, and Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check for active fault codes. |  |
> |  | **STEP 1A.** Read the fault codes with INSITE™ electronic service tool. | Fault Code 1552, 1548, or 1622 active? |
> |  | **STEP 1B.** Read the fault codes with INSITE™ electronic service tool. | **Only** Fault Code 1552 is active? |
> |  | **STEP 1C.** Read the fault codes with INSITE™ electronic service tool. | Multiple injector fault codes active? |
> | STEP 2. | Check the injector and injector solenoid driver cylinder 11 for an open circuit. |  |
> |  | **STEP 2A.** Inspect the engine harness connections. | Connectors properly connected? |
> |  | **STEP 2A-1.** Inspect the engine harness and ECM connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check for an open circuit. | Resistance between 0.5 and 5 ohms? |
> |  | **STEP 2C.** Inspect the injector connector pins. | Dirty or damaged pins? |
> |  | **STEP 2D.** Check for an open circuit. | Resistance between 0.5 and 5 ohms? |
> |  | **STEP 2E.** Read the fault codes. | **Only** Fault Code 1552 is active? |
> | STEP 3. | Check the engine harness. |  |
> |  | **STEP 3A.** Inspect the engine harness and injector solenoid driver connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the injector solenoid drivers for a short circuit to ground. | Greater than 100k ohms? |
> |  | **STEP 3C.** Inspect the engine harness. | Dirty or damaged pins, or damaged wire insulation? |
> |  | **STEP 3C-1.** Check the engine harness for a short circuit to ground. | Greater than 100k ohms? |
> |  | **STEP 3C-2.** Check the engine harness for a pin-to-pin short circuit. | Greater than 100k ohms? |
> | STEP 4. | Disable and clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault code. | Same multiple injector fault codes active? |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check for active fault codes.
>
> #### STEP 1A. Read the fault codes with INSITE™ electronic service tool.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Operate the engine and observe the fault codes. Use INSITE™ electronic service tool to clear the fault codes. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1552, 1548, or 1622 active? **YES** | 1B |
> | Fault Code 1552, 1548, or 1622 active? **NO** | Use the following procedure for inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |
>
> #### STEP 1B. Read the fault codes with INSITE™ electronic service tool.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | **Only** Fault Code 1552 is active? **YES** | 2A |
> | **Only** Fault Code 1552 is active? **NO** | 1C |  |
>
> #### STEP 1C. Read the fault codes with INSITE™ electronic service tool.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Multiple injector fault codes active? **YES** | 3A |
> | Multiple injector fault codes active? **NO** | 2A |  |
>
> ### STEP 2. Check the injector and injector solenoid driver cylinder 11 for an open circuit.
>
> #### STEP 2A. Inspect the engine harness connections.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Make sure the following engine harness connections are properly made: Engine harness connected to ECM Engine harness connected to the injector solenoid driver cylinder 11. | Connectors properly connected? **YES** | 2A-1 |
> | Connectors properly connected? **NORepair:** Install the engine harness connectors properly. | 4A |  |
>
> #### STEP 2A-1. Inspect the engine harness and ECM connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged locking tab connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Replace the damaged section of the harness. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for continuity in the injector solenoid driver cylinder 11 circuit. Measure the resistance between the injector solenoid driver 11 SIGNAL pin and the injector solenoid driver 11 RETURN pin at the ECM 60 pin connector of the engine harness. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Resistance between 0.5 and 5 ohms? **YES** | 2E |
> | Resistance between 0.5 and 5 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Inspect the injector connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the engine harness connector from the injector solenoid driver cylinder 11 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and injector solenoid driver 11 connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire or insulation damage Damaged locking tab connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Replace the damaged section of the harness or damaged injector. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the engine harness. Refer to Procedure 019-043 in Section 19. Replace the damaged injector. Use the following procedure from the K38, K50, QSK38, and QSK60 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-026 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-026 in Section 6. | 4A |
> | Dirty or damaged pins? **NO** | 2D |  |
>
> #### STEP 2D. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the engine harness connector from the injector solenoid driver cylinder 11 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for continuity in the injector solenoid driver cylinder 11. Measure the resistance between the injector solenoid driver cylinder 11 SIGNAL pin and the injector solenoid driver cylinder 11 RETURN pin at the injector solenoid driver cylinder 11 connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Resistance between 0.5 and 5 ohms? **YESRepair:** Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |
> | Resistance between 0.5 and 5 ohms? **NORepair:** Replace the injector. Use the following procedure from the K38, K50, QSK38, and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. [[28-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. [[28-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] | 4A |  |
>
> #### STEP 2E. Read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Operate the engine and observe the fault codes. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to read the fault codes. | **Only** Fault Code 1552 is active? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |
> | **Only** Fault Code 1552 is active? **NO** | 4A |  |
>
> ### STEP 3. Check the engine harness.
>
> #### STEP 3A. Inspect the engine harness and injector solenoid driver connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connectors from the injector connectors for cylinders 11, 7, and 9. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and injector solenoid driver cylinder 11, 7, and 9 connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire or insulation damage Damaged locking tab connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Replace the damaged section of the harness or damaged injector(s). Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the engine harness. Refer to Procedure 019-043 in Section 19. Replace the damaged injector. Use the following procedure from the K38, K50, QSK38, and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-026 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-026 in Section 6. | 4A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the injector solenoid drivers for short circuits to ground.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the engine harness connectors from the injector solenoid driver cylinder 11, 7, and 9 connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground. Measure the resistance between the injector solenoid driver cylinder 11 SIGNAL pin and engine block ground. Measure the resistance between the injector solenoid driver cylinder 7 SIGNAL pin and engine block ground. Measure the resistance between the injector solenoid driver cylinder 9 SIGNAL pin and engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3C |
> | Greater than 100k ohms? **NORepair:** Replace the injector(s). Use the following procedure from the K38, K50, QSK38, and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-026 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-026 in Section 6. | 4A |  |
>
> #### STEP 3C. Inspect the engine harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the injector connectors from the engine harness connectors. Disconnect the engine harness connector from the ECM 60 pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connectors for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire or insulation damage Damaged locking tab connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins or damaged wire insulation? **YESRepair:** Replace the damaged section of the harness or damaged injector(s). Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the engine harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] Replace the damaged injector. Use the following procedure from the K38, K50, QSK38, and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. [[28-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. [[28-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] | 4A |
> | Dirty or damaged pins or damaged wire insulation? **NO** | 3C-1 |  |
>
> #### STEP 3C-1. Check the engine harness for a short circuit to ground.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the injector solenoid driver cylinder 11, 7, and 9 connectors from the engine harness connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground. Measure the resistance from the injector solenoid driver cylinder 11 SIGNAL pin at the ECM 60 pin connector of the engine harness to engine block ground. Repeat the check at the injector solenoid driver cylinder 7 SIGNAL and injector solenoid driver cylinder 9 SIGNAL pins. Measure the resistance from the injector solenoid driver cylinder 11 RETURN pin at the ECM 60 pin connector of the engine harness to engine block ground. Repeat the check for the injector solenoid driver cylinder 7 RETURN and injector solenoid driver cylinder 9 RETURN pins. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3C-2 |
> | Greater than 100k ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |  |
>
> #### STEP 3C-2. Check the engine harness for pin-to-pin short circuits.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the injector solenoid driver cylinder 11, 7, and 9 connectors from the engine harness connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin to pin. Measure the resistance from the injector solenoid driver cylinder 11 SIGNAL pin at the ECM 60 pin connector of the engine harness to all other pins in the connector. Repeat the check at the injector solenoid driver cylinder 7 SIGNAL and injector solenoid driver cylinder 9 SIGNAL pins. Measure the resistance from the injector solenoid driver cylinder 11 RETURN pin at the ECM 60 pin connector of the engine harness to all other pins in the connector. Repeat the check for the injector solenoid driver cylinder 7 RETURN and injector solenoid driver cylinder 9 RETURN pins. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 4A |
> | Greater than 100k ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the pin-to-pin short. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |  |
>
> ### STEP 4. Disable and clear the fault codes.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Start the engine and idle engine for 1 minute. Use INSITE™ electronic service tool to verify that the fault codes are inactive. | Same multiple injector fault codes active? **YESRepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance. |
> | Same multiple injector fault codes active? **NO** | 4B |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Go to the appropriate troubleshooting steps. |  |
