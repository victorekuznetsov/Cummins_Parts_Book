---
aliases:
  - "Код 351 — питание форсунок — неисправное устройство"
type: "Процедура"
doc: "178-t05-351"
title_en: "FAULT CODE 351 - Injector Power Supply - Bad Intelligent Device or Component"
title_ru: "Код 351 — питание форсунок — неисправное устройство"
modified: "2021-11-03"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326169"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-351.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-351.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/178"
  - "перевод/машинный"
---

# FAULT CODE 351 - Injector Power Supply - Bad Intelligent Device or Component
**Код 351 — питание форсунок — неисправное устройство**

> [!abstract] Процедура · `178-t05-351`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326169 — QSB6.7 CM2150 B109 Fault Code Troubleshooting Manual|4326169]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-11-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-351.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-351.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить новый блок управления двигателем (ЭБУ), перед его заменой разберитесь со всеми остальными активными кодами неисправностей.

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3164133 - пробный щуп типа пробки DeutschTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Код 441 неактивен или неактивен? |
|  | **СТЭП 1В.** Управляйте двигателем. | Запуск двигателя? |
|  | **СТЭП 1С.** Прочитайте коды неисправностей. | Код ошибки 351 активен? |
| ШАГ 2. | Проверьте электропитание ECM. |  |
|  | **STEP 2A.** Проверить разъемы и предохранители источника питания ECM. | Грязные или поврежденные контакты? |
|  | **ШАГ 2В.** Проверить наличие открытой цепи. | Менее 0,5 Ом? |
|  | **STEP 2C** Проверить наличие открытой цепи в цепи электропитания ECM. | Менее 10 Ом? |
| ШАГ 3. | Проверить наличие этого кода неисправности. |  |
|  | **STEP 3A.** Управляйте двигателем и определяйте, существует ли условие кода неисправности. | Код 351 ошибки возникает во время работы двигателя. |
| ШАГ 4. | Проверьте калибровку ECM и четкие коды неисправностей. |  |
|  | **STEP 4A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 4B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 441 неактивен или неактивен? Вначале устранение неисправностей код 441. | Соответствующий код неисправности дерево |
| Код 441 неактивен или неактивен? **НЕТ** | 1В |  |

#### ШАГ 1B. Управляйте двигателем.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Управляйте двигателем. | Запуск двигателя? *Да | 1С |
| Запуск двигателя? Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 4А |  |

#### ШАГ 1C. Считайте коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Управляйте двигателем и определяйте, существует ли еще условие кода неисправности. Работайте с двигателем на высоком холостом ходу, без нагрузки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 351 активен? **Ремонт: **Возможна предельная нагрузка на аккумулятор. Убедитесь, что батареи полностью заряжены или заменены, если это необходимо. Вероятно, что незначительное состояние батареи приведет к тому, что код 351 ошибки станет активным при проворачивании двигателя. | 2А |
| Код ошибки 351 активен? **НЕТ** | 4А |  |

### ШАГ 2. Проверьте электропитание ECM.

#### ШАГ 2A. Проверить разъемы и предохранители источника питания ECM.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку ECM от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить источник питания и предохранители ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. Ремонт или замена поврежденной проводов жгута, булавок, предохранителей или разъемов. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку ECM от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерьте сопротивление между контактами ECM аккумулятора SUPPLY (+) на разъеме питания электропроводки ECM и положительными (+) контактами аккумулятора на положительном (+) соединении аккумулятора. Используйте схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 0,5 Ом? *Да | 2C |
| Менее 0,5 Ом? **NORepair:** Ремонтировать или заменить электропроводку электропитания ECM, предохранители или держатели предохранителей. Очистите подключение к терминалу батареи. См. сервисную документацию изготовителя оборудования. | 4А |  |

#### ШАГ 2C. Проверьте наличие открытой цепи в цепи электропитания ECM.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку ECM от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие открытой цепи в наземной цепи ECM. Измерьте сопротивление между отрицательными (-) штифтами батареи на разъеме питания ECM к заземлению блока двигателя. Используйте схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 3А |
| Менее 10 Ом? **NORepair:** Ремонтировать или заменить электропроводку электропитания ECM, предохранители или держатели предохранителей. Очистите подключение к терминалу батареи. См. сервисную документацию изготовителя оборудования. | 4А |  |

### ШАГ 3. Проверить наличие этого кода неисправности.

#### ШАГ 3A. Управляйте двигателем и определяйте, существует ли условие кода неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Управляйте двигателем и определяйте, существует ли еще условие кода неисправности. Работайте с двигателем на высоком холостом ходу, без нагрузки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 351 ошибки возникает во время работы двигателя. Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 4А |
| Код 351 ошибки возникает во время работы двигателя. **NORepair: **Возможна предельная нагрузка на аккумулятор. Убедитесь, что батареи полностью заряжены или заменены, если это необходимо. Вероятно, что незначительное состояние батареи приведет к тому, что код 351 ошибки станет активным при проворачивании двигателя. | 4А |  |

### ШАГ 4. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 4A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и его пересмотр с изменениями калибровки, перечисленными в истории калибровочных изменений ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код ECM и номера изменений находятся в разделе «Информация о калибровке» идентификатора системы и таблички данных в разделе «Особенности и параметры». | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 4B |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]] | 4B |  |

#### ШАГ 4B. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да | Ремонт завершён |
| Код неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

## Связанные процедуры

| Связанные процедуры |  |  |  |
|---|---|---|---|
| Название процедуры | Процедурный номер | Модельный сервис | Номер бюллетеня |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB4.5 CM2150 B108 | 4326163 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF2.8 CM2880 F104 | 4332741 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF2.8 CM2880 F108 | 4332746 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB7 CM2880 B117 | 4358390 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB3.9 CM2200 B107 | 4310792 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL9.5 CM2150 SN | 4310608 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSNT14 CM876 N102 | 4325993 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG11 CM2880 G106 | 4332695 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG11 CM2880 G108 | 4332901 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG12 CM2880 G107 | 4332690 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG12 CM2880 G109 | 4332906 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL8.9 CM2880 L112 | 4358493 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB5.9 CM2880 B127 | 4383645 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF3.8 CM2880 F112 | 4383825 |
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
| Жгут проводов двигателя | См. процедуру 019-043 | QSB4.5 CM2150 B108 | 4326163 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB7 CM2880 B117 | 4358390 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB2.8 CM2880 F104 | 4332741 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB2.8 CM2880 F108 | 4332746 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISB3.9 CM2200 B107 | 4310792 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISL9.5 CM2150 SN | 4310608 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSNT14 CM876 N102 | 4325993 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG11 CM2880 G106 | 4332695 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG11 CM2880 G108 | 4332901 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG12 CM2880 G107 | 4332690 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISG12 CM2880 G109 | 4332906 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISL8.9 CM2880 L112 | 4358493 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISB5.9 CM2880 B127 | 4383645 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSF3.8 CM2880 F112 | 4383825 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSL9.3 CM2880 L113 | 4383811 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISF3.8 CM2220 F116 | 4383664 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSC8.3 CM2880 C102 | 4388785 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB5.9 CM2880 B139 | 4388870 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSB3.9 CM2880 B138 | 5411050 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISD6.7 CM2880 D101 | 5411372 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISF2.8 CM2220 F129 | 5411325 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISF4.5 CM2220 F123 | 5411320 |
| Жгут проводов двигателя | См. процедуру 019-043 | QSG12 CM2880 G112 | 4388731 |
| Жгут проводов двигателя | См. процедуру 019-043 | ISF3.8 CM2220 F134B | 5504165 |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3164133 - male Deutsch™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Code 441 active or inactive? |
> |  | **STEP 1B.** Operate the engine. | Will the engine start? |
> |  | **STEP 1C.** Read the fault codes. | Fault Code 351 active? |
> | STEP 2. | Check the ECM power supply. |  |
> |  | **STEP 2A.** Inspect the ECM power supply connectors and fuses. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check for an open circuit. | Less than 0.5 ohms? |
> |  | **STEP 2C.** Check for an open circuit in the ECM power supply circuit. | Less than 10 ohms? |
> | STEP 3. | Validate the occurrence of this fault code. |  |
> |  | **STEP 3A.** Operate the engine and determine if fault code condition exists. | Fault Code 351 occurs during engine operation? |
> | STEP 4. | Check ECM calibration and clear fault codes. |  |
> |  | **STEP 4A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 4B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 441 active or inactive? **YESRepair:** Troubleshoot Fault Code 441 first. | Appropriate fault code troubleshooting tree |
> | Fault Code 441 active or inactive? **NO** | 1B |  |
>
> #### STEP 1B. Operate the engine.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Operate the engine. | Will the engine start? **YES** | 1C |
> | Will the engine start? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 4A |  |
>
> #### STEP 1C. Read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Operate the engine and determine whether the fault code condition still exists. Operate the engine at high idle, no load. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 351 active? **YESRepair:** A marginal battery voltage condition is possible. Make sure the batteries are fully charged or replace, if needed. It is likely that a marginal battery condition will result in Fault Code 351 becoming active at engine cranking. | 2A |
> | Fault Code 351 active? **NO** | 4A |  |
>
> ### STEP 2. Check the ECM power supply.
>
> #### STEP 2A. Inspect the ECM power supply connectors and fuses.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ECM power supply harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the ECM power supply and fuses for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Repair or replace the damaged harness, pins, fuses, or connectors. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ECM power supply harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the ECM battery SUPPLY (+) pins at the power connector of the ECM power supply harness and the battery positive (+) pins at the battery positive (+) connection. Use the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 0.5 ohms? **YES** | 2C |
> | Less than 0.5 ohms? **NORepair:** Repair or replace the ECM power supply harness, fuses, or fuse holders. Clean the battery terminal connections. See equipment manufacturer service information. | 4A |  |
>
> #### STEP 2C. Check for an open circuit in the ECM power supply circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ECM power supply harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit in the ECM ground circuit. Measure the resistance between the battery negative (-) pins at the ECM power supply connector to engine block ground. Use the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3A |
> | Less than 10 ohms? **NORepair:** Repair or replace the ECM power supply harness, fuses, or fuse holders. Clean the battery terminal connections. See equipment manufacturer service information. | 4A |  |
>
> ### STEP 3. Validate the occurrence of this fault code.
>
> #### STEP 3A. Operate the engine and determine if fault code condition exists.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Operate the engine and determine whether the fault code condition still exists. Operate the engine at high idle, no load. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 351 occurs during engine operation? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 4A |
> | Fault Code 351 occurs during engine operation? **NORepair:** A marginal battery voltage condition is possible. Make sure the batteries are fully charged or replace, if needed. It is likely that a marginal battery condition will result in Fault Code 351 becoming active at engine cranking. | 4A |  |
>
> ### STEP 4. Check ECM calibration and clear fault codes.
>
> #### STEP 4A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision numbers are found in the Calibration Information section of System ID and Dataplate in Features & Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 4B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 4B |  |
>
> #### STEP 4B. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault Code inactive? **YES** | Repair complete |
> | Fault Code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> ## Associated Procedures
>
> | Associated Procedures |  |  |  |
> |---|---|---|---|
> | Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
> | Engine Control Module | Refer to Procedure 019-031 | QSB4.5 CM2150 B108 | 4326163 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
> | Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F104 | 4332741 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F108 | 4332746 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB7 CM2880 B117 | 4358390 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB3.9 CM2200 B107 | 4310792 |
> | Engine Control Module | Refer to Procedure 019-031 | ISL9.5 CM2150 SN | 4310608 |
> | Engine Control Module | Refer to Procedure 019-031 | QSNT14 CM876 N102 | 4325993 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G106 | 4332695 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G108 | 4332901 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G107 | 4332690 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G109 | 4332906 |
> | Engine Control Module | Refer to Procedure 019-031 | ISL8.9 CM2880 L112 | 4358493 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB5.9 CM2880 B127 | 4383645 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF3.8 CM2880 F112 | 4383825 |
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
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB4.5 CM2150 B108 | 4326163 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB7 CM2880 B117 | 4358390 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB2.8 CM2880 F104 | 4332741 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB2.8 CM2880 F108 | 4332746 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISB3.9 CM2200 B107 | 4310792 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISL9.5 CM2150 SN | 4310608 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSNT14 CM876 N102 | 4325993 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG11 CM2880 G106 | 4332695 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG11 CM2880 G108 | 4332901 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG12 CM2880 G107 | 4332690 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISG12 CM2880 G109 | 4332906 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISL8.9 CM2880 L112 | 4358493 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISB5.9 CM2880 B127 | 4383645 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSF3.8 CM2880 F112 | 4383825 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSL9.3 CM2880 L113 | 4383811 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISF3.8 CM2220 F116 | 4383664 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSC8.3 CM2880 C102 | 4388785 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB5.9 CM2880 B139 | 4388870 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSB3.9 CM2880 B138 | 5411050 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISD6.7 CM2880 D101 | 5411372 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISF2.8 CM2220 F129 | 5411325 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISF4.5 CM2220 F123 | 5411320 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | QSG12 CM2880 G112 | 4388731 |
> | Engine Wiring Harness | Refer to Procedure 019-043 | ISF3.8 CM2220 F134B | 5504165 |
