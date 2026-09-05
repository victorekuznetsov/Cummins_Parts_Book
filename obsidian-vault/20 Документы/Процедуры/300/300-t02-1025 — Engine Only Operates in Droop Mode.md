---
aliases:
  - "Двигатель работает только в режиме статизма"
type: "Процедура"
doc: "300-t02-1025"
title_en: "Engine Only Operates in Droop Mode"
title_ru: "Двигатель работает только в режиме статизма"
modified: "2019-05-22"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4332828"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1025.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1025.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
  - "перевод/машинный"
---

# Engine Only Operates in Droop Mode
**Двигатель работает только в режиме статизма**

> [!abstract] Процедура · `300-t02-1025`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1025.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1025.pdf)

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

Нет.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс (C.I.B.) проводов. |  |
|  | **ШАГ 1А.** Проверьте проволоку с потенциометром SUPPLY и SIGNAL для короткого замыкания. | Больше 100 тысяч ом? |
| ШАГ 2. | Проверьте жгут электропроводки двигателя на C.I.B. |  |
|  | **ШАГ 2А.** Проверьте проволоку с потенциометром SUPPLY и SIGNAL. | Менее 10 Ом? |

### ШАГ 1. Проверьте клиентский интерфейс (C.I.B.) проводов.

#### ШАГ 1A. Проверьте потенциометр SUPPLY и SIGNAL для короткого замыкания.

| **Условия: **Открыть ЦБ. Отключите компьютерную систему. кабельному разъему C1 от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте потенциометр SUPPLY и провода SIGNAL. Отсоедините провод SUPPLY с регулировкой сбрасывания 5 вольт и провод SIGNAL с регулировкой сбрасывания от разъема X1. Поместите один испытательный щуп на суп-регулировку потенциометра 5 вольт контакта питания в разъёме С1. Поместите другой испытательный щуп на контакт сигнала потенциометра с откидным регулятором в разъём C1. | Больше 100 тысяч ом? **Ремонт: **Заменить неисправный провод(ы).[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |
| Больше 100 тысяч ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут электропроводки двигателя на C.I.B.

#### ШАГ 2A. Проверьте потенциометр SUPPLY и провода SIGNAL.

| **Условия: **Отключить C.I.B. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. Отключите компьютерную систему. к проводах двигателя жгут кабельный разъём С4 от жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте потенциометр SUPPLY и провода SIGNAL. Поместите один испытательный щуп в контакт подачи потенциометра с подачей сбрасывания разъема C1. Поместите другой испытательный щуп в контакт сигнала потенциометра с подвеской от разъема C1. | Менее 10 Ом? Заменить кабель. | Ремонт завершён |
| Менее 10 Ом? **NORepair: **Используйте следующие инструкции по ремонту потенциометра: См. Руководство по устранению неполадок в коде CM850 морского вспомогательного QSB7-DM, Бюллетень 4325972, Раздел TF; Руководство по устранению и ремонту неполадок в электронной системе управления ISM и QSM11, Бюллетень [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Раздел TF; Руководство по устранению неполадок в коде X15 CM2350 X125M, Бюллетень 5504346, Раздел TF; или информация об услугах производителя оборудования. | Ремонт завершён |  |


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
> None.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box (C.I.B.) wiring. |  |
> |  | **STEP 1A.** Check the droop adjust potentiometer SUPPLY and SIGNAL wires for a short circuit. | Greater than 100k ohms? |
> | STEP 2. | Check the engine harness to the C.I.B. |  |
> |  | **STEP 2A.** Check the droop adjust potentiometer SUPPLY and SIGNAL wires. | Less than 10 ohms? |
>
> ### STEP 1. Check the customer interface box (C.I.B.) wiring.
>
> #### STEP 1A. Check the droop adjust potentiometer SUPPLY and SIGNAL wires for a short circuit.
>
> | **Conditions:** Open the C.I.B. Disconnect the C.I.B. to engine harness cable connector C1 from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the droop adjust potentiometer SUPPLY and SIGNAL wires. Disconnect the droop adjust 5 volt SUPPLY wire and the droop adjust potentiometer SIGNAL wire from the X1 connector. Place one test lead on the droop adjust potentiometer 5 volt SUPPLY pin in connector C1. Place the other test lead on the droop adjust potentiometer SIGNAL pin in connector C1. | Greater than 100k ohms? **YESRepair:** Replace the faulty wire(s). [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
> | Greater than 100k ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the engine harness to the C.I.B.
>
> #### STEP 2A. Check the droop adjust potentiometer SUPPLY and SIGNAL wires.
>
> | **Conditions:** Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C4 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the droop adjust potentiometer SUPPLY and SIGNAL wires. Place one test lead in the droop adjust potentiometer SUPPLY pin of the C1 connector. Place the other test lead in the droop adjust potentiometer SIGNAL pin of the C1 connector. | Less than 10 ohms? **YESRepair:** Replace the cable. | Repair complete |
> | Less than 10 ohms? **NORepair:** Use the following for potentiometer repair instructions. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF; the ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF; X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346, Section TF; or the equipment manufacturer service information. | Repair complete |  |
