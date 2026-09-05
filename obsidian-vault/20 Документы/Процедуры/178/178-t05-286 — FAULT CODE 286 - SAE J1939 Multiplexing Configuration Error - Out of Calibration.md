---
type: "Процедура"
doc: "178-t05-286"
title_en: "FAULT CODE 286 - SAE J1939 Multiplexing Configuration Error - Out of Calibration"
modified: "2019-01-04"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326169"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-286.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-286.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/178"
  - "перевод/машинный"
---

# FAULT CODE 286 - SAE J1939 Multiplexing Configuration Error - Out of Calibration

> [!abstract] Процедура · `178-t05-286`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326169 — QSB6.7 CM2150 B109 Fault Code Troubleshooting Manual|4326169]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-01-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-286.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-286.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить наличие активного кода неисправности. | Код ошибки 286 активен? |
| ШАГ 2. | Проверьте электронный блок управления транспортного средства производителя оригинального оборудования (OEM) и модуль управления двигателем (ECM) для правильной конфигурации мультиплексирования. |  |
|  | **STEP 2A.** Определить, какие компоненты мультиплексного блока управления транспортным средством (коммутаторы, ускорители или датчики) включены для мультиплексирования через шину данных J1939 CAN в ECM и сравнить с конфигурацией ECM. | Соответствует ли конфигурация мультиплексирования ECM конфигурации мультиплексирования электронного блока управления OEM-производителя транспортного средства? |
| ШАГ 3. | Проверьте калибровку ECM и четкие коды неисправностей. |  |
|  | **STEP 3A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 3B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 286 активен? *Да | 2А |
| Код ошибки 286 активен? **NORepair:** Выявлена проблема с OEM-производителями. Свяжитесь с OEM для дальнейших инструкций по ремонту. До сих пор существует возможность наличия электронного блока управления транспортным средством, установки электронного блока управления транспортным средством или электронного блока управления транспортным средством для проблемы подключения шины данных CAN. | Ремонт завершён. |  |

### ШАГ 2. Проверьте электронный блок управления транспортного средства производителя оригинального оборудования (OEM) и модуль управления двигателем (ECM) для правильной конфигурации мультиплексирования.

#### ШАГ 2A. Определить, какие компоненты мультиплексного блока управления транспортным средством (коммутаторы, ускорители или датчики) включены для мультиплексирования через шину данных J1939 CAN в ECM и сравнить с конфигурацией ECM.

| **Условия:** Определить надлежащий компонент конфигурации мультиплексирования электронного блока управления OEM-автомобиля и адреса источника электронного блока управления OEM-автомобиля из соответствующей информации OEM-производителя или из сохраненного изображения работы. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте конфигурацию мультиплексирования. Используйте инструмент электронного сервиса INSITETM SAE J1939 Multiplexed Fault Data, расположенный в данных Advanced ECM, чтобы определить, какой компонент вызывает неисправность. Если в колонке состояния указано "Активный" для мультиплексированного компонента, проверьте, что мультиплексированный компонент ECM включает и адреса источников соответствуют опциям мультиплексированного компонента электронного блока управления OEM-производителя транспортного средства и адресам источников. Эти компоненты можно найти в разделе SAE J1939 Multiplexing in Features and Parameters. Используйте следующую информацию для конкретной мультиплексной конфигурации OEM. См. Service Bulletin, Multiplexing Troubleshooting, Bulletin[[4021378 — Multiplexing Troubleshooting\|4021378]]. | Соответствует ли конфигурация мультиплексирования ECM конфигурации мультиплексирования электронного блока управления OEM-производителя транспортного средства? **Ремонт: **Выявлена проблема с OEM-производителями. Свяжитесь с OEM для дальнейших инструкций по ремонту. До сих пор существует возможность наличия электронного блока управления транспортным средством, установки электронного блока управления транспортным средством или электронного блока управления транспортным средством для проблемы подключения шины данных CAN. | 3А |
| Соответствует ли конфигурация мультиплексирования ECM конфигурации мультиплексирования электронного блока управления OEM-производителя транспортного средства? **NORepair: **Неправильная установка была обнаружена в Cummins® ECM. Включите соответствующие компоненты для мультиплексирования в применимом приложении OEM и убедитесь, что адреса источника электронного блока управления OEM-производителя для каждого компонента являются правильными. | 3А |  |

### ШАГ 3. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 3A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе Калибровочная информация идентификатора системы и таблички данных в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 3B |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]] | 3B |  |

#### ШАГ 3B. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да | Ремонт завершён. |
| Код неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for an active fault code. | Fault Code 286 active? |
> | STEP 2. | Check the Original Equipment Manufacturer (OEM) vehicle electronic control unit and Engine Control Module (ECM) for proper multiplexing configuration. |  |
> |  | **STEP 2A.** Determine which vehicle electronic control unit multiplexed components (switches, accelerators, or sensors) are enabled for multiplexing over the J1939 data link to the ECM and compare to the ECM configuration. | Does the ECM multiplexing configuration match the OEM vehicle electronic control unit multiplexing configuration? |
> | STEP 3. | Check ECM calibration and clear fault codes. |  |
> |  | **STEP 3A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 3B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for an active fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 286 active? **YES** | 2A |
> | Fault Code 286 active? **NORepair:** An OEM issue has been detected. Contact the OEM for further repair instructions. It is still possible that there is a vehicle electronic control unit, vehicle electronic control unit setup, or vehicle electronic control unit to data link connection issue. | Repair complete. |  |
>
> ### STEP 2. Check the Original Equipment Manufacturer (OEM) vehicle electronic control unit and Engine Control Module (ECM) for proper multiplexing configuration.
>
> #### STEP 2A. Determine which vehicle electronic control unit multiplexed components (switches, accelerators, or sensors) are enabled for multiplexing over the J1939 data link to the ECM and compare to the ECM configuration.
>
> | **Conditions:** Determine proper OEM vehicle electronic control unit multiplexing configuration component enables and OEM vehicle electronic control unit source addresses from the appropriate OEM information, or from a saved job image. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the multiplexing configuration. Use INSITE™ electronic service tool SAE J1939 Multiplexed Fault Data, located in Advanced ECM data, to determine which multiplexed component is causing the fault. If the status column indicates "Active" for a multiplexed component, check that the ECM multiplexed component enables and source addresses match the OEM vehicle electronic control unit multiplexed component enables and source addresses. These components can be found under SAE J1939 Multiplexing in Features and Parameters. Use the following for OEM specific multiplexing configuration information. Refer to Service Bulletin, Multiplexing Troubleshooting, Bulletin [[4021378 — Multiplexing Troubleshooting\|4021378]]. | Does the ECM multiplexing configuration match the OEM vehicle electronic control unit multiplexing configuration? **YESRepair:** An OEM issue has been detected. Contact the OEM for further repair instructions. It is still possible that there is a vehicle electronic control unit, vehicle electronic control unit setup, or vehicle electronic control unit to data link connection issue. | 3A |
> | Does the ECM multiplexing configuration match the OEM vehicle electronic control unit multiplexing configuration? **NORepair:** An incorrect setup has been detected in the Cummins® ECM. Enable the proper components for multiplexing on the applicable OEM application and make sure the OEM vehicle electronic control unit source addresses for each component are correct. | 3A |  |
>
> ### STEP 3. Check ECM calibration and clear fault codes.
>
> #### STEP 3A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Data Plate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 3B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 3B |  |
>
> #### STEP 3B. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
> | Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
