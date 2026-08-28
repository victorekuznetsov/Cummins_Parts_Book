---
aliases:
  - "Неисправность драйвера лампы останова по низкому давлению масла (LOP)"
type: "Процедура"
doc: "116-t02-1061"
title_en: "Low Oil Pressure (LOP) Shutdown Lamp Driver Malfunction"
title_ru: "Неисправность драйвера лампы останова по низкому давлению масла (LOP)"
modified: "2007-03-02"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1061.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1061.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Low Oil Pressure (LOP) Shutdown Lamp Driver Malfunction
**Неисправность драйвера лампы останова по низкому давлению масла (LOP)**

> [!abstract] Процедура · `116-t02-1061`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1061.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1061.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Лампа выключения низкого давления (LOP) освещается, когда условие выключения низкого давления (LOP) не существует.

- Лампа выключения низкого давления (LOP) **не** освещается при наличии состояния выключения низкого давления (LOP).

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неисправности водителя лампы с низким давлением масла (LOP). Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 1A.** Проверьте низкое давление масла (LOP) | Менее 10 Ом? |
|  | **STEP 1B.** Проверьте низкое давление масла (LOP) сигнал отключения для провода к проводу | Менее 10 Ом? |
|  | **STEP 1C.** Проверьте низкое давление масла (LOP) на короткое время | Менее 10 Ом? |
| ШАГ 2. | Проверьте электропроводку двигателя на кабель клиентского интерфейса |  |
|  | **STEP 2A.** Проверьте низкое давление масла (LOP) | Менее 10 Ом? |
|  | **STEP 2B.** Проверьте низкое давление масла (LOP) сигнал отключения для провода к проводу | Менее 10 Ом? |

### ШАГ 1. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 1A. Проверьте низкое давление масла (LOP) выключение сигнала провода для открытого доступа

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте низкое давление масла (LOP) выключателя сигнала провода для открытого. Поместите один испытательный щуп на контакт сигнала отключения низкого давления масла (LOP) в разъёме C3. Поместите другой испытательный щуп на сигнальный терминал с низким давлением масла (LOP) на разъем X4. | Менее 10 Ом? *Да | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |  |

#### ШАГ 1B. Проверьте низкое давление масла (LOP) сигнал отключения для провода к проводу короткий

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте низкое давление масла (LOP) выключателя сигнала провода для провода к проводу короткий. Поместите один испытательный щуп на контакт сигнала отключения низкого давления масла (LOP) в разъёме C3. Поместите другой испытательный щуп на каждый из оставшихся терминалов в разъем X4. | Менее 10 Ом? * Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте низкое давление масла (LOP) сигнал отключения для короткой до земли

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте низкое давление масла (LOP) выключателя сигнала провода для короткого на землю. Поместите один испытательный щуп на контакт сигнала отключения низкого давления масла (LOP) в разъёме C3. Поместите другой испытательный щуп на панельную площадку. | Менее 10 Ом? * Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте электропроводку двигателя на кабель клиентского интерфейса

#### ШАГ 2A. Проверьте низкое давление масла (LOP) выключение сигнала провода для открытого доступа

| **Условия:** Отсоединить окно интерфейса клиента к разъёму кабеля C3 с помощью проводов двигателя от окна интерфейса клиента Отключить окно интерфейса клиента к разъёму кабеля C10 с помощью проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте низкое давление масла (LOP) выключателя сигнала провода для открытого. Поместите перемычку между контактом сигнала отключения низкого давления масла (LOP) и общим контактом сигнала отключения в разъеме C10. Поместите один испытательный щуп в контакт сигнала отключения низкого давления масла (LOP) разъема C3. Поместите другой испытательный щуп в общий контакт сигнала отключения разъема C3. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **Заменить кабель.** | Ремонт завершён |  |

#### ШАГ 2B. Проверьте низкое давление масла (LOP) сигнал отключения для провода к проводу короткий

| **Условия:** Отсоединить окно интерфейса клиента к разъёму кабеля C3 с помощью проводов двигателя от коробки интерфейса клиента Отключить окно интерфейса клиента к проводах кабеля C10 от жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте низкое давление масла (LOP) выключателя сигнала провода для провода к проводу короткий. Поместите один испытательный щуп на контакт сигнала отключения низкого давления масла (LOP) в разъёме C3. Поместите другой испытательный щуп на каждый из оставшихся штифтов в разъеме C3. | Менее 10 Ом? * Заменить кабель. | Ремонт завершён |
| Менее 10 Ом? **NORepair:** См. раздел TF в руководстве по устранению неполадок и ремонту, электронной системе управления, двигателях серий модульных систем общего пользования QSK19 CM850, в бюллетене 4021493 или руководстве по устранению неполадок и ремонту, электронной системе управления, QSK38, QSK50 и QSK60, двигателях серий модульных систем общего пользования CM850, в бюллетене 4021533 или обратитесь к руководству по обслуживанию OEM. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The low pressure (LOP) shutdown lamp is illuminated when a low pressure (LOP) shutdown condition does **not** exist.
>
> - The low pressure (LOP) shutdown lamp is **not** illuminated when a low pressure (LOP) shutdown condition exists.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a low oil pressure (LOP) shutdown lamp driver malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box Wiring |  |
> |  | **STEP 1A.** Check Low Oil Pressure (LOP) Shutdown Signal Wire for Open | Less than 10 ohms? |
> |  | **STEP 1B.** Check Low Oil Pressure (LOP) Shutdown Signal Wire for Wire to Wire Short | Less than 10 ohms? |
> |  | **STEP 1C.** Check Low Oil Pressure (LOP) Shutdown Signal Wire for Short to Ground | Less than 10 ohms? |
> | STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
> |  | **STEP 2A.** Check Low Oil Pressure (LOP) Shutdown Signal Wire for Open | Less than 10 ohms? |
> |  | **STEP 2B.** Check Low Oil Pressure (LOP) Shutdown Signal Wire for Wire to Wire Short | Less than 10 ohms? |
>
> ### STEP 1. Check Customer Interface Box Wiring
>
> #### STEP 1A. Check Low Oil Pressure (LOP) Shutdown Signal Wire for Open
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the low oil pressure (LOP) shutdown signal wire for an open. Place one test lead on the low oil pressure (LOP) shutdown signal pin in connector C3. Place the other test lead on low oil pressure (LOP) shutdown signal terminal on the X4 connector. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |  |
>
> #### STEP 1B. Check Low Oil Pressure (LOP) Shutdown Signal Wire for Wire to Wire Short
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the low oil presssure (LOP) shutdown signal wire for wire to wire short. Place one test lead on the low oil pressure (LOP) shutdown signal pin in connector C3. Place the other test lead on each of the remaining terminals in X4 connector. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check Low Oil Pressure (LOP) Shutdown Signal Wire for Short to Ground
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the low oil pressure (LOP) shutdown signal wire for short to ground. Place one test lead on the low oil pressure (LOP) shutdown signal pin in connector C3. Place the other test lead on panel ground. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check Engine Harness to Customer Interface Box Cable
>
> #### STEP 2A. Check Low Oil Pressure (LOP) Shutdown Signal Wire for Open
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box Disconnect customer interface box to engine harness cable connector C10 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the low oil presssure (LOP) shutdown signal wire for an open. Place a jumper between the low oil pressure (LOP) shutdown signal pin and the common shutdown signal pin in the C10 connector. Place one test lead in the low oil pressure (LOP) shutdown signal pin of the C3 connector. Place the other test lead in the common shutdown signal pin of the C3 connector. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
>
> #### STEP 2B. Check Low Oil Pressure (LOP) Shutdown Signal Wire for Wire to Wire Short
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box Disconnect customer inteface box to engine harness cable connector C10 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the low oil pressure (LOP) shutdown signal wire for wire to wire short. Place one test lead on the low oil pressure (LOP) shutdown signal pin in connector C3. Place the other test lead on each of the remaining pins in the C3 connector. | Less than 10 ohms? **YESRepair:** Replace the cable. | Repair complete |
> | Less than 10 ohms? **NORepair:** Refer to Section TF in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493, or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60, CM850 Modular Common Rail System Series Engines, Bulletin 4021533 or refer to the OEM service manual. | Repair complete |  |
