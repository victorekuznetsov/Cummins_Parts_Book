---
aliases:
  - "Неисправности сигнала регулировки статизма"
type: "Процедура"
doc: "115-t02-1021"
title_en: "Droop Adjust Signal Malfunctions"
title_ru: "Неисправности сигнала регулировки статизма"
modified: "2006-08-09"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1021.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1021.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Droop Adjust Signal Malfunctions
**Неисправности сигнала регулировки статизма**

> [!abstract] Процедура · `115-t02-1021`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1021.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1021.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Сигнал регулировки Droop **не** доступен из окна интерфейса клиента.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неполадок, корректирующих симптомы. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **ШАГ 1А.** Проверьте, чтобы настроить потенциометр | Сопротивление менее 10 Ом? |
|  | **ШАГ 1В** Проверьте, чтобы настроить петлю обратной проводов потенциометра | Сопротивление менее 10 Ом? |
|  | **STEP 1C** Проверьте регулировку потенциометра сигнала | Сопротивление менее 10 Ом? |
| ШАГ 2. | Проверьте электропроводку двигателя на кабель клиентского интерфейса |  |
|  | **ШАГ 2А.** Проверьте, чтобы настроить потенциометр и проволоку сигнала | Сопротивление менее 10 Ом? |
|  | **STEP 2B.** Проверьте, чтобы отрегулировать потенциометр и проволоку сигнала | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 1A. Проверьте Droop Adjust Potentiometer

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проволоку питания потенциометра с отвисанием. Поместите один испытательный щуп на штифт с потенциометром 5 вольт (сенсорный штифт 1) в разъем C3. Поместите другой испытательный щуп на потенциометр 5 вольт (сенсорный источник 1) на разъем X4. | Сопротивление менее 10 Ом? *Да | 1В |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 1B. Проверить регулировку петли Potentiometer Return Wire

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод возврата потенциометра с откидным регулировкой. Поместите один пробный щуп на штифт возврата потенциометра с откидным регулированием (отдача датчика 1) в разъём C3. Поместите другой испытательный щуп на выводной потенциометр с откидным регулированием (отдача датчика 1) на разъем X4. | Сопротивление менее 10 Ом? *Да | 1С |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 1C. Проверьте регулировку сигнала Potentiometer

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнальный провод с потенциометром. Поместите один испытательный щуп на контакт сигнала потенциометра с откидным регулятором в разъём C3. Поместите другой испытательный щуп на сигнальный терминал с потенциометром с откидным верхом на разъем X4. | Сопротивление менее 10 Ом? *Да | 2А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 2. Проверьте электропроводку двигателя на кабель клиентского интерфейса

#### ШАГ 2A. Проверьте Droop Adjust Potentiometer Supply and Signal Wires

| **Условия:** Отсоединить окно интерфейса клиента к разъёму кабеля C3 с помощью проводов двигателя от окна интерфейса клиента Отключить окно интерфейса клиента к разъёму кабеля C9 с помощью проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте подачу потенциометра с отвисанием и сигнальные провода. Поместите перемычку между штырем питания с потенциометром 5 вольт (сенсорный источник 1) и контактом сигнала с потенциометром с потенциометром с понижающим регулировкой в разъеме C9. Поместите один испытательный щуп в штепсель потенциометра 5 вольт (сенсорный штифт 1) разъема C3. Поместите другой испытательный щуп в контакт сигнала потенциометра с подвеской от разъема C3. | Сопротивление менее 10 Ом? *Да | 2В |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 2B. Проверьте Droop Adjust Potentiometer Return и проволоку сигнала

| **Условия:** Отсоединить окно интерфейса клиента к разъёму кабеля C3 с помощью проводов двигателя от окна интерфейса клиента Отключить окно интерфейса клиента к разъёму кабеля C9 с помощью проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте регулировку потенциометра с понижением и провода сигнала. Поместите перемычку между контактом сигнала с потенциометром с регулировкой сбрасывания и штифтом возврата потенциометра с регулировкой сбрасывания (отдача датчика 1) в разъеме C9. Поместите один пробный щуп в штырь с откидным регулятором возврата потенциометра (датчик возврата 1) разъема C3. Поместите другой испытательный щуп в контакт сигнала потенциометра с подвеской от разъема C3. | Сопротивление менее 10 Ом? **Ремонт:** См. раздел TF в руководстве по устранению неполадок и ремонту, QSK19 CM850 Модульные двигатели серии Common Rail System, Бюллетень 4021493 или обратитесь к руководству по обслуживанию OEM для инструкций по ремонту потенциометра. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Droop adjust signal **not** available from customer interface box.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot droop adjust symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box Wiring |  |
> |  | **STEP 1A.** Check Droop Adjust Potentiometer Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 1B.** Check Droop Adjust Potentiometer Return Wire | Less than 10 ohms resistance? |
> |  | **STEP 1C.** Check Droop Adjust Potentiometer Signal Wire | Less than 10 ohms resistance? |
> | STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
> |  | **STEP 2A.** Check Droop Adjust Potentiometer Supply and Signal Wires | Less than 10 ohms resistance? |
> |  | **STEP 2B.** Check Droop Adjust Potentiometer Return and Signal Wires | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Customer Interface Box Wiring
>
> #### STEP 1A. Check Droop Adjust Potentiometer Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the droop adjust potentiometer supply wire. Place one test lead on the droop adjust potentiometer 5 volt supply (sensor supply 1) pin in connector C3. Place the other test lead on droop adjust potentiometer 5 volt supply (sensor supply 1) terminal on the X4 connector. | Less than 10 ohms resistance? **YES** | 1B |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 1B. Check Droop Adjust Potentiometer Return Wire
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the droop adjust potentiometer return wire. Place one test lead on the droop adjust potentiometer return (sensor return 1) pin in connector C3. Place the other test lead on droop adjust potentiometer return (sensor return 1) terminal on the X4 connector. | Less than 10 ohms resistance? **YES** | 1C |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 1C. Check Droop Adjust Potentiometer Signal Wire
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the droop adjust potentiometer signal wire. Place one test lead on the droop adjust potentiometer signal pin in connector C3. Place the other test lead on droop adjust potentiometer signal terminal on the X4 connector. | Less than 10 ohms resistance? **YES** | 2A |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 2. Check Engine Harness to Customer Interface Box Cable
>
> #### STEP 2A. Check Droop Adjust Potentiometer Supply and Signal Wires
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box Disconnect customer interface box to engine harness cable connector C9 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the droop adjust potentiometer supply and signal wires. Place a jumper between the droop adjust potentiometer 5 volt supply (sensor supply 1) pin and the droop adjust potentiometer signal pin in the C9 connector. Place one test lead in the droop adjust potentiometer 5 volt supply (sensor supply 1) pin of the C3 connector. Place the other test lead in the droop adjust potentiometer signal pin of the C3 connector. | Less than 10 ohms resistance? **YES** | 2B |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> #### STEP 2B. Check Droop Adjust Potentiometer Return and Signal Wires
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box Disconnect customer interface box to engine harness cable connector C9 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the droop adjust potentiometer retrun and signal wires. Place a jumper between the droop adjust potentiometer signal pin and the droop adjust potentiometer return (sensor return 1) pin in the C9 connector. Place one test lead in the droop adjust potentiometer return (sensor return 1) pin of the C3 connector. Place the other test lead in the droop adjust potentiometer signal pin of the C3 connector. | Less than 10 ohms resistance? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493 or refer to the OEM Service Manual for potentiometer repair instructions. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
