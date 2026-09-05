---
aliases:
  - "Цепь электромагнита клапана впрыска — обрыв"
type: "Процедура"
doc: "96-fc223"
title_en: "Burn Valve Solenoid Circuit - Open Circuit"
title_ru: "Цепь электромагнита клапана впрыска — обрыв"
modified: "2004-02-25"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc223.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc223.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# Burn Valve Solenoid Circuit - Open Circuit
**Цепь электромагнита клапана впрыска — обрыв**

> [!abstract] Процедура · `96-fc223`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc223.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc223.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 223

### Цепь электромагнита клапана впрыска — обрыв

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 223 PID(P): СПН: ФМИ: Лампа: Красная СТО: | Цепь электромагнита клапана впрыска — обрыв. Горящий соленоид открыт. | Система CentinelTM будет работать **не**. |

![[07800053.png]]

### Описание цепи

Соленоид горящего клапана контролирует поток масла в клапане управления маслом во время цикла горения.

### Расположение компонента

Сольноид горящего клапана расположен поверх клапана управления маслом.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерений: Испытательный щуп Male Cannon, Metri-Pack и Deutsch, Испытательный щуп Part Number 3822758 Female AMP, Metri-Pack и Deutsch, Испытательный щуп Part Number 3822917 Male Deutsch, Испытательный щуп Part Number 3823993 Female Deutsch, Испытательный щуп Part Number 3823994 Male Weather-Pack, Часть Number 3823995 Гнездовой испытательный щуп Weather-Pack, Часть Number 3823996.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте соленоид горящего клапана. |  |
|  | **STEP 1A.** Проверить, подключен ли соленоид горящего клапана к проводной упряжке CentinelTM. | Соленоид связан |
|  | **STEP 1B.** Осмотрите разъемы жгучего клапана соленоида и проводов CentinelTM. | Никаких поврежденных контактов |
|  | **STEP 1C.** Проверьте напряжение питания соленоидов в управляющем модуле CentinelTM. | Напряжение аккумулятора |
|  | **STEP 1D.** Проверьте соленоид горящего клапана на наличие открытого. | менее 120 Ом |
| ШАГ 2. | Проверьте проводную упряжку CentinelTM. |  |
|  | **STEP 2A.** Осмотрите жгут проводов CentinelTM и разъемы модуля управления CentinelTM. | Никаких поврежденных контактов |
|  | **ШАГ 2В.** Проверить наличие открытой цепи. | Менее 10 Ом |
|  | **ШАГ 2С.** Проверить короткое замыкание на землю. | Более 1к Ом |
|  | **STEP 2D.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 1к Ом |
| ШАГ 3. | Сбросьте коды неисправностей. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код ошибки 223 неактивен |

### ШАГ 1. Проверьте соленоид горящего клапана.

#### ШАГ 1A. Проверьте, что соленоид горящего клапана подключен к проводной упряжке CentinelTM.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[96-007-076 — Burn Solenoid\|007-076]]. | Соленоид связан | 1В |
| **Подключите соленоид к электропроводке CentinelTM** | 3А |  |

#### ШАГ 1B. Осмотрите соленоид горящего клапана и разъём проводов CentinelTM.

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от соленоида горящего клапана. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разъема или разъема разъема разъема или разъема разъема разъема или на разъеме разъема повреждения изоляции Проволоки Разъемная оболочка разорвана Поврежденная блокировка вкладки разъема. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 1С |
| **Починить поврежденные контакты** Починить или заменить проводную упряжку CentinelTM или соленоид горящего клапана, в зависимости от того, какие контакты повреждены. Ремонт проводной упряжки CentinelTM. См. процедуру 019-202. Замените проводную упряжку CentinelTM. См. процедуру 019-131. Замените горящий клапан соленоидом. См. процедуру 007-076. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. | 3А |  |

#### ШАГ 1C. Проверьте напряжение питания соленоида управляющего модуля CentinelTM.

| **Условия: **Запустить двигатель. Введите режим обслуживания. См. процедуру 007-999. Отсоедините соленоид горящего клапана от проводной упряжки CentinelTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение питания от контакта А до контакта В на стороне проводов жгута горелого клапана соленоида в течение 15 секунд после входа в режим обслуживания. См. схему проводов для идентификации контакта с разъемом. | Приблизительно = нормальное напряжение батареи в течение 15 секунд после входа в режим обслуживания. | 1D |
| **Заменить модуль управления CentinelTM или электропроводку **Заменить модуль управления CentinelTM. См. процедуру 019-130. Замените проводную упряжку CentinelTM. См. процедуру 019-131. | 3А |  |

#### ШАГ 1D. Проверьте соленоид горящего клапана на наличие открытого.

| **Условия:** Выключите замок зажигания. Отсоедините соленоид горящего клапана от проводной упряжки CentinelTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта А до контакта В сгорающего клапана соленоидного разъёма. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | менее 120 Ом | 2А |
| **Заменить горящий клапан соленоидом**См. процедуру[[96-007-076 — Burn Solenoid\|007-076]]. | 3А |  |

### ШАГ 2. Проверьте проводную упряжку CentinelTM.

#### ШАГ 2A. Осмотрите проводную упряжку CentinelTM и разъёмы модуля управления CentinelTM.

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разъема или разъема разъема разъема или разъема разъема разъема или на разъеме разъема повреждения изоляции Проволоки Разъемная оболочка разорвана Поврежденная блокировка вкладки разъема. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2В |
| **Починить поврежденные контакты** Починить или заменить проводную упряжку CentinelTM или модуль управления CentinelTM, в зависимости от того, какие контакты повреждены. Ремонт проводной упряжки CentinelTM. См. процедуру 019-202. Замените проводную упряжку CentinelTM. См. процедуру 019-131. Заменить модуль управления CentinelTM. См. процедуру 019-130. | 3А |  |

#### ШАГ 2B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините соленоид горящего клапана от проводной упряжки CentinelTM. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. Отключите реле питания от проводной ремни CentinelTM (только двигатели большой мощности). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Тяжелая работа: Измерить сопротивление от контакта 4 реле питания разъёма, проводов ремня стороны, до контакта А ожогового клапана соленоидной, проводов ремня стороны. Тяжелая работа: Измерьте сопротивление от контакта 12 разъёма проводов CentinelTM с контактом В с соленоидным клапаном, проводкой с жгутом проводов. Высокая мощность: Измерьте сопротивление от контакта 21 разъёма проводов CentinelTM к контакту А с соленоидным клапаном, стороной проводов. Высокая мощность: Измерьте сопротивление от контакта 25 разъёма проводов CentinelTM с контактом В с соленоидным клапаном, проводкой с жгутом проводов. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 2C |
| **Заменить проводную упряжку CentinelTM**См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3А |  |

#### ШАГ 2C. Проверьте короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините соленоид горящего клапана от проводной упряжки CentinelTM. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. Отключите реле питания от проводной ремни CentinelTM (только двигатели большой мощности). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Тяжелая работа: Измерьте сопротивление между контактом 12 и контактом 2 разъёма проводов CentinelTM. Высокая мощность: Измерить сопротивление между контактом 21 и контактом 22 разъёма проводов CentinelTM. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 1к Ом | 2D |
| **Заменить проводную упряжку CentinelTM**См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3А |  |

#### ШАГ 2D. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от соленоида горящего клапана. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. Отключите реле питания от проводной ремни CentinelTM (только двигатели большой мощности). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Тяжелая работа: Измерить сопротивление от контакта 12 проводов разъема упряжки CentinelTM ко всем соседним штифтам в разъеме, исключая контакты 1 и 11. Высокая мощность: Измерить сопротивление от контакта 21 проводов разъема упряжки CentinelTM ко всем соседним штифтам в разъеме, исключая контакты 1, 20, 22 и 23. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 1к Ом | 3А |
| **Заменить проводную упряжку CentinelTM**См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3А |  |

### ШАГ 3. Сбросьте коды неисправностей.

#### ШАГ 3A. Отключите код неисправности.

| **Условия: **Соедините все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Цикл питания. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте плагин службы для проверки вывода. Убедитесь, что код 223 неактивен. | Код ошибки 223 неактивен | Полный комплект |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и проверены снова. | 1А |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 223
>
> ### Burn Valve Solenoid Circuit - Open Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 223 PID(P): SPN: FMI: Lamp: Red SRT: | Burn Valve Solenoid Circuit - Open Circuit. The burn solenoid is open. | The Centinel™ system will **not** operate. |
>
> ### Circuit Description
>
> The burn valve solenoid controls the flow of oil in the oil control valve during the burn cycle.
>
> ### Component Location
>
> The burn valve solenoid is located on top of the oil control valve.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To avoid pin and harness damage, use the following test leads when taking measurements: Male Cannon, Metri-Pack, and Deutsch test lead, Part Number 3822758 Female AMP, Metri-Pack, and Deutsch test lead, Part Number 3822917 Male Deutsch test lead, Part Number 3823993 Female Deutsch test lead, Part Number 3823994 Male Weather-Pack test lead, Part Number 3823995 Female Weather-Pack test lead, Part Number 3823996.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the burn valve solenoid. |  |
> |  | **STEP 1A.** Verify the burn valve solenoid is connected to the Centinel™ harness. | Solenoid is connected |
> |  | **STEP 1B.** Inspect the burn valve solenoid and Centinel™ harness connectors. | No damaged pins |
> |  | **STEP 1C.** Check the Centinel™ control module burn valve solenoid supply voltage. | Battery voltage |
> |  | **STEP 1D.** Check the burn valve solenoid for an open. | Less than 120 ohms |
> | STEP 2. | Check the Centinel™ harness. |  |
> |  | **STEP 2A.** Inspect the Centinel™ harness and the Centinel™ control module connectors. | No damaged pins |
> |  | **STEP 2B.** Check for an open circuit. | Less than 10 ohms |
> |  | **STEP 2C.** Check for a short circuit to ground. | More than 1k ohms |
> |  | **STEP 2D.** Check for a short circuit from pin to pin. | More than 1k ohms |
> | STEP 3. | Clear the fault codes. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 223 inactive |
>
> ### STEP 1. Check the burn valve solenoid.
>
> #### STEP 1A. Verify the burn valve solenoid is connected to the Centinel™ harness.
>
> | **Conditions:** Turn the keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[96-007-076 — Burn Solenoid\|007-076]]. | Solenoid is connected | 1B |
> | **Connect the solenoid to the Centinel™ wiring harness** | 3A |  |
>
> #### STEP 1B. Inspect the burn valve solenoid and the Centinel™ harness connector.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the burn valve solenoid. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 1C |
> | **Repair the damaged pins** Repair or replace the Centinel™ harness or the burn valve solenoid, whichever has damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the burn valve solenoid. Refer to Procedure 007-076. Install the appropriate connector seal if damaged or missing. | 3A |  |
>
> #### STEP 1C. Check the Centinel™ control module burn valve solenoid supply voltage.
>
> | **Conditions:** Start the engine. Enter the service mode. Refer to Procedure 007-999. Disconnect the burn valve solenoid from the Centinel™ harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the supply voltage from pin A to pin B on the harness side of the burn valve solenoid within 15 seconds of entering the service mode. Refer to the wiring diagram for connector pin identification. | Approximately = normal battery voltage within 15 seconds after entering the service mode. | 1D |
> | **Replace the Centinel™ control module or wiring harness** Replace the Centinel™ control module. Refer to Procedure 019-130. Replace the Centinel™ wiring harness. Refer to Procedure 019-131. | 3A |  |
>
> #### STEP 1D. Check the burn valve solenoid for an open.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the burn valve solenoid from the Centinel™ harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin A to pin B of the burn valve solenoid connector. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 120 ohms | 2A |
> | **Replace the burn valve solenoid** Refer to Procedure [[96-007-076 — Burn Solenoid\|007-076]]. | 3A |  |
>
> ### STEP 2. Check the Centinel™ harness.
>
> #### STEP 2A. Inspect the Centinel™ wiring harness and Centinel™ control module connectors.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the Centinel™ control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
> | **Repair the damaged pins** Repair or replace the Centinel™ wiring harness or the Centinel™ control module, whichever has the damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the Centinel™ control module. Refer to Procedure 019-130. | 3A |  |
>
> #### STEP 2B. Check for an open circuit.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the burn valve solenoid from the Centinel™ harness. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty engines only). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Heavy-duty: Measure the resistance from pin 4 of the power relay connector, harness side, to pin A of the burn valve solenoid, harness side. Heavy-duty: Measure the resistance from pin 12 of the Centinel™ harness connector to pin B of the burn valve solenoid, harness side. High-horsepower: Measure the resistance from pin 21 of the Centinel™ harness connector to pin A of the burn valve solenoid, harness side. High-horsepower: Measure the resistance from pin 25 of the Centinel™ harness connector to pin B of the burn valve solenoid, harness side. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 2C |
> | **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |
>
> #### STEP 2C. Check for a short circuit to ground.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the burn valve solenoid from the Centinel™ harness. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty engines only). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Heavy-duty: Measure the resistance between pin 12 and pin 2 of the Centinel™ harness connector. High-horsepower: Measure the resistance between pin 21 and pin 22 of the Centinel™ harness connector. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 2D |
> | **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |
>
> #### STEP 2D. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the burn valve solenoid. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty engines only). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Heavy-duty: Measure the resistance from pin 12 of the Centinel™ harness connector to all adjacent pins in the connector, excluding pins 1 and 11. High-horsepower: Measure the resistance from pin 21 of the Centinel™ harness connector to all adjacent pins in the connector, excluding pins 1, 20, 22, and 23. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 3A |
> | **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |
>
> ### STEP 3. Clear the fault codes.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all the components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Cycle power. Start the engine and let it idle for 1 minute. Use the service plug to check output. Verify that Fault Code 223 is inactive. | Fault Code 223 inactive | Complete |
> | Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
