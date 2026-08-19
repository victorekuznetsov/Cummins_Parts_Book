---
aliases:
  - "Код 2727 — сеть SAE J1939 №2 — недопустимая частота обновления"
type: "Процедура"
doc: "122-t05-2727"
title_en: "FAULT CODE 2727 - SAE J1939 Data Link 2 Engine Network - Abnormal Update Rate"
title_ru: "Код 2727 — сеть SAE J1939 №2 — недопустимая частота обновления"
modified: "2015-09-18"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-2727.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-2727.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 2727 - SAE J1939 Data Link 2 Engine Network - Abnormal Update Rate
**Код 2727 — сеть SAE J1939 №2 — недопустимая частота обновления**

> [!abstract] Процедура · `122-t05-2727`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-09-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-2727.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-2727.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 — пробный щуп типа штепсельной заглушки DeutschTM/AMPTM/Metri-PackTM, номер детали 3822917 — пробный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM, а номер детали 3823995 — штыревой пробный щуп Weather PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить наличие активного кода неисправности. | Код 2727 активен? |
| ШАГ 2. | Проверьте оригинальную электропроводку производителя оборудования (OEM) и электропроводку двигателя. |  |
|  | **STEP 2A.** Проверить 4-контактный разъем питания и контакты разъема ECM. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте наличие открытой цепи в цепях питания аккумулятора. | Напряжение от 10,0 до 15,0-VDC для системы 12 вольт или от 21 до 27-VDC для системы 24 вольт? |
|  | **STEP 2C.** Проверьте источник питания аккумулятора на короткое замыкание от контакта к контакту. | Больше 100 тысяч ом? |
|  | **STEP 2D.** Проверьте надстройку или вспомогательную проводку в положительном (+) терминале батареи. | Поврежденные провода? |
|  | **ШАГ 2Е.** Проверить провод входа-в-ECM зажигания. | Провод зажигания бесперебойный? |
|  | **STEP 2F.** Проверьте схему входа зажигания. | Менее 5 Ом? |
| ШАГ 3. | Проверить Общество автомобильной инженерии (SAE) J1939 CAN данных шины 2 схемы. |  |
|  | **STEP 3A.** Проверить все контакты разъема жгута электропроводки двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте устойчивость шины данных SAE J1939 CAN 2 в ремне электропроводки двигателя. | От 54 до 66 Ом? |
|  | **STEP 3C.** Проверьте резистор-терминатор сети шин данных SAE J1939 CAN 2. | От 108 до 132 Ом? |
|  | **STEP 3D.** Проверьте связь ECM с электронным сервисом INSITETM. | Общается ли ECM? |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 2727 неактивен? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте активный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 2727 активен? *Да** | 2А |
| Код 2727 активен? ** НЕТ** | Используйте следующую процедуру для неактивного или прерывистого кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |  |

### ШАГ 2. Проверьте OEM силовую проводку и электропроводку двигателя.

#### ШАГ 2A. Проверьте 4-контактный разъем питания и контакты разъема ECM.

| **Условия:** Выключите замок зажигания. Отключите 4-контактный разъем питания от ECM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить контакты разъёма электропроводки ECM и разъёма ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или разъема разъема разъема разъема изоляции Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? *** Ремонт:** Очистить разъем и штифты. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом. Ремонт ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 4А |
| Грязные или поврежденные контакты? ** НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте наличие открытой цепи в цепях питания батареи.

| **Условия: ** Ссылка на схему схемы или схему проводов для контакта с разъемом для идентификации. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте наличие открытой цепи в цепях питания батареи. Измерьте напряжение между контактом питания батареи в 4-контактном разъеме питания с заземлением блока двигателя. Ссылка на схему схемы или схему проводов для контакта с разъемом для идентификации. | Напряжение от 10,0 до 15,0 ВДК для системы 12 вольт или от 21 до 27 ВДК для системы 24 вольт? *Да** | 2C |
| Напряжение от 10,0 до 15,0 ВДК для системы 12 вольт или от 21 до 27 ВДК для системы 24 вольт? **NORepair:** Устранение неполадок во всех проводных упряжках, соединенных последовательно, для определения того, какая из них содержит открытую цепь. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом. Ремонт ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 2C. Проверьте источник питания батареи для короткого замыкания от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините 4-контактный разъём силовой проводов от разъема ECM. Отключите провода батареи. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте короткое замыкание от пин-кодов до пин-кодов. Измерьте сопротивление от контакта питания питания батареи в 4-контактном разъеме питания ко всем другим штифтам в разъеме. Измерьте сопротивление от обратного контакта напряжения батареи в 4-контактном разъеме питания ко всем другим штифтам в разъеме. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да** | 2D |
| Больше 100 тысяч ом? **NORepair:** Устранение неполадок во всех проводных упряжках, соединенных последовательно, для определения того, в какой из них содержится короткое замыкание. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом. Ремонт ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 2D. Проверьте надстройку или вспомогательную проводку в положительном (+) терминале батареи.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте надстройку или вспомогательную проводку в положительном (+) терминале батареи. Начиная с положительного (+) терминала батареи, следуйте любой надстройке или вспомогательной проводах и проверьте провод(ы) на наличие поврежденной изоляции или ошибки установки, которая может привести к тому, что подающий провод будет сокращен блоком двигателя. | Поврежденные провода? *** Ремонт: ** Ремонт или замена поврежденных проводов. См. сервисное руководство изготовителя машины. | 4А |
| Поврежденные провода? ** НЕТ** | 2Е |  |

#### ШАГ 2E. Проверьте провод входа зажигания в ECM.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте провод входа зажигания в ECM. Проверить провод зажигания от поста зажигания в сборе зажигания до ECM, чтобы убедиться, что в проводе нет прерываний, то есть нет соленоидов или реле. | Провод переключателя зажигания бесперебойный? *Да** | 2F |
| Провод переключателя зажигания бесперебойный? **NORepair: ** Исправьте проводку так, чтобы провод был бесперебойным. | 4А |  |

#### ШАГ 2F. Проверьте схему входа зажигания.

| **Условия:** Выключите замок зажигания. Отсоедините разъем электропроводки жгута двигателя от разъема ECM 50-pin. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте схему входа зажигания. Измерить сопротивление от положения зажигания в сборе зажигания до контакта подачи зажигания 50-контактного разъёма проводов двигателя. | Менее 5 Ом? *Да** | 3А |
| Менее 5 Ом? **NORepair:** Устранение неполадок во всех проводных упряжках, соединенных последовательно, для определения того, в какой из них содержится короткое замыкание. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом. Ремонт ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 4А |  |

### ШАГ 3. Проверьте схему шины данных SAE J1939 CAN 2.

#### ШАГ 3A. Проверьте контакты разъема жгута проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините проводку двигателя от 60-контактного разъема от ECM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Осмотрите разъём ремней электропроводки двигателя и контакты разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или разъема разъема разъема разъема изоляции Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В разъеме жгутов проводов двигателя или разъеме ECM обнаружено поврежденное соединение. Смой грязь, мусор или влагу из контактов разъема. Используйте электрическую контактную очистку, номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт поврежденных контактов. Ремонт или замена жгута проводов двигателя, OEM жгута проводов или замена ECM, в зависимости от того, какие контакты повреждены. Заменить поврежденный участок ремня электропроводки двигателя или ECM. См. процедуру 019-043 в разделе 19. Замените проводку OEM. См. процедуру См. процедуру 019-071 в разделе 19. Заменить ECM. См. процедуру 019-031 в разделе 19. | 3D |
| Грязные или поврежденные контакты? ** НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте устойчивость сети SAE J1939 CAN 2 в ремне электропроводки двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините разъем электропроводки ремня от разъема ECM 60-pin. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте устойчивость сети SAE J1939 CAN 2 к шине данных двигателя. Измерить сопротивление между контактом питания сети питания шины данных SAE J1939 CAN 2 и обратным контактом шины данных SAE J1939 CAN 2 в разъеме электропроводки двигателя ECM. См. схему или схему проводов для контакта с разъемом для идентификации. Используйте следующую процедуру для общих методов измерения сопротивления. См. процедуру 019-360 в разделе 19. | От 54 до 66 Ом? *** Сопротивление сети шин данных SAE J1939 CAN 2 двигателя находится в заданных пределах. В калибровке есть проблема. Проверьте, чтобы убедиться, что соответствующие калибровки установлены в ECM. | 3D |
| От 54 до 66 Ом? ** НЕТ** | 3C |  |

#### ШАГ 3C. Проверьте резистор-терминатор SAE J1939 CAN 2.

| **Условия:** Выключите замок зажигания. Отсоедините разъем электропроводки ремня от разъема ECM 60-pin. Отсоедините один из резисторов системы обработки данных SAE J1939 CAN 2 от жгутов проводов электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте устойчивость сети SAE J1939 CAN 2 к шине данных двигателя. Измерить сопротивление между контактом питания сети питания шины данных SAE J1939 CAN 2 и обратным контактом шины данных SAE J1939 CAN 2 в разъеме электропроводки двигателя ECM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления. См. процедуру 019-360 в разделе 19. | От 108 до 132 Ом? *** Удаленный резистор-терминатор SAE J1939 CAN 2 сети движков поврежден. Заменить резистор-терминатор сети SAE J1939 CAN 2. См. процедуру 019-428 в разделе 19. | 3D |
| От 108 до 132 Ом? **NORepair:** Обнаружен открытый или короткоствольный двигатель SAE J1939 CAN шины 2 передачи данных или поврежденный резистор терминатора, все еще подключенный к электропроводке ремня. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов двигателя ремнем. См. процедуру 019-043 в разделе 19. Замените резистор теминатора. См. процедуру 019-428 в разделе 19. | 3D |  |

#### ШАГ 3D. Проверьте связь ECM с электронным сервисным оборудованием INSITETM.

| **Условия:** Электронный сервисный инструмент INSITETM, подключенный к автомобилю. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте связь между электронным сервисным оборудованием INSITETM и ECM. Используйте инструмент электронного сервиса INSITETM для проверки связи с ECM. | Общается ли ECM? *Да** | 4А |
| Общается ли ECM? ** НЕТ** | Ссылка на ECM - № Communication Troubleshooting Tree в разделе TT. |  |

### ШАГ 4. Сбросьте коды неисправностей.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: ** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код 2727 неактивен? *Да** | 4B |
| Код 2727 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 4B |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия: ** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да** | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair:** Устранение неполадок с оставшимися кодами неисправностей. | Соответствующие шаги по устранению неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, and Part Number 3823995 - male Weather Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for an active fault code. | Fault Code 2727 active? |
> | STEP 2. | Check the original equipment manufacturer (OEM) power harness and engine harness. |  |
> |  | **STEP 2A.** Inspect the 4-pin power connector and the ECM connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check for an open circuit in the battery power circuits. | Voltage between 10.0 to 15.0-VDC for 12 volt system or 21 to 27-VDC for 24 volt system? |
> |  | **STEP 2C.** Check the battery supply for a short circuit from pin-to-pin. | Greater than 100k ohms? |
> |  | **STEP 2D.** Check the add-on or accessory wiring at the positive (+) battery terminal. | Damaged wires? |
> |  | **STEP 2E.** Check the ignition input-to-ECM wire. | Ignition wire uninterrupted? |
> |  | **STEP 2F.** Check the ignition input circuit. | Less than 5 ohms? |
> | STEP 3. | Check the Society of Automotive Engineering (SAE) J1939 data link 2 circuit. |  |
> |  | **STEP 3A.** Inspect all engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the SAE J1939 data link 2 engine network resistance in the engine harness. | Between 54 to 66 ohms? |
> |  | **STEP 3C.** Check the SAE J1939 data link 2 engine network terminator resistor. | Between 108 to 132 ohms? |
> |  | **STEP 3D.** Check for ECM communication to INSITE™ electronic service tool. | Does the ECM communicate? |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 2727 inactive? |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for an active fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2727 active? **YES** | 2A |
> | Fault Code 2727 active? **NO** | Use the following procedure for an inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |
>
> ### STEP 2. Check the OEM power harness and engine harness.
>
> #### STEP 2A. Inspect the 4-pin power connector and the ECM connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 4-pin power connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the ECM harness connector and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Repair the engine harness. Refer to Procedure 019-043 in Section 19. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check for an open circuit in the battery power circuits.
>
> | **Conditions:** Reference the circuit diagram or wiring diagram for connector pin for identification. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit in the battery power circuits. Measure the voltage between the battery voltage SUPPLY pin in the 4-pin power connector to engine block ground. Reference the circuit diagram or wiring diagram for connector pin for identification. | Voltage between 10.0 to 15.0 VDC for 12 volt system or 21 to 27 VDC for 24 volt system? **YES** | 2C |
> | Voltage between 10.0 to 15.0 VDC for 12 volt system or 21 to 27 VDC for 24 volt system? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Repair the engine harness. Refer to Procedure 019-043 in Section 19. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 2C. Check the battery supply for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 4-pin power harness connector from the ECM connector. Disconnect the battery leads. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin to pin. Measure the resistance from a battery voltage SUPPLY pin in the 4-pin power connector to all other pins in the connector. Measure the resistance from a battery voltage RETURN pin in the 4-pin power connector to all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 2D |
> | Greater than 100k ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Repair the engine harness. Refer to Procedure 019-043 in Section 19. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 2D. Check the add-on or accessory wiring at the positive (+) battery terminal.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the add-on or the accessory wiring at the positive (+) battery terminal. Starting at the positive (+) battery terminal, follow any add-on or accessory wiring, and examine the wire(s) for damaged insulation or an installation error that can cause the supply wire to be shorted the engine block. | Damaged wires? **YESRepair:** Repair or replace the damaged wires. Refer to the OEM service manual. | 4A |
> | Damaged wires? **NO** | 2E |  |
>
> #### STEP 2E. Check the ignition input-to-ECM wire.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ignition input-to-ECM wire. Inspect the ignition wire from the ignition post in the ignition assembly to the ECM to make sure there are no interruptions in the wire, that is, no solenoids or relays. | Keyswitch wire uninterrupted? **YES** | 2F |
> | Keyswitch wire uninterrupted? **NORepair:** Correct the wiring so the wire is uninterrupted. | 4A |  |
>
> #### STEP 2F. Check the ignition input circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 50-pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ignition input circuit. Measure the resistance from the ignition post in the ignition assembly to the ignition input SUPPLY pin of the 50-pin engine harness connector. | Less than 5 ohms? **YES** | 3A |
> | Less than 5 ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Repair the engine harness. Refer to Procedure 019-043 in Section 19. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> ### STEP 3. Check the SAE J1939 data link 2 circuit.
>
> #### STEP 3A. Inspect the engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness 60-pin connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness connector and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the engine harness connector or ECM connector. Flush the dirt, debris, or moisture from the connector pins. Use electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the damaged pins. Repair or replace the engine harness, OEM harness, or replace the ECM, whichever has the damaged pins. Replace the damaged section of the engine harness or the ECM. Refer to Procedure 019-043 in Section 19. Replace the OEM harness. Refer to Procedure Refer to Procedure 019-071 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 3D |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the SAE J1939 data link 2 engine network resistance in the engine harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link 2 engine network resistance. Measure the resistance between the SAE J1939 data link 2 engine network SUPPLY pin and the SAE J1939 data link 2 engine network RETURN pin in the ECM engine harness connector. Refer to the circuit diagram or wiring diagram for connector pin for identification. Use the following procedure for general resistance measurement techniques. Refer to Procedure 019-360 in Section 19. | Between 54 to 66 ohms? **YESRepair:** The SAE J1939 data link 2 engine network resistance is within specification. There is a problem in the calibration. Check to make sure the appropriate calibrations are installed in the ECMs. | 3D |
> | Between 54 to 66 ohms? **NO** | 3C |  |
>
> #### STEP 3C. Check the SAE J1939 data link 2 engine network terminator resistor.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin connector. Disconnect one of the SAE J1939 data link 2 engine network terminator resistors from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link 2 engine network resistance. Measure the resistance between the SAE J1939 data link 2 engine network SUPPLY pin and the SAE J1939 data link 2 engine network RETURN pin in the ECM engine harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. Refer to Procedure 019-360 in Section 19. | Between 108 to 132 ohms? **YESRepair:** The removed SAE J1939 data link 2 engine network terminator resistor is damaged. Replace the SAE J1939 data link 2 engine network terminator resistor. Refer to Procedure 019-428 in Section 19. | 3D |
> | Between 108 to 132 ohms? **NORepair:** An open or shorted engine SAE J1939 data link 2 circuit or damaged terminator resistor still connected to the harness has been detected. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the engine harness. Refer to Procedure 019-043 in Section 19. Replace the teminator resistor. Refer to Procedure 019-428 in Section 19. | 3D |  |
>
> #### STEP 3D. Check for ECM communication to INSITE™ electronic service tool.
>
> | **Conditions:** INSITE™ electronic service tool connected to the vehicle. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for communication between INSITE™ electronic service tool and the ECM. Use INSITE™ electronic service tool to check for communication with the ECM. | Does the ECM communicate? **YES** | 4A |
> | Does the ECM communicate? **NO** | Reference the ECM - No Communication Troubleshooting Tree in Section TT. |  |
>
> ### STEP 4. Clear the fault codes.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 2727 inactive? **YES** | 4B |
> | Fault Code 2727 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 4B |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Appropriate troubleshooting steps |  |
