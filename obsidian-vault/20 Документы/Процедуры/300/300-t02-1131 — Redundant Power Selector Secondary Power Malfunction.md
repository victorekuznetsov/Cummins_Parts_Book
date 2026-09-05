---
type: "Процедура"
doc: "300-t02-1131"
title_en: "Redundant Power Selector Secondary Power Malfunction"
modified: "2019-10-15"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1131.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1131.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
  - "перевод/машинный"
---

# Redundant Power Selector Secondary Power Malfunction

> [!abstract] Процедура · `300-t02-1131`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1131.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1131.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Сообщение об ошибке первичного источника питания, отображаемое на блоке управления дизельным двигателем (DCU).

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неполадок сигнала от скорости пикапа сигнала, потерянного. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Сообщение об ошибке вторичного сбоя питания.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс (C.I.B.) проводов. |  |
|  | **STEP 1A.** Проверьте дисплеи панели управления на наличие неисправностей. | Панель управления указывает на неисправность (неисправности)? |
| ШАГ 2. | Проверьте избыточную проводку силового селектора. |  |
|  | **ШАГ 2А.** Проверить избыточный селектор мощности вторичного входа мощности Провода SUPPLY на напряжение +18 ВДК. | Меньше +18±0,2 VDC? |
|  | **STEP 2B.** Проверить избыточный селектор питания первичного входа питания Провода SUPPLY на напряжение +18 ВДК. | Меньше +18±0,2 VDC? |
| ШАГ 3. | Проверьте избыточное напряжение селектора мощности. |  |
|  | **ШАГ 3А.** Проверить избыточный выход мощности селектора питания ПОДДЕРЖАНИЕ. | Выход в пределах ± 0,5 VDC? |

### ШАГ 1. Проверьте клиентский интерфейс (C.I.B.) проводов.

#### ШАГ 1A. Проверьте дисплей панели управления на наличие неисправностей.

| **Условия: **Найдите дисплей панели управления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей панели управления на наличие неисправностей. | Панель управления указывает на неисправность (неисправности)? **Ремонт: **Устранение неисправностей с помощью соответствующего кода ошибки. См. Руководство по устранению неполадок в коде QSB7-DM CM850, Бюллетень 4325972, Раздел TF, или Руководство по устранению и ремонту неполадок в электронной системе управления ISM и QSM 11, Бюллетень [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Раздел TF, Руководство по устранению неполадок в коде X15 CM2350 X125M, Бюллетень 5504346. | Перейдите к соответствующему дереву устранения неисправностей кода ошибки. |
| Панель управления указывает на неисправность (неисправности)? **NORepair:** Заменить приводную муфту. | 2А |  |

### ШАГ 2. Проверьте избыточную проводку силового селектора.

#### ШАГ 2A. Проверьте избыточный селектор мощности вторичного входа мощности Провода SUPPLY на напряжение +18±0,2 VDC.

| **Условия: **Открыть ЦБ. Испытать избыточный селектор питания вторичного ввода мощности SUPPLY провода контакта 6. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение при контакте 6 избыточного селектора питания. Поместите один испытательный щуп на провод вторичной мощности SUPPLY при контакте 6 с избыточным селектором мощности. Поместите другой испытательный щуп на наземный провод панели при контакте 7. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +18±0,2 VDC? **Ремонт:** Проверить аккумуляторы. См. сервисную документацию изготовителя оборудования. | Ремонт завершён. |
| Меньше +18±0,2 VDC? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте избыточный селектор питания первичного ввода мощности Провода SUPPLY на напряжение +18±0,2 VDC.

| **Условия: **Открыть ЦБ. Испытать избыточный селектор питания вторичного ввода мощности SUPPLY провода контакта 1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение при контакте 1 избыточного селектора питания. Поместите один испытательный щуп на первичный провод питания SUPPLY при контакте 1 избыточного селектора питания. Поместите другой испытательный щуп на наземный провод панели при контакте 2. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +18±0,2 VDC? *Да | 3А |
| Меньше +18±0,2 VDC? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте избыточное напряжение селектора мощности.

#### ШАГ 3A. Проверьте избыточную мощность селектора мощности.

| **Условия: **Открыть ЦБ. Испытать избыточный селектор мощности выходной мощности SUPPLY провода контакта 17. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте выходное напряжение при контакте 17 избыточного селектора питания. Поместите один испытательный щуп на выходной провод при контакте 17 избыточного селектора питания. Поместите другой испытательный щуп на наземный провод панели при контакте 16. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Выходное напряжение ±0,5 ВДК первичного и вторичного входных напряжений? *Да | Ремонт завершён. |
| Выходное напряжение ±0,5 ВДК первичного и вторичного входных напряжений? **NORepair:** Заменить избыточный селектор питания. | 1А |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Primary power supply failure error message shown on diesel control unit (DCU).
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot signal from the speed pick-up is signal lost. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Secondary power failure error message.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box (C.I.B.) wiring. |  |
> |  | **STEP 1A.** Check the control panel display for faults. | Control panel indicates fault(s)? |
> | STEP 2. | Check redundant power selector wiring. |  |
> |  | **STEP 2A.** Check redundant power selector secondary power input SUPPLY wire for voltage +18 VDC. | Less than +18±0.2 VDC? |
> |  | **STEP 2B.** Check redundant power selector primary power input SUPPLY wire for voltage +18 VDC. | Less than +18±0.2 VDC? |
> | STEP 3. | Check redundant power selector voltage. |  |
> |  | **STEP 3A.** Check redundant power selector power output SUPPLY. | Output within ± 0.5 VDC? |
>
> ### STEP 1. Check the customer interface box (C.I.B.) wiring.
>
> #### STEP 1A. Check the control panel display for faults.
>
> | **Conditions:** Locate the control panel display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the control panel display for faults. | Control panel indicates fault(s)? **YESRepair:** Troubleshoot the appropriate fault code. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF, or the ISM and QSM 11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF, X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346. | Go to appropriate fault code troubleshooting tree. |
> | Control panel indicates fault(s)? **NORepair:** Replace the drive coupling. | 2A |  |
>
> ### STEP 2. Check redundant power selector wiring.
>
> #### STEP 2A. Check redundant power selector secondary power input SUPPLY wire for voltage +18±0.2 VDC.
>
> | **Conditions:** Open the C.I.B. Test the redundant power selector secondary power input SUPPLY wire pin 6. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at pin 6 of the redundant power selector. Place one test lead at the secondary power SUPPLY wire at pin 6 of the redundant power selector. Place the other test lead on the panel ground wire at pin 7. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +18±0.2 VDC? **YESRepair:** Check the batteries. See equipment manufacturer service information. | Repair complete. |
> | Less than +18±0.2 VDC? **NO** | 2B |  |
>
> #### STEP 2B. Check redundant power selector primary power input SUPPLY wire for voltage +18±0.2 VDC.
>
> | **Conditions:** Open the C.I.B. Test the redundant power selector secondary power input SUPPLY wire pin 1. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at pin 1 of the redundant power selector. Place one test lead at the primary power SUPPLY wire at pin 1 of the redundant power selector. Place the other test lead on the panel ground wire at pin 2. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +18±0.2 VDC? **YES** | 3A |
> | Less than +18±0.2 VDC? **NO** | 3A |  |
>
> ### STEP 3. Check redundant power selector voltage.
>
> #### STEP 3A. Check redundant power selector power output.
>
> | **Conditions:** Open the C.I.B. Test the redundant power selector power output SUPPLY wire pin 17. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the output voltage at pin 17 of the redundant power selector. Place one test lead at the power output wire at pin 17 of the redundant power selector. Place the other test lead on the panel ground wire at pin 16. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Output voltage ±0.5 VDC of the primary and secondary input voltages? **YES** | Repair complete. |
> | Output voltage ±0.5 VDC of the primary and secondary input voltages? **NORepair:** Replace redundant power selector. | 1A |  |
