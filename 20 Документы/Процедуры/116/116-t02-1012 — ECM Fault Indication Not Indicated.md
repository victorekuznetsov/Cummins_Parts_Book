---
aliases:
  - "Индикация неисправности ЭБУ не отображается"
type: "Процедура"
doc: "116-t02-1012"
title_en: "ECM Fault Indication Not Indicated"
title_ru: "Индикация неисправности ЭБУ не отображается"
modified: "2008-05-29"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1012.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1012.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# ECM Fault Indication Not Indicated
**Индикация неисправности ЭБУ не отображается**

> [!abstract] Процедура · `116-t02-1012`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1012.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1012.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- DCU410 или удаленная панель ** не** указывают на неисправности, потому что она ** не** имеет мощность +24-VDC.

- Подсвечивается блок DCU410 и дистанционные светодиоды панели.

- У ECM есть активные дефекты.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Шина данных SAE J1939 CAN передает сигнал тревоги, генерируемый ECM, в окно интерфейса клиента. Коробка интерфейса клиента передает информацию тревоги на DCU410 и удаленную панель.

Это дерево обращается к источнику питания DCU410 и возврату.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента. |  |
|  | **STEP 1A.** Проверьте дисплей блока DCU410 на наличие неисправностей. |  |
|  | **STEP 1A-1.** Проверьте провод питания DCU410 на напряжение +24-VDC. |  |
|  | **STEP 1B.** Проверьте проводку удаленной панели. |  |
|  | **STEP 1B-1.** Проверьте провод питания удаленной панели на напряжение +24-VDC. |  |
| ШАГ 2. | Проверьте клиентский интерфейс коробки проводов. |  |
|  | **ШАГ 2А.** Проверить провод DCU410 для открытого сигнала тревоги. |  |
|  | **STEP 2A-1.** Проверьте провод DCU410 (обычно закрытый) на наличие открытого сигнала тревоги. |  |
|  | **STEP 2B.** Проверьте общий сигнал тревоги DCU410 (общий) для короткого провода к проводу. |  |
|  | **STEP 2B-1.** Проверьте общий сигнал тревоги DCU410 для короткого провода. |  |
|  | **STEP 2B-2.** Проверьте общий сигнал тревоги DCU410 для короткого провода. |  |
|  | **STEP 2C.** Проверить провод DCU410 для короткого заземления. |  |
|  | **STEP 2C-1.** Проверьте обычный сигнал тревоги DCU410 (обычно закрытый) на короткое время до земли. |  |
|  | **STEP 2C-2.** Проверьте обычный сигнал тревоги DCU410 (обычно закрытый) на короткое время до земли. |  |
|  | **STEP 2D.** Проверьте наличие шины данных SAE J1939 CAN и проводов возврата данных для открытия. |  |
|  | **STEP 2D-1.** Проверьте, может ли шина передачи данных SAE J1939 подавать и возвращать провода для короткого провода к проводу. |  |
|  | **STEP 2D-2.** Проверьте провод передачи данных шины SAE J1939 на короткое время до земли. |  |
| ШАГ 3. | Проверьте жгут проводов изготовителя машины. |  |
|  | **STEP 3A.** Проверьте наличие шины данных SAE J1939 CAN и проводов возврата данных для открытия. |  |
|  | **STEP 3A-1.** Проверьте, может ли шина передачи данных SAE J1939 подавать и возвращать провода для короткого провода к проводу. |  |
|  | **STEP 3A-2.** Проверьте провод передачи данных шины SAE J1939 на короткое время до земли. |  |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте дисплей блока DCU410 на наличие неисправностей.

| **Условия: ** Найдите дисплей блока DCU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте дисплей блока DCU410 для указания неисправностей. | Блок DCU410 указывает на неисправность (неисправности)? *Да** | 1В |
| Блок DCU410 указывает на неисправность (неисправности)? ** НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте провод питания DCU410 на напряжение +24-VDC.

| **Условия: ** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте напряжение батареи 1 (переключенная мощность) в блоке DCU410. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? *** Ремонт:** Проверить аккумуляторы. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Меньше +24-VDC? ** НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте проводку удаленной панели.

| **Условия: ** Найдите дисплей удаленной панели. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте дисплей удаленной панели для указания неисправностей. | Удаленный панельный блок указывает на неисправность (неисправности)? *Да** | Ремонт завершён |
| Удаленный панельный блок указывает на неисправность (неисправности)? ** НЕТ** | 1В-1-1 |  |

#### ШАГ 1B-1. Проверьте провод питания удаленной панели на напряжение +24-VDC.

| **Условия: ** Откройте пульт дистанционного управления. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте напряжение батареи 1 (переключенная мощность) в блоке DCU410. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блок удаленной панели. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? *** Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию OEM. | Ремонт завершён |
| Меньше +24-VDC? ** НЕТ** | 2А |  |

### ШАГ 2. Проверьте клиентский интерфейс коробки проводов.

#### ШАГ 2A. Проверьте провод DCU410 для открытого сигнала тревоги (общего).

| **Условия: ** Откройте окно интерфейса клиента. Отключите провод DCU410 общего сигнала тревоги (общего) в соединении DCU410 и X4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте общий сигнал тревоги DCU410 (общий) провод в блоке DCU410 и подключение X4 для открытого доступа. Поместите один испытательный щуп на провод общей сигнализации DCU410 (общий) в блок DCU410. Поместите другой испытательный щуп на общую сигнализацию DCU410 (общую) на соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 2А-1-1 |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. Процедура 015-023 (ящик пользовательского интерфейса) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2A-1. Проверьте общий сигнал тревоги DCU410 (обычно закрытый) на наличие открытого провода.

| **Условия: ** Откройте окно интерфейса клиента. Отключите провод DCU410 общего сигнала тревоги (обычно закрытого) в соединении DCU410 и X4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте общий сигнал тревоги DCU410 (обычно закрытый) провод в соединении DCU410 и X4 для открытого соединения. Поместите один испытательный щуп на провод общей сигнализации DCU410 (обычно закрытой) в блоке DCU410. Поместите другой испытательный щуп на общую сигнализацию DCU410 (обычно закрытую) на разъем X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. Процедура 015-023 (ящик пользовательского интерфейса) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2B. Проверьте общий сигнал тревоги DCU410 (общий) провод для короткого провода к проводу.

| **Условия: ** Откройте окно интерфейса клиента. Отключите провод DCU410 общего сигнала тревоги (общего) в блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте общий сигнал тревоги DCU410 (общий) провод на блоке DCU410 и разъеме X4 для короткого провода к проводу. Поместите один испытательный щуп на провод общей сигнализации DCU410 (общий) в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на провод DCU410 общего сигнала тревоги (общего) в соединение X4. Поместите другой испытательный щуп на все другие провода в соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. Процедура 015-023 (ящик пользовательского интерфейса) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2В-1-1 |  |

#### ШАГ 2B-1. Проверьте общий сигнал тревоги DCU410 (обычно закрытый) для короткого провода.

| **Условия: ** Откройте окно интерфейса клиента. Отключите провод DCU410 общего сигнала тревоги (обычно закрытого) на блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте общий сигнал тревоги DCU410 (обычно закрытый) провод на блоке DCU410 и разъеме X4 для короткого провода к проводу. Поместите один испытательный щуп на провод общей сигнализации DCU410 (обычно закрытой) в блоке DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на провод DCU410 общего сигнала тревоги (обычно закрытого) в соединении X4. Поместите другой испытательный щуп на все другие провода в соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. Процедура 015-023 (ящик пользовательского интерфейса) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2В-2-2 |  |

#### ШАГ 2B-2. Проверьте общий сигнал тревоги DCU410 (обычно открытый) для короткого провода.

| **Условия: ** Откройте окно интерфейса клиента. Отключите провод DCU410 общего сигнала тревоги (обычно открытый) на блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте общий сигнал тревоги DCU410 (обычно открытый) провод на блоке DCU410 и разъеме X4 для короткого провода к проводу. Поместите один испытательный щуп на провод общей сигнализации DCU410 (обычно открытый) в блоке DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на провод DCU410 общего сигнала тревоги (обычно открытый) в соединении X4. Поместите другой измерительный щуп на все остальные провода, которые являются соединением X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. Процедура 015-023 (ящик пользовательского интерфейса) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте провод DCU410 для короткого заземления.

| **Условия: ** Откройте окно интерфейса клиента. Отключите провод DCU410 общего сигнала тревоги (общего) в блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте общий сигнал тревоги DCU410 (общий) провод в блоке DCU410 и подключение X4 для короткого заземления. Поместите один испытательный щуп на провод общей сигнализации DCU410 (общий) в блок DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на провод DCU410 общего сигнала тревоги (общего) в соединение X4. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. Процедура 015-023 (ящик пользовательского интерфейса) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2С-1 |  |

#### ШАГ 2C-1. Проверьте обычный сигнал тревоги DCU410 (обычно закрытый) на короткое время до земли.

| **Условия: ** Откройте окно интерфейса клиента. Отключите провод DCU410 общего сигнала тревоги (обычно закрытого) на блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте общий сигнал тревоги DCU410 (обычно закрытый) провод на блоке DCU410 и разъеме X4 для короткого заземления. Поместите один испытательный щуп на провод общей сигнализации DCU410 (обычно закрытой) в блоке DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на провод DCU410 общего сигнала тревоги (обычно закрытого) в соединении X4. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. Процедура 015-023 (ящик пользовательского интерфейса) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2С-2 |  |

#### ШАГ 2C-2. Проверьте обычный сигнал тревоги DCU410 (обычно закрытый) на короткое время до земли.

| **Условия: ** Откройте окно интерфейса клиента. Отключите провод DCU410 общего сигнала тревоги (обычно открытый) на блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте провод DCU410 с обычной сигнализацией (обычно открытый) на блоке DCU410 и разъеме X4 для короткого заземления. Поместите один испытательный щуп на провод общей сигнализации DCU410 (обычно открытый) в блоке DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на провод DCU410 общего сигнала тревоги (обычно открытый) в соединении X4. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. Процедура 015-023 (ящик пользовательского интерфейса) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте провода питания и возврата SAE J1939 на наличие открытого.

| **Условия: ** Откройте окно интерфейса клиента. Отключите шину передачи данных SAE J1939 CAN и провода возврата данных в блоке DCU410 и соединении X4. Отключите разъем C3. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте провода передачи и возврата данных SAE J1939 CAN на блоке DCU410, соединении X4 и разъеме C3 для открытого доступа. Поместите один испытательный щуп на провод передачи данных шины SAE J1939 CAN (C3) в блок DCU410. Поместите другой измерительный щуп на подачу шины данных SAE J1939 CAN (C3) в соединение X4. Поместите один испытательный щуп на провод передачи данных шины SAE J1939 CAN (C3) в блок DCU410. Поместите другой испытательный щуп на подачу шины данных SAE J1939 CAN (C3) на разъем C3. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN (C3) в блок DCU410. Поместите другой измерительный щуп на возврат шины данных SAE J1939 CAN (C3) в соединение X4. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN (C3) в блок DCU410. Поместите другой измерительный щуп на возврат шины данных SAE J1939 CAN (C3) на разъем C3. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 2D-1 |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. Процедура 015-023 (ящик пользовательского интерфейса) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2D-1. Проверьте данные шины SAE J1939 CAN для подачи и возврата проводов для короткого провода к проводу.

| **Условия: ** Откройте окно интерфейса клиента. Отключите шину передачи данных SAE J1939 CAN и провода возврата данных в блоке DCU410 и соединении X4. Отключите разъем C3. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте данные шины передачи данных SAE J1939 CAN на блоке DCU410, соединении X4 и разъеме C3 для короткого провода к проводу. Поместите один испытательный щуп на провод передачи данных шины SAE J1939 CAN (C3) в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN (C3) в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на провод шины передачи данных SAE J1939 CAN (C3) на разъеме X4. Поместите другой испытательный щуп на все другие провода в разъем X4. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN (C3) на разъеме X4. Поместите другой испытательный щуп на все другие провода в разъем X4. Поместите один испытательный щуп на провод шин передачи данных SAE J1939 CAN (C3) на разъеме C3. Поместите другой испытательный щуп на все другие провода на разъеме C3. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN (C3) на разъеме C3. Поместите другой испытательный щуп на все другие провода на разъеме C3. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2D-2 |  |

#### ШАГ 2D-2. Проверьте провод передачи данных SAE J1939 CAN для короткого заземления.

| **Условия: ** Откройте окно интерфейса клиента. Отключите шину передачи данных SAE J1939 CAN и провода возврата данных в блоке DCU410 и соединении X4. Отключите разъем C3. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте провод передачи данных шины SAE J1939 CAN на блоке DCU410, соединении X4 и разъеме C3 для короткого заземления. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в соединение X4. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на провод передачи данных шины SAE J1939 CAN на разъеме C3. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 3А |  |

### ШАГ 3. Проверьте жгут проводов изготовителя машины.

#### ШАГ 3A. Проверьте данные шины SAE J1939 CAN для подачи и возврата проводов для открытого доступа.

| **Условия: ** Откройте окно интерфейса клиента. Отключите шину передачи данных SAE J1939 CAN и верните провода в соединение X4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте данные шины SAE J1939 CAN для подачи и возврата проводов для открытого доступа. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в соединение X4. Поместите другой измерительный щуп на провод передачи данных шины данных SAE J1939 CAN на разъем порта обслуживания шины данных SAE J1939 CAN. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN в соединение X4. Поместите другой измерительный щуп на провод возврата шины данных SAE J1939 CAN в разъем порта обслуживания шины данных SAE J1939 CAN. | Менее 10 Ом? *Да** | 3А-1-1 |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 3A-1. Проверьте данные шины SAE J1939 CAN для подачи и возврата проводов для короткого провода к проводу.

| **Условия: ** Откройте окно интерфейса клиента. Отключите шину передачи данных SAE J1939 CAN и верните провода в соединение X4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте данные шины SAE J1939 CAN на подаче и возврате проводов в соединении X4 для короткого провода к проводу. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в соединение X4. Поместите другой испытательный щуп на все другие провода в соединение X4. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN в соединение X4. Поместите другой испытательный щуп на все другие провода в соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 3А-2 |
| Менее 10 Ом? **NORepair:** Заменить разъем порта обслуживания шины данных SAE J1939. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 3A-2. Проверьте провод передачи данных SAE J1939 CAN для короткого заземления.

| **Условия: ** Откройте окно интерфейса клиента. Отсоедините провод передачи данных шины SAE J1939 CAN на соединении X4 и разъем порта обслуживания шины данных SAE J1939 CAN. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте провод передачи данных SAE J1939 CAN для короткого заземления. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в соединение X4. Поместите другой испытательный щуп на землю двигателя. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN в разъем порта обслуживания шины данных SAE J1939 CAN. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | Обратитесь в авторизованный сервисный центр Cummins®. |
| Менее 10 Ом? **NORepair:** Заменить разъем порта обслуживания шины данных SAE J1939. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The DCU410 or remote panel does **not** indicate faults because it does **not** have power +24-VDC.
>
> - The DCU410 unit and remote panel LEDs illuminated.
>
> - The ECM has active faults.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The SAE J1939 data link delivers alarm information, generated by the ECM, to the customer interface box. The customer interface box transfers alarm information to the DCU410 and remote panel.
>
> This tree addresses the DCU410 power supply and return.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box. |  |
> |  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
> |  | **STEP 1A-1.** Check the DCU410 power supply wire for voltage +24-VDC. |  |
> |  | **STEP 1B.** Check the remote panel wiring. |  |
> |  | **STEP 1B-1.** Check the remote panel power supply wire for voltage +24-VDC. |  |
> | STEP 2. | Check the customer interface box wiring. |  |
> |  | **STEP 2A.** Check the DCU410 common alarm (common) wire for an open. |  |
> |  | **STEP 2A-1.** Check the DCU410 common alarm (normally closed) wire for an open. |  |
> |  | **STEP 2B.** Check the DCU410 common alarm (common) wire for a wire-to-wire short. |  |
> |  | **STEP 2B-1.** Check the DCU410 common alarm (common) wire for a wire-to-wire short. |  |
> |  | **STEP 2B-2.** Check the DCU410 common alarm (common) wire for a wire-to-wire short. |  |
> |  | **STEP 2C.** Check the DCU410 common alarm (common) wire for a short to ground. |  |
> |  | **STEP 2C-1.** Check the DCU410 common alarm (normally closed) wire for a short to ground. |  |
> |  | **STEP 2C-2.** Check the DCU410 common alarm (normally closed) wire for a short to ground. |  |
> |  | **STEP 2D.** Check the SAE J1939 data link supply and return wires for an open. |  |
> |  | **STEP 2D-1.** Check the SAE J1939 data link supply and return wires for a wire-to-wire short. |  |
> |  | **STEP 2D-2.** Check the SAE J1939 data link supply wire for short to ground. |  |
> | STEP 3. | Check the OEM wiring harness. |  |
> |  | **STEP 3A.** Check the SAE J1939 data link supply and return wires for an open. |  |
> |  | **STEP 3A-1.** Check the SAE J1939 data link supply and return wires for a wire-to-wire short. |  |
> |  | **STEP 3A-2.** Check the SAE J1939 data link supply wire for a short to ground. |  |
>
> ### STEP 1. Check the customer interface box.
>
> #### STEP 1A. Check the DCU410 unit display for faults.
>
> | **Conditions:** Locate the DCU410 unit display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 unit display for indication of faults. | The DCU410 unit indicates fault(s)? **YES** | 1B |
> | The DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |
>
> #### STEP 1A-1. Check the DCU410 power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery 1 voltage (switched power) at the DCU410 unit. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 1B |  |
>
> #### STEP 1B. Check the remote panel wiring.
>
> | **Conditions:** Locate the remote panel display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel display for an indication of faults. | The remote panel unit indicates fault(s)? **YES** | Repair complete |
> | The remote panel unit indicates fault(s)? **NO** | 1B-1 |  |
>
> #### STEP 1B-1. Check the remote panel power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery 1 voltage (switched power) at the DCU410 unit. Place one test lead on the battery 1 voltage (switched power) supply wire at the remote panel unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 2A |  |
>
> ### STEP 2. Check the customer interface box wiring.
>
> #### STEP 2A. Check the DCU410 common alarm (common) wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the DCU410 common alarm (common) wire at the DCU410 and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 common alarm (common) wire at the DCU410 unit and X4 connection for an open. Place one test lead on the DCU410 common alarm (common) wire at the DCU410 unit. Place the other test lead on the DCU410 common alarm (common) at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2A-1 |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to the Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2A-1. Check the DCU410 common alarm (normally closed) wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the DCU410 common alarm (normally closed) wire at the DCU410 and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 common alarm (normally closed) wire at the DCU410 and X4 connection for an open. Place one test lead on the DCU410 common alarm (normally closed) wire at the DCU410 unit. Place the other test lead on the DCU410 common alarm (normally closed) at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to the Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2B. Check the DCU410 common alarm (common) wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the DCU410 common alarm (common) wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 common alarm (common) wire at the DCU410 unit and X4 connector for a wire-to-wire short. Place one test lead on the DCU410 common alarm (common) wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the DCU410 common alarm (common) wire at the X4 connection. Place the other test lead on all other wires at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to the Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2B-1 |  |
>
> #### STEP 2B-1. Check the DCU410 common alarm (normally closed) wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the DCU410 common alarm (normally closed) wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 common alarm (normally closed) wire at the DCU410 unit and X4 connector for a wire-to-wire short. Place one test lead on the DCU410 common alarm (normally closed) wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the DCU410 common alarm (normally closed) wire at the X4 connection. Place the other test lead on all other wires at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to the Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2B-2 |  |
>
> #### STEP 2B-2. Check the DCU410 common alarm (normally open) wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the DCU410 common alarm (normally open) wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 common alarm (normally open) wire at the DCU410 unit and X4 connector for a wire-to-wire short. Place one test lead on the DCU410 common alarm (normally open) wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the DCU410 common alarm (normally open) wire at the X4 connection. Place the other test lead on all other wires are the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to the Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the DCU410 common alarm (common) wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the DCU410 common alarm (common) wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 common alarm (common) wire at the DCU410 unit and X4 connection for a short to ground. Place one test lead on the DCU410 common alarm (common) wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the DCU410 common alarm (common) wire at the X4 connection. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to the Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2C-1 |  |
>
> #### STEP 2C-1. Check the DCU410 common alarm (normally closed) wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the DCU410 common alarm (normally closed) wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 common alarm (normally closed) wire at the DCU410 unit and X4 connector for a short to ground. Place one test lead on the DCU410 common alarm (normally closed) wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the DCU410 common alarm (normally closed) wire at the X4 connection. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to the Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2C-2 |  |
>
> #### STEP 2C-2. Check the DCU410 common alarm (normally closed) wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the DCU410 common alarm (normally open) wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 common alarm (normally open) wire at the DCU410 unit and X4 connector for a short to ground. Place one test lead on the DCU410 common alarm (normally open) wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the DCU410 common alarm (normally open) wire at the X4 connection. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to the Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2D |  |
>
> #### STEP 2D. Check the SAE J1939 supply and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link supply and return wires at the DCU410 unit and X4 connection. Disconnect the C3 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply and return wires at the DCU410 unit, X4 connection, and C3 connector for an open. Place one test lead on the SAE J1939 data link supply (C3) wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link supply (C3) at the X4 connection. Place one test lead on the SAE J1939 data link supply (C3) wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link supply (C3) at the C3 connector. Place one test lead on the SAE J1939 data link return (C3) wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link return (C3) at the X4 connection. Place one test lead on the SAE J1939 data link return (C3) wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link return (C3) at the C3 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2D-1 |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to the Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2D-1. Check the SAE J1939 data link supply and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link supply and return wires at the DCU410 unit and X4 connection. Disconnect the C3 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply and return wires at the DCU410 unit, X4 connection, and C3 connector for a wire-to-wire short. Place one test lead on the SAE J1939 data link supply (C3) wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the SAE J1939 data link return (C3) wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the SAE J1939 data link supply (C3) wire at the X4 connector. Place the other test lead on all other wires at the X4 connector. Place one test lead on the SAE J1939 data link return (C3) wire at the X4 connector. Place the other test lead on all other wires at the X4 connector. Place one test lead on the SAE J1939 data link supply (C3) wire at the C3 connector. Place the other test lead on all other wires at the C3 connector. Place one test lead on the SAE J1939 data link return (C3) wire at the C3 connector. Place the other test lead on all other wires at the C3 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2D-2 |  |
>
> #### STEP 2D-2. Check the SAE J1939 data link supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link supply and return wires at the DCU410 unit and X4 connection. Disconnect the C3 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply wire at the DCU410 unit, X4 connection, and C3 connector for a short to ground. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the SAE J1939 data link supply wire at the X4 connection. Place the other test lead on panel ground. Place one test lead on the SAE J1939 data link supply wire at the C3 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 3A |  |
>
> ### STEP 3. Check the OEM wiring harness.
>
> #### STEP 3A. Check the SAE J1939 data link supply and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link supply and return wires at the X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply and return wires for an open. Place one test lead on the SAE J1939 data link supply wire at the X4 connection. Place the other test lead on the SAE J1939 data link supply wire at the SAE J1939 data link service port connector. Place one test lead on the SAE J1939 data link return wire at the X4 connection. Place the other test lead on the SAE J1939 data link return wire at the SAE J1939 data link service port connector. | Less than 10 ohms? **YES** | 3A-1 |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 3A-1. Check the SAE J1939 data link supply and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link supply and return wires at the X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply and return wires at the X4 connection for a wire-to-wire short. Place one test lead on the SAE J1939 data link supply wire at the X4 connection. Place the other test lead on all other wires at the X4 connection. Place one test lead on the SAE J1939 data link return wire at the X4 connection. Place the other test lead on all other wires at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3A-2 |
> | Less than 10 ohms? **NORepair:** Replace the SAE J1939 data link service port connector. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 3A-2. Check the SAE J1939 data link supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link supply wire at the X4 connection and SAE J1939 data link service port connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply wire for a short to ground. Place one test lead on the SAE J1939 data link supply wire at the X4 connection. Place the other test lead on engine ground. Place one test lead on the SAE J1939 data link return wire at the SAE J1939 data link service port connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Contact a Cummins® Authorized Repair Location. |
> | Less than 10 ohms? **NORepair:** Replace the SAE J1939 data link service port connector. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
