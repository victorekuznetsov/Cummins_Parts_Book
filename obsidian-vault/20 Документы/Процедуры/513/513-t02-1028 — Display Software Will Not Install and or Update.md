---
type: "Процедура"
doc: "513-t02-1028"
title_en: "Display Software Will Not Install and/or Update"
modified: "2019-10-22"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1028.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1028.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Display Software Will Not Install and/or Update

> [!abstract] Процедура · `513-t02-1028`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1028.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1028.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Программное обеспечение отображения **не **загружается на дисплей.

- Дисплей показывает красный экран во время загрузки.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения проблем с загрузкой программного обеспечения дисплея. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Возможные причины включают:

- Несовместимая USB-накопитель

- USB-накопитель **не** подключен правильно

- Программное обеспечение повреждено.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте USB-накопитель и порт. |  |
|  | **STEP 1A.** Загрузка файла программного обеспечения. | Загрузка программного файла? |
|  | **STEP 1B.** Проверьте установку USB-накопителя. | USB-накопитель установлен правильно? |
|  | **STEP 1C.** Проверьте совместимость USB-накопителей. | USB-накопитель совместим? |
| ШАГ 2. | Проверьте программное обеспечение дисплея. |  |
|  | **STEP 2A.** Проверьте программное обеспечение дисплея. | Совместимое программное обеспечение? |
|  | **STEP 2B.** Загрузите программное обеспечение дисплея на другой дисплей ED-4. | Программное обеспечение для отображения загружается правильно? |
|  | **STEP 2C.** Загрузите программное обеспечение дисплея в другой USB-накопитель. | Программное обеспечение для отображения загружается правильно? |

### ШАГ 1. Проверьте USB-накопитель и порт.

#### ШАГ 1A. Загрузка программного файла.

| **Условия: **Выключите выключатель. Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте USB-накопитель и порт. Попробуйте загрузить файл программного обеспечения на дисплей ED-4. См. процедуру 015-107 в разделе 15. | Загрузка программного файла? **Ремонт: **Загрузка файла программного обеспечения исправила проблему. | Ремонт завершён. |
| Загрузка программного файла? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте установку USB-накопителя.

| **Условия: **Нет. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте установку USB-накопителя. Убедитесь, что USB-накопитель установлен в порт USB дисплея должным образом. См. процедуру 015-107 в разделе 15. Если используется USB-узел расширения Cummins® **не**, проверьте соединение USB. Некоторые USB-разъемы являются обратимыми. | USB-накопитель установлен правильно? *Да | 1С |
| USB-накопитель установлен правильно? **NORepair:** Установите USB-накопитель правильно.[[513-015-107 — Display Software\|См. процедуру 015-107 в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 1C. Проверьте совместимость USB-накопителей.

| **Условия: **Нет. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте совместимость USB-накопителей. Проверьте, совместима ли USB-накопитель с дисплеем.[[513-015-107 — Display Software\|См. процедуру 015-107 в разделе 15.]] | USB-накопитель совместим? *Да | 2А |
| USB-накопитель совместим? **NORepair:** Загрузите программное обеспечение дисплея на совместимый USB-накопитель.[[513-015-107 — Display Software\|См. процедуру 015-107 в разделе 15.]] | Ремонт завершён. |  |

### ШАГ 2. Проверьте программное обеспечение дисплея.

#### ШАГ 2A. Проверьте программное обеспечение дисплея.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте программное обеспечение дисплея. Проверьте, что программное обеспечение отображения на USB-накопителе соответствует требованиям к загрузке.[[513-015-107 — Display Software\|См. процедуру 015-107 в разделе 15.]] | Совместимое программное обеспечение? *Да | 2В |
| Совместимое программное обеспечение? **NORepair:** Перезагрузите последнюю версию программного обеспечения для отображения с веб-страницы Cummins® QuickServe® на USB-накопитель.[[513-015-107 — Display Software\|См. процедуру 015-107 в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 2B. Загрузите программное обеспечение дисплея в другой дисплей ED-4.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Скачать программное обеспечение для отображения. Загрузите новейшее программное обеспечение для отображения на другой дисплей ED-4.[[513-015-107 — Display Software\|См. процедуру 015-107 в разделе 15.]] | Отображать программное обеспечение загружать правильно? **YESRepair:** Загрузка программного обеспечения для отображения исправила проблему. | Ремонт завершён. |
| Отображать программное обеспечение загружать правильно? **НЕТ** | 2C |  |

#### ШАГ 2C. Загрузите программное обеспечение дисплея в другой USB-накопитель.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Скачать программное обеспечение для отображения. Загрузите программное обеспечение дисплея в другой USB-накопитель. Повторно попробуйте загрузить программное обеспечение на неисправный дисплей ED-4. | Программное обеспечение для отображения загружается правильно? **YESRepair:** Загрузка программного обеспечения для отображения исправила проблему. | Ремонт завершён. |
| Программное обеспечение для отображения загружается правильно? **NORepair:** Заменить дисплей ED-4.[[513-015-035 — Display(s) and Instrumentation\|См. процедуру 015-035 в разделе 15.]] | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Display software will **not** download into the display.
>
> - Display shows a red screen while downloading.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot display software download issues. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible causes include:
>
> - Incompatible USB stick
>
> - USB stick **not** plugged in properly
>
> - Software corrupted.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check USB stick and port. |  |
> |  | **STEP 1A.** Software file download. | Software file download? |
> |  | **STEP 1B.** Check the USB stick installation. | USB stick installed properly? |
> |  | **STEP 1C.** Check USB stick compatibility. | USB stick compatible? |
> | STEP 2. | Check the display software. |  |
> |  | **STEP 2A.** Check the display software. | Display software compatible? |
> |  | **STEP 2B.** Download display software into another ED-4 display. | Display software downloaded properly? |
> |  | **STEP 2C.** Download display software into another USB stick. | Display software downloaded properly? |
>
> ### STEP 1. Check USB stick and port.
>
> #### STEP 1A. Software file download.
>
> | **Conditions:** Turn enable switch OFF. Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check USB stick and port. Attempt to download the software file to the ED-4 display. Refer to Procedure 015-107 in Section 15. | Software file download? **YESRepair:** The download of the software file has corrected the issue. | Repair complete. |
> | Software file download? **NO** | 1B |  |
>
> #### STEP 1B. Check the USB stick installation.
>
> | **Conditions:** None. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the USB stick installation. Verify the USB stick is installed in the display USB port properly. Refer to Procedure 015-107 in Section 15. If a Cummins® USB extension harness is **not** being used, verify USB connection. Some USB connectors are reversible. | USB stick installed properly? **YES** | 1C |
> | USB stick installed properly? **NORepair:** Install USB stick properly. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Repair complete. |  |
>
> #### STEP 1C. Check USB stick compatibility.
>
> | **Conditions:** None. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check USB stick compatibility. Verify the USB stick is compatible with the display. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | USB stick compatible? **YES** | 2A |
> | USB stick compatible? **NORepair:** Download the display software to a compatible USB stick. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Repair complete. |  |
>
> ### STEP 2. Check the display software.
>
> #### STEP 2A. Check the display software.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check display software. Verify the display software on USB stick meets download requirements. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Display software compatible? **YES** | 2B |
> | Display software compatible? **NORepair:** Re-download the latest version of the display software from Cummins® QuickServe® On-line webpage to the USB stick. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Repair complete. |  |
>
> #### STEP 2B. Download the display software into another ED-4 display.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Download the display software. Download the latest display software to another ED-4 display. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Display software download properly? **YESRepair:** The download of the display software has corrected the issue. | Repair complete. |
> | Display software download properly? **NO** | 2C |  |
>
> #### STEP 2C. Download the display software into another USB stick.
>
> | **Conditions:** Turn enable ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Download the display software. Download the display software into another USB stick. Re-attempt to download software to malfunctioning ED-4 display. | Display software downloaded properly? **YESRepair:** The download of the display software has corrected the issue. | Repair complete. |
> | Display software downloaded properly? **NORepair:** Replace the ED-4 display. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035 in Section 15.]] | Repair complete. |  |
