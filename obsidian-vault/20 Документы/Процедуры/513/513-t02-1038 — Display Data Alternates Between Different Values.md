---
type: "Процедура"
doc: "513-t02-1038"
title_en: "Display Data Alternates Between Different Values"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1038.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1038.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Display Data Alternates Between Different Values

> [!abstract] Процедура · `513-t02-1038`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1038.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1038.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Параметры данных неоднократно переключаются между различными значениями на дисплее.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неполадок в устройствах управления реле. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Возможные причины:

- Неправильный файл личности судна

- ED-4 дисплеи установлены неправильно.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте дисплей ED-4. |  |
|  | **STEP 1A.** Проверьте конфигурацию дисплея ED-4. | Источники 1 и 2 J1939 установлены правильно? |
|  | **STEP 1B.** Проверить файл личности судна. | Файл личности судна правильный? |

### ШАГ 1. Проверьте дисплей ED-4.

#### ШАГ 1A. Проверьте конфигурацию дисплея ED-4.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить источник двигателя J1939. Перейдите в конфигурацию в меню на дисплее ED-4. Проверьте настройки источника 1 и 2 двигателя J1939. См. процедуру 015-108 в разделе 15. | Источники 1 и 2 J1939 установлены правильно? *Да | 1В |
| Источники 1 и 2 J1939 установлены правильно? **NORepair:** Настройка дисплея ED-4.[[513-015-108 — Display Configuration\|См. процедуру 015-108 в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 1B. Проверьте файл личности судна.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление. Проверьте, правильно ли файл личности судна загружается на дисплее. См. процедуру 015-044 в разделе 15. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Файл личности судна правильный? Запросить инженера-исполнителя Cummins® Marine на месте. | Ремонт завершён. |
| Файл личности судна правильный? **NORepair:** Загрузите правильный файл личности судна на дисплей для Cummins QuickServe® Online.[[513-015-035 — Display(s) and Instrumentation\|См. процедуру 015-035 в разделе 15.]] | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Data parameters repeatedly switch between different values on the display.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot accessory relay control devices. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible causes are:
>
> - Incorrect vessel personality file
>
> - ED-4 display setup improperly.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the ED-4 display. |  |
> |  | **STEP 1A.** Check ED-4 display configuration. | J1939 source 1 and 2 set properly? |
> |  | **STEP 1B.** Check vessel personality file. | Vessel personality file correct? |
>
> ### STEP 1. Check the ED-4 display.
>
> #### STEP 1A. Check ED-4 display configuration.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify engine J1939 source. Go to the configuration in the menu in the ED-4 display. Verify engine J1939 source 1 and 2 settings. Refer to Procedure 015-108 in Section 15. | J1939 source 1 and 2 set properly? **YES** | 1B |
> | J1939 source 1 and 2 set properly? **NORepair:** Configure the ED-4 display properly. [[513-015-108 — Display Configuration\|Refer to Procedure 015-108 in Section 15.]] | Repair complete. |  |
>
> #### STEP 1B. Check the vessel personality file.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance. Verify correct vessel personality file is downloaded in the display. Refer to Procedure 015-044 in Section 15. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Vessel personality file correct? **YESRepair:** Request a Cummins® Marine application engineer on site. | Repair complete. |
> | Vessel personality file correct? **NORepair:** Download correct vessel personality file to the display for Cummins QuickServe® Online. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035 in Section 15.]] | Repair complete. |  |
