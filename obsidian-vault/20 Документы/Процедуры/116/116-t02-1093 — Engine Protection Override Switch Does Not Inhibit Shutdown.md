---
aliases:
  - "Выключатель блокировки защиты не отменяет останов"
type: "Процедура"
doc: "116-t02-1093"
title_en: "Engine Protection Override Switch Does Not Inhibit Shutdown"
title_ru: "Выключатель блокировки защиты не отменяет останов"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1093.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1093.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Engine Protection Override Switch Does Not Inhibit Shutdown
**Выключатель блокировки защиты не отменяет останов**

> [!abstract] Процедура · `116-t02-1093`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1093.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1093.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Проверьте, что блок отключения SDU410 перекрывает светодиодные огни, когда переключатель перекрытия отключения активируется на разъеме SDU410.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Входные сигналы SDU410 являются переключателями. Эти переключатели обычно открыты и закрыты для активации отключения.

Попробуйте закрыть выключатель на SDU410. Если двигатель все еще выключается (с переопределением выключения по-прежнему активен), то SDU410 выходит из строя. Ссылка на соответствующее дерево устранения неполадок в разделе ТТ настоящего руководства.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента |  |
|  | **STEP 1A.** Проверьте логическую блокировку светодиодного освещения в интерфейсе клиента. | Активны ли какие-либо сигналы тревоги или светодиоды освещены? |
|  | **STEP 1B.** Проверьте провод электропитания SDU410 на +24-VDC. | Меньше +24-VDC? |
| ШАГ 2. | Проверьте клиентский интерфейс коробки проводов |  |
|  | **STEP 2A.** Проверьте сигнал реле переопределения защиты двигателя и провода возврата для открытого. | Менее 10 Ом? |

### ШАГ 1. Проверьте окно интерфейса клиента

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

### ШАГ 2. Проверьте клиентский интерфейс коробки проводов

#### ШАГ 2A. Проверьте сигнал реле защиты двигателя и возвратные провода для открытого.

| **Условия: **Откройте окно интерфейса клиента Отключите сигнал реле защиты двигателя и провода возврата на блоке SDU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал реле защиты от engne и верните провода для открытого. Поместите один испытательный щуп на провод ретрансляции реле защиты двигателя на блоке SDU410. Поместите другой испытательный щуп на защитный реле реле сигнального провода на реле контакта. Поместите один испытательный щуп на реле реле обратной проволоки защиты двигателя на блоке SDU410. Поместите другой испытательный щуп на реле реле защиты двигателя, перекрывающем реле обратного провода, на реле контакта. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Менее 10 Ом? *Да | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Замените реле. Свяжитесь с авторизованным местом ремонта Cummins® для замены реле клиентского интерфейса. | Свяжитесь с авторизованным местом ремонта Cummins® |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Check the SDU410 unit shutdown override LED lights when shutdown override switch is activated at the SDU410 connector.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The SDU410 input signals are switches. These switches are normally open and closed to activate a shutdown.
>
> Try closing a shutdown switch on the SDU410 unit. If the engine still shuts down (with shutdown override still active), then the SDU410 has malfunctioned. Reference the appropriate troubleshooting tree in Section TT of this manual.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box |  |
> |  | **STEP 1A.** Check the customer interface box logic unit LED illumination. | Are any alarms active or LEDs illuminated? |
> |  | **STEP 1B.** Check the SDU410 power supply wire for +24-VDC. | Less than +24-VDC? |
> | STEP 2. | Check the customer interface box wiring |  |
> |  | **STEP 2A.** Check the engine protection override relay signal and return wires for an open. | Less than 10 ohms? |
>
> ### STEP 1. Check the customer interface box
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
> ### STEP 2. Check the customer interface box wiring
>
> #### STEP 2A. Check the engine protection override relay signal and return wires for an open.
>
> | **Conditions:** Open the customer interface box Disconnect the engine protection override relay signal and return wires at the SDU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engne protection override relay signal and return wires for an open. Place one test lead on the engine protection override relay signal wire at the SDU410 unit. Place the other test lead on the engine protection override relay signal wire at the relay contact. Place one test lead on the engine protection override relay return wire at the SDU410 unit. Place the other test lead on the engine protection override relay return wire at the relay contact. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the relay. Contact a Cummins® Authorized Repair Location for replacement of the customer interface box relay. | Contact a Cummins® Authorized Repair Location |  |
