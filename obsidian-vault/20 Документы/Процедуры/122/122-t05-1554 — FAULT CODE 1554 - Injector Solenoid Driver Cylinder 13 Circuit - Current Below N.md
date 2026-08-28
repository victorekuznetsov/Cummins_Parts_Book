---
aliases:
  - "Код 1554 — цепь электромагнита форсунки цилиндра 13 — ток ниже нормы или обрыв"
type: "Процедура"
doc: "122-t05-1554"
title_en: "FAULT CODE 1554 - Injector Solenoid Driver Cylinder 13 Circuit - Current Below Normal or Open Circuit"
title_ru: "Код 1554 — цепь электромагнита форсунки цилиндра 13 — ток ниже нормы или обрыв"
modified: "2019-06-04"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1554.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1554.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 1554 - Injector Solenoid Driver Cylinder 13 Circuit - Current Below Normal or Open Circuit
**Код 1554 — цепь электромагнита форсунки цилиндра 13 — ток ниже нормы или обрыв**

> [!abstract] Процедура · `122-t05-1554`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-06-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1554.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1554.pdf)

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
|  | **ШАГ 1А.** Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM. | Код 324 и 1554 активен? |
|  | **ШАГ 1В.** Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM. | * Действует только код 1554 ошибки. |
|  | **STEP 1C.** Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM. | Активны коды разломов топливных форсунок? |
| ШАГ 2. | Проверьте схему 13 цилиндра двигателя соленоида форсунки для открытой цепи. |  |
|  | **STEP 2A.** Проверить соединения жгута с проводкой двигателя. | Подключатели правильно подключены? |
|  | **STEP 2A-1.** Проверить контактные линзы для проводов двигателя и разъема ECM | Грязные или поврежденные контакты? |
|  | **ШАГ 2В.** Проверить наличие открытой цепи. | Сопротивление между 0,5 и 5 Ом? |
|  | **STEP 2C** Проверить контакты разъема топливного форсунка. | Грязные или поврежденные контакты? |
|  | **STEP 2D.** Проверьте наличие открытой цепи. | Сопротивление между 0,5 и 5 Ом? |
|  | **ШАГ 2Е.** Прочитайте коды ошибок. | * Действует только код 1554 ошибки. |
| ШАГ 3. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 3A.** Осмотрите контактные линзы для подключения к электропроводке двигателя и форсунка соленоидный драйвер. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте двигатель соленоида форсунки на короткое замыкание на землю. | Больше 100 тысяч ом? |
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
| Управляйте двигателем и соблюдайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неисправностей Запустите двигатель и запустите его на холостом ходу в течение одной минуты. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 324 или 1554 активен? *Да | 1В |
| Код ошибки 324 или 1554 активен? **НЕТ** | Используйте следующую процедуру для неактивного или прерывистого кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |  |

#### ШАГ 1B. Считайте коды неисправностей программой INSITE™.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | *** Действует только код 1554 ошибки. *Да** | 2А |
| *** Действует только код 1554 ошибки. **НЕТ | 1С |  |

#### ШАГ 1C. Считайте коды неисправностей программой INSITE™.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Активны коды разломов топливных форсунок? *Да | 3А |
| Активны коды разломов топливных форсунок? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте схему 13 цилиндра двигателя соленоида форсунки для открытой цепи.

#### ШАГ 2A. Проверьте соединения жгутов для проводов двигателя.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что следующие соединения жгутов проводов для проводов двигателя правильно сделаны: Упряжка для проводов двигателя, подключенная к электропроводке двигателя ECM, подключенная к топливному форсунке соленоидного цилиндра 13 водителя. | Подключатели правильно подключены? *Да | 2А-1-1 |
| Подключатели правильно подключены? **НЕТ** | 4А |  |

#### ШАГ 2A-1. Проверьте контакты разъёма электропроводки двигателя и разъема ECM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем электропроводки ремня от разъема ECM 69-pin. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы электропроводки двигателя и разъёма ECM 69-pin для следующих целей: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые разъемы Разъем разъема или разъема Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? *** Ремонт:** Очистить разъем и штифты. Заменить поврежденный участок проводов жгутом. См. схему или схему проводов для всех соединений проводов. Ремонт ремня электропроводки двигателя.[[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043 в разделе 19.]] | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Измерить сопротивление между топливным форсункой соленоидного цилиндра 13 сигнального контакта и топливным форсункой соленоидного цилиндра 13 возвратного контакта у разъема ECM проводов двигателя жгута проводов. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общей техники измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление между 0,5 и 5 Ом? *Да | 2Е |
| Сопротивление между 0,5 и 5 Ом? **NORepair:** Установите правильно разъёмы жгутов проводов двигателя. | 2C |  |

#### ШАГ 2C. Проверьте контакты топливных форсунок.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. Отсоедините разъём жгута проводов двигателя от разъема форсунки соленоидного цилиндра водителя 13. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы разъема 13 двигателя и форсунки соленоидного водителя для следующих целей: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые разъемы Разъем разъема или разъема Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? *** Ремонт:** Очистить разъем и штифты. Заменить поврежденный участок проводов ремня или поврежденный форсунка. См. схему или схему проводов для всех соединений проводов. Ремонт ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. Заменить поврежденный форсунка (форсунки). Используйте следующие процедуры из руководства по обслуживанию K38, K50, QSK38 и QSK50, вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-026 в разделе 6. Используйте следующую процедуру из руководства по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-026 в разделе 6. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. Отсоедините разъём жгута проводов двигателя от разъема форсунки соленоидного цилиндра водителя 13. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте непрерывность в топливном форсунке соленоидного цилиндра 13. Измерить сопротивление между топливным форсункой соленоидного цилиндра 13 сигнального контакта и топливным форсункой соленоидного цилиндра 13 возвратного контакта у форсунки соленоидного разъема водителя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление между 0,5 и 5 Ом? **Ремонт:** Устранение неполадок во всех проводных упряжках, соединенных последовательно, чтобы определить, какая из них содержит открытую цепь. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом.[[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043 в разделе 19.]] | 4А |
| Сопротивление между 0,5 и 5 Ом? **NORepair:** Заменить поврежденный форсунка (форсунки). Используйте следующие процедуры из руководства по обслуживанию K38, K50, QSK38 и QSK50, вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-026 в разделе 6. Используйте следующую процедуру из руководства по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-026 в разделе 6. | 4А |  |

#### ШАГ 2E. Считайте коды неисправностей.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Управляйте двигателем и соблюдайте коды неисправностей. Используйте инструмент электронного обслуживания INSITETM для очистки кодов неисправностей Запустите двигатель и запустите его на холостом ходу в течение 1 минуты Используйте инструмент электронного обслуживания INSITETM для считывания кодов неисправностей. | *** Действует только код 1554 ошибки. *** Заменить ЭКМ. См. процедуру 019-031 в разделе 19. | 4А |
| *** Действует только код 1554 ошибки. **НЕТ | 4А |  |

### ШАГ 3. Проверьте жгут проводов двигателя.

#### ШАГ 3A. Проверьте контакты разъёма проводов двигателя и топливного форсунка.

| **Условия:** Выключите замок зажигания. Отсоедините форсунка соленоидного цилиндра водителя 3 и 13 разъемов от разъемов электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите проводку двигателя и форсунка соленоидного цилиндра водителя 3 и 13 соединительных контактов на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые разъемы Разъем разъема или разъема Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? *** Ремонт:** Очистить разъем и штифты. Заменить поврежденный участок ремня электропроводки двигателя или поврежденный форсунка (форсунки). См. схему или схему проводов fro всех соединений проводов. Ремонт ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. Заменить поврежденный форсунка (форсунки). Используйте следующую процедуру из руководства по обслуживанию K38, K50, QSK38 и QSK50, Вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-026 в разделе 6. Используйте следующую процедуру из руководства по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-026 в разделе 6. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте соленоиды форсунки для короткого замыкания на землю.

| **Условия:** Выключите замок зажигания. Отсоедините форсунка соленоидного цилиндра водителя 3 и 13 разъемов от разъемов электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на землю. Измерьте сопротивление между соленоидным водителем 3-го форсунки и заземлением блока двигателя. Измерить сопротивление между топливным форсункой соленоидного водителя 13 сигнального контакта и блоком двигателя заземления. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3C |
| Больше 100 тысяч ом? **NORepair:** Заменить поврежденный форсунка (форсунки). Используйте следующую процедуру из руководства по обслуживанию K38, K50, QSK38 и QSK50, Вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-026 в разделе 6. Используйте следующую процедуру из руководства по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-026 в разделе 6. | 4А |  |

#### ШАГ 3C. Проверьте жгут электропроводки двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините форсунка соленоидного цилиндра водителя 3 и 13 разъемов от разъемов электропроводки двигателя. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите жгут электропроводки двигателя и разъемы ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые разъемы Разъем разъема или разъема Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты, или поврежденная изоляция провода? *** Ремонт:** Заменить поврежденный участок проводов ремня или поврежденный форсунка(ы). См. схему или схему проводов для всех соединений проводов. Ремонт ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. Заменить поврежденный форсунка (форсунки). Используйте следующую процедуру из руководства по обслуживанию K38, K50, QSK38 и QSK50, Вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-026 в разделе 6. Используйте следующую процедуру из руководства по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-026 в разделе 6. | 4А |
| Грязные или поврежденные контакты, или поврежденная изоляция провода? **НЕТ** | 3С-1-1 |  |

#### ШАГ 3C-1. Проверьте упряжку проводов двигателя для короткого замыкания на землю.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. Отсоедините форсунка соленоидного цилиндра водителя 3 и 13 разъемов от разъемов электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на землю. Измерить сопротивление от форсунки соленоидного цилиндра водителя 3 сигнального контакта на разъеме ECM проводов двигателя упряжкой к заземлению блока двигателя. Повторите проверку на соленоидном цилиндре 13 форсунки. Измерить сопротивление от форсунки соленоидного цилиндра водителя 3 обратного контакта на разъеме ECM проводов двигателя упряжкой к заземлению блока двигателя. Повторите проверку на наличие у форсунки соленоидного цилиндра 13 возвратного контакта. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч омов? *Да | 3С-2 |
| Больше 100 тысяч ом? **NORepair:** Устранение неполадок во всех проводных упряжках, соединенных последовательно, для определения того, в какой из них содержится короткое замыкание. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом.[[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043 в разделе 19.]] | 4А |  |

#### ШАГ 3C-2. Проверьте упряжку проводов двигателя для короткого замыкания «контакт-контакт».

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема ECM 60 контактов. Отсоедините форсунка соленоидного цилиндра водителя 3 и 13 разъемов от разъемов электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание контакт-контакт. Измерить сопротивление от форсунки соленоидного цилиндра водителя 3 сигнального контакта на разъеме ECM проводов двигателя жгута ко всем другим штифтам в разъеме. Повторите проверку на соленоидном цилиндре 13 форсунки. Измерить сопротивление от форсунки соленоидного цилиндра водителя 3 обратного контакта на разъеме ECM проводов двигателя жгута проводов ко всем другим штифтам в разъеме. Повторите проверку на наличие у форсунки соленоидного цилиндра 13 возвратного контакта. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Тогда графа 100к Ом? *Да | 4А |
| Тогда больше 100 тысяч ом? **NORepair:** Устранение неполадок во всех проводных упряжках, соединенных последовательно, для определения того, какая из них содержит короткое контактное соединение. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом.[[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043 в разделе 19.]] | 4А |  |

### ШАГ 4. Отключите и очистите коды ошибок.

#### ШАГ 4A. Отключите коды неисправностей.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте инструмент Insite для проверки неактивности кодов неисправностей. | Одинаковые коды разломов топливных форсунок? Если все шаги выполнены, то следуйте процессу технической эскалации. | Эскалация или призыв к помощи. |
| Одинаковые коды разломов топливных форсунок? **НЕТ** | 4B |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент Insite для очистки неактивных кодов неисправностей. | Все коды неисправностей очищены? *Да | Ремонт завершён. |
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
> |  | **STEP 1A.** Read the fault codes with INSITE™ electronic service tool. | Fault Code 324 and 1554 active? |
> |  | **STEP 1B.** Read the fault codes with INSITE™ electronic service tool. | **Only** Fault Code 1554 is active? |
> |  | **STEP 1C.** Read the fault codes with INSITE™ electronic service tool. | Multiple injector fault codes active? |
> | STEP 2. | Check the injector solenoid driver cylinder 13 circuit for an open circuit. |  |
> |  | **STEP 2A.** Inspect the engine harness connections. | Connectors properly connected? |
> |  | **STEP 2A-1.** Inspect the engine harness and ECM connector pins | Dirty or damaged pins? |
> |  | **STEP 2B.** Check for an open circuit. | Resistance between 0.5 and 5 ohms? |
> |  | **STEP 2C.** Inspect the injector connector pins. | Dirty or damaged pins? |
> |  | **STEP 2D.** Check for an open circuit. | Resistance between 0.5 and 5 ohms? |
> |  | **STEP 2E.** Read the fault codes. | **Only** Fault Code 1554 is active? |
> | STEP 3. | Check the engine harness. |  |
> |  | **STEP 3A.** Inspect the engine harness and injector solenoid driver connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the injector solenoid driver for a short circuit to ground. | Greater than 100k ohms? |
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
> | Operate the engine and observe the fault codes. Use INSITE™ electronic service tool to clear the fault codes Start the engine and let it idle for one minute. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 324 or 1554 active? **YES** | 1B |
> | Fault Code 324 or 1554 active? **NO** | Use the following procedure for inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |
>
> #### STEP 1B. Read the fault codes with INSITE™ electronic service tool.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | **Only** Fault Code 1554 is active? **YES** | 2A |
> | **Only** Fault Code 1554 is active? **NO** | 1C |  |
>
> #### STEP 1C. Read the fault codes with INSITE™ electronic service tool.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Multiple injector fault codes active? **YES** | 3A |
> | Multiple injector fault codes active? **NO** | 2A |  |
>
> ### STEP 2. Check the injector solenoid driver cylinder 13 circuit for an open circuit.
>
> #### STEP 2A. Inspect the engine harness connections.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Make sure the following engine harness connections are properly made: Engine harness connected to ECM Engine harness connected to the injector solenoid driver cylinder 13. | Connectors properly connected? **YES** | 2A-1 |
> | Connectors properly connected? **NO** | 4A |  |
>
> #### STEP 2A-1. Inspect the engine harness and ECM connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 69-pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM 69-pin connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged locking tab connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Replace the damaged section of the harness. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the engine harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Measure the resistance between the injector solenoid driver cylinder 13 SIGNAL pin and the injector solenoid driver cylinder 13 RETURN pin at the ECM connector of the engine harness. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement technique. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Resistance between 0.5 and 5 ohms? **YES** | 2E |
> | Resistance between 0.5 and 5 ohms? **NORepair:** Install the engine harness connectors properly. | 2C |  |
>
> #### STEP 2C. Inspect the injector connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the engine harness connector from the injector solenoid driver cylinder 13 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and injector solenoid driver cylinder 13 connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged locking tab connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Replace the damaged section of the harness or damaged injector. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the engine harness. Refer to Procedure 019-043 in Section 19. Replace the damaged injector(s). Use the following procedure from the K38, K50, QSK38, and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-026 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-026 in Section 6. | 4A |
> | Dirty or damaged pins? **NO** | 2D |  |
>
> #### STEP 2D. Check for an open circuit.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the engine harness connector from the injector solenoid driver cylinder 13 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for continuity in the injector solenoid driver cylinder 13. Measure the resistance between the injector solenoid driver cylinder 13 SIGNAL pin and the injector solenoid driver cylinder 13 RETURN pin at the injector solenoid driver connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Resistance between 0.5 and 5 ohms? **YESRepair:** Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |
> | Resistance between 0.5 and 5 ohms? **NORepair:** Replace the damaged injector(s). Use the following procedure from the K38, K50, QSK38, and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-026 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-026 in Section 6. | 4A |  |
>
> #### STEP 2E. Read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect the INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Operate the engine and observe the fault codes. Use INSITE™ electronic service tool to clear the fault codes Start the engine and let it idle for 1 minute Use INSITE™ electronic service tool to read the fault codes. | **Only** Fault Code 1554 is active? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |
> | **Only** Fault Code 1554 is active? **NO** | 4A |  |
>
> ### STEP 3. Check the engine harness.
>
> #### STEP 3A. Inspect the engine harness and injector connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the injector solenoid driver cylinder 3 and 13 connectors from the engine harness connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and injector solenoid driver cylinder 3 and 13 connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged locking tab connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Replace the damaged section of the engine harness or damaged injector(s). Refer to the circuit diagram or wiring diagram fro all harness interconnections. Repair the engine harness. Refer to Procedure 019-043 in Section 19. Replace the damaged injector(s). Use the following procedure from the K38, K50, QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-026 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-026 in Section 6. | 4A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the injector solenoids for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the injector solenoid driver cylinder 3 and 13 connectors from the engine harness connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground. Measure the resistance between the injector solenoid driver 3 SIGNAL pin and engine block ground. Measure the resistance between the injector solenoid driver 13 SIGNAL pin and engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3C |
> | Greater than 100k ohms? **NORepair:** Replace the damaged injector(s). Use the following procedure from the K38, K50, QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-026 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-026 in Section 6. | 4A |  |
>
> #### STEP 3C. Inspect the engine harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the injector solenoid driver cylinder 3 and 13 connectors from the engine harness connectors. Disconnect the engine harness connector from the ECM 60 pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connectors for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged locking tab connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in section 19.]] | Dirty or damaged pins, or damaged wire insulation? **YESRepair:** Replace the damaged section of the harness or damaged injector(s). Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the engine harness. Refer to Procedure 019-043 in Section 19. Replace the damaged injector(s). Use the following procedure from the K38, K50, QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-026 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-026 in Section 6. | 4A |
> | Dirty or damaged pins, or damaged wire insulation? **NO** | 3C-1 |  |
>
> #### STEP 3C-1. Check the engine harness for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the injector solenoid driver cylinder 3 and 13 connectors from the engine harness connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground. Measure the resistance from the injector solenoid driver cylinder 3 SIGNAL pin at the ECM connector of the engine harness to engine block ground. Repeat the check at the injector solenoid driver cylinder 13 SIGNAL pin. Measure the resistance from the injector solenoid driver cylinder 3 RETURN pin at the ECM connector of the engine harness to engine block ground. Repeat the check for the injector solenoid driver cylinder 13 RETURN pin. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater the 100k ohms? **YES** | 3C-2 |
> | Greater than 100k ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |  |
>
> #### STEP 3C-2. Check the engine harness for a pin-to-pin short circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pins connector. Disconnect the injector solenoid driver cylinder 3 and 13 connectors from the engine harness connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short circuit. Measure the resistance from the injector solenoid driver cylinder 3 SIGNAL pin at the ECM connector of the engine harness to all other pins in the connector. Repeat the check at the injector solenoid driver cylinder 13 SIGNAL pin. Measure the resistance from the injector solenoid driver cylinder 3 RETURN pin at the ECM connector of the engine harness to all other pins in the connector. Repeat the check for the injector solenoid driver cylinder 13 RETURN pin. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Grater then 100k ohms? **YES** | 4A |
> | Greater then 100k ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the pin-to-pin short. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |  |
>
> ### STEP 4. Disable and clear the fault codes.
>
> #### STEP 4A. Disable the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Start the engine and let it idle for 1 minute. Use INSITE electronic service tool to verify that the fault codes are inactive. | Same multiple injector fault codes active? **YESRepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance. |
> | Same multiple injector fault codes active? **NO** | 4B |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Go to the appropriate troubleshooting steps. |  |
