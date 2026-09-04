---
aliases:
  - "Останов: разница температур ОГ по рядам"
type: "Процедура"
doc: "330-t02-1032"
title_en: "Sd EGTBankDelta"
title_ru: "Останов: разница температур ОГ по рядам"
modified: "2017-03-03"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "4358403"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1032.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1032.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/330"
  - "перевод/машинный"
---

# Sd EGTBankDelta
**Останов: разница температур ОГ по рядам**

> [!abstract] Процедура · `330-t02-1032`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[4358403 — Dual Fuel Technology DF101 Master Repair Manual|4358403]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2017-03-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1032.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1032.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

Двухтопливная работа будет остановлена.

Весь поток газа остановится, если система работает в режиме двойного топлива.

EGT Delta представляет собой анализ температурного баланса выхлопных газов на основе температуры входного отверстия катализатора окисления дизельного топлива (DOC). Если измеренная температура имеет абсолютную разницу (дельту), превышающую заданную заданную точку, модуль управления двойным топливом отключает работу двойного топлива.

### Как пользоваться этим деревом

Это дерево можно использовать для устранения неисправности. Начните с шага 1 поиска неисправностей. Шаг 2 задаст ряд вопросов и предоставит список шагов по устранению неполадок, в зависимости от симптома.

**Описание:**

В любое время модуль управления включен.

**Условия активации сообщения об ошибке:**

Модуль управления двойным топливом приводится в действие, и измеренные температуры входа DOC варьируются больше, чем заданная точка. Система будет указывать на это сообщение и защиту.

**Условия автоматической очистки кодов по умолчанию:**

Нет.

**Условия для очистки кодов ошибок вручную:**

Сброс неисправностей осуществляется локально или с помощью программного обеспечения.

### Практические замечания

В сообщении указывается на неприемлемые различия в температурах выхлопных газов между банками.

Предыдущее использование модуля управления двигателем (ECM) с удельной температурой цилиндра было удалено из-за частых неисправностей термопары цилиндра.

Предыдущее использование расчетных средних ECM для температуры выхлопных газов в банках было удалено из-за частых неисправностей на одну термопару цилиндров.

Возможные причины включают:

- Неисправная термопара или термопарная проводка

- Включенные или ограниченные DOC или глушители, вызывающие повышенные температуры.

Несбалансированная доставка газа из банка в банк в связи со следующим:

- Различия в ограничении впускного воздуха от одного банка к другому

- Различия в производительности турбокомпрессора от одного банка к другому

- Различия в ограничении сантехники от одного банка к другому

- Утечки в системе воздухозаборника на прокладках, шлангах, зажимах и воздушных кроссоверах.

| Код сообщения | Причина | Последствия |
|---|---|---|
| Дельта Sd EGT | Температура выхлопных газов несбалансирована между левым и правым (A/B) банками. | Модуль двойного управления топливом не позволит работать с газом. Модуль управления двойным топливом остановит поток газа. |

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверить сообщение о вине. |  |
|  | **STEP 1A.** Проверить коды неисправностей двигателя. | Есть коды неисправностей, связанные с двигателем? |
|  | **STEP 1B** Проверить наличие дополнительных систем сигнализации. | Другие сообщения о выключении для бинарных входов произошли одновременно с Sd EGTBankDelta? |
|  | **STEP 1C.** Проверить сообщение об ошибке. | Модуль управления в неисправном состоянии? |
| ШАГ 2. | Мониторинг датчиков температуры. |  |
|  | **STEP 2A.** Мониторинг датчиков температуры выхлопных газов после обработки. | Датчики температуры DOC левого и правого берега изменяются более чем на 24 ° C или 43 ° F друг с другом с помощью InteliMonitor. |
|  | **STEP 2B** Мониторинг датчиков температуры выхлопных газов после обработки. | Датчики температуры на входе DOC левого и правого берега в пределах 38 ° C \[100° F \] друг от друга? |
|  | **STEP 2C.** Проверьте ограничение потребления. | Элементы воздухоочистителя грязные или ограниченные? |
|  | **STEP 2D.** Проверка на наличие утечек впускной и выхлопной систем. | Утечки, обнаруженные в системах воздухозаборника или выхлопных газов? |
|  | **ШАГ 2Е.** Проверить газовые линии. | Какие-нибудь повреждения на газовых линиях? |
|  | **ШАГ 2F.** Проверьте воздушные трубы. | Какие-нибудь повреждения на линии сжатого воздуха? |
|  | **STEP 2G.** Проверьте работу турбокомпрессора. | Какие-либо измерения в разделе «Опыт повторного использования» выходят за пределы установленных пределов? |
|  | **STEP 2H.** Проверьте работу DOC. | Какие-нибудь обломки или повреждения, найденные на DOC? |
| ШАГ 3. | Снимите вину. |  |
|  | **СТАП 3А.** Сбросить вину. | Вернулись? |

### ШАГ 1. Проверить сообщение о вине.

#### ШАГ 1A. Проверьте коды неисправностей двигателя.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Есть коды неисправностей, связанные с двигателем? *Да | Перейдите к соответствующему дереву устранения неисправностей кода ошибки. |
| Есть коды неисправностей, связанные с двигателем? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте наличие дополнительных систем сигнализации.

| **Условия: **Модуль управления питанием на двухтопливном топливе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подключайтесь к панели управления двойным топливом. Используйте InteliMonitor. Сохраните копию файла конфигурации модуля управления (архивного файла) на локальном ПК. Доступ к короткому пути истории. Проверьте наличие сообщений Sd EGTBankDelta. Проверяйте другие сообщения о выключении, происходящие в момент или около времени Sd EGTBankDelta. | Другие сообщения о выключении для бинарных входов произошли одновременно с Sd EGTBankDelta? **Ремонт: **Если другие сообщения о выключении для бинарных входов происходят одновременно, см. следующую процедуру для наземных и наземных измерительн.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | 2А |
| Другие сообщения о выключении для бинарных входов произошли одновременно с Sd EGTBankDelta? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте «активное» сообщение о вине.

| **Условия: **Модуль управления питанием на двухтопливном топливе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте локальную панель отображения для сообщения о неисправности. Навигация на экран дисплея с ошибкой. | Модуль управления в неисправном состоянии? *Да | 2А |
| Модуль управления в неисправном состоянии? **НЕТ** | 2В |  |

### ШАГ 2. Мониторинг датчиков температуры.

#### ШАГ 2A. Мониторинг датчиков температуры выхлопных газов после обработки.

| **Условия: **Модуль управления питанием на двухтопливном топливе. Ключ включен, двигатель не работает. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подключайтесь к двойной топливной панели. Используйте InteliMonitor. Сохраните копию файла конфигурации (архивного файла) на локальном ПК. Если возникают какие-либо коды неисправностей, см. соответствующее дерево устранения неисправностей кода неисправностей. Если не происходит никаких кодов неисправностей, запишите значения трех датчиков температуры выхлопных газов после обработки. | Датчики температуры DOC левого и правого берега изменяются более чем на 24 ° C или 43 ° F друг с другом с помощью InteliMonitor. **Ремонт:** Проверьте короткое замыкание от сигнального контакта датчика температуры до всех других штифтов в проводах. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]]Если не найдено короткого считывания, замените датчик температуры, считывающий выше или ниже, чем другие датчики. См. процедуру 019-449 в разделе 19. | 3А |
| Датчики температуры DOC левого и правого берега изменяются более чем на 24 ° C или 43 ° F друг с другом с помощью InteliMonitor. **НЕТ** | Обратитесь в авторизованный сервисный центр Cummins®. |  |

#### ШАГ 2B. Мониторинг датчиков температуры выхлопных газов после обработки.

| **Условия:** Включить модуль управления двойным топливом. Сбросьте неисправность на панели. Запуск двигателя на частоте от 1500 до 2000 оборотов в минуту для удовлетворения условий эксплуатации для работы с двойным топливом. Включите газовый регулятор на панели в режим выключения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте локальную панель отображения для сообщения о неисправности. Мониторинг левого и правого бортового датчика температуры входа DOC в режиме Diesel Only. | Датчики температуры на входе DOC левого и правого берега в пределах 38 ° C \[100° F \] друг от друга? *Да | 3А |
| Датчики температуры на входе DOC левого и правого берега в пределах 38 ° C \[100° F \] друг от друга? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте ограничение потребления.

| **Условия: **Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте элементы воздухоочистителя. Используйте GTA38, K38, K50, QSK38 и QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 010-014 в разделе 10. | Элементы воздухоочистителя грязные или ограниченные? **Ремонт:** Очистить или заменить фильтрующий элемент воздухоочистителя. См. сервисную документацию изготовителя оборудования. | 3А |
| Элементы воздухоочистителя грязные или ограниченные? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте на наличие утечек впускной и выхлопной систем.

| **Условия: **Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте воздухозаборник и выхлопную систему на наличие утечек. Используйте GTA38, K38, K50, QSK38 и QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 010-024 в разделе 10. | Утечки, обнаруженные в системах воздухозаборника или выхлопных газов? **Ремонт:** Ремонт источника утечки. Используйте GTA38, K38, K50, QSK38 и QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 010-024 в разделе 10. | 3А |
| Утечки, обнаруженные в системах воздухозаборника или выхлопных газов? **НЕТ** | 2Е |  |

#### ШАГ 2E. Проверьте газовые линии.

| **Условия: **Выключите двигатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить газовые линии на предмет повреждения. См. процедуру 005-248 в разделе 5. | Какие-нибудь повреждения на газовых линиях? Заменить поврежденную часть газовой линии. См. процедуру 005-248 в разделе 5. | 3А |
| Какие-нибудь повреждения на газовых линиях? **НЕТ** | 2F |  |

#### ШАГ 2F. Проверьте воздушные трубы.

| **Условия: **Выключите двигатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить воздушные трубопроводы на предмет повреждения. См. процедуру 005-248 в разделе 5. | Какие-нибудь повреждения на линии сжатого воздуха? **Ремонт:** Заменить поврежденную часть линии сжатого воздуха. См. процедуру 005-248 в разделе 5. | 3А |
| Какие-нибудь повреждения на линии сжатого воздуха? **НЕТ** | 2G |  |

#### ШАГ 2G. Проверьте работу турбокомпрессора.

| **Условия: **Выключите двигатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте зазоры турбокомпрессора. Используйте GTA38, K38, K50, QSK38 и QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 010-033 в разделе 10. | Какие-либо измерения в разделе «Опыт повторного использования» выходят за пределы установленных пределов? **Ремонт:** Ремонт или замена турбокомпрессора. Используйте GTA38, K38, K50, QSK38 и QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]].[[28-010-033-tr — Turbocharger\|См. процедуру 010-033 в разделе 10.]] | 3А |
| Какие-либо измерения в разделе «Опыт повторного использования» выходят за пределы установленных пределов? **НЕТ** | 2 ч. |  |

#### ШАГ 2H. Проверьте работу DOC.

| **Условия: **Выключите двигатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить DOC на предмет повреждений или наращивания. См. процедуру 011-049 в разделе 11. | Какие-нибудь обломки или повреждения, найденные на DOC? **Ремонт: **Очистить или заменить DOC. См. процедуру 011-049 в разделе 11. | 3А |
| Какие-нибудь обломки или повреждения, найденные на DOC? **НЕТ** | 3А |  |

### ШАГ 3. Снимите вину.

#### ШАГ 3A. Снимите вину.

| **Условия: **Двигатель не работает. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отложите неисправность на панели управления или через InteliMonitor. Работайте с двигателем в условиях, позволяющих замену газа. | Вернулись? Возвращение к шагам устранения неполадок или обращение в авторизованное место ремонта Cummins®, если все шаги были завершены и проверены повторно. | 1А |
| Вернулись? **НЕТ** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> Dual fuel operation will be stopped.
>
> All gas flow will stop if the system is operating in dual fuel mode.
>
> EGT Delta is an analysis of the exhaust gas temperature balance based on the diesel oxidation catalyst (DOC) inlet temperatures. If the measured temperature has an absolute difference (delta) exceeding the defined set-point, the dual fuel control module shuts down dual fuel operation.
>
> ### How To Use This Tree
>
> This tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending up the symptom.
>
> **Circuit Description:**
>
> Anytime the control module is powered ON.
>
> **Conditions for Activating the Fault Message:**
>
> The dual fuel control module is powered ON and the measured DOC inlet temperatures vary greater than the set-point. The system will indicate this message and protection.
>
> **Conditions for Clearing the Fault Codes Automatically:**
>
> None.
>
> **Conditions for Clearing the Fault Codes Manually:**
>
> The fault reset is operated locally or via software.
>
> ### Shoptalk
>
> The message indicates unacceptable differences in bank-to-bank exhaust gas temperatures.
>
> Previous use of engine control module (ECM) cylinder specific temperatures was removed due to frequent per cylinder thermocouple malfunctions.
>
> Previous use of ECM calculated averages for bank exhaust gas temperature was removed due to frequent per cylinder thermocouple malfunctions.
>
> Possible causes include:
>
> - Malfunctioning thermocouple or thermocouple wiring
>
> - Plugged or restricted DOC or silencers causing elevated temperatures.
>
> Imbalanced bank-to-bank gas delivery due to the following:
>
> - Differences in intake air restriction from one bank to the other
>
> - Differences in turbocharger performance from one bank to the other
>
> - Differences in plumbing restriction from one bank to the other
>
> - Leaks in the intake air system at gaskets, hoses, clamps, and air crossover connections.
>
> | Code of Message | Reason | Effect |
> |---|---|---|
> | Sd EGT Delta | Exhaust gas temperatures are imbalanced between the left and right (A/B) banks. | The dual fuel control module will not allow gas operations. The dual fuel control module will stop gas flow. |
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Validate the fault message. |  |
> |  | **STEP 1A.** Check for engine fault codes. | Any engine related fault codes? |
> |  | **STEP 1B.** Check for additional gas system alarms. | Other shutdown messages for binary inputs occurred at the same time as Sd EGTBankDelta? |
> |  | **STEP 1C.** Check for 'Active' fault message. | Control module in fault condition? |
> | STEP 2. | Monitor the temperature sensors. |  |
> |  | **STEP 2A.** Monitor the aftertreatment exhaust gas temperature sensors. | Left bank and right bank DOC temperature sensors vary by more than 24°C or 43°F with each other using InteliMonitor? |
> |  | **STEP 2B.** Monitor the aftertreatment exhaust gas temperature sensors. | Left and right bank DOC inlet temperature sensors within 38°C \[100°F\] of each other? |
> |  | **STEP 2C.** Check the intake restriction. | Air cleaner elements dirty or restricted? |
> |  | **STEP 2D.** Check for intake and exhaust system leaks. | Leaks found in the air intake or exhaust systems? |
> |  | **STEP 2E.** Check the gas lines. | Any damage found to the gas lines? |
> |  | **STEP 2F.** Check the air piping. | Any damage found to the air lines? |
> |  | **STEP 2G.** Check the turbocharger operation. | Any measurements in the Inspect for Reuse section outside of the stated limits? |
> |  | **STEP 2H.** Check the DOC operation. | Any debris or damage found on the DOC? |
> | STEP 3. | Reset the fault. |  |
> |  | **STEP 3A.** Reset the fault. | Fault returns? |
>
> ### STEP 1. Validate the fault message.
>
> #### STEP 1A. Check for engine fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use INSITE™ electronic service tool to read the fault codes. | Any engine related fault codes? **YES** | Go to the appropriate fault code troubleshooting tree. |
> | Any engine related fault codes? **NO** | 1B |  |
>
> #### STEP 1B. Check for additional gas system alarms.
>
> | **Conditions:** Power ON dual fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect to the dual fuel control panel. Use InteliMonitor. Save a copy of the control module configuration file (archive file) on the local PC. Access the history shortcut. Check for occurrences of the message Sd EGTBankDelta. Check for other shutdown messages occurring at or near the time of the Sd EGTBankDelta. | Other shutdown messages for binary inputs occurred at the same time as Sd EGTBankDelta? **YESRepair:** If other shutdown messages for binary inputs occur at the same time, see the following procedure for ground and ground loop tests. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | 2A |
> | Other shutdown messages for binary inputs occurred at the same time as Sd EGTBankDelta? **NO** | 1C |  |
>
> #### STEP 1C. Check for 'Active' fault message.
>
> | **Conditions:** Power ON dual fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check local display panel for fault message. Navigate to fault display screen. | Control module in fault condition? **YES** | 2A |
> | Control module in fault condition? **NO** | 2B |  |
>
> ### STEP 2. Monitor the temperature sensors.
>
> #### STEP 2A. Monitor the aftertreatment exhaust gas temperature sensors.
>
> | **Conditions:** Power ON dual fuel control module. Key ON, engine not running. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect to the dual fuel panel. Use InteliMonitor. Save a copy of the configuration file (archive file) on the local PC. If any fault codes occur, see the appropriate fault code troubleshooting tree. If no fault codes occur, record the values of the three aftertreatment exhaust gas temperature sensors. | Left bank and right bank DOC temperature sensors vary by more than 24°C or 43°F with each other using InteliMonitor? **YESRepair:** Check for short circuit from the SIGNAL pin of the temperature sensor in question to all other pins in the harness. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] If no short is found, replace the temperature sensor reading higher or lower than the other sensors. Refer to Procedure 019-449 in Section 19. | 3A |
> | Left bank and right bank DOC temperature sensors vary by more than 24°C or 43°F with each other using InteliMonitor? **NO** | Contact a Cummins® Authorized Repair Location. |  |
>
> #### STEP 2B. Monitor the aftertreatment exhaust gas temperature sensors.
>
> | **Conditions:** Turn dual fuel control module ON. Reset the fault on the panel. Run engine at 1500 to 2000 rpm to meet operating conditions for dual fuel operation. Turn gas control switch on the panel to OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the local display panel for the fault message. Monitor the left and right bank DOC inlet temperature sensor in Diesel Only mode. | Left and right bank DOC inlet temperature sensors within 38°C \[100°F\] of each other? **YES** | 3A |
> | Left and right bank DOC inlet temperature sensors within 38°C \[100°F\] of each other? **NO** | 2C |  |
>
> #### STEP 2C. Check the intake restriction.
>
> | **Conditions:** Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the air cleaner elements. Use the GTA38, K38, K50, QSK38, and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 010-014 in Section 10. | Air cleaner elements dirty or restricted? **YESRepair:** Clean or replace the air filter element. See equipment manufacturer service information. | 3A |
> | Air cleaner elements dirty or restricted? **NO** | 2D |  |
>
> #### STEP 2D. Check for intake and exhaust system leaks.
>
> | **Conditions:** Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the air intake and exhaust system for leaks. Use the GTA38, K38, K50, QSK38, and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 010-024 in Section 10. | Leaks found in the air intake or exhaust systems? **YESRepair:** Repair the source of the leak. Use the GTA38, K38, K50, QSK38, and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 010-024 in Section 10. | 3A |
> | Leaks found in the air intake or exhaust systems? **NO** | 2E |  |
>
> #### STEP 2E. Check the gas lines.
>
> | **Conditions:** Turn OFF engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the gas lines for damage. Refer to Procedure 005-248 in Section 5. | Any damage found to the gas lines? **YESRepair:** Replace the damaged portion of gas line. Refer to Procedure 005-248 in Section 5. | 3A |
> | Any damage found to the gas lines? **NO** | 2F |  |
>
> #### STEP 2F. Check the air piping.
>
> | **Conditions:** Turn OFF engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the air piping for damage. Refer to Procedure 005-248 in Section 5. | Any damage found to the air lines? **YESRepair:** Replace the damaged portion of air lines. Refer to Procedure 005-248 in Section 5. | 3A |
> | Any damage found to the air lines? **NO** | 2G |  |
>
> #### STEP 2G. Check the turbocharger operation.
>
> | **Conditions:** Turn OFF engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure turbocharger clearances. Use the GTA38, K38, K50, QSK38, and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 010-033 in Section 10. | Any measurements in the Inspect for Reuse section outside of the stated limits? **YESRepair:** Repair or replace the turbocharger. Use the GTA38, K38, K50, QSK38, and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. [[28-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | 3A |
> | Any measurements in the Inspect for Reuse section outside of the stated limits? **NO** | 2H |  |
>
> #### STEP 2H. Check the DOC operation.
>
> | **Conditions:** Turn OFF engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the DOC for any damage or buildup. Refer to Procedure 011-049 in Section 11. | Any debris or damage found on the DOC? **YESRepair:** Clean or replace the DOC. Refer to Procedure 011-049 in Section 11. | 3A |
> | Any debris or damage found on the DOC? **NO** | 3A |  |
>
> ### STEP 3. Reset the fault.
>
> #### STEP 3A. Reset the fault.
>
> | **Conditions:** Engine not operating. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Rest the fault on the control panel or through InteliMonitor. Operate the engine under conditions to allow gas substitution. | Fault returns? **YESRepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |
> | Fault returns? **NO** | Repair complete. |  |
