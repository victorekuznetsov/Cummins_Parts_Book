---
aliases:
  - "Ложный сигнал останова по разносу на блоке останова"
type: "Процедура"
doc: "116-t02-1102"
title_en: "False Overspeed Shut Down Signal at Shutdown Unit"
title_ru: "Ложный сигнал останова по разносу на блоке останова"
modified: "2008-04-04"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1102.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1102.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# False Overspeed Shut Down Signal at Shutdown Unit
**Ложный сигнал останова по разносу на блоке останова**

> [!abstract] Процедура · `116-t02-1102`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1102.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1102.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- SDU410 отключает двигатель из-за превышения скорости, хотя двигатель работал на нормальной скорости.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 1A.** Проверьте устройство SDU410 на наличие сигнализации и светодиодной подсветки. | Светодиод быстро мигает? |
|  | **STEP 1A-1.** Проверьте сигнал 2 оборота двигателя и провода возврата для открытого. | Менее 10 Ом? |
|  | **STEP 1B.** Проверьте конфигурацию блока SDU410. | Правильно ли пороговое значение? |
|  | **STEP 1C.** Проверьте сигнал 1 оборота двигателя и провода возврата для открытого сигнала. | Менее 10 Ом? |
|  | **STEP 1C-1.** Проверьте сигнал 2 оборота двигателя и провода возврата для открытого. | Менее 10 Ом? |
|  | **STEP 1D.** Проверьте сигнал 1 оборота двигателя и провода возврата для короткого провода на блоке SDU410 и разъеме C4. | Менее 10 Ом? |
|  | **STEP 1D-1.** Проверьте скорость двигателя 2 сигнала и провода возврата для короткого провода на блоке SDU410 и разъеме C4. | Менее 10 Ом? |
|  | **STEP 1E.** Проверьте скорость двигателя 1 сигнального провода на короткое время до заземления на блоке SDU410 и разъеме C4. | Менее 10 Ом? |
|  | **STEP 1E-1.** Проверьте скорость 2 двигателя на короткое время до заземления на SDU410 и разъеме C4. | Менее 10 Ом? |
| ШАГ 2. | Проверьте OEM проводку жгут |  |
|  | **STEP 2A.** Проверьте сигнал 1 оборота двигателя и провода возврата для разъемов C4 и C11. | Менее 10 Ом? |
|  | **STEP 2A-1.** Проверьте сигнал 2 оборота двигателя и провода возврата для разъемов C4 и C11. | Менее 10 Ом? |
|  | **STEP 2B.** Проверьте сигнал 1 оборота двигателя и провода возврата для короткого провода на разъемах C4 и C11. | Менее 10 Ом? |
|  | **STEP 2B-1.** Проверьте сигнал 2 оборота двигателя и провода возврата для короткого провода на разъемах C4 и C11. | Менее 10 Ом? |
|  | **STEP 2C.** Проверьте скорость 1 сигнала двигателя на короткое время до заземления на разъемах C4 и C11. | Менее 10 Ом? |
|  | **STEP 2C-1.** Проверьте скорость 2 двигателя на короткое время на земле на разъемах C4 и C11. | Менее 10 Ом? |

### ШАГ 1. Проверьте клиентский интерфейс коробки проводов.

#### ШАГ 1A. Проверьте устройство SDU410 на наличие сигнализации и светодиодной подсветки.

| **Условия:** Проверить наличие сигнализации и светодиодного освещения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте устройство SDU410 на наличие сигнализации и мигающего светодиода. Нажмите и удерживайте кнопку тестирования на сверхскоростной скорости, чтобы очистить режим тестирования на сверхскоростной скорости. | Светодиод быстро мигает? Заменить модуль SDU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Светодиод быстро мигает? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте конфигурацию блока SDU410.

| **Условия:** Проверьте параметры конфигурации блока SDU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте конфигурацию блока SDU410. Убедитесь, что порог скорости двигателя правильный. | Правильно ли пороговое значение? Заменить модуль SDU410. Обратитесь в авторизованный сервисный центр Cummins®. | 1С |
| Правильно ли пороговое значение? **NORepair:** Установите правильный параметр скорости. Обратитесь в авторизованный сервисный центр Cummins®. | 1В |  |

#### ШАГ 1C. Проверьте сигнал 1 оборота двигателя и верните провода для открытого.

| **Условия: **Откройте окно интерфейса клиента. Отсоедините сигнал 1 оборота двигателя и провода возврата от блока SDU410 и отсоедините разъем C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал и верните провода для открытого. Поместите один испытательный щуп на провод питания 1 двигателя на блоке SDU410. Поместите другой испытательный щуп на контакт сигнала скорости двигателя 1 на разъеме C4. Поместите один испытательный щуп на обратный провод двигателя 1 на блоке SDU410. Поместите другой испытательный щуп на обратный контакт скорости двигателя 1 на разъеме C4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1С-1-1 |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1C-1. Проверьте сигнал 2 оборота двигателя и верните провода для открытого.

| **Условия: **Откройте окно интерфейса клиента. Отсоедините сигнал 2 оборота двигателя и провода возврата от блока SDU410 и отсоедините разъем C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал и верните провода для открытого. Поместите один испытательный щуп на провод питания 2-го двигателя в блок SDU410. Поместите другой испытательный щуп на контакт сигнала 2 скорости двигателя на разъеме C4. Поместите один испытательный щуп на обратный провод 2 оборота двигателя в блок SDU410. Поместите другой испытательный щуп на обратный контакт с двигателем 2 на разъеме C4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1D |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1D. Проверьте сигнал 1 оборота двигателя и возвратные провода для короткого провода на блоке SDU410 и разъеме C4.

| **Условия: **Откройте окно интерфейса клиента. Отсоедините сигнал 1 оборота двигателя и провода возврата от блока SDU410 и отсоедините разъем C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал и верните провода для короткого провода к проводу. Поместите один испытательный щуп на провод сигнала 1 скорости двигателя в блок SDU410. Поместите другой испытательный щуп на все другие провода на блоке SDU410. Поместите один испытательный щуп на обратный провод двигателя 1 на блоке SDU410. Поместите другой испытательный щуп на все другие провода на блоке SDU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1D-1 |  |

#### ШАГ 1D-1. Проверьте сигнал 2 оборота двигателя и возвратные провода для короткого провода на блоке SDU410 и разъеме C4.

| **Условия: **Откройте окно интерфейса клиента. Отсоедините сигнал 2 оборота двигателя и провода возврата от блока SDU410 и отсоедините разъем C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал и верните провода для короткого провода к проводу. Поместите один испытательный щуп на провод питания 2-го двигателя в блок SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. Поместите один испытательный щуп на обратный провод 2 оборота двигателя в блок SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1Е |  |

#### ШАГ 1E. Проверьте скорость 1 сигнала двигателя на короткое время до земли в блоке SDU410 и разъеме C4.

| **Условия: **Откройте окно интерфейса клиента. Отсоедините провод сигнала 1 оборота двигателя от блока SDU410 и отсоедините разъем C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнальный провод на короткое время до земли. Поместите один испытательный щуп на сигнал скорости двигателя 1 в блок SDU410. Поместите другой испытательный щуп на панель. Поместите один испытательный щуп на контакт сигнала скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1Е-1 |  |

#### ШАГ 1E-1. Проверьте скорость 2 двигателя сигнального провода для короткого приземления на блоке SDU410 и разъеме C4.

| **Условия: **Откройте окно интерфейса клиента. Отсоедините сигнальный провод 2 оборота двигателя от блока SDU410 и отсоедините разъем C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнальный провод на короткое время до земли. Поместите один испытательный щуп на сигнал 2 оборота двигателя в блок SDU410. Поместите другой испытательный щуп на панель. Поместите один испытательный щуп на контакт сигнала скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов изготовителя машины.

#### ШАГ 2A. Проверьте сигнал 1 оборота двигателя и возвратные провода для открытия на разъемах C4 и C11.

| **Условия: **Откройте окно интерфейса клиента. Отключите разъемы датчиков C4, C11 и 1 скорости двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал и верните провода для открытого. Поместите один испытательный щуп на контакт сигнала скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на контакт сигнала 1 скорости двигателя на разъеме C11. Поместите один испытательный щуп на обратный контакт скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на обратный контакт с двигателем 1 на разъеме C11. Поместите один испытательный щуп на контакт сигнала скорости двигателя 1 на разъем датчика. Поместите другой испытательный щуп на контакт сигнала 1 скорости двигателя на разъеме C11. Поместите один испытательный щуп на скорость 1 оборота двигателя обратного контакта на разъем датчика. Поместите другой испытательный щуп на обратный контакт с двигателем 1 на разъеме C11. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2А-1-1 |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2A-1. Проверьте сигнал 2 оборота двигателя и возвратные провода для открытого соединения на разъемах C4 и C11.

| **Условия: **Откройте окно интерфейса клиента. Отключите разъемы датчиков C4, C11 и 2 скорости двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал и верните провода для открытого. Поместите один испытательный щуп на контакт сигнала 2 оборота двигателя на разъеме С4. Поместите другой испытательный щуп на контакт сигнала 2 скорости двигателя на разъеме C11. Поместите один испытательный щуп на обратный контакт 2 оборота двигателя на разъеме C4. Поместите другой испытательный щуп на обратный контакт с двигателем 2 на разъеме C11. Поместите один испытательный щуп на контакт сигнала 2 скорости двигателя на разъем датчика. Поместите другой испытательный щуп на контакт сигнала 2 скорости двигателя на разъеме C11. Поместите один испытательный щуп на скорость 2 оборота двигателя обратного контакта на разъем датчика. Поместите другой испытательный щуп на обратный контакт с двигателем 2 на разъеме C11. См. схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2B. Проверьте скорость двигателя 1 сигнал и возврат проводов для провода к проводу короткой на разъемах C4 и C11.

| **Условия: **Откройте окно интерфейса клиента. Отключите разъемы C4 и C11. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал и верните провода для короткого провода к проводу. Поместите один испытательный щуп на контакт сигнала скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на все другие штифты на разъеме C4. Поместите один испытательный щуп на обратный контакт скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на все другие штифты на разъеме C4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2В-1-1 |  |

#### ШАГ 2B-1. Проверьте скорость двигателя 2 проводной сигнал и вернитесь к короткому проводу на разъемах C4 и C11.

| **Условия: **Откройте окно интерфейса клиента. Отключите разъемы C4 и C11. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал и верните провода для короткого провода к проводу. Поместите один испытательный щуп на контакт сигнала 2 скорости двигателя на разъеме C4. Поместите другой испытательный щуп на все другие штифты на разъеме C4. Поместите один испытательный щуп на обратный контакт 2 оборота двигателя на разъеме C4. Поместите другой испытательный щуп на все другие штифты на разъеме C4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте скорость 1 сигнала двигателя на короткое время, чтобы заземлиться на разъемах C4 и C11.

| **Условия: **Откройте окно интерфейса клиента. Отключите разъемы датчиков C4, C11 и 1 скорости двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнальный провод на короткое время до земли. Поместите один испытательный щуп на контакт сигнала скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на панель. Поместите один испытательный щуп на контакт сигнала 1 скорости двигателя на разъеме C11. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на контакт сигнала 1 оборота двигателя на разъем датчика 1 оборота двигателя. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2С-1 |  |

#### ШАГ 2C-1. Проверьте скорость 2 двигателя сигнального провода для короткого приземления на разъемах C4 и C11.

| **Условия: **Откройте окно интерфейса клиента. Отключите разъемы датчиков C4, C11 и 2 скорости двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнальный провод на короткое время до земли. Поместите один испытательный щуп на контакт сигнала 2 скорости двигателя на разъеме C4. Поместите другой испытательный щуп на панель. Поместите один испытательный щуп на контакт сигнала 2 скорости двигателя на разъеме C11. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на контакт сигнала 2 оборота двигателя на разъем датчика 2 оборота двигателя. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | Свяжитесь с авторизованным местом ремонта Cummins® |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The SDU410 shuts down engine due to overspeed even though engine was running at normal speed.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check customer interface box wiring |  |
> |  | **STEP 1A.** Check the SDU410 unit for alarms and LED illumination. | LED flashing rapidly? |
> |  | **STEP 1A-1.** Check the engine speed 2 signal and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 1B.** Check the SDU410 unit configuration. | Is threshold value correct? |
> |  | **STEP 1C.** Check the engine speed 1 signal and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 1C-1.** Check the engine speed 2 signal and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 1D.** Check the engine speed 1 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector. | Less than 10 ohms? |
> |  | **STEP 1D-1.** Check the engine speed 2 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector. | Less than 10 ohms? |
> |  | **STEP 1E.** Check the engine speed 1 signal wire for a short to ground at the SDU410 unit and C4 connector. | Less than 10 ohms? |
> |  | **STEP 1E-1.** Check the engine speed 2 signal wire for a short to ground at the SDU410 unit and C4 connector. | Less than 10 ohms? |
> | STEP 2. | Check the OEM wiring harness |  |
> |  | **STEP 2A.** Check the engine speed 1 signal and return wires for an open at the C4 and C11 connectors. | Less than 10 ohms? |
> |  | **STEP 2A-1.** Check the engine speed 2 signal and return wires for an open at the C4 and C11 connectors. | Less than 10 ohms? |
> |  | **STEP 2B.** Check the engine speed 1 signal and return wires for a wire-to-wire short at the C4 and C11 connectors. | Less than 10 ohms? |
> |  | **STEP 2B-1.** Check the engine speed 2 signal and return wires for a wire-to-wire short at the C4 and C11 connectors. | Less than 10 ohms? |
> |  | **STEP 2C.** Check the engine speed 1 signal wire for a short to ground at the C4 and C11 connectors. | Less than 10 ohms? |
> |  | **STEP 2C-1.** Check the engine speed 2 signal wire for a short to ground at the C4 and C11 connectors. | Less than 10 ohms? |
>
> ### STEP 1. Check the customer interface box wiring.
>
> #### STEP 1A. Check the SDU410 unit for alarms and LED illumination.
>
> | **Conditions:** Check for alarm and LED illumination. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SDU410 unit for alarms and flashing LED. Press and hold the overspeed test button to clear overspeed test mode. | LED flashing rapidly? **YESRepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | LED flashing rapidly? **NO** | 1B |  |
>
> #### STEP 1B. Check the SDU410 unit configuration.
>
> | **Conditions:** Check SDU410 unit configuration parameters. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SDU410 unit configuration. Be sure the engine overspeed threshold is correct. | Is threshold value correct? **YESRepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | 1C |
> | Is threshold value correct? **NORepair:** Set the correct overspeed parameter. Contact a Cummins® Authorized Repair Location. | 1B |  |
>
> #### STEP 1C. Check the engine speed 1 signal and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for an open. Place one test lead on the engine speed 1 supply wire at the SDU410 unit. Place the other test lead on the engine speed 1 signal pin at the C4 connector. Place one test lead on the engine speed 1 return wire at the SDU410 unit. Place the other test lead on the engine speed 1 return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C-1 |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1C-1. Check the engine speed 2 signal and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 2 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for an open. Place one test lead on the engine speed 2 supply wire at the SDU410 unit. Place the other test lead on the engine speed 2 signal pin at the C4 connector. Place one test lead on the engine speed 2 return wire at the SDU410 unit. Place the other test lead on the engine speed 2 return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1D. Check the engine speed 1 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 1 signal wire at the SDU410 unit. Place the other test lead on all other wires on the SDU410 unit. Place one test lead on the engine speed 1 return wire at the SDU410 unit. Place the other test lead on all other wires on the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1D-1 |  |
>
> #### STEP 1D-1. Check the engine speed 2 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 2 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 2 supply wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the engine speed 2 return wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1E |  |
>
> #### STEP 1E. Check the engine speed 1 signal wire for a short to ground at the SDU410 unit and C4 connector.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal wire from the SDU410 unit and disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal wire for short to ground. Place one test lead on the engine speed 1 signal at the SDU410 unit. Place the other test lead to panel ground. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1E-1 |  |
>
> #### STEP 1E-1. Check the engine speed 2 signal wire for a short to ground at the SDU410 unit and C4 connector.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 2 signal wire from the SDU410 unit and disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal wire for short to ground. Place one test lead on the engine speed 2 signal at the SDU410 unit. Place the other test lead to panel ground. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM wiring harness.
>
> #### STEP 2A. Check the engine speed 1 signal and return wires for an open at the C4 and C11 connectors.
>
> | **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 1 sensor connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for an open. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on the engine speed 1 signal pin at the C11 connector. Place one test lead on the engine speed 1 return pin at the C4 connector. Place the other test lead on the engine speed 1 return pin at the C11 connector. Place one test lead on the engine speed 1 signal pin at the sensor connector. Place the other test lead on the engine speed 1 signal pin at the C11 connector. Place one test lead on the engine speed 1 return pin at the sensor connector. Place the other test lead on the engine speed 1 return pin at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2A-1 |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2A-1. Check the engine speed 2 signal and return wires for an open at the C4 and C11 connectors.
>
> | **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 2 sensor connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for an open. Place one test lead on the engine speed 2 signal pin at C4 connector. Place the other test lead on the engine speed 2 signal pin at the C11 connector. Place one test lead on the engine speed 2 return pin at the C4 connector. Place the other test lead on the engine speed 2 return pin at the C11 connector. Place one test lead on the engine speed 2 signal pin at the sensor connector. Place the other test lead on the engine speed 2 signal pin at the C11 connector. Place one test lead on the engine speed 2 return pin at the sensor connector. Place the other test lead on the engine speed 2 return pin at the C11 connector. Refer to the circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2B. Check the engine speed 1 signal and return wires for a wire-to-wire short at the C4 and C11 connectors.
>
> | **Conditions:** Open the customer interface box. Disconnect the C4 and C11 connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the engine speed 1 return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2B-1 |  |
>
> #### STEP 2B-1. Check the engine speed 2 wire signal and return for a wire-to-wire short at the C4 and C11 connectors.
>
> | **Conditions:** Open the customer interface box. Disconnect the C4 and C11 connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 2 signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the engine speed 2 return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the engine speed 1 signal wire for a short to ground at the C4 and C11 connectors.
>
> | **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 1 sensor connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal wire for short to ground. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead to panel ground. Place one test lead on the engine speed 1 signal pin at the C11 connector. Place the other test lead on panel ground. Place one test lead on the engine speed 1 signal pin at the engine speed 1 sensor connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2C-1 |  |
>
> #### STEP 2C-1. Check the engine speed 2 signal wire for a short to ground at the C4 and C11 connectors.
>
> | **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 2 sensor connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal wire for short to ground. Place one test lead on the engine speed 2 signal pin at the C4 connector. Place the other test lead to panel ground. Place one test lead on the engine speed 2 signal pin at the C11 connector. Place the other test lead on panel ground. Place one test lead on the engine speed 2 signal pin at the engine speed 2 sensor connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location |  |
