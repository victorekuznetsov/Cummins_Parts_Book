---
aliases:
  - "Пульт машинного отделения показывает неверное назначение"
type: "Процедура"
doc: "115-t02-1036"
title_en: "Engine Room Panel Indicates Incorrect Assignment"
title_ru: "Пульт машинного отделения показывает неверное назначение"
modified: "2006-06-12"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1036.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1036.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Engine Room Panel Indicates Incorrect Assignment
**Пульт машинного отделения показывает неверное назначение**

> [!abstract] Процедура · `115-t02-1036`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1036.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1036.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Удалённая панель указывает, что панель машинного отделения находится в локальном режиме.

- Локальная лампа режима **не** освещена на панели управления машинного отделения.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов панели. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте панель машинного отделения Local Start Only Button Operation |  |
|  | **STEP 1A.** Проверьте локальный запуск панели удаленного управления только лампой | Светильник подсвечивается? |
| ШАГ 2. | Проверить панель управления панелью Engine Room Panel |  |
|  | **STEP 2A.** Проверить на напряжённость панели управления | Светильник подсвечивается? |

### ШАГ 1. Проверьте панель машинного отделения Local Start Only Button Operation

#### ШАГ 1A. Проверьте локальный запуск удаленной панели только лампой

| **Условия:** Убедитесь, что выключатель питания панели машинного отделения включен и лампа освещена. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что лампа питания удаленной панели освещена. Нажмите локальный запуск только на кнопку на панели машинного отделения. Убедитесь, что на удаленной панели освещена только лампа локального запуска. | Светильник подсвечивается? *Да | 2А |
| Светильник подсвечивается? **NORepair:** См. Дистанционная панель Указывает на неправильную елку симптомов назначения. | Ремонт завершён. |  |

### ШАГ 2. Проверить панель управления панелью Engine Room Panel

#### ШАГ 2A. Проверьте напряжение на панели управления

| **Условия:** Нажмите локальный запуск только на кнопку на панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте панель машинного отделения локальной пусковой только лампы. | Светильник подсвечивается? *Да | Ремонт завершён. |
| Светильник подсвечивается? **NORepair:** Заменить панель управления машинного отделения. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The remote panel indicates the engine room panel is in the local mode.
>
> - The local mode lamp is **not** illuminated on the engine room control panel.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot panel symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Engine Room Panel Local Start Only Button Operation |  |
> |  | **STEP 1A.** Check Remote Panel Local Start Only Lamp | Lamp illuminated? |
> | STEP 2. | Check Engine Room Panel Control Panel |  |
> |  | **STEP 2A.** Check for Voltage to Control Panel | Lamp illuminated? |
>
> ### STEP 1. Check Engine Room Panel Local Start Only Button Operation
>
> #### STEP 1A. Check Remote Panel Local Start Only Lamp
>
> | **Conditions:** Verify that engine room panel power switch is on and lamp illuminated. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify that remote panel power lamp is illuminated. Press the local start only on button on the engine room panel. Verify that the local start only lamp is illuminated on the remote panel. | Lamp illuminated? **YES** | 2A |
> | Lamp illuminated? **NORepair:** Refer to Remote Panel Indicates Incorrect Assignment symptom tree. | Repair complete. |  |
>
> ### STEP 2. Check Engine Room Panel Control Panel
>
> #### STEP 2A. Check for Voltage to Control Panel
>
> | **Conditions:** Press local start only on button on the engine room panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel local start only lamp. | Lamp illuminated? **YES** | Repair complete. |
> | Lamp illuminated? **NORepair:** Replace the engine room panel control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
