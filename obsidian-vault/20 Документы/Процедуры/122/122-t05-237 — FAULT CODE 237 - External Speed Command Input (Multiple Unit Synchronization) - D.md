---
aliases:
  - "Код 237 — внешний вход задания частоты (синхронизация агрегатов) — данные нестабильны или неверны"
type: "Процедура"
doc: "122-t05-237"
title_en: "FAULT CODE 237 - External Speed Command Input (Multiple Unit Synchronization) - Data Erratic, Intermittent, or Incorrect"
title_ru: "Код 237 — внешний вход задания частоты (синхронизация агрегатов) — данные нестабильны или неверны"
modified: "2017-09-08"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-237.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-237.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 237 - External Speed Command Input (Multiple Unit Synchronization) - Data Erratic, Intermittent, or Incorrect
**Код 237 — внешний вход задания частоты (синхронизация агрегатов) — данные нестабильны или неверны**

> [!abstract] Процедура · `122-t05-237`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-09-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-237.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-237.pdf)

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
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 - пробный щуп типа пробки DeutschTM/AMPTM/Metri-PackTM, номер детали 3823993 - пробный щуп типа пробки DeutschTM, а номер детали 3823994 - пробный щуп типа разъема DeutschTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Определите, какой двигатель выключен. |  |
|  | **STEP 1A.** Проверить наличие нескольких кодов неисправностей. | Коды 426 и 497 неисправностей активны или неактивны, если количество неисправностей превышает одного за последние 25 часов работы двигателя. |
| ШАГ 2. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 2A.** Проверить контакты разъема жгута электромотора. | Грязные или поврежденные контакты? |
|  | **ШАГ 2В.** Проверьте напряжение питания привода на выходе. | 11.75 до 12.25-VDC? |
|  | **STEP 2C** Проверьте запас в 5 вольт. | 4,75-5,25-ВДЦ? |
|  | **STEP 2D.** Проверьте наличие открытой цепи. | Менее 10 Ом? |
|  | **ШАГ 2Е.** Проверить короткое замыкание от контакта к контакту. | Больше 100 тысяч ом? |
|  | **STEP 2F.** Проверьте короткое замыкание на блокировке двигателя. | Больше 100 тысяч ом? |
| ШАГ 3. | Проверьте оригинальную проводку производителя оборудования (OEM). |  |
|  | **STEP 3A.** Проверить контакты разъёма проводов OEM-приемника. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте наличие открытой цепи. | Менее 10 Ом? |
|  | **STEP 3C.** Проверить короткое замыкание от контакта к контакту. | Больше 100 тысяч ом? |
|  | **STEP 3D.** Проверьте короткое замыкание на блокировке двигателя. | Больше 100 тысяч ом? |
| ШАГ 4. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 4A.** Проверить контакты разъема жгутов проводов двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 4B.** Проверьте наличие открытой цепи. | Менее 10 Ом? |
|  | **STEP 4C.** Проверить короткое замыкание от контакта к контакту. | Больше 100 тысяч ом? |
|  | **STEP 4D.** Проверьте короткое замыкание на блокировке двигателя. | Больше 100 тысяч ом? |
| ШАГ 5. | Сбросьте коды неисправностей. |  |
|  | **STEP 5A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 5B.** Отключить код ошибки. | Код ошибки 237 неактивен? |

### ШАГ 1. Определите, какой двигатель выключен.

#### ШАГ 1A. Проверьте несколько кодов ошибок.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте несколько кодов ошибок. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Коды 426 и 497 неисправностей активны или неактивны, если количество неисправностей превышает одного за последние 25 часов работы двигателя. *Да | Соответствующие шаги по устранению неполадок |
| Коды 426 и 497 неисправностей активны или неактивны, если количество неисправностей превышает одного за последние 25 часов работы двигателя. **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов двигателя.

#### ШАГ 2A. Проверьте контакты разъема жгута проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините проводку двигателя от разъема ECM от разъема ECM на вторичном двигателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите разъём ремней электропроводки двигателя и контакты разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема контактной оболочки разбитого провода Повреждение разъема блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19]]. | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. Заменить поврежденный участок проводов жгутом. См. схему или схему проводов для всех соединений проводов. Ремонтировать разъем. См. процедуру 019-204 Ремонт ремня электропроводки двигателя. Процедура 019-043 Заменить ECM. См. процедуру 019-031 в разделе 19. | 5а |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте напряжение питания драйвера выхода.

| **Условия:** Отсоединить разъём ремней электропроводки двигателя от ECM на вторичном двигателе. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение питания драйвера выхода. Измерить напряжение от внешнего входного сигнала команды скорости контакта проводов двигателя с разъемом ECM на блоке двигателя. См. схему или схему проводов для идентификации контакта с разъемом. | 11.75 до 12.25-VDC? *Да | 2C |
| 11.75 до 12.25-VDC? **НЕТ** | 2D |  |

#### ШАГ 2C. Проверьте 5-вольтовый запас.

| **Условия:** Отсоедините разъем ECM от разъема ECM на вторичном двигателе. Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте 5-вольтовый запас. Измерить напряжение от внешнего входного обратного контакта скорости проводов двигателя с помощью разъема ECM к заземлению блока двигателя. См. схему или схему проводов для идентификации контакта с разъемом. | 4,75-5,25-ВДЦ? *Да | 5а |
| 4,75-5,25-ВДЦ? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините проводку двигателя от разъема ECM от разъема ECM на вторичном двигателе. Отсоедините разъем ECM электропроводки от разъема OEM-проводов на вторичном двигателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление внешнего контакта входного сигнала команды скорости проводов двигателя с помощью разъема ECM к внешнему контакту входного сигнала команды скорости разъема OEM. Измерить сопротивление от входного частотного включения RETURN (VSS)/вспомогательного регулятора разъема проводов двигателя к внешнему входному обратному контакту команды скорости разъема OEM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 2Е |
| Менее 10 Ом? **NORepair: **В ремне электропроводки двигателя обнаружена открытая схема. Устранение неполадок все проводные ремни, соединенные последовательно, чтобы определить, который содержит открытую цепь. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом. См. процедуру 019-043 в разделе 19. Ремонтировать разъем. См. процедуру 019-199 в разделе 19. | 5а |  |

#### ШАГ 2E. Проверьте короткое замыкание от контакта к контакту.

| **Условия:** Выключите замок зажигания. Отсоедините проводку двигателя от разъема ECM от разъема ECM на вторичном двигателе. Отсоедините разъем ECM электропроводки от разъема OEM-проводов на вторичном двигателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание от контакта к контакту. Измерить сопротивление от внешнего входного сигнала команды скорости контакта проводов двигателя с помощью разъема ECM со всеми другими штифтами в разъеме. Измерить сопротивление от внешнего входного контакта команды скорости возврата проводов двигателя упряжка разъема ECM ко всем другим штифтам в разъеме. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Более 100 тысяч ом? *Да | 2F |
| Более 100 тысяч ом? **NORepair: **В ремне электропроводки двигателя обнаружено короткое замыкание. Устранение неполадок все проводные ремни, соединенные последовательно, чтобы определить, который содержит короткое замыкание контакта с контактом. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом. См. процедуру 019-043 в разделе 19. Ремонтировать разъем. См. процедуру 019-199 в разделе 19. | 5а |  |

#### ШАГ 2F. Проверьте короткое замыкание на блокировку двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините проводку двигателя от разъема ECM от разъема ECM на вторичном двигателе. Отсоедините разъем ECM электропроводки от разъема OEM-проводов на вторичном двигателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на блокировку двигателя. Измерить сопротивление внешнего входного сигнала команды скорости контакта проводов двигателя с разъемом ECM на блоке двигателя. Измерить сопротивление от внешнего входного контакта команды скорости возврата проводов двигателя с помощью разъема ECM к заземлению блока двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Более 100 тысяч ом? *Да | 3А |
| Более 100 тысяч ом? **NORepair: **В ремне электропроводки двигателя обнаружено короткое замыкание на землю. Устранение неполадок во всех проводных упряжках, соединенных последовательно, чтобы определить, какая из них содержит короткое замыкание. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом. См. процедуру 019-043 в разделе 19. Ремонтировать разъем. См. процедуру 019-199 в разделе 19. | 5а |  |

### ШАГ 3. Проверьте OEM проводку.

#### ШАГ 3A. Проверьте контакты разъёма OEM-проводов.

| **Условия:** Выключите замок зажигания. Отсоедините разъём ремня электропроводки двигателя от разъёма ремня электропроводки OEM на вторичном двигателе. Отсоедините разъем жгута проводов двигателя от разъема жгута проводов OEM на основном двигателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъёма ремней OEM-проводов и разъёма ремней двигателя для следующего: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема контактной оболочки разбитого провода Повреждение разъема блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]]. | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите контакты разъема. Заменить поврежденный участок проводов жгутом. См. схему или схему проводов для всех соединений проводов. Ремонт ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. Ремонтировать разъем. См. процедуру 019-207 в разделе 19. | 5а |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините 23-контактный OEM-разъем от электропроводки двигателя на основном двигателе. Отсоедините 31-контактный OEM-разъем от электропроводки двигателя на вторичном двигателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление от вспомогательного контакта PWM-сигнала водителя на 23-контактном OEM-разъеме основного двигателя внешнему контакту командного входного сигнала команды скорости на 31-контактном OEM-разъеме вторичного двигателя. Измерьте сопротивление от OEM-обеспеченного 5-вольтового SUPPLY внешнему входному контакту команды скорости на 31-контактном OEM-разъеме вторичного двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 3C |
| Менее 10 Ом? **NORepair: **В электропроводке OEM обнаружена открытая схема. Устранение неполадок все проводные ремни, соединенные последовательно, чтобы определить, который содержит открытую цепь. См. сервисное руководство изготовителя машины. См. схему или схему проводов для всех соединений проводов. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 5а |  |

#### ШАГ 3C. Проверьте короткое замыкание от контакта к контакту.

| **Условия:** Выключите замок зажигания. Отсоедините 23-контактный OEM-разъем от электропроводки двигателя на основном двигателе. Отсоедините 31-контактный OEM-разъем от электропроводки двигателя на вторичном двигателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание от контакта к контакту. Измерить сопротивление от вспомогательного контакта PWM-сигнала водителя на 23-контактном OEM-разъеме основного двигателя ко всем другим штифтам в разъеме. Измерьте сопротивление от OEM-обеспеченного 5-вольтового SUPPLY ко всем другим штифтам в 23-контактном OEM-разъеме основного двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Более 100 тысяч ом? *Да | 3D |
| Более 100 тысяч ом? **NORepair: **В электропроводке OEM обнаружено короткое замыкание от контакта к контакту. Устранение неполадок все проводные ремни, соединенные последовательно, чтобы определить, который содержит короткое замыкание контакта с контактом. См. сервисное руководство изготовителя машины. См. схему или схему проводов для всех соединений проводов. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 5а |  |

#### ШАГ 3D. Проверьте короткое замыкание на блокировку двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините 23-контактный OEM-разъем от электропроводки двигателя на основном двигателе. Отсоедините 31-контактный OEM-разъем от электропроводки двигателя на вторичном двигателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на блокировку двигателя. Измерить сопротивление от выходного штифта модуляции ширины импульса OEM-привода на 23-контактном OEM-разъеме основного двигателя к заземлению блока двигателя. Измерьте сопротивление от OEM-предоставленной 5-вольтовой SUPPLY к заземлению блока двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Более 100 тысяч ом? *Да | 4А |
| Более 100 тысяч ом? **NORepair: **В электропроводке OEM обнаружено короткое замыкание на землю. Устранение неполадок все проводов, соединенные последовательно, чтобы определить, который содержит короткое замыкание на землю. См. схему или схему проводов для всех соединений проводов. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 5а |  |

### ШАГ 4. Проверьте жгут проводов двигателя.

#### ШАГ 4A. Проверьте контакты разъема жгута проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините разъём OEM-проводов от разъема жгута проводов двигателя на основном двигателе. Отсоедините разъем ECM от разъема ECM на первичном двигателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите разъём ремней электропроводки двигателя и контакты разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема контактной оболочки разбитого провода Повреждение разъема блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]]. | Грязные или поврежденные контакты? **Ремонт:** В разъеме жгутов проводов двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. Заменить поврежденный участок проводов жгутом. См. схему или схему проводов для всех соединений проводов. Ремонт проводов жгута. См. процедуру 019-043 в разделе 19. Ремонтировать разъем. См. процедуру 019-204 в разделе 19. | 5а |
| Грязные или поврежденные контакты? **НЕТ** | 4B |  |

#### ШАГ 4B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините 23-контактный OEM-разъем от электропроводки двигателя на основном двигателе. Отсоедините проводку двигателя от разъема ECM от ECM на основном двигателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление от вспомогательного импульса шириной модуля (PWM) драйвера 1 сигнального контакта на 23-контактном OEM-разъеме к вспомогательному PWM-водителю 1 сигнального контакта на разъеме ECM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 4C |
| Менее 10 Ом? **NORepair: **В ремне электропроводки двигателя обнаружена открытая схема. Устранение неполадок все проводные ремни, соединенные последовательно, чтобы определить, который содержит открытую цепь. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом. См. процедуру 019-043 в разделе 19. Ремонтировать разъем. См. процедуру 019-199 в разделе 19. | 5а |  |

#### ШАГ 4C. Проверьте короткое замыкание от контакта к контакту.

| **Условия:** Выключите замок зажигания. Отсоедините 23-контактный OEM-разъем от разъема жгута проводов двигателя на основном двигателе. Отсоедините разъем ECM от разъема ECM на первичном двигателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание от контакта к контакту. Измерить сопротивление от вспомогательного PWM драйвера 1 сигнального контакта на проводах двигателя упряжка ECM разъёма всех остальных штифтов в разъеме. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Более 100 тысяч ом? *Да | 4D |
| Более 100 тысяч ом? **NORepair: **В ремне электропроводки двигателя обнаружено короткое замыкание. Устранение неполадок во всех проводных упряжках, соединенных последовательно, чтобы определить, какая из них содержит короткое замыкание. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом. См. процедуру 019-043 в разделе 19. Ремонтировать разъем. См. процедуру 019-199 в разделе 19. | 5а |  |

#### ШАГ 4D. Проверьте короткое замыкание на блокировку двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините 23-контактный OEM-разъем от разъема жгута проводов двигателя на основном двигателе. Отсоедините разъем ECM от разъема ECM на первичном двигателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на блокировку двигателя. Измерить сопротивление вспомогательного PWM драйвера 1 сигнального контакта на разъеме ECM к заземлению блока двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Более 100 тысяч ом? *Да | 5а |
| Более 100 тысяч ом? **NORepair: **В ремне электропроводки двигателя обнаружено короткое замыкание на землю. Устранение неполадок во всех проводных упряжках, соединенных последовательно, чтобы определить, какая из них содержит короткое замыкание. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом. См. процедуру 019-043 в разделе 19. Ремонтировать разъем. См. процедуру 019-199 в разделе 19. | 5а |  |

### ШАГ 5. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 5A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 5В |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]]. | 5В |  |

#### ШАГ 5B. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода 237. | Код ошибки 237 неактивен? *Да | Ремонт завершён. |
| Код ошибки 237 неактивен? **Секретарь:**Проверить, что все шаги были выполнены. Если все шаги выполнены, то следуйте процессу технической эскалации. | Эскалация или призыв к помощи. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3823993 - male Deutsch™ test lead, and Part Number 3823994 - female Deutsch™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Determine which engine is shutting down. |  |
> |  | **STEP 1A.** Check for multiple fault codes. | Fault Codes 426 and 497 active or inactive with more than one count in the last 25 engine hours? |
> | STEP 2. | Check the engine harness. |  |
> |  | **STEP 2A.** Inspect the engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the output driver supply voltage. | 11.75 to 12.25-VDC? |
> |  | **STEP 2C.** Check the 5 volt supply. | 4.75 to 5.25-VDC? |
> |  | **STEP 2D.** Check for an open circuit. | Less than 10 ohms? |
> |  | **STEP 2E.** Check for a short circuit from pin-to-pin. | Greater than 100k ohms? |
> |  | **STEP 2F.** Check for a short circuit to engine block ground. | Greater than 100k ohms? |
> | STEP 3. | Check the original equipment manufacturer (OEM) harness. |  |
> |  | **STEP 3A.** Inspect the OEM harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check for an open circuit. | Less than 10 ohms? |
> |  | **STEP 3C.** Check for a short circuit from pin-to-pin. | Greater than 100k ohms? |
> |  | **STEP 3D.** Check for a short circuit to engine block ground. | Greater than 100k ohms? |
> | STEP 4. | Check the engine harness. |  |
> |  | **STEP 4A.** Inspect the engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 4B.** Check for an open circuit. | Less than 10 ohms? |
> |  | **STEP 4C.** Check for a short circuit from pin-to-pin. | Greater than 100k ohms? |
> |  | **STEP 4D.** Check for a short circuit to engine block ground. | Greater than 100k ohms? |
> | STEP 5. | Clear the fault codes. |  |
> |  | **STEP 5A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 5B.** Disable the fault code. | Fault Code 237 inactive? |
>
> ### STEP 1. Determine which engine is shutting down.
>
> #### STEP 1A. Check for multiple fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for multiple fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Codes 426 and 497 active or inactive with more than one count in the last 25 engine hours? **YES** | Appropriate troubleshooting steps |
> | Fault Codes 426 and 497 active or inactive with more than one count in the last 25 engine hours? **NO** | 2A |  |
>
> ### STEP 2. Check the engine harness.
>
> #### STEP 2A. Inspect the engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness ECM connector from the ECM connector on the secondary engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness connector and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pin Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361in Section 19]]. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Replace the damaged section of the harness. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the connector. Refer to Procedure 019-204 Repair the engine harness. Refer to Procedure 019-043 Replace the ECM. Refer to Procedure 019-031 in Section 19. | 5A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the output driver supply voltage.
>
> | **Conditions:** Disconnect the engine harness connector from the ECM on the secondary engine. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the output driver supply voltage. Measure the voltage from the external speed command input SIGNAL pin of the engine harness ECM connector to engine block ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. | 11.75 to 12.25-VDC? **YES** | 2C |
> | 11.75 to 12.25-VDC? **NO** | 2D |  |
>
> #### STEP 2C. Check the 5 volt supply.
>
> | **Conditions:** Disconnect the engine harness ECM connector from the ECM connector on the secondary engine. Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the 5 volt supply. Measure the voltage from the external speed input RETURN pin of the engine harness ECM connector to engine block ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. | 4.75 to 5.25-VDC? **YES** | 5A |
> | 4.75 to 5.25-VDC? **NO** | 2D |  |
>
> #### STEP 2D. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness ECM connector from the ECM connector on the secondary engine. Disconnect the engine harness ECM connector from the OEM harness connector on the secondary engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance from the external speed command input SIGNAL pin of the engine harness ECM connector to the external speed command input SIGNAL pin of the OEM connector. Measure the resistance from the frequency input RETURN (VSS)/auxiliary governor pin of the engine harness connector to the external speed command input RETURN pin of the OEM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 2E |
> | Less than 10 ohms? **NORepair:** An open circuit has been detected in the engine harness. Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the connector. Refer to Procedure 019-199 in Section 19. | 5A |  |
>
> #### STEP 2E. Check for a short circuit from pin-to-pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness ECM connector from the ECM connector on the secondary engine. Disconnect the engine harness ECM connector from the OEM harness connector on the secondary engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin-to-pin. Measure the resistance from the external speed command input SIGNAL pin of the engine harness ECM connector to all other pins in the connector. Measure the resistance from the external speed command input RETURN pin of the engine harness ECM connector to all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | More than 100k ohms? **YES** | 2F |
> | More than 100k ohms? **NORepair:** A pin-to-pin short circuit has been detected in the engine harness. Troubleshoot all harnesses connected in series to determine which contains the pin-to-pin short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 inSection 19. Repair the connector. Refer to Procedure 019-199 in Section 19. | 5A |  |
>
> #### STEP 2F. Check for a short circuit to engine block ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness ECM connector from the ECM connector on the secondary engine. Disconnect the engine harness ECM connector from the OEM harness connector on the secondary engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to engine block ground. Measure the resistance from the external speed command input SIGNAL pin of the engine harness ECM connector to engine block ground. Measure the resistance from the external speed command input RETURN pin of the engine harness ECM connector to engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | More than 100k ohms? **YES** | 3A |
> | More than 100k ohms? **NORepair:** A short circuit to ground has been detected in the engine harness. Troubleshoot all harnesses connected in series to determine which contains the short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the connector. Refer to Procedure 019-199 in Section 19. | 5A |  |
>
> ### STEP 3. Check the OEM harness.
>
> #### STEP 3A. Inspect the OEM harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the OEM harness connector on the secondary engine. Disconnect the engine harness connector from the OEM harness connector on the primary engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness connector and engine harness connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pin Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector pins. Replace the damaged section of the harness. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the engine harness. Refer to Procedure 019-043 in Section 19. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. Repair the connector. Refer to Procedure 019-207 in Section 19. | 5A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 23 pin OEM connector from the engine harness on the primary engine. Disconnect the 31 pin OEM connector from the engine harness on the secondary engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance from the auxiliary PWM driver SIGNAL pin on the 23 pin OEM connector of the primary engine to the external speed command input SIGNAL pin on the 31 pin OEM connector of the secondary engine. Measure the resistance from the OEM-provided 5 volt SUPPLY to the external speed command input RETURN pin on the 31-pin OEM connector of the secondary engine. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3C |
> | Less than 10 ohms? **NORepair:** An open circuit has been detected in the OEM harness. Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the OEM service manual. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 5A |  |
>
> #### STEP 3C. Check for a short circuit from pin-to-pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 23 pin OEM connector from the engine harness on the primary engine. Disconnect the 31 pin OEM connector from the engine harness on the secondary engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin-to-pin. Measure the resistance from the auxiliary PWM driver SIGNAL pin on the 23 pin OEM connector of the primary engine to all other pins in the connector. Measure the resistance from the OEM-provided 5 volt SUPPLY to all other pins in the 23 pin OEM connector of the primary engine. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | More than 100k ohms? **YES** | 3D |
> | More than 100k ohms? **NORepair:** A pin-to-pin short circuit has been detected in the OEM harness. Troubleshoot all harnesses connected in series to determine which contains the pin-to-pin short circuit. Refer to the OEM service manual. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 5A |  |
>
> #### STEP 3D. Check for a short circuit to engine block ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 23 pin OEM connector from the engine harness on the primary engine. Disconnect the 31 pin OEM connector from the engine harness on the secondary engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to engine block ground. Measure the resistance from the OEM actuator pulse width modulation output pin on the 23 pin OEM connector of the primary engine to engine block ground. Measure the resistance from the OEM-provided 5 volt SUPPLY to engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | More than 100k ohms? **YES** | 4A |
> | More than 100k ohms? **NORepair:** A short circuit to ground has been detected in the OEM harness. Troubleshoot all harnesses connected in series to determine which contains the short circuit to ground. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 5A |  |
>
> ### STEP 4. Check the engine harness.
>
> #### STEP 4A. Inspect the engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the engine harness connector on the primary engine. Disconnect the engine harness ECM connector from the ECM connector on the primary engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness connector and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pin Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the engine harness connector. Clean the connector and pins. Replace the damaged section of the harness. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the harness. Refer to Procedure 019-043 in Section 19. Repair the connector. Refer to Procedure 019-204 in Section 19. | 5A |
> | Dirty or damaged pins? **NO** | 4B |  |
>
> #### STEP 4B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 23 pin OEM connector from the engine harness on the primary engine. Disconnect the engine harness ECM connector from the ECM on the primary engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance from the auxiliary pulse width moduled (PWM) driver 1 SIGNAL pin on the 23 pin OEM connector to the auxiliary PWM driver 1 SIGNAL pin on the ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 4C |
> | Less than 10 ohms? **NORepair:** An open circuit has been detected in the engine harness. Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the connector. Refer to Procedure 019-199 in Section 19. | 5A |  |
>
> #### STEP 4C. Check for a short circuit from pin-to-pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 23 pin OEM connector from the engine harness connector on the primary engine. Disconnect the engine harness ECM connector from the ECM connector on the primary engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin-to-pin. Measure the resistance from the auxiliary PWM driver 1 SIGNAL pin on the engine harness ECM connector all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | More than 100k ohms? **YES** | 4D |
> | More than 100k ohms? **NORepair:** A pin-to-pin short circuit has been detected in the engine harness. Troubleshoot all harnesses connected in series to determine which contains the short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the connector. Refer to Procedure 019-199 in Section 19. | 5A |  |
>
> #### STEP 4D. Check for a short circuit to engine block ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 23 pin OEM connector from the engine harness connector on the primary engine. Disconnect the engine harness ECM connector from the ECM connector on the primary engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to engine block ground. Measure the resistance from the auxiliary PWM driver 1 SIGNAL pin on the ECM connector to engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | More than 100k ohms? **YES** | 5A |
> | More than 100k ohms? **NORepair:** A short circuit to ground has been detected in the engine harness. Troubleshoot all harnesses connected in series to determine which contains the short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the connector. Refer to Procedure 019-199 in Section 19. | 5A |  |
>
> ### STEP 5. Check ECM calibration and clear fault codes.
>
> #### STEP 5A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 5B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19]]. | 5B |  |
>
> #### STEP 5B. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify Fault Code 237 is inactive. | Fault Code 237 inactive? **YES** | Repair complete. |
> | Fault Code 237 inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance. |  |
