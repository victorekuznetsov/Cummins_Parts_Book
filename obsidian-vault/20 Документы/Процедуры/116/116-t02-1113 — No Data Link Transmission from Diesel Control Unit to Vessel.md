---
aliases:
  - "Нет передачи данных от блока управления дизелем на судовую систему"
type: "Процедура"
doc: "116-t02-1113"
title_en: "No Data Link Transmission from Diesel Control Unit to Vessel"
title_ru: "Нет передачи данных от блока управления дизелем на судовую систему"
modified: "2008-04-15"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1113.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1113.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# No Data Link Transmission from Diesel Control Unit to Vessel
**Нет передачи данных от блока управления дизелем на судовую систему**

> [!abstract] Процедура · `116-t02-1113`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1113.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1113.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- DCU410 или удаленная панель **не** указывают на неисправности, потому что она **не** имеет мощность +24-VDC.

- Подсвечивается блок DCU410 и дистанционные светодиоды панели.

- У ECM есть активные дефекты

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Шина данных SAE J1939 CAN передает сигнал тревоги, генерируемый ECM, в окно интерфейса клиента. Коробка интерфейса клиента передает информацию тревоги на DCU410 и удаленную панель.

Это дерево обращается к источнику питания DCU410 и возврату.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс коробки проводов. |  |
|  | **STEP 1A.** Проверьте дисплей блока DCU410 на наличие неисправностей. | DCU410 указывает на неисправность (неисправности)? |
|  | **STEP 1A-1.** Проверьте провод питания DCU410 на напряжение +24-VDC. | Меньше +24-VDC? |
|  | **STEP 1B.** Проверить проводку пульта дистанционного управления. | Удаленный панельный блок указывает на неисправность (неисправности)? |
|  | **STEP 1B-1.** Проверьте провод питания удаленной панели на напряжение +24-VDC. | Меньше +24-VDC? |
| ШАГ 2. | Проверка проводки интерфейсной коробки заказчика. |  |
|  | **STEP 2A.** Проверьте открытые провода в сети контроллера DCU410 на разъеме DCU410 и X4 для открытого доступа. | Менее 10 Ом? |
|  | **STEP 2B.** Проверьте сеть контроллера DCU410 с открытым проводом питания и возврата на блоке DCU410 и разъеме X4 для короткого провода к проводу. | Менее 10 Ом? |
|  | **STEP 2C.** Проверить сеть контроллера DCU410 на открытом питающем проводе в блоке DCU410 и разъеме X4 для короткого заземления. | Менее 10 Ом? |
|  | **STEP 2D.** Проверьте наличие проводов передачи и возврата данных в шине SAE J1939 CAN на блоке DCU410, разъеме X4 и разъеме C3 для открытия. | Менее 10 Ом? |
|  | **STEP 2D-1.** Проверьте провода передачи и возврата данных SAE J1939 CAN на блоке DCU410, разъеме X4 и разъеме C3 для короткого провода к проводу. | Менее 10 Ом? |
|  | **STEP 2D-2.** Проверьте провод передачи данных шины SAE J1939 CAN на блоке DCU410, разъеме X4 и разъеме C3 для короткого заземления. | Менее 10 Ом? |
| ШАГ 3. | Проверьте OEM Wiring Harness |  |
|  | **STEP 3A.** Проверьте сигнал шины данных SAE J1939 CAN и провода возврата для открытого доступа. | Менее 10 Ом? |
|  | **STEP 3A-1.** Проверьте сигнал шины данных SAE J1939 CAN и верните провода для короткого провода к проводу. | Менее 10 Ом? |
|  | **STEP 3A-2.** Проверьте сигнальный провод шины данных SAE J1939 на короткое время до заземления. | Менее 10 Ом? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте дисплей блока DCU410 на наличие неисправностей.

| **Условия: **Найдите дисплей блока DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей блока DCU410 на наличие неисправностей. | Блок DCU410 указывает на неисправность (неисправности)? *Да | 1В |
| Блок DCU410 указывает на неисправность (неисправности)? **НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте провод питания DCU410 на напряжение +24-VDC.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Поместите один испытательный щуп на источник питания 1 напряжения (переключенной мощности) батареи, где находится блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? **Ремонт:** Проверить аккумуляторы. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте проводку удаленной панели.

| **Условия: **Найдите дисплей удаленной панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей удаленной панели для указания неисправностей. | Указывает ли удаленный панельный блок неисправности (неисправностей)? *Да | Ремонт завершён |
| Указывает ли удаленный панельный блок неисправности (неисправностей)? **НЕТ** | 1В-1-1 |  |

#### ШАГ 1B-1. Проверьте провод питания удаленной панели на напряжение +24-VDC.

| **Условия: **Откройте пульт дистанционного управления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? **Ремонт:** Проверить аккумуляторы. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте клиентский интерфейс коробки проводов.

#### ШАГ 2A. Проверьте сеть контроллера DCU410 на открытых проводах питания и возврата в блоке DCU410 и на разъеме X4 для открытого соединения.

| **Условия: **Откройте окно интерфейса клиента. Отключите сеть контроллеров DCU410, откройте провода питания и возврата в DCU410 и отсоедините разъем X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провода подачи и возврата для открытого. Поместите один испытательный щуп на провод открытой сети контроллера DCU410 в блоке DCU410. Поместите другой измерительный щуп на сеть DCU410 с открытым контактом питания на разъем X4. Поместите один измерительный щуп на контроллер DCU410, открытый обратный провод в блоке DCU410. Поместите другой измерительный щуп в сеть DCU410 с открытым обратным контактом на разъеме X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (ящик пользовательского интерфейса) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2B. Проверьте сеть контроллера DCU410 с открытым проводом питания и возврата на блоке DCU410 и разъеме X4 для короткого провода к проводу.

| **Условия: **Откройте окно интерфейса клиента. Отсоедините сеть контроллера DCU410 с открытым проводом питания на блоке DCU410 и отсоедините разъем X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провода подачи и возврата для короткого провода к проводу. Поместите один испытательный щуп на провод открытой сети контроллера DCU410 в блоке DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один измерительный щуп на контроллер DCU410, который будет иметь открытый обратный контакт в разъеме X4. Поместите другой испытательный щуп на все остальные штифты в разъем X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (ящик пользовательского интерфейса) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте сеть контроллера DCU410 с открытым проводом питания на блоке DCU410 и разъеме X4 для короткого заземления.

| **Условия: **Откройте окно интерфейса клиента. Отсоедините сеть контроллера DCU410 с открытым проводом питания на блоке DCU410 и отсоедините разъем X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проволоку питания на короткое время до земли. Поместите один испытательный щуп на провод открытой сети контроллера DCU410 в блоке DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (ящик пользовательского интерфейса) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте данные шины SAE J1939 CAN на блоке DCU410, разъеме X4 и разъеме C3 для открытого доступа.

| **Условия: **Откройте окно интерфейса клиента. Отключите шину передачи данных SAE J1939 CAN и провода возврата в блоке DCU410. Отключите разъемы X4 и C3. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте данные шины SAE J1939 CAN для подачи и возврата проводов для открытого доступа. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на контактную шину передачи данных SAE J1939 CAN на разъем X4. Поместите другой испытательный щуп на контактную шину передачи данных SAE J1939 CAN на разъем C3. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN в блок DCU410. Поместите другой измерительный щуп на шину данных SAE J1939 CAN обратного контакта на разъеме X4. Поместите другой измерительный щуп на шину данных SAE J1939 CAN обратного контакта на разъеме C3. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2D-1 |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (ящик пользовательского интерфейса) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2D-1. Проверьте данные шины передачи данных SAE J1939 CAN на блоке DCU410, разъеме X4 и разъеме C3 для короткого провода к проводу.

| **Условия: **Откройте окно интерфейса клиента. Отключите шину передачи данных SAE J1939 CAN и провода возврата в блоке DCU410. Отключите разъемы X4 и C3. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте данные шины передачи данных SAE J1939 CAN на блоке DCU410, разъеме X4 и разъеме C3 для короткого провода к проводу. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на все другие штифты в разъем X4. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на контактную шину передачи данных SAE J1939 CAN на разъем X4. Поместите другой испытательный щуп на все другие штифты в разъем X4. Поместите один измерительный щуп на шину данных SAE J1939 CAN обратного контакта на разъеме X4. Поместите другой испытательный щуп на все другие штифты в разъем X4. Поместите один испытательный щуп на контактную шину передачи данных SAE J1939 CAN на разъеме C3. Поместите другой испытательный щуп на все другие штифты на разъем C3. Поместите один измерительный щуп на шину данных SAE J1939 CAN обратного контакта на разъеме C3. Поместите другой испытательный щуп на все другие штифты на разъем C3. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2D-2 |  |

#### ШАГ 2D-2. Проверьте провод передачи данных шины SAE J1939 CAN на блоке DCU410, разъеме X4 и разъеме C3 для короткого заземления.

| **Условия: **Откройте окно интерфейса клиента. Отключите провод передачи данных шины SAE J1939 в блоке DCU410. Отключите разъемы X4 и C3. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод передачи данных шины SAE J1939 CAN на блоке DCU410, разъеме X4 и разъеме C3 для короткого заземления. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один измерительный щуп на контактную шину передачи данных SAE J1939 CAN на блок X4. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на контактную шину передачи данных SAE J1939 CAN на разъеме C3. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте жгут проводов изготовителя машины.

#### ШАГ 3A. Проверьте сигнал шины данных SAE J1939 CAN и верните провода для открытия.

| **Условия: **Откройте окно интерфейса клиента. Отключите шину данных SAE J1939 CAN и разъемы X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал шины данных SAE J1939 CAN и верните провода для открытия. Поместите один испытательный щуп на контакт сигнала шины данных SAE J1939 CAN на разъем X4. Поместите другой измерительный щуп на контактный сигнал шины данных SAE J1939 CAN в разъем порта службы данных шины SAE J1939 CAN. Поместите один измерительный щуп на шину данных SAE J1939 CAN обратного контакта на разъеме X4. Поместите другой измерительный щуп на обратный контакт шины данных SAE J1939 CAN в разъем порта обслуживания шины данных SAE J1939 CAN. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 3А-1-1 |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (ящик пользовательского интерфейса) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 3A-1. Проверьте сигнал шины данных SAE J1939 CAN и верните провода для короткого провода к проводу.

| **Условия: **Откройте окно интерфейса клиента. Отключите шину данных SAE J1939 CAN и разъемы X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал шины данных SAE J1939 CAN и верните провода для короткого провода к проводу. Поместите один испытательный щуп на контакт сигнала шины данных SAE J1939 CAN на разъем X4. Поместите другой испытательный щуп на все другие штифты в разъем X4. Поместите один измерительный щуп на шину данных SAE J1939 CAN обратного контакта на разъеме X4. Поместите другой испытательный щуп на все другие штифты в разъем X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 3А-2 |
| Менее 10 Ом? **NORepair:** Заменить разъем порта обслуживания шины данных SAE J1939. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 3A-2. Проверить сигнал шины данных SAE J1939 CAN на короткое время до земли.

| **Условия: **Откройте окно интерфейса клиента. Отключите шину данных SAE J1939 CAN и разъемы X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить сигнал шины данных SAE J1939 CAN на короткое время до земли. Поместите один испытательный щуп на контакт сигнала шины данных SAE J1939 CAN на разъем X4. Поместите другой испытательный щуп на землю двигателя. Поместите один измерительный щуп на шину данных SAE J1939 CAN обратного контакта на разъеме X4. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | Обратитесь в авторизованный сервисный центр Cummins®. |
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
> - The ECM has active faults
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
> | STEP 1. | Check the customer interface box wiring. |  |
> |  | **STEP 1A.** Check the DCU410 unit display for indication of faults. | DCU410 unit indicate fault(s)? |
> |  | **STEP 1A-1.** Check the DCU410 power supply wire for voltage +24-VDC. | Less than +24-VDC? |
> |  | **STEP 1B.** Check remote panel wiring. | Remote panel unit indicate fault(s)? |
> |  | **STEP 1B-1.** Check the remote panel power supply wire for voltage +24-VDC. | Less than +24-VDC? |
> | STEP 2. | Check customer interface box wiring. |  |
> |  | **STEP 2A.** Check the DCU410 controller area network open supply and return wires at the DCU410 and X4 connector for an open. | Less than 10 ohms? |
> |  | **STEP 2B.** Check the DCU410 controller area network open supply and return wire at the DCU410 unit and X4 connector for a wire-to-wire short. | Less than 10 ohms? |
> |  | **STEP 2C.** Check the DCU410 controller area network open supply wire at the DCU410 unit and X4 connector for a short to ground. | Less than 10 ohms? |
> |  | **STEP 2D.** Check the SAE J1939 data link supply and return wires at the DCU410 unit, X4 connector, and C3 connector for an open. | Less than 10 ohms? |
> |  | **STEP 2D-1.** Check the SAE J1939 data link supply and return wires at the DCU410 unit, X4 connector, and C3 connector for a wire-to-wire short. | Less than 10 ohms? |
> |  | **STEP 2D-2.** Check the SAE J1939 data link supply wire at the DCU410 unit, X4 connector, and C3 connector for a short to ground. | Less than 10 ohms? |
> | STEP 3. | Check the OEM Wiring Harness |  |
> |  | **STEP 3A.** Check the SAE J1939 data link signal and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 3A-1.** Check the SAE J1939 data link signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
> |  | **STEP 3A-2.** Check the SAE J1939 data link signal wire for a short to ground. | Less than 10 ohms? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check the DCU410 unit display for faults.
>
> | **Conditions:** Locate the DCU410 unit display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 unit display for faults. | The DCU410 unit indicates fault(s)? **YES** | 1B |
> | The DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |
>
> #### STEP 1A-1. Check the DCU410 power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test lead on the battery 1 voltage (switched power) supply where at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 1B |  |
>
> #### STEP 1B. Check the remote panel wiring.
>
> | **Conditions:** Locate the remote panel display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel display for an indication of faults. | Does the remote panel unit indicate fault(s)? **YES** | Repair complete |
> | Does the remote panel unit indicate fault(s)? **NO** | 1B-1 |  |
>
> #### STEP 1B-1. Check the remote panel power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 2A |  |
>
> ### STEP 2. Check the customer interface box wiring.
>
> #### STEP 2A. Check the DCU410 controller area network open supply and return wires at the DCU410 unit and at the X4 connector for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the DCU410 controller area network open supply and return wires at the DCU410 and disconnect the X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply and return wires for an open. Place one test lead on the DCU410 controller area network open supply wire at the DCU410 unit. Place the other test lead on the DCU410 network open supply pin at the X4 connector. Place one test lead on the DCU410 controller area network open return wire at the DCU410 unit. Place the other test lead on the DCU410 network open return pin at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2B. Check the DCU410 controller area network open supply and return wire at the DCU410 unit and X4 connector for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the DCU410 controller area network open supply wire at the DCU410 unit and disconnect the X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply and return wires for a wire-to-wire short. Place one test lead on the DCU410 controller area network open supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the DCU410 controller area network open return pin in the X4 connector. Place the other test lead on all other pin in the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the DCU410 controller area network open supply wire at the DCU410 unit and X4 connector for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the DCU410 controller area network open supply wire at the DCU410 unit and disconnect the X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply wire for a short to ground. Place one test lead on the DCU410 controller area network open supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2D |  |
>
> #### STEP 2D. Check the SAE J1939 data link supply and return wires at the DCU410 unit, X4 connector, and C3 connector for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link supply and return wires at the DCU410 unit. Disconnect the X4 and C3 connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply and return wires for an open. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link supply pin at the X4 connector. Place the other test lead on the SAE J1939 data link supply pin at the C3 connector. Place one test lead on the SAE J1939 data link return wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link return pin at the X4 connector. Place the other test lead on the SAE J1939 data link return pin at the C3 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2D-1 |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2D-1. Check the SAE J1939 data link supply and return wires at the DCU410 unit, X4 connector, and C3 connector for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link supply and return wires at the DCU410 unit. Disconnect the X4 and C3 connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply and return wires at the DCU410 unit, X4 connector, and C3 connector for a wire-to-wire short. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on all other pins at the X4 connector. Place one test lead on the SAE J1939 data link return wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the SAE J1939 data link supply pin at the X4 connector. Place the other test lead on all other pins at the X4 connector. Place one test lead on the SAE J1939 data link return pin at the X4 connector. Place the other test lead on all other pins at the X4 connector. Place one test lead on the SAE J1939 data link supply pin at the C3 connector. Place the other test lead on all other pins at the C3 connector. Place one test lead on the SAE J1939 data link return pin at the C3 connector. Place the other test lead on all other pins at the C3 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2D-2 |  |
>
> #### STEP 2D-2. Check the SAE J1939 data link supply wire at the DCU410 unit, X4 connector, and C3 connector for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link supply wire at the DCU410 unit. Disconnect the X4 and C3 connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply wire at the DCU410 unit, X4 connector, and C3 connector for a short to ground. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the SAE J1939 data link supply pin at the X4 unit. Place the other test lead on panel ground. Place one test lead on the SAE J1939 data link supply pin at the C3 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 3A |  |
>
> ### STEP 3. Check the OEM wiring harness.
>
> #### STEP 3A. Check the SAE J1939 data link signal and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link and X4 connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link signal and return wires for an open. Place one test lead on the SAE J1939 data link signal pin at the X4 connector. Place the other test lead on the SAE J1939 data link signal pin at the SAE J1939 data link service port connector. Place one test lead on the SAE J1939 data link return pin at the X4 connector. Place the other test lead on the SAE J1939 data link return pin at the SAE J1939 data link service port connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3A-1 |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] | Repair complete |  |
>
> #### STEP 3A-1. Check the SAE J1939 data link signal and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link and X4 connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link signal and return wires for a wire-to-wire short. Place one test lead on the SAE J1939 data link signal pin at the X4 connector. Place the other test lead on all other pins at the X4 connector. Place one test lead on the SAE J1939 data link return pin at the X4 connector. Place the other test lead on all other pins at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3A-2 |
> | Less than 10 ohms? **NORepair:** Replace the SAE J1939 data link service port connector. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 3A-2. Check the SAE J1939 data link signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link and X4 connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link signal wire for a short to ground. Place one test lead on the SAE J1939 data link signal pin at the X4 connector. Place the other test lead on engine ground. Place one test lead on the SAE J1939 data link return pin at the X4 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Contact a Cummins® Authorized Repair Location. |
> | Less than 10 ohms? **NORepair:** Replace the SAE J1939 data link service port connector. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
