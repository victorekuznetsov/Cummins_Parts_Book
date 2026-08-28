---
aliases:
  - "Цепь электромагнита клапана подпитки — обрыв"
type: "Процедура"
doc: "96-fc225"
title_en: "Make-up Valve Solenoid Circuit - Open Circuit"
title_ru: "Цепь электромагнита клапана подпитки — обрыв"
modified: "2004-03-03"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc225.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc225.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# Make-up Valve Solenoid Circuit - Open Circuit
**Цепь электромагнита клапана подпитки — обрыв**

> [!abstract] Процедура · `96-fc225`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-03-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc225.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc225.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 225

### Цепь электромагнита клапана подпитки — обрыв

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 225 P(P): СПН: ФМИ: Лампа: Красная СТО: | Цепь электромагнита клапана подпитки — обрыв. Соленоид макияжа открыт. | Система CentinelTM будет работать **не**. |

![[07800054.png]]

### Описание цепи

Соленоид макияжного клапана контролирует поток масла в клапане управления маслом во время цикла макияжа.

### Расположение компонента

Соленоид макияжного клапана расположен поверх клапана управления маслом. Это клапан, который питается моторным маслом шунтирующей трубки.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерений: Испытательный щуп Male Cannon, Metri-Pack и Deutsch, Испытательный щуп Part Number 3822758 Female AMP, Metri-Pack и Deutsch, Испытательный щуп Part Number 3822917 Male Deutsch, Испытательный щуп Part Number 3823993 Female Deutsch, Испытательный щуп Part Number 3823994 Male Weather-Pack, Часть Number 3823995 Гнездовой испытательный щуп Weather-Pack, Часть Number 3823996.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте соленоидный клапан макияжа. |  |
|  | **STEP 1A.** Проверить, подключен ли соленоид к проводной упряжке CentinelTM. | Соленоид связан |
|  | **STEP 1B.** Осмотрите разъемы для монтажа соленоидных клапанов и проводных ремней CentinelTM. | Никаких поврежденных контактов |
|  | **STEP 1C.** Проверьте напряжение питания соленоида в модуле управления CentinelTM. | Напряжение аккумулятора |
|  | **STEP 1D.** Проверьте наличие соленоида в косметологическом клапане на наличие открытого. | менее 120 Ом |
| ШАГ 2. | Проверьте проводную упряжку CentinelTM. |  |
|  | **STEP 2A.** Осмотрите жгут проводов CentinelTM и разъемы модуля управления CentinelTM. | Никаких поврежденных контактов |
|  | **ШАГ 2В.** Проверить наличие открытой цепи. | Менее 10 Ом |
|  | **ШАГ 2С.** Проверить короткое замыкание на землю. | Более 1к Ом |
|  | **STEP 2D.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 1к Ом |
| ШАГ 3. | Сбросьте коды неисправностей. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код ошибки 225 неактивен |

### ШАГ 1. Проверьте соленоидный клапан макияжа.

#### ШАГ 1A. Проверьте, что соленоид клапана косметики подключен к проводах CentinelTM.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[96-007-077 — Make-Up Solenoid\|007-077]]. | Соленоид связан | 1В |
| **Подключите соленоид к электропроводке CentinelTM** | 3А |  |

#### ШАГ 1B. Осмотрите визажный клапан соленоида и разъём проводов CentinelTM.

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от соленоида макияжного клапана. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разъема или разъема разъема разъема или разъема разъема разъема или на разъеме разъема повреждения изоляции Проволоки Разъемная оболочка разорвана Поврежденная блокировка вкладки разъема. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 1С |
| **Починить поврежденные контакты** Починить или заменить проводную упряжку CentinelTM или соленоид визажного клапана, в зависимости от того, какие контакты повреждены. Ремонт проводной упряжки CentinelTM. См. процедуру 019-202. Замените проводную упряжку CentinelTM. См. процедуру 019-131. Замените косметологический клапан соленоидом. См. процедуру 007-077. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. | 3А |  |

#### ШАГ 1C. Проверьте напряжение питания соленоида в модуле управления CentinelTM.

| **Условия:** Запустить двигатель. Введите режим обслуживания. См. 007-999. Отсоедините соленоид визажного клапана от проводной упряжки CentinelTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение питания от контакта А до контакта В на стороне проводов ремня косметики соленоида в течение 15 секунд после входа в режим обслуживания. См. схему проводов для идентификации контакта с разъемом. | Приблизительно = нормальное напряжение батареи через 15 секунд после входа в режим работы. | 1D |
| **Заменить модуль управления CentinelTM или проводную упряжку CentinelTM** Заменить модуль управления CentinelTM. См. процедуру 019-130. Замените проводную упряжку CentinelTM. См. процедуру 019-131. | 3А |  |

#### ШАГ 1D. Проверьте косметологический клапан соленоида на наличие открытого.

| **Условия:** Выключите замок зажигания. Отсоедините соленоид визажного клапана от проводной упряжки CentinelTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта А до контакта В косметологического клапана соленоидного разъёма. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | менее 120 Ом | 2А |
| **Заменить косметологический клапан соленоидом**См. процедуру[[96-007-077 — Make-Up Solenoid\|007-077]]. | 3А |  |

### ШАГ 2. Проверьте проводную упряжку CentinelTM.

#### ШАГ 2A. Осмотрите проводную упряжку CentinelTM и разъёмы модуля управления CentinelTM.

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разъема или разъема разъема разъема или разъема разъема разъема или на разъеме разъема повреждения изоляции Проволоки Разъемная оболочка разорвана Поврежденная блокировка вкладки разъема. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2В |
| **Починить поврежденные контакты** Починить или заменить проводную упряжку CentinelTM или модуль управления CentinelTM, в зависимости от того, какие контакты повреждены. Ремонт проводной упряжки CentinelTM. См. процедуру 019-202. Замените проводную упряжку CentinelTM. См. процедуру 019-131. Заменить модуль управления CentinelTM. См. процедуру 019-130. | 3А |  |

#### ШАГ 2B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините соленоид визажного клапана от проводной упряжки CentinelTM. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. Отключите реле питания от проводной ремни CentinelTM (только двигатели большой мощности). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Тяжелая работа: Измерить сопротивление от контакта 4 разъёма реле питания, проводов упряжки стороны, до контакта А косметики клапана соленоидной, проводов упряжки стороны. Тяжелая работа: Измерьте сопротивление от контакта 11 разъёма проводов CentinelTM к контакту В косметологической клапанной соленоидной стороны проводов. Высокая мощность: Измерьте сопротивление от контакта 20 разъёма проводов CentinelTM к контакту А соленоидного клапана макияжа, стороны проводов ремня. Высокая мощность: Измерьте сопротивление от контакта 25 разъёма проводов CentinelTM с контактом В косметологической клапанной соленоидной стороны проводов. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 2C |
| **Заменить проводную упряжку CentinelTM**См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3А |  |

#### ШАГ 2C. Проверьте короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините соленоид визажного клапана от проводной упряжки CentinelTM. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. Отключите реле питания от проводной ремни CentinelTM (только двигатели большой мощности). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Тяжелая работа: Измерьте сопротивление между контактом 11 и контактом 2 разъёма проводов CentinelTM. Высокая мощность: Измерьте сопротивление между контактами 20 и 22 разъёма проводной ремни CentinelTM. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 1к Ом | 3А |
| **Заменить проводную упряжку CentinelTM**См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3А |  |

#### ШАГ 2D. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от соленоида макияжного клапана. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. Отключите реле питания от проводной ремни CentinelTM (только двигатели большой мощности). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Тяжелая работа: Измерить сопротивление от контакта 11 проводов разъема упряжки CentinelTM ко всем соседним штифтам в разъеме, исключая контакты 1 и 12. Высокая мощность: Измерить сопротивление от контакта 20 проводов разъема упряжки CentinelTM со всеми смежными штифтами в разъеме, исключая контакты 1, 21, 22 и 23. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 1к Ом | 3А |
| **Заменить проводную упряжку CentinelTM**См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3А |  |

### ШАГ 3. Сбросьте коды неисправностей.

#### ШАГ 3A. Отключите код неисправности.

| **Условия:** Соедините все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Цикл питания. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте сервисный плагин для проверки вывода. Убедитесь, что код 225 неактивен. | Код ошибки 225 неактивен | Полный комплект |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и проверены снова. | 1А |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 225
>
> ### Make-up Valve Solenoid Circuit - Open Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 225 PID(P): SPN: FMI: Lamp: Red SRT: | Make-up Valve Solenoid Circuit - Open Circuit. The make-up solenoid is open. | The Centinel™ system will **not** operate. |
>
> ### Circuit Description
>
> The make-up valve solenoid controls the flow of oil within the oil control valve during the make-up cycle.
>
> ### Component Location
>
> The make-up valve solenoid is located on top of the oil control valve. It is the valve that is fed by the lubricating oil bypass tube.
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
> | STEP 1. | Check the make-up valve solenoid. |  |
> |  | **STEP 1A.** Verify the make-up valve solenoid is connected to the Centinel™ harness. | Solenoid is connected |
> |  | **STEP 1B.** Inspect the make-up valve solenoid and Centinel™ harness connectors. | No damaged pins |
> |  | **STEP 1C.** Check the Centinel™ control module make-up valve solenoid supply voltage. | Battery voltage |
> |  | **STEP 1D.** Check the make-up valve solenoid for an open. | Less than 120 ohms |
> | STEP 2. | Check the Centinel™ harness. |  |
> |  | **STEP 2A.** Inspect the Centinel™ harness and the Centinel™ control module connectors. | No damaged pins |
> |  | **STEP 2B.** Check for an open circuit. | Less than 10 ohms |
> |  | **STEP 2C.** Check for a short circuit to ground. | More than 1k ohms |
> |  | **STEP 2D.** Check for a short circuit from pin to pin. | More than 1k ohms |
> | STEP 3. | Clear the fault codes. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 225 inactive |
>
> ### STEP 1. Check the make-up valve solenoid.
>
> #### STEP 1A. Verify the make-up valve solenoid is connected to the Centinel™ harness.
>
> | **Conditions:** Turn the keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[96-007-077 — Make-Up Solenoid\|007-077]]. | Solenoid is connected | 1B |
> | **Connect the solenoid to the Centinel™ wiring harness** | 3A |  |
>
> #### STEP 1B. Inspect the make-up valve solenoid and the Centinel™ harness connector.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the make-up valve solenoid. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 1C |
> | **Repair the damaged pins** Repair or replace the Centinel™ harness or the make-up valve solenoid, whichever has damaged pins. Repair the Centinel™ wiring harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the make-up valve solenoid. Refer to Procedure 007-077. Install the appropriate connector seal if damaged or missing. | 3A |  |
>
> #### STEP 1C. Check the Centinel™ control module make-up valve solenoid supply voltage.
>
> | **Conditions:** Start the engine. Enter the service mode. Refer to 007-999. Disconnect the make-up valve solenoid from the Centinel™ harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the supply voltage from pin A to pin B on the harness side of the make-up valve solenoid within 15 seconds of entering the service mode. Refer to the wiring diagram for connector pin identification. | Approximately = normal battery voltage 15 seconds after entering the service mode. | 1D |
> | **Replace the Centinel™ control module or Centinel™ harness** Replace the Centinel™ control module. Refer to Procedure 019-130. Replace the Centinel™ harness. Refer to Procedure 019-131. | 3A |  |
>
> #### STEP 1D. Check the make-up valve solenoid for an open.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the make-up valve solenoid from the Centinel™ harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin A to pin B of the make-up valve solenoid connector. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 120 ohms | 2A |
> | **Replace the make-up valve solenoid** Refer to Procedure [[96-007-077 — Make-Up Solenoid\|007-077]]. | 3A |  |
>
> ### STEP 2. Check the Centinel™ harness.
>
> #### STEP 2A. Inspect the Centinel™ harness and Centinel™ control module connectors.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the Centinel™ control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
> | **Repair the damaged pins** Repair or replace the Centinel™ wiring harness or the Centinel™ control module, whichever has the damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the Centinel™ control module. Refer to Procedure 019-130. | 3A |  |
>
> #### STEP 2B. Check for an open circuit.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the make-up valve solenoid from the Centinel™ harness. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty engines only). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Heavy-duty: Measure the resistance from pin 4 of the power relay connector, harness side, to pin A of the make-up valve solenoid, harness side. Heavy-duty: Measure the resistance from pin 11 of the Centinel™ harness connector to pin B of the make-up valve solenoid, harness side. High-horsepower: Measure the resistance from pin 20 of the Centinel™ harness connector to pin A of the make-up valve solenoid, harness side. High-horsepower: Measure the resistance from pin 25 of the Centinel™ harness connector to pin B of the make-up valve solenoid, harness side. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 2C |
> | **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |
>
> #### STEP 2C. Check for a short circuit to ground.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the make-up valve solenoid from the Centinel™ harness. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty engines only). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Heavy-duty: Measure the resistance between pin 11 and pin 2 of Centinel™ harness connector. High-horsepower: Measure the resistance between pin 20 and 22 of the Centinel™ harness connector. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 3A |
> | **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |
>
> #### STEP 2D. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the make-up valve solenoid. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty engines only). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Heavy-duty: Measure the resistance from pin 11 of the Centinel™ harness connector to all adjacent pins in the connector, excluding pins 1 and 12. High-horsepower: Measure the resistance from pin 20 of the Centinel™ harness connector to all adjacent pins in the connector, excluding pins 1, 21, 22, and 23. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 3A |
> | **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |
>
> ### STEP 3. Clear the fault codes.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all the components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Cycle power. Start the engine and let it idle for 1 minute. Use a service plug to check output. Verify that Fault Code 225 is inactive. | Fault Code 225 inactive | Complete |
> | Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
