---
type: "Процедура"
doc: "300-t02-1061"
title_en: "Low Oil Pressure Shutdown Lamp Driver Malfunction"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1061.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1061.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
  - "перевод/машинный"
---

# Low Oil Pressure Shutdown Lamp Driver Malfunction

> [!abstract] Процедура · `300-t02-1061`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1061.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1061.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Лампа выключения низкого давления освещается, когда условие выключения низкого давления не существует.

- Лампа выключения низкого давления **не** освещается при наличии состояния выключения низкого давления.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неисправности водителя лампы с низким давлением масла. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Нет.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс (C.I.B.) проводов. |  |
|  | **ШАГ 1А.** Проверьте SIGNAL провод с низким давлением для открытой цепи. | Менее 10 Ом? |
|  | **ШАГ 1В.** Проверьте SIGNAL-провод низкого давления на короткое замыкание. | Больше 100 тысяч ом? |
|  | **ШАГ 1С.** Проверьте отключение низкое давление SIGNAL провода для короткого замыкания на землю. | Больше 100 тысяч ом? |
| ШАГ 2. | Проверьте жгут электропроводки двигателя на C.I.B. |  |
|  | **ШАГ 2А.** Проверьте SIGNAL провод с низким давлением для открытой цепи. | Менее 10 Ом? |
|  | **ШАГ 2В.** Проверьте SIGNAL-провод низкого давления для короткого замыкания. | Больше 100 тысяч ом? |

### ШАГ 1. Проверьте клиентский интерфейс (C.I.B.) проводов.

#### ШАГ 1A. Проверьте SIGNAL-провод низкого давления для открытой цепи.

| **Условия: **Открыть ЦБ. Отключите компьютерную систему. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте низкое давление масла выключателя провода SIGNAL для открытой цепи. Поместите один испытательный щуп на контакт сигнала отключения низкого давления масла в разъём C1. Поместите другой испытательный щуп на терминал SIGNAL с низким давлением масла на разъем X1. | Менее 10 Ом? *Да | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1B. Проверьте SIGNAL-провод низкого давления для короткого замыкания.

| **Условия: **Открыть ЦБ. Отключите компьютерную систему. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте SIGNAL-провод низкого давления для короткого замыкания. Поместите один испытательный щуп на контакт сигнала отключения низкого давления масла в разъём C1. Поместите другой испытательный щуп на каждый из оставшихся терминалов в разъем X1. | Больше 100 тысяч ом? Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |
| Больше 100 тысяч ом? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте низкое давление выключения провода SIGNAL для короткого замыкания на землю.

| **Условия: **Открыть ЦБ. Отключите компьютерную систему. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте низкое давление выключения провода SIGNAL для короткого замыкания на землю. Поместите один испытательный щуп на контакт сигнала отключения низкого давления масла в разъём C1. Поместите другой испытательный щуп на землю панели. | Больше 100 тысяч ом? Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |
| Больше 100 тысяч ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут электропроводки двигателя на C.I.B. Кабель.

#### ШАГ 2A. Проверьте низкое давление масла выключателя провода SIGNAL для открытой цепи.

| **Условия: **Отключить C.I.B. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. Отключите компьютерную систему. к проводах двигателя жгут кабельный разъём С4 от жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте низкое давление масла выключателя провода SIGNAL для открытой цепи. Поместите перемычку между контактом сигнала отключения низкого давления масла и общим контактом сигнала отключения в разъеме C4. Поместите один испытательный щуп в контакт сигнала отключения низкого давления масла разъема C1. Поместите другой испытательный щуп в общий контакт сигнала отключения разъема C1. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2B. Проверьте SIGNAL-провод низкого давления для короткого замыкания.

| **Условия: **Отключить C.I.B. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. Отключите компьютерную систему. к проводах двигателя жгут кабельный разъём С4 от жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте SIGNAL-провод низкого давления для короткого замыкания. Поместите один испытательный щуп на контакт сигнала отключения низкого давления масла в разъём C1. Поместите другой испытательный щуп на каждый из оставшихся штифтов в разъеме C1. | Больше 100 тысяч ом? Заменить кабель. | Ремонт завершён |
| Больше 100 тысяч ом? **NORepair:** Устранение неисправностей с помощью соответствующего кода ошибки. См. Руководство по устранению неполадок в коде CM850 морского вспомогательного QSB7-DM, Бюллетень 4325972, Раздел TF; или Руководство по устранению и ремонту неполадок в электронной системе управления ISM и QSM 11, Бюллетень [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Раздел TF; или Руководство по устранению неполадок в коде X15 CM2350 X125M, Бюллетень 5504346, Раздел TF; или информация об услугах производителя оборудования. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The low pressure shutdown lamp is illuminated when a low pressure shutdown condition does **not** exist.
>
> - The low pressure shutdown lamp is **not** illuminated when a low pressure shutdown condition exists.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a low oil pressure shutdown lamp driver malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
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
> |  | **STEP 1A.** Check the low pressure shutdown SIGNAL wire for an open circuit. | Less than 10 ohms? |
> |  | **STEP 1B.** Check the low pressure shutdown SIGNAL wire for a wire-to-wire short circuit. | Greater than 100k ohms? |
> |  | **STEP 1C.** Check the low pressure shutdown SIGNAL wire for a short circuit to ground. | Greater than 100k ohms? |
> | STEP 2. | Check the engine harness to the C.I.B. |  |
> |  | **STEP 2A.** Check the low pressure shutdown SIGNAL wire for an open circuit. | Less than 10 ohms? |
> |  | **STEP 2B.** Check the low pressure shutdown SIGNAL wire for a wire-to-wire short circuit. | Greater than 100k ohms? |
>
> ### STEP 1. Check the customer interface box (C.I.B.) wiring.
>
> #### STEP 1A. Check the low pressure shutdown SIGNAL wire for an open circuit.
>
> | **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the low oil pressure shutdown SIGNAL wire for an open circuit. Place one test lead on the low oil pressure shutdown SIGNAL pin in connector C1. Place the other test lead on the low oil pressure shutdown SIGNAL terminal on the X1 connector. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> #### STEP 1B. Check the low pressure shutdown SIGNAL wire for a wire-to-wire short circuit.
>
> | **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the low pressure shutdown SIGNAL wire for a wire-to-wire short circuit. Place one test lead on the low oil pressure shutdown SIGNAL pin in connector C1. Place the other test lead on each of the remaining terminals in the X1 connector. | Greater than 100k ohms? **YESRepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
> | Greater than 100k ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check the low pressure shutdown SIGNAL wire for a short circuit to ground.
>
> | **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the low pressure shutdown SIGNAL wire for a short circuit to ground. Place one test lead on the low oil pressure shutdown SIGNAL pin in connector C1. Place the other test lead on the panel ground. | Greater than 100k ohms? **YESRepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
> | Greater than 100k ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the engine harness to the C.I.B. cable.
>
> #### STEP 2A. Check the low oil pressure shutdown SIGNAL wire for an open circuit.
>
> | **Conditions:** Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C4 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the low oil pressure shutdown SIGNAL wire for an open circuit. Place a jumper between the low oil pressure shutdown SIGNAL pin and the common shutdown SIGNAL pin in the C4 connector. Place one test lead in the low oil pressure shutdown SIGNAL pin of the C1 connector. Place the other test lead in the common shutdown SIGNAL pin of the C1 connector. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> #### STEP 2B. Check the low pressure shutdown SIGNAL wire for a wire-to-wire short circuit.
>
> | **Conditions:** Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C4 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the low pressure shutdown SIGNAL wire for a wire-to-wire short circuit. Place one test lead on the low oil pressure shutdown SIGNAL pin in connector C1. Place the other test lead on each of the remaining pins in the C1 connector. | Greater than 100k ohms? **YESRepair:** Replace the cable. | Repair complete |
> | Greater than 100k ohms? **NORepair:** Troubleshoot the appropriate fault code. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF; or ISM and QSM 11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF; or X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346, Section TF; or the equipment manufacturer service information. | Repair complete |  |
