---
type: "Процедура"
doc: "178-t05-234"
title_en: "FAULT CODE 234 - Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Most Severe Level"
modified: "2019-08-22"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326169"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-234.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-234.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/178"
  - "перевод/машинный"
---

# FAULT CODE 234 - Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Most Severe Level

> [!abstract] Процедура · `178-t05-234`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326169 — QSB6.7 CM2150 B109 Fault Code Troubleshooting Manual|4326169]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-08-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-234.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-234.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!danger] ОПАСНО
> Не используйте дизельный двигатель там, где есть или могут быть совместимые капоры. Эти пары могут всасываться через систему воздухозаборника и вызывать ускорение и превышение скорости двигателя, что может привести к пожару, взрыву и обширному имущественному ущербу. Доступны многочисленные устройства безопасности, такие как устройства отключения воздухозаборника, чтобы минимизировать риск превышения скорости, когда двигатель из-за его применения может работать в горючей среде, например, из-за разлива топлива или утечки газа. Помни, Камминс Инк. Вы не можете знать, как использовать ваш двигатель. Владелец и оператор оборудования отвечают за безопасное функционирование в условиях эксплуатации. УСЛУЖИТЬ ВАШИ КОММИНЫ ® УДАЛЕННЫЙ РЕПЕРАТОРНЫЙ ЛИЦАЦИЯ ДЛЯ ДРУГИХ ИНФОРМАЦИЙ.

> [!warning] ОСТОРОЖНО
> Если скорость двигателя остается выше 3500 об/мин, двигатель должен быть немедленно выключен или может произойти повреждение двигателя.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить новый блок управления двигателем (ЭБУ), перед его заменой разберитесь со всеми остальными активными кодами неисправностей.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Определите причину превышения скорости. |  |
|  | **СТЭП 1А** Проверить наличие надлежащих условий эксплуатации. | Двигаемся вниз по склону? |
|  | **СТЭП 1В** Проверить наличие альтернативного источника топлива. | Альтернативный источник топлива? |
|  | **STEP 1C.** Проверьте обороты двигателя с помощью электронного инструментария INSITETM. | Корректировка оборотов в минуту (об/мин) показаний? |
|  | **STEP 1D.** Проверьте наличие активной неисправности при низких оборотах двигателя. | Неактивный код ошибки при низком обороте в минуту? |
|  | **ШАГ 1Е.** Испытание транспортного средства. | Код 234 неактивен? |
| ШАГ 2. | Проверьте калибровку ECM и четкие коды неисправностей. |  |
|  | **STEP 2A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 2B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Определите причину превышения скорости.

#### ШАГ 1A. Проверьте надлежащие условия эксплуатации.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте надлежащие условия эксплуатации. Проверьте, двигался ли двигатель вниз по склону, когда ошибка была зарегистрирована. | Двигаемся вниз по склону? *Да | 1В |
| Двигаемся вниз по склону? **NORepair:** Проверка повреждений двигателя. Электроника в порядке. Проверьте базовый двигатель на предмет повреждения из-за превышения скорости. | 2А |  |

#### ШАГ 1B. Проверьте альтернативный источник топлива.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте альтернативный источник топлива. Проверьте, не сообщил ли водитель о контролируемом топливом событии, когда двигатель быстро разгонялся до красной области тахометра двигателя. | Альтернативный источник топлива? **YESRepair: **Найдите любые альтернативные источники топлива, такие как работа двигателя вблизи легковоспламеняющихся паров, продувные уплотнения турбокомпрессора и т.д. | 2А |
| Альтернативный источник топлива? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте обороты двигателя с помощью электронного инструментария обслуживания INSITETM.

| **Условия:** Включить переключатель зажигания. Двигатель работает. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте обороты двигателя с помощью электронного инструментария обслуживания INSITETM. Сравните показания скорости двигателя на электронном сервисном оборудовании INSITETM с механическим тахометром или тахометром тире. | Корректировка оборотов в минуту (об/мин) показаний? *Да | 1D |
| Корректировка оборотов в минуту (об/мин) показаний? **NORepair:** Осмотрите датчик скорости коленчатого вала и датчик положения двигателя вала, как указано в Кодах 689 и 778 по умолчанию. | Устранение неисправностей 689 и 778. |  |

#### ШАГ 1D. Проверьте наличие активной неисправности при низких оборотах двигателя.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активный код 234 ошибки, когда двигатель работает **не **выше высокой скорости холостого хода. - | Неактивный код ошибки при низком обороте в минуту? *Да | 1Е |
| Неактивный код ошибки при низком обороте в минуту? Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 2А |  |

#### ШАГ 1E. Испытайте автомобиль.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Испытание транспортного средства в ходе дорожного испытания или судна в морской тропе для определения того, присутствует ли еще состояние превышения скорости. - | Код 234 неактивен? *Да | 2А |
| Код 234 неактивен? **NORepair:** Возврат к шагам устранения неполадок или обращение в авторизованное место ремонта Cummins®, если все шаги были завершены и проверены повторно. | 1А |  |

### ШАГ 2. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 2A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 2В |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]] | 2В |  |

#### ШАГ 2B. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да | Ремонт завершён. |
| Код неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

## Связанные процедуры

| Связанные процедуры |  |  |  |
|---|---|---|---|
| Название процедуры | Процедурный номер | Модельный сервис | Номер бюллетеня |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL8.9 CM2880 L112 | 4358493 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL9.5 CM2150 SN | 4310608 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB3.9 CM2220 B107 | 4310792 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSNT14 CM876 N102 | 4325993 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB4.5 CM2150 B108 | 4326163 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB7 CM2880 B117 | 4358390 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG11 CM2880 G106 | 4332695 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG12 CM2880 G107 | 4332690 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG11 CM2880 G108 | 4332901 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG12 CM2880 G109 | 4332906 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF2.8 CM2880 F104 | 4332741 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF2.8 CM2880 F108 | 4332746 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF3.8 CM2880 F112 | 4383825 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB5.9 CM2880 B127 | 4383645 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSL9.3 CM2880 L113 | 4383811 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF3.8 CM2220 F116 | 4383664 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSC8.3 CM2880 C102 | 4388785 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB5.9 CM2880 B139 | 4388870 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB3.9 CM2880 B138 | 5411050 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISD6.7 CM2880 D101 | 5411372 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF2.8 CM2220 F129 | 5411325 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF4.5 CM2220 F123 | 5411320 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSG12 CM2880 G112 | 4388731 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF3.8 CM2220 F134B | 5504165 |
| Электронный блок управления двигателем | См. процедуру 019-031 | Z14 M2670 Z103B | 5504577 |
| Электронный блок управления двигателем | См. процедуру 019-031 | D6.7 CM2670 D102B | 5504515 |
| Электронный блок управления двигателем | См. процедуру 019-031 | B6.2 CM2670 B156B | 5579510 |
| Электронный блок управления двигателем | См. процедуру 019-031 | X12 CM2670 X121B | 5504455 |
| Электронный блок управления двигателем | См. процедуру 019-031 | L9 CM2670 L128B | 5504589 |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **WARNING · Опасно**
> DO NOT OPERATE A DIESEL ENGINE WHERE THERE ARE OR CAN BE COMBUSTIBLE VAPORS. These vapors can be sucked through the air intake system and cause engine acceleration and overspeeding that can result in a fire, an explosion, and extensive property damage. Numerous safety devices are available, such as air intake shutoff devices, to minimize the risk of overspeeding where an engine, due to its application, might operate in a combustible environment, such as due to a fuel spill or gas leak. Remember, Cummins Inc. has no way of knowing the use you have for your engine. THE EQUIPMENT OWNER AND OPERATOR ARE RESPONSIBLE FOR SAFE OPERATION IN A HOSTILE ENVIRONMENT. CONSULT YOUR Cummins® AUTHORIZED REPAIR LOCATION FOR FURTHER INFORMATION.
>
> **CAUTION · Осторожно**
> If the engine speed stays above 3500 rpm, the engine must be shut off immediately or engine damage can occur.
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Identify the reason for the overspeed. |  |
> |  | **STEP 1A.** Check for proper operating conditions. | Motoring downhill? |
> |  | **STEP 1B.** Check for an alternate fuel source. | Alternate fuel source? |
> |  | **STEP 1C.** Check the engine rpm with INSITE™ electronic service tool. | Correct revolutions per minute (rpm) reading? |
> |  | **STEP 1D.** Check for an active fault at low engine rpm. | Inactive fault code at low rpm? |
> |  | **STEP 1E.** Test the vehicle. | Fault Code 234 inactive? |
> | STEP 2. | Check ECM calibration and clear fault codes. |  |
> |  | **STEP 2A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 2B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Identify the reason for the overspeed.
>
> #### STEP 1A. Check for proper operating conditions.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for proper operating conditions. Check if the engine was motoring downhill when the fault was logged. | Motoring downhill? **YES** | 1B |
> | Motoring downhill? **NORepair:** Check for engine damage. Electronics are ok. Check the base engine for damage due to overspeed condition. | 2A |  |
>
> #### STEP 1B. Check for an alternate fuel source.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an alternate fuel source. Check if the driver reported a fuel-controlled event where the engine rapidly accelerated to the engine tachometer red area. | Alternate fuel source? **YESRepair:** Locate any alternate fuel sources, such as operating the engine near flammable vapors, blown turbocharger seals, etc. | 2A |
> | Alternate fuel source? **NO** | 1C |  |
>
> #### STEP 1C. Check the engine rpm with INSITE™ electronic service tool.
>
> | **Conditions:** Turn keyswitch ON. Engine is running. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine rpm with INSITE™ electronic service tool. Compare the engine speed reading on INSITE™ electronic service tool to a mechanical tachometer or the dash tachometer. | Correct revolutions per minute (rpm) reading? **YES** | 1D |
> | Correct revolutions per minute (rpm) reading? **NORepair:** Inspect the crankshaft engine speed sensor and camshaft engine position sensor as outlined in Fault Codes 689 and 778. | Troubleshoot Fault Codes 689 and 778. |  |
>
> #### STEP 1D. Check for an active fault at low engine rpm.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for active Fault Code 234 when the engine is **not** running above high idle speed. - | Inactive fault code at low rpm? **YES** | 1E |
> | Inactive fault code at low rpm? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 2A |  |
>
> #### STEP 1E. Test the vehicle.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Test the vehicle in a road test or the vessel in a sea trail to determine if the overspeed condition is still present. - | Fault Code 234 inactive? **YES** | 2A |
> | Fault Code 234 inactive? **NORepair:** Return to troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> ### STEP 2. Check ECM calibration and clear fault codes.
>
> #### STEP 2A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 2B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 2B |  |
>
> #### STEP 2B. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
> | Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> ## Associated Procedures
>
> | Associated Procedures |  |  |  |
> |---|---|---|---|
> | Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
> | Engine Control Module | Refer to Procedure 019-031 | ISL8.9 CM2880 L112 | 4358493 |
> | Engine Control Module | Refer to Procedure 019-031 | ISL9.5 CM2150 SN | 4310608 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB3.9 CM2220 B107 | 4310792 |
> | Engine Control Module | Refer to Procedure 019-031 | QSNT14 CM876 N102 | 4325993 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB4.5 CM2150 B108 | 4326163 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
> | Engine Control Module | Refer to Procedure 019-031 | QSB7 CM2880 B117 | 4358390 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G106 | 4332695 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G107 | 4332690 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G108 | 4332901 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G109 | 4332906 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F104 | 4332741 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F108 | 4332746 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF3.8 CM2880 F112 | 4383825 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB5.9 CM2880 B127 | 4383645 |
> | Engine Control Module | Refer to Procedure 019-031 | QSL9.3 CM2880 L113 | 4383811 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F116 | 4383664 |
> | Engine Control Module | Refer to Procedure 019-031 | QSC8.3 CM2880 C102 | 4388785 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB5.9 CM2880 B139 | 4388870 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB3.9 CM2880 B138 | 5411050 |
> | Engine Control Module | Refer to Procedure 019-031 | ISD6.7 CM2880 D101 | 5411372 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF2.8 CM2220 F129 | 5411325 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF4.5 CM2220 F123 | 5411320 |
> | Engine Control Module | Refer to Procedure 019-031 | QSG12 CM2880 G112 | 4388731 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F134B | 5504165 |
> | Engine Control Module | Refer to Procedure 019-031 | Z14 CM2670 Z103B | 5504577 |
> | Engine Control Module | Refer to Procedure 019-031 | D6.7 CM2670 D102B | 5504515 |
> | Engine Control Module | Refer to Procedure 019-031 | B6.2 CM2670 B156B | 5579510 |
> | Engine Control Module | Refer to Procedure 019-031 | X12 CM2670 X121B | 5504455 |
> | Engine Control Module | Refer to Procedure 019-031 | L9 CM2670 L128B | 5504589 |
