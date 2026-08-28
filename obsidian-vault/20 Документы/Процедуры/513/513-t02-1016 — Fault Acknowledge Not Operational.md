---
type: "Процедура"
doc: "513-t02-1016"
title_en: "Fault Acknowledge Not Operational"
modified: "2019-10-21"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1016.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1016.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Fault Acknowledge Not Operational

> [!abstract] Процедура · `513-t02-1016`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1016.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1016.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Нажатие кнопки на дисплее ED-4 не подтверждает сигнал тревоги.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения проблем с дисплеем ED-4. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Возможные причины:

- Программное обеспечение для отображения

- Дисплей ED-4 (кнопка).

Проверить отказ 2 независимых систем? Неисправности должны быть признаны на двигатель.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте программное обеспечение дисплея. |  |
|  | **ШАГ 1А.** Проверить наличие активной ошибки. | Возможно ли распознать ошибку с помощью дисплея ED-4? |
|  | **STEP 1B.** Проверить программное обеспечение дисплея. | Последующая правка программного обеспечения для дисплея ED-4? |
|  | **STEP 1C.** Валидация признания неисправности. | Возможно ли распознать ошибку с помощью дисплея ED-4? |

### ШАГ 1. Проверьте программное обеспечение дисплея.

#### ШАГ 1A. Проверьте неактивное сообщение тревоги.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините датчик температуры охлаждающей жидкости двигателя от электропроводки двигателя. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подождите 30 секунд, монитор ED-4. Проверьте неисправность датчика температуры охлаждающей жидкости. С дисплеями ED-4 на независимых системах, неисправность **должна быть признана на двигатель | Возможно ли распознать ошибку с помощью дисплея ED-4?**| Ремонт завершён. |
| Возможно ли распознать ошибку с помощью дисплея ED-4? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте программное обеспечение дисплея.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте Cummins® QuickServe® Онлайн веб-страницу для новейшего программного обеспечения на дисплее ED-4. Справочная процедура 015-075 в разделе 15 соответствующего руководства по обслуживанию. | Последующая правка программного обеспечения для дисплея ED-4? **YESRepair:** Загрузите новейшее программное обеспечение на дисплей ED-4. Справочная процедура 015-075 в разделе 15 соответствующего руководства по обслуживанию. | 1С |
| Последующая правка программного обеспечения для дисплея ED-4? **NORepair:** Заменить дисплей ED-4.[[513-015-035 — Display(s) and Instrumentation\|См. процедуру 015-035 в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 1C. Проверить признание вины.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините датчик температуры охлаждающей жидкости двигателя от электропроводки двигателя. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подожди 30 секунд. Мониторинг дисплея ED-4. Проверьте неисправность датчика температуры охлаждающей жидкости. | Возможно ли распознать ошибку с помощью дисплея ED-4?| Ремонт завершён. |
| Возможно ли распознать ошибку с помощью дисплея ED-4? **NORepair:** Заменить дисплей ED-4.[[513-015-035 — Display(s) and Instrumentation\|См. процедуру 015-035 в разделе 15.]] | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Pressing the button on the ED-4 display does **not** acknowledge the alarm.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot ED-4 display issues. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible causes are:
>
> - Display software
>
> - ED-4 display (button).
>
> Verify failure 2 independent systems? Faults **must** be acknowledged per engine.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the display software. |  |
> |  | **STEP 1A.** Verify active fault. | Fault acknowledge possible with ED-4 display? |
> |  | **STEP 1B.** Check display software. | Later software revision for the ED-4 display? |
> |  | **STEP 1C.** Validate fault acknowledgement. | Fault acknowledge possible with ED-4 display? |
>
> ### STEP 1. Check the display software.
>
> #### STEP 1A. Check for an inactive alarm message.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the engine coolant temperature sensor from the engine harness. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Wait 30 seconds, monitor ED-4 display. Verify coolant temperature sensor fault. With ED-4 displays on independent systems, fault **must** be acknowledged per engine | Fault acknowledge possible with ED-4 display? **YESRepair:** ED-4 display is working properly. | Repair complete. |
> | Fault acknowledge possible with ED-4 display? **NO** | 1B |  |
>
> #### STEP 1B. Check display software.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check Cummins® QuickServe® On-line webpage for the latest software to ED-4 display. Reference Procedure 015-075 in Section 15 of the appropriate service manual. | Later software revision for the ED-4 display? **YESRepair:** Download the latest software to the ED-4 display. Reference Procedure 015-075 in Section 15 of the appropriate service manual. | 1C |
> | Later software revision for the ED-4 display? **NORepair:** Replace the ED-4 display. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035 in Section 15.]] | Repair complete. |  |
>
> #### STEP 1C. Validate fault acknowledgement.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the engine coolant temperature sensor from the engine harness. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Wait 30 seconds. Monitor ED-4 display. Verify coolant temperature sensor fault. | Fault acknowledge possible with ED-4 display? **YESRepair:** The download of the latest software corrected the issue. | Repair complete. |
> | Fault acknowledge possible with ED-4 display? **NORepair:** Replace the ED-4 display. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035 in Section 15.]] | Repair complete. |  |
