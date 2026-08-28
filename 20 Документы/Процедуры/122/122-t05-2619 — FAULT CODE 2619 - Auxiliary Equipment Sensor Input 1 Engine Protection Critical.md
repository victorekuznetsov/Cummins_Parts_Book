---
aliases:
  - "Код 2619 — вход датчика вспомогательного оборудования 1, защита двигателя — особые указания"
type: "Процедура"
doc: "122-t05-2619"
title_en: "FAULT CODE 2619 - Auxiliary Equipment Sensor Input 1 Engine Protection Critical - Special Instructions"
title_ru: "Код 2619 — вход датчика вспомогательного оборудования 1, защита двигателя — особые указания"
modified: "2012-08-07"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-2619.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-2619.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 2619 - Auxiliary Equipment Sensor Input 1 Engine Protection Critical - Special Instructions
**Код 2619 — вход датчика вспомогательного оборудования 1, защита двигателя — особые указания**

> [!abstract] Процедура · `122-t05-2619`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-08-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-2619.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-2619.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 — пробный щуп типа штепсельной заглушки DeutschTM/AMPTM/Metri-PackTM, номер детали 3822917 — пробный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM, а номер детали 3823995 — штыревой пробный щуп Weather PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте, находится ли кнопка остановки двигателя в положении STOP. |  |
|  | **STEP 1A.** Проверьте, находится ли кнопка остановки двигателя в положении STOP. | Кнопка остановки двигателя в положении STOP? |
|  | **STEP 1B.** Проверить информацию о блоке управления дизельным топливом (DCU). | DCU показывает событие с кнопкой остановки или тест свидетеля? |
|  | **STEP 1C.** Проверить наличие других кодов неисправностей. | Активные или неактивные коды ошибок? |
| ШАГ 2. | Проверьте правильное положение клапанов отключения воздуха. |  |
|  | **ШАГ 2А.** Проверить правильное положение клапанов отключения воздуха. | Запорные клапаны в положении OPEN? |
| ШАГ 3. | Проверьте кнопку остановки двигателя для короткого замыкания. |  |
|  | **STEP 3A.** Проверьте кнопку остановки двигателя на короткое замыкание. | Больше 100 тысяч ом? |
| ШАГ 4. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 4A.** Проверить упряжку электропроводки двигателя и разъемы ECM. | Грязные или поврежденные контакты? |
|  | **ШАГ 4В.** Проверьте короткое замыкание на землю. | Больше 100 тысяч ом? |
|  | **STEP 4C.** Проверьте короткое замыкание. | Больше 100 тысяч ом? |
| ШАГ 5. | Проверьте OEM проводку. |  |
|  | **STEP 5A.** Проверить электропроводку OEM и 23-контактные разъемы. | Грязные или поврежденные контакты? |
|  | **ШАГ 5В.** Проверьте короткое замыкание на землю. | Больше 100 тысяч ом? |
|  | **STEP 5C** Проверьте короткое замыкание. | Больше 100 тысяч ом? |
| ШАГ 6. | Проверьте внутреннюю проводку клиентского интерфейса (CIB). |  |
|  | **STEP 6A.** Проверьте внутреннюю проводку между кнопкой E-stop и 23-контактным OEM-разъемом. | Грязные или поврежденные контакты? |
|  | **ШАГ 6В.** Проверьте короткое замыкание на землю. | Больше 100 тысяч ом? |
|  | **STEP 6C.** Проверьте короткое замыкание. | Больше 100 тысяч ом? |
| ШАГ 7. | Очистите коды неисправностей и проверьте прогрессивный ущерб. |  |
|  | **7А.** Подтверждают условия. | Данные снимка показывают, что код ошибки 2619 был установлен на уровне или ниже холостого хода и 10-процентного крутящего момента. |
|  | **STEP 7B.** Завершите проверку с выключенным двигателем. | Горбатые шланги и турбокомпрессоры соответствуют спецификациям? |
|  | **STEP 7C.** Отключить код ошибки. | Код ошибки 2619 неактивен? |
|  | **STEP 7D.** Проверка прокладок при нагрузке. | Ущерб обнаружен прокладкам? |
|  | **STEP 7E.** Отключить код ошибки. | Код ошибки 2619 неактивен? |
|  | **STEP 7F.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте, что кнопка остановки двигателя находится в положении STOP.

#### ШАГ 1A. Проверьте, что кнопка остановки двигателя находится в положении STOP.

| **Условия:** Включить переключатель зажигания. Все компоненты подключены. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, что кнопка остановки двигателя находится в положении STOP. | Кнопка остановки двигателя в положении STOP? **Ремонт:** Сбросьте кнопку остановки двигателя. | 8а |
| Кнопка остановки двигателя в положении STOP? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте информацию о блоке управления дизельным топливом (DCU) (только для морских судов).

| **Условия:** Включить переключатель зажигания. Все компоненты подключены. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте информацию DCU. Проверьте журнал событий в DCU для события кнопки остановки двигателя или теста на сверхскоростную защиту двигателя. Используйте следующую процедуру в руководстве по ремонту панелей Marine C Command EliteTM и C Command Elite PlusTM Panel Systems Master Repair Manual, Bulletin [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual\|4021617]].[[116-101-013 — General Operating Instructions\|См. процедуру 101-013 в разделе 1.]] | DCU показывает событие с кнопкой остановки или тест свидетеля? **Ремонт:** Сбросьте кнопку остановки двигателя или выйдите из измерительного режима. Используйте следующую процедуру в руководстве по ремонту панелей Marine C Command EliteTM и C Command Elite PlusTM Panel Systems Master Repair Manual, Bulletin [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual\|4021617]].[[116-101-013 — General Operating Instructions\|См. процедуру 101-013 в разделе 1.]] | 7А |
| DCU показывает событие с кнопкой остановки или тест свидетеля? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте другие коды неисправностей.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кода ошибки. | Активные или неактивные коды ошибок? *Да | Устранение неисправностей других кодов и возврат к этому коду неисправности. |
| Активные или неактивные коды ошибок? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте правильное положение клапанов отключения воздуха.

#### ШАГ 2A. Проверьте правильное положение клапанов отключения воздуха.

| **Условия:** Включить переключатель зажигания. Все компоненты подключены. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что все клапаны отключения воздуха находятся в открытом положении. | Запорные клапаны в положении OPEN? *Да | 3А |
| Запорные клапаны в положении OPEN? **NORepair:** См. руководство по обслуживанию OEM. | 7А |  |

### ШАГ 3. Проверьте кнопку остановки двигателя для короткого замыкания.

#### ШАГ 3A. Проверьте кнопку остановки двигателя для короткого замыкания.

| **Условия:** Выключите замок зажигания. Отсоедините провода от терминалов остановки двигателя NO (Normally Open). Выключатель остановки двигателя NO является средним выключателем трех терминалов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на короткое замыкание. Измерьте сопротивление между терминалами переключателей NO (обычно открытые). См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 4А |
| Больше 100 тысяч ом? **NORepair:** Заменить кнопку остановки двигателя. Используйте процедуру в руководстве по ремонту панелей Marine C Command EliteTM и C Command Elite PlusTM Panel Systems Master Repair Manual, Bulletin [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual\|4021617]].[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | 7А |  |

### ШАГ 4. Проверьте жгут проводов двигателя.

#### ШАГ 4A. Проверьте жгут электропроводки двигателя и разъемы ECM.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты электропроводки двигателя и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** Ремонт поврежденных контактов. Смой грязь, мусор или влагу из контактов разъема. Ремонт или замена ремня электропроводки двигателя, или замена ECM, в зависимости от того, какие контакты повреждены. Смой грязь, мусор или влагу из контактов разъема. Используйте электрическую контактную очистку, номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут электропроводки двигателя. См. процедуру 019-043 в разделе 19. Заменить ECM. См. процедуру 019-031 в разделе 19. | 7А |
| Грязные или поврежденные контакты? **НЕТ** | 5В |  |

#### ШАГ 4B. Проверьте короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от электропроводки двигателя на 23-контактном разъеме. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на землю. Измерить сопротивление от OEM переключателя / двойного вывода B-контакта разъема проводов двигателя к заземлению блока двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 4C |
| Больше 100 тысяч ом? **NORepair:** Заменить электропроводку двигателя.[[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043 в разделе 19.]] | 7А |  |

#### ШАГ 4C. Проверьте короткое замыкание от контакта к контакту.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от электропроводки двигателя на 23-контактном разъеме. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание от контакта к контакту. Измерьте сопротивление от OEM-переключателя / двойного выходного B-контакта разъема жгута проводов двигателя ко всем другим штифтам в разъеме. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 5а |
| Больше 100 тысяч ом? **NORepair:** Заменить электропроводку двигателя.[[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043 в разделе 19.]] | 7А |  |

### ШАГ 5. Проверьте OEM проводку.

#### ШАГ 5A. Проверьте OEM-проводку и 23-контактные разъемы.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от электропроводки двигателя на 23-контактном разъеме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите проводную упряжку OEM и 23-контактные соединительные контакты для следующего: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** Ремонт поврежденных контактов. Смой грязь, мусор или влагу из контактов разъема. Ремонт или замена OEM проводов жгута. Смой грязь, мусор или влагу из контактов разъема. Используйте электрическую контактную очистку, номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт проводной упряжки OEM. См. процедуру 019-204 в разделе 19. Замените проводку OEM. См. процедуру 019-071 в разделе 19. | 7А |
| Грязные или поврежденные контакты? **НЕТ** | 5В |  |

#### ШАГ 5B. Проверьте короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от электропроводки двигателя на 23-контактном разъеме. Отсоедините проводку OEM от переключателя OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на землю. Измерьте сопротивление от переключателя OEM / двойного выходного штифта B 23-контактного разъема OEM-проводов, OEM-стороны, к заземлению блока двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 5С |
| Больше 100 тысяч ом? **NORepair:** Заменить проводку OEM.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]] | 7А |  |

#### ШАГ 5C. Проверьте короткое замыкание от контакта к контакту.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от электропроводки двигателя на 23-контактном разъеме. Отсоедините проводку OEM от переключателя OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание от контакта к контакту. Измерьте сопротивление от OEM-переключателя / двойного выходного B-контакта 23-контактного разъёма OEM-проводов, OEM-стороны, ко всем другим штифтам в разъеме. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 6А |
| Больше 100 тысяч ом? **NORepair:** Заменить проводку OEM.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]] | 7А |  |

### ШАГ 6. Проверьте внутреннюю проводку клиентского интерфейса (CIB).

#### ШАГ 6A. Проверьте внутреннюю проводку CIB между кнопкой E-stop и 23-контактным OEM-разъемом (Marine).

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от электропроводки двигателя на 23-контактном разъеме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить 23-контактные контакты разъёма на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** Ремонт поврежденных контактов. Смой грязь, мусор или влагу из контактов разъема. Ремонт или замена OEM проводов жгута. Смой грязь, мусор или влагу из контактов разъема. Используйте электрическую контактную очистку, номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт проводной упряжки OEM. См. процедуру 019-204 в разделе 19. Замените проводку OEM. См. процедуру 019-071 в разделе 19. | 7А |
| Грязные или поврежденные контакты? **НЕТ** | 6B |  |

#### ШАГ 6B. Проверьте короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от электропроводки двигателя на 23-контактном разъеме. Отсоедините проводку OEM от переключателя OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на землю. Измерьте сопротивление от переключателя OEM / двойного выходного штифта B 23-контактного разъема OEM-проводов, OEM-стороны, к заземлению блока двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 6C |
| Больше 100 тысяч ом? **NORepair:** Заменить проводку CIB.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]] | 7А |  |

#### ШАГ 6C. Проверьте короткое замыкание от контакта к контакту.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от CIB на 23-контактном разъеме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание от контакта к контакту. Измерьте сопротивление от OEM-переключателя / двойного выходного штифта B 23-контактного разъема OEM-проводов, OEM-стороны, ко всем другим штифтам в разъеме. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 7А |
| Больше 100 тысяч ом? **NORepair:** Заменить проводку CIB.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]] | 7А |  |

### ШАГ 7. Очистите коды неисправностей и проверьте прогрессивный ущерб.

#### ШАГ 7A. Подтвердить условия.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подтвердите условия работы двигателя. Используйте инструмент электронного обслуживания INSITETM для просмотра данных моментального снимка кода неисправности для проверки условий работы двигателя при возникновении кода ошибки 2619. | Данные снимка показывают, что код ошибки 2619 был установлен на уровне или ниже холостого хода и 10-процентного крутящего момента. *Да | 7Е |
| Данные снимка показывают, что код ошибки 2619 был установлен на уровне или ниже холостого хода и 10-процентного крутящего момента. **NORepair:** Проверьте двигатель на наличие прогрессивных повреждений. | 7B |  |

#### ШАГ 7B. Полные проверки с выключенным двигателем.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проведите следующие проверки: Осмотрите шланги горба на наличие признаков повреждения или утечки. Проверьте зазор конца турбокомпрессора. Используйте следующую процедуру в руководстве по обслуживанию QSK45 и QSK60, в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 010-033 в разделе 10. Используйте следующую процедуру в руководстве по обслуживанию QSK38 и QSK50, в бюллетене [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 010-033 в разделе 10. Осмотр колеса компрессора турбокомпрессора. | Горбатые шланги и турбокомпрессоры соответствуют спецификациям? *Да | 7C |
| Горбатые шланги и турбокомпрессоры соответствуют спецификациям? Заменить поврежденные компоненты. Используйте следующие процедуры в руководстве по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]: См. процедуру 010-034 в разделе 10. См. процедуру 010-035 в разделе 10. | 7C |  |

#### ШАГ 7C. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Использование инструментария электронного сервиса INSITETM для проверки неактивности кода 2619. | Код ошибки 2619 неактивен? *Да | 7D |
| Код ошибки 2619 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 7D. Проверьте прокладки на загрузке.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Управляйте двигателем с нагрузкой и проверяйте прокладки. Запустите двигатель и загрузите его. Проверяйте и слушайте любой шум, связанный с утечкой прокладки головы или послеохлаждения. | Ущерб обнаружен прокладкам?  Заменить прокладки по мере необходимости. Используйте следующие процедуры в руководстве по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]: Для ремонта прокладки головы: См. процедуру 002-021 в разделе 2. Для ремонта прокладки после охлаждения: См. процедуру 010-002 в разделе 10. Используйте следующие процедуры в Руководстве по обслуживанию QSK38 и QSK50, Вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]: Для ремонта прокладки головы: См. процедуру 002-021 в разделе 2. Для ремонта прокладки после охлаждения: См. процедуру 010-002 в разделе 10. | 7Е |
| Ущерб обнаружен прокладкам? **НЕТ** | 7Е |  |

#### ШАГ 7E. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте электронный инструмент для проверки неактивности кода 2619. | Код ошибки 2619 неактивен? *Да | 7F |
| Код ошибки 2619 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 7F. Сбросьте неактивные коды неисправностей.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair:** Устранение неполадок с оставшимися кодами неисправностей. | Правильное дерево для устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, and Part Number 3823995 - male Weather Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Verify if the engine stop button is in the STOP position. |  |
> |  | **STEP 1A.** Verify if the engine stop button is in the STOP position. | Engine stop button in the STOP position? |
> |  | **STEP 1B.** Check Diesel Control Unit (DCU) information. | DCU shows a stop button event or witness test? |
> |  | **STEP 1C.** Check for other fault codes. | Active or inactive fault codes? |
> | STEP 2. | Check for correct position of the air shutoff valves. |  |
> |  | **STEP 2A.** Check for correct position of the air shutoff valves. | Air shutoff valves in the OPEN position? |
> | STEP 3. | Check the engine stop button for short circuit. |  |
> |  | **STEP 3A.** Check the engine stop button for short circuit. | Greater than 100k ohms? |
> | STEP 4. | Check the engine harness. |  |
> |  | **STEP 4A.** Inspect the engine harness and ECM connectors. | Dirty or damaged pins? |
> |  | **STEP 4B.** Check for a short circuit to ground. | Greater than 100k ohms? |
> |  | **STEP 4C.** Check for a pin-to-pin short circuit. | Greater than 100k ohms? |
> | STEP 5. | Check the OEM harness. |  |
> |  | **STEP 5A.** Inspect the OEM harness and 23-pin connectors. | Dirty or damaged pins? |
> |  | **STEP 5B.** Check for a short circuit to ground. | Greater than 100k ohms? |
> |  | **STEP 5C.** Check for a pin-to-pin short circuit. | Greater than 100k ohms? |
> | STEP 6. | Check the Customer Interface Box (CIB) internal wiring. |  |
> |  | **STEP 6A.** Check the Customer Interface Box (CIB) internal wiring between the E-stop button and the 23-pin OEM connector. | Dirty or damaged pins? |
> |  | **STEP 6B.** Check for a short circuit to ground. | Greater than 100k ohms? |
> |  | **STEP 6C.** Check for a pin-to-pin short circuit. | Greater than 100k ohms? |
> | STEP 7. | Clear the fault codes and check for progressive damage. |  |
> |  | **STEP 7A.** Confirm conditions. | Snapshot data shows Fault Code 2619 was set at or below idle and 10 percent torque? |
> |  | **STEP 7B.** Complete checks with engine off. | Hump hoses and turbochargers meet specifications? |
> |  | **STEP 7C.** Disable the fault code. | Fault Code 2619 inactive? |
> |  | **STEP 7D.** Check gaskets at load. | Damage to gaskets detected? |
> |  | **STEP 7E.** Disable the fault code. | Fault Code 2619 inactive? |
> |  | **STEP 7F.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Verify the engine stop button is in the STOP position.
>
> #### STEP 1A. Verify the engine stop button is in the STOP position.
>
> | **Conditions:** Turn keyswitch ON. All components connected. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify the engine stop button is in the STOP position. | Engine stop button in the STOP position? **YESRepair:** Reset the engine stop button. | 8A |
> | Engine stop button in the STOP position? **NO** | 1B |  |
>
> #### STEP 1B. Check Diesel Control Unit (DCU) information (marine **only**).
>
> | **Conditions:** Turn keyswitch ON. All components connected. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check DCU information. Check the event log in the DCU for an engine stop button event or an engine protection overspeed witness test. Use the following procedure in the Marine C Command Elite™ and C Command Elite Plus™ Panel Systems Master Repair Manual, Bulletin [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual\|4021617]]. [[116-101-013 — General Operating Instructions\|Refer to Procedure 101-013 in Section 1.]] | DCU shows a stop button event or witness test? **YESRepair:** Reset the engine stop button or move out of test mode. Use the following procedure in the Marine C Command Elite™ and C Command Elite Plus™ Panel Systems Master Repair Manual, Bulletin [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual\|4021617]]. [[116-101-013 — General Operating Instructions\|Refer to Procedure 101-013 in Section 1.]] | 7A |
> | DCU shows a stop button event or witness test? **NO** | 1C |  |
>
> #### STEP 1C. Check for other fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fault codes. Use INSITE™ electronic service tool to read the fault code. | Active or inactive fault codes? **YES** | Troubleshoot other fault codes and return to this fault code. |
> | Active or inactive fault codes? **NO** | 2A |  |
>
> ### STEP 2. Check for correct position of the air shutoff valves.
>
> #### STEP 2A. Check for correct position of the air shutoff valves.
>
> | **Conditions:** Turn keyswitch ON. All components connected. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check that all of the air shutoff valves are in the OPEN position. | Air shutoff valves in the OPEN position? **YES** | 3A |
> | Air shutoff valves in the OPEN position? **NORepair:** Refer to the OEM service manual. | 7A |  |
>
> ### STEP 3. Check the engine stop button for short a circuit.
>
> #### STEP 3A. Check the engine stop button for a short circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect wires from NO (Normally Open) engine stop switch terminals. The NO engine stop switch is the middle switch of the three terminals. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit. Measure the resistance between the NO (Normally Open) switch terminals. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 4A |
> | Greater than 100k ohms? **NORepair:** Replace the engine stop button. Use the procedure in the Marine C Command Elite™ and C Command Elite Plus™ Panel Systems Master Repair Manual, Bulletin [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual\|4021617]]. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | 7A |  |
>
> ### STEP 4. Check the engine harness.
>
> #### STEP 4A. Inspect the engine harness and ECM connectors.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Use electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine wiring harness. Refer to Procedure 019-204 in Section 19. Replace the engine wiring harness. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 7A |
> | Dirty or damaged pins? **NO** | 5B |  |
>
> #### STEP 4B. Check for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground. Measure the resistance from the OEM switch/dual output B pin of the engine harness connector to engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 4C |
> | Greater than 100k ohms? **NORepair:** Replace the engine wiring harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 7A |  |
>
> #### STEP 4C. Check for a short circuit from pin-to-pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin-to-pin. Measure the resistance from the OEM switch/dual output B-pin of the engine harness connector to all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 5A |
> | Greater than 100k ohms? **NORepair:** Replace the engine wiring harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 7A |  |
>
> ### STEP 5. Check the OEM harness.
>
> #### STEP 5A. Inspect the OEM harness and 23-pin connectors.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness and 23-pin connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Repair or replace the OEM harness. Flush the dirt, debris, or moisture from the connector pins. Use electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 7A |
> | Dirty or damaged pins? **NO** | 5B |  |
>
> #### STEP 5B. Check for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. Disconnect the OEM harness from the OEM switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground. Measure the resistance from the OEM switch/dual output B pin of the 23-pin OEM harness connector, OEM side, to engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 5C |
> | Greater than 100k ohms? **NORepair:** Replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 7A |  |
>
> #### STEP 5C. Check for a short circuit from pin-to-pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. Disconnect the OEM harness from the OEM switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin-to-pin. Measure the resistance from the OEM switch/dual output B-pin of the 23-pin OEM harness connector, OEM side, to all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 6A |
> | Greater than 100k ohms? **NORepair:** Replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 7A |  |
>
> ### STEP 6. Check the Customer Interface Box (CIB) internal wiring.
>
> #### STEP 6A. Check the CIB internal wiring between the E-stop button and the 23-pin OEM connector (Marine).
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the 23-pin connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Repair or replace the OEM harness. Flush the dirt, debris, or moisture from the connector pins. Use electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 7A |
> | Dirty or damaged pins? **NO** | 6B |  |
>
> #### STEP 6B. Check for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. Disconnect the OEM harness from the OEM switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground. Measure the resistance from the OEM switch/dual output B pin of the 23-pin OEM harness connector, OEM side, to engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 6C |
> | Greater than 100k ohms? **NORepair:** Replace the CIB harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 7A |  |
>
> #### STEP 6C. Check for a short circuit from pin-to-pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the CIB at the 23-pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin-to-pin. Measure the resistance from the OEM switch/dual output B pin of the 23-pin OEM harness connector, OEM side, to all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 7A |
> | Greater than 100k ohms? **NORepair:** Replace the CIB harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 7A |  |
>
> ### STEP 7. Clear the fault codes and check for progressive damage.
>
> #### STEP 7A. Confirm conditions.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Confirm the conditions of the engine. Use INSITE™ electronic service tool to view the fault code snapshot data to verify the conditions of the engine when Fault Code 2619 occured. | Snapshot data shows that Fault Code 2619 was set at or below idle and 10 percent torque? **YES** | 7E |
> | Snapshot data shows that Fault Code 2619 was set at or below idle and 10 percent torque? **NORepair:** Check the engine for progressive damage. | 7B |  |
>
> #### STEP 7B. Complete checks with engine OFF.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Perform the following inspections: Inspect the hump hoses for signs of damage or leakage. Check the turbocharger shaft end clearance. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 010-033 in Section 10. Use the following procedure in the QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 010-033 in Section 10. Inspect the turbocharger compressor impeller wheel. | Hump hoses and turbochargers meet specifications? **YES** | 7C |
> | Hump hoses and turbochargers meet specifications? **NORepair:** Replace the damaged components. Use the following procedures in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]: Refer to Procedure 010-034 in Section 10. Refer to Procedure 010-035 in Section 10. | 7C |  |
>
> #### STEP 7C. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Start the engine, and let it idle for 1 minute. Use INSITE™ electronic service tool to verify Fault Code 2619 is inactive. | Fault Code 2619 inactive? **YES** | 7D |
> | Fault Code 2619 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
>
> #### STEP 7D. Check gaskets at load.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Operate the engine with load and check the gaskets. Start the engine and load it. Check and listen for any noise associated with head gasket or aftercooler gasket leaks. | Damage to gaskets detected? **YESRepair:** Replace gaskets as necessary. Use the following procedures in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]: For head gasket repair: Refer to Procedure 002-021 in Section 2. For aftercooler gasket repair: Refer to Procedure 010-002 in Section 10. Use the following procedures in the QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]: For head gasket repair: Refer to Procedure 002-021 in Section 2. For aftercooler gasket repair: Refer to Procedure 010-002 in Section 10. | 7E |
> | Damage to gaskets detected? **NO** | 7E |  |
>
> #### STEP 7E. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic serivce tool to verify Fault Code 2619 is inactive. | Fault Code 2619 inactive? **YES** | 7F |
> | Fault Code 2619 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
>
> #### STEP 7F. Clear the inactive fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Appropriate troubleshooting tree |  |
