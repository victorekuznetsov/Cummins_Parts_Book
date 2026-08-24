---
aliases:
  - "Неисправность драйвера лампы приближения к перегреву"
type: "Процедура"
doc: "116-t02-1058"
title_en: "Pre-High Engine Temperature Lamp Driver Malfunction"
title_ru: "Неисправность драйвера лампы приближения к перегреву"
modified: "2007-03-02"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1058.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1058.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Pre-High Engine Temperature Lamp Driver Malfunction
**Неисправность драйвера лампы приближения к перегреву**

> [!abstract] Процедура · `116-t02-1058`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1058.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1058.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Предупредительная лампа с предвысокой температурой двигателя освещается, когда условие с предвысокой температурой двигателя ** не существует.

- Предупредительная лампа с предвысокой температурой двигателя ** не** освещается при наличии предварительной высокой температуры двигателя.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неисправности водителя лампы при высокой температуре. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 1A.** Проверьте сигнальную проводку с предупредительным сигналом высокой температуры двигателя для открытого доступа | Менее 10 Ом? |
|  | **STEP 1B.** Проверьте сигнальную проводку с предупредительным сигналом высокой температуры двигателя для короткой проводной проводов | Менее 10 Ом? |
|  | **STEP 1C.** Проверьте сигнальную проводку с предупредительным сигналом высокой температуры двигателя для короткой посадки | Менее 10 Ом? |
| ШАГ 2. | Проверьте электропроводку двигателя на кабель клиентского интерфейса |  |
|  | **STEP 2A.** Проверьте сигнальную проводку с предупредительным сигналом высокой температуры двигателя для открытого доступа | Менее 10 Ом? |
|  | **STEP 2B.** Проверьте сигнал предупредительного сигнала высокой температуры двигателя для короткой проводной проводов | Менее 10 Ом? |

### ШАГ 1. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 1A. Проверьте предупредительный сигнал высокой температуры двигателя для открытого доступа

| **Условия: ** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C2 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте провод предупредительного сигнала о высокой температуре двигателя на наличие открытого. Поместите один испытательный щуп на контакт предупредительного сигнала о высокой температуре двигателя в разъёме C2. Поместите другой испытательный щуп на предупредительный сигнал высокой температуры двигателя на разъем X4. | Менее 10 Ом? *Да** | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |  |

#### ШАГ 1B. Проверьте предупредительный сигнал высокой температуры двигателя для провода на провод короткой

| **Условия: ** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C2 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте провод предупредительного сигнала температуры двигателя для провода для короткого провода. Поместите один испытательный щуп на контакт предупредительного сигнала о высокой температуре двигателя в разъёме C2. Поместите другой испытательный щуп на каждый из оставшихся терминалов в разъем X4. | Менее 10 Ом? *** Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте предупредительный сигнал высокой температуры двигателя для короткой посадки

| **Условия: ** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C2 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте провод предупредительного сигнала о высокой температуре двигателя для короткого приземления. Поместите один испытательный щуп на контакт предупредительного сигнала о высокой температуре двигателя в разъёме C2. Поместите другой испытательный щуп на панельную площадку. | Менее 10 Ом? *** Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2А |  |

### ШАГ 2. Проверьте электропроводку двигателя на кабель клиентского интерфейса

#### ШАГ 2A. Проверьте предупредительный сигнал высокой температуры двигателя для открытого доступа

| **Условия:** Отсоединить окно интерфейса клиента к разъёму кабеля C2 с помощью проводов двигателя от окна интерфейса клиента Отключить окно интерфейса клиента к разъёму кабеля C9 с помощью проводов двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте провод предупредительного сигнала о высокой температуре двигателя на наличие открытого. Поместите перемычку между контактом предупредительного сигнала о высокой температуре двигателя и контактом сигнала выключения высокой температуры двигателя (HET) в разъеме C9. Поместите один испытательный щуп в контакт предупредительного сигнала высокой температуры двигателя разъема C2. Поместите другой испытательный щуп в контакт сигнала отключения высокой температуры двигателя (HET) разъема C2. | Менее 10 Ом? *Да** | 2В |
| Менее 10 Ом? **Заменить кабель.** | Ремонт завершён |  |

#### ШАГ 2B. Проверьте предупредительный сигнал высокой температуры двигателя для провода на провод короткой

| **Условия:** Отсоединить окно интерфейса клиента к разъёму кабеля C2 с помощью проводов двигателя от коробки интерфейса клиента Отключить окно интерфейса клиента к проводах кабеля C9 от жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте предупредительный сигнал температуры двигателя для провода для провода короткого. Поместите один испытательный щуп на контакт предупредительного сигнала о высокой температуре двигателя в разъёме C2. Поместите другой испытательный щуп на каждый из оставшихся штифтов в разъеме C2. | Менее 10 Ом? ** Ремонт: ** См. раздел TF в руководстве по устранению неполадок и ремонту, Электронная система управления, двигатели серии модульных общих железнодорожных систем QSK19 CM850, Бюллетень 4021493 или руководство по устранению неполадок и ремонту, Электронная система управления, QSK38, QSK50 и QSK60, двигатели серии модульных общих железнодорожных систем CM850, Бюллетень 4021533 или обратитесь к руководству по обслуживанию OEM. | Ремонт завершён |
| Менее 10 Ом? **Заменить кабель.** | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The pre-high engine temperature warning lamp is illuminated when a pre-high engine temperature condition does **not** exist.
>
> - The pre-high engine temperature warning lamp is **not** illuminated when a pre-high engine temperature condition exists.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a pre-high temperature lamp driver malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box Wiring |  |
> |  | **STEP 1A.** Check Pre-High Engine Temperature Warning Signal Wire for Open | Less than 10 ohms? |
> |  | **STEP 1B.** Check Pre-High Engine Temperature Warning Signal Wire for Wire to Wire Short | Less than 10 ohms? |
> |  | **STEP 1C.** Check Pre-High Engine Temperature Warning Signal Wire for Short to Ground | Less than 10 ohms? |
> | STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
> |  | **STEP 2A.** Check Pre-High Engine Temperature Warning Signal Wire for Open | Less than 10 ohms? |
> |  | **STEP 2B.** Check Pre-High Engine Temperature Warning Signal Wire for Wire to Wire Short | Less than 10 ohms? |
>
> ### STEP 1. Check Customer Interface Box Wiring
>
> #### STEP 1A. Check Pre-High Engine Temperature Warning Signal Wire for Open
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the pre-high engine temperature warning signal wire for an open. Place one test lead on the pre-high engine temperature warning signal pin in connector C2. Place the other test lead on pre-high engine temperature warning signal terminal on the X4 connector. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |  |
>
> #### STEP 1B. Check Pre-High Engine Temperature Warning Signal Wire for Wire to Wire Short
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the pre-high engine temperature warning signal wire for wire to wire short. Place one test lead on the pre-high engine temperature warning signal pin in connector C2. Place the other test lead on each of the remaining terminals in X4 connector. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check Pre-High Engine Temperature Warning Signal Wire for Short to Ground
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the pre-high engine temperature warning signal wire for short to ground. Place one test lead on the pre-high engine temperature warning signal pin in connector C2. Place the other test lead on panel ground. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check Engine Harness to Customer Interface Box Cable
>
> #### STEP 2A. Check Pre-High Engine Temperature Warning Signal Wire for Open
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C2 from the customer interface box Disconnect customer interface box to engine harness cable connector C9 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check pre-high engine temperature warning signal wire for an open. Place a jumper between the pre-high engine temperature warning signal pin and the high engine temperature (HET) shutdown signal pin in the C9 connector. Place one test lead in the pre-high engine temperature warning signal pin of the C2 connector. Place the other test lead in the high engine temperature (HET) shutdown signal pin of the C2 connector. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
>
> #### STEP 2B. Check Pre-High Engine Temperature Warning Signal Wire for Wire to Wire Short
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C2 from the customer interface box Disconnect customer inteface box to engine harness cable connector C9 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check pre-high engine temperature warning signal wire for wire to wire short. Place one test lead on the pre-high engine temperature warning signal pin in connector C2. Place the other test lead on each of the remaining pins in the C2 connector. | Less than 10 ohms? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493, or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60, CM850 Modular Common Rail System Series Engines, Bulletin 4021533 or refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
