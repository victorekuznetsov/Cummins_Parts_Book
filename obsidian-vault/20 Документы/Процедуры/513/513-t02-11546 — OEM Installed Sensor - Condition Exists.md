---
type: "Процедура"
doc: "513-t02-11546"
title_en: "OEM Installed Sensor - Condition Exists"
modified: "2020-08-05"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-11546.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-11546.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# OEM Installed Sensor - Condition Exists

> [!abstract] Процедура · `513-t02-11546`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2020-08-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-11546.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-11546.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Код сигнализации датчика оригинального производителя оборудования (OEM), отображаемый на экране ED-4.

- Значение параметра датчика OEM превышает или ниже предела, определенного в файле личности судна ED-4 OEM.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения проблем с отображением данных. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Проверьте, правильно ли файл личности судна загружается на дисплее.[[513-015-044 — Managing Vessel Personalities|См. процедуру 015-044]]В разделе 15.

Эта сигнализация датчика OEM активируется, когда вход от датчика OEM превышает предел, определенный в файле личности сосуда, определенном для потребностей OEM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте код сигнализации датчика OEM. |  |
|  | **STEP 1A.** Проверить сигнализацию датчика OEM. | Активные или неактивные подсчеты сигнализации OEM-датчика. |

### ШАГ 1. Проверьте сигнализацию OEM-сенсора.

#### ШАГ 1A. Проверьте сигнализацию OEM-сенсора.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте неактивный код тревоги. Используйте экран ED-4 Advanced Fault для показаний кодов сигнализации. | Активный или неактивный статус сигнала тревоги OEM-датчика? **Ремонт:** Предел был превышен для входных данных, поставляемых OEM. См. руководство по обслуживанию OEM или руководство по ремонту. | Перейдите в руководство по обслуживанию OEM. |
| Активный или неактивный счетчик состояния сигнализации OEM-сенсора? **НЕТ** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Original Equipment Manufacturer (OEM) Sensor alarm code displayed on ED-4 screen.
>
> - OEM sensor parameter value exceeds over or under limit defined in ED-4 Vessel Personality File by the OEM.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot display data issues. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Verify correct vessel personality file is downloaded in the display. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044]] in Section 15.
>
> This OEM Sensor Alarm is activated when the input from the OEM sensor exceeds the limit defined in the vessel personality file defined for the OEM needs.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the OEM Sensor Alarm Code. |  |
> |  | **STEP 1A.** Check for OEM Sensor Alarm. | Active or inactive counts of OEM Sensor Alarm. |
>
> ### STEP 1. Check the OEM Sensor Alarm.
>
> #### STEP 1A. Check for OEM Sensor Alarm.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an inactive alarm code. Use ED-4 Advanced Fault screen to read the alarm codes. | Active or inactive status of OEM Sensor Alarm? **YESRepair:** The limit has been exceeded for the OEM supplied input. Refer to the OEM service manual or repair manual. | Go to the OEM service manual. |
> | Active or inactive counts status of OEM Sensor Alarm ? **NO** | Repair complete. |  |
