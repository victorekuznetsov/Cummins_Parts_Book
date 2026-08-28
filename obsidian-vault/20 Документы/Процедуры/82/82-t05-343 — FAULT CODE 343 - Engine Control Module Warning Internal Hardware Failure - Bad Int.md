---
aliases:
  - "Код 343 — предупреждение о внутреннем аппаратном отказе ЭБУ"
type: "Процедура"
doc: "82-t05-343"
title_en: "FAULT CODE 343 - Engine Control Module Warning Internal Hardware Failure - Bad Intelligent Device or Component"
title_ru: "Код 343 — предупреждение о внутреннем аппаратном отказе ЭБУ"
modified: "2014-01-22"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-343.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-343.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# FAULT CODE 343 - Engine Control Module Warning Internal Hardware Failure - Bad Intelligent Device or Component
**Код 343 — предупреждение о внутреннем аппаратном отказе ЭБУ**

> [!abstract] Процедура · `82-t05-343`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2014-01-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-343.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-343.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
> Чтобы не повредить новый блок управления двигателем (ЭБУ), перед его заменой разберитесь со всеми остальными активными кодами неисправностей.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 - пробный щуп типа вилки DeutschTM/AMPTM/Metri-PackTM и номер детали 3164133 - пробный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **ШАГ 1А.** Проверка кодов неисправностей. | Код ошибки 343 активен или более трех неактивных чисел? |
| ШАГ 2. | Проверьте батареи и разъем питания. |  |
|  | **ШАГ 2А.** Проверьте аккумуляторы и разъем питания. | Соединения плотные и без коррозии? |
|  | **ШАГ 2В.** Проверьте напряжение батареи. | Нормальные условия: По меньшей мере (+) 12-VDC \[(+) 24-VDC с 24-вольтовой системой\]; Во время Кранка: По крайней мере (+) 6.2-VDC? |
| ШАГ 3. | Проверьте оригинальную электропроводку производителя оборудования (OEM). |  |
|  | **STEP 3A.** Проверить проводную упряжку и контакты разъема ECM. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте наличие открытой цепи в цепи питания аккумулятора. | По крайней мере (+) 10-VDC \[(+) 20VDC для 24-вольтовой системы\]? |
|  | **STEP 3B-1.** Убедитесь, что предохранитель установлен правильно. | Правильно установлен предохранитель? |
|  | **ШАГ 3В-2.** Проверьте, не взорван ли предохранитель. | Взорван предохранитель? |
|  | **STEP 3B-3.** Проверьте надстройку или вспомогательную проводку в (+) клемме батареи. | Поврежденные провода? |
|  | **STEP 3C** Проверьте сопротивление цепи питания аккумулятора. | Менее 1,0 Ом? |
|  | **STEP 3D.** Проверьте провод входа-в-ECM переключателя зажигания. | Вводный провод переключателя зажигания бесперебойный? |
|  | **STEP 3E.** Проверьте схему ввода переключателя зажигания. | Менее 5 Ом? |
| ШАГ 4. | Перенастройка ECM. |  |
|  | **STEP 4A.** Перенастройка ECM. | Код 343 активен после перекалибровки ECM? |
| ШАГ 5. | Проверьте калибровку ECM и четкие коды неисправностей. |  |
|  | **STEP 5A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 5B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Считайте коды неисправностей.

#### ШАГ 1A. Проверьте коды неисправностей.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 343 активен или более трех неактивных чисел? *Да | 2А |
| Код ошибки 343 активен или более трех неактивных чисел? **НЕТ** | 5а |  |

### ШАГ 2. Проверьте батареи и разъем питания.

#### ШАГ 2A. Проверьте батареи и разъем питания.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соединения аккумуляторов. Проверьте соединения терминала батареи. | Соединения плотные и без коррозии? *Да | 2В |
| Соединения плотные и без коррозии? **NORepair:** Затягивание связей. Затягивайте свободные соединения и очищайте терминалы. См. сервисное руководство изготовителя машины. | 5а |  |

#### ШАГ 2B. Проверьте напряжение батареи.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение батареи. Поместите положительный (+) щуп мультиметра на положительный вывод батареи и прикоснитесь к отрицательному (-) датчику к отрицательному выводу батареи при попытке запустить двигатель. | Нормальные условия: По меньшей мере (+) 12-VDC \[(+) 24-VDC с 24-вольтовой системой\]; При проворачивании: По крайней мере (+) 6.2-VDC? *Да | 3А |
| Нормальные условия: По меньшей мере (+) 12-VDC \[(+) 24-VDC с 24-вольтовой системой\]; При проворачивании: По крайней мере (+) 6.2-VDC? **NORepair:** Зарядить или заменить аккумулятор. См. сервисное руководство изготовителя машины. | 5а |  |

### ШАГ 3. Проверьте электропроводку OEM.

#### ШАГ 3A. Проверьте проводную упряжку и контакты разъема ECM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем электропроводки OEM от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить контакты разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **В репарации:** В электропроводке OEM обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]] | 5а |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте наличие открытой цепи в цепи питания батареи.

| **Условия:** Выключите замок зажигания. Отсоедините проводку двигателя от заглушки питания аккумулятора ECM от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие открытой цепи в цепях питания батареи. Используйте мультиметр для измерения напряжения от розетки питания (+) блока питания двигателя (ECM) разъема ствола питания аккумулятора ECM и заземления блока двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов использования мультиметра.[[99-019-359 — Multimeter Usage\|См. процедуру 019-359 в разделе 19.]] | По крайней мере (+) 10-VDC \[(+) 20VDC для 24-вольтовой системы\]? *Да | 3C |
| По крайней мере (+) 10-VDC \[(+) 20VDC для 24-вольтовой системы\]? **НЕТ** | 3В-1-1 |  |

#### ШАГ 3B-1. Убедитесь, что предохранитель OEM установлен правильно.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте предохранитель OEM для правильной установки. | Правильно установлен предохранитель? *Да | 3В-2-2 |
| Правильно установлен предохранитель? **NORepair:** Установите предохранитель правильно.[[99-019-198 — Fuse, Harness In-Line\|См. процедуру 019-198 в разделе 19.]] | 5а |  |

#### ШАГ 3B-2. Проверьте, не взорван ли предохранитель.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что предохранитель OEM не взорван. | Взорван предохранитель? **Ремонт:** Найдите короткое замыкание. Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]]Заменить выдувной предохранитель(ы).[[99-019-198 — Fuse, Harness In-Line\|См. процедуру 019-198 в разделе 19.]] | 5а |
| Взорван предохранитель? **НЕТ** | 3В-3 |  |

#### ШАГ 3B-3. Проверьте надстройку или вспомогательную проводку в (+) терминале батареи.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте надстройку или вспомогательную проводку в (+) терминале батареи. Начиная с (+) терминала, следуйте любой надстройке или вспомогательной проводах и проверяйте провод(ы) на наличие поврежденной изоляции или ошибки установки, которая может привести к тому, что подающий провод будет закорочен до блока двигателя. | Поврежденные провода? **Ремонт:** Ремонт или замена поврежденной проводов. | 5а |
| Поврежденные провода? **NORepair:** Ремонтировать или заменить электропроводку OEM от разъема питания OEM к батареям. См. сервисное руководство изготовителя машины. | 5а |  |

#### ШАГ 3C. Проверьте сопротивление цепи питания батареи.

| **Условия:** Выключите замок зажигания. Отсоедините проводку двигателя от заглушки питания аккумулятора ECM от разъема ECM. Отключите положительный терминал от батареи. Цифровой мультиметр устанавливается в режим низкого сопротивления и калибруется до нуля. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сопротивление цепи питания батареи. Измерьте сопротивление между флажком (+) разъема электропроводки двигателя (ECM) разъема блоков питания ECM и разъемом положительной батареи. Измерьте сопротивление между флажком (-) разъема электропроводки двигателя (ECM) разъема блоков питания ECM и разъемом отрицательной батареи. См. схему или схему проводов для идентификации контакта с разъемом. Поскольку сопротивление цепи питания батареи обычно очень низкое, необходимо использовать цифровой мультиметр, калиброванный до нуля на установке низкого сопротивления, чтобы точно измерить сопротивление цепи. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 1,0 Ом? *Да | 3D |
| Менее 1,0 Ом? **NORepair:** Ремонт или замена электропроводки ECM.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]] | 5а |  |

#### ШАГ 3D. Проверьте провод входного сигнала зажигания в ECM.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте вход переключателя зажигания. Проверить входной провод переключателя зажигания от поста зажигания переключателя в сборе переключателя зажигания до ECM, чтобы убедиться, что в проводе нет прерываний, то есть нет соленоидов или реле. | Вводный провод переключателя зажигания бесперебойный? **Ремонт:** Исправьте проводку так, чтобы провод был бесперебойным. | 5а |
| Вводный провод переключателя зажигания бесперебойный? **НЕТ** | 3E |  |

#### ШАГ 3E. Проверьте схему ввода переключателя зажигания.

| **Условия:** Выключите замок зажигания. Отсоедините разъём OEM-проводов от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте схему ввода переключателя зажигания. Измерить сопротивление от положения зажигания переключателя зажигания в сборе переключателя зажигания к контакту входного сигнала переключателя зажигания разъёма проводов OEM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 5 Ом? *Да | 4А |
| Менее 5 Ом? **NORepair:** Ремонтировать или заменить проводку OEM.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]] | 5а |  |

### ШАГ 4. Перенастройка ECM.

#### ШАГ 4A. Перенастройка ECM

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на землю. Используйте инструмент электронного обслуживания INSITETM для перекалибровки ECM с помощью новейшей калибровки двигателя. | Код 343 активен после перекалибровки ECM?  Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 5а |
| Код 343 активен после перекалибровки ECM? **НЕТ** | 5а |  |

### ШАГ 5. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 5A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички данных в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 5В |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]] | 5В |  |

#### ШАГ 5B. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да | Ремонт завершён. |
| Код неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

## Связанные процедуры

| Связанные процедуры |  |  |  |
|---|---|---|---|
| Название процедуры | Процедурный номер | Модельный сервис | Номер бюллетеня |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF2.8 CM2220 E ISF2.8 CM2220 AN ISF2.8 CM2220 IAN | 4022178 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF3.8 CM2220 ISF3.8 CM2220 AN ISF3.8 CM2220 IAN | 4021704 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF3.8 CM2220 F103 | 4310839 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB4.5, ISB6.7, ISD4.5 и ISD6.7 CM2150 SN | 4022188 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL8.9 CM2150 SN | 4022190 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISM11 CM876 SN | 4022196 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISZ13 CM2150 | 4022133 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISX15 CM2250 GX CM2250 | 4022250 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISX12/ISX11.9 CM2250 | 2883445 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSL9 CM2250 | 4022256 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB6.7 CM2250 | 4022255 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB6.7 CM2350 B105 | 4332778 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSL9 CM2350 L102 | 4332796 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB6.7 CM2250 EC | 2883621 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB3.3 CM2250 EC | 2883647 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSK78 CM2250 K104 | 4332682 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSX15 CM2250 ECF | 2883557 |
| Электронный блок управления двигателем | См. процедуру 019-031 | PowerGen QSX15 CM2250 ECF | 4310661 |
| Электронный блок управления двигателем | См. процедуру 019-031 | PowerGen QSX15 CM2250 | 4310664 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSX11.9 CM2250 ECF | 2883561 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB6.7 CM2350 B101 | 2883567 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL9 CM2350 L101 | 4310787 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISX12 CM2350 X102 | 4310646 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISX15 CM2350 X101 | 4310641 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISX15 CM2250 SN | 4310736 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB4.5 CM2350 B104 | 4332646 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB6.7 CM2350 B103 | 4332641 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB/ISD4.5 CM2150 B119 | 4358465 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB/ISD6.7 CM2150 B120 | 4358470 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL8.9 CM2150 L110 | 4358475 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF3.8 CM2220 F110 | 4358480 |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3164133 - female Deutsch™/AMP™/Metri-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for fault codes. | Fault Code 343 active or more than three inactive counts? |
> | STEP 2. | Check the batteries and the power connector. |  |
> |  | **STEP 2A.** Check the batteries and the power connector. | Connections tight and corrosion-free? |
> |  | **STEP 2B.** Check the battery voltage. | Normal conditions: At least (+) 12-VDC \[(+) 24-VDC with 24 volt system\]; During Cranking: At least (+) 6.2-VDC? |
> | STEP 3. | Check the original equipment manufacturer (OEM) power harness. |  |
> |  | **STEP 3A.** Inspect the harness and the ECM connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check for an open circuit in the battery power circuit. | At least (+) 10-VDC \[(+) 20-VDC for a 24 volt system\]? |
> |  | **STEP 3B-1.** Verify that the OEM fuse is installed correctly. | Fuse installed correctly? |
> |  | **STEP 3B-2.** Check if the OEM fuse is blown. | Fuse blown? |
> |  | **STEP 3B-3.** Check the add-on or accessory wiring at the (+) terminal of the battery. | Any damaged wires? |
> |  | **STEP 3C.** Check the resistance of the battery supply circuit. | Less than 1.0 ohms? |
> |  | **STEP 3D.** Check the keyswitch input-to-ECM wire. | Keyswitch input wire uninterrupted? |
> |  | **STEP 3E.** Check the keyswitch input circuit. | Less than 5 ohms? |
> | STEP 4. | Recalibrate the ECM. |  |
> |  | **STEP 4A.** Recalibrate the ECM. | Fault Code 343 active after recalibrating the ECM? |
> | STEP 5. | Check ECM calibration and clear fault codes. |  |
> |  | **STEP 5A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 5B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Read the fault codes.
>
> #### STEP 1A. Check for fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 343 active or more than three inactive counts? **YES** | 2A |
> | Fault Code 343 active or more than three inactive counts? **NO** | 5A |  |
>
> ### STEP 2. Check the batteries and the power connector.
>
> #### STEP 2A. Check the batteries and the power connector.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery connections. Check the battery terminal connections. | Connections tight and corrosion-free? **YES** | 2B |
> | Connections tight and corrosion-free? **NORepair:** Tighten the connections. Tighten the loose connections and clean the terminals. Refer to the OEM service manual. | 5A |  |
>
> #### STEP 2B. Check the battery voltage.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery voltage. Place the positive (+) probe of the multimeter on the positive battery terminal and touch the negative (-) probe to the negative battery terminal while trying to start the engine. | Normal conditions: At least (+) 12-VDC \[(+) 24-VDC with 24 volt system\]; During cranking: At least (+) 6.2-VDC? **YES** | 3A |
> | Normal conditions: At least (+) 12-VDC \[(+) 24-VDC with 24 volt system\]; During cranking: At least (+) 6.2-VDC? **NORepair:** Charge or replace the battery. Refer to the OEM service manual. | 5A |  |
>
> ### STEP 3. Check the OEM power harness.
>
> #### STEP 3A. Inspect the harness and the ECM connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM power harness connector from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the OEM harness. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 5A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check for an open circuit in the battery power circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness ECM battery supply stub from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit in the battery power circuits. Use a multimeter to measure the voltage from the ECM battery supply (+) pin of the engine harness ECM battery supply stub connector and engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | At least (+) 10-VDC \[(+) 20-VDC for a 24 volt system\]? **YES** | 3C |
> | At least (+) 10-VDC \[(+) 20-VDC for a 24 volt system\]? **NO** | 3B-1 |  |
>
> #### STEP 3B-1. Verify that the OEM fuse is installed correctly.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM fuse for correct installation. | Fuse installed correctly? **YES** | 3B-2 |
> | Fuse installed correctly? **NORepair:** Install the fuse correctly. [[99-019-198 — Fuse, Harness In-Line\|Refer to Procedure 019-198 in Section 19.]] | 5A |  |
>
> #### STEP 3B-2. Check if the OEM fuse is blown.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify that the OEM fuse is not blown. | Fuse blown? **YESRepair:** Locate the short circuit. Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] Replace the blown fuse(s). [[99-019-198 — Fuse, Harness In-Line\|Refer to Procedure 019-198 in Section 19.]] | 5A |
> | Fuse blown? **NO** | 3B-3 |  |
>
> #### STEP 3B-3. Check the add-on or the accessory wiring at the (+) terminal of the battery.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the add-on or the accessory wiring at the (+) terminal of the battery. Starting at the (+) terminal, follow any add-on or accessory wiring and examine wire(s) for damaged insulation or an installation error that can cause the supply wire to be shorted to the engine block. | Any damaged wires? **YESRepair:** Repair or replace the damaged wiring. | 5A |
> | Any damaged wires? **NORepair:** Repair or replace the OEM power harness from the OEM power connector to the batteries. Refer to the OEM service manual. | 5A |  |
>
> #### STEP 3C. Check the resistance of the battery supply circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness ECM battery supply stub from the ECM connector. Disconnect the positive terminal from the battery. Digital multimeter set to low resistance mode and calibrated to zero. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the resistance of the battery supply circuit. Measure the resistance between the ECM battery SUPPLY (+) pin of the engine harness ECM battery supply stub connector and the positive battery connector. Measure the resistance between the ECM battery SUPPLY (-) pin of the engine harness ECM battery supply stub connector and the negative battery connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Since the battery supply circuit resistance is normally very low, it is necessary to use a digital multimeter calibrated to zero on the low resistance setting to accurately measure the circuit resistance. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 1.0 ohms? **YES** | 3D |
> | Less than 1.0 ohms? **NORepair:** Repair or replace the ECM power harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 5A |  |
>
> #### STEP 3D. Check the keyswitch input-to-ECM wire.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the keyswitch input. Inspect the keyswitch input wire from the keyswitch ignition post in the keyswitch assembly to the ECM to make sure there are no interruptions in the wire, that is, no solenoids or relays. | Keyswitch input wire uninterrupted? **YESRepair:** Correct the wiring so the wire is uninterrupted. | 5A |
> | Keyswitch input wire uninterrupted? **NO** | 3E |  |
>
> #### STEP 3E. Check the keyswitch input circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the keyswitch input circuit. Measure the resistance from the keyswitch ignition post in the keyswitch assembly to keyswitch input SIGNAL pin of the OEM harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 5 ohms? **YES** | 4A |
> | Less than 5 ohms? **NORepair:** Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 5A |  |
>
> ### STEP 4. Recalibrate the ECM.
>
> #### STEP 4A. Recalibrate the ECM
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground. Use INSITE™ electronic service tool to recalibrate the ECM with the latest engine calibration. | Fault Code 343 active after recalibrating the ECM? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 5A |
> | Fault Code 343 active after recalibrating the ECM? **NO** | 5A |  |
>
> ### STEP 5. Check ECM calibration and clear fault codes.
>
> #### STEP 5A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 5B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 5B |  |
>
> #### STEP 5B. Disable the fault code.
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
> | Engine Control Module | Refer to Procedure 019-031 | ISF2.8 CM2220 E ISF2.8 CM2220 AN ISF2.8 CM2220 IAN | 4022178 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 ISF3.8 CM2220 AN ISF3.8 CM2220 IAN | 4021704 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F103 | 4310839 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB4.5, ISB6.7, ISD4.5, and ISD6.7 CM2150 SN | 4022188 |
> | Engine Control Module | Refer to Procedure 019-031 | ISL8.9 CM2150 SN | 4022190 |
> | Engine Control Module | Refer to Procedure 019-031 | ISM11 CM876 SN | 4022196 |
> | Engine Control Module | Refer to Procedure 019-031 | ISZ13 CM2150 | 4022133 |
> | Engine Control Module | Refer to Procedure 019-031 | ISX15 CM2250 GX CM2250 | 4022250 |
> | Engine Control Module | Refer to Procedure 019-031 | ISX12/ISX11.9 CM2250 | 2883445 |
> | Engine Control Module | Refer to Procedure 019-031 | QSL9 CM2250 | 4022256 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB6.7 CM2250 | 4022255 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB6.7 CM2350 B105 | 4332778 |
> | Engine Control Module | Refer to Procedure 019-031 | QSL9 CM2350 L102 | 4332796 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB6.7 CM2250 EC | 2883621 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB3.3 CM2250 EC | 2883647 |
> | Engine Control Module | Refer to Procedure 019-031 | QSK78 CM2250 K104 | 4332682 |
> | Engine Control Module | Refer to Procedure 019-031 | QSX15 CM2250 ECF | 2883557 |
> | Engine Control Module | Refer to Procedure 019-031 | PowerGen QSX15 CM2250 ECF | 4310661 |
> | Engine Control Module | Refer to Procedure 019-031 | PowerGen QSX15 CM2250 | 4310664 |
> | Engine Control Module | Refer to Procedure 019-031 | QSX11.9 CM2250 ECF | 2883561 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB6.7 CM2350 B101 | 2883567 |
> | Engine Control Module | Refer to Procedure 019-031 | ISL9 CM2350 L101 | 4310787 |
> | Engine Control Module | Refer to Procedure 019-031 | ISX12 CM2350 X102 | 4310646 |
> | Engine Control Module | Refer to Procedure 019-031 | ISX15 CM2350 X101 | 4310641 |
> | Engine Control Module | Refer to Procedure 019-031 | ISX15 CM2250 SN | 4310736 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB4.5 CM2350 B104 | 4332646 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB6.7 CM2350 B103 | 4332641 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB/ISD4.5 CM2150 B119 | 4358465 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB/ISD6.7 CM2150 B120 | 4358470 |
> | Engine Control Module | Refer to Procedure 019-031 | ISL8.9 CM2150 L110 | 4358475 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F110 | 4358480 |
