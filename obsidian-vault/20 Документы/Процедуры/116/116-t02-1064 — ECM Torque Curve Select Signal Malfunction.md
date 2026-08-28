---
aliases:
  - "Неисправность сигнала выбора кривой момента ЭБУ"
type: "Процедура"
doc: "116-t02-1064"
title_en: "ECM Torque Curve Select Signal Malfunction"
title_ru: "Неисправность сигнала выбора кривой момента ЭБУ"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1064.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1064.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# ECM Torque Curve Select Signal Malfunction
**Неисправность сигнала выбора кривой момента ЭБУ**

> [!abstract] Процедура · `116-t02-1064`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1064.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1064.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Сигнал выбора кривой крутящего момента ECM не доступен.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неполадок в выбранном сигнале кривой крутящего момента ECM. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 1A.** Проверьте кривую крутящего момента, выберите сигнальную проводку для открытого доступа | Менее 10 Ом? |
|  | **STEP 1B.** Проверьте кривую крутящего момента, выберите сигнальную проводку для провода короткой проводов | Менее 10 Ом? |
|  | **STEP 1C.** Проверьте кривую крутящего момента, выберите сигнальную проводку для короткой посадки | Менее 10 Ом? |
| ШАГ 2. | Проверьте электропроводку двигателя на кабель клиентского интерфейса |  |
|  | **STEP 2A.** Проверьте кривую крутящего момента, выберите сигнальную проводку для открытого доступа | Менее 10 Ом? |

### ШАГ 1. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 1A. Проверьте кривую крутящего момента Выберите сигнальную проводку для открытого доступа

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кривую крутящего момента, выберите сигнальный провод для открытого. Поместите один испытательный щуп на кривую крутящего момента, выберите контакт сигнала в разъеме C3. Поместите другой испытательный щуп на кривую крутящего момента, выберите сигнальный терминал на разъеме X4. | Менее 10 Ом? *Да | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |  |

#### ШАГ 1B. Проверьте кривую крутящего момента выберите сигнальную проводку для провода короткой проводов

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кривую крутящего момента, выберите сигнальный провод для провода для короткого провода. Поместите один испытательный щуп на кривую крутящего момента, выберите контакт сигнала в разъеме C3. Поместите другой испытательный щуп на каждый из оставшихся терминалов в разъем X4. | Менее 10 Ом?  Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте кривую крутящего момента выберите сигнальную проводку для короткой посадки

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кривую крутящего момента, выберите сигнальный провод для короткого заземления. Поместите один испытательный щуп на кривую крутящего момента, выберите контакт сигнала в разъеме C3. Поместите другой испытательный щуп на панельную площадку. | Менее 10 Ом?  Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте электропроводку двигателя на кабель клиентского интерфейса

#### ШАГ 2A. Проверьте кривую крутящего момента Выберите сигнальную проводку для открытого доступа

| **Условия:** Отсоединить окно интерфейса клиента к разъёму кабеля C3 с помощью проводов двигателя от окна интерфейса клиента Отключить окно интерфейса клиента к разъёму кабеля C10 с помощью проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить кривую крутящего момента выберите сигнальный провод. Поместите перемычку между контактом сигнала кривой крутящего момента и штифтом выбора сбрасывания в разъеме C10. Поместите один испытательный щуп в кривую крутящего момента, выберите сигнальный контакт разъема C3. Поместите другой испытательный щуп в контакт сигнала сбрасывания разъема C3. | Менее 10 Ом? **Ремонт:** См. раздел TF в руководстве по устранению неполадок и ремонту, QSK19 CM850 Модульные двигатели общей системы железных дорог серии, бюллетень 4021493 или руководство по устранению неполадок и ремонту, электронная система управления, QSK38, QSK50 и QSK60, двигатели серии модульной общей системы железных дорог CM850, бюллетень 4021533 или обратитесь к руководству по обслуживанию OEM. | Ремонт завершён |
| Менее 10 Ом? **Заменить кабель.** | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - ECM torque curve select signal is **not** available.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot an ECM torque curve select signal. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box Wiring |  |
> |  | **STEP 1A.** Check Torque Curve Select Signal Wire for Open | Less than 10 ohms? |
> |  | **STEP 1B.** Check Torque Curve Select Signal Wire for Wire to Wire Short | Less than 10 ohms? |
> |  | **STEP 1C.** Check Torque Curve Select Signal Wire for Short to Ground | Less than 10 ohms? |
> | STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
> |  | **STEP 2A.** Check Torque Curve Select Signal Wire for Open | Less than 10 ohms? |
>
> ### STEP 1. Check Customer Interface Box Wiring
>
> #### STEP 1A. Check Torque Curve Select Signal Wire for Open
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the torque curve select signal wire for an open. Place one test lead on the torque curve select signal pin in connector C3. Place the other test lead on torque curve select signal terminal on the X4 connector. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |  |
>
> #### STEP 1B. Check Torque Curve Select Signal Wire for Wire to Wire Short
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the torque curve select signal wire for wire to wire short. Place one test lead on the torque curve select signal pin in connector C3. Place the other test lead on each of the remaining terminals in X4 connector. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check Torque Curve Select Signal Wire for Short to Ground
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the torque curve select signal wire for short to ground. Place one test lead on the torque curve select signal pin in connector C3. Place the other test lead on panel ground. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check Engine Harness to Customer Interface Box Cable
>
> #### STEP 2A. Check Torque Curve Select Signal Wire for Open
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box Disconnect customer interface box to engine harness cable connector C10 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check torque curve select signal wire. Place a jumper between the torque curve select signal pin and the droop select pin in the C10 connector. Place one test lead in the torque curve select signal pin of the C3 connector. Place the other test lead in the droop select signal pin of the C3 connector. | Less than 10 ohms? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493, or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60, CM850 Modular Common Rail System Series Engines, Bulletin 4021533, or refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
