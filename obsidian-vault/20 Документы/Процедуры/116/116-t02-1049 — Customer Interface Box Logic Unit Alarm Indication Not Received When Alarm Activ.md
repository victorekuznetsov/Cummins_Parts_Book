---
aliases:
  - "Нет индикации тревоги от логического блока интерфейсной коробки"
type: "Процедура"
doc: "116-t02-1049"
title_en: "Customer Interface Box Logic Unit Alarm Indication Not Received When Alarm Activated"
title_ru: "Нет индикации тревоги от логического блока интерфейсной коробки"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1049.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1049.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Customer Interface Box Logic Unit Alarm Indication Not Received When Alarm Activated
**Нет индикации тревоги от логического блока интерфейсной коробки**

> [!abstract] Процедура · `116-t02-1049`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1049.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1049.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- При включении сигнализации между блоком DCU410 и блоком CLU не осуществляется связь.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента. |  |
|  | **STEP 1A.** Проверьте дисплей блока DCU410 на наличие неисправностей. |  |
|  | **ШАГ 1А-1.** Проверьте провод электропитания CLU на напряжение +24-VDC. |  |
|  | **STEP 1B.** Проверьте провод сигнала тревоги в логическом блоке клиентского интерфейса на наличие открытого сигнала. |  |
|  | **STEP 1C.** Проверьте логическую логическую единицу интерфейса клиента на коротком проводе. |  |
|  | **STEP 1D.** Проверьте логическую связку логического блока клиента на коротком пути к земле. |  |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте дисплей блока DCU410 на наличие неисправностей.

| **Условия:** Найдите дисплей блока DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей блока DCU410 для указания неисправностей. | DCU410 указывает на неисправность (неисправности)? *Да | 1В |
| DCU410 указывает на неисправность (неисправности)? **НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте провод электропитания CLU на напряжение +24-VDC.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Поместите один испытательный щуп на провод питания напряжения батареи 1 в CLU. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC. **Ремонт:** Проверить аккумуляторы. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Меньше +24-VDC. **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте логическое устройство логического блока клиентского интерфейса на наличие открытого сигнала тревоги.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод сигнала тревоги в блоке DCU410 и CLU. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте логическое устройство логического блока клиентского интерфейса на наличие открытого сигнала тревоги. Поместите один измерительный щуп на провод сигнала логического блока интерфейса клиента в блок DCU410. Поместите другой измерительный щуп на провод сигнала логического блока интерфейса клиента в соединение CLU X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1С |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1C. Проверьте логическое устройство логического блока интерфейса клиента для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте логическое устройство логического блока интерфейса клиента для короткого провода к проводу. Поместите один измерительный щуп на провод логического блока логической связи клиентского интерфейса в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Заменить КЛУ. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1D |  |

#### ШАГ 1D. Проверьте логическое устройство логического блока интерфейса клиента на короткое время до земли.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте логическое устройство логического блока интерфейса клиента на короткое время до земли. Поместите один измерительный щуп на провод логического блока логической связи клиентского интерфейса в блок DCU410. Поместите другой тест на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Заменить КЛУ. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | Обратитесь в авторизованный сервисный центр Cummins®. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - No communication between the DCU410 unit and CLU unit when alarm is activated.
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
> |  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
> |  | **STEP 1A-1.** Check the CLU power supply wire for voltage +24-VDC. |  |
> |  | **STEP 1B.** Check the customer interface box logic unit alarm signal wire for an open. |  |
> |  | **STEP 1C.** Check the customer interface box logic unit alarm signal wire for a wire to wire short. |  |
> |  | **STEP 1D.** Check the customer interface box logic unit alarm signal wire for short to ground. |  |
>
> ### STEP 1. Check the customer interface box.
>
> #### STEP 1A. Check the DCU410 unit display for faults.
>
> | **Conditions:** Locate the DCU410 unit display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 unit display for indication of faults. | DCU410 unit indicates fault(s)? **YES** | 1B |
> | DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |
>
> #### STEP 1A-1. Check the CLU power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test lead on the battery 1 voltage supply wire at the CLU. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC. **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
> | Less than +24-VDC. **NO** | 1B |  |
>
> #### STEP 1B. Check the customer interface box logic unit alarm signal wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the customer interface box logic unit alarm signal wire at the DCU410 unit and CLU. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the customer interface box logic unit alarm signal wire for an open. Place one test lead on the customer interface box logic unit signal wire at the DCU410 unit. Place the other test lead on the customer interface box logic unit signal wire at the CLU X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1C. Check the customer interface box logic unit alarm signal wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the customer interface box logic unit alarm signal wire for a wire-to-wire short. Place one test lead on the customer interface box logic unit alarm signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the CLU. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 1D |  |
>
> #### STEP 1D. Check the customer interface box logic unit alarm signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the customer interface box logic unit alarm signal wire for a short to ground. Place one test lead on the customer interface box logic unit alarm signal wire at the DCU410 unit. Place the other test on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the CLU. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location. |  |
