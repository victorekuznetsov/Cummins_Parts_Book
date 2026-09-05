---
type: "Процедура"
doc: "513-t02-1027"
title_en: "Display Vessel Personality File Will Not Import and/or Export"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1027.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1027.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Display Vessel Personality File Will Not Import and/or Export

> [!abstract] Процедура · `513-t02-1027`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1027.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1027.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Файл личности судна **не** загружается на дисплей.

- Файл личности судна **не будет** экспортироваться с дисплея.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения проблем с загрузкой файла личности судна и экспортом проблем. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Возможные причины включают:

- Несовместимая универсальная последовательная шина (USB)

- USB-накопитель **не** встроен правильно

- Файл личности судна поврежден.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте USB-накопитель и порт. |  |
|  | **STEP 1A.** Проверить файл личности судна. | Файл личности судна загружен? |
|  | **STEP 1B.** Проверьте совместимость USB-накопителей. | USB-накопитель совместим? |
|  | **STEP 1C** Проверьте установку USB-накопителя. | USB-накопитель установлен правильно? |
| ШАГ 2. | Импорт личных данных судна. |  |
|  | **STEP 2A.** Импорт персонального файла судна. | Файл личности судна загружается должным образом? |
|  | **STEP 2B.** Импортировать файл личности судна на другой дисплей. | Файл личности судна загружается на другой дисплей ED-4? |
|  | **STEP 2C.** Импорт файла личности судна на другой USB-накопитель. | Файл личности судна загружается должным образом? |
| ШАГ 3. | Экспорт дисплея ED-4. |  |
|  | **STEP 3A.** Проверьте ED-4 дисплей. | Файлы личности судна экспортируются должным образом? |
|  | **STEP 3B.** Экспортный файл личности судна на другой дисплей. | Файл личности судна экспортируется с другого дисплея ED-4? |
|  | **STEP 3C.** Экспорт файла личности судна на другой USB-накопитель. | Файлы личности судна экспортируются должным образом? |
| ШАГ 4. | Проверьте программное обеспечение ED-4. |  |
|  | **STEP 4A.** Проверить программное обеспечение дисплея. | Файл личности судна скачать? |

### ШАГ 1. Проверьте USB-накопитель и порт.

#### ШАГ 1A. Загрузите файл личности судна на дисплей ED-4.

| **Условия:** Система поворота позволяет выключать выключатель. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Загрузите файл личности судна на дисплей ED-4. Повторно попытаться загрузить или экспортировать файл личности судна на дисплей ED-4. См. процедуру 015-044 в разделе 15. | Файл личности судна загружен? Загрузка файла личности судна исправила проблему. | Ремонт завершён. |
| Файл личности судна загружен? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте совместимость USB-накопителей.

| **Условия: **Нет. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте совместимость USB-накопителей. Проверьте, совместима ли USB-накопитель с дисплеем. См. процедуру 015-107 в разделе 15. | USB-накопитель совместим? *Да | 1С |
| USB-накопитель совместим? **NORepair: **Загрузите файл личности сосуда на совместимый USB-накопитель.[[513-015-107 — Display Software\|См. процедуру 015-107 в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 1C. Проверьте установку USB-накопителя.

| **Условия:** Система поворота позволяет выключать выключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте установку USB-накопителя. Убедитесь, что USB-накопитель установлен в порт USB дисплея должным образом. См. процедуру 015-107 в разделе 15. Если используется утилита расширения Cummins® **не**, проверьте соединение USB. Некоторые USB-разъемы являются обратимыми. | USB-накопитель установлен правильно? **Ремонт: **Пройдите к шагу 2А по вопросам импорта. Переходим к шагу 3А по вопросам экспорта. | Перейдите к соответствующим шагам устранения неполадок. |
| USB-накопитель установлен правильно? **NORepair:** Установите USB-накопитель правильно.[[513-015-044 — Managing Vessel Personalities\|См. процедуру 015-044 в разделе 15.]] | Ремонт завершён. |  |

### ШАГ 2. Импорт личных данных судна.

#### ШАГ 2A. Импорт личных данных судна.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте требования к личному файлу судна. См. процедуру 015-044 в разделе 15. Скачайте последнюю версию файла личности судна из Cummins QuickServe® Online. Замените USB-накопитель. См. процедуру 015-044 в разделе 15. Скачайте файл личности судна на дисплей ED-4 снова. | Файл личности судна загружается должным образом? **Ремонт: **Загрузка файла личности судна исправила проблему. | Ремонт завершён. |
| Файл личности судна загружается должным образом? **НЕТ** | 2В |  |

#### ШАГ 2B. Импорт файла личности судна на другой дисплей.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Импорт файла личности судна на другой дисплей. Установите USB-накопитель на другой дисплей ED-4, если он доступен. Загрузите файл личности судна на дисплей ED-4. См. процедуру 015-044 в разделе 15. Если другой ЭД-4 недоступен, переходите к следующему шагу. | Файл личности судна загружается на другой дисплей ED-4? *Да | 2C |
| Файл личности судна загружается на другой дисплей ED-4? **НЕТ** | 2C |  |

#### ШАГ 2C. Импорт файла личности судна на другой USB-накопитель.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Загрузите последнюю версию файла личности судна на другой USB-накопитель.[[513-015-044 — Managing Vessel Personalities\|См. процедуру 015-044 в разделе 15.]]Скачайте файл личности судна в неисправный ED-4 снова. | Файл личности судна загружается должным образом? *Да | Ремонт завершён. |
| Файл личности судна загружается должным образом? **НЕТ** | 4А |  |

### ШАГ 3. Экспорт дисплея ED-4.

#### ШАГ 3A. Проверьте дисплей ED-4.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей ED-4. Проверить инструкцию и экспортировать файл личности судна. См. процедуру 015-044 в разделе 15. | Файлы личности судна экспортируются должным образом? *Да | Ремонт завершён. |
| Файлы личности судна экспортируются должным образом? **НЕТ** | 3B |  |

#### ШАГ 3B. Экспортировать файл личности судна на другой дисплей.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Экспортировать файл личности судна на другой дисплей. Установите USB-накопитель на другой дисплей ED-4, если он доступен. См. процедуру 015-044 в разделе 15. Если другой ЭД-4 недоступен, переходите к следующему шагу. | Экспорт личных файлов судна с другого дисплея ED-4? *Да | 3C |
| Экспорт личных файлов судна с другого дисплея ED-4? **НЕТ** | 3C |  |

#### ШАГ 3C. Экспорт файла личности судна на другой USB-накопитель.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Экспорт файла личности судна на другой USB-накопитель. Вывозить файл личности судна из неисправного дисплея ED-4 снова. Если другой ЭД-4 недоступен, переходите к следующему шагу.[[513-015-044 — Managing Vessel Personalities\|См. процедуру 015-044 в разделе 15.]] | Файлы личности судна экспортируются должным образом? **Ремонт: **Загрузка файла личности судна исправила проблему. | Ремонт завершён. |
| Файлы личности судна экспортируются должным образом? **НЕТ** | 4А |  |

### ШАГ 4. Проверьте программное обеспечение ED-4.

#### ШАГ 4A. Проверьте программное обеспечение дисплея.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте программное обеспечение дисплея. Загрузите новейшее программное обеспечение на неисправный дисплей ED-4. См. процедуру 015-107 в разделе 15. Скачайте файл личности судна в неисправный дисплей ED-4 снова. См. процедуру 015-044 в разделе 15. | Файл личности судна скачать? **YESRepair:** Загрузка программного обеспечения для отображения исправила проблему. | Ремонт завершён. |
| Файл личности судна скачать? **NORepair:** Заменить дисплей ED-4.[[513-015-035 — Display(s) and Instrumentation\|См. процедуру 015-035 в разделе 15.]] | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Vessel personality file will **not** download into the display.
>
> - Vessel personality file will **not** export from the display.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot vessel personality file download and export issues. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible causes include:
>
> - Incompatible universal serial bus (USB) stick
>
> - USB stick **not** plugged in correctly
>
> - Vessel personality file corrupted.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check USB stick and port. |  |
> |  | **STEP 1A.** Check vessel personality file. | Vessel personality file downloaded? |
> |  | **STEP 1B.** Check USB stick compatibility. | USB stick compatible? |
> |  | **STEP 1C.** Check the USB stick installation. | USB stick installed properly? |
> | STEP 2. | Importing vessel personality file. |  |
> |  | **STEP 2A.** Importing vessel personality file. | Vessel personality file download properly? |
> |  | **STEP 2B.** Import vessel personality file to another display. | Vessel personality file download into the other ED-4 display? |
> |  | **STEP 2C.** Importing vessel personality file to another USB stick. | Vessel personality file download properly? |
> | STEP 3. | Exporting the ED-4 display. |  |
> |  | **STEP 3A.** Check ED-4 display. | Vessel personality file export properly? |
> |  | **STEP 3B.** Export vessel personality file to another display. | Vessel personality file export from the other ED-4 display? |
> |  | **STEP 3C.** Exporting vessel personality file to another USB stick. | Vessel personality file export properly? |
> | STEP 4. | Check the ED-4 display software. |  |
> |  | **STEP 4A.** Check display software. | Vessel personality file download? |
>
> ### STEP 1. Check USB stick and port.
>
> #### STEP 1A. Download the vessel personality file to the ED-4 display.
>
> | **Conditions:** Turn system enable switch OFF. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Download the vessel personality file to the ED-4 display. Re-Attempt to download or export the vessel personality file to the ED-4 display. Refer to Procedure 015-044 in Section 15. | Vessel personality file downloaded? **YESRepair:** The download of vessel personality file has corrected the issue. | Repair complete. |
> | Vessel personality file downloaded? **NO** | 1B |  |
>
> #### STEP 1B. Check USB stick compatibility.
>
> | **Conditions:** None. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check USB stick compatibility. Verify the USB stick is compatible with the display. Refer to Procedure 015-107 in Section 15. | USB stick compatible? **YES** | 1C |
> | USB stick compatible? **NORepair:** Download the vessel personality file to a compatible USB stick. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Repair complete. |  |
>
> #### STEP 1C. Check the USB stick installation.
>
> | **Conditions:** Turn system enable switch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the USB stick installation. Verify the USB stick is installed in the display USB port properly. Refer to Procedure 015-107 in Section 15. If a Cummins® extension harness is **not** being used, verify USB connection. Some USB connectors are reversible. | USB stick installed properly? **YESRepair:** Skip to Step 2A for import issues. Skip to Step 3A for export issues. | Go to the appropriate troubleshooting steps. |
> | USB stick installed properly? **NORepair:** Install USB stick properly. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Repair complete. |  |
>
> ### STEP 2. Importing the vessel personality file.
>
> #### STEP 2A. Importing the vessel personality file.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check vessel personality file requirements. Refer to Procedure 015-044 in Section 15. Download latest version of the vessel personality file from Cummins QuickServe® Online. Replace to the USB stick. Refer to Procedure 015-044 in Section 15. Download the vessel personality file to the ED-4 display again. | Vessel personality file download properly? **YESRepair:** The download of the vessel personality file has corrected the issue. | Repair complete. |
> | Vessel personality file download properly? **NO** | 2B |  |
>
> #### STEP 2B. Import vessel personality file to another display.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Import vessel personality file to another display. Install the USB stick in another ED-4 display, if available. Download the vessel personality file into the ED-4 display. Refer to Procedure 015-044 in Section 15. If another ED-4 is **not** available, proceed to the next step. | Vessel personality file download into the other ED-4 display? **YES** | 2C |
> | Vessel personality file download into the other ED-4 display? **NO** | 2C |  |
>
> #### STEP 2C. Importing the vessel personality file to another USB stick.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Download the latest version of the vessel personality file to another USB stick. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] Download the vessel personality file to the malfunctioning ED-4 again. | Vessel personality file download properly? **YES** | Repair complete. |
> | Vessel personality file download properly? **NO** | 4A |  |
>
> ### STEP 3. Exporting the ED-4 display.
>
> #### STEP 3A. Check ED-4 display.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check ED-4 display. Verify instruction and export the vessel personality file. Refer to Procedure 015-044 in Section 15. | Vessel personality file export properly? **YES** | Repair complete. |
> | Vessel personality file export properly? **NO** | 3B |  |
>
> #### STEP 3B. Export vessel personality file to another display.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Export vessel personality file to another display. Install the USB stick in another ED-4 display, if available. Refer to Procedure 015-044 in Section 15. If another ED-4 is **not** available, proceed to the next step. | Vessel personality file export from other ED-4 display? **YES** | 3C |
> | Vessel personality file export from other ED-4 display? **NO** | 3C |  |
>
> #### STEP 3C. Exporting vessel personality file to another USB stick.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Exporting vessel personality file to another USB stick. Export the vessel personality file from the malfunctioning ED-4 display again. If another ED-4 is **not** available, proceed to the next step. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Vessel personality file export properly? **YESRepair:** The download of the vessel personality file has corrected the issue. | Repair complete. |
> | Vessel personality file export properly? **NO** | 4A |  |
>
> ### STEP 4. Check the ED-4 display software.
>
> #### STEP 4A. Check the display software.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the display software. Download the latest software to the malfunctioning ED-4 display. Refer to Procedure 015-107 in Section 15. Download the vessel personality file into the malfunctioning ED-4 display again. Refer to Procedure 015-044 in Section 15. | Vessel personality file download? **YESRepair:** The download of display software has corrected the issue. | Repair complete. |
> | Vessel personality file download? **NORepair:** Replace the ED-4 display. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035 in Section 15.]] | Repair complete. |  |
