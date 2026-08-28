---
aliases:
  - "Цепь диагностической лампы — короткое замыкание"
type: "Процедура"
doc: "96-fc199"
title_en: "Diagnostic Lamp Circuit - Short Circuit"
title_ru: "Цепь диагностической лампы — короткое замыкание"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc199.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc199.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# Diagnostic Lamp Circuit - Short Circuit
**Цепь диагностической лампы — короткое замыкание**

> [!abstract] Процедура · `96-fc199`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-03-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc199.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc199.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 199

### Цепь диагностической лампы — короткое замыкание

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 199 PID(P): СПН: ФМИ: Лампа: СТО: | Цепь диагностической лампы — короткое замыкание. Диагностическая лампа закорочена. | Статус системы CentinelTM или показания к неисправности не будут отображаться должным образом. |

![[05800060.png]]

### Описание цепи

Модуль управления CentinelTM постоянно контролирует эксплуатационные параметры системы. Статус системы отображается с помощью диагностических ламп. Существуют две диагностические лампы CentinelTM. Они зеленого и красного цвета. Зеленая лампа включает свет, указывающий, что эксплуатационные параметры системы находятся в пределах установленных допусков для сверхмощных **только**. Для высокой мощности зеленый свет указывает на то, что система имеет мощность. Красная лампа освещает, чтобы указать, что системный параметр не имеет указанных допусков.

### Расположение компонента

Тяжеловесные двигатели: Диагностические лампы расположены на модуле управления CentinelTM, расположенном на масляном баке макияжа.

Высокомощные двигатели: Диагностические лампы расположены на диагностическом фонарном сборе на масляном макияже.

### Практические замечания

Процедуры ремонта для тяжелых работ не существует. Модуль *** должен быть заменен. Следующая процедура относится к высокопроизводительным **только. Убедитесь, что напряжение высокопроизводительной диагностической лампы соответствует приложению.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерений: Гнездовой AMP, Metri-Pack и Deutsch, номер детали 3822917.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте диагностические лампы. |  |
|  | **STEP 1A.** Проверить диагностические лампы и разъёмы электропроводки CentinelTM (только с высокой мощностью). | Никаких поврежденных контактов |
|  | **ШАГ 1В.** Проверьте наличие открытых диагностических ламп. | Менее 2 м ом |
|  | **СТЭП 1С** Проверить диагностические лампы на короткое время. | Более 10 Ом |
| ШАГ 2. | Проверьте проводную упряжку CentinelTM. |  |
|  | **STEP 2A.** Осмотрите жгут проводов CentinelTM и разъемы модуля управления CentinelTM. | Никаких поврежденных контактов |
|  | **ШАГ 2В.** Проверить наличие открытой цепи. | Менее 10 Ом |
|  | **ШАГ 2С.** Проверить короткое замыкание на землю. | Более 1к Ом |
|  | **STEP 2D.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 1к Ом |
| ШАГ 3. | Сбросьте коды неисправностей. |  |
|  | **СТЭП 3А** Соедините все компоненты. | Коды ошибок 198 неактивные |

### ШАГ 1. Проверьте диагностические лампы.

#### ШАГ 1A. Осмотрите диагностические лампы и разъёмы проводной упряжки CentinelTM (только с высокой мощностью).

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от диагностического лампового агрегата для высокопроизводительных систем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разъема или разъема разъема разъема или разъема разъема разъема или на разъеме разъема повреждения изоляции Проволоки Разъемная оболочка разорвана Поврежденная блокировка вкладки разъема. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 1В |
| **Починить поврежденные контакты** Починить или заменить проводную упряжку CentinelTM или диагностический узел лампы, в зависимости от того, какие контакты повреждены. Ремонт проводной упряжки CentinelTM. См. процедуру 019-202. Замените проводную упряжку CentinelTM. См. процедуру 019-131. Заменить диагностический ламповый сбор. См. процедуру 007-999. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. | 3А |  |

#### ШАГ 1B. Проверьте диагностический ламповый сбор для открытого.

| **Условия:** Выключите замок зажигания. Отсоедините диагностический ламповый узел от проводной упряжки CentinelTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Высокая мощность: Измерить сопротивление от контакта А до контакта D на диагностическом разъёме лампы для цепи зеленой лампы и от контакта D до контакта В для цепи красной лампы. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 2 м ом | 1С |
| **Заменить диагностический ламповый сборщик** См. процедуру[[96-007-999 — Lubricating Oil System - Overview\|007-999]]. | 3А |  |

#### ШАГ 1C. Проверьте диагностический ламповый сбор на короткое время.

| **Условия:** Выключите замок зажигания. Отсоедините диагностический ламповый узел от проводной упряжки CentinelTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Высокая мощность: Измерить сопротивление от контакта А до контакта D на диагностическом разъёме лампы для цепи зеленой лампы и от контакта D до контакта В для цепи красной лампы. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 10 Ом | 2А |
| **Заменить диагностический ламповый сборщик** См. процедуру[[96-007-999 — Lubricating Oil System - Overview\|007-999]]. | 3А |  |

### ШАГ 2. Проверьте высокопроизводительную проводную упряжку CentinelTM.

#### ШАГ 2A. Осмотрите проводную упряжку CentinelTM и разъёмы модуля управления CentinelTM.

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разъема или разъема разъема разъема или разъема разъема разъема или на разъеме разъема повреждения изоляции Проволоки Разъемная оболочка разорвана Поврежденная блокировка вкладки разъема. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2В |
| **Починить поврежденные контакты** Починить или заменить проводную упряжку CentinelTM или модуль управления CentinelTM, в зависимости от того, какие контакты повреждены. Ремонт проводной упряжки CentinelTM. См. процедуру 019-202. Замените проводную упряжку CentinelTM. См. процедуру 019-131. Заменить модуль управления CentinelTM. См. процедуру 019-130. | 3А |  |

#### ШАГ 2B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините диагностический ламповый узел от проводной упряжки CentinelTM. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. Отключите реле питания от проводной ремни CentinelTM (только для тяжелых приложений). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Высокая мощность: Измерить сопротивление от контакта 1 проводов разъема упряжки CentinelTM до контакта А диагностического лампового узла, проводов упряжки борта. Высокая мощность: Измерить сопротивление от контакта 25 проводов разъема упряжки CentinelTM до контакта В диагностического лампового узла, проводов упряжки борта. Высокая мощность: Измерить сопротивление от контакта 22 проводов разъема упряжки CentinelTM до контакта С диагностического лампового узла, проводов упряжки борта. Высокая мощность: Измерить сопротивление от контакта 10 проводов разъема упряжки CentinelTM до контакта D диагностического лампового узла, проводов упряжки борта. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 2C |
| **Заменить проводную упряжку CentinelTM**См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3А |  |

#### ШАГ 2C. Проверьте короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините диагностический ламповый узел от проводной упряжки CentinelTM. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. Отключите реле питания от проводной ремни CentinelTM (только для тяжелых приложений). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Высокая мощность: Измерьте сопротивление от контакта 1 разъёма проводов CentinelTM к контакту 25. Высокая мощность: Измерьте сопротивление от контакта 22 разъёма проводов CentinelTM к контакту 25. Высокая мощность: Измерьте сопротивление от контакта 10 разъёма проводов CentinelTM к контакту 22. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 1к Ом | 2D |
| **Заменить электропроводку CentinelTM или модуль управления CentinelTM** Заменить электропроводку CentinelTM. См. процедуру 019-131. Заменить модуль управления CentinelTM. См. процедуру 019-130. | 3А |  |

#### ШАГ 2D. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от диагностического лампового узла. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. Отключите реле питания от проводной ремни CentinelTM (только двигатели большой мощности). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Высокая мощность: Измерьте сопротивление контактов 1, 10, 22 и 25 разъёма проводов CentinelTM со всеми другими штифтами в разъеме. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 1к Ом | 3А |
| **Заменить электропроводку CentinelTM или модуль управления CentinelTM** Заменить электропроводку CentinelTM. См. процедуру 019-131. Заменить модуль управления CentinelTM. См. процедуру 019-130. | 3А |  |

### ШАГ 3. Сбросьте коды неисправностей.

#### ШАГ 3A. Отключите код неисправности.

| **Условия:** Соедините все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Убедитесь, что код 199 неактивен. | Код ошибки 198 неактивен | Полный комплект |
| **Заменить модуль управления CentinelTM, если коды неисправностей активны**[[96-019-130-tr — Centinel™ Control Module\|019-130]]. | Полный. |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 199
>
> ### Diagnostic Lamp Circuit - Short Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 199 PID(P): SPN: FMI: Lamp: SRT: | Diagnostic Lamp Circuit - Short Circuit. The diagnostic lamp is shorted out. | Centinel™ system status or fault indications will **not** be properly displayed. |
>
> ### Circuit Description
>
> The Centinel™ control module constantly monitors the operational parameters of the system. The status of the system is displayed by means of diagnostic lamps. There are two Centinel™ diagnostic lamps. They are green and red in color. The green lamp illuminates to indicate that the system's operational parameters are within specified tolerances for heavy-duty **only**. For high-horsepower, the green light indicates the system has power. The red lamp illuminates to indicate that a system parameter is out of specified tolerances.
>
> ### Component Location
>
> Heavy-duty engines: The diagnostic lamps are located on the Centinel™ control module, located on the make up oil tank.
>
> High-horsepower engines: The diagnostic lamps are located on the diagnostic lamp assembly on the oil make-up tank.
>
> ### Shoptalk
>
> There is no repair procedure for the heavy-duty. The module **must** be replaced. The following procedure pertains to high-horsepower **only**. Be certain the voltage of the high-horsepower diagnostic lamp assembly matches the application.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To avoid pin and harness damage, use the following test lead when taking measurements: Female AMP, Metri-Pack and Deutsch test lead, Part Number 3822917.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the diagnostic lamps. |  |
> |  | **STEP 1A.** Inspect the diagnostic lamps and Centinel™ harness connectors (high-horsepower only.) | No damaged pins |
> |  | **STEP 1B.** Check the diagnostic lamps for an open. | Less than 2M ohms |
> |  | **STEP 1C.** Check the diagnostic lamps for a short. | More than 10 ohms |
> | STEP 2. | Check the Centinel™ harness. |  |
> |  | **STEP 2A.** Inspect the Centinel™ harness and the Centinel™ control module connectors. | No damaged pins |
> |  | **STEP 2B.** Check for an open circuit. | Less than 10 ohms |
> |  | **STEP 2C.** Check for a short circuit to ground. | More than 1k ohms |
> |  | **STEP 2D.** Check for a short circuit from pin to pin. | More than 1k ohms |
> | STEP 3. | Clear the fault codes. |  |
> |  | **STEP 3A.** Connect all the components. | Fault Codes 198 inactive |
>
> ### STEP 1. Check the diagnostic lamps.
>
> #### STEP 1A. Inspect the diagnostic lamps and Centinel™ harness connectors (high-horsepower only.)
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the diagnostic lamp assembly for high-horsepower systems. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 1B |
> | **Repair the damaged pins** Repair or replace the Centinel™ wiring harness or the diagnostic lamp assembly, whichever has damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the diagnostic lamp assembly. Refer to Procedure 007-999. Install the appropriate connector seal if damaged or missing. | 3A |  |
>
> #### STEP 1B. Check the diagnostic lamp assembly for an open.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the diagnostic lamp assembly from the Centinel™ harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | High-horsepower: Measure the resistance from pin A to pin D on the diagnostic lamp assembly connector for the green lamp circuit and from pin D to pin B for the red lamp circuit. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 2M ohms | 1C |
> | **Replace the diagnostic lamp assembly** Refer to Procedure [[96-007-999 — Lubricating Oil System - Overview\|007-999]]. | 3A |  |
>
> #### STEP 1C. Check the diagnostic lamp assembly for a short.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the diagnostic lamp assembly from the Centinel™ harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | High-horsepower: Measure the resistance from pin A to pin D on the diagnostic lamp assembly connector for the green lamp circuit and from pin D to pin B for the red lamp circuit. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 10 ohms | 2A |
> | **Replace the diagnostic lamp assembly** Refer to Procedure [[96-007-999 — Lubricating Oil System - Overview\|007-999]]. | 3A |  |
>
> ### STEP 2. Check the high-horsepower Centinel™ harness.
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
> | **Conditions:** Turn the keyswitch OFF. Disconnect the diagnostic lamp assembly from the Centinel™ harness. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty applications only). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | High-horsepower: Measure the resistance from pin 1 of the Centinel™ harness connector to pin A of the diagnostic lamp assembly, harness side. High-horsepower: Measure the resistance from pin 25 of the Centinel™ harness connector to pin B of the diagnostic lamp assembly, harness side. High-horsepower: Measure the resistance from pin 22 of the Centinel™ harness connector to pin C of the diagnostic lamp assembly, harness side. High-horsepower: Measure the resistance from pin 10 of the Centinel™ harness connector to pin D of the diagnostic lamp assembly, harness side. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 2C |
> | **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |
>
> #### STEP 2C. Check for a short circuit to ground.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the diagnostic lamp assembly from the Centinel™ harness. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty applications only). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | High-horsepower: Measure the resistance from pin 1 of the Centinel™ harness connector to pin 25. High-horsepower: Measure the resistance from pin 22 of the Centinel™ harness connector to pin 25. High-horsepower: Measure the resistance from pin 10 of the Centinel™ harness connector to pin 22. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 2D |
> | **Replace the Centinel™ harness or Centinel™ control module** Replace the Centinel™ wiring harness. Refer to Procedure 019-131. Replace the Centinel™ control module. Refer to Procedure 019-130. | 3A |  |
>
> #### STEP 2D. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the diagnostic lamp assembly. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty engines only). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | High-horsepower: Measure the resistance from pins 1, 10, 22, and 25 of the Centinel™ harness connector to all other pins in the connector. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 3A |
> | **Replace the Centinel™ harness or Centinel™ control module** Replace the Centinel™ wiring harness. Refer to Procedure 019-131. Replace the Centinel™ control module. Refer to Procedure 019-130. | 3A |  |
>
> ### STEP 3. Clear the fault codes.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all the components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Start the engine and let it idle for 1 minute. Verify that Fault Code 199 is inactive. | Fault Code 198 inactive | Complete |
> | **Replace the Centinel™ control module if the fault codes are active** Refer to Procedure [[96-019-130-tr — Centinel™ Control Module\|019-130]]. | Complete. |  |
