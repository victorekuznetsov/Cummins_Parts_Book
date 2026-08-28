---
aliases:
  - "Система не запускается после останова"
type: "Процедура"
doc: "116-t02-1019"
title_en: "System Will Not Start After Shutdown"
title_ru: "Система не запускается после останова"
modified: "2008-05-29"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# System Will Not Start After Shutdown
**Система не запускается после останова**

> [!abstract] Процедура · `116-t02-1019`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1019.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Устройство SDU410 предотвращает запуск двигателя после отключения двигателя.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Примечание: Прыгун **должен быть на месте на датчике прелюбрикации, если прелюбрикация** не используется.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента. |  |
|  | **STEP 1A.** Проверьте логическую блокировку светодиодного освещения в интерфейсе клиента. |  |
|  | **STEP 1B.** Проверьте провод питания DCU410 на напряжение +24-VDC. |  |
|  | **STEP 1C.** Проверьте провод дистанционного пускового питания на наличие открытого. |  |
|  | **STEP 1D.** Проверьте провод сигнала реле-ретранслятора стартера на наличие открытого. |  |
|  | **STEP 1E.** Проверить провод сигнала прелюбрикационной активации на наличие открытого сигнала. |  |
|  | **STEP 1F.** Проверить наличие провода сигнала для открытого сигнала. |  |
|  | **STEP 1G.** Проверьте провод дистанционного пускового питания на короткое время. |  |
|  | **STEP 1H.** Проверьте сигнальный провод реле стартера на короткое расстояние от провода к проводу. |  |
|  | **STEP 1I.** Проверить сигнал прелюбрикационной активации на короткое расстояние от провода к проводу. |  |
|  | **STEP 1J.** Проверить полный сигнальный провод на короткое расстояние от провода к проводу. |  |
|  | **STEP 1K.** Проверьте провод дистанционного пускового питания на короткое время до земли. |  |
|  | **STEP 1L.** Проверить сигнал прелюбрикационной активации на короткое время до заземления. |  |
|  | **STEP 1M.** Проверить прелюбрикационный полный сигнальный провод на короткое время до заземления. |  |
| ШАГ 2. | Проверьте жгут проводов изготовителя машины. |  |
|  | **STEP 2A.** Проверьте сигнал переключателя реле стартера и провода возврата для открытого. |  |
|  | **STEP 2B.** Проверьте сигнал переключателя реле стартера и провода возврата для короткого провода к проводу. |  |
|  | **STEP 2C.** Проверить сигнальный провод стартового реле-переключателя на короткое время до заземления. |  |
|  | **STEP 2D.** Проверьте наличие проводов для подачи и возврата смазки на наличие открытого. |  |
|  | **ШАГ 2Е.** Проверьте предсмазочные подводящие и возвратные провода на короткое расстояние от провода к проводу. |  |
|  | **STEP 2F.** Проверьте проволоку подачи смазки на короткое время до заземления. |  |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте логическое устройство клиентского интерфейса LED подсветка.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте лампу с коленчатым приводом на блоке DCU 410 или удаленной панели для освещения. | Светильник с кривошипом? *Да | 1В |
| Светильник с кривошипом? **НЕТ** | Свяжитесь с авторизованным местом ремонта Cummins® |  |

#### ШАГ 1B. Проверьте провод питания DCU410 на напряжение +24-VDC.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Проведите один тест на питающем проводе с напряжением батареи 1 (переключенной мощностью) в блоке DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? *** Ремонт:** Проверить аккумуляторы. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте провод дистанционного запуска для открытия.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод дистанционного пускового питания от блока DCU410 и соединения X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания дистанционного запуска на блоке DCU410 и подключение X4 для открытого доступа. Поместите один испытательный щуп на провод дистанционного пускового питания в блок DCU410. Поместите другой испытательный щуп на провод дистанционного пускового питания в соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1D |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1D. Проверьте стартовый реле переключатель сигнала провода для открытого.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод сигнала реле стартера в блоке DCU410. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод сигнала реле-ретранслятора стартера на блоке DCU410 и разъеме C1 для открытого. Поместите один испытательный щуп на провод сигнала реле стартера в блок DCU410. Поместите другой испытательный щуп на провод сигнала стартового реле переключателя в разъем С1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1Е |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1E. Проверьте провод сигнала прелюбрикационной активации на наличие открытого.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините провод сигнала прелюбрикационной активации от блока DCU410. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод сигнала прелюбрикационной активации на блоке DCU410 и разъеме C1 для открытого соединения. Поместите один испытательный щуп на провод сигнала прелюбрикационной активации в блок DCU410. Поместите другой контакт сигнала активации предварительной смазки на разъем C1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1F |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1F. Проверьте прелюбрикационный полный сигнальный провод на наличие открытого.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините провод с прелюбрикацией полного сигнала на блоке DCU410. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте полную смазку сигнального провода на блоке DCU410 и разъеме C1 для открытого. Поместите один испытательный щуп на предсмазочный полный сигнальный провод в блок DCU410. Поместите другой испытательный щуп на провод с прелюбрикацией полного сигнала на разъеме C1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1G |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1G. Проверьте провод дистанционного запуска для короткого провода.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод питания дистанционного запуска на блоке DCU410 и подключение X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте источник питания дистанционного запуска на блоке DCU410 для короткого провода к проводу. Поместите один испытательный щуп на провод дистанционного пускового питания в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на провод дистанционного пускового питания на разъеме X4. Поместите другой испытательный щуп на все другие провода в разъем X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1 ч. |  |

#### ШАГ 1H. Проверьте сигнальный провод переключателя реле стартера для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод сигнала реле стартера в блоке DCU410. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод сигнала реле-ретранслятора стартера на блоке DCU410 и разъеме C1 для короткого провода к проводу. Поместите один испытательный щуп на провод сигнала реле стартера в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на контакт сигнала стартового реле переключателя в разъем С1. Поместите другой испытательный щуп на все другие штифты на разъеме C1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. Заменить SDU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1II |  |

#### ШАГ 1I. Проверьте сигнал прелюбрикации для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините провод сигнала прелюбрикационной активации на блоке DCU410. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод сигнала прелюбрикационной активации на блоке DCU410 и разъеме C1 для короткого провода к проводу. Поместите один испытательный щуп на провод сигнала прелюбрикационной активации в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на контакт сигнала прелюбрикационной активации на разъеме С1. Поместите другой испытательный щуп на все другие штифты на разъеме C1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1J |  |

#### ШАГ 1J. Проверьте прелюбрикационный полный сигнальный провод для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините провод с прелюбрикацией полного сигнала на блоке DCU410. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте полный сигнальный провод прелюбрики на блоке DCU410 и разъеме C1 для короткого провода к проводу. Поместите один испытательный щуп на предсмазочный полный сигнальный провод в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на прелюбрикационный полный контакт сигнала на разъеме С1. Поместите другой испытательный щуп на все другие штифты на разъеме C1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1кг |  |

#### ШАГ 1K. Проверьте провод дистанционного пуска для короткого приземления.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод дистанционного пускового питания на блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод дистанционного пуска на блоке DCU410 и подключение X4 для короткого заземления. Поместите один испытательный щуп на провод дистанционного пускового питания в блок DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на провод дистанционного пускового питания в соединение X4. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1 л |  |

#### ШАГ 1L. Проверьте сигнал прелюбрикационной активации на короткое время до земли.

| **Условия:** Откройте окно интерфейса клиента. Отключите прелюбрикационную активацию и полные сигнальные провода на блоке DCU410. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить провод сигнала прелюбрикационной активации на блоке DCU410 и разъеме C1 для короткого отключения. Поместите один испытательный щуп на провод сигнала прелюбрикационной активации в блок DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на контакт сигнала прелюбрикационной активации на разъеме С1. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. Заменить SDU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1 мкм |  |

#### ШАГ 1M. Проверьте прелюбрикационный полный сигнальный провод на короткое время до земли.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините провод с прелюбрикацией полного сигнала на блоке DCU410. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте полную смазку сигнального провода на блоке DCU410 и разъеме C1 для короткого заземления. Поместите один испытательный щуп на предсмазочный полный сигнальный провод в блок DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на прелюбрикационный полный контакт сигнала на разъеме С1. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. Заменить SDU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов изготовителя машины.

#### ШАГ 2A. Проверьте сигнал переключателя реле стартера и верните провода для открытого.

| **Условия:** Отключите сигнал переключателя реле стартера и провода возврата в пусковых клеммах колец двигателя. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал переключателя реле стартера и провода возврата на разъеме C1 для открытого. Поместите один испытательный щуп на контакт сигнала стартового реле переключателя в разъем С1. Поместите другой испытательный щуп на провод сигнала переключателя стартового реле в пусковой двигательный кольцевой терминал. Поместите один испытательный щуп на стартовый реле реле обратного контакта на разъеме С1. Поместите другой испытательный щуп на провод возврата реле стартера в пусковой кольцевой терминал. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 2B. Проверьте сигнал переключателя реле стартера и возвращайте провода для короткого провода к проводу.

| **Условия:** Отключить разъем С1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал переключателя реле стартера и возвращайте провода на разъеме C1 для короткого провода к проводу. Поместите один испытательный щуп на контакт сигнала стартового реле переключателя в разъем С1. Поместите другой испытательный щуп на все другие штифты на разъеме C1. Поместите один испытательный щуп на стартовый реле реле обратного контакта на разъеме С1. Поместите другой испытательный щуп на все другие штифты на разъеме C1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Ремонт:** Заменить провод или разъем. См. процедуру 015-023 (Customer Interface Box) в разделе 15 для замены провода. Свяжитесь с авторизованным местом ремонта Cummins® для замены разъема. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте стартовый реле переключатель сигнала провода для короткого на землю.

| **Условия:** Откройте окно интерфейса клиента. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте стартовый релейный сигнальный провод на разъеме C1 для короткого заземления. Поместите один испытательный щуп на контакт сигнала стартового реле переключателя в разъем С1. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Ремонт:** Заменить провод или разъем. См. процедуру 015-023 (Customer Interface Box) в разделе 15 для замены провода. Свяжитесь с авторизованным местом ремонта Cummins® для замены разъема. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте прелюбрикационные подводящие и возвращающие провода для открытого.

| **Условия:** Отключить разъем С1. Отключите прелюбрикационный датчик. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте прелюбрикационные подводящие и возвращающие провода для открытого. Поместите один испытательный щуп на контакт подачи прелюбрикации на разъеме C1. Поместите другой испытательный щуп на контакт подачи прелюбрикации на разъем датчика прелюбрики. Поместите один испытательный щуп на обратный контакт прелюбрикации на разъеме C1. Поместите другой испытательный щуп на обратный контакт прелюбрикации на разъем датчика прелюбрики. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2Е |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 2E. Проверьте прелюбрикационные подводящие и возвращающие провода для короткого провода к проводу.

| **Условия:** Отключить разъем С1. Отключите прелюбрикационный датчик. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте прелюбрикационные подводящие и возвращающие провода для короткого провода к проводу. Поместите один испытательный щуп на контакт подачи прелюбрикации на разъеме C1. Поместите другой испытательный щуп на все другие штифты на разъеме C1. Поместите один испытательный щуп на обратный контакт прелюбрикации на разъеме C1. Поместите другой испытательный щуп на все другие штифты на разъеме C1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2F |  |

#### ШАГ 2F. Проверьте провод подачи прелюбрикации на короткий срок до земли.

| **Условия:** Отключить разъем С1. Отключите прелюбрикационный датчик. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод подачи прелюбрикации на короткий срок до земли. Поместите один испытательный щуп на контакт подачи прелюбрикации на разъеме C1. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить прелюбрикационный датчик. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The SDU410 unit is preventing the engine from starting after engine shutdown.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> NOTE: A jumper **must** be in place at the prelubrication sensor, if prelubrication is **not** used.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box. |  |
> |  | **STEP 1A.** Check the customer interface box logic unit LED illumination. |  |
> |  | **STEP 1B.** Check the DCU410 power supply wire for voltage +24-VDC. |  |
> |  | **STEP 1C.** Check the remote start supply wire for an open. |  |
> |  | **STEP 1D.** Check the starter relay switch signal wire for an open. |  |
> |  | **STEP 1E.** Check the prelubrication activation signal wire for an open. |  |
> |  | **STEP 1F.** Check the prelubrication complete signal wire for an open. |  |
> |  | **STEP 1G.** Check the remote start supply wire for a wire-to-wire short. |  |
> |  | **STEP 1H.** Check the starter relay switch signal wire for a wire-to-wire short. |  |
> |  | **STEP 1I.** Check the prelubrication activation signal wire for a wire-to-wire short. |  |
> |  | **STEP 1J.** Check the prelubrication complete signal wire for a wire-to-wire short. |  |
> |  | **STEP 1K.** Check the remote start supply wire for a short to ground. |  |
> |  | **STEP 1L.** Check the prelubrication activation signal wire for a short to ground. |  |
> |  | **STEP 1M.** Check the prelubrication complete signal wire for a short to ground. |  |
> | STEP 2. | Check the OEM wiring harness. |  |
> |  | **STEP 2A.** Check the starter relay switch signal and return wires for an open. |  |
> |  | **STEP 2B.** Check the starter relay switch signal and return wires for a wire-to-wire short. |  |
> |  | **STEP 2C.** Check the starter relay switch signal wire for a short to ground. |  |
> |  | **STEP 2D.** Check the prelubrication supply and return wires for an open. |  |
> |  | **STEP 2E.** Check the prelubrication supply and return wires for a wire-to-wire short. |  |
> |  | **STEP 2F.** Check the prelubrication supply wire for a short to ground. |  |
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
> | Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 1C |  |
>
> #### STEP 1C. Check the remote start supply wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the remote start supply wire from the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote start supply wire at the DCU410 unit and X4 connection for an open. Place one test lead on the remote start supply wire at the DCU410 unit. Place the other test lead on the remote start supply wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1D. Check the starter relay switch signal wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the starter relay switch signal wire at the DCU410 unit. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter relay switch signal wire at the DCU410 unit and C1 connector for an open. Place one test lead on the starter relay switch signal wire at the DCU410 unit. Place the other test lead on the starter relay switch signal wire at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1E |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1E. Check the prelubrication activation signal wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the prelubrication activation signal wire from the DCU410 unit. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication activation signal wire at the DCU410 unit and C1 connector for an open. Place one test lead on the prelubrication activation signal wire at the DCU410 unit. Place the other test lead prelubrication activation signal pin at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1F |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1F. Check the prelubrication complete signal wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the prelubrication complete signal wire at the DCU410 unit. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication complete signal wire at the DCU410 unit and C1 connector for an open. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on the prelubrication complete signal wire at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1G |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1G. Check the remote start supply wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the remote start supply wire at the DCU410 unit and the X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote start supply at the DCU410 unit for a wire-to-wire short. Place one test lead on the remote start supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the remote start supply wire at the X4 connector. Place the other test lead on all other wires at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 1H |  |
>
> #### STEP 1H. Check the starter relay switch signal wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the starter relay switch signal wire at the DCU410 unit. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter relay switch signal wire at the DCU410 unit and C1 connector for a wire-to-wire short. Place one test lead on the starter relay switch signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the starter relay switch signal pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 1I |  |
>
> #### STEP 1I. Check the prelubrication activation signal wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the prelubrication activation signal wire at the DCU410 unit. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication activation signal wire at the DCU410 unit and C1 connector for a wire-to-wire short. Place one test lead on the prelubrication activation signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the prelubrication activation signal pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 1J |  |
>
> #### STEP 1J. Check the prelubrication complete signal wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the prelubrication complete signal wire at the DCU410 unit. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication complete signal wire at the DCU410 unit and C1 connector for a wire-to-wire short. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the prelubrication complete signal pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 1K |  |
>
> #### STEP 1K. Check the remote start supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the remote start supply wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote start supply wire at the DCU410 unit and X4 connection for a short to ground. Place one test lead on the remote start supply wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the remote start supply wire at the X4 connection. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 1L |  |
>
> #### STEP 1L. Check the prelubrication activation signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the prelubrication activation and complete signal wires at the DCU410 unit. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication activation signal wire at the DCU410 unit and C1 connector for a short to ground. Place one test lead on the prelubrication activation signal wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the prelubrication activation signal pin at the C1 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 1M |  |
>
> #### STEP 1M. Check the prelubrication complete signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the prelubrication complete signal wire at the DCU410 unit. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication complete signal wire at the DCU410 unit and C1 connector for a short to ground. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the prelubrication complete signal pin at the C1 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM wiring harness.
>
> #### STEP 2A. Check the starter relay switch signal and return wires for an open.
>
> | **Conditions:** Disconnect the starter relay switch signal and return wires at the starting motor ring terminals. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter relay switch signal and return wires at the C1 connector for an open. Place one test lead on the starter relay switch signal pin at the C1 connector. Place the other test lead on the starter relay switch signal wire at the starting motor ring terminal. Place one test lead on the starter relay switch return pin at the C1 connector. Place the other test lead on the starter relay switch return wire at the starting motor ring terminal. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 2B. Check the starter relay switch signal and return wires for a wire-to-wire short.
>
> | **Conditions:** Disconnect the C1 connector. |  |  |
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
> | Check the starter relay switch signal wire at the C1 connector for a short to ground. Place one test lead on the starter relay switch signal pin at the C1 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire or connector. Refer to Procedure 015-023 (Customer Interface Box) in Section 15 to replace the wire. Contact a Cummins® Authorized Repair Location to replace the connector. | Repair complete |
> | Less than 10 ohms? **NO** | 2D |  |
>
> #### STEP 2D. Check the prelubrication supply and return wires for an open.
>
> | **Conditions:** Disconnect the C1 connector. Disconnect the prelubrication sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication supply and return wires for an open. Place one test lead on the prelubrication supply pin at the C1 connector. Place the other test lead on the prelubrication supply pin at the prelubrication sensor connector. Place one test lead on the prelubrication return pin at the C1 connector. Place the other test lead on the prelubrication return pin at the prelubrication sensor connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2E |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 2E. Check the prelubrication supply and return wires for a wire-to-wire short.
>
> | **Conditions:** Disconnect the C1 connector. Disconnect the prelubrication sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication supply and return wires for a wire-to-wire short. Place one test lead on the prelubrication supply pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Place one test lead on the prelubrication return pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2F |  |
>
> #### STEP 2F. Check the prelubrication supply wire for a short to ground.
>
> | **Conditions:** Disconnect the C1 connector. Disconnect the prelubrication sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication supply wire for a short to ground. Place one test lead on the prelubrication supply pin at the C1 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the prelubrication sensor. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |  |
