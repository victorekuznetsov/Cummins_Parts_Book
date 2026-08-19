---
aliases:
  - "Стартер не отключается"
type: "Процедура"
doc: "116-t02-1007"
title_en: "Starter Does Not Disengage"
title_ru: "Стартер не отключается"
modified: "2008-06-02"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Starter Does Not Disengage
**Стартер не отключается**

> [!abstract] Процедура · `116-t02-1007`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-06-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1007.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Стартер делает **не** отключение после включения двигателя и переключатель зажигания находится в положении Включения.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента. |  |
|  | **STEP 1A.** Проверьте логическую блокировку светодиодного освещения в интерфейсе клиента. |  |
|  | **STEP 1B.** Проверьте провод питания DCU410 на напряжение +24-VDC. |  |
|  | **STEP 1C.** Проверьте скорость 1 и скорость 2 двигателя на наличие проводов сигнала. |  |
|  | **STEP 1D.** Проверьте скорость 1 и скорость 2 оборота двигателя на наличие проводов с открытым исходным кодом. |  |
|  | **ШАГ 1Е.** Проверьте провод сигнала переключателя реле стартера на наличие открытого. |  |
|  | **STEP 1F.** Проверьте блок отключения питания шины связи ModiconTM и провода возврата для открытого доступа. |  |
|  | **STEP 1G.** Проверьте скорость двигателя 1 и скорость двигателя 2 сигнал и обратные провода для короткого провода к проводу. |  |
|  | **STEP 1H.** Проверьте блок отключения питания шины связи ModiconTM и провода возврата для короткого провода к проводу. |  |
|  | **STEP 1I.** Проверьте скорость двигателя 1 и скорость двигателя 2 сигнальных проводов для короткого до земли. |  |
|  | **STEP 1J.** Проверьте отключаемый блок питания коммуникационной шины ModiconTM на короткое время до заземления. |  |
| ШАГ 2. | Проверьте жгут проводов изготовителя машины. |  |
|  | **STEP 2A.** Проверьте сигнал переключателя реле стартера и провода возврата для открытого. |  |
|  | **STEP 2B.** Проверьте сигнал переключателя реле стартера и провода возврата для короткого провода к проводу. |  |
|  | **STEP 2C.** Проверить сигнальный провод стартового реле-переключателя на короткое время до заземления. |  |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте логическое устройство клиентского интерфейса LED подсветка.

| **Условия: ** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте лампу с коленчатым приводом на блоке DCU 410 или удаленной панели для освещения. | Светильник с кривошипом? *Да** | 1В |
| Светильник с кривошипом? ** НЕТ** | Свяжитесь с авторизованным местом ремонта Cummins® |  |

#### ШАГ 1B. Проверьте провод питания DCU410 на напряжение +24-VDC.

| **Условия: ** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? *** Ремонт:** Проверить аккумуляторы. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Меньше +24-VDC? ** НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте скорость двигателя 1 и скорость двигателя 2 сигнальных проводов для открытого.

| **Условия: ** Откройте окно интерфейса клиента. Отключите сигнальные провода 1 и 2 на блоке SDU410. Отключите разъем C4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте скорость 1 и 2 сигнала двигателя на блоке SDU410 и разъеме C4 для открытого доступа. Поместите один испытательный щуп на провод сигнала 1 скорости двигателя в блок SDU410. Поместите другой испытательный щуп со скоростью 1 сигнала контакта на разъем С4. Поместите один испытательный щуп на сигнальный провод 2 оборота двигателя в блок SDU410. Поместите другой испытательный щуп со скоростью 2 сигнала контакта на разъем С4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 1D |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1D. Проверьте скорость 1 двигателя и скорость 2 двигателя на обратные провода для открытого.

| **Условия: ** Откройте окно интерфейса клиента. Отсоедините обороты двигателя 1 и обороты двигателя 2 обратной проводов на блоке SDU410. Отключите разъем C4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте скорость 1 и скорость 2 возврата проводов в блоке SDU410 и разъеме C4 для открытого доступа. Поместите один испытательный щуп на обратный провод двигателя 1 на блоке SDU410. Поместите другой испытательный щуп на обратный контакт скорости двигателя 1 на разъеме C4. Поместите один испытательный щуп на обратный провод 2 оборота двигателя в блок SDU410. Поместите другой испытательный щуп на обратный контакт с двигателем 2 на разъеме C4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 1Е |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1E. Проверьте стартовый реле переключатель сигнала провода для открытого.

| **Условия: ** Откройте окно интерфейса клиента. Отключите провод сигнала реле стартера в блоке DCU410. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте провод сигнала реле-ретранслятора стартера на блоке DCU410 и разъеме C1 для открытого. Поместите один испытательный щуп на провод сигнала реле стартера в блок DCU410. Поместите другой испытательный щуп на контакт сигнала стартового реле переключателя в разъем С1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 1F |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1F. Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для открытого доступа.

| **Условия: ** Откройте окно интерфейса клиента. Отключите блок отключения питания и возврата шины связи ModiconTM на блоке DCU410 и блоке SDU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте блок отключения питания и возврата шин связи ModiconTM на блоке DCU410 и блоке SDU410 для открытого доступа. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM в блок DCU410. Поместите другой испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM в блок DCU410. Поместите другой испытательный щуп на отключаемый модуль обратного провода шины связи ModiconTM на блок SDU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 1G |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1G. Проверьте скорость двигателя 1 и скорость двигателя 2 сигнал и возврат проводов для провода к проводу короткий.

| **Условия: ** Откройте окно интерфейса клиента. Отключите сигнальные и обратные провода 1 и 2 оборотов двигателя на блоке DCU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте скорость двигателя 1 и скорость двигателя 2 сигнала и обратные линии на блоке DCU410 для короткого провода к проводу. Поместите один испытательный щуп на сигнальный провод 1 оборота двигателя в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на сигнальный провод 2 оборота двигателя в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на обратный провод двигателя 1 в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на обратный провод 2 оборота двигателя в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 1 ч. |  |

#### ШАГ 1H. Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для короткого провода к проводу.

| **Условия: ** Откройте окно интерфейса клиента. Отключите блок отключения питания шины связи ModiconTM и провода возврата в блоке DCU410. Отключите блок отключения питания шины связи ModiconTM и провода возврата на блоке SDU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте блок отключения питания и возврата шин связи ModiconTM на блоке DCU410 и блоке SDU410 для короткого провода к проводу. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. Заменить SDU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 1II |  |

#### ШАГ 1I. Проверьте скорость двигателя 1 и скорость двигателя 2 сигнальных проводов для короткого наземного.

| **Условия: ** Откройте окно интерфейса клиента. Отсоедините сигнальные провода 1 и 2 от блока DCU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте скорость двигателя 1 и скорость двигателя 2 сигнальных проводов в блоке DCU410 для короткого наземного движения. Поместите один испытательный щуп на сигнальный провод 1 оборота двигателя в блок DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на сигнальный провод 2 оборота двигателя в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 1J |  |

#### ШАГ 1J. Проверьте блок отключения провода питания коммуникационной шины ModiconTM для короткого заземления.

| **Условия: ** Откройте окно интерфейса клиента. Отключите отключающий блок провода питания коммуникационной шины ModiconTM от блока DCU410. Отключите отключение отключения блока питания шины связи ModiconTM от блока SDU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте отключаемый блок питания коммуникационной шины ModiconTM на блоке DCU410 и блоке SDU410 для короткой посадки. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM в блок DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. Заменить SDU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов изготовителя машины.

#### ШАГ 2A. Проверьте сигнал переключателя реле стартера и верните провода для открытого.

| **Условия: ** Откройте окно интерфейса клиента. Отключите разъем C1. Отключите сигнал переключателя реле стартера и возвращайте провода в конце замыкания колец стартера. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнал переключателя реле стартера и провода возврата на разъеме C1 для открытого. Поместите один испытательный щуп на контакт сигнала стартового реле переключателя в разъем С1. Поместите другой испытательный щуп на провод сигнала переключателя стартового реле в пусковой двигательный кольцевой терминал. Поместите один испытательный щуп на стартовый реле реле обратного контакта на разъеме С1. Поместите другой испытательный щуп на провод возврата реле стартера в пусковой кольцевой терминал. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2B. Проверьте сигнал переключателя реле стартера и возвращайте провода для короткого провода к проводу.

| **Условия: ** Откройте окно интерфейса клиента. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнал переключателя реле стартера и возвращайте провода на разъеме C1 для короткого провода к проводу. Поместите один испытательный щуп на контакт сигнала стартового реле переключателя в разъем С1. Поместите другой испытательный щуп на все другие штифты на разъеме C1. Поместите один испытательный щуп на стартовый реле реле обратного контакта на разъеме С1. Поместите другой испытательный щуп на все другие штифты на разъеме C1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Ремонт: ** Заменить провод или разъем. См. процедуру 015-023 (Customer Interface Box) в разделе 15 для замены провода. Свяжитесь с авторизованным местом ремонта Cummins® для замены разъема. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте стартовый реле переключатель сигнала провода для короткого на землю.

| **Условия: ** Откройте окно интерфейса клиента. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте стартовый релейный сигнальный провод на разъеме C1 для короткого заземления. Поместите один испытательный щуп на провод сигнала стартового реле переключателя в разъем С1. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Ремонт: ** Заменить провод или разъем. См. процедуру 015-023 (Customer Interface Box) в разделе 15 для замены провода. Свяжитесь с авторизованным местом ремонта Cummins® для замены разъема. | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить блок DCU410. Свяжитесь с авторизованным местом ремонта Cummins® для замены разъема. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Starter does **not** disengage after engine cranking and the keyswitch is in the ON position.
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
> | STEP 1. | Check the customer interface box. |  |
> |  | **STEP 1A.** Check the customer interface box logic unit LED illumination. |  |
> |  | **STEP 1B.** Check the DCU410 power supply wire for voltage +24-VDC. |  |
> |  | **STEP 1C.** Check the engine speed 1 and engine speed 2 signal wires for an open. |  |
> |  | **STEP 1D.** Check the engine speed 1 and engine speed 2 return wires for an open. |  |
> |  | **STEP 1E.** Check the starter relay switch signal wire for an open. |  |
> |  | **STEP 1F.** Check the shutdown unit Modicon™ communication bus supply and return wires for an open. |  |
> |  | **STEP 1G.** Check the engine speed 1 and engine speed 2 signal and return wires for a wire-to-wire short. |  |
> |  | **STEP 1H.** Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. |  |
> |  | **STEP 1I.** Check the engine speed 1 and engine speed 2 signal wires for a short to ground. |  |
> |  | **STEP 1J.** Check the shutdown unit Modicon™ communication bus supply wire for a short to ground. |  |
> | STEP 2. | Check the OEM wiring harness. |  |
> |  | **STEP 2A.** Check the starter relay switch signal and return wires for an open. |  |
> |  | **STEP 2B.** Check the starter relay switch signal and return wires for a wire-to-wire short. |  |
> |  | **STEP 2C.** Check the starter relay switch signal wire for a short to ground. |  |
>
> ### STEP 1. Check the customer interface box.
>
> #### STEP 1A. Check the customer interface box logic unit LED illumination.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the crank lamp LED on the DCU 410 unit or remote panel for illumination. | Crank lamp illuminated? **YES** | 1B |
> | Crank lamp illuminated? **NO** | Contact a Cummins® Authorized Repair Location |  |
>
> #### STEP 1B. Check the DCU410 power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 1C |  |
>
> #### STEP 1C. Check the engine speed 1 and engine speed 2 signal wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 1 and engine speed 2 signal wires at the SDU410 unit. Disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine speed 1 and engine 2 signal wires at the SDU410 unit and C4 connector for an open. Place one test lead on the engine speed 1 signal wire at the SDU410 unit. Place the other test lead engine speed 1 signal pin at the C4 connector. Place one test lead on the engine speed 2 signal wire at the SDU410 unit. Place the other test lead engine speed 2 signal pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1D. Check the engine speed 1 and engine speed 2 return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 1 and engine speed 2 return wires at the SDU410 unit. Disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine speed 1 and engine speed 2 return wires at the SDU410 unit and C4 connector for an open. Place one test lead on the engine speed 1 return wire at the SDU410 unit. Place the other test lead on the engine speed 1 return pin at the C4 connector. Place one test lead on the engine speed 2 return wire at the SDU410 unit. Place the other test lead on the engine speed 2 return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1E |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1E. Check the starter relay switch signal wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the starter relay switch signal wire at the DCU410 unit. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter relay switch signal wire at the DCU410 unit and C1 connector for an open. Place one test lead on the starter relay switch signal wire at the DCU410 unit. Place the other test lead on the starter relay switch signal pin at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1F |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1F. Check the shutdown unit Modicon™ communication bus supply and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the DCU410 unit and SDU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication bus supply and return wires at the DCU410 unit and the SDU410 unit for an open. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1G |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1G. Check the engine speed 1 and engine speed 2 signal and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 1 and engine speed 2 signal and return wires at the DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine speed 1 and engine speed 2 signal and return lines at the DCU410 unit for a wire-to-wire short. Place one test lead on the engine speed 1 signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the engine speed 2 signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the engine speed 1 return wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the engine speed 2 return wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 1H |  |
>
> #### STEP 1H. Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the DCU410 unit. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the SDU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication bus supply and return wires at the DCU410 unit and SDU410 unit for a wire-to-wire short. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 1I |  |
>
> #### STEP 1I. Check the engine speed 1 and engine speed 2 signal wires for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine speed 1 and engine speed 2 signal wires from the DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine speed 1 and engine speed 2 signal wires at the DCU410 unit for a short to ground. Place one test lead on the engine speed 1 signal wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the engine speed 2 signal wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 1J |  |
>
> #### STEP 1J. Check the shutdown unit Modicon™ communication bus supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply wire from the DCU410 unit. Disconnect the shutdown unit Modicon™ communication bus supply wire from the SDU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit and SDU410 unit for a short to ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM wiring harness.
>
> #### STEP 2A. Check the starter relay switch signal and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the C1 connector. Disconnect the starter relay switch signal and return wires at the starter motor ring terminal. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter relay switch signal and return wires at the C1 connector for an open. Place one test lead on the starter relay switch signal pin at the C1 connector. Place the other test lead on the starter relay switch signal wire at the starting motor ring terminal. Place one test lead on the starter relay switch return pin at the C1 connector. Place the other test lead on the starter relay switch return wire at the starting motor ring terminal. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2B. Check the starter relay switch signal and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter relay switch signal and return wires at the C1 connector for a wire-to-wire short. Place one test lead on the starter relay switch signal pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Place one test lead on the starter relay switch return pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire or connector. Refer to Procedure 015-023 (Customer Interface Box) in Section 15 to replace the wire. Contact a Cummins® Authorized Repair Location to replace the connector. | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the starter relay switch signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter relay switch signal wire at the C1 connector for a short to ground. Place one test lead on the starter relay switch signal wire at the C1 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire or connector. Refer to Procedure 015-023 (Customer Interface Box) in Section 15 to replace the wire. Contact a Cummins® Authorized Repair Location to replace the connector. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location to replace the connector. | Repair complete |  |
