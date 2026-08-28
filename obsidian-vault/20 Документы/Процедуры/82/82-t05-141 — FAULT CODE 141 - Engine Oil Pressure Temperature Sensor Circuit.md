---
aliases:
  - "Код 141 — цепь датчика давления и температуры масла"
type: "Процедура"
doc: "82-t05-141"
title_en: "FAULT CODE 141 - Engine Oil Pressure/Temperature Sensor Circuit"
title_ru: "Код 141 — цепь датчика давления и температуры масла"
modified: "2015-08-04"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# FAULT CODE 141 - Engine Oil Pressure/Temperature Sensor Circuit
**Код 141 — цепь датчика давления и температуры масла**

> [!abstract] Процедура · `82-t05-141`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-08-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-141.pdf)

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
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 — пробный щуп типа штепсельной вилки DeutschTM/AMPTM/Metri-PackTM, номер детали 3822917 — пробный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM, а номер детали 3162898 — проводной ответвление жгута.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить коды неисправностей датчиков. | Сенсор подает коды неисправностей активные? |
|  | **STEP 1B.** Проверить наличие кода сбоя. | Код 141 активен? |
| ШАГ 2. | Проверьте датчик давления/температуры масла и схему. |  |
|  | **STEP 2A** Проверить датчик давления/температуры масла и контакты разъема. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте напряжение питания датчика и схему возврата. | 4,75 VDC до 5,25 VDC? |
| ШАГ 3. | Проверьте ECM и электропроводку двигателя. |  |
|  | **STEP 3A.** Проверить контакты разъема ECM и проводов двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте напряжение питания датчика и схему возврата. | 4,75 VDC до 5,25 VDC? |
|  | **STEP 3C** Проверить контакты разъема электропроводки и электропроводки двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 3D.** Проверьте наличие открытой цепи в исходной стороне сигнала, используемой производителем оборудования (OEM). | Менее 10 Ом? |
|  | **ШАГ 3Е.** Проверьте наличие открытой цепи в обратной стороне проводов OEM. | Менее 10 Ом? |
|  | **STEP 3F.** Проверьте короткое замыкание в электропроводке OEM. | Больше 100 тысяч ом? |
|  | **STEP 3G.** Проверьте короткое замыкание в проводной упряжке OEM. | Больше 100 тысяч ом? |
|  | **STEP 3H.** Проверить наличие кода сбоя. | Код 141 активен? |
| ШАГ 4. | Проверьте калибровку ECM и четкие коды неисправностей. |  |
|  | **STEP 4A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 4B.** Отключить код ошибки. | Активный код ошибки? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте коды неисправностей датчика.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте коды неисправностей датчика. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Сенсор подает коды неисправностей активные? *Да | Соответствующий код неисправности дерево |
| Сенсор подает коды неисправностей активные? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте активный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 141 активен? *Да | 2А |
| Код 141 активен? **НЕТ** | Используйте следующую процедуру для неактивного или прерывистого кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |  |

### ШАГ 2. Проверьте датчик давления/температуры масла и схему.

#### ШАГ 2A. Проверьте датчик давления масла / температурного давления и контакты разъема.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления/температуры масла от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы датчика давления/температуры двигателя и проводов для следующих устройств: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 Раздел 19.]] | Грязные или поврежденные контакты? **Ремонт:** В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте напряжение питания датчика и обратную цепь.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления/температуры масла от электропроводки двигателя. Установите проводной ремень ветки кабеля, номер детали 3162898, между датчиком и разъемом ремня электропроводки двигателя. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение питания и обратную цепь. Измерьте напряжение от контакта подачи масла +5 вольт до обратного контакта давления масла на разъеме датчика проводов двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов использования мультиметра.[[99-019-359 — Multimeter Usage\|См. процедуру 019-359 в разделе 19.]] | 4,75 VDC до 5,25 VDC? *Да | 3C |
| 4,75 VDC до 5,25 VDC? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте ECM и электропроводку двигателя.

#### ШАГ 3A. Проверьте контакты разъема ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъёма электропроводки двигателя и разъема двигателя ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? В разъеме двигателя ECM обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте напряжение питания датчика и обратную цепь.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Установите проводной ремень ветки кабеля, номер детали 3162898, между датчиком и разъемом ремня электропроводки двигателя. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение питания и обратную цепь. Измерить напряжение от контакта подачи масла +5 вольт до обратного контакта давления масла при ECM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов использования мультиметра.[[99-019-359 — Multimeter Usage\|См. процедуру 019-359 в разделе 19.]] | 4,75 VDC до 5,25 VDC? *Да | 3C |
| 4,75 VDC до 5,25 VDC? Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 4А |  |

#### ШАГ 3C. Проверьте контакты разъема ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъёма электропроводки двигателя и разъема двигателя ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 Раздел 19.]] | Грязные или поврежденные контакты? **Ремонт:** В разъеме двигателя ECM или разъеме ремней электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3D |  |

#### ШАГ 3D. Проверьте наличие открытой цепи в стороне сигнала OEM-проводов.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от ECM. Отсоедините датчик давления/температуры масла от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление между OEM проводкой жгута разъема давления/температурного датчика датчика контакта и OEM проводкой жгута масла давления/температурного датчика разъема контакта. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 3E |
| Менее 10 Ом? **NORepair:** В электропроводке OEM обнаружена схема открытого сигнала. Устранение неполадок в каждой проводах, соединенной последовательно, чтобы определить, какая из них содержит цепь открытого сигнала. Ремонт или замена OEM проводов жгута. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 3E. Проверьте наличие открытой цепи в обратной стороне проводов OEM.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от ECM. Отсоедините датчик давления/температуры масла от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление между OEM проводкой жгута разъема давления/температурного датчика обратного контакта и OEM проводкой ремня давления/температурного датчика разъема обратного контакта. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 3F |
| Менее 10 Ом? **NORepair:** В электропроводке OEM обнаружена открытая обратная цепь. Устранение неполадок в каждой проводах, соединенной последовательно, чтобы определить, которая содержит открытую обратную цепь. Ремонт или замена OEM проводов жгута. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 3F. Проверьте короткое замыкание, чтобы приземлиться в OEM-проводах.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от ECM. Отсоедините датчик давления/температуры масла от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на землю. Измерьте сопротивление между контактом датчика давления/температуры масла в разъёме электропроводки OEM ECM и землей шасси. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3G |
| Больше 100 тысяч ом? **NORepair:** В электропроводке OEM обнаружено короткое замыкание на землю на проводе SIGNAL. Ремонт или замена OEM проводов жгута. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 3G. Проверьте короткое замыкание контакт-контакт в электропроводке OEM.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от ECM. Отсоедините датчик давления/температуры масла от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание контакт-контакт. Измерьте сопротивление между контактом сигнала датчика давления/температуры масла в разъеме ECM проводов OEM и всеми другими штифтами в разъеме ECM проводов OEM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3х |
| Больше 100 тысяч ом? **NORepair:** В электропроводке OEM обнаружено короткое замыкание на проводе SIGNAL. Ремонт или замена OEM проводов жгута. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 3H. Проверьте активный код ошибки.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITE. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, отвечает ли подходящая схема через 30 секунд. Используйте инструмент Insite для показаний кодов ошибок. | Код 141 активен?  Поврежденный датчик был обнаружен. Замените датчик давления/температуры масла. См. процедуру 019-155 в Таблице ассоциированных процедур. | 4А |
| Код 141 активен? **Норвегия:** Нет. Удаление и установка разъема исправили неисправность. | 4А |  |

### ШАГ 4. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 4A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички данных в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 4B |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]] | 4B |  |

#### ШАГ 4B. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Активный код ошибки? Возвращение к шагам устранения неполадок или обращение в авторизованное место ремонта Cummins®, если все шаги были завершены и проверены повторно. | 1А |
| Активный код ошибки? **НЕТ** | Ремонт завершён |  |

## Связанные процедуры

| Связанные процедуры |  |  |  |
|---|---|---|---|
| Название процедуры | Процедурный номер | Модельный сервис | Номер бюллетеня |
| Электронный блок управления двигателем | [[82-019-031 — Engine Control Module\|См. процедуру 019-031]] | ISM11 CM570 QSM11 CM570 | [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]] |
| Жгут проводов двигателя | [[82-019-043-tr — Engine Wiring Harness\|См. процедуру 019-043]] | ISM11 CM570 QSM11 CM570 | [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]] |
| Датчик давления и температуры масла | [[82-019-155 — Oil Pressure Temperature Sensor\|См. процедуру 019-155]] | ISM11 CM570 QSM11 CM570 | [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]] |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, and Part Number 3162898 - breakout cable.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for sensor supply fault codes. | Sensor supply fault codes active? |
> |  | **STEP 1B.** Check for an active fault code. | Fault Code 141 active? |
> | STEP 2. | Check the oil pressure/temperature sensor and circuit. |  |
> |  | **STEP 2A.** Inspect the oil pressure/temperature sensor and connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the sensor supply voltage and return circuit. | 4.75 VDC to 5.25 VDC? |
> | STEP 3. | Check the ECM and engine harness. |  |
> |  | **STEP 3A.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the sensor supply voltage and return circuit. | 4.75 VDC to 5.25 VDC? |
> |  | **STEP 3C.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3D.** Check for an open circuit in the original equipment manufacturer (OEM) harness signal side. | Less than 10 ohms? |
> |  | **STEP 3E.** Check for an open circuit in the OEM harness return side. | Less than 10 ohms? |
> |  | **STEP 3F.** Check for a short circuit to ground in the OEM harness. | Greater than 100k ohms? |
> |  | **STEP 3G.** Check for a pin-to-pin short circuit in the OEM harness. | Greater than 100k ohms? |
> |  | **STEP 3H.** Check for an active fault code. | Fault Code 141 active? |
> | STEP 4. | Check ECM calibration and clear fault codes. |  |
> |  | **STEP 4A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 4B.** Disable the fault code. | Fault code active? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for sensor supply fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for sensor supply fault codes. Use INSITE™ electronic service tool to read the fault codes. | Sensor supply fault codes active? **YES** | Appropriate fault code troubleshooting tree |
> | Sensor supply fault codes active? **NO** | 1B |  |
>
> #### STEP 1B. Check for an active fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 141 active? **YES** | 2A |
> | Fault Code 141 active? **NO** | Use the following procedure for an inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |
>
> ### STEP 2. Check the oil pressure/temperature sensor and circuit.
>
> #### STEP 2A. Inspect the oil pressure/temperatrue sensor and connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the oil pressure/temperature sensor from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and oil pressure/temperature sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the sensor supply voltage and return circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the oil pressure/temperature sensor from the engine harness. Install the breakout cable, Part Number 3162898, between the sensor and the engine harness connector. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply voltage and return circuit. Measure the voltage from the oil pressure +5 volt SUPPLY pin to the oil pressure RETURN pin at the sensor connector of the engine harness. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | 4.75 VDC to 5.25 VDC? **YES** | 3C |
> | 4.75 VDC to 5.25 VDC? **NO** | 3A |  |
>
> ### STEP 3. Check the ECM and engine harness.
>
> #### STEP 3A. Inspect the ECM and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM engine connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM engine connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the sensor supply voltage and return circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Install the breakout cable, Part Number 3162898, between the sensor and the engine harness connector. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply voltage and return circuit. Measure the voltage from the oil pressure +5 volt SUPPLY pin to the oil pressure RETURN pin at the ECM. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | 4.75 VDC to 5.25 VDC? **YES** | 3C |
> | 4.75 VDC to 5.25 VDC? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 4A |  |
>
> #### STEP 3C. Inspect the ECM and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM engine connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM engine connector or engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
> | Dirty or damaged pins? **NO** | 3D |  |
>
> #### STEP 3D. Check for an open circuit in the OEM harness signal side.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM. Disconnect the oil pressure/temperature sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the OEM harness ECM connector oil pressure/temperature sensor SIGNAL pin and the OEM harness oil pressure/temperature sensor connector SIGNAL pin. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3E |
> | Less than 10 ohms? **NORepair:** An open signal circuit has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the open signal circuit. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 3E. Check for an open circuit in the OEM harness return side.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM. Disconnect the oil pressure/temperature sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the OEM harness ECM connector oil pressure/temperature sensor RETURN pin and the OEM harness oil pressure/temperature sensor connector RETURN pin. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3F |
> | Less than 10 ohms? **NORepair:** An open returnl circuit has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the open return circuit. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 3F. Check for a short circuit to ground in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM. Disconnect the oil pressure/temperature sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground. Measure the resistance between the oil pressure/temperature sensor SIGNAL pin in the OEM harness ECM connector and chassis ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3G |
> | Greater than 100k ohms? **NORepair:** A short circuit to ground on the SIGNAL wire has been detected in the OEM harness. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 3G. Check for a pin-to-pin short circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM. Disconnect the oil pressure/temperature sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short circuit. Measure the resistance between the oil pressure/temperature sensor SIGNAL pin in the OEM harness ECM connector and all other pins in the OEM harness ECM connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3H |
> | Greater than 100k ohms? **NORepair:** A pin-to-pin short circuit on the SIGNAL wire has been detected in the OEM harness. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 3H. Check for active fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit respons after 30 seconds. Use INSITE electronic service tool to read the fault codes. | Fault Code 141 active? **YESRepair:** A damaged sensor has been detected. Replace the oil pressure/temperature sensor. Refer to Procedure 019-155 in the Associated Procedures Table. | 4A |
> | Fault Code 141 active? **NORepair:** None. The removal and installation of the connector corrected the fault. | 4A |  |
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
> | Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code active? **YESRepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |
> | Fault code active? **NO** | Repair complete |  |
>
> ## Associated Procedures
>
> | Associated Procedures |  |  |  |
> |---|---|---|---|
> | Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
> | Engine Control Module | [[82-019-031 — Engine Control Module\|Refer to Procedure 019-031]] | ISM11 CM570 QSM11 CM570 | [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]] |
> | Engine Wiring Harness | [[82-019-043-tr — Engine Wiring Harness\|Refer to Procedure 019-043]] | ISM11 CM570 QSM11 CM570 | [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]] |
> | Oil Pressure/Temperature Sensor | [[82-019-155 — Oil Pressure Temperature Sensor\|Refer to Procedure 019-155]] | ISM11 CM570 QSM11 CM570 | [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]] |
