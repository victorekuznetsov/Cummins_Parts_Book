---
type: "Процедура"
doc: "513-t02-1026"
title_en: "Generator Data Does Not Appear On Display"
modified: "2019-10-25"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Generator Data Does Not Appear On Display

> [!abstract] Процедура · `513-t02-1026`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1026.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Данные набора генераторов показывают тире или **не**, присутствующие на дисплее ED-4.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения проблем связи J1939 с генераторной установкой. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Возможные причины:

- Неправильный файл личности судна

- Короткометражный в J1939

- Неправильная настройка на дисплее ED-4.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте дисплей. |  |
|  | **СТЭП 1А.** Проверить файл личности судна. | Новый файл личности судна только что загружен? |
|  | **STEP 1B.** Проверьте настройку двигателя J1939 на дисплее ED-4. | Показаны параметры двигателя J1939? |
|  | **STEP 1C** Проверьте генераторный набор J1939 на дисплее ED-4. | Генератор настроен правильно на дисплее ED-4? |
| ШАГ 2. | Проверьте проводку J1939. |  |
|  | **STEP 2A.** Проверьте наличие открытого диска в схеме J1939. | Менее 10 Ом? |

### ШАГ 1. Проверьте дисплей.

#### ШАГ 1A. Проверьте файл личности судна.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте файл личности судна. Проверьте файл личности судна. | Новый файл личности судна только что загружен? **YESRepair:** Скачать правильный файл личности судна на дисплей от QuickServe® Online.[[513-015-044 — Managing Vessel Personalities\|См. процедуру 015-044 в разделе 15.]] | Ремонт завершён |
| Новый файл личности судна только что загружен? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте двигатель J1939 на дисплее ED-4.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте двигатель J1939 на дисплее ED-4. Контролируйте скорость двигателя, давление масла и температурные параметры охлаждающей жидкости на дисплее ED-4. | Показаны параметры двигателя J1939? *Да | 1С |
| Показаны параметры двигателя J1939? **NORepair: **Ссылка на дисплей **Not** Данные дисплея - J1939 Не работает в дереве симптомов устранения неполадок в разделе TT. | Ремонт завершён |  |

#### ШАГ 1C. Проверьте генераторный набор J1939 в дисплее ED-4.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте генераторный набор J1939 в дисплее ED-4. Проверьте, что генераторный набор настроен на дисплее ED-4. Перейдите в конфигурацию в меню на дисплее ED-4. См. процедуру 015-108 в разделе 15. | Генератор настроен правильно на дисплее ED-4? *Да | 2А |
| Генератор настроен правильно на дисплее ED-4? **NORepair: **На дисплее ED-4 обнаружена неправильная настройка. Выберите правильный идентификатор источника генераторного набора или адрес для этого дисплея.[[513-015-108 — Display Configuration\|См. процедуру 015-108 в разделе 15.]] | Ремонт завершён |  |

### ШАГ 2. Проверьте проводку J1939.

#### ШАГ 2A. Проверьте наличие открытого диска в схеме J1939.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините генераторный набор J1939 от генераторного набора. Отключите генераторный набор J1939 от жгута проводов двигателя или окна интерфейса клиента (C.I.B.). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие открытого диска в схеме J1939. Измерьте сопротивление J1939 (+) в проводной упряжке. Поместите один испытательный щуп на J1939 (+) терминал генераторной установки J1939 разъёма проводной упряжки (прикрепляется к упряжке проводной упряжки двигателя или C.I.B.). Поместите другой испытательный щуп на J1939 (+) терминал генераторного набора J1939 проводного ремня разъема (прикрепляющегося к генераторному набору). Измерьте сопротивление J1939 (-) в проводной упряжке. Поместите один испытательный щуп на J1939 (-) терминал генераторной установки J1939 разъёма проводной упряжки (прикрепляется к упряжке проводной упряжки двигателя или C.I.B.). Поместите другой испытательный щуп на J1939 (-) терминал генераторного комплекса J1939 проводного ремня разъема (прикрепляющегося к генераторному множеству). См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? **Ремонт: **Устранение неполадок в цепи генераторной установки J1939. Ссылка на руководство по обслуживанию генераторной установки. | Ремонт завершён. |
| Менее 10 Ом? **NORepair:** Ремонтировать или заменить генераторный комплекс J1939 проводной упряжкой. Ссылка на руководство по обслуживанию генераторной установки. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Generator set data shows dashes or **not** present on the ED-4 display.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot J1939 communication issues with the generator set. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible causes are:
>
> - Incorrect vessel personality file
>
> - Short in the J1939 circuit
>
> - Improper setup in the ED-4 display.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the display. |  |
> |  | **STEP 1A.** Check the vessel personality file. | New vessel personality file just been downloaded? |
> |  | **STEP 1B.** Check the engine J1939 setup in the ED-4 display. | J1939 engine parameters displayed? |
> |  | **STEP 1C.** Check the generator set J1939 setup in the ED-4 display. | Generator set configured properly in ED-4 display? |
> | STEP 2. | Check the J1939 harness. |  |
> |  | **STEP 2A.** Check for an open in the J1939 circuit. | Less than 10 ohms? |
>
> ### STEP 1. Check the display.
>
> #### STEP 1A. Check the vessel personality file.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the vessel personality file. Check the vessel personality file. | New vessel personality file just been downloaded? **YESRepair:** Download correct vessel personality file to the display from QuickServe® Online. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Repair complete |
> | New vessel personality file just been downloaded? **NO** | 1B |  |
>
> #### STEP 1B. Check the engine J1939 setup in the ED-4 display.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine J1939 setup in the ED-4 display. Monitor the engine speed, oil pressure, and coolant temperature parameters in the ED-4 display. | J1939 engine parameters displayed? **YES** | 1C |
> | J1939 engine parameters displayed? **NORepair:** Reference the Display Does **Not** Display Data - J1939 Does **Not** Work in the troubleshooting symptom tree in Section TT. | Repair complete |  |
>
> #### STEP 1C. Check the generator set J1939 setup in the ED-4 display.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the generator set J1939 setup in the ED-4 display. Verify the generator set is configured in the ED-4 display. Go to the configuration in the menu in the ED-4 display. Refer to Procedure 015-108 in Section 15. | Generator set configured properly in ED-4 display? **YES** | 2A |
> | Generator set configured properly in ED-4 display? **NORepair:** An incorrect setup has been detected in the ED-4 display. Select the proper generator set source ID or address for this display. [[513-015-108 — Display Configuration\|Refer to Procedure 015-108 in Section 15.]] | Repair complete |  |
>
> ### STEP 2. Check the J1939 harness.
>
> #### STEP 2A. Check for an open in the J1939 circuit.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect display generator set J1939 wiring harness from the generator set. Disconnect the generator set J1939 from the engine harness or customer interface box (C.I.B.). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open in the J1939 circuit. Measure the J1939 (+) resistance in the harness. Place one test lead on J1939 (+) terminal of the generator set J1939 wiring harness connector (mating to the engine wiring harness or C.I.B.). Place the other test lead on J1939 (+) terminal of the generator set J1939 wiring harness connector (mating to the generator set). Measure the J1939 (-) resistance in the harness. Place one test lead on J1939 (-) terminal of the generator set J1939 wiring harness connector (mating to the engine wiring harness or C.I.B.). Place the other test lead on J1939 (-) terminal of the generator set J1939 wiring harness connector (mating to the generator set). Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YESRepair:** Troubleshoot the generator set J1939 circuit. Reference the generator set service manual. | Repair complete. |
> | Less than 10 ohms? **NORepair:** Repair or replace the generator set J1939 harness. Reference the generator set service manual. | Repair complete. |  |
