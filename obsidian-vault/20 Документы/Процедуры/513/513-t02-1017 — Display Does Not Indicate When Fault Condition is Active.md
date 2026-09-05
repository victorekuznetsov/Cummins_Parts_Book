---
type: "Процедура"
doc: "513-t02-1017"
title_en: "Display Does Not Indicate When Fault Condition is Active"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1017.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1017.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Display Does Not Indicate When Fault Condition is Active

> [!abstract] Процедура · `513-t02-1017`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1017.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1017.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Неисправность или код сигнализации не отображается на экране ED-4 при наличии неисправности.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения проблем с дисплеем ошибок. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Возможные причины:

- Неправильный файл личности судна

- Файлы Vessel Personality File установлены неправильно

- Неправильная калибровка двигателя.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте вину. |  |
|  | **СТЭП 1А.** Проверьте дисплей. | Код неисправности или сигнал тревоги заранее экран тревоги? |
|  | **STEP 1B.** Проверьте настройку на дисплее ED-4. | Дисплей ED-4 установлен правильно? |
| ШАГ 2. | Проверьте файл личности судна. |  |
|  | **STEP 2A.** Проверьте ED-4 дисплей. | Файл личности судна правильный для этого судна? |
| ШАГ 3. | Проверьте калибровку модуля управления двигателем (ECM). |  |
|  | **STEP 3A.** Проверить калибровку ECM. | Правильно ли настроена калибровка ECM? |
|  | **STEP 3B.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |

### ШАГ 1. Проверьте вину.

#### ШАГ 1A. Проверьте дисплей.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей. Проверьте, активен ли сбой заранее, на экране сбоя. | Код неисправности или сигнал тревоги заранее экран тревоги? *Да | 1В |
| Код неисправности или сигнал тревоги заранее экран тревоги? **NORepair:** Скачать правильный файл личности судна на дисплей с веб-страницы Cummins® QuickServe® On-line.[[513-015-044 — Managing Vessel Personalities\|См. процедуру 015-044 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1B. Проверьте настройки на дисплее ED-4.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте настройки на дисплее ED-4. Проверьте, правильно ли настроен дисплей ED-4 с двигателем. См. процедуру 015-108 в разделе 15. | Дисплей ED-4 установлен правильно? *Да | 2А |
| Дисплей ED-4 установлен правильно? **NORepair:** Настройка дисплея ED-4 для этого двигателя.[[513-015-108 — Display Configuration\|См. процедуру 015-108 в разделе 15.]] | Ремонт завершён |  |

### ШАГ 2. Проверьте файл личности судна.

#### ШАГ 2A. Проверьте дисплей ED-4.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей ED-4. Проверьте правильность загрузки файла Vessel Personality File на дисплее. См. процедуру 015-044 в разделе 15. | Показатель? *Да | 3А |
| Показатель? **NORepair:** Скачать правильный файл личности судна на дисплей с веб-страницы Cummins® QuickServe® On-line.[[513-015-044 — Managing Vessel Personalities\|См. процедуру 015-044 в разделе 15.]] | Ремонт завершён |  |

### ШАГ 3. Проверьте калибровку ECM.

#### ШАГ 3A. Проверьте калибровку ECM.

| **Условия: **Включите включение. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте калибровку ECM. Определите, были ли компоненты правильно настроены в ECM. | Правильно ли настроена калибровка ECM? *Да | 3B |
| Правильно ли настроена калибровка ECM? **NORepair: **Включите соответствующие компоненты для мультиплексирования и убедитесь, что адреса источника SIM для каждого компонента верны. | Ремонт завершён |  |

#### ШАГ 3B. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, доступно ли обновление калибровки ECM. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? Запросить инженера по морским приложениям Cummins® на месте. | Ремонт завершён |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM. Справочная процедура 019-032 в разделе 19 соответствующего руководства по эксплуатации двигателя. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - No fault or alarm code displays on ED-4 screen when malfunction is present.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot Fault Display issues. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible causes are:
>
> - Incorrect Vessel Personality File
>
> - Vessel Personality File setup improperly
>
> - Incorrect engine calibration.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault. |  |
> |  | **STEP 1A.** Check the display. | Fault or alarm code in advance alarm screen? |
> |  | **STEP 1B.** Check the setup in the ED-4 display. | ED-4 display set up properly? |
> | STEP 2. | Check the Vessel Personality File. |  |
> |  | **STEP 2A.** Check ED-4 display. | Vessel Personality File correct for this vessel? |
> | STEP 3. | Check the engine control module (ECM) calibration. |  |
> |  | **STEP 3A.** Check the ECM calibration. | ECM calibration setup properly? |
> |  | **STEP 3B.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
>
> ### STEP 1. Check the fault.
>
> #### STEP 1A. Check the display.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the display. Check if fault is active in advance fault screen. | Fault or alarm code in advance alarm screen? **YES** | 1B |
> | Fault or alarm code in advance alarm screen? **NORepair:** Download correct Vessel Personality File to the display from Cummins® QuickServe® On-line webpage. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Repair complete |  |
>
> #### STEP 1B. Check the setup in the ED-4 display.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the setup in the ED-4 display. Verify ED-4 display is properly configured with the engine. Refer to Procedure 015-108 in Section 15. | ED-4 display setup properly? **YES** | 2A |
> | ED-4 display setup properly? **NORepair:** Configure the ED-4 display properly for this engine. [[513-015-108 — Display Configuration\|Refer to Procedure 015-108 in Section 15.]] | Repair complete |  |
>
> ### STEP 2. Check the Vessel Personality File.
>
> #### STEP 2A. Check ED-4 display.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check ED-4 display. Verify correct Vessel Personality File is downloaded in the display. Refer to Procedure 015-044 in Section 15. | Indicator on? **YES** | 3A |
> | Indicator on? **NORepair:** Download correct Vessel Personality File to the display from Cummins® QuickServe® On-line webpage. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Repair complete |  |
>
> ### STEP 3. Check the ECM calibration.
>
> #### STEP 3A. Check the ECM calibration.
>
> | **Conditions:** Turn enable switch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ECM calibration. Determine if components have been configured properly in the ECM. | ECM calibration setup properly? **YES** | 3B |
> | ECM calibration setup properly? **NORepair:** Enable the proper components for multiplexing and make sure the SIM source addresses for each component are correct. | Repair complete |  |
>
> #### STEP 3B. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check if an ECM calibration update is available. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YESRepair:** Request a Cummins® Marine Application Engineer on site. | Repair complete |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. Reference Procedure 019-032 in Section 19 of the appropriate engine service manual. | Repair complete |  |
