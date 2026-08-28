---
type: "Процедура"
doc: "97-fc585aft"
title_en: "Starter Relay Circuit - Voltage Below Normal or Shorted to Low Source"
modified: "2007-01-26"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc585aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc585aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Starter Relay Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `97-fc585aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2007-01-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc585aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc585aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 585 (Послепродажное и OEM)

### Стартовая релейная схема - напряжение ниже нормального или короткое до низкого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 585 PID(P): СПН: ФМИ: Лампа: СТО: | Стартовая релейная схема - напряжение ниже нормального или короткое до низкого источника. Менее 6-VDC обнаруживается в цепи стартового реле, когда высокое напряжение ожидалось от модуля управления холостым ходом ICONTM. | Система ICONTM будет отключена. Включено только обязательное отключение. Может быть, не может нормально запустить двигатель. |

![[19c01537.png]]

### Описание цепи

Стартерная реле соединяет мощность с стартовым магнитным переключателем для запуска двигателя. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Стартовое реле обычно устанавливается на переборке транспортного средства на впускной стороне двигателя.

Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Эта неисправность обычно указывает на открытую цепь или короткое замыкание на землю. Если на стартовой реле (-) цепи есть короткое замыкание, то стартер будет продолжать задействоваться; в противном случае двигатель будет **не** запускать.

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного кода неисправности, система ICONTM выдает наиболее приоритетную ошибку. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

**Примечание: **Электронная система ICONTM может отображать более одного активного и неактивного кода неисправности одновременно.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822917 - пробный щуп типа гнезда Deutsch/AMP/Metri-Pack Номер детали 3822758 - пробный щуп типа пробки Deutsch/AMP/Metri-Pack.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Считайте коды неисправностей. |  |
|  | **STEP 1A.** Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код ошибки 585 неактивен |
|  | **STEP 1B.** Проверить выход и вход с помощью инструментария ICONTM. | Проверить, что вход зажигания пустой (не помеченный), проверить, что реле зажигания пустой (не помеченный), проверить переключатель зажигания на двигатель ECM помечено |
| ШАГ 2. | Стартовый тест. |  |
|  | **ШАГ 2А.** Проведите тест на старт. | Стартап работает правильно |
| ШАГ 3. | Проверьте стартовую эстафету. |  |
|  | **STEP 3A.** Осмотрите стартовые ретрансляционные штифты. | Никаких поврежденных контактов |
|  | **STEP 3B.** Проверьте сопротивление катушки реле стартера. | От 30 до 99 Ом |
| ШАГ 4. | Проверьте проводные ремни ICONTM. |  |
|  | **STEP 4A.** Проверить коннекторы разъемов двигателя ICONTM и неработающего модуля управления ICONTM. | Никаких поврежденных контактов |
|  | **STEP 4B.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 4C.** Проверьте короткое замыкание на землю. | Более 100 тыс. ом |
|  | **STEP 4D.** Проверьте наличие открытой схемы. | менее 100 Ом |
| ШАГ 5. | Очистите код ошибки. |  |
|  | **STEP 5A.** Отключить код ошибки. | Код ошибки 585 обезврежен |

### ШАГ 1. Считайте коды неисправностей.

#### ШАГ 1A. Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код ошибки 585 неактивен. | 2А |
|  | 1В |  |

#### ШАГ 1B. Проверьте выход и вход с помощью инструментария электронного обслуживания ICONTM.

| **Условия:** Включить переключатель зажигания. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте вход стартера, выход реле стартера (закрытого) и переключатель зажигания на выход электронного модуля управления двигателем (ECM). | Проверить вход стартера пустой (не помеченный) Проверить реле стартера пустой (не помеченный) Проверить переключатель зажигания на двигатель ECM помечено | 3А |
| Заменить модуль управления ICONTM idle. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |  |

### ШАГ 2. Стартовый тест.

#### ШАГ 2A. Проведите тест на старт.

| **Условия:** Включить переключатель зажигания. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проведите тест на старт. | Стартер работает правильно. Неактивные или прерывистые коды ошибок, процедура[[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 5а |
|  | 3А |  |

### ШАГ 3. Проверьте стартовую эстафету.

#### ШАГ 3A. Проверьте стартовые ретрансляционные штифты.

| **Условия:** Выключите замок зажигания. Отсоедините стартовую реле от ремня электропроводки двигателя ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите стартовое реле на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или разъема изоляции Поврежденный разъем блокировки вкладки. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 3B |
| Замените реле Смой грязь, мусор или влагу из контактов реле-коннектора с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Замените стартер реле. См. процедуру 019-302. | 5а |  |

#### ШАГ 3B. Проверьте сопротивление катушки реле стартера.

| **Условия:** Выключите замок зажигания. Отсоедините стартовую реле от ремня электропроводки двигателя ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сопротивление катушки реле Stater. Измерить сопротивление от контакта 85 до контакта 86 стартового реле. См. схему проводов или схему схемы для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | От 30 до 99 Ом | 4А |
| Замените стартер реле. См. процедуру[[97-019-302 — Starter Relay\|019-302]]. | 5а |  |

### ШАГ 4. Проверьте проводные ремни ICONTM.

#### ШАГ 4A. Осмотрите контактные линзы разъема для проводов двигателя ICONTM и коннектора модуля управления ICONTM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъема модуля управления ICONTM и проводов двигателя ICONTM для следующих целей: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или разъема изоляции Поврежденный разъем блокировки вкладки. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 4B |
| Ремонт поврежденных контактов. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 5а |  |

#### ШАГ 4B. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. Отключите разъем электронного модуля управления OEM (ECM). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание от пин-кодов до пин-кодов. Измерьте сопротивление от контакта 6 в разъеме для проводов Aftermarket или OEM ICONTM B со всеми другими штифтами в разъемах, кроме контакта 5 в разъеме для проводов B. См. схему проводов или схему схемы для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 4C |
| Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 5а |  |

#### ШАГ 4C. Проверьте короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на землю. Измерьте сопротивление от контакта 5 разъема проводов Aftermarket или OEM ICONTM B к заземлению блока двигателя. См. схему проводов или схему схемы для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 4D |
| Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 5а |  |

#### ШАГ 4D. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. Убедитесь, что реле стартера установлено. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление от контакта 6 модуля управления ICONTM холостого хода B проводов жгута разъёма до контакта 5 разъёма. См. схему проводов или схему схемы для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 100 Ом заменяют модуль управления ICONTM. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | 5а |
| Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | Ремонт завершён |  |

### ШАГ 5. Очистите код ошибки.

#### ШАГ 5A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Очистите код неактивной ошибки. Цикл переключателя зажигания для проверки кода неисправности неактивен. | Код ошибки 585 обезврежен | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 585 (Aftermarket and OEM)
>
> ### Starter Relay Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 585 PID(P): SPN: FMI: Lamp: SRT: | Starter Relay Circuit - Voltage Below Normal or Shorted to Low Source. Less than 6-VDC detected at the starter relay circuit when high voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Can possibly **not** be able to start the engine normally. |
>
> ### Circuit Description
>
> The starter relay connects power to the starter magnetic switch for starting the engine. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The starter relay is typically mounted on the vehicle's bulkhead on the intake side of the engine.
>
> The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault typically indicates an open circuit or a short circuit to ground. If there is a short circuit to ground on the starter relay (-) circuit, then the starter will continue to be engaged; otherwise the engine will **not** start.
>
> The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.
>
> **Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Read the fault codes. |  |
> |  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 585 inactive |
> |  | **STEP 1B.** Check the output and input with the ICON™ electronic service tool. | Verify starter input is blank (not marked), verify starter relay is blank (not marked), verify keyswitch to engine ECM is marked |
> | STEP 2. | Starter test. |  |
> |  | **STEP 2A.** Run the starter test. | Starter operates properly |
> | STEP 3. | Check the starter relay. |  |
> |  | **STEP 3A.** Inspect the starter relay pins. | No damaged pins |
> |  | **STEP 3B.** Check the starter relay coil resistance. | 30 to 99 ohms |
> | STEP 4. | Check the ICON™ harnesses. |  |
> |  | **STEP 4A.** Inspect the ICON™ engine harness and ICON™ idle control module connector pins. | No damaged pins |
> |  | **STEP 4B.** Check for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 4C.** Check for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 4D.** Check for an open circuit. | Less than 100 ohms |
> | STEP 5. | Clear the fault code. |  |
> |  | **STEP 5A.** Disable the fault code. | Fault Code 585 cleared |
>
> ### STEP 1. Read the fault codes.
>
> #### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use the fault flashout feature or the ICON™ electronic service tool read the fault codes. | Fault Code 585 inactive. | 2A |
> |  | 1B |  |
>
> #### STEP 1B. Check the output and input with the ICON™ electronic service tool.
>
> | **Conditions:** Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter input, starter relay (closed) output, and keyswitch to the engine electronic control module (ECM) output. | Verify starter input is blank (not marked) Verify starter relay is blank (not marked) Verify keyswitch to engine ECM is marked | 3A |
> | Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair complete |  |
>
> ### STEP 2. Starter test.
>
> #### STEP 2A. Run starter test.
>
> | **Conditions:** Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Run the starter test. | Starter operates properly. Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 5A |
> |  | 3A |  |
>
> ### STEP 3. Check the starter relay.
>
> #### STEP 3A. Inspect the starter relay pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the starter relay from the ICON™ engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the starter relay for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
> | Replace the relay Flush the dirt, debris, or moisture from the relay connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Replace the starter relay. Refer to Procedure 019-302. | 5A |  |
>
> #### STEP 3B. Check the starter relay coil resistance.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the starter relay from the ICON™ engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the stater relay coil resistance. Measure the resistance from pin 85 to pin 86 of the starter relay. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | 30 to 99 ohms | 4A |
> | Replace the starter relay. Refer to Procedure [[97-019-302 — Starter Relay\|019-302]]. | 5A |  |
>
> ### STEP 4. Check the ICON™ harnesses.
>
> #### STEP 4A. Inspect the ICON™ engine harness and ICON™ idle control module connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the ICON™ engine harness and ICON™ idle control module connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4B |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 5A |  |
>
> #### STEP 4B. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect the OEM electronic control module (ECM) connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin to pin. Measure the resistance from pin 6 in the Aftermarket or OEM ICON™ B harness connector to all other pins in the connectors except pin 5 in the B harness connector. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4C |
> | Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 5A |  |
>
> #### STEP 4C. Check for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground. Measure the resistance from pin 5 of the Aftermarket or OEM ICON™ B harness connector to engine block ground. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4D |
> | Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 5A |  |
>
> #### STEP 4D. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Make sure the starter relay is installed. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance from pin 6 of the ICON™ idle control module B harness connector to pin 5 of the connector. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 100 ohms Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | 5A |
> | Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | Repair complete |  |
>
> ### STEP 5. Clear the fault code.
>
> #### STEP 5A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault code. Cycle the keyswitch to verify the fault code is inactive. | Fault Code 585 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
