---
aliases:
  - "Для останова использован неверный сигнал датчика частоты"
type: "Процедура"
doc: "116-t02-1099"
title_en: "Incorrect Speed Pickup Signal Used to Shut Down Unit"
title_ru: "Для останова использован неверный сигнал датчика частоты"
modified: "2008-04-04"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1099.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1099.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Incorrect Speed Pickup Signal Used to Shut Down Unit
**Для останова использован неверный сигнал датчика частоты**

> [!abstract] Процедура · `116-t02-1099`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1099.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1099.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Значение скорости двигателя SDU410 некорректно.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Установка SDU410 имеет два входных сигнала скорости двигателя. Если сигналы различаются, то в качестве сигнала блок SDU410 использует более высокое из двух показаний.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте интерфейс клиента |  |
|  | **STEP 1A.** Проверьте логическую блокировку светодиодного освещения в интерфейсе клиента. | Активны ли какие-либо сигналы тревоги или светодиоды освещены? |
|  | **STEP 1B.** Проверьте провод электропитания SDU410 на +24-VDC. | Меньше +24-VDC? |
| ШАГ 2. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 2A.** Проверьте скорость двигателя 1 и скорость двигателя 2 сигнала и возвращайте провода для открытого. | Менее 10 Ом? |
|  | **STEP 1A-1.** Проверьте сигнал 2 оборота двигателя и провода возврата для открытого. | Менее 10 Ом? |
|  | **STEP 2B.** Проверьте сигнал 1 оборота двигателя и провода возврата для короткого провода на блоке SDU410 и разъеме C4. | Менее 10 Ом? |
|  | **STEP 1B-1.** Проверьте сигнал 2 оборота двигателя и провода возврата для короткого провода на блоке SDU410 и разъеме C4. | Менее 10 Ом? |
|  | **STEP 2C.** Проверьте скорость 1 сигнала двигателя на короткое время до заземления на SDU410 и разъеме C4. | Менее 10 Ом? |
|  | **STEP 2C-1.** Проверьте скорость 2 двигателя на короткое время до заземления на SDU410 и разъеме C4. | Менее 10 Ом? |
| ШАГ 3. | Проверьте OEM проводку жгут |  |
|  | **STEP 3A.** Проверьте сигнал 1 оборота двигателя и провода возврата для разъемов C4 и C11. | Менее 10 Ом? |
|  | **STEP 3A-1.** Проверьте сигнал 2 оборота двигателя и провода возврата для разъемов C4 и C11. | Менее 10 Ом? |
|  | **STEP 3B.** Проверьте сигнал 1 оборота двигателя и провода возврата для короткого провода на разъемах C4 и C11. | Менее 10 Ом? |
|  | **STEP 3B-1.** Проверьте скорость двигателя 2 сигнала и провода возврата для короткого провода на разъемах C4 и C11. | Менее 10 Ом? |
|  | **STEP 3C.** Проверьте скорость двигателя 1 сигнального провода на короткое время до заземления на разъеме С4. | Менее 10 Ом? |
|  | **STEP 3C-1.** Проверьте скорость 2 двигателя на короткое время на земле на разъемах C4 и C11. | Менее 10 Ом? |

### ШАГ 1. Проверьте интерфейс клиента

#### ШАГ 1A. Проверьте логическое устройство клиентского интерфейса LED подсветка.

| ** Условия:** Проверьте устройство DCU410 на наличие сигнализации и светодиодной подсветки. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте наличие сигнализации и светодиодной подсветки на устройстве DCU410. | Активны ли какие-либо сигналы тревоги или светодиоды освещены? *Да** | Свяжитесь с авторизованным местом ремонта Cummins® |
| Активны ли какие-либо сигналы тревоги или светодиоды освещены? ** НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте провод питания DCU410 для +24-VDC.

| ** Условия: ** Откройте окно интерфейса клиента |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте напряжение на блоке отключения питания 24-VDC на блоке SDU410. Поместите один испытательный щуп на блок отключения питания 24-VDC на блоке питания SDU410. Поместите другой испытательный щуп на провод возврата блока отключения в блок SDU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? *** Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |
| Меньше +24-VDC? ** НЕТ** | 2А |  |

### ШАГ 2. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 2A. Проверьте сигнал 1 оборота двигателя и верните провода для открытого.

| **Условия: ** Откройте окно интерфейса клиента. Отсоедините скорость двигателя 1 и скорость двигателя 2 сигнала и возвращайте провода от блока SDU410 и отсоедините разъем C4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнал и верните провода для открытого. Поместите один испытательный щуп на провод питания 1 двигателя на блоке SDU410. Поместите другой испытательный щуп на контакт сигнала скорости двигателя 1 на разъеме C4. Поместите один испытательный щуп на обратный провод двигателя 1 на блоке SDU410. Поместите другой испытательный щуп на двигатель 1 обратного контакта на разъеме С4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 2А-1-1 |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2A-1. Проверьте сигнал 2 оборота двигателя и верните провода для открытого.

| **Условия: ** Откройте окно интерфейса клиента. Отсоедините сигнал 2 оборота двигателя и провода возврата от блока SDU410 и отсоедините разъем C4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнал и верните провода для открытого. Поместите один испытательный щуп на провод питания 2-го двигателя в блок SDU410. Поместите другой испытательный щуп на контакт сигнала 2 скорости двигателя на разъеме C4. Поместите один испытательный щуп на обратный провод 2 оборота двигателя в блок SDU410. Поместите другой испытательный щуп на обратный контакт с двигателем 2 на разъеме C4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2B. Проверьте сигнал 1 оборота двигателя и возвратные провода для короткого провода на блоке SDU410 и разъеме C4.

| **Условия: ** Откройте окно интерфейса клиента. Отсоедините сигнал 1 оборота двигателя и провода возврата от блока SDU410 и отсоедините разъем C4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнал и верните провода для короткого провода к проводу. Поместите один испытательный щуп на сигнал скорости двигателя 1 в блок SDU410. Поместите другой испытательный щуп на все другие провода на блоке SDU410. Поместите один испытательный щуп на обратный провод двигателя 1 на блоке SDU410. Поместите другой испытательный щуп на все другие провода на блоке SDU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2В-1-1 |  |

#### ШАГ 2B-1. Проверьте сигнал 2 оборота двигателя и возвратные провода для короткого провода на блоке SDU410 и разъеме C4.

| **Условия: ** Откройте окно интерфейса клиента. Отсоедините датчик 2 оборотов двигателя и отсоедините провода возврата от блока SDU410 и отсоедините разъем C4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнал и верните провода для короткого провода к проводу. Поместите один испытательный щуп на провод питания 2-го двигателя в блок SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. Поместите один испытательный щуп на обратный провод 2 оборота двигателя в блок SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте скорость 1 сигнала двигателя на короткое время до земли в блоке SDU410 и разъеме C4.

| **Условия: ** Откройте окно интерфейса клиента. Отсоедините провод сигнала 1 оборота двигателя от блока SDU410 и отсоедините разъем C4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнальный провод на короткое время до земли. Поместите один испытательный щуп на провод сигнала 1 скорости двигателя в блок SDU410. Поместите другой испытательный щуп на панель. Поместите один испытательный щуп на контакт сигнала скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2С-1 |  |

#### ШАГ 2C-1. Проверьте скорость 2 двигателя сигнального провода для короткого приземления на блоке SDU410 и разъеме C4.

| **Условия: ** Откройте окно интерфейса клиента. Отсоедините сигнальный провод 2 оборота двигателя от блока SDU410 и отсоедините разъем C4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнальный провод на короткое время до земли. Поместите один испытательный щуп на сигнальный провод 2 оборота двигателя в блок SDU410. Поместите другой испытательный щуп на панель. Поместите один испытательный щуп на контакт сигнала скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 3А |  |

### ШАГ 3. Проверьте OEM проводку жгут

#### ШАГ 3A. Проверьте сигнал 1 оборота двигателя и возвратные провода для открытия на разъемах C4 и C11.

| **Условия: ** Откройте окно интерфейса клиента. Отключите разъемы датчиков C4, C11 и 1 скорости двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнал и верните провода для открытого. Поместите один испытательный щуп на контакт сигнала 1 оборота двигателя на разъеме С4. Поместите другой испытательный щуп на контакт сигнала 1 скорости двигателя на разъеме C11. Поместите один испытательный щуп на обратный контакт скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на обратный контакт с двигателем 1 на разъеме C11. Поместите один испытательный щуп на контакт сигнала скорости двигателя 1 на разъем датчика. Поместите другой испытательный щуп на контакт сигнала 1 скорости двигателя на разъеме C11. Поместите один испытательный щуп на скорость 1 оборота двигателя обратного контакта на разъем датчика. Поместите другой испытательный щуп на обратный контакт с двигателем 1 на разъеме C11. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 3А-1-1 |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 3A-1. Проверьте сигнал 2 оборота двигателя и возвратные провода для открытого соединения на разъемах C4 и C11.

| **Условия: ** Откройте окно интерфейса клиента. Отключите разъемы датчиков C4, C11 и 2 скорости двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнал и верните провода для открытого. Поместите один испытательный щуп на контакт сигнала 2 оборота двигателя на разъеме С4. Поместите другой испытательный щуп на контакт сигнала 2 скорости двигателя на разъеме C11. Поместите один испытательный щуп на обратный контакт 2 оборота двигателя на разъеме C4. Поместите другой испытательный щуп на обратный контакт с двигателем 2 на разъеме C11. Поместите один испытательный щуп на контакт сигнала 2 скорости двигателя на разъем датчика. Поместите другой испытательный щуп на контакт сигнала 2 скорости двигателя на разъеме C11. Поместите один испытательный щуп на скорость 2 оборота двигателя обратного контакта на разъем датчика. Поместите другой испытательный щуп на обратный контакт с двигателем 2 на разъеме C11. См. схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 3B |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 3B. Проверьте скорость двигателя 1 сигнал и возврат проводов для провода к проводу короткой на разъемах C4 и C11.

| **Условия: ** Откройте окно интерфейса клиента. Отключите разъемы датчиков C4, C11 и 1 скорости двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнал и верните провода для короткого провода к проводу. Поместите один испытательный щуп на контакт сигнала скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на все другие штифты на разъеме C4. Поместите один испытательный щуп на обратный контакт скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на все другие штифты на разъеме C4. Поместите один испытательный щуп на контакт сигнала 1 скорости двигателя на разъеме C11. Поместите другой испытательный щуп на все другие штифты на разъеме C11. Поместите один испытательный щуп на обратный контакт скорости двигателя 1 на разъеме C11. Поместите другой испытательный щуп на все другие штифты на разъеме C11. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 3В-1-1 |  |

#### ШАГ 3B-1. Проверьте сигнал 2 оборота двигателя и возвратные провода для короткого провода на разъемах C4 и C11.

| **Условия: ** Откройте окно интерфейса клиента. Отключите разъемы датчиков C4, C11 и 2 скорости двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнал и верните провода для короткого провода к проводу. Поместите один испытательный щуп на контакт сигнала 2 скорости двигателя на разъеме C4. Поместите другой испытательный щуп на все другие штифты на разъеме C4. Поместите один испытательный щуп на обратный контакт 2 оборота двигателя на разъеме C4. Поместите другой испытательный щуп на все другие штифты на разъеме C4. Поместите один испытательный щуп на контакт сигнала 2 скорости двигателя на разъеме C11. Поместите другой испытательный щуп на все другие штифты на разъеме C11. Поместите один испытательный щуп на обратный контакт 2-го двигателя на разъеме C11. Поместите другой испытательный щуп на все другие штифты на разъеме C11. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 3C |  |

#### ШАГ 3C. Проверьте скорость 1 сигнала двигателя на короткое время, чтобы заземлиться на разъемах C4 и C11.

| **Условия: ** Откройте окно интерфейса клиента. Отключите разъемы датчиков C4, C11 и 1 скорости двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнальный провод на короткое время до земли. Поместите один испытательный щуп на контакт сигнала скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на панель. Поместите один испытательный щуп на контакт сигнала 1 скорости двигателя на разъеме C11. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на контакт сигнала 1 оборота двигателя на датчике 1 разъема скорости двигателя. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 3С-1-1 |  |

#### ШАГ 3C-1. Проверьте скорость 2 двигателя сигнального провода для короткого приземления на разъемах C4 и C11.

| **Условия: ** Откройте окно интерфейса клиента. Отключите разъемы датчиков C4, C11 и 2 скорости двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнальный провод на короткое время до земли. Поместите один испытательный щуп на контакт сигнала 2 скорости двигателя на разъеме C4. Поместите другой испытательный щуп на панель. Поместите один испытательный щуп на контакт сигнала 2 скорости двигателя на разъеме C11. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на контакт сигнала 2 оборота двигателя на датчике 1 разъема скорости двигателя. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **Норэпэр:** Шаги устранения неполадок*** должны быть проверены с самого начала. Режим неисправности должен был быть обнаружен. | 1А |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The SDU410 unit engine speed value is incorrect.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The SDU410 unit has two engine speed input signals. If the signals differ, the SDU410 unit uses the higher of the two readings as the signal.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check customer interface box |  |
> |  | **STEP 1A.** Check the customer interface box logic unit LED illumination. | Are any alarms active or LEDs illuminated? |
> |  | **STEP 1B.** Check the SDU410 power supply wire for +24-VDC. | Less than +24-VDC? |
> | STEP 2. | Check customer interface box wiring |  |
> |  | **STEP 2A.** Check the engine speed 1 and engine speed 2 signal and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 1A-1.** Check the engine speed 2 signal and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 2B.** Check the engine speed 1 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector. | Less than 10 ohms? |
> |  | **STEP 1B-1.** Check the engine speed 2 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector. | Less than 10 ohms? |
> |  | **STEP 2C.** Check the engine speed 1 signal wire for a short to ground at the SDU410 unit and C4 connector. | Less than 10 ohms? |
> |  | **STEP 2C-1.** Check the engine speed 2 signal wire for a short to ground at the SDU410 unit and C4 connector. | Less than 10 ohms? |
> | STEP 3. | Check the OEM wiring harness |  |
> |  | **STEP 3A.** Check the engine speed 1 signal and return wires for an open at the C4 and C11 connectors. | Less than 10 ohms? |
> |  | **STEP 3A-1.** Check the engine speed 2 signal and return wires for an open at the C4 and C11 connectors. | Less than 10 ohms? |
> |  | **STEP 3B.** Check the engine speed 1 signal and return wires for a wire-to-wire short at the C4 and C11 connectors. | Less than 10 ohms? |
> |  | **STEP 3B-1.** Check the engine speed 2 signal and return wires for a wire-to-wire short at the C4 and C11 connectors. | Less than 10 ohms? |
> |  | **STEP 3C.** Check the engine speed 1 signal wire for a short to ground at the C4 connector. | Less than 10 ohms? |
> |  | **STEP 3C-1.** Check the engine speed 2 signal wire for a short to ground at the C4 and C11 connectors. | Less than 10 ohms? |
>
> ### STEP 1. Check customer interface box
>
> #### STEP 1A. Check the customer interface box logic unit LED illumination.
>
> | **Conditions:** Check the DCU410 unit for alarms and LED illumination. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for alarms and LED illumination on the DCU410 unit. | Are any alarms active or LEDs illuminated? **YES** | Contact a Cummins® Authorized Repair Location |
> | Are any alarms active or LEDs illuminated? **NO** | 1B |  |
>
> #### STEP 1B. Check the DCU410 power supply wire for +24-VDC.
>
> | **Conditions:** Open the customer interface box |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the shutdown unit supply 24-VDC at the SDU410 unit. Place one test lead on the shutdown unit supply 24-VDC supply wire at the SDU410 unit. Place the other test lead on the shutdown unit return wire at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than +24-VDC? **NO** | 2A |  |
>
> ### STEP 2. Check customer interface box wiring
>
> #### STEP 2A. Check the engine speed 1 signal and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 1 and engine speed 2 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for an open. Place one test lead on the engine speed 1 supply wire at the SDU410 unit. Place the other test lead on the engine speed 1 signal pin at the C4 connector. Place one test lead on the engine speed 1 return wire at the SDU410 unit. Place the other test lead on the engine 1 return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2A-1 |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2A-1. Check the engine speed 2 signal and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 2 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for an open. Place one test lead on the engine speed 2 supply wire at the SDU410 unit. Place the other test lead on the engine speed 2 signal pin at the C4 connector. Place one test lead on the engine speed 2 return wire at the SDU410 unit. Place the other test lead on the engine speed 2 return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2B. Check the engine speed 1 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 1 signal at the SDU410 unit. Place the other test lead on all other wires on the SDU410 unit. Place one test lead on the engine speed 1 return wire at the SDU410 unit. Place the other test lead on all other wires on the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2B-1 |  |
>
> #### STEP 2B-1. Check the engine speed 2 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed sensor 2 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 2 supply wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the engine speed 2 return wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the engine speed 1 signal wire for a short to ground at the SDU410 unit and C4 connector.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal wire from the SDU410 unit and disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal wire for short to ground. Place one test lead on the engine speed 1 signal wire at the SDU410 unit. Place the other test lead to panel ground. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2C-1 |  |
>
> #### STEP 2C-1. Check the engine speed 2 signal wire for a short to ground at the SDU410 unit and C4 connector.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 2 signal wire from the SDU410 unit and disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal wire for short to ground. Place one test lead on the engine speed 2 signal wire at the SDU410 unit. Place the other test lead to panel ground. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 3A |  |
>
> ### STEP 3. Check the OEM wiring harness
>
> #### STEP 3A. Check the engine speed 1 signal and return wires for an open at the C4 and C11 connectors.
>
> | **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 1 sensor connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for an open. Place one test lead on the engine speed 1 signal pin at C4 connector. Place the other test lead on the engine speed 1 signal pin at the C11 connector. Place one test lead on the engine speed 1 return pin at the C4 connector. Place the other test lead on the engine speed 1 return pin at the C11 connector. Place one test lead on the engine speed 1 signal pin at the sensor connector. Place the other test lead on the engine speed 1 signal pin at the C11 connector. Place one test lead on the engine speed 1 return pin at the sensor connector. Place the other test lead on the engine speed 1 return pin at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3A-1 |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 3A-1. Check the engine speed 2 signal and return wires for an open at the C4 and C11 connectors.
>
> | **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 2 sensor connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for an open. Place one test lead on the engine speed 2 signal pin at C4 connector. Place the other test lead on the engine speed 2 signal pin at the C11 connector. Place one test lead on the engine speed 2 return pin at the C4 connector. Place the other test lead on the engine speed 2 return pin at the C11 connector. Place one test lead on the engine speed 2 signal pin at the sensor connector. Place the other test lead on the engine speed 2 signal pin at the C11 connector. Place one test lead on the engine speed 2 return pin at the sensor connector. Place the other test lead on the engine speed 2 return pin at the C11 connector. Refer to the circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 3B. Check the engine speed 1 signal and return wires for a wire-to-wire short at the C4 and C11 connectors.
>
> | **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 1 sensor connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the engine speed 1 return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the engine speed 1 signal pin at the C11 connector. Place the other test lead on all other pins at the C11 connector. Place one test lead on the engine speed 1 return pin at the C11 connector. Place the other test lead on all other pins at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 3B-1 |  |
>
> #### STEP 3B-1. Check the engine speed 2 signal and return wires for a wire-to-wire short at the C4 and C11 connectors.
>
> | **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 2 sensor connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 2 signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the engine speed 2 return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the engine speed 2 signal pin at the C11 connector. Place the other test lead on all other pins at the C11 connector. Place one test lead on the engine speed 2 return pin at the C11 connector. Place the other test lead on all other pins at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 3C |  |
>
> #### STEP 3C. Check the engine speed 1 signal wire for a short to ground at the C4 and C11 connectors.
>
> | **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 1 sensor connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal wire for short to ground. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead to panel ground. Place one test lead on the engine speed 1 signal pin at the C11 connector. Place the other test lead on panel ground. Place one test lead on the engine speed 1 signal pin at the engine speed sensor 1 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 3C-1 |  |
>
> #### STEP 3C-1. Check the engine speed 2 signal wire for a short to ground at the C4 and C11 connectors.
>
> | **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 2 sensor connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal wire for short to ground. Place one test lead on the engine speed 2 signal pin at the C4 connector. Place the other test lead to panel ground. Place one test lead on the engine speed 2 signal pin at the C11 connector. Place the other test lead on panel ground. Place one test lead on the engine speed 2 signal pin at the engine speed sensor 1 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NORepair:** The troubleshooting steps **must** be checked again from the beginning. A fault mode should have been detected. | 1A |  |
