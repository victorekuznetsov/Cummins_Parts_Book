---
type: "Процедура"
doc: "178-t05-133"
title_en: "FAULT CODE 133 - Remote Accelerator Pedal or Lever Position Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2019-08-22"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326169"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-133.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-133.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/178"
  - "перевод/машинный"
---

# FAULT CODE 133 - Remote Accelerator Pedal or Lever Position Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `178-t05-133`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326169 — QSB6.7 CM2150 B109 Fault Code Troubleshooting Manual|4326169]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-08-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-133.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-133.pdf)

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
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3823996 - гнездовой испытательный щуп Weather PackTM и номер детали 3822758 - пробный щуп типа plug-Plug DeutschTM/AMPTM/Metri-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить коды неисправностей датчиков. | Код ошибки 1695 или 1696 активен? |
|  | **STEP 1B.** Проверить наличие кода сбоя. | Код 133 активен? |
| ШАГ 2. | Проверьте педаль дистанционного ускорителя или датчик положения рычага, питающий напряжение и обратную цепь. |  |
|  | **STEP 2A.** Проверить педаль дистанционного ускорителя или датчик положения рычага и контакты разъема. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте педаль дистанционного ускорителя или датчик положения рычага, питающий напряжение и обратную цепь. | 4,75 VDC и 5,25 VDC? |
|  | **STEP 2C.** Проверьте реакцию цепи. | Код 134 активен, а Код 133 неактивен? |
|  | **STEP 2D.** Проверьте коды неисправностей и проверьте состояние педали или рычага дистанционного ускорителя. | Код 134 активен? |
| ШАГ 3. | Проверьте электропроводку ECM и производителя оригинального оборудования (OEM). |  |
|  | **STEP 3A.** Проверить контакты разъёма электропроводки ECM и OEM. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте наличие открытой цепи в электропроводке OEM. | Менее 10 Ом? |
|  | **STEP 3C.** Проверьте короткое замыкание в проводной ремне OEM. | Больше 100 тысяч ом? |
|  | **STEP 3D.** Проверить неактивный код ошибки. | Код 133 неактивен? |
| ШАГ 4. | Проверьте калибровку ECM и четкие коды неисправностей. |  |
|  | **STEP 4A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 4B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте коды неисправностей датчика.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте коды неисправностей датчика. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 1695 или 1696 активен? *Да | Код ошибки 1695 и/или 1696. |
| Код ошибки 1695 или 1696 активен? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте активный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 133 активен? *Да | 2А |
| Код 133 активен? **НЕТ** | Используйте следующую процедуру для неактивного или прерывистого кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |  |

### ШАГ 2. Проверьте педаль дистанционного ускорителя или датчик положения рычага и напряжение питания цепи и обратную цепь.

#### ШАГ 2A. Осмотрите педаль дистанционного ускорителя или датчик положения рычага и контакты разъема.

| **Условия:** Выключите замок зажигания. Отсоедините датчик положения педали или рычага удаленного ускорителя от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы OEM-проводов и разъёма датчиков на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]] | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте педаль дистанционного ускорителя или датчик положения рычага, питающий напряжение и обратную цепь.

| **Условия:** Выключите замок зажигания. Отсоедините датчик положения педали удаленного ускорителя от электропроводки OEM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение питания датчика и обратную цепь. Измерить напряжение от датчика положения педали удаленного ускорителя +5 вольт контакта питания к датчику обратного контакта педали удаленного ускорителя на разъеме датчика проводов OEM. Используйте схему проводов для идентификации штифта и следующую процедуру для общего многометрового использования.[[99-019-359 — Multimeter Usage\|См. процедуру 019-359 в разделе 19.]] | 4,75 VDC и 5,25 VDC? *Да | 2C |
| 4,75 VDC и 5,25 VDC? **НЕТ** | 3А |  |

#### ШАГ 2C. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Отсоедините датчик положения педали или рычага удаленного ускорителя от электропроводки OEM. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующий ответ на ECM через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 134 активен, а Код 133 неактивен? *Да | 2D |
| Код 134 активен, а Код 133 неактивен? **НЕТ** | 3А |  |

#### ШАГ 2D. Проверьте коды неисправностей и проверьте состояние педали или рычага удаленного ускорителя.

| **Условия:** Выключите замок зажигания. Подключите педаль или рычаг удаленного ускорителя к электропроводке OEM. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 134 активен? **Ремонт: **Поврежденная педаль или рычаг дистанционного ускорителя были обнаружены. Свяжитесь с соответствующим дилером OEM для получения инструкций по ремонту. Замените педаль или рычаг удаленного ускорителя. См. сервисную документацию изготовителя оборудования. | 4А |
| Код 134 активен? **Норвегия: **Нет. Удаление и установка разъема исправили неисправность. | 4А |  |

### ШАГ 3. Проверьте электропроводку ECM и OEM.

#### ШАГ 3A. Проверьте контакты разъёма ECM и OEM-проводов.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты проводов OEM и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]] | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте наличие открытой цепи в OEM-проводах.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. Отсоедините датчик положения педали или рычага удаленного ускорителя от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление между OEM проводкой жгута разъема ECM удаленного ускорителя или обратного контакта рычага и OEM проводов жгута удаленного обратного контакта педали акселератора. Используйте схему проводов для идентификации штифта и следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 3C |
| Менее 10 Ом? **NORepair:** В электропроводке OEM обнаружена схема с открытым возвратом. Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]] | 4А |  |

#### ШАГ 3C. Проверьте короткое замыкание контакт-контакт в электропроводке OEM.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. Отсоедините датчик положения педали удаленного ускорителя от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое контактное соединение. Измерьте сопротивление между контактом педали удаленного ускорителя или сигнала рычага в разъеме ECM проводов OEM и всеми другими штифтами в разъеме OEM. Используйте схему проводов и следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3D |
| Больше 100 тысяч ом? **NORepair:** Ремонтировать или заменить проводку OEM.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]] | 4А |  |

#### ШАГ 3D. Проверьте неактивный код ошибки.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 133 неактивен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | 4А |
| Код 133 неактивен? Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 4А |  |

### ШАГ 4. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 4A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 4B |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]] | 4B |  |

#### ШАГ 4B. Отключите код неисправности.

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
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL9.5 CM2150 SN | 4310608 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB3.9 CM2220 B107 | 4310792 |
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
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB5.9 CM2880 B127 | 4383645 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF3.8 CM2220 F116 | 4383664 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSL9.3 CM2880 L113 | 4383811 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSC8.3 CM2880 C102 | 4388785 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB5.9 CM2880 B139 | 4388870 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB3.9 CM2880 B138 | 5411050 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISD6.7 CM2880 D101 | 5411372 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF2.8 CM2220 F129 | 5411325 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF4.5 CM2220 F123 | 5411320 |
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
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3823996 - female Weather Pack™ test lead and Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for sensor supply fault codes. | Fault Code 1695 or 1696 active? |
> |  | **STEP 1B.** Check for an active fault code. | Fault Code 133 active? |
> | STEP 2. | Check the remote accelerator pedal or lever position sensor supply voltage and return circuit. |  |
> |  | **STEP 2A.** Inspect the remote remote accelerator pedal or lever position sensor and connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the remote accelerator pedal or lever position sensor supply voltage and return circuit. | Between 4.75 VDC and 5.25 VDC? |
> |  | **STEP 2C.** Check the circuit response. | Fault Code 134 active and Fault Code 133 inactive? |
> |  | **STEP 2D.** Check the fault codes and verify remote remote accelerator pedal or lever condition. | Fault Code 134 active? |
> | STEP 3. | Check the ECM and original equipment manufacturer (OEM) harness. |  |
> |  | **STEP 3A.** Inspect ECM and OEM harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
> |  | **STEP 3C.** Check for a pin-to-pin short circuit in the OEM harness. | Greater than 100k ohms? |
> |  | **STEP 3D.** Check for an inactive fault code. | Fault Code 133 inactive? |
> | STEP 4. | Check ECM calibration and clear fault codes. |  |
> |  | **STEP 4A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 4B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for sensor supply fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for sensor supply fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1695 or 1696 active? **YES** | Troubleshoot Fault Code 1695 and/or 1696. |
> | Fault Code 1695 or 1696 active? **NO** | 1B |  |
>
> #### STEP 1B. Check for an active fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 133 active? **YES** | 2A |
> | Fault Code 133 active? **NO** | Use the following procedure for inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |
>
> ### STEP 2. Check the remote accelerator pedal or lever position sensor and circuit supply voltage and return circuit.
>
> #### STEP 2A. Inspect the remote accelerator pedal or lever position sensor and connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the remote accelerator pedal or lever position sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair or replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the remote accelerator pedal or lever position sensor supply voltage and return circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the remote accelerator pedal position sensor from the OEM harness. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the sensor supply voltage and return circuit. Measure the voltage from the remote accelerator pedal position sensor +5 volt SUPPLY pin to the remote accelerator pedal position sensor RETURN pin at the sensor connector of the OEM harness. Use a wiring diagram for pin identification and the following procedure for general multimeter usage. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Between 4.75 VDC and 5.25 VDC? **YES** | 2C |
> | Between 4.75 VDC and 5.25 VDC? **NO** | 3A |  |
>
> #### STEP 2C. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the remote accelerator pedal or lever position sensor from the OEM harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 134 active and Fault Code 133 inactive? **YES** | 2D |
> | Fault Code 134 active and Fault Code 133 inactive? **NO** | 3A |  |
>
> #### STEP 2D. Check the fault codes and verify remote remote accelerator pedal or lever condition.
>
> | **Conditions:** Turn keyswitch OFF. Connect the remote accelerator pedal or lever to the OEM harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 134 active? **YESRepair:** A damaged remote accelerator pedal or lever has been detected. Contact the appropriate OEM dealership for repair instructions. Replace the remote accelerator pedal or lever. See equipment manufacturer service information. | 4A |
> | Fault Code 134 active? **NORepair:** None. The removal and installation of the connector corrected the fault. | 4A |  |
>
> ### STEP 3. Check the ECM and OEM harness.
>
> #### STEP 3A. Inspect the ECM and OEM harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair or replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check for an open circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the remote accelerator pedal or lever position sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the OEM harness ECM connector remote accelerator pedal or lever RETURN pin and the OEM harness remote accelerator pedal RETURN pin. Use a wiring diagram for pin identification and the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3C |
> | Less than 10 ohms? **NORepair:** An open return circuit has been detected in the OEM harness. Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |  |
>
> #### STEP 3C. Check for a pin-to-pin short circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the remote accelerator pedal position sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short. Measure the resistance between the remote accelerator pedal or lever SIGNAL pin in the OEM harness ECM connector and all other pins in the OEM connector. Use a wiring diagram and the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3D |
> | Greater than 100k ohms? **NORepair:** Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |  |
>
> #### STEP 3D. Check for an inactive fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 133 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
> | Fault Code 133 inactive? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 4A |  |
>
> ### STEP 4. Check ECM calibration and clear fault codes.
>
> #### STEP 4A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 4B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 4B |  |
>
> #### STEP 4B. Disable the fault code.
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
> | Engine Control Module | Refer to Procedure 019-031 | ISL9.5 CM2150 SN | 4310608 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB3.9 CM2220 B107 | 4310792 |
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
> | Engine Control Module | Refer to Procedure 019-031 | ISB5.9 CM2880 B127 | 4383645 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F116 | 4383664 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Engine Control Module | Refer to Procedure 019-031 | QSL9.3 CM2880 L113 | 4383811 |
> | Engine Control Module | Refer to Procedure 019-031 | QSC8.3 CM2880 C102 | 4388785 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB5.9 CM2880 B139 | 4388870 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB3.9 CM2880 B138 | 5411050 |
> | Engine Control Module | Refer to Procedure 019-031 | ISD6.7 CM2880 D101 | 5411372 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF2.8 CM2220 F129 | 5411325 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF4.5 CM2220 F123 | 5411320 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F134B | 5504165 |
> | Engine Control Module | Refer to Procedure 019-031 | Z14 CM2670 Z103B | 5504577 |
> | Engine Control Module | Refer to Procedure 019-031 | D6.7 CM2670 D102B | 5504515 |
> | Engine Control Module | Refer to Procedure 019-031 | B6.2 CM2670 B156B | 5579510 |
> | Engine Control Module | Refer to Procedure 019-031 | X12 CM2670 X121B | 5504455 |
> | Engine Control Module | Refer to Procedure 019-031 | L9 CM2670 L128B | 5504589 |
