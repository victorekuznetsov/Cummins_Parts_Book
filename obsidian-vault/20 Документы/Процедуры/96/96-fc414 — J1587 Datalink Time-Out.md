---
aliases:
  - "Тайм-аут шины данных J1587"
type: "Процедура"
doc: "96-fc414"
title_en: "J1587 Datalink Time-Out"
title_ru: "Тайм-аут шины данных J1587"
modified: "2004-02-25"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc414.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc414.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# J1587 Datalink Time-Out
**Тайм-аут шины данных J1587**

> [!abstract] Процедура · `96-fc414`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc414.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc414.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 414

### Тайм-аут шины данных J1587

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 414 PID(P): СПН: ФМИ: Лампа: СТО: | Тайм-аут шины данных J1587. Данные были получены модулем управления CentinelTM в течение указанного времени. | Система CentinelTM будет **не** следить за динамикой двигателя и может **не** работать. |

![[19803802.png]]

### Описание цепи

Шина данных J1587 CAN обеспечивает связь между электронным модулем управления двигателем (ECM) и модулем управления CentinelTM. Это позволяет системе CentinelTM контролировать динамику двигателя. Используя эти данные, система CentinelTM способна функционировать в пределах заданных параметров.

### Расположение компонента

### Практические замечания

Прежде чем приступить к работе с этим кодом неисправности, убедитесь, что разъем проводной жгуты проводов CentinelTM надежно подключен к шине данных J1587 CAN.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

** Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерений: Испытательный щуп Male Cannon, Merti-Pack и Deutsch, Испытательный щуп Part Number 3822758 Female AMP, Metri-Pack и Deutsch, Испытательный щуп Part Number 3822917 Male Deutsch, Испытательный щуп Part Number 3823993 Female Deutsch, Часть Number 3823994.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте шину данных CAN. |  |
|  | **STEP 1A.** Проверить разъем шины данных CAN. | Никаких поврежденных контактов |
| ШАГ 2. | Проверьте проводную упряжку CentinelTM. |  |
|  | **ШАГ 2А.** Проверка на наличие реверсивных проводов. | Пин А: 4 VDC; Pin B: 1 VDC |
|  | **STEP 2B.** Проверить контакты разъема модуля управления CentinelTM. | Никаких поврежденных контактов |
|  | **ШАГ 2С.** Проверить короткое замыкание. | Более 1к Ом |
| ШАГ 3. | Очистите код ошибки. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код 414 неактивен |

### ШАГ 1. Проверьте шину данных.

#### ШАГ 1A. Проверить разъем шины данных CAN.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разъема разъема разъема разъема разъема или разъема разъема разъема или разъема разъема разъема или на разъеме разъема повреждения изоляции Проволоки Разъемная оболочка разорвана Поврежденная блокировка вкладки разъема. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2А |
| ** Ремонт поврежденных контактов** Ремонт или замена разъема шины данных CAN управления. См. процедуру[[99-019-207 — Deutsch HD10 Connector Series\|019-207]]или[[99-019-203 — AMP Connector Series\|019-203]]. | 3А |  |

### ШАГ 2. Проверьте проводную упряжку CentinelTM.

#### ШАГ 2A. Проверьте обратные провода.

| **Условия:** Включить переключатель зажигания. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте напряжение от контакта 8 на стороне проводов ремня управления разъемом модуля CentinelTM для контакта 2. Измерьте напряжение от контакта 9 на стороне проводов ремня управления разъемом модуля CentinelTM для контакта 2. См. схему проводов для идентификации контакта с разъемом. | Контакт 8: Контакт 2: 4 VDC; контакт 9 - контакт 2: Примерно 1 VDC | 2В |
| ** Если напряжения противоположны спецификации, переверните провода** | 3А |  |

#### ШАГ 2B. Осмотрите проводную упряжку CentinelTM и разъёмы модуля управления CentinelTM.

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разъема разъема разъема разъема разъема или разъема разъема разъема или разъема разъема разъема или на разъеме разъема повреждения изоляции Проволоки Разъемная оболочка разорвана Поврежденная блокировка вкладки разъема. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2C |
| ** Починить поврежденные контакты** Починить или заменить проводную упряжку CentinelTM или модуль управления CentinelTM, в зависимости от того, какие контакты повреждены. Ремонт проводной упряжки CentinelTM. См. процедуру 019-202. Замените проводную упряжку CentinelTM. См. процедуру 019-131. Заменить модуль управления CentinelTM. См. процедуру 019-130. | 3А |  |

#### ШАГ 2C. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. Отсоедините проводную упряжку CentinelTM от цепи шины данных CAN. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте сопротивление от контакта 8 разъема модуля CentinelTM со всеми другими штифтами. Измерить сопротивление от контакта 9 разъема модуля CentinelTM со всеми другими штифтами. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 1к Ом | 3А |
| **Заменить модуль управления CentinelTM**См. процедуру[[96-019-130-tr — Centinel™ Control Module\|019-130]]. | 3А |  |

### ШАГ 3. Очистите код ошибки.

#### ШАГ 3A. Отключите код неисправности.

| **Условия: ** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить, что код 414 неактивен. | Код 414 неактивен | Полный комплект |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и перепроверены. | 1А |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 414
>
> ### J1587 Datalink Time-Out
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 414 PID(P): SPN: FMI: Lamp: SRT: | J1587 Datalink Time-Out. The data was **not** received by the Centinel™ control module within the specified time. | The Centinel™ system will **not** monitor engine dynamics and can **not** operate. |
>
> ### Circuit Description
>
> The J1587 datalink provides communications capability between the parent engine electronic control module (ECM) and the Centinel™ control module. This allows the Centinel™ system the ability to monitor engine dynamics. Using these data, the Centinel™ system is able to function within the specified parameters.
>
> ### Component Location
>
> ### Shoptalk
>
> Before proceeding with this fault code, make certain that the Centinel™ wiring harness connector is securely connected to the J1587 datalink.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To avoid pin and harness damage, use the following test leads when taking measurements: Male Cannon, Merti-Pack, and Deutsch test lead, Part Number 3822758 Female AMP, Metri-Pack, and Deutsch test lead, Part Number 3822917 Male Deutsch test lead, Part Number 3823993 Female Deutsch test lead, Part Number 3823994.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the datalink. |  |
> |  | **STEP 1A.** Inspect datalink connector. | No damaged pins |
> | STEP 2. | Check the Centinel™ wiring harness. |  |
> |  | **STEP 2A.** Check for reversed wires. | Pin A: 4 VDC; Pin B: 1 VDC |
> |  | **STEP 2B.** Inspect Centinel™ control module connector pins. | No damaged pins |
> |  | **STEP 2C.** Check for short circuit. | More than 1k ohms |
> | STEP 3. | Clear the fault code. |  |
> |  | **STEP 3A.** Disable fault code. | Fault Code 414 inactive |
>
> ### STEP 1. Check data link.
>
> #### STEP 1A. Inspect datalink connector.
>
> | **Conditions:** Turn the keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2A |
> | **Repair damaged pins** Repair or replace the control datalink connector. Refer to Procedure [[99-019-207 — Deutsch HD10 Connector Series\|019-207]] or [[99-019-203 — AMP Connector Series\|019-203]]. | 3A |  |
>
> ### STEP 2. Check the Centinel™ wiring harness.
>
> #### STEP 2A. Check for reversed wires.
>
> | **Conditions:** Turn the keyswitch ON. Disconnect the Centinel™ wiring harness from the Centinel™ control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin 8 on the harness side of the Centinel™ control module connector to pin 2. Measure the voltage from pin 9 on the harness side of the Centinel™ control module connector to pin 2. Refer to the wiring diagram for connector pin identification. | Pin 8 to pin 2: Approximately 4 VDC; Pin 9 to pin 2: Approximately 1 VDC | 2B |
> | **If voltages are opposite of specification, reverse the wires** | 3A |  |
>
> #### STEP 2B. Inspect the Centinel™ wiring harness and Centinel™ control module connectors.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ wiring harness from the Centinel™ control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2C |
> | **Repair the damaged pins** Repair or replace the Centinel™ wiring harness or Centinel™ control module, whichever has the damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the Centinel™ control module. Refer to Procedure 019-130. | 3A |  |
>
> #### STEP 2C. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ wiring harness from the Centinel™ control module. Disconnect the Centinel™ wiring harness from the datalink circuit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 8 of the Centinel™ module connector to all other pins. Measure the resistance from pin 9 of the Centinel™ module connector to all other pins. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 3A |
> | **Replace the Centinel™ control module** Refer to Procedure [[96-019-130-tr — Centinel™ Control Module\|019-130]]. | 3A |  |
>
> ### STEP 3. Clear the fault code.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify Fault Code 414 is inactive. | Fault Code 414 inactive | Complete |
> | Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and rechecked. | 1A |  |
