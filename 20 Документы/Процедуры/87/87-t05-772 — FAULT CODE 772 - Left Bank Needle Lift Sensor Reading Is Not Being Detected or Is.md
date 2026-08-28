---
aliases:
  - "Код 772 — нет показаний датчика подъёма иглы левого ряда или они вне диапазона"
type: "Процедура"
doc: "87-t05-772"
title_en: "FAULT CODE 772 - Left Bank Needle Lift Sensor Reading Is Not Being Detected or Is Out of Range"
title_ru: "Код 772 — нет показаний датчика подъёма иглы левого ряда или они вне диапазона"
modified: "2018-08-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-772.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-t05-772.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# FAULT CODE 772 - Left Bank Needle Lift Sensor Reading Is Not Being Detected or Is Out of Range
**Код 772 — нет показаний датчика подъёма иглы левого ряда или они вне диапазона**

> [!abstract] Процедура · `87-t05-772`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-772.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-t05-772.pdf)

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
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822758 - пробный щуп типа пробки DeutschTM/AMPTM/Metri-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте несколько кодов ошибок. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Коды 115 и 121 активны? |
| ШАГ 2. | Проверьте датчик подъема иглы. |  |
|  | **STEP 2A.** Осмотрите контактные линзы разъёма иглы и проводов двигателя. | Грязные или поврежденные контакты? |
| ШАГ 3. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 3A.** Проверить упряжку электропроводки двигателя и разъемы ECM. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте наличие открытой цепи. | Сопротивление более 100 Км? |
|  | **ШАГ 3С.** Проверить на короткое замыкание. | Сопротивление менее 10 Ом? |
| ШАГ 4. | Проверьте, доступно ли обновление калибровки ECM. |  |
|  | **STEP 4A.** Проверьте наличие обновлений калибровки ECM. | Представляет ли калибровка самый последний пересмотр? |
| ШАГ 5. | Проверьте топливный насос. |  |
|  | **STEP 5A.** Проверить линию подачи топлива между топливным насосом и клапаном подъема иглы. | Ограничение топливной линии? |
|  | **STEP 5B.** Проверьте время работы топливного насоса. | Сроки, указанные в коде топливного насоса на табличке? |
| ШАГ 6. | Очистите код ошибки. |  |
|  | **STEP 6A.** Отключить коды неисправностей. | Код 772 неактивен? |
|  | **STEP 6B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте несколько кодов ошибок.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Коды 115 и 121 активны?  Исправление неисправностей Код 115 и Код 121 | Многократное дерево кода ошибки |
| Коды 115 и 121 активны? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте игольноподъемный форсунка

#### ШАГ 2A. Проверьте жгут проводов двигателя и контакты датчика подъема иглы.

| **Условия:** Выключите замок зажигания. Отсоедините проводку двигателя от датчика подъема иглы. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды неисправностей и проверьте контакты разъема на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** Ремонт поврежденных контактов. Смой грязь, мусор или влагу из контактов разъема. Используйте электрическую контактную очистку, номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. Используйте следующие процедуры. См. процедуру 019-201 в разделе 19 См. процедуру 019-202 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. Заменить форсунка № 1 на левом берегу. Используйте следующую процедуру в руководстве по обслуживанию QST30, в бюллетене [[4021539 — QST30 Service Manual\|4021539]]. См. процедуру 006-026 в разделе 6. | 6А |
| Грязные или поврежденные контакты? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте жгут проводов двигателя.

#### ШАГ 3A. Проверьте жгут электропроводки двигателя и разъемы ECM.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты электропроводки двигателя и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** Ремонт поврежденных контактов. Ремонт или замена ремня электропроводки двигателя, или замена ECM, в зависимости от того, какие контакты повреждены. Смой грязь, мусор или влагу из контактов разъема. Используйте электрическую контактную очистку, номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. Заменить ECM. См. процедуру 019-031 в разделе 19. | 6А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отсоедините проводку двигателя от датчика подъема иглы. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление от сигнального контакта проводов двигателя разъема жгута к сигнальному контакту разъема датчика подъема иглы, проводов двигателя стороны жгута. Измерить сопротивление от обратного контакта разъёма ремня электропроводки двигателя к обратному контакту датчика подъема иглы, стороны ремня электропроводки двигателя. | Сопротивление более 100k ом? **Ремонт:** Ремонт или замена ремня электропроводки двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-201 в разделе 19. См. процедуру 019-202 в разделе 19. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 6А |
| Сопротивление более 100k ом? **НЕТ** | 3C |  |

#### ШАГ 3C. Проверьте цепь на короткое замыкание.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отсоедините проводку OEM от ECM. Отсоедините жгут электропроводки двигателя от датчика давления впускного коллектора. Отсоедините проводку двигателя от датчика подъема иглы. Отсоедините проводку двигателя от датчика температуры впускного коллектора. Отсоедините проводку двигателя от датчика давления окружающего воздуха. Отсоедините проводку двигателя от датчика давления охлаждающей жидкости. Отсоедините проводку двигателя от датчика давления масла. Отсоедините жгут проводов двигателя от разъема CENSETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание от контакта к контакту. Измерьте сопротивление от сигнального контакта разъёма жгута проводов двигателя ко всем другим штифтам в разъеме и ко всем штифтам в разъеме OEM-проводов. Измерьте сопротивление от обратного контакта разъёма жгутов проводов двигателя со всеми другими штифтами в разъеме и со всеми штифтами в разъеме OEM-проводов. | Сопротивление менее 10 Ом? **Ремонт:** Ремонт или замена ремня электропроводки двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 6А |
| Сопротивление менее 10 Ом? **НЕТ** | 4А |  |

### ШАГ 4. Проверьте этап калибровки программного обеспечения.

#### ШАГ 4A. Проверить текущую фазу калибровки программного обеспечения.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подтвердите текущую фазу калибровки программного обеспечения. Используйте инструмент электронного обслуживания INSITETM для проверки текущей фазы калибровочного программного обеспечения. | Текущая фаза калибровки 5.1.0.5 (0501005) или выше? *Да | 5а |
| Текущая фаза калибровки 5.1.0.5 (0501005) или выше? **НЕТ** | 6А |  |

### ШАГ 4. Проверьте фазу калибровки программного обеспечения.

#### ШАГ 4A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички данных в функциях и параметрах. | Является ли нынешняя калибровка самой последней редакцией? *Да | 5а |
| Является ли нынешняя калибровка самой последней редакцией? **NORepair:** При необходимости откалибровать ECM. См. процедуру 019-032 в Таблице ассоциированных процедур. | 6А |  |

### ШАГ 5. Проверьте топливный насос.

#### ШАГ 5A. Проверьте топливопровод.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить линию подачи топлива между топливным насосом и левобережным топливным форсункой № 1 на предмет: Обструкции Обрезка сухая трубка. | Ограничение топливной линии?  Заменить топливный бак. | 6А |
| Ограничение топливной линии? **НЕТ** | 5В |  |

#### ШАГ 5B. Проверьте время впрыска топлива.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте время работы топливного насоса. Используйте следующую процедуру в руководстве по обслуживанию QST30, в бюллетене [[4021539 — QST30 Service Manual\|4021539]]. См. процедуру 005-012 в разделе 5. | Соответствует ли указанное время коду топливного насоса на табличке с данными? *Да | 6А |
| Соответствует ли указанное время коду топливного насоса на табличке с данными? **NORepair:** Установить время работы топливного насоса, как указано в следующем руководстве по эксплуатации QST30, Bulletin [[4021539 — QST30 Service Manual\|4021539]].[[57-005-012-tr — Fuel Injection Pumps, In-Line\|См. процедуру 005-012 в разделе 5.]] | 6А |  |

### ШАГ 6. Сбросьте коды неисправностей.

#### ШАГ 6A. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. С 5.1.0.5 фаза программного обеспечения, работа двигателя выше 1000 об/мин в течение 1 минуты. Проверить код 772 неактивен. | Код 772 неактивен? *Да | 5В |
| Код 772 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 6B. Сбросьте неактивные коды неисправностей.

| **Условия:** Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён. |
| Все коды неисправностей очищены? **NORepair:** Устранение неполадок с оставшимися активными кодами неисправностей. | Перейдите к соответствующим диаграммам устранения неполадок. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check for multiple fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Codes 115 and 121 active? |
> | STEP 2. | Check the needle lift sensor. |  |
> |  | **STEP 2A.** Inspect the engine harness and the needle lift sensor connector pins. | Dirty or damaged pins? |
> | STEP 3. | Check the engine harness. |  |
> |  | **STEP 3A.** Inspect the engine harness and ECM connectors. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check for an open circuit. | Resistance greater than 100K ohms? |
> |  | **STEP 3C.** Check for a short circuit. | Resistance less than 10 ohms? |
> | STEP 4. | Check if an ECM calibration update is availablet. |  |
> |  | **STEP 4A.** Check if an ECM calibration update is available. | Present calibration the most recent revision? |
> | STEP 5. | Check the fuel pump. |  |
> |  | **STEP 5A.** Inspect the fuel line between the fuel pump and the needle lift valve. | Fuel line restriction? |
> |  | **STEP 5B.** Check the fuel pump timing. | Timing specified matches fuel pump code on the dataplate? |
> | STEP 6. | Clear the fault code. |  |
> |  | **STEP 6A.** Disable the fault codes. | Fault Code 772 inactive? |
> |  | **STEP 6B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check for multiple fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Codes 115 and 121 active? **YESRepair:** Troubleshoot Fault Code 115 and Fault Code 121 | Multiple fault code tree |
> | Fault Codes 115 and 121 active? **NO** | 2A |  |
>
> ### STEP 2. Check the needle lift injector
>
> #### STEP 2A. Inspect the engine harness and the needle lift sensor connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the needle lift sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes and inspect the connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Use electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Use the following procedures. Refer to Procedure 019-201 in Section 19 Refer to Procedure 019-202 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the number 1 injector on the left bank. Use the following procedure in the QST30 Service Manual, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. Refer to Procedure 006-026 in Section 6. | 6A |
> | Dirty or damaged pins? **NO** | 3A |  |
>
> ### STEP 3. Check the engine harness.
>
> #### STEP 3A. Inspect the engine harness and ECM connectors.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Use electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 6A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness from the needle lift sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance from the SIGNAL pin of the engine harness connector to the SIGNAL pin of the needle lift sensor connector, engine harness side. Measure the resistance from the RETURN pin of the engine harness connector to the RETURN pin of the needle lift sensor, engine harness side. | Resistance greater than 100k ohms? **YESRepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-201 in Section 19. Refer to Procedure 019-202 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 6A |
> | Resistance greater than 100k ohms? **NO** | 3C |  |
>
> #### STEP 3C. Check for a short circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the OEM harness from the ECM. Disconnect the engine harness from the intake manifold pressure sensor. Disconnect the engine harness from the needle lift sensor. Disconnect the engine harness from the intake manifold temperature sensor. Disconnect the engine harness from the ambient air pressure sensor. Disconnect the engine harness from the coolant pressure sensor. Disconnect the engine harness from the oil pressure sensor. Disconnect the engine harness from the CENSE™ connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin-to-pin. Measure the resistance from the SIGNAL pin of the engine harness connector to all other pins in the connector, and to all pins in the OEM harness connector. Measure the resistance from the RETURN pin of the engine harness connector to all other pins in the connector, and to all pins in the OEM harness connector. | Resistance less than 10 ohms? **YESRepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 6A |
> | Resistance less than 10 ohms? **NO** | 4A |  |
>
> ### STEP 4. Check the calibration software phase.
>
> #### STEP 4A. Verify the current calibration software phase.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Confirm the current calibration software phase. Use INSITE™ electronic service tool to verify the current calibration software phase. | Current calibration software phase 5.1.0.5 (0501005) or greater? **YES** | 5A |
> | Current calibration software phase 5.1.0.5 (0501005) or greater? **NO** | 6A |  |
>
> ### STEP 4. Check calibration software phase.
>
> #### STEP 4A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | Is the present calibration the most recent revision? **YES** | 5A |
> | Is the present calibration the most recent revision? **NORepair:** If necessary, calibrate the ECM. Refer to Procedure 019-032 in the Associated Procedures Table. | 6A |  |
>
> ### STEP 5. Check the fuel pump.
>
> #### STEP 5A. Inspect the fuel line.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the fuel line between the fuel pump and number 1 left bank injector for the following: Obstructions Debris Crimped tube. | Fuel line restriction? **YESRepair:** Replace the fuel line. | 6A |
> | Fuel line restriction? **NO** | 5B |  |
>
> #### STEP 5B. Check fuel injection pump timing.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the fuel pump timing. Use the following procedure in QST30 Service Manual, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. Refer to Procedure 005-012 in Section 5. | Does the timing specified match the fuel pump code on the dataplate? **YES** | 6A |
> | Does the timing specified match the fuel pump code on the dataplate? **NORepair:** Set the fuel pump timing as specified in the following procedure in QST30 Service Manual, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. [[57-005-012-tr — Fuel Injection Pumps, In-Line\|Refer to Procedure 005-012 in Section 5.]] | 6A |  |
>
> ### STEP 6. Clear the fault codes.
>
> #### STEP 6A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Start the engine and let it idle for 1 minute. With the 5.1.0.5 software phase, operate the engine above 1000 rpm for 1 minute. Verify Fault Code 772 is inactive. | Fault Code 772 inactive? **YES** | 5B |
> | Fault Code 772 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 6B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Go to the appropriate troubleshooting charts. |  |
