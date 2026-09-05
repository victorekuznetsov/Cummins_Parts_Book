---
aliases:
  - "Реле блока останова не индицирует активную неисправность"
type: "Процедура"
doc: "116-t02-1097"
title_en: "Shutdown Unit Relay Does Not Indicate Fault When Fault is Active"
title_ru: "Реле блока останова не индицирует активную неисправность"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1097.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1097.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Shutdown Unit Relay Does Not Indicate Fault When Fault is Active
**Реле блока останова не индицирует активную неисправность**

> [!abstract] Процедура · `116-t02-1097`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1097.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1097.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Схема шины данных CAN неисправна между SDU410 и DCU410.

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
|  | **STEP 2A.** Проверьте цепь коммуникационных шин ModiconTM на предмет открытия. | Менее 10 Ом? |
|  | **STEP 2B.** Проверьте цепь коммуникационных шин ModiconTM на короткое время от провода до провода. | Менее 10 Ом? |
|  | **STEP 2C.** Проверьте цепь коммуникационных шин ModiconTM на короткое время до земли. | Менее 10 Ом? |
|  | **STEP 2D.** Убедитесь, что устройство DCU410 взаимодействует с устройством SDU410. |  |

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

#### ШАГ 2A. Проверьте цепь коммуникационных шин ModiconTM на предмет открытия.

| **Условия: **Откройте окно интерфейса клиента Отключите сигнал и провода возврата на цепи коммуникационных шин блока отключения ModiconTM на терминальных полосах SDU410 и DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь коммуникационных шин ModiconTM на предмет открытия. Поместите один испытательный щуп на блок отключения провода питания коммуникационных шин ModiconTM на терминальной полосе SDU410. Поместите другой испытательный щуп на блок отключения питания коммуникационных шин ModiconTM на терминальной полосе DCU410. Поместите один испытательный щуп на отключающем блоке коммуникационных шины ModiconTM обратного провода на терминальной полосе SDU410. Поместите другой испытательный щуп на отключающем блоке ModiconTM, возвращающемся на терминальной полосе DCU410. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2B. Проверьте цепь коммуникационных шин ModiconTM для короткого провода.

| **Условия: **Откройте окно интерфейса клиента. Отключите сигнал и провода возврата на цепи коммуникационных шин блока отключения ModiconTM на терминальных полосах SDU410 и DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь коммуникационного блока ModiconTM для короткой проводной проводов. Поместите один испытательный щуп на блок отключения провода питания коммуникационных шин ModiconTM на терминальной полосе SDU410. Поместите другой испытательный щуп на все другие штифты на терминальной полосе в SDU410. Поместите один испытательный щуп на блок отключения коммуникационных шины ModiconTM обратного провода на терминальной полосе SDU410. Поместите другой испытательный щуп на все другие штифты на терминальной полосе в SDU410. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте цепь коммуникационных шин ModiconTM для короткого приземления.

| **Условия: **Откройте окно интерфейса клиента. Отключите сигнал и обратный провод на блоке отключения ModiconTM цепи коммуникационных шин на терминальных полосах SDU410 и DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь коммуникационных шин ModiconTM для короткого приземления. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте дисплеи устранения неполадок DCU410.

| **Условия:** |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что блок DCU410 взаимодействует с блоком SDU410. Проверьте DCU410 для правильной настройки. | Общается ли DCU410 с SDU410? *Да | Ремонт завершён |
| Общается ли DCU410 с SDU410? **NORepair:** Проверьте конфигурацию. Обратитесь в авторизованный сервисный центр Cummins®. | Свяжитесь с авторизованным местом ремонта Cummins® |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Data link circuit is malfunctioning between the SDU410 and DCU410 exists.
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
> |  | **STEP 2A.** Check the shutdown unit Modicon™ communication buss circuit for an open. | Less than 10 ohms? |
> |  | **STEP 2B.** Check the shutdown unit Modicon™ communication buss circuit for a wire-to-wire short. | Less than 10 ohms? |
> |  | **STEP 2C.** Check the shutdown unit Modicon™ communication buss circuit for a short to ground. | Less than 10 ohms? |
> |  | **STEP 2D.** Check to make sure the DCU410 unit is communicating with the SDU410 unit. |  |
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
> #### STEP 2A. Check the shutdown unit Modicon™ communication buss circuit for an open.
>
> | **Conditions:** Open the customer interface box Disconnect the signal and return wires at the shutdown unit Modicon™ communication buss circuit at the SDU410 and DCU410 terminal strips. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication buss circuit for an open. Place one test lead on the shutdown unit Modicon™ communication buss supply wire at the SDU410 terminal strip. Place the other test lead on the shutdown unit Modicon™ communication buss supply at the DCU410 terminal strip. Place one test lead on the shutdown unit Modicon™ communication buss return wire at the SDU410 terminal strip. Place the other test lead on the shutdown unit Modicon™ communication buss return at the DCU410 terminal strip. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2B. Check the shutdown unit Modicon™ communication buss circuit for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the signal and return wires at the shutdown unit Modicon™ communication buss circuit at the SDU410 and DCU410 terminal strips. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communicaton buss circuit for a wire-to-wire short. Place one test lead on the shutdown unit Modicon™ communication buss supply wire on the SDU410 terminal strip. Place the other test lead on all other pins on the terminal strip at the SDU410. Place one test lead on the shutdown unit Modicon™ communication buss return wire on the SDU410 terminal strip. Place the other test lead on all other pins on the terminal strip at the SDU410. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the shutdown unit Modicon™ communication buss circuit for short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the signal and return wire at the shutdown unit Modicon™ communication buss circuit at the SDU410 and DCU410 terminal strips. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication buss circuit for a short to ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on panel ground. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2D |  |
>
> #### STEP 2D. Check the DCU410 troubleshooting display.
>
> | **Conditions:** |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check to make sure the DCU410 unit is communicating with the SDU410 unit. Check the DCU410 for correct configuration. | Is the DCU410 communicating with SDU410 unit? **YES** | Repair complete |
> | Is the DCU410 communicating with SDU410 unit? **NORepair:** Check the configuration. Contact a Cummins® Authorized Repair Location. | Contact a Cummins® Authorized Repair Location |  |
