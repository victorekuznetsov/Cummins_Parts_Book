---
type: "Процедура"
doc: "513-t02-1021"
title_en: "Display Does Not Dim or Illuminate"
modified: "2019-09-27"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1021.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1021.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Display Does Not Dim or Illuminate

> [!abstract] Процедура · `513-t02-1021`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1021.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1021.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Дисплей **не** тускнеет или светлеет при нажатии кнопки на дисплее ED-4.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения проблем с дисплеем, если оно оборудовано. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Функция затемнения может быть доступна на всех судах.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте дисплей. |  |
|  | **ШАГ 1А.** Проверьте выключатель диммера (помощь). | Сопротивление более 100k Ом, когда переключатель находится в положении выключения? |
|  | **ШАГ 1В.** Проверьте диммер дисплея. | Дисплей ED-4 становится светлее или тусклее при нажатии кнопок? |
|  | **STEP 1C.** Проверить программное обеспечение дисплея. | Есть ли более поздний пересмотр программного обеспечения для дисплея ED-4? |

### ШАГ 1. Проверьте дисплей.

#### ШАГ 1A. Проверьте выключатель диммера (помощь).

| **Условия:** Отключите тусклый переключатель у руля. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление через установленный на штурвале тусклый выключатель. | Сопротивление более 100k Ом, когда переключатель находится в положении выключения? *Да | 1В |
| Сопротивление более 100k Ом, когда переключатель находится в положении выключения? **NORepair:** Заменить выключатель диммера.[[513-015-101 — Start Switch\|См. процедуру 015-101 в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 1B. Проверьте диммер дисплея.

| **Условия: **Выключите выключатель. Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подтвердите функцию затемнения на дисплее ED-4. Переходите к Свету, выбирайте тусклый или яркий. | Дисплей ED-4 становится светлее или тусклее при нажатии кнопок? **Ремонт: **ED-4 работает правильно. | Ремонт завершён. |
| Дисплей ED-4 становится светлее или тусклее при нажатии кнопок? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте программное обеспечение дисплея.

| **Условия:** Система поворота позволяет выключать выключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте INCALTM на наличие новейшего программного обеспечения для дисплея ED-4. | Есть ли более поздний пересмотр программного обеспечения для дисплея ED-4? **Ремонт:** Загрузите новейшее программное обеспечение на дисплей ED-4.[[513-015-107 — Display Software\|См. процедуру 015-107 в разделе 15.]] | Ремонт завершён. |
| Есть ли более поздний пересмотр программного обеспечения для дисплея ED-4? **NORepair:** Заменить дисплей ED-4.[[513-015-035 — Display(s) and Instrumentation\|См. процедуру 015-035 в разделе 15.]]Для ЦРУ. Дисплей ED-4: См. процедуру 015-023 в разделе 15. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Display does **not** dim or brighten when pressing the button on the ED-4 display.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot display dimming issues, if equipped. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The dimming feature may **not** be available on all vessels.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the display. |  |
> |  | **STEP 1A.** Check the dimmer switch (helm). | Greater than 100k ohms resistance when switch is in OFF position? |
> |  | **STEP 1B.** Check the display dimmer. | Does the ED-4 display brighten or dim when buttons are pressed? |
> |  | **STEP 1C.** Check display software. | Is there a later software revision for the ED-4 display? |
>
> ### STEP 1. Check the display.
>
> #### STEP 1A. Check the dimmer switch (helm).
>
> | **Conditions:** Disconnect the dimmer switch at the helm. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance across the helm mounted dimmer switch. | Greater than 100k ohms resistance when switch is in OFF position? **YES** | 1B |
> | Greater than 100k ohms resistance when switch is in OFF position? **NORepair:** Replace the dimmer switch. [[513-015-101 — Start Switch\|Refer to Procedure 015-101 in Section 15.]] | Repair complete. |  |
>
> #### STEP 1B. Check the display dimmer.
>
> | **Conditions:** Turn enable switch OFF. Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Confirm the dimmer function on the ED-4 display. Go to Light, choose dimmer or brighter. | Does the ED-4 display brighten or dim when buttons are pressed? **YESRepair:** ED-4 is working properly. | Repair complete. |
> | Does the ED-4 display brighten or dim when buttons are pressed? **NO** | 1C |  |
>
> #### STEP 1C. Check display software.
>
> | **Conditions:** Turn system enable switch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check INCAL™ for the latest software to ED-4 display. | Is there a later software revision for the ED-4 display? **YESRepair:** The download the latest software to the ED-4 display. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Repair complete. |
> | Is there a later software revision for the ED-4 display? **NORepair:** Replace the ED-4 display. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035 in Section 15.]] For the C.I.B. ED-4 display: Refer to Procedure 015-023 in Section 15. | Repair complete. |  |
