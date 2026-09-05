---
aliases:
  - "Неверная индикация неисправности"
type: "Процедура"
doc: "513-t02-1015"
title_en: "Incorrect Fault Indication"
title_ru: "Неверная индикация неисправности"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1015.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1015.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Incorrect Fault Indication
**Неверная индикация неисправности**

> [!abstract] Процедура · `513-t02-1015`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1015.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1015.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Неправильная ошибка отображается на экране ED-4.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения проблем с программным обеспечением для отображения ошибок. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Возможные причины:

- Неправильный файл личности судна

- Файл личности судна установлен неправильно.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте файл личности судна. |  |
|  | **STEP 1A.** Проверить файл личности судна. | Является ли файл с личными данными судна правильным? |
| ШАГ 2. | Проверьте калибровку модуля управления двигателем (ECM). |  |
|  | **STEP 2A.** Проверить калибровку ECM. | Правильно ли настроена калибровка ECM? |
|  | **STEP 2B.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |

### ШАГ 1. Проверьте файл личности судна.

#### ШАГ 1A. Проверьте файл личности судна.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте правильность загрузки файла Vessel Personality File на дисплее.[[513-015-044 — Managing Vessel Personalities\|См. процедуру 015-044 в разделе 15.]] | Является ли файл с личными данными судна правильным? *Да | 2А |
| Является ли файл с личными данными судна правильным? **NORepair:** Скачать правильный файл личности судна на дисплей с веб-страницы Cummins® QuickServe® On-line.[[513-015-044 — Managing Vessel Personalities\|См. процедуру 015-044 в разделе 15.]] | Ремонт завершён. |  |

### ШАГ 2. Проверьте калибровку ECM.

#### ШАГ 2A. Проверьте калибровку ECM.

| **Условия: **Включите включение. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Определите, были ли компоненты правильно настроены в ECM. | Правильно ли настроена калибровка ECM? *Да | 2В |
| Правильно ли настроена калибровка ECM? **NORepair: **Включите соответствующие компоненты для мультиплексирования и убедитесь, что адреса источника SIM для каждого компонента верны. | Ремонт завершён. |  |

#### ШАГ 2B. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? Запросить инженера по морским приложениям Cummins® на месте. | Ремонт завершён. |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM. Справочная процедура 019-032 в разделе 19 соответствующего руководства по эксплуатации двигателя. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Incorrect fault displayed on ED-4 screen.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot Fault Display Software issues. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible causes are:
>
> - Incorrect Vessel Personality File
>
> - Vessel Personality File setup improperly.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the Vessel Personality File. |  |
> |  | **STEP 1A.** Check Vessel Personality File. | Is Vessel Personality File correct? |
> | STEP 2. | Check the engine control module (ECM) calibration. |  |
> |  | **STEP 2A.** Check the ECM calibration. | ECM calibration setup properly? |
> |  | **STEP 2B.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
>
> ### STEP 1. Check the Vessel Personality File.
>
> #### STEP 1A. Check Vessel Personality File.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify correct Vessel Personality File is downloaded in the display. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Is Vessel Personality File correct? **YES** | 2A |
> | Is Vessel Personality File correct? **NORepair:** Download correct Vessel Personality File to the display from Cummins® QuickServe® On-line webpage. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Repair complete. |  |
>
> ### STEP 2. Check the ECM calibration.
>
> #### STEP 2A. Check the ECM calibration.
>
> | **Conditions:** Turn enable switch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Determine if components have been configured properly in the ECM. | ECM calibration setup properly? **YES** | 2B |
> | ECM calibration setup properly? **NORepair:** Enable the proper components for multiplexing and make sure the SIM source addresses for each component are correct. | Repair complete. |  |
>
> #### STEP 2B. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YESRepair:** Request a Cummins® Marine Application Engineer on site. | Repair complete. |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. Reference Procedure 019-032 in Section 19 of the appropriate engine service manual. | Repair complete. |  |
