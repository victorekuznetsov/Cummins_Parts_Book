---
aliases:
  - "Код 323 — цепь электромагнита форсунки цилиндра 5 — ток ниже нормы или обрыв"
type: "Процедура"
doc: "82-t05-323"
title_en: "FAULT CODE 323 - Injector Solenoid Driver Cylinder 5 Circuit - Current Below Normal, or Open Circuit"
title_ru: "Код 323 — цепь электромагнита форсунки цилиндра 5 — ток ниже нормы или обрыв"
modified: "2012-06-12"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-323.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-323.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# FAULT CODE 323 - Injector Solenoid Driver Cylinder 5 Circuit - Current Below Normal, or Open Circuit
**Код 323 — цепь электромагнита форсунки цилиндра 5 — ток ниже нормы или обрыв**

> [!abstract] Процедура · `82-t05-323`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-323.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-323.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!danger] ОПАСНО
> На электромагниты форсунок при работающем двигателе подаётся высокое напряжение. Чтобы уменьшить вероятность получения травмы или смерти от поражения электрическим током, не носите ювелирные изделия или сырую одежду, и не прикасайтесь к соленоидам форсунки или соленоидным проводам при работе двигателя.

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения новой ECM, все другие активные коды неисправностей должны быть исследованы до замены ECM.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 - пробный щуп типа вилки DeutschTM/AMPTM/Metri-PackTM и номер детали 3822917 - пробный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверка активных кодов неисправностей. | Код ошибки 111 активен? |
| ШАГ 2. | Проверьте форсунку и схему. |  |
|  | **STEP 2A.** Проверить контакты разъема электропроводки и электропроводки двигателя. | Грязные, свободные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте наличие неисправности в топливном форсунке соленоида и цепи. | Является ли сопротивление топливного форсунка и схемы от 0,5 до 2,5 Ом? |
|  | **STEP 2C** Проверьте наличие неисправности в топливном форсунке соленоида и цепи. | Было ли сопротивление, измеренное на шаге 2В, меньше 0,5 Ом? |
| ШАГ 3. | Проверьте короткое замыкание в топливном форсунке соленоида и цепи. |  |
|  | **STEP 3A.** Проверить контакты форсунки и разъема топливного топлива. | Грязные, свободные или поврежденные контакты? |
|  | **ШАГ 3В.** Проверить короткое замыкание в топливном форсунке соленоида. | Сопротивление форсунки соленоида меньше 0,5 Ом? |
|  | **STEP 3C** Проверьте короткое замыкание в ремне электропроводки двигателя. | Сопротивление больше 100k ом? |
|  | **STEP 3D.** Проверьте короткое замыкание в ремне электропроводки двигателя. | Сопротивление больше, чем 100k ом? |
| ШАГ 4. | Проверьте высокое сопротивление или открытую цепь в топливном форсунке соленоида и цепи. |  |
|  | **STEP 4A.** Проверить контакты форсунки и разъема топливного топлива. | Грязные, свободные или поврежденные контакты? |
|  | **STEP 4B.** Проверить наличие высокого сопротивления или открытой цепи в соленоиде форсунки. | Сопротивление форсунки соленоида больше 1,5 Ом? |
|  | **STEP 4C** Проверить наличие высокого сопротивления или открытой цепи в ремне электропроводки двигателя. | Является ли сопротивление цепи больше 1 Ом? |
| ШАГ 5. | Сбросьте коды неисправностей. |  |
|  | **STEP 5A.** Отключить код ошибки. | Код 323 неактивен? |
|  | **STEP 5B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте наличие активных кодов неисправностей.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие активных кодов неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 111 активен? *Да | Устранение неисправностей Код 111 |
| Код ошибки 111 активен? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте форсунку и схему.

#### ШАГ 2A. Проверьте контакты разъема ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините жгут электропроводки двигателя от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты электропроводки двигателя и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или разъема изоляции Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для или общие методы проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные, свободные или поврежденные контакты? **Ремонт: **См. схему или схему проводов для всех соединений проводов. В разъеме ECM или в ремне электропроводки двигателя обнаружено поврежденное соединение. Ремонт поврежденных контактов. Ремонт или замена ремня электропроводки двигателя или замена ECM, в зависимости от того, какие контакты повреждены. Смывать грязь, мусор или влагу с контактов разъема, использовать электронный контактный очиститель, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 019-043 в разделе 19. Заменить ECM. См. процедуру 019-031 в разделе 19. | 5а |
| Грязные, свободные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте неисправность схемы в соленоиде и цепи форсунки.

| **Условия:** Выключите замок зажигания. Отсоедините жгут электропроводки двигателя от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте неисправность схемы в соленоиде и цепи форсунки. Измерить сопротивление между контактами 4 и 3 на разъеме ECM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Является ли сопротивление топливного форсунка и схемы от 0,5 до 2,5 Ом? Заменить ЭКМ. См. процедуру 019-031 в разделе 19. | 5а |
| Является ли сопротивление топливного форсунка и схемы от 0,5 до 2,5 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте неисправность схемы в соленоиде и цепи форсунки.

| **Условия:** Выключите замок зажигания. Отсоедините жгут электропроводки двигателя от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте измерение сопротивления на шаге 2B. | Было ли сопротивление, измеренное на шаге 2В, меньше 0,5 Ом? *Да | 3А |
| Было ли сопротивление, измеренное на шаге 2В, больше 2,5 Ом? **НЕТ** | 4А |  |

### ШАГ 3. Проверьте короткое замыкание в топливном форсунке соленоида и цепи.

#### ШАГ 3A. Осмотрите контакты форсунки и разъёма топлива.

| **Условия:** Выключите замок зажигания. Снимите крышку коромысел. Используйте следующую процедуру в руководстве по обслуживанию ISM, ISMe и QSM11, Бюллетень [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. См. процедуру 003-011 в разделе 3. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъёма электропроводки двигателя и топливного форсунка для следующих целей: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или разъема изоляции Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные, свободные или поврежденные контакты? **Ремонт:** В ремне электропроводки двигателя или разъеме форсунки топлива обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 019-043 в разделе 19. | 5а |
| Грязные, свободные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте короткое замыкание в топливном форсунке соленоид.

| **Условия:** Выключите замок зажигания. Снимите крышку коромысел. Используйте следующие процедуры в руководстве по обслуживанию ISM, ISMe и QSM11, Бюллетень [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. См. процедуру 003-011 в разделе 3. Отсоедините внутреннюю проводку привода от форсунки соленоида. Удалите форсунка соленоидных проводов из соленоида. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание в топливном форсунке соленоид. Измерьте сопротивление от поста к посту на топливном форсунке соленоида. См. схему или схему проводов для идентификации контакта с разъемом. Пользователю предлагается следующая процедура для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление форсунки соленоида меньше 0,5 Ом? Заменить форсунка. Используйте следующую процедуру в руководстве по обслуживанию ISM, ISMe и QSM11, Бюллетень [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]].[[35-006-026-tr — Injector\|См. процедуру 006-026 в разделе 6.]] | 4А |
| Сопротивление форсунки соленоида меньше 0,5 Ом? **НЕТ** | 3C |  |

#### ШАГ 3C. Проверьте короткое замыкание в ремне электропроводки двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините форсунку от электропроводки двигателя. Отсоедините жгут электропроводки двигателя от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание в ремне электропроводки двигателя. Измерьте сопротивление между топливным форсункой SIGNAL (+) и всеми другими штифтами в разъеме ECM. Измерьте сопротивление между топливным форсункой RETURN (-) и всеми другими штифтами в разъеме ECM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление больше 100k ом? *Да | 3D |
| Сопротивление больше 100k ом? **NORepair: **В ремне электропроводки двигателя обнаружено короткое замыкание. Неисправности устраняют межсоединение на клапанном клапане качалки рычага проездного разъёма. Определите, находится ли короткое замыкание во внутренней электропроводке упряжки внутри корпуса рычага клапанного клапана или в электропроводке двигателя. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. | 4А |  |

#### ШАГ 3D. Проверьте короткое замыкание, чтобы заземлиться в ремне электропроводки двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините форсунку от электропроводки двигателя. Отсоедините жгут электропроводки двигателя от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание, чтобы заземлиться в ремне электропроводки двигателя. Измерьте сопротивление между топливным форсункой SIGNAL (+) и заземлением блока двигателя. Измерить сопротивление между топливным форсункой ВПЕРЕД (-) штифта на блок двигателя заземление. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление больше, чем 100k ом? *Да | 5а |
| Сопротивление больше, чем 100k ом? **NORepair: **В ремне электропроводки двигателя обнаружено короткое замыкание. Неисправности устраняют межсоединение на клапанном клапане качалки рычага проездного разъёма. Определите, находится ли короткое замыкание во внутренней электропроводке упряжки внутри корпуса рычага клапанного клапана или в электропроводке двигателя. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. | 5а |  |

### ШАГ 4. Проверьте высокое сопротивление или открытую цепь в топливном форсунке соленоида и цепи.

#### ШАГ 4A. Осмотрите контакты форсунки и разъёма топлива.

| **Условия:** Выключите замок зажигания. Отсоедините жгут электропроводки двигателя от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты электропроводки двигателя и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или разъема изоляции Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные, свободные или поврежденные контакты? **Ремонт:** В разъеме ECM или разъеме ремней электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 019-043 в разделе 19. | 5а |
| Грязные, свободные или поврежденные контакты? **НЕТ** | 4B |  |

#### ШАГ 4B. Проверьте высокое сопротивление или открытую цепь в соленоиде форсунки.

| **Условия:** Выключите замок зажигания. Снимите крышку коромысел. Используйте следующую процедуру в руководстве по обслуживанию ISM, ISMe и QSM11, Бюллетень [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. См. процедуру 003-011 в разделе 3. Отсоедините внутреннюю проводку привода от форсунки соленоида. Удалите форсунка соленоидных проводов из соленоида. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие открытой цепи в соленоиде форсунки. Измерьте сопротивление от поста к посту на топливном форсунке соленоида. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление форсунки соленоида больше 1,5 Ом? Заменить форсунка. Используйте следующую процедуру в руководстве по обслуживанию ISM, ISMe и QSM11, Бюллетень [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]].[[35-006-026-tr — Injector\|См. процедуру 006-026 в разделе 6.]] | 5а |
| Сопротивление форсунки соленоида больше 1,5 Ом? **НЕТ** | 4C |  |

#### ШАГ 4C. Проверьте высокое сопротивление или открытую цепь в ремне электропроводки двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините форсунку от электропроводки двигателя. Отсоедините жгут электропроводки двигателя от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие открытой цепи в ремне электропроводки двигателя. Измерить сопротивление между топливным форсункой SIGNAL (+) штифтом на топливном форсунке и контактом 4 на разъеме электропроводки двигателя ECM. Измерить сопротивление между топливным форсункой ВПЕРЕД (-) штифтом на топливном форсунке и контактом 3 на разъёме электропроводки двигателя ECM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Является ли сопротивление цепи больше 1 Ом? **Ремонт: **В ремне электропроводки двигателя обнаружена открытая схема или высокое сопротивление. Неисправности устраняют межсоединение на клапанном клапане качалки рычага проездного разъёма. Определите, находится ли короткое замыкание во внутренней электропроводке упряжки внутри корпуса рычага клапанного клапана или в электропроводке двигателя. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. | 5а |
| Является ли сопротивление цепи больше 1 Ом? **НЕТ** | 5а |  |

### ШАГ 5. Сбросьте коды неисправностей.

#### ШАГ 5A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода 323. | Код 323 неактивен? *Да | 5а |
| Код 323 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 5B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair: **Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующая диаграмма устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **WARNING · Опасно**
> The injector solenoids receive high voltage when the engine is operating. To reduce the possibility of personal injury or death from electrical shock, do not wear jewelry or damp clothing, and do not touch the injector solenoids or the solenoid wires when the engine is operating.
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for active fault codes. | Fault Code 111 active? |
> | STEP 2. | Check the fuel injector and circuit. |  |
> |  | **STEP 2A.** Inspect the ECM and engine harness connector pins. | Dirty, loose, or damaged pins? |
> |  | **STEP 2B.** Check for a circuit fault in the injector solenoid and circuit. | Is the resistance of the injector and circuit 0.5 to 2.5 ohms? |
> |  | **STEP 2C.** Check for a circuit fault in the injector solenoid and circuit. | Was the resistance measured in Step 2B less than 0.5 ohms? |
> | STEP 3. | Check for a short circuit in the injector solenoid and circuit. |  |
> |  | **STEP 3A.** Inspect the fuel injector and connector pins. | Dirty, loose, or damaged pins? |
> |  | **STEP 3B.** Check for a short circuit in the injector solenoid. | Is the resistance of the injector solenoid less than 0.5 ohms? |
> |  | **STEP 3C.** Check for a short circuit in the engine harness. | Is the resistance greater than 100k ohms? |
> |  | **STEP 3D.** Check for a short circuit to ground in the engine harness. | Is the resistance greater then 100k ohms? |
> | STEP 4. | Check for high resistance or an open circuit in the injector solenoid and circuit. |  |
> |  | **STEP 4A.** Inspect the fuel injector and connector pins. | Dirty, loose, or damaged pins? |
> |  | **STEP 4B.** Check for high resistance or an open circuit in the injector solenoid. | Is the resistance of the injector solenoid greater than 1.5 ohms? |
> |  | **STEP 4C.** Check for high resistance or an open circuit in the engine harness. | Is the resistance of the circuit greater than 1 ohm? |
> | STEP 5. | Clear the fault codes. |  |
> |  | **STEP 5A.** Disable the fault code. | Fault Code 323 inactive? |
> |  | **STEP 5B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for active fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for active fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 111 active? **YES** | Troubleshoot Fault Code 111 |
> | Fault Code 111 active? **NO** | 2A |  |
>
> ### STEP 2. Check the fuel injector and circuit.
>
> #### STEP 2A. Inspect the ECM and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for or general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty, loose, or damaged pins? **YESRepair:** Refer to the circuit diagram or wiring diagram for all harness interconnections. A damaged connection has been detected in the ECM connector or engine harness. Repair the damaged pins. Repair or replace the engine harness or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins, use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 5A |
> | Dirty, loose, or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check for a circuit fault in the injector solenoid and circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a circuit fault in the injector solenoid and circuit. Measure the resistance between pins 4 and 3 at the ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Is the resistance of the injector and circuit 0.5 to 2.5 ohms? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 5A |
> | Is the resistance of the injector and circuit 0.5 to 2.5 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check for a circuit fault in the injector solenoid and circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use the resistance measurement from Step 2B. | Was the resistance measured in Step 2B less than 0.5 ohms? **YES** | 3A |
> | Was the resistance measured in Step 2B greater than 2.5 ohms? **NO** | 4A |  |
>
> ### STEP 3. Check for a short circuit in the injector solenoid and circuit.
>
> #### STEP 3A. Inspect the fuel injector and connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Remove the rocker lever cover. Use the following procedure in the ISM, ISMe, and QSM11 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 003-011 in Section 3. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and fuel injector connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty, loose, or damaged pins? **YESRepair:** A damaged connection has been detected in the engine harness or fuel injector connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in Section 19. | 5A |
> | Dirty, loose, or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check for a short circuit in the injector solenoid.
>
> | **Conditions:** Turn keyswitch OFF. Remove the rocker lever cover. Use the following procedeure in the ISM, ISMe, and QSM11 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 003-011 in Section 3. Disconnect the internal actuator harness from the injector solenoid. Remove the injector solenoid wires from the solenoid. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit in the injector solenoid. Measure the resistance from post to post on the injector solenoid. Refer to the circuit diagram or wiring diagram for connector pin identification. User the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Is the resistance of the injector solenoid less than 0.5 ohms? **YESRepair:** Replace the injector. Use the following procedure in the ISM, ISMe, and QSM11 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] | 4A |
> | Is the resistance of the injector solenoid less than 0.5 ohms? **NO** | 3C |  |
>
> #### STEP 3C. Check for a short circuit in the engine harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the injector from the engine harness. Disconnect the engine harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit in the engine harness. Measure the resistance between the injector SIGNAL (+) pin and all other pins in the engine harness ECM connector. Measure the resistance between the injector RETURN (-) pin and all other pins in the engine harness ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Is the resistance greater than 100k ohms? **YES** | 3D |
> | Is the resistance greater than 100k ohms? **NORepair:** A short circuit has been detected in the engine harness. Troubleshoot the interconnect at the rocker lever housing pass-through connector. Determine if the short circuit is in the internal harness inside the rocker lever housing or in the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |
>
> #### STEP 3D. Check for a short circuit to ground in the engine harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the injector from the engine harness. Disconnect the engine harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground in the engine harness. Measure the resistance between the injector SIGNAL (+) pin to engine block ground. Measure the resistance between the injector RETURN (-) pin to engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Is the resistance greater then 100k ohms? **YES** | 5A |
> | Is the resistance greater then 100k ohms? **NORepair:** A short circuit has been detected in the engine harness. Troubleshoot the interconnect at the rocker lever housing pass-through connector. Determine if the short circuit is in the internal harness inside the rocker lever housing or in the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in Section 19. | 5A |  |
>
> ### STEP 4. Check for high resistance or an open circuit in the injector solenoid and circuit.
>
> #### STEP 4A. Inspect the fuel injector and connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty, loose, or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in Section 19. | 5A |
> | Dirty, loose, or damaged pins? **NO** | 4B |  |
>
> #### STEP 4B. Check for high resistance or an open circuit in the injector solenoid.
>
> | **Conditions:** Turn keyswitch OFF. Remove the rocker lever cover. Use the following procedure in the ISM, ISMe, and QSM11 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 003-011 in Section 3. Disconnect the internal actuator harness from the injector solenoid. Remove the injector solenoid wires from the solenoid. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit in the injector solenoid. Measure the resistance from post to post on the injector solenoid. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Is the resistance of the injector solenoid greater than 1.5 ohms? **YESRepair:** Replace the injector. Use the following procedure in the ISM, ISMe, and QSM11 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] | 5A |
> | Is the resistance of the injector solenoid greater than 1.5 ohms? **NO** | 4C |  |
>
> #### STEP 4C. Check for high resistance or an open circuit in the engine harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the injector from the engine harness. Disconnect the engine harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit in the engine harness. Measure the resistance between the injector SIGNAL (+) pin at the injector and pin 4 at the engine harness ECM connector. Measure the resistance between the injector RETURN (-) pin at the injector and pin 3 at the engine harness ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Is the resistance of the circuit greater than 1 ohm? **YESRepair:** An open circuit or high resistance has been detected in the engine harness. Troubleshoot the interconnect at the rocker lever housing pass-through connector. Determine if the short circuit is in the internal harness inside the rocker lever housing or in the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in Section 19. | 5A |
> | Is the resistance of the circuit greater than 1 ohm? **NO** | 5A |  |
>
> ### STEP 5. Clear the fault codes.
>
> #### STEP 5A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify Fault Code 323 is inactive. | Fault Code 323 inactive? **YES** | 5A |
> | Fault Code 323 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 5B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting chart |  |
