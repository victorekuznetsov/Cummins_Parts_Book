---
aliases:
  - "Неисправность сигнала промежуточной частоты 2"
type: "Процедура"
doc: "116-t02-1065"
title_en: "Intermediate Speed Control 2 Signal Malfunction"
title_ru: "Неисправность сигнала промежуточной частоты 2"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1065.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1065.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Intermediate Speed Control 2 Signal Malfunction
**Неисправность сигнала промежуточной частоты 2**

> [!abstract] Процедура · `116-t02-1065`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1065.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1065.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Промежуточный сигнал 2 управления скоростью не доступен.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неисправности сигнала управления средней скоростью 2. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 1A.** Проверьте промежуточную систему управления скоростью 2 Switch Signal Wire | Менее 10 Ом? |
|  | **STEP 1B.** Проверьте промежуточную скорость 2 переключатель сигнала Wire для провода короткой проводов | Менее 10 Ом? |
|  | **STEP 1C.** Проверьте промежуточную систему управления скоростью 2 Switch Signal Wire для короткой посадки | Менее 10 Ом? |
| ШАГ 2. | Проверьте электропроводку двигателя на кабель клиентского интерфейса |  |
|  | **STEP 2A.** Проверьте промежуточную систему управления скоростью 2 Switch Signal Wire для открытого доступа | Менее 10 Ом? |

### ШАГ 1. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 1A. Проверить Intermediate Speed Control 2 Switch Signal Wire для открытого доступа

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте промежуточный контроль скорости 2 переключателя сигнала провода для открытого. Поместите один испытательный щуп на промежуточный контроль скорости 2 переключателя сигнала контакта в разъем С3. Поместите другой испытательный щуп на промежуточный сигнальный терминал 2 управления скоростью на разъем X4. | Менее 10 Ом? *Да | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |  |

#### ШАГ 1B. Проверить Intermediate Speed Control 2 Switch Signal Wire для провода

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте промежуточный контроль скорости 2 переключателя сигнала провода для провода на провод короткий. Поместите один испытательный щуп на промежуточный контроль скорости 2 переключателя сигнала контакта в разъем С3. Поместите другой испытательный щуп на каждый из оставшихся терминалов в разъем X4. | Менее 10 Ом?  Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверить промежуточную скорость 2 Switch сигнальную проводку для короткой посадки

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте промежуточный контроль скорости 2 переключателя сигнала провода для короткого на землю. Поместите один испытательный щуп на промежуточный контроль скорости 2 переключателя сигнала контакта в разъем С3. Поместите другой испытательный щуп на панельную площадку. | Менее 10 Ом?  Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте электропроводку двигателя на кабель клиентского интерфейса

#### ШАГ 2A. Проверить Intermediate Speed Control 2 Switch Signal Wire для открытого доступа

| **Условия:** Отсоединить окно интерфейса клиента к разъёму кабеля C3 с помощью проводов двигателя от окна интерфейса клиента Отключить окно интерфейса клиента к разъёму кабеля C10 с помощью проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте промежуточный контроль скорости 2 переключатель сигнала провода. Поместите перемычку между кривой крутящего момента выбора сигнального контакта и промежуточным контролем скорости 2 переключателя сигнального контакта в разъеме C10. Поместите один испытательный щуп в кривую крутящего момента, выберите сигнальный контакт разъема C3. Поместите другой испытательный щуп в промежуточный сигнал управления скоростью 2 переключателя контакта разъема C3. | Менее 10 Ом? **Ремонт:** См. раздел TF в руководстве по устранению неполадок и ремонту, QSK19 CM850 Модульные двигатели серии Common Rail System, Бюллетень 4021493 или Руководство по устранению и ремонту неполадок, Электронная система управления, QSK38, QSK50 и QSK60, Двигатели серии модульных общих железнодорожных систем CM850, Бюллетень 4021533 или обратитесь к руководству по обслуживанию OEM. | Ремонт завершён |
| Менее 10 Ом? **Заменить кабель.** | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Intermediate speed control 2 signal is **not** available.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot an intermediate speed control 2 signal malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box Wiring |  |
> |  | **STEP 1A.** Check Intermediate Speed Control 2 Switch Signal Wire for Open | Less than 10 ohms? |
> |  | **STEP 1B.** Check Intermediate Speed Control 2 Switch Signal Wire for Wire to Wire Short | Less than 10 ohms? |
> |  | **STEP 1C.** Check Intermediate Speed Control 2 Switch Signal Wire for Short to Ground | Less than 10 ohms? |
> | STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
> |  | **STEP 2A.** Check Intermediate Speed Control 2 Switch Signal Wire for Open | Less than 10 ohms? |
>
> ### STEP 1. Check Customer Interface Box Wiring
>
> #### STEP 1A. Check Intermediate Speed Control 2 Switch Signal Wire for Open
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the intermediate speed control 2 switch signal wire for an open. Place one test lead on the intermediate speed control 2 switch signal pin in connector C3. Place the other test lead on intermediate speed control 2 switch signal terminal on the X4 connector. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |  |
>
> #### STEP 1B. Check Intermediate Speed Control 2 Switch Signal Wire for Wire to Wire Short
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the intermediate speed control 2 switch signal wire for wire to wire short. Place one test lead on the intermediate speed control 2 switch signal pin in connector C3. Place the other test lead on each of the remaining terminals in X4 connector. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check Intermediate Speed Control 2 Switch Signal Wire for Short to Ground
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the intermediate speed control 2 switch signal wire for short to ground. Place one test lead on the intermediate speed control 2 switch signal pin in connector C3. Place the other test lead on panel ground. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check Engine Harness to Customer Interface Box Cable
>
> #### STEP 2A. Check Intermediate Speed Control 2 Switch Signal Wire for Open
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box Disconnect customer interface box to engine harness cable connector C10 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check intermediate speed control 2 switch signal wire. Place a jumper between the torque curve select signal pin and the intermediate speed control 2 switch signal pin in the C10 connector. Place one test lead in the torque curve select signal pin of the C3 connector. Place the other test lead in the intermediate speed control 2 switch signal pin of the C3 connector. | Less than 10 ohms? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493, or the Troublehshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60, CM850 Modular Common Rail System Series Engines, Bulletin 4021533, or refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
