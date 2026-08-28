---
aliases:
  - "Неверная индикация останова двигателя на блоке останова"
type: "Процедура"
doc: "116-t02-1081"
title_en: "Incorrect Indication of Engine Shut Down at Shutdown Unit"
title_ru: "Неверная индикация останова двигателя на блоке останова"
modified: "2008-03-20"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1081.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1081.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Incorrect Indication of Engine Shut Down at Shutdown Unit
**Неверная индикация останова двигателя на блоке останова**

> [!abstract] Процедура · `116-t02-1081`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-03-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1081.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1081.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Нет связи между блоком SDU410 и блоком DCU410.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Входные сигналы SDU410 являются переключателями. Эти переключатели обычно открыты и закрыты для активации отключения.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте интерфейс клиента |  |
|  | **STEP 1A.** Проверьте логическую блокировку светодиодного освещения в интерфейсе клиента. | Активны ли какие-либо сигналы тревоги или светодиоды освещены? |
|  | **STEP 1B.** Проверьте провод электропитания SDU410 на +24-VDC. | Меньше +24-VDC? |
| ШАГ 2. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 2A.** Проверьте сигнал переопределения защиты двигателя и провода возврата для открытого сигнала. | Менее 10 Ом? |
|  | **STEP 2B.** Проверьте реле переопределения защиты двигателя на наличие открытого. | Менее 10 Ом? |
|  | **STEP 2C.** Проверьте блок отключения питания и возврата коммуникационных шины ModiconTM на наличие открытых проводов | Менее 10 Ом? |

### ШАГ 1. Проверьте интерфейс клиента

#### ШАГ 1A. Проверьте логическое устройство клиентского интерфейса LED подсветка.

| **Условия:** Проверьте устройство DCU410 на наличие сигнализации и светодиодной подсветки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие сигнализации и светодиодной подсветки на устройстве DCU410. | Активны ли какие-либо сигналы тревоги или светодиоды освещены? *Да | Свяжитесь с авторизованным местом ремонта Cummins® |
| Активны ли какие-либо сигналы тревоги или светодиоды освещены? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте провод питания DCU410 для +24-VDC.

| **Условия: **Откройте окно интерфейса клиента |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на блоке отключения питания 24-VDC на блоке SDU410. Поместите один испытательный щуп на блок отключения питания 24-VDC на блоке питания SDU410. Поместите другой испытательный щуп на провод возврата блока отключения в блок SDU410. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Меньше +24-VDC? **Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 2А |  |

### ШАГ 2. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 2A. Проверьте сигнал переопределения защиты двигателя и верните провода для открытого.

| **Условия: **Откройте окно интерфейса клиента Отключите сигнал опровержения защиты двигателя и провода возврата на блоке SDU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал переопределения защиты от двигателя и верните провода для открытого. Поместите один испытательный щуп на сигнальный провод защиты двигателя на блоке SDU410. Поместите другой испытательный щуп на сигнальный провод защиты двигателя в блок DCU410. Поместите один испытательный щуп на обратный провод защиты двигателя на блоке SDU410. Поместите другой испытательный щуп на обратный провод защиты двигателя в блок DCU410. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Менее 10 Ом? *Да | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | 2В |  |

#### ШАГ 2B. Проверьте реле защиты от переопределения двигателя на наличие открытого.

| **Условия: **Откройте окно интерфейса клиента. Отключите сигнал опровержения защиты двигателя и возвращайте провода при контакте реле реле защиты двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте контакты реле защиты двигателя на предмет открытия. Поместите один испытательный щуп на провод ретрансляции реле защиты двигателя на блоке SDU410. Поместите другой испытательный щуп на сигнальный провод защиты двигателя на контакт реле. Поместите один испытательный щуп на обратный провод защиты двигателя на блоке SDU410. Поместите другой испытательный щуп на защитный провод обратной передачи двигателя при контакте реле. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Менее 10 Ом? *Да | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить реле. Заменить SDU410. Свяжитесь с авторизованным местом ремонта Cummins® для замены реле клиентского интерфейса. | 2C |  |

#### ШАГ 2C. Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для открытого доступа.

| **Условия: **Откройте окно интерфейса клиента. Отключите блок отключения питания и возврата шины связи ModiconTM на блоке SDU410 и блоке DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте контакты реле защиты двигателя на предмет открытия. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на блок отключения провода питания шины связи ModiconTM в блок DCU410. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на отключаемый модуль обратного провода шины связи ModiconTM в блок DCU410. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Менее 10 Ом? *Да | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить модуль SDU410. Свяжитесь с авторизованным местом ремонта Cummins® для замены реле клиентского интерфейса. | Свяжитесь с авторизованным местом ремонта Cummins® |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - No communication between the SDU410 unit and DCU410 unit.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The SDU410 input signals are switches. These switches are normally open and closed to activate a shutdown.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check customer interface box |  |
> |  | **STEP 1A.** Check the customer interface box logic unit LED illumination. | Are any alarms active or LEDs illuminated? |
> |  | **STEP 1B.** Check the SDU410 power supply wire for +24-VDC. | Less than +24-VDC? |
> | STEP 2. | Check customer interface box wiring |  |
> |  | **STEP 2A.** Check the engine protection override signal and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 2B.** Check the engine protection override relay for an open. | Less than 10 ohms? |
> |  | **STEP 2C.** Check the shutdown unit Modicon™ communication bus supply and return wires for an open | Less than 10 ohms? |
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
> | Check the voltage at the shutdown unit supply 24-VDC at the SDU410 unit. Place one test lead on the shutdown unit supply 24-VDC supply wire at the SDU410 unit. Place the other test lead on the shutdown unit return wire at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than +24-VDC? **NO** | 2A |  |
>
> ### STEP 2. Check customer interface box wiring
>
> #### STEP 2A. Check the engine protection override signal and return wires for an open.
>
> | **Conditions:** Open the customer interface box Disconnect the engine protection override signal and return wires at the SDU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engne protection override signal and return wires for an open. Place one test lead on the engine protection override signal wire at the SDU410 unit. Place the other test lead on the engine protection override signal wire at the DCU410 unit. Place one test lead on the engine protection override return wire at the SDU410 unit. Place the other test lead on the engine protection override return wire at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | 2B |  |
>
> #### STEP 2B. Check the engine protection override relay for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine protection override signal and return wires at the engine protection override relay contact. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine protection override relay contacts for an open. Place one test lead on the engine protection override relay signal wire at the SDU410 unit. Place the other test lead on the engine protection override signal wire at the relay contact. Place one test lead on the engine protection override return wire at the SDU410 unit. Place the other test lead on the engine protection override return wire at the relay contact. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the relay. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location for replacement of the customer interface box relay. | 2C |  |
>
> #### STEP 2C. Check the shutdown unit Modicon™ communication bus supply and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the SDU410 unit and DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine protection override relay contacts for an open. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location for replacement of the customer interface box relay. | Contact a Cummins® Authorized Repair Location |  |
