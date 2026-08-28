---
aliases:
  - "Код 2186 — цепь питания датчиков 4 — напряжение ниже нормы"
type: "Процедура"
doc: "123-t05-2186"
title_en: "FAULT CODE 2186 - Sensor Supply 4 Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Код 2186 — цепь питания датчиков 4 — напряжение ниже нормы"
modified: "2026-02-09"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-2186.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-2186.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# FAULT CODE 2186 - Sensor Supply 4 Circuit - Voltage Below Normal or Shorted to Low Source
**Код 2186 — цепь питания датчиков 4 — напряжение ниже нормы**

> [!abstract] Процедура · `123-t05-2186`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-02-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-2186.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-2186.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения новой ECM, все другие активные коды неисправностей должны быть исследованы до замены ECM.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 — пробный щуп типа штепсельной заглушки DeutschTM/AMPTM/Metri-PackTM, номер детали 3822917 — пробный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM, номер детали 3164596 — штыревой пробный щуп FramatomeTM, а номер детали 3164597 — гнездовой пробный щуп FramatomeTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить наличие активного кода неисправности. | Код 2186 активен? |
| ШАГ 2. | Проверьте датчики и схемы, подключенные к датчику питания 4 и возвращайтесь. |  |
|  | **STEP 2A.** Осмотрите датчик скорости/положения вала двигателя и схему, подключенную к датчику питания 4 и возврата. | Грязные или поврежденные контакты? |
|  | **STEP 2A-1.** Проверьте реакцию цепи. | Код 2186 активен? |
|  | **STEP 2B.** Проверить впускной коллектор 1 датчика давления и схему, подключенную к датчику питания 4 и возврата. | Грязные или поврежденные контакты? |
|  | **STEP 2B-1.** Проверьте реакцию цепи. | Код 2186 активен? |
|  | **STEP 2C** Проверить датчик давления и цепь, подключенные к датчику питания 4 и возврата, на рельсе учета топливного форсунка 1. | Грязные или поврежденные контакты? |
|  | **STEP 2C-1.** Проверьте реакцию цепи. | Код 2186 активен? |
|  | **STEP 2D.** Проверить барометрический датчик давления и схему, подключенную к датчику питания 4 и возврата. | Грязные или поврежденные контакты? |
|  | **STEP 2D-1.** Проверьте реакцию цепи. | Код 2186 активен? |
|  | **STEP 2E.** Проверить датчик давления подачи топлива и схему, подключенную к датчику подачи 4 и возврата. | Грязные или поврежденные контакты? |
|  | **ШАГ 2Е-1.** Проверьте реакцию цепи. | Код 2186 активен? |
|  | **STEP 2F.** Осмотрите датчик давления масляной винтовки и цепь, подключенную к датчику питания 4 и возвращайте. | Грязные или поврежденные контакты? |
|  | **STEP 2F-1.** Проверьте реакцию цепи. | Код 2186 активен? |
|  | **STEP 2G.** Осмотрите датчик давления в картере и схему, подключенную к датчику питания 4, и возвращайте, если они оборудованы. | Грязные или поврежденные контакты? |
|  | **STEP 2G-1.** Проверьте реакцию цепи. | Код 2186 активен? |
| ШАГ 3. | Проверьте ECM. |  |
|  | **STEP 3A.** Проверить контакты разъема ECM и проводов двигателя. | Грязные или поврежденные контакты? |
|  | **СТЭП 3В.** Проверить реакцию ECM. | Код 2186 активен? |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 2186 неактивен? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия:** Включите переключатель зажигания на электронном сервисном оборудовании Connect INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 2186 активен? *Да | 2А |
| Код 2186 активен? **НЕТ** | Используйте следующую процедуру для неактивного или прерывистого кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |  |

### ШАГ 2. Проверьте датчики и схемы, подключенные к датчику питания 4 и возвращайтесь.

#### ШАГ 2A. Осмотрите датчик скорости/положения распределительного вала двигателя и схему, подключенную к датчику питания 4 и возврата.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика скорости/положения распределительного вала двигателя от разъема жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы для проводов двигателя и разъёма датчика на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В датчике или разъёме жгута проводов было обнаружено поврежденное соединение. Очистите разъем и булавки. Замените поврежденный участок проводов двигателя ремнем или поврежденный датчик. См. схему или схему проводов для всех соединений проводов. См. процедуру 019-043 в разделе 19. См. процедуру 019-218 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2А-1-1 |  |

#### ШАГ 2A-1. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика скорости/положения распределительного вала двигателя от разъема жгута проводов двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующий ответ на ECM через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 2186 активен? *Да | 2В |
| Код 2186 активен? **NORepair:** Заменить датчик скорости/положения распределительного вала двигателя. См. процедуру 019-363 в разделе 19. | 4А |  |

#### ШАГ 2B. Осмотрите впускной коллектор 1 датчика давления и схему, подключенную к датчику питания 4 и возвращаемую.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика давления впускного коллектора 1 от разъема жгутов проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы для проводов двигателя и разъёма датчика на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. Замените поврежденный участок проводов двигателя ремнем или поврежденный датчик. См. схему или схему проводов для всех соединений проводов. См. процедуру 019-043 в разделе 19. См. процедуру 019-209 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В-1-1 |  |

#### ШАГ 2B-1. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика давления впускного коллектора 1 от разъема жгутов проводов двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующий ответ на ECM через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 2186 активен? *Да | 2C |
| Код 2186 активен? **NORepair:** Заменить датчик давления впускного коллектора 1. См. процедуру 019-061 в разделе 19. | 4А |  |

#### ШАГ 2C. Осмотрите датчик давления и цепь форсунки 1, подключенные к датчику питания 4 и возвращающиеся.

| **Условия:** Выключите замок зажигания. Отсоедините рельс 1 датчика давления форсунки от разъёма ремня жгута электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы для проводов двигателя и разъёма датчика на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. Замените поврежденный участок проводов двигателя ремнем или поврежденный датчик. См. схему или схему проводов для всех соединений проводов. См. процедуру 019-043 в разделе 19. См. процедуру 019-215 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2С-1 |  |

#### Шаг 2C-1 Проверьте реакцию цепи.

| **Условия:** Выключите замок зажигания. Отсоедините рельс 1 датчика давления форсунки от разъёма ремня жгута электропроводки двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующий ответ на ECM через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 2186 активен? *Да | 2D |
| Код 2186 активен? **NORepair:** Заменить датчик давления в рельсе 1 для измерения давления в топливной форсунке.[[123-019-115 — Rail Fuel Pressure Sensor\|См. процедуру 019-115 в разделе 19.]] | 4А |  |

#### ШАГ 2D. Осмотрите барометрический датчик давления и схему, подключенную к датчику питания 4 и возвращайте.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика барометрического давления от разъема жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы для проводов двигателя и разъёма датчика на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. Замените поврежденный участок проводов двигателя ремнем или поврежденный датчик. См. схему или схему проводов для всех соединений проводов. См. процедуру 019-043 в разделе 19. См. процедуру 019-218 в разделе 19. См. процедуру 019-390 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2D-1 |  |

#### ШАГ 2D-1. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика барометрического давления от разъема жгута проводов двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующий ответ на ECM через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 2186 активен? *Да | 2Е |
| Код 2186 активен? **Норэпар:** Поврежденный датчик барометрического давления обнаружен. Замените датчик барометрического давления. См. процедуру 019-004 в разделе 19. | 4А |  |

#### ШАГ 2E. Проверить датчик давления подачи топлива и схему, подключенную к датчику подачи 4 и возврата.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика давления подачи топлива от разъема жгутов проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы для проводов двигателя и разъёма датчика на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. Замените поврежденный участок проводов двигателя ремнем или поврежденный датчик. См. схему или схему проводов для всех соединений проводов. См. процедуру 019-043 в разделе 19. См. процедуру 019-209 в разделе 19. См. процедуру 019-390 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2Е-1 |  |

#### ШАГ 2E-1. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления подачи топлива от электропроводки двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующий ответ на ECM через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 2186 активен? *Да | 2F |
| Код 2186 активен? **NORepair:** Поврежденный датчик давления подачи топлива обнаружен. Заменить датчик давления подачи топлива. См. процедуру 019-398 в разделе 19. | 4А |  |

#### ШАГ 2F. Осмотрите датчик давления масляной винтовки и цепь, подключенную к датчику питания 4 и возвращайте.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика давления масляной винтовки от разъема жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы для проводов двигателя и разъёма датчика на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. Замените поврежденный участок проводов двигателя ремнем или поврежденный датчик. См. схему или схему проводов для всех соединений проводов. См. процедуру 019-043 в разделе 19. См. процедуру 019-209 в разделе 19. См. процедуру 019-390 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2F-1-1 |  |

#### ШАГ 2F-1. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления масляной винтовки от электропроводки двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующий ответ на ECM через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 2186 активен? *Да | 2G |
| Код 2186 активен? **НОРЭПАР:** Был обнаружен неисправный или поврежденный датчик давления масляной винтовки. Замените датчик давления масляной винтовки. См. процедуру 019-066 в разделе 19. | 4А |  |

#### ШАГ 2G. Осмотрите датчик давления и схему, подключенную к датчику питания 4 и возвращайте, если они оборудованы.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика давления картерного ящика от разъема жгута проводов двигателя, если он оборудован. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы для проводов двигателя и разъёма датчика на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. Замените поврежденный участок проводов двигателя ремнем или поврежденный датчик. См. схему или схему проводов для всех соединений проводов. См. процедуру 019-043 в разделе 19. См. процедуру 019-209 в разделе 19. См. процедуру 019-390 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2G-1 |  |

#### ШАГ 2G-1. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления картер от электропроводки двигателя, если он оборудован. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующий ответ на ECM через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 2186 активен? *Да | 3А |
| Код 2186 активен? **NORepair:** Выявлен неисправный или поврежденный датчик давления в картере. Замените датчик давления в картере, если он оборудован. См. процедуру 019-445 в разделе 19. | 4А |  |

### ШАГ 3. Проверьте ECM.

#### ШАГ 3A. Проверьте контакты разъема ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты электропроводки двигателя и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В разъеме ECM или в ремне электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. Заменить поврежденный участок проводов двигателя ремнем. См. схему или схему проводов для всех соединений жгутов проводов двигателя. См. процедуру 019-043 в разделе 19. См. процедуру 019-204 в разделе 19. Заменить ECM. См. процедуру 019-031 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте реакцию ECM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем электропроводки ремня от разъема ECM 60-pin. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующий ответ на ECM через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 2186 активен?  Заменить ЭКМ.[[123-019-031 — Engine Control Module\|См. процедуру 019-031 в разделе 19.]] | 4А |
| Код 2186 активен? **NORepair:** epair или замена жгута проводов двигателя.[[123-019-043 — Engine Wiring Harness\|См. процедуру 019-043 в разделе 19.]] | 4А |  |

### ШАГ 4. Сбросьте коды неисправностей.

#### ШАГ 4A. Отключите код неисправности.

| **Условия:** Подключите все компоненты Включите переключатель зажигания ON Connect INSITETM электронный сервисный инструмент. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код 2186 неактивен? *Да | 4B |
| Код 2186 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия:** Подключите все компоненты Включите переключатель зажигания ON Connect INSITETM электронный сервисный инструмент. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair:** Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие шаги по устранению неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3164596 - male Framatome™ test lead, and Part Number 3164597 - female Framatome™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for an active fault code. | Fault Code 2186 active? |
> | STEP 2. | Check the sensors and circuits connected to the sensor supply 4 and return. |  |
> |  | **STEP 2A.** Inspect the engine camshaft speed/position sensor and circuit connected to the sensor supply 4 and return. | Dirty or damaged pins? |
> |  | **STEP 2A-1.** Check the circuit response. | Fault Code 2186 active? |
> |  | **STEP 2B.** Inspect the intake manifold 1 pressure sensor and circuit connected to the sensor supply 4 and return. | Dirty or damaged pins? |
> |  | **STEP 2B-1.** Check the circuit response. | Fault Code 2186 active? |
> |  | **STEP 2C.** Inspect the injector metering rail 1 pressure sensor and circuit connected to the sensor supply 4 and return. | Dirty or damaged pins? |
> |  | **STEP 2C-1.** Check the circuit response. | Fault Code 2186 active? |
> |  | **STEP 2D.** Inspect the barometric pressure sensor and circuit connected to the sensor supply 4 and return. | Dirty or damaged pins? |
> |  | **STEP 2D-1.** Check the circuit response. | Fault Code 2186 active? |
> |  | **STEP 2E.** Inspect the fuel delivery pressure sensor and circuit connected to the sensor supply 4 and return. | Dirty or damaged pins? |
> |  | **STEP 2E-1.** Check the circuit response. | Fault Code 2186 active? |
> |  | **STEP 2F.** Inspect the oil rifle pressure sensor and circuit connected to the sensor supply 4 and return. | Dirty or damaged pins? |
> |  | **STEP 2F-1.** Check the circuit response. | Fault Code 2186 active? |
> |  | **STEP 2G.** Inspect the crankcase pressure sensor and circuit connected to the sensor supply 4 and return, if equipped. | Dirty or damaged pins? |
> |  | **STEP 2G-1.** Check the circuit response. | Fault Code 2186 active? |
> | STEP 3. | Check the ECM. |  |
> |  | **STEP 3A.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the ECM response. | Fault Code 2186 active? |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 2186 inactive? |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for an active fault code.
>
> | **Conditions:** Turn keyswitch ON Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2A |
> | Fault Code 2186 active? **NO** | Use the following procedure for an inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |
>
> ### STEP 2. Check the sensors and circuits connected to the sensor supply 4 and return.
>
> #### STEP 2A. Inspect the engine camshaft speed/position sensor and circuit connected to the sensor supply 4 and return.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine camshaft speed/position sensor connector from the engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection had been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-218 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2A-1 |  |
>
> #### STEP 2A-1. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine camshaft speed/position sensor connector from the engine harness connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 30 seconds. Use INSITE ™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2B |
> | Fault Code 2186 active? **NORepair:** Replace the engine camshaft speed/position sensor. Refer to Procedure 019-363 in Section 19. | 4A |  |
>
> #### STEP 2B. Inspect the intake manifold 1 pressure sensor and circuit connected to the sensor supply 4 and return.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the intake manifold 1 pressure sensor connector from the engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-209 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2B-1 |  |
>
> #### STEP 2B-1. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the intake manifold 1 pressure sensor connector from the engine harness connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2C |
> | Fault Code 2186 active? **NORepair:** Replace the intake manifold 1 pressure sensor. Refer to Procedure 019-061 in Section 19. | 4A |  |
>
> #### STEP 2C. Inspect the injector metering rail 1 pressure sensor and circuit connected to the sensor supply 4 and return.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the injector metering rail 1 pressure sensor connector from the engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-215 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2C-1 |  |
>
> #### STEP 2C-1 Check the circuit response..
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the injector metering rail 1 pressure sensor connector from the engine harness connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2D |
> | Fault Code 2186 active? **NORepair:** Replace the injector metering rail 1 pressure sensor. [[123-019-115 — Rail Fuel Pressure Sensor\|Refer to Procedure 019-115 in Section 19.]] | 4A |  |
>
> #### STEP 2D. Inspect the barometric pressure sensor and circuit connected to the sensor supply 4 and return.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the barometric pressure sensor connector from the engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-218 in Section 19. Refer to Procedure 019-390 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2D-1 |  |
>
> #### STEP 2D-1. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the barometric pressure sensor connector from the engine harness connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2E |
> | Fault Code 2186 active? **NORepair:** A damaged barometric pressure sensor has been detected. Replace the barometric pressure sensor. Refer to Procedure 019-004 in Section 19. | 4A |  |
>
> #### STEP 2E. Inspect the fuel delivery pressure sensor and circuit connected to the sensor supply 4 and return.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the fuel delivery pressure sensor connector from the engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-209 in Section 19. Refer to Procedure 019-390 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2E-1 |  |
>
> #### STEP 2E-1. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the fuel delivery pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2F |
> | Fault Code 2186 active? **NORepair:** A damaged fuel delivery pressure sensor has been detected. Replace the fuel delivery pressure sensor. Refer to Procedure 019-398 in Section 19. | 4A |  |
>
> #### STEP 2F. Inspect the oil rifle pressure sensor and circuit connected to the sensor supply 4 and return.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the oil rifle pressure sensor connector from the engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-209 in Section 19. Refer to Procedure 019-390 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2F-1 |  |
>
> #### STEP 2F-1. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the oil rifle pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2G |
> | Fault Code 2186 active? **NORepair:** A malfunctioning or damaged oil rifle pressure sensor has been detected. Replace the oil rifle pressure sensor. Refer to Procedure 019-066 in Section 19. | 4A |  |
>
> #### STEP 2G. Inspect the crankcase pressure sensor and circuit connected to the sensor supply 4 and return, if equipped.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the crankcase pressure sensor connector from the engine harness connector, if equipped. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-209 in Section 19. Refer to Procedure 019-390 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2G-1 |  |
>
> #### STEP 2G-1. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the crankcase pressure sensor from the engine harness, if equipped. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 3A |
> | Fault Code 2186 active? **NORepair:** A malfunctioning or damaged crankcase pressure sensor has been detected. Replace the crankcase pressure sensor, if equipped. Refer to Procedure 019-445 in Section 19. | 4A |  |
>
> ### STEP 3. Check the ECM.
>
> #### STEP 3A. Inspect the ECM and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or engine harness. Clean the connector and pins. Replace the damaged section of the engine harness. Refer to the circuit art or wiring diagram for all engine harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the ECM response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YESRepair:** Replace the ECM. [[123-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19.]] | 4A |
> | Fault Code 2186 active? **NORepair:** epair or replace the engine harness. [[123-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |  |
>
> ### STEP 4. Clear the fault codes.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components Turn keyswitch ON Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 2186 inactive? **YES** | 4B |
> | Fault Code 2186 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components Turn keyswitch ON Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting steps |  |
