---
aliases:
  - "Двигатель работает только в режиме статизма"
type: "Процедура"
doc: "116-t02-1025"
title_en: "Engine Only Operates in Droop Mode"
title_ru: "Двигатель работает только в режиме статизма"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1025.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1025.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Engine Only Operates in Droop Mode
**Двигатель работает только в режиме статизма**

> [!abstract] Процедура · `116-t02-1025`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1025.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1025.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель будет работать только в режиме droop.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов сбоя двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **ШАГ 1А.** Проверьте, чтобы настроить потенциометр и сигнальную проводку для короткой цепи | Сопротивление менее 10 Ом? |
| ШАГ 2. | Проверьте электропроводку двигателя на кабель клиентского интерфейса |  |
|  | **ШАГ 2А.** Проверьте, чтобы настроить потенциометр и проволоку сигнала | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 1A. Проверьте Droop настроить потенциометр поставки и сигнальную проводку для короткой цепи

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C2 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте подачу потенциометра с отвисанием и сигнальные провода. Отсоедините провод с подачей 5 вольт (сенсорный подачу 1) и провод сигнала с подачей потенциометра от разъема X4. Поместите один испытательный щуп на штифт с потенциометром 5 вольт (сенсорный штифт 1) в разъеме C2. Поместите другой испытательный щуп на контакт сигнала потенциометра с отсевом в разъёме C2. | Сопротивление менее 10 Ом? * Заменить провод(ы) См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте электропроводку двигателя на кабель клиентского интерфейса

#### ШАГ 2A. Проверьте Droop Adjust Potentiometer Supply and Signal Wires

| **Условия:** Отсоедините окно клиентского интерфейса к проводах двигателя, ремня кабельного разъема C2 от окна клиентского интерфейса. Отсоедините окно интерфейса клиента к проводах двигателя кабельного разъема C9 от проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте подключение потенциометра к потенциометру и сигнальные провода. Поместите один испытательный щуп в штепсель потенциометра 5 вольт (сенсорный штепсель 1) разъема C2. Поместите другой испытательный щуп в контакт сигнала потенциометра с подвеской от суп-регулировки разъема C2. | Сопротивление менее 10 Ом? **Ремонт:** См. раздел TF в руководстве по устранению неполадок и ремонту, QSK19 CM850 Модульные двигатели общей системы железной дороги, вестник 4021493 или руководство по устранению неполадок и ремонту, электронная система управления, QSK38, QSK50 и QSK60, вестник 4021533 модульной общей системы железной дороги CM850 или обратитесь к руководству по обслуживанию OEM для инструкций по ремонту потенциометра. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine will **only** operate in droop mode.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine droop symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box Wiring |  |
> |  | **STEP 1A.** Check Droop Adjust Potentiometer Supply and Signal Wire for Short Circuit | Less than 10 ohms resistance? |
> | STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
> |  | **STEP 2A.** Check Droop Adjust Potentiometer Supply and Signal Wires | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Customer Interface Box Wiring
>
> #### STEP 1A. Check Droop Adjust Potentiometer Supply and Signal Wire for Short Circuit
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the droop adjust potentiometer supply and signal wires. Disconnect the droop adjust 5 volt supply (sensor supply 1) wire and the droop adjust potentiometer signal wire from the X4 connector. Place one test lead on the droop adjust potentiometer 5 volt supply (sensor supply 1) pin in connector C2. Place the other test lead on droop adjust potentiometer signal pin in connector C2. | Less than 10 ohms resistance? **YESRepair:** Replace the wire(s). Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
> | Less than 10 ohms resistance? **NO** | 2A |  |
>
> ### STEP 2. Check Engine Harness to Customer Interface Box Cable
>
> #### STEP 2A. Check Droop Adjust Potentiometer Supply and Signal Wires
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. Disconnect customer interface box to engine harness cable connector C9 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check droop adjust potentiometer supply and signal wires. Place one test lead in the droop adjust potentiometer 5 volt supply (sensor supply 1) pin of the C2 connector. Place the other test lead in the droop adjust potentiometer signal pin of the C2 connector. | Less than 10 ohms resistance? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493, or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60, CM850 Modular Common Rail System Series Engines, Bulletin 4021533, or refer to the OEM service manual for potentiometer repair instructions. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
